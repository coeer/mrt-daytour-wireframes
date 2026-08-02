"""Verify the published Furano editorial pages and their large WebP assets."""

from urllib.request import Request, urlopen


BASE = "https://coeer.github.io/mrt-daytour-wireframes/furano"
PAGES = {
    "zh": f"{BASE}/index.html?v=4",
    "kr": f"{BASE}/wireframe_kr.html?v=4",
    "bi": f"{BASE}/bilingual.html?v=4",
}
REQUIRED = (
    "20260729-v4",
    "hero-farm-tomita-1600.webp",
    'id="itinerary"',
    'id="faq"',
)
BANNED = (
    "spec-bar",
    "设计建议",
    "한국어 기사",
    "司机会韩语",
    "카카오톡 한국어 상담",
    "KakaoTalk韩语咨询",
)
IMAGE_URLS = tuple(
    f"{BASE}/img/{name}-1600.webp?v=4"
    for name in (
        "hero-farm-tomita",
        "furano-people",
        "shikisai",
        "blue-pond",
        "shirahige",
    )
)


def fetch(url: str):
    """Return an HTTP response for *url* with a descriptive user agent."""
    request = Request(url, headers={"User-Agent": "Furano-v4-publication-verifier/1.0"})
    return urlopen(request, timeout=30)


def verify_page(label: str, url: str) -> None:
    """Require one published page to have the expected status and markers."""
    with fetch(url) as response:
        if response.status != 200:
            raise AssertionError(f"{label}: expected HTTP 200, got {response.status}")
        html = response.read().decode("utf-8")

    missing = tuple(marker for marker in REQUIRED if marker not in html)
    present = tuple(marker for marker in BANNED if marker in html)
    if missing:
        raise AssertionError(f"{label}: missing required markers: {missing!r}")
    if present:
        raise AssertionError(f"{label}: found banned markers: {present!r}")
    print(f"PASS page {label}: HTTP 200, required markers present, banned markers absent")


def verify_image(url: str) -> None:
    """Require one published large image to be an HTTP 200 WebP response."""
    with fetch(url) as response:
        if response.status != 200:
            raise AssertionError(f"{url}: expected HTTP 200, got {response.status}")
        content_type = response.headers.get_content_type()
        if content_type != "image/webp":
            raise AssertionError(f"{url}: expected image/webp, got {content_type!r}")
        response.read(1)
    print(f"PASS image {url}: HTTP 200, Content-Type image/webp")


def main() -> None:
    """Verify all three pages and five large image assets."""
    for label, url in PAGES.items():
        verify_page(label, url)
    for url in IMAGE_URLS:
        verify_image(url)


if __name__ == "__main__":
    main()
