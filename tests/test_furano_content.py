import hashlib
import json
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

    def test_itinerary_records_keep_the_canonical_stable_key_sequence(self):
        for content in (KR, ZH):
            self.assertEqual(
                tuple(item.get("key") for item in content["itinerary"]),
                ITINERARY_KEYS,
            )

    def test_itinerary_records_match_the_authoritative_baseline_digests(self):
        expected = (
            (KR, "58a84d0897f5a713c6805250a98fdab8f3145f807fb02950e629f8a0f1414455"),
            (ZH, "c623354ee406268b3625e7880b38e414eb20076973fe96f0fc250da925ece65a"),
        )
        for content, expected_digest in expected:
            digest = hashlib.sha256(
                json.dumps(
                    content["itinerary"],
                    ensure_ascii=False,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()
            self.assertEqual(digest, expected_digest)

    def test_language_redlines(self):
        korean_blob = repr(KR)
        chinese_blob = repr(ZH)
        self.assertNotIn("한국어 기사", korean_blob)
        self.assertNotIn("카카오톡 한국어 상담", korean_blob)
        self.assertNotIn("司机会韩语", chinese_blob)
        self.assertNotIn("KakaoTalk韩语咨询", chinese_blob)
        self.assertIn("일본어·영어", korean_blob)
        self.assertIn("日语/英语", chinese_blob)

    def test_refund_redlines_preserve_all_eligibility_boundaries(self):
        self.assertIn("3일 전까지", KR["refund_summary"])
        self.assertIn("2일 전~당일", KR["refund_summary"])
        self.assertIn("환불 불가", KR["refund_summary"])
        self.assertIn("미성사", KR["refund_summary"])
        self.assertIn("提前3天及之前", ZH["refund_summary"])
        self.assertIn("提前2天至当天", ZH["refund_summary"])
        self.assertIn("不可退款", ZH["refund_summary"])
        self.assertIn("不成团", ZH["refund_summary"])
