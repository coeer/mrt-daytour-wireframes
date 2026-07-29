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

    def test_refund_redlines_preserve_all_eligibility_boundaries(self):
        self.assertIn("3일 전까지", KR["refund_summary"])
        self.assertIn("2일 전~당일", KR["refund_summary"])
        self.assertIn("환불 불가", KR["refund_summary"])
        self.assertIn("미성사", KR["refund_summary"])
        self.assertIn("提前3天及之前", ZH["refund_summary"])
        self.assertIn("提前2天至当天", ZH["refund_summary"])
        self.assertIn("不可退款", ZH["refund_summary"])
        self.assertIn("不成团", ZH["refund_summary"])
