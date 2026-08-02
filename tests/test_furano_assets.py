import unittest
from pathlib import Path

from PIL import Image

from tools.furano_assets import ASSETS, decoded_dimensions_are_usable, render_sources_markdown


class AssetContractTests(unittest.TestCase):
    def test_decoded_dimension_mismatch_is_rejected(self):
        asset = next(item for item in ASSETS if item.key == "furano-people")
        self.assertFalse(
            decoded_dimensions_are_usable(
                asset, (asset.source_width + 1, asset.source_height)
            )
        )

    def test_decoded_height_only_mismatch_is_rejected(self):
        asset = next(item for item in ASSETS if item.key == "furano-people")
        self.assertFalse(
            decoded_dimensions_are_usable(
                asset, (asset.source_width, asset.source_height + 1)
            )
        )

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
