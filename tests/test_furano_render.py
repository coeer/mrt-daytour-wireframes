import subprocess
import sys
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
            self.assertNotIn(b"\r\n", (output_dir / "index.html").read_bytes())
            self.assertNotIn(b"\r\n", (output_dir / "wireframe_kr.html").read_bytes())
            for filename in ("index.html", "wireframe_kr.html"):
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
