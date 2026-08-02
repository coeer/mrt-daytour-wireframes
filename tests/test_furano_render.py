from copy import deepcopy
import hashlib
from html import escape as html_escape
import json
import re
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

from tools.build_furano import ITINERARY_KEYS, KR, ZH, build_all
from tools.furano_renderer import render_bilingual, render_single


class _Element:
    def __init__(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
        parent: "_Element | None" = None,
    ) -> None:
        self.tag = tag
        self.attrs = dict(attrs)
        self.parent = parent
        self.children: list[_Element] = []

    @property
    def classes(self) -> set[str]:
        return set((self.attrs.get("class") or "").split())

    def find_all(self, class_name: str | None = None) -> list["_Element"]:
        found = []
        if class_name is None or class_name in self.classes:
            found.append(self)
        for child in self.children:
            found.extend(child.find_all(class_name))
        return found


class _ContractParser(HTMLParser):
    _VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                  "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self) -> None:
        super().__init__()
        self.root = _Element("document", [])
        self.stack = [self.root]

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        node = _Element(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in self._VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in self._VOID_TAGS:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return


def _parse(html: str) -> _Element:
    parser = _ContractParser()
    parser.feed(html)
    return parser.root


def _outside_itinerary(html: str) -> str:
    start = html.index('<section class="section itinerary"')
    end = html.index('<section class="section included"', start)
    return html[:start] + html[end:]


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
            self.assertNotRegex(
                html,
                r'<figure class="route-figure"[^>]*>\n\n',
            )

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

    def test_hero_layers_and_badge_contrast_are_explicit(self):
        html = render_single(KR, "ko")
        self.assertIn(".hero__photo { z-index: 0; }", html)
        self.assertRegex(html, r"\.hero::after \{[^}]*z-index: 1;")
        self.assertRegex(html, r"\.hero__inner \{[^}]*z-index: 2;")
        self.assertRegex(
            html,
            r"\.included-badge \{[^}]*background: var\(--flower-pink\);"
            r"[^}]*color: var\(--ink\);",
        )

    def test_korean_itinerary_ctas_use_the_correct_word(self):
        html = render_single(KR, "ko")
        self.assertIn(">일정과 포함 내용 보기</a>", html)
        self.assertIn(">일정 다시 보기</a>", html)
        self.assertNotIn(">행정", html)

    def test_bilingual_language_order_and_shared_images(self):
        html = render_bilingual(KR, ZH)
        self.assertIn(
            'class="language-column language-column--kr" lang="ko"',
            html,
        )
        self.assertIn(
            'class="language-column language-column--zh" lang="zh-CN"',
            html,
        )
        self.assertLess(html.index("language-column--kr"), html.index("language-column--zh"))
        self.assertEqual(html.count("<picture"), 7)
        self.assertIn("gap: 40px", html)
        self.assertIn("border-right: 1px solid var(--line)", html)
        self.assertIn("@media (max-width: 880px)", html)
        self.assertIn("grid-template-columns: 1fr", html)
        self.assertIn("border-bottom: 1px solid var(--line)", html)
        self.assertIn('<span lang="zh-CN">札幌</span>', html)
        self.assertIn(".bilingual .timeline::before { display: none; }", html)
        pickup = html[html.index('id="pickup"') : html.index('id="itinerary"')]
        self.assertLess(pickup.index("route-canvas"), pickup.index("language-grid"))

    def test_bilingual_shared_photos_have_unique_two_language_names(self):
        root = _parse(render_bilingual(KR, ZH))
        photos = root.find_all("shared-photo")
        self.assertEqual(len(photos), 7)
        ids = {
            node.attrs["id"]: node
            for node in root.find_all()
            if "id" in node.attrs
        }
        referenced_ids: list[str] = []
        for photo in photos:
            self.assertEqual(photo.attrs.get("role"), "img")
            self.assertIn("data-shared-media", photo.attrs)
            self.assertNotIn("aria-label", photo.attrs)
            references = (photo.attrs.get("aria-labelledby") or "").split()
            self.assertEqual(len(references), 2)
            referenced_ids.extend(references)
            self.assertEqual(
                [ids[reference].attrs.get("lang") for reference in references],
                ["ko", "zh-CN"],
            )
            self.assertTrue(
                all("visually-hidden" in ids[reference].classes for reference in references)
            )
            images = [node for node in photo.find_all() if node.tag == "img"]
            self.assertEqual(len(images), 1)
            self.assertEqual(images[0].attrs.get("alt"), "")
        self.assertEqual(len(referenced_ids), 14)
        self.assertEqual(len(referenced_ids), len(set(referenced_ids)))

    def test_single_language_photos_keep_language_owned_alt_text(self):
        for content, lang in ((KR, "ko"), (ZH, "zh-CN")):
            ui = content["editorial"]
            images = [
                node for node in _parse(render_single(content, lang)).find_all()
                if node.tag == "img"
            ]
            self.assertEqual(
                [node.attrs.get("alt") for node in images],
                [
                    ui["hero_alt"],
                    ui["people_alt"],
                    ui["shikisai_alt"],
                    ui["softserve_alt"],
                    ui["blue_pond_alt"],
                    ui["shirahige_alt"],
                    ui["blue_pond_alt"],
                ],
            )

    def test_bilingual_language_markers_include_hidden_full_language_names(self):
        root = _parse(render_bilingual(KR, ZH))
        labels = root.find_all("language-label")
        self.assertGreater(len(labels), 0)
        for label in labels:
            visible = [child for child in label.children if "language-code" in child.classes]
            hidden = [child for child in label.children if "visually-hidden" in child.classes]
            self.assertEqual(len(visible), 1)
            self.assertEqual(len(hidden), 1)
            self.assertIn(hidden[0].attrs.get("lang"), {"ko", "zh-CN"})

    def test_bilingual_mobile_hero_compacts_only_its_language_separator(self):
        html = render_bilingual(KR, ZH)
        mobile_css = html[html.index("@media (max-width: 880px)") :]
        self.assertIn(".bilingual .hero__inner { gap: 0; }", mobile_css)
        self.assertRegex(
            mobile_css,
            r"\.bilingual \.hero \.language-column--kr \{\s*"
            r"padding-bottom: 16px;\s*\}",
        )
        self.assertRegex(
            mobile_css,
            r"\.bilingual \.hero \.language-column--zh \{\s*"
            r"padding-top: 16px;\s*\}",
        )

    def test_bilingual_phone_hero_keeps_both_actions_in_compact_rows(self):
        html = render_bilingual(KR, ZH)
        hero = html[html.index('<header class="hero"') : html.index("</header>")]
        self.assertEqual(hero.count('class="language-column'), 2)
        self.assertEqual(hero.count('class="button'), 4)

        phone_css = html[html.rindex("@media (max-width: 560px)") :]
        self.assertRegex(
            phone_css,
            r"\.bilingual \.hero__inner \{\s*padding: 36px 0 20px;\s*\}",
        )
        self.assertRegex(
            phone_css,
            r"\.bilingual \.hero \.language-label \{[^}]*min-height: 0;",
        )
        self.assertRegex(
            phone_css,
            r"\.bilingual \.hero h1 \{[^}]*"
            r"font-size: clamp\(1\.85rem, 8vw, 2rem\);",
        )
        self.assertRegex(
            phone_css,
            r"\.bilingual \.hero \.actions \{[^}]*"
            r"grid-template-columns: repeat\(2, minmax\(0, 1fr\)\);",
        )
        self.assertRegex(
            phone_css,
            r"\.bilingual \.hero \.button \{[^}]*min-height: 44px;",
        )

    def test_finish_review_uses_renderer_authored_typographic_devices(self):
        single_kr = render_single(KR, "ko")
        single_zh = render_single(ZH, "zh-CN")
        bilingual = render_bilingual(KR, ZH)

        self.assertIn(
            '<span class="language-code" aria-hidden="true">KR</span>',
            bilingual,
        )
        self.assertIn(
            '<span class="language-code" aria-hidden="true">CN</span>',
            bilingual,
        )
        self.assertIn(
            '<span class="visually-hidden" lang="ko">한국어 원문</span>',
            bilingual,
        )
        self.assertIn(
            '<span class="visually-hidden" lang="zh-CN">中文对照</span>',
            bilingual,
        )

        for html in (single_kr, single_zh, bilingual):
            outside_itinerary = _outside_itinerary(html)
            for glyph in (
                "🇰🇷",
                "🇨🇳",
                "💜",
                "🌈",
                "💙",
                "🚗",
                "👨‍👩‍👧‍👦",
                "🎫",
                "💰",
                "🏠",
                "🚉",
                "🚐",
                "📍",
                "🗣️",
                "💡",
                "💬",
            ):
                self.assertNotIn(glyph, outside_itinerary)
            self.assertIn('class="hero-color-dots"', html)
            self.assertIn('data-icon="ticket"', html)

    def test_finish_review_structures_and_escapes_hero_subtitle(self):
        content = deepcopy(KR)
        content["subtitle"] = ("<strong>first line</strong>", "second & line")
        html = render_single(content, "ko")
        hero = html[html.index('<header class="hero"') : html.index("</header>")]

        self.assertEqual(hero.count('class="hero__subtitle-line"'), 2)
        self.assertNotIn("<br>", hero)
        self.assertNotIn("<strong>first line</strong>", hero)
        self.assertIn("&lt;strong&gt;first line&lt;/strong&gt;", hero)
        self.assertIn("second &amp; line", hero)
        self.assertEqual(hero.count('class="hero-color-dot"'), 3)

    def test_finish_review_keeps_all_itinerary_emoji_low_salience(self):
        for html, expected_count in (
            (render_single(KR, "ko"), 1),
            (render_single(ZH, "zh-CN"), 1),
            (render_bilingual(KR, ZH), 2),
        ):
            for glyph in ("🚗", "💜", "🎢", "🌈", "🍽️", "📸", "💧", "⏰"):
                wrapped = (
                    '<span class="copy-emoji" aria-hidden="true">'
                    f"{glyph}</span>"
                )
                self.assertEqual(html.count(glyph), expected_count)
                self.assertEqual(html.count(wrapped), expected_count)

    def test_itinerary_media_and_peak_follow_stable_keys_after_reorder(self):
        content = deepcopy(KR)
        for key, item in zip(ITINERARY_KEYS, content["itinerary"], strict=True):
            item["key"] = key
        content["itinerary"] = content["itinerary"][3:] + content["itinerary"][:3]
        html = render_single(content, "ko")

        def stop(key: str) -> str:
            self.assertIn(f'data-itinerary-key="{key}"', html)
            start = html.index(f'data-itinerary-key="{key}"')
            return html[start : html.index("</article>", start)]

        self.assertIn('data-peak="true"', stop("farm_tomita"))
        self.assertNotIn('data-peak="true"', stop("shikisai_no_oka"))
        self.assertIn("road-window", stop("roller_coaster_road"))
        self.assertIn("shikisai-1600.webp", stop("shikisai_no_oka"))
        self.assertIn("included-badge", stop("shikisai_no_oka"))
        self.assertIn("lavender-softserve-1200.webp", stop("free_lunch"))
        self.assertIn("blue-pond-1600.webp", stop("blue_pond"))
        self.assertIn("shirahige-1600.webp", stop("shirahige_falls"))

    def test_finish_review_removes_faq_title_emoji_without_changing_qa(self):
        expected = (
            (
                KR,
                render_single(KR, "ko"),
                "695302d0c97aecf11c71e198146914d9e41103a43b874bf3694d498b6cddb5d2",
            ),
            (
                ZH,
                render_single(ZH, "zh-CN"),
                "42f2716a4131be3401c3d6ec94ec022960da5331efa35035422be6d57e87a97a",
            ),
        )
        for content, html, expected_digest in expected:
            digest = hashlib.sha256(
                json.dumps(
                    content["faq"],
                    ensure_ascii=False,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            self.assertEqual(digest, expected_digest)

            faq = html[html.index('<section class="section faq"') : html.index(
                '<section class="closing"'
            )]
            self.assertEqual(faq.count("<details"), 8)
            self.assertNotIn("💡", faq)
            for question, answer in content["faq"]:
                self.assertIn(html_escape(question), faq)
                self.assertIn(html_escape(answer), faq)

    def test_all_modes_have_exact_section_order_and_direction_contract(self):
        section_ids = [
            "top",
            "benefits",
            "pain-solution",
            "pickup",
            "itinerary",
            "included",
            "cancellation",
            "faq",
            "closing",
        ]
        for html in (
            render_single(KR, "ko"),
            render_single(ZH, "zh-CN"),
            render_bilingual(KR, ZH),
        ):
            rendered_ids = re.findall(
                r'<(?:header|section)\b[^>]*\bid="([^"]+)"',
                html,
            )
            self.assertEqual(rendered_ids, section_ids)
            self.assertEqual(html.count("<details open>"), 1)
            self.assertIn("seed 88bbc100", html)
            self.assertRegex(html, r"<body><!--\s*THESIS:")

    def test_each_page_preloads_exactly_one_responsive_hero(self):
        for html in (
            render_single(KR, "ko"),
            render_single(ZH, "zh-CN"),
            render_bilingual(KR, ZH),
        ):
            root = _parse(html)
            preloads = [
                node for node in root.find_all()
                if node.tag == "link"
                and node.attrs.get("rel") == "preload"
                and node.attrs.get("as") == "image"
            ]
            self.assertEqual(len(preloads), 1)
            self.assertEqual(
                preloads[0].attrs.get("href"),
                "img/hero-farm-tomita-1600.webp?v=20260729-v4",
            )
            self.assertEqual(preloads[0].attrs.get("imagesizes"), "100vw")
            self.assertEqual(
                preloads[0].attrs.get("imagesrcset"),
                "img/hero-farm-tomita-960.webp?v=20260729-v4 960w, "
                "img/hero-farm-tomita-1600.webp?v=20260729-v4 1600w",
            )
            hero_images = [
                node for node in root.find_all()
                if node.tag == "img" and node.attrs.get("fetchpriority") == "high"
            ]
            self.assertEqual(len(hero_images), 1)
            self.assertEqual(
                hero_images[0].attrs.get("srcset"),
                preloads[0].attrs.get("imagesrcset"),
            )
            self.assertEqual(
                hero_images[0].attrs.get("sizes"),
                preloads[0].attrs.get("imagesizes"),
            )
            assert hero_images[0].parent is not None
            self.assertEqual(hero_images[0].parent.tag, "picture")
            self.assertFalse(
                any(child.tag == "source" for child in hero_images[0].parent.children)
            )

    def test_hero_alone_has_priority_and_nonhero_photos_are_lazy(self):
        for html in (
            render_single(KR, "ko"),
            render_single(ZH, "zh-CN"),
            render_bilingual(KR, ZH),
        ):
            images = [node for node in _parse(html).find_all() if node.tag == "img"]
            priority = [node for node in images if node.attrs.get("fetchpriority") == "high"]
            self.assertEqual(len(priority), 1)
            self.assertIn("hero-farm-tomita", priority[0].attrs["src"])
            self.assertEqual(priority[0].attrs.get("loading"), "eager")
            nonhero = [node for node in images if node is not priority[0]]
            self.assertTrue(nonhero)
            self.assertTrue(all(node.attrs.get("loading") == "lazy" for node in nonhero))
            self.assertTrue(all("fetchpriority" not in node.attrs for node in nonhero))

    def test_each_mode_has_exactly_one_itinerary_peak(self):
        for html in (
            render_single(KR, "ko"),
            render_single(ZH, "zh-CN"),
            render_bilingual(KR, ZH),
        ):
            itinerary = html[
                html.index('<section class="section itinerary"') :
                html.index('<section class="section included"')
            ]
            self.assertEqual(itinerary.count('data-peak="true"'), 1)

    def test_every_bilingual_grid_has_one_immediately_preceding_shared_media(self):
        root = _parse(render_bilingual(KR, ZH))
        grids = root.find_all("language-grid")
        shared_media = [
            node
            for node in root.find_all()
            if "data-shared-media" in node.attrs
        ]
        self.assertEqual(len(grids), 17)
        self.assertEqual(len(shared_media), len(grids))
        for grid in grids:
            assert grid.parent is not None
            index = grid.parent.children.index(grid)
            self.assertGreater(index, 0)
            self.assertIn(
                "data-shared-media",
                grid.parent.children[index - 1].attrs,
            )

        stops = root.find_all("bilingual-stop")
        self.assertEqual(len(stops), 8)
        for stop in stops:
            direct_shared = [
                child for child in stop.children if "data-shared-media" in child.attrs
            ]
            direct_grids = [
                child for child in stop.children if "language-grid" in child.classes
            ]
            self.assertEqual(len(direct_shared), 1)
            self.assertEqual(len(direct_grids), 1)
            self.assertEqual(
                stop.children.index(direct_shared[0]) + 1,
                stop.children.index(direct_grids[0]),
            )

    def test_bilingual_mixed_language_controls_have_owned_accessible_names(self):
        root = _parse(render_bilingual(KR, ZH))
        skip_links = root.find_all("skip-link")
        self.assertEqual(len(skip_links), 1)
        self.assertEqual(
            [child.attrs.get("lang") for child in skip_links[0].children],
            ["ko", None, "zh-CN"],
        )

        labelled_media = [
            node
            for node in root.find_all()
            if node.attrs.get("role") == "img"
            and ({"route-figure", "road-window"} & node.classes)
        ]
        self.assertEqual(len(labelled_media), 2)
        ids = {
            node.attrs["id"]: node
            for node in root.find_all()
            if "id" in node.attrs
        }
        referenced_ids: list[str] = []
        for media in labelled_media:
            self.assertNotIn("aria-label", media.attrs)
            references = (media.attrs.get("aria-labelledby") or "").split()
            self.assertEqual(len(references), 2)
            referenced_ids.extend(references)
            self.assertEqual(
                [ids[reference].attrs.get("lang") for reference in references],
                ["ko", "zh-CN"],
            )
        self.assertEqual(len(referenced_ids), len(set(referenced_ids)))

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
            output_dir = Path(temp_dir)
            written = build_all(output_dir)
            self.assertEqual(
                written,
                {
                    "zh": "index.html",
                    "kr": "wireframe_kr.html",
                    "bi": "bilingual.html",
                },
            )
            for filename in ("index.html", "wireframe_kr.html", "bilingual.html"):
                self.assertTrue((output_dir / filename).exists())
                self.assertNotIn(b"\r\n", (output_dir / filename).read_bytes())
                lines = (output_dir / filename).read_text(encoding="utf-8").splitlines()
                self.assertTrue(
                    all(line == line.rstrip() for line in lines),
                    f"{filename} contains trailing whitespace",
                )

    def test_build_script_runs_directly_from_repository_root(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/build_furano.py",
                    "--output",
                    temp_dir,
                ],
                cwd=Path(__file__).resolve().parents[1],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(temp_dir) / "index.html").exists())
            self.assertTrue((Path(temp_dir) / "wireframe_kr.html").exists())
            self.assertTrue((Path(temp_dir) / "bilingual.html").exists())
