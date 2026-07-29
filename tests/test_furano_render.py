import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.build_furano import KR, ZH, build_all
from tools.furano_renderer import render_bilingual, render_single


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
        self.assertEqual(html.count("hero-farm-tomita-1600.webp"), 1)
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

    def test_bilingual_section_order_faq_state_and_direction_contract(self):
        html = render_bilingual(KR, ZH)
        section_ids = (
            "top",
            "benefits",
            "pain-solution",
            "pickup",
            "itinerary",
            "included",
            "cancellation",
            "faq",
            "closing",
        )
        positions = [html.index(f'id="{section_id}"') for section_id in section_ids]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(html.count("<details open>"), 1)
        self.assertIn("seed 88bbc100", html)
        self.assertRegex(html, r"<body><!--\s*THESIS:")

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
