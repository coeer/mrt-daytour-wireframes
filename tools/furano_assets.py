"""Download, validate, and optimize the licensed Furano editorial images."""

from __future__ import annotations

import argparse
import io
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Final
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen

from PIL import Image, ImageOps


USER_AGENT: Final = "FuranoEditorialAssetBuilder/1.0 (licensed-image-processing)"
REQUEST_ATTEMPTS: Final = 4


@dataclass(frozen=True)
class AssetSpec:
    key: str
    creator: str
    source_page: str
    download_url: str
    license_id: str
    license_url: str
    source_width: int
    source_height: int
    widths: tuple[int, ...]
    web_aspect_ratio: float | None = None


ASSETS = (
    AssetSpec(
        key="hero-farm-tomita",
        creator="Natsuko Aoyama",
        source_page="https://www.pexels.com/photo/8797283/",
        download_url="https://images.pexels.com/photos/8797283/pexels-photo-8797283.jpeg?cs=srgb&fm=jpg",
        license_id="Pexels",
        license_url="https://www.pexels.com/license/",
        source_width=4032,
        source_height=3024,
        widths=(1600, 960),
    ),
    AssetSpec(
        key="furano-people",
        creator="Cindy Bissig",
        source_page="https://unsplash.com/photos/KzAiQAFcfIc",
        download_url="https://images.unsplash.com/photo-1626911635167-0b3006fbda39?auto=format&fit=max&fm=jpg&q=90&w=4000",
        license_id="Unsplash",
        license_url="https://unsplash.com/license",
        source_width=4000,
        source_height=2667,
        widths=(1600, 960),
        web_aspect_ratio=2.0,
    ),
    AssetSpec(
        key="shikisai",
        creator="663highland",
        source_page="https://commons.wikimedia.org/wiki/File:140726_Shikisai-no-oka_Biei_Hokkaido_Japan01n.jpg",
        download_url="https://upload.wikimedia.org/wikipedia/commons/a/a2/140726_Shikisai-no-oka_Biei_Hokkaido_Japan01n.jpg",
        license_id="CC-BY-2.5",
        license_url="https://creativecommons.org/licenses/by/2.5/",
        source_width=6000,
        source_height=4000,
        widths=(1600, 960),
    ),
    AssetSpec(
        key="blue-pond",
        creator="AndyLeungHK",
        source_page="https://commons.wikimedia.org/wiki/File:Shirogane_Blue_Pond,_Biei,_Hokkaido_Japan.jpg",
        download_url="https://upload.wikimedia.org/wikipedia/commons/d/d5/Shirogane_Blue_Pond%2C_Biei%2C_Hokkaido_Japan.jpg",
        license_id="CC0-1.0",
        license_url="https://creativecommons.org/publicdomain/zero/1.0/",
        source_width=6000,
        source_height=4000,
        widths=(1600, 960),
    ),
    AssetSpec(
        key="shirahige",
        creator="OKJaguar",
        source_page="https://commons.wikimedia.org/wiki/File:Shirahige_Falls,_Biei_River,_Hokkaido,_Japan.jpg",
        download_url="https://upload.wikimedia.org/wikipedia/commons/e/e1/Shirahige_Falls%2C_Biei_River%2C_Hokkaido%2C_Japan.jpg",
        license_id="CC-BY-SA-4.0",
        license_url="https://creativecommons.org/licenses/by-sa/4.0/",
        source_width=6000,
        source_height=4000,
        widths=(1600, 960),
    ),
    AssetSpec(
        key="lavender-softserve",
        creator="Douglas Perkins",
        source_page="https://commons.wikimedia.org/wiki/File:Lavender_soft_serve_at_Farm_Tomita.jpg",
        download_url="https://upload.wikimedia.org/wikipedia/commons/3/3e/Lavender_soft_serve_at_Farm_Tomita.jpg",
        license_id="CC-BY-4.0",
        license_url="https://creativecommons.org/licenses/by/4.0/",
        source_width=4000,
        source_height=3000,
        widths=(1200, 720),
    ),
)


def _commons_redirect_url(url: str) -> str | None:
    """Return the stable Commons original-file redirect for an upload URL."""
    parsed = urlparse(url)
    if parsed.netloc != "upload.wikimedia.org":
        return None
    filename = unquote(parsed.path.rsplit("/", 1)[-1])
    return f"https://commons.wikimedia.org/wiki/Special:Redirect/file/{quote(filename)}"


def _download(url: str) -> bytes:
    """Fetch an original with backoff and a Commons redirect recovery path."""
    active_url = url
    for attempt in range(REQUEST_ATTEMPTS):
        try:
            request = Request(active_url, headers={"User-Agent": USER_AGENT})
            with urlopen(request, timeout=45) as response:
                return response.read()
        except HTTPError as error:
            fallback = _commons_redirect_url(active_url)
            if error.code == 429 and fallback and active_url != fallback:
                active_url = fallback
                continue
            if error.code not in {429, 500, 502, 503, 504} or attempt == REQUEST_ATTEMPTS - 1:
                raise
        except URLError:
            if attempt == REQUEST_ATTEMPTS - 1:
                raise
        time.sleep(2**attempt)
    raise RuntimeError(f"Unable to download {url}")


def decoded_dimensions_are_usable(asset: AssetSpec, size: tuple[int, int]) -> bool:
    """Require a decoded source to be high-resolution and fit every requested width."""
    return max(size) >= 2400 and min(size) > 0 and max(size) >= max(asset.widths)


def _source_image(asset: AssetSpec) -> Image.Image:
    data = _download(asset.download_url)
    with Image.open(io.BytesIO(data)) as original:
        original.load()
        if not decoded_dimensions_are_usable(asset, original.size):
            raise ValueError(
                f"{asset.key}: decoded source is too small for the requested derivatives: "
                f"{original.width}x{original.height}"
            )
        return ImageOps.exif_transpose(original).convert("RGB")


def _derivative_name(asset: AssetSpec, width: int) -> str:
    return f"{asset.key}-{width}.webp"


def _crop_for_web(image: Image.Image, asset: AssetSpec) -> Image.Image:
    if asset.web_aspect_ratio is None:
        return image
    crop_height = round(image.width / asset.web_aspect_ratio)
    if crop_height >= image.height:
        return image
    return image.crop((0, 0, image.width, crop_height))


def _save_derivative(image: Image.Image, destination: Path, width: int) -> None:
    height = round(image.height * width / image.width)
    resized = image.resize((width, height), Image.Resampling.LANCZOS)
    resized.save(destination, "WEBP", quality=84, method=6)


def render_sources_markdown() -> str:
    lines = [
        "# Furano editorial image sources",
        "",
        "All derivatives are real photographs, downloaded from the linked source pages and "
        "cropped/resized for web. No destination, visitor, vehicle, certificate, review, "
        "rating, price, inventory, or urgency imagery has been fabricated.",
        "",
    ]
    for asset in ASSETS:
        lines.extend(
            (
                f"## {asset.key}",
                "",
                f"- Creator: {asset.creator}",
                f"- Source page: {asset.source_page}",
                f"- Original download: {asset.download_url}",
                f"- Original dimensions: {asset.source_width}×{asset.source_height}px",
                f"- License: {asset.license_id} — {asset.license_url}",
                "- Modification: cropped/resized for web and encoded as WebP.",
                "",
            )
        )
    return "\n".join(lines)


def build_assets(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for asset in ASSETS:
        image = _crop_for_web(_source_image(asset), asset)
        for width in asset.widths:
            _save_derivative(image, output_dir / _derivative_name(asset, width), width)
        print(f"Validated {asset.key}; wrote {len(asset.widths)} WebP derivatives.")
    (output_dir / "SOURCES.md").write_text(render_sources_markdown(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Directory for WebP derivatives")
    args = parser.parse_args()
    build_assets(args.output)


if __name__ == "__main__":
    main()
