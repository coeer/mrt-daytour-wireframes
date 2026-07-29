# Furano Editorial Detail Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Furano v3 wireframe with three reproducible, photo-led, production-quality static detail pages while preserving the approved itinerary and FAQ facts.

**Architecture:** Keep all Korean/Chinese product content and immutable facts in `tools/build_furano.py`, preserving the established single-source workflow. Delegate only licensed asset acquisition and HTML component rendering to imported helper modules. Generate the Chinese, Korean, and bilingual HTML files through that one build entry point; use responsive `<picture>` assets and semantic native HTML so the final pages need no framework or runtime dependency.

**Tech Stack:** Python 3 standard library, Pillow for deterministic image resizing, static HTML/CSS, native `<details>` FAQ, inline SVG route diagram, `unittest`, GitHub Pages.

## Global Constraints

- Only modify `furano/`, `tools/`, `tests/`, and the plan/spec documents created for this feature; do not modify Fuji or other destination directories.
- FAQ and itinerary facts must remain aligned with `furano/bilingual.html` at baseline commit `8eff922` and the approved design spec.
- Every displayed itinerary time must include `예정` in Korean and `预计` in Chinese.
- Cancellation remains: 100% refund through 3 days before departure; no refund from 2 days before through the travel day; failed group formation receives a full refund.
- Drivers speak Japanese/English and use a translation app; never claim the driver speaks Korean.
- Never add “KakaoTalk Korean-language consultation”; the existing list of contact messenger options may remain.
- Use only real photographs with source long edge at least 2400px and a commercial-use license; do not generate or fake destination, visitor, vehicle, certificate, review, rating, price, inventory, or urgency imagery/data.
- Korean and Chinese single-language pages must share component order and visual tokens; the bilingual page must place Korean on the left and Chinese on the right at widths above 880px and stack Korean above Chinese at or below 880px.
- Use warm white `#F7F5F0`, white `#FFFFFF`, lavender `#7C5DAA`, pale lavender `#E9E0F3`, flower pink `#D96B87`, pond blue `#2D7F9D`, CTA berry `#B7445F`, body `#202329`, and secondary text `#62666D`.
- Main text contrast must meet WCAG AA 4.5:1; interactive targets must be at least 44px high.
- The largest visual is the Farm Tomita hero; do not create a second equally dominant visual peak.
- Use static HTML/CSS with no application framework; FAQ uses native `<details>` and animations respect `prefers-reduced-motion`.
- All three pages include no-cache meta tags and asset query version `20260729-v4`.
- Generate all three HTML files from the same `tools/build_furano.py`; never hand-edit generated HTML.
- The first child of every generated `<body>` must be the same auditable direction contract comment with the seed key `88bbc100`, the pinned Korean select-shop editorial direction, and the exact Impeccable FINISH sentence.
- Preserve the canonical local workflow by copying the reviewed `tools/build_furano.py` plus its imported modules to `C:\Users\38185\ZCodeProject\` only after final review.
- Push each reviewed task commit to the remote feature branch; publish to `main` only after the whole-feature review passes.

## File Structure

- `tools/furano_assets.py`: exact licensed source manifest, downloads, metadata validation, WebP derivatives, and `SOURCES.md`.
- `tools/furano_renderer.py`: semantic page components, CSS, inline SVG route graphic, and three render modes.
- `tools/build_furano.py`: sole language-content source and command-line orchestrator that writes all generated deliverables.
- `tests/test_furano_content.py`: factual and language-redline tests.
- `tests/test_furano_assets.py`: license, source dimensions, derivative dimensions, and file-size tests.
- `tests/test_furano_render.py`: structure, accessibility, bilingual order, and generated-file tests.
- `tests/verify_furano_remote.py`: post-publish HTTP verification.
- `furano/img/*.webp`: generated desktop and mobile image derivatives.
- `furano/img/SOURCES.md`: generated attribution and licensing manifest.

---

### Task 1: Freeze the approved bilingual content model

**Files:**
- Create: `tools/build_furano.py`
- Create: `tests/test_furano_content.py`
- Reference only: `furano/bilingual.html`
- Reference only: `C:\Users\38185\ZCodeProject\build_furano.py`

**Interfaces:**
- Produces: `ASSET_VERSION: str`, `KR: dict[str, object]`, `ZH: dict[str, object]`, `ITINERARY_KEYS: tuple[str, ...]`, `FAQ_COUNT: int`.
- Consumers: Tasks 3 and 4 import these names without redefining product copy.

- [ ] **Step 1: Write the failing content contract tests**

Create `tests/test_furano_content.py` with tests that import `tools.build_furano` and assert the approved facts:

```python
import unittest

from tools.build_furano import ASSET_VERSION, FAQ_COUNT, ITINERARY_KEYS, KR, ZH


class ContentContractTests(unittest.TestCase):
    def test_version_and_counts(self):
        self.assertEqual(ASSET_VERSION, "20260729-v4")
        self.assertEqual(FAQ_COUNT, 8)
        self.assertEqual(
            ITINERARY_KEYS,
            (
                "sapporo_depart",
                "farm_tomita",
                "roller_coaster_road",
                "shikisai_no_oka",
                "free_lunch",
                "blue_pond",
                "shirahige_falls",
                "sapporo_return",
            ),
        )

    def test_product_facts_are_preserved(self):
        self.assertEqual(KR["pickup_radius_km"], 3)
        self.assertEqual(ZH["pickup_radius_km"], 3)
        self.assertEqual(KR["minimum_departure"], 4)
        self.assertEqual(ZH["minimum_departure"], 4)
        self.assertEqual(KR["included_ticket"], "사계채의 언덕 입장권")
        self.assertEqual(ZH["included_ticket"], "四季彩之丘门票")
        self.assertIn("미성사", KR["refund_summary"])
        self.assertIn("不成团", ZH["refund_summary"])

    def test_itinerary_times_are_explicitly_estimated(self):
        for item in KR["itinerary"]:
            self.assertIn("예정", item["time"])
        for item in ZH["itinerary"]:
            self.assertIn("预计", item["time"])

    def test_language_redlines(self):
        korean_blob = repr(KR)
        chinese_blob = repr(ZH)
        self.assertNotIn("한국어 기사", korean_blob)
        self.assertNotIn("카카오톡 한국어 상담", korean_blob)
        self.assertNotIn("司机会韩语", chinese_blob)
        self.assertNotIn("KakaoTalk韩语咨询", chinese_blob)
        self.assertIn("일본어·영어", korean_blob)
        self.assertIn("日语/英语", chinese_blob)
```

- [ ] **Step 2: Run the content tests and confirm the missing module failure**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_content -v
```

Expected: FAIL because `tools.build_furano` does not exist.

- [ ] **Step 3: Implement the immutable content module**

Create `tools/build_furano.py` with:

```python
ASSET_VERSION = "20260729-v4"
ITINERARY_KEYS = (
    "sapporo_depart",
    "farm_tomita",
    "roller_coaster_road",
    "shikisai_no_oka",
    "free_lunch",
    "blue_pond",
    "shirahige_falls",
    "sapporo_return",
)
FAQ_COUNT = 8
```

Copy the complete `KR` and `ZH` dictionaries from the canonical v3 generator, retaining all eight itinerary entries and all eight FAQ answers. Add the normalized keys tested above (`pickup_radius_km`, `minimum_departure`, `included_ticket`, `refund_summary`) without deleting the original display copy. Do not define product copy in any other Python file.

- [ ] **Step 4: Run the content contract**

Run the command from Step 2.

Expected: all tests PASS.

- [ ] **Step 5: Commit**

```powershell
git add tools/build_furano.py tests/test_furano_content.py
git commit -m "feat: freeze Furano bilingual content model"
```

---

### Task 2: Acquire and optimize licensed high-resolution imagery

**Files:**
- Create: `tools/furano_assets.py`
- Create: `tests/test_furano_assets.py`
- Create: `furano/img/SOURCES.md`
- Create: `furano/img/hero-farm-tomita-1600.webp`
- Create: `furano/img/hero-farm-tomita-960.webp`
- Create: `furano/img/furano-people-1600.webp`
- Create: `furano/img/furano-people-960.webp`
- Create: `furano/img/shikisai-1600.webp`
- Create: `furano/img/shikisai-960.webp`
- Create: `furano/img/blue-pond-1600.webp`
- Create: `furano/img/blue-pond-960.webp`
- Create: `furano/img/shirahige-1600.webp`
- Create: `furano/img/shirahige-960.webp`
- Create: `furano/img/lavender-softserve-1200.webp`
- Create: `furano/img/lavender-softserve-720.webp`

**Interfaces:**
- Produces: `ASSETS: tuple[AssetSpec, ...]`, `build_assets(output_dir: Path) -> None`, `render_sources_markdown() -> str`.
- Consumers: Task 3 uses the output filenames verbatim in `<picture>` elements.

- [ ] **Step 1: Write the failing asset manifest tests**

Create `tests/test_furano_assets.py`:

```python
import unittest
from pathlib import Path

from PIL import Image

from tools.furano_assets import ASSETS, render_sources_markdown


class AssetContractTests(unittest.TestCase):
    def test_all_sources_meet_resolution_and_license_rules(self):
        self.assertEqual(len(ASSETS), 6)
        for asset in ASSETS:
            self.assertGreaterEqual(max(asset.source_width, asset.source_height), 2400)
            self.assertIn(
                asset.license_id,
                {
                    "Pexels",
                    "Unsplash",
                    "CC-BY-2.5",
                    "CC0-1.0",
                    "CC-BY-SA-4.0",
                    "CC-BY-4.0",
                },
            )
            self.assertTrue(asset.creator)
            self.assertTrue(asset.source_page.startswith("https://"))
            self.assertTrue(asset.download_url.startswith("https://"))

    def test_sources_markdown_names_every_creator(self):
        markdown = render_sources_markdown()
        for asset in ASSETS:
            self.assertIn(asset.creator, markdown)
            self.assertIn(asset.source_page, markdown)
            self.assertIn(asset.license_url, markdown)

    def test_generated_derivatives_are_webp_and_bounded(self):
        image_dir = Path("furano/img")
        expected = {
            "hero-farm-tomita-1600.webp": 1600,
            "hero-farm-tomita-960.webp": 960,
            "furano-people-1600.webp": 1600,
            "furano-people-960.webp": 960,
            "shikisai-1600.webp": 1600,
            "shikisai-960.webp": 960,
            "blue-pond-1600.webp": 1600,
            "blue-pond-960.webp": 960,
            "shirahige-1600.webp": 1600,
            "shirahige-960.webp": 960,
            "lavender-softserve-1200.webp": 1200,
            "lavender-softserve-720.webp": 720,
        }
        for name, width in expected.items():
            path = image_dir / name
            self.assertTrue(path.exists(), name)
            self.assertLess(path.stat().st_size, 650_000, name)
            with Image.open(path) as image:
                self.assertEqual(image.format, "WEBP")
                self.assertEqual(image.width, width)
```

- [ ] **Step 2: Run the asset tests and confirm the missing module failure**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_assets -v
```

Expected: FAIL because `tools.furano_assets` does not exist.

- [ ] **Step 3: Implement the exact asset manifest**

Define a frozen `AssetSpec` dataclass and the six entries below in `tools/furano_assets.py`:

```python
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
```

Download with a descriptive user agent, verify the decoded original dimensions meet each manifest entry, apply EXIF orientation, convert to RGB, resize with `Image.Resampling.LANCZOS`, and save WebP at quality 84 with method 6. Write attribution details and a “cropped/resized for web” modification note to `SOURCES.md`.

- [ ] **Step 4: Build assets and run the tests**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/furano_assets.py --output furano/img
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_assets -v
```

Expected: six source entries validated, twelve WebP files written, all tests PASS.

- [ ] **Step 5: Visually inspect the six 1600/1200px derivatives**

Open each large derivative and reject any file that is visibly soft, incorrectly rotated, color-banded, or poorly cropped. The accepted hero must show the Farm Tomita sign, lavender field, blue sky, and mountain line; the people image must visibly show two travelers for scale.

- [ ] **Step 6: Commit**

```powershell
git add tools/furano_assets.py tests/test_furano_assets.py furano/img
git commit -m "feat: add licensed Furano image system"
```

---

### Task 3: Build the Korean and Chinese editorial pages

**Files:**
- Create: `tools/furano_renderer.py`
- Modify: `tools/build_furano.py`
- Create: `tests/test_furano_render.py`
- Modify generated: `furano/index.html`
- Modify generated: `furano/wireframe_kr.html`

**Interfaces:**
- Consumes: `KR`, `ZH`, and `ASSET_VERSION` defined in `tools/build_furano.py`; exact asset filenames from Task 2.
- Produces: `render_single(content: dict[str, object], lang: str) -> str`, `build_all(output_dir: Path) -> dict[str, str]`.
- Consumer: Task 4 adds `render_bilingual` to the same renderer and build mapping.

- [ ] **Step 1: Write the failing single-page render tests**

Add to `tests/test_furano_render.py`:

```python
import tempfile
import unittest
from pathlib import Path

from tools.build_furano import KR, ZH, build_all
from tools.furano_renderer import render_single


class RenderContractTests(unittest.TestCase):
    def test_single_pages_have_required_sections_and_no_wireframe_meta(self):
        for lang, content in (("ko", KR), ("zh-CN", ZH)):
            html = render_single(content, lang)
            self.assertIn(f'<html lang="{lang}">', html)
            for section_id in (
                "top",
                "benefits",
                "pickup",
                "itinerary",
                "included",
                "cancellation",
                "faq",
                "closing",
            ):
                self.assertIn(f'id="{section_id}"', html)
            self.assertNotIn("spec-bar", html)
            self.assertNotIn("设计建议", html)
            self.assertIn("20260729-v4", html)

    def test_single_pages_use_responsive_real_photos(self):
        html = render_single(KR, "ko")
        self.assertGreaterEqual(html.count("<picture"), 6)
        self.assertIn("hero-farm-tomita-1600.webp", html)
        self.assertIn("furano-people-1600.webp", html)
        self.assertIn("shikisai-1600.webp", html)
        self.assertIn("blue-pond-1600.webp", html)
        self.assertIn("shirahige-1600.webp", html)
        self.assertIn('loading="lazy"', html)
        self.assertIn('fetchpriority="high"', html)

    def test_build_writes_single_language_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            written = build_all(output_dir)
            self.assertEqual(written["zh"], "index.html")
            self.assertEqual(written["kr"], "wireframe_kr.html")
            self.assertTrue((output_dir / "index.html").exists())
            self.assertTrue((output_dir / "wireframe_kr.html").exists())
```

- [ ] **Step 2: Run the render tests and confirm the missing renderer failure**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render -v
```

Expected: FAIL because the renderer and build orchestrator do not exist.

- [ ] **Step 3: Implement the shared design tokens and page shell**

In `tools/furano_renderer.py`, define `TOKENS` with the exact global colors, a `picture(key, alt, *, hero=False)` helper that emits 960/1600 WebP sources and explicit width/height attributes, and a `document(title, lang, body)` helper with:

```html
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Use Pretendard first for Korean and a CJK system fallback for Chinese. Add a visible “skip to content” link, semantic `<main>`, and `scroll-behavior: smooth` only outside reduced-motion mode.

Make this comment the first child of `<body>` in all outputs:

```html
<!--
THESIS: A Furano day tour reads like a Korean select-shop travel issue, not a card-heavy booking template.
OWN-WORLD: Warm white editorial fields, disciplined black type, lavender/fuchsia route accents, decisive real photography, and timeline-led geometry.
STORY: See the landscape, understand the travel effort and safeguards, then inspect the full itinerary or continue to booking.
FIRST VIEWPORT: Farm Tomita fills the frame; compact Korean or Chinese copy sits low-left, with itinerary and pickup actions above the next-section reveal.
FORM: Photo-led travel issue; pinned direction overrides the seed assignment; seed 88bbc100.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->
```

- [ ] **Step 4: Implement the approved section sequence**

Implement `render_single` in this exact order:

1. `hero`: Farm Tomita full-bleed picture, title, “three colors” subtitle, itinerary and pickup anchor buttons.
2. `benefits`: pickup radius, four-person small group, included ticket, group-failure refund.
3. `pain-solution`: one short traditional-bus pain statement plus the real people-scale image.
4. `pickup`: estimated 08:00 anchor, pickup rules, and an inline SVG route diagram.
5. `itinerary`: eight items in the approved order; Farm Tomita is the only `data-peak="true"` item; Roller Coaster Road uses a styled window/route graphic instead of an unlicensed photo; lunch uses the licensed soft-serve detail photo only as a “free choice” visual aside, not as an included meal claim.
6. `included`: included/not-included lists, vehicle allocation, Japanese/English driver and translation app.
7. `cancellation`: the two cancellation bands, group-formation refund, bad-weather refund.
8. `faq`: eight native `<details>` items, first item `open`.
9. `closing`: quiet Blue Pond crop, three guarantees, itinerary and top anchors.
10. attribution footer linking `img/SOURCES.md`.

- [ ] **Step 5: Implement the build orchestrator**

Extend `tools/build_furano.py`, keeping `ASSET_VERSION`, `KR`, `ZH`, `ITINERARY_KEYS`, and `FAQ_COUNT` in this file, and expose:

```python
from pathlib import Path


def build_all(output_dir: Path) -> dict[str, str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "zh": ("index.html", render_single(ZH, "zh-CN")),
        "kr": ("wireframe_kr.html", render_single(KR, "ko")),
    }
    for _, (filename, html) in outputs.items():
        (output_dir / filename).write_text(html, encoding="utf-8")
    return {key: filename for key, (filename, _) in outputs.items()}
```

The CLI default output is `<repo>/furano`.

- [ ] **Step 6: Build and run all current tests**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/build_furano.py
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests -v
```

Expected: both single pages generated and all tests PASS.

- [ ] **Step 7: Commit**

```powershell
git add tools/furano_renderer.py tools/build_furano.py tests/test_furano_render.py furano/index.html furano/wireframe_kr.html
git commit -m "feat: redesign Furano single-language pages"
```

---

### Task 4: Add the bilingual review page and responsive accessibility checks

**Files:**
- Modify: `tools/furano_renderer.py`
- Modify: `tools/build_furano.py`
- Modify: `tests/test_furano_render.py`
- Modify generated: `furano/bilingual.html`

**Interfaces:**
- Consumes: Task 3 section renderers and shared picture helper.
- Produces: `render_bilingual(kr: dict[str, object], zh: dict[str, object]) -> str`; `build_all` returns the additional mapping `"bi": "bilingual.html"`.

- [ ] **Step 1: Write the failing bilingual and accessibility tests**

Add:

```python
from tools.furano_renderer import render_bilingual


class RenderContractTests(unittest.TestCase):
    # Keep the Task 3 methods above in this same class.

    def test_bilingual_language_order_and_shared_images(self):
        html = render_bilingual(KR, ZH)
        self.assertIn('class="language-column language-column--kr"', html)
        self.assertIn('class="language-column language-column--zh"', html)
        self.assertLess(html.index("language-column--kr"), html.index("language-column--zh"))
        self.assertEqual(html.count("hero-farm-tomita-1600.webp"), 1)
        self.assertIn("@media (max-width: 880px)", html)
        self.assertIn("grid-template-columns: 1fr", html)

    def test_faq_and_motion_are_accessible(self):
        for html in (
            render_single(KR, "ko"),
            render_single(ZH, "zh-CN"),
            render_bilingual(KR, ZH),
        ):
            self.assertEqual(html.count("<details"), 8)
            self.assertIn("<summary", html)
            self.assertIn("prefers-reduced-motion: reduce", html)
            self.assertIn("min-height: 44px", html)
            self.assertIn('class="skip-link"', html)

    def test_build_writes_all_three_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            written = build_all(Path(temp_dir))
            self.assertEqual(
                written,
                {
                    "zh": "index.html",
                    "kr": "wireframe_kr.html",
                    "bi": "bilingual.html",
                },
            )
```

- [ ] **Step 2: Run the render tests and confirm the bilingual failure**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render -v
```

Expected: FAIL because `render_bilingual` and the third build mapping are missing.

- [ ] **Step 3: Implement bilingual section composition**

Each content section must render one shared photo or illustration followed by:

```html
<div class="language-grid">
  <section class="language-column language-column--kr" lang="ko">…</section>
  <section class="language-column language-column--zh" lang="zh-CN">…</section>
</div>
```

Use a 40px desktop gap, a subtle right divider on the Korean column, and at `max-width: 880px` switch to a single column with Korean first and a bottom divider. Do not force sentence-by-sentence row alignment.

- [ ] **Step 4: Add the bilingual build target and regenerate all pages**

Update `build_all` with:

```python
"bi": ("bilingual.html", render_bilingual(KR, ZH))
```

Run the builder, then the full test suite.

Expected: all three generated files exist and all tests PASS.

- [ ] **Step 5: Run static content parity checks**

Run:

```powershell
rg -n "예정|预计|미성사|不成团|일본어·영어|日语/英语" furano/index.html furano/wireframe_kr.html furano/bilingual.html
rg -n "한국어 기사|카카오톡 한국어 상담|司机会韩语|KakaoTalk韩语咨询|spec-bar|设计建议" furano/index.html furano/wireframe_kr.html furano/bilingual.html
```

Expected: the first command finds the approved phrases; the second command has zero matches.

- [ ] **Step 6: Commit**

```powershell
git add tools/furano_renderer.py tools/build_furano.py tests/test_furano_render.py furano
git commit -m "feat: add responsive Furano bilingual page"
```

---

### Task 5: Complete visual QA, canonical sync, and remote publication

**Files:**
- Create at finish: `DESIGN.md`
- Create at finish: `DESIGN.sidecar.json` if required by the documenter
- Create: `tests/verify_furano_remote.py`
- Modify if findings require it: `tools/furano_renderer.py`
- Regenerate after fixes: `furano/index.html`
- Regenerate after fixes: `furano/wireframe_kr.html`
- Regenerate after fixes: `furano/bilingual.html`
- Copy after review: `C:\Users\38185\ZCodeProject\build_furano.py`
- Copy after review: `C:\Users\38185\ZCodeProject\furano_assets.py`
- Copy after review: `C:\Users\38185\ZCodeProject\furano_renderer.py`

**Interfaces:**
- Consumes: all generated Task 4 outputs.
- Produces: verified remote pages at the existing three GitHub Pages URLs with `?v=4`.

- [ ] **Step 1: Write the remote verifier**

Create `tests/verify_furano_remote.py` using `urllib.request` with:

```python
BASE = "https://coeer.github.io/mrt-daytour-wireframes/furano"
PAGES = {
    "zh": f"{BASE}/index.html?v=4",
    "kr": f"{BASE}/wireframe_kr.html?v=4",
    "bi": f"{BASE}/bilingual.html?v=4",
}
REQUIRED = ("20260729-v4", "hero-farm-tomita-1600.webp", "id=\"itinerary\"", "id=\"faq\"")
BANNED = ("spec-bar", "设计建议", "한국어 기사", "司机会韩语")
```

For each page, require HTTP 200, every `REQUIRED` marker, and no `BANNED` marker. Also fetch the five `-1600.webp` files and require HTTP 200 plus `Content-Type: image/webp`.

- [ ] **Step 2: Run fresh local correctness tests**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/build_furano.py
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 3: Perform desktop and mobile visual review**

Serve the repository locally and inspect all three pages at:

- 1280×900 desktop.
- 390×844 mobile.
- `prefers-reduced-motion: reduce`.

For each page verify:

- No horizontal scrolling.
- Hero copy remains readable over the image.
- The next section peeks above the initial fold.
- No three consecutive screens have the same density.
- Farm Tomita remains the only dominant visual peak.
- FAQ summaries are keyboard reachable and open with Enter/Space.
- Every button is at least 44px high.
- Korean does not clip or wrap one character per line.
- Bilingual layout is side-by-side above 880px and Korean-first stacked below it.

- [ ] **Step 4: Run the Impeccable mechanical detector once**

Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' 'C:\Users\38185\.codex\skills\impeccable\scripts\detect.mjs' --json furano/index.html furano/wireframe_kr.html furano/bilingual.html
```

Expected: no load-bearing design-system, accessibility, overflow, or generic-AI-style findings. Fix confirmed findings in the renderer, regenerate, and rerun Steps 2–4.

- [ ] **Step 5: Commit the verified feature**

```powershell
git add tools tests furano
git commit -m "test: verify Furano editorial detail pages"
```

- [ ] **Step 6: Run the finish review and document the built system**

Capture desktop and mobile screenshots for all three pages, then dispatch an Impeccable finish reviewer with the original brief, direction contract, changed targets, detector output, and screenshot paths. Apply material findings in one batch, rebuild, recapture, and return the recaptures to the same reviewer for the final verdict. After the verdict, dispatch the Impeccable documenter with the built artifact, `PRODUCT.md`, direction contract, and `impeccable/reference/document.md`; commit the resulting `DESIGN.md` and sidecar. Completion requires the generated HTML to retain the seed `88bbc100` contract comment.

- [ ] **Step 7: Copy the reviewed canonical source modules**

Copy the three reviewed Python source files from `tools/` to `C:\Users\38185\ZCodeProject\`, keeping all language content and the sole command entry point in `build_furano.py`. Run the canonical entry point from `ZCodeProject` and compare SHA-256 hashes of its three outputs with the repository’s three generated HTML files; all three hashes must match.

- [ ] **Step 8: Push the reviewed feature branch and publish**

Push `codex/furano-editorial-v4`, then fast-forward or merge its reviewed commits to `main` and push `main`. Do not force-push.

- [ ] **Step 9: Verify the live GitHub Pages content**

GitHub Pages may cache for up to ten minutes. Run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tests/verify_furano_remote.py
```

Repeat only while the response still proves the old version and remain within the monitoring budget. Completion requires three page HTTP 200 results, required v4 markers on all pages, banned markers absent, and five large WebP asset HTTP 200 results.

- [ ] **Step 10: Final commit/push consistency check**

Verify:

```powershell
git status --short --branch
git rev-parse HEAD
git rev-parse origin/main
```

Expected: clean worktree and local `HEAD` equal to `origin/main`.
