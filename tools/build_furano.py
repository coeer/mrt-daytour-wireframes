"""Approved bilingual product content for the Furano/Biei day tour."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

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

KR_ITINERARY = [
    {"type": "pass", "time": "예정 08:00", "name": "삿포로 출발 🚗", "dur": "(숙소 픽업 또는 삿포로역 집합 후)"},
    {"time": "예정 10:30", "name": "팜 토미타", "dur": "(약 60분 · 포토타임)", "peak": True,
     "color": "#9b5de5", "img": "img/tomita.jpg", "cap": "팜 토미타 라벤더 밭",
     "desc": "보랏빛 라벤더가 언덕 끝까지 💜 라벤더 소프트크림은 필수!"},
    {"time": "예정 11:30", "name": "차창 감상: 제트코스터 로드", "dur": "(약 15분 · 하차 없음)",
     "color": "#06d6a0", "placeholder": "[ 제트코스터 로드 차창 시점 사진 ]",
     "desc": "롤러코스터처럼 오르내리는 언덕길, 창밖으로 흐르는 여름 🎢"},
    {"time": "예정 12:15", "name": "사계채의 언덕", "dur": "(약 60분)", "free": True,
     "color": "#ff5d8f", "img": "img/shikisai.jpg", "cap": "사계채의 언덕 무지개 꽃밭",
     "desc": "15헥타르 무지개 꽃밭, 계절마다 새로운 색 🌈"},
    {"type": "pass", "time": "예정 13:15", "name": "자유 점심 🍽️", "dur": "(약 1시간 · 개별 결제)",
     "desc": "정해진 단체 식사 NO, 내가 고르는 자유 점심"},
    {"time": "예정 15:00", "name": "청의 호수", "dur": "(약 30분 · 포토타임)",
     "color": "#00b4d8", "img": "img/aoiike.jpg", "cap": "청의 호수(아오이이케)",
     "desc": "SNS 최다 공유 블루 스폿, 오늘의 인생샷 📸"},
    {"time": "예정 15:35", "name": "시라히게 폭포", "dur": "(약 25분)",
     "color": "#2ec4b6", "img": "img/shirahige.jpg", "cap": "시라히게 폭포",
     "desc": "흰 수염처럼 흘러내리는 드문 잠수 폭포 💧"},
    {"type": "pass", "time": "예정 16:00", "name": "삿포로로 출발 → 예정 18:30 삿포로 도착",
     "note": "⏰ 도로 상황에 따라 도착 시간이 앞뒤로 달라질 수 있습니다. 출발 시간이 정해진 교통편(항공·기차)이나 공연·레스토랑 예약은 가급적 다른 날짜에 잡아 주세요."},
]

ZH_ITINERARY = [
    {"type": "pass", "time": "预计 08:00", "name": "札幌出发 🚗", "dur": "(住宿接送或札幌站集合后)"},
    {"time": "预计 10:30", "name": "富田农场", "dur": "(约60分钟·拍照时间)", "peak": True,
     "color": "#9b5de5", "img": "img/tomita.jpg", "cap": "富田农场薰衣草花田",
     "desc": "紫色薰衣草一路铺到山坡尽头 💜 薰衣草冰淇淋必尝!"},
    {"time": "预计 11:30", "name": "车窗观赏：云霄飞车之路", "dur": "(约15分钟·不下车)",
     "color": "#06d6a0", "placeholder": "[ 云霄飞车之路 车内视角照片 ]",
     "desc": "像过山车一样起伏的坡道，窗外流动的夏天 🎢"},
    {"time": "预计 12:15", "name": "四季彩之丘", "dur": "(约60分钟)", "free": True,
     "color": "#ff5d8f", "img": "img/shikisai.jpg", "cap": "四季彩之丘彩虹花田",
     "desc": "15公顷彩虹花田，每个季节都有新颜色 🌈"},
    {"type": "pass", "time": "预计 13:15", "name": "自由午餐 🍽️", "dur": "(约1小时·各自结账)",
     "desc": "不是固定的团餐，是自己选的午餐"},
    {"time": "预计 15:00", "name": "青池", "dur": "(约30分钟·拍照时间)",
     "color": "#00b4d8", "img": "img/aoiike.jpg", "cap": "青池",
     "desc": "SNS上被分享最多的蓝色景点，拍出今天的人生照片 📸"},
    {"time": "预计 15:35", "name": "白须瀑布", "dur": "(约25分钟)",
     "color": "#2ec4b6", "img": "img/shirahige.jpg", "cap": "白须瀑布",
     "desc": "像白色胡须一样流下的罕见\"潜水瀑布\" 💧"},
    {"type": "pass", "time": "预计 16:00", "name": "返程回札幌 → 预计18:30左右抵达札幌",
     "note": "⏰ 根据当天路况，抵达时间可能前后浮动。有固定出发时间的交通工具（航班·火车）或演出、餐厅预约，建议您尽量安排在其他日期。"},
]

KR = {
    "header": "한국어 원문",
    "language_code": "KR",
    "slogan": "ONE DAY. THREE COLORS OF SUMMER.",
    "h1": "삿포로 출발 후라노·비에이 4인 소그룹 1일 투어",
    "subtitle": (
        "보랏빛 라벤더 · 무지개 꽃밭 · 신비로운 파란 연못",
        "여름 홋카이도의 세 가지 색을 하루에",
    ),
    "hl": [
        ("pickup", "삿포로역 3km 이내 숙소 앞 픽업 (이른 아침 집합 장소 이동 NO)"),
        ("group", "최소 4명 출발 · 49인승 대형 버스가 아닌 소그룹"),
        ("ticket", "사계채의 언덕 입장권 포함 · 현지 추가 비용 없음 (식사 제외)"),
        ("photo", "소그룹 운행이라 사진·관람 시간이 넉넉합니다"),
        ("language", "일본어·영어 기사 + 번역 앱"),
        ("refund", "여행일 3일 전까지 통보 시 100% 전액 환불 · 미성사 시에도 전액 환불"),
    ],
    "pain": "\"7시 반 집합, 49인승 버스, 좌석은 선착순.\" 대형 버스투어의 하루는 이렇게 시작합니다.<br>이 투어는 <b>숙소 앞에서 시작</b>해, 돌아오는 길엔 편하게 잠들 수 있습니다. 운전과 길 찾기는 저희가 할게요. 당신은 창밖의 여름만 담으세요.",
    "pickup_time": "예정 08:00 삿포로 출발",
    "pickup": [
        "삿포로역 반경 3km 이내 숙소 → 숙소 앞 픽업",
        "3km 밖 숙소 → 삿포로역 집합 (상세 장소는 전날 안내)",
        "정확한 픽업 시간은 출발 전날 단톡방에서 안내드립니다",
    ],
    "tl": KR_ITINERARY,
    "itinerary": KR_ITINERARY,
    "logi_title": "일본 오사카부지사 등록 여행사 · JNTO(일본정부관광국) 협력사",
    "logi": [
        "차량: 당일 모객 인원에 맞춘 승합차 배차",
        "픽업: 삿포로역 반경 3km 숙소 앞 (범위 밖은 삿포로역 집합)",
        "언어: 일본어·영어 가능 기사 + 번역 앱 지원",
    ],
    "logi_placeholder": "[ 자질증명서 + 차량 실물 사진 ]",
    "faq_title": "■ 예약 전, 이것만 알아두세요",
    "faq": [
        ("Q1. 몇 명부터 출발하나요?", "4명 이상 모이면 출발이 확정됩니다. 전 세계에서 동시에 예약을 받아 모객하기 때문에, 예약이 빠를수록 출발 확정 확률이 높아집니다. 만약 출발이 어렵게 되면 미리 개별로 안내드리며, 취소하실 경우 수수료 없이 전액 환불해 드립니다."),
        ("Q2. 차량은 어떻게 배차되나요? 함께 타는 분은 누구인가요?", "소규모 합승으로 운행되며, 당일 모객 인원에 맞춰 승합차가 배차됩니다. 전 세계 게스트를 모객하기 때문에 다른 국가에서 오신 분들과 동승하실 수 있습니다. 함께하는 시간 동안 서로의 여행 이야기를 나누는 소소한 즐거움이 되기도 합니다. 한 번의 여행은 누구에게나 특별한 계획입니다. 저희는 모든 게스트분을 한 분 한 분 정성스럽게 모시고 있습니다."),
        ("Q3. 비가 오거나 날씨가 흐려도 진행되나요?", "네, 진행됩니다. 비가 그친 뒤 꽃밭은 색이 더 선명해지고, 흐린 날에도 청의 호수의 파란색은 그대로입니다. 다만 태풍·폭설 등 악천후로 안전상 진행이 어려운 경우에는 출발 전 안내 후 전액 환불해 드립니다."),
        ("Q4. 기사님이 안내도 해 주시나요?", "운전 겸 안내 기사가 동행합니다. 주요 포인트 도착 시 간단한 안내를 드리며, 각 명소에서 하차하여 자유롭게 관람하시면 됩니다. 기사님은 차량에서 대기하며 출발 시간에 맞춰 다음 장소로 이동합니다. 기사님은 일본어·영어가 가능합니다."),
        ("Q5. 출발 전 연락은 어떻게 오나요?", "예약 완료 후, 자주 사용하시는 메신저(WhatsApp·LINE·KakaoTalk)를 남겨 주세요. WhatsApp을 가장 추천해 드립니다. 출발 전날, 온라인 여행 그룹(단톡방)을 만들어 드립니다. 그룹에는 기사님과 저희 담당자가 함께 계시며, 당일 이동 일정과 픽업 안내를 드립니다. 출발 당일 아침, 기사님이 약속된 시간에 숙소(또는 삿포로역 집합 장소) 앞으로 모시러 옵니다."),
        ("Q6. 식사와 입장료는 포함되어 있나요?", "사계채의 언덕 입장권은 포함되어 있습니다. 팜 토미타·청의 호수·시라히게 폭포는 무료 입장입니다. 식사는 불포함이며, 점심 시간(약 1시간)에 주변 식당에서 개별 결제로 자유롭게 드시면 됩니다. 입장권 외에 현지에서 추가로 결제하실 비용은 없습니다."),
        ("Q7. 취소 및 환불 규정은 어떻게 되나요?", "여행일 기준 3일 전까지 통보 시: 100% 전액 환불 / 여행일 기준 2일 전~당일 통보 시: 환불 불가 ※ 여행일은 현지(일본) 시각 기준입니다."),
        ("Q8. 라벤더는 언제가 가장 예쁜가요?", "보통 6월 말부터 8월 초가 절정이며, 개화 시기는 그해 날씨에 따라 달라질 수 있습니다. 라벤더 시즌이 지나도 사계채의 언덕에는 여름 내내 계절 꽃이 피어 꽃밭을 즐기실 수 있습니다."),
    ],
    "faq_closing": "■ 그 외에 궁금하신 점이 있으시면, 언제든 편하게 문의해 주세요",
    "pickup_radius_km": 3,
    "minimum_departure": 4,
    "included_ticket": "사계채의 언덕 입장권",
    "refund_summary": "여행일 기준 3일 전까지 통보 시: 100% 전액 환불 / 여행일 기준 2일 전~당일 통보 시: 환불 불가 · 미성사 시에도 전액 환불",
}

ZH = {
    "header": "中文对照",
    "language_code": "CN",
    "slogan": "ONE DAY. THREE COLORS OF SUMMER.（一天，收集夏天的三种颜色）",
    "h1": "札幌出发 富良野·美瑛4人小团1日游",
    "subtitle": (
        "紫色薰衣草 · 彩虹花田 · 神秘的蓝色池塘",
        "一天收集夏日北海道的三种颜色",
    ),
    "hl": [
        ("pickup", "札幌站3km内住宿门口接送（不用一早赶去集合点）"),
        ("group", "4人成团·不是49座大巴的小团"),
        ("ticket", "含四季彩之丘门票·当地无额外费用（餐食除外）"),
        ("photo", "因为我们是小团，拍照游玩时间会很充裕"),
        ("language", "日语/英语司机+翻译app"),
        ("refund", "出行日前3天通知可100%全额退款·不成团也无损退款"),
    ],
    "pain": "\"7点半集合、49座大巴、座位先到先得。\"大巴团的一天是这样开始的。<br>这个团从<b>住宿门口开始</b>，回程路上可以安心睡一觉。开车和找路交给我们，你只管把夏天装进相机。",
    "pickup_time": "预计 08:00 札幌出发",
    "pickup": [
        "札幌站半径3km内住宿 → 住宿门口接送",
        "3km范围外住宿 → 札幌站集合（详细地点前一天告知）",
        "准确接送时间会在出发前一天通过群聊通知",
    ],
    "tl": ZH_ITINERARY,
    "itinerary": ZH_ITINERARY,
    "logi_title": "日本大阪府知事登记旅行社·JNTO（日本政府观光局）合作方",
    "logi": [
        "车辆：按当日成团人数安排商务车",
        "接送：札幌站半径3km内住宿门口（范围外为札幌站集合）",
        "语言：日语/英语司机+翻译app支持",
    ],
    "logi_placeholder": "[ 资质证书+车辆实拍 ]",
    "faq_title": "■ 预订前，这些请先了解一下",
    "faq": [
        ("Q1. 几个人成团出发？", "4人成团。我们在全球同步收客拼团，越早预订成团概率越大。如果最终未能成团，会提前单独通知您；取消的话不收取任何手续费，全额退款。"),
        ("Q2. 车辆怎么安排？同车的是谁？", "本行程为小团拼车，按当日成团人数安排商务车。因为面向全球收客，车上可能有来自其他国家的客人。同行时光里分享彼此的旅途故事，也是一种小小的乐趣。一次旅行对每个人来说都是特别的计划，我们会一位一位用心接待每位客人。"),
        ("Q3. 下雨或阴天行程还进行吗？", "是的，照常进行。雨后的花田颜色更鲜艳，阴天青池的蓝色也依然如故。但因台风、暴雪等恶劣天气导致安全上难以进行时，会在出发前通知并全额退款。"),
        ("Q4. 司机也做讲解吗？", "司机兼向导陪同。到达主要景点时做简短介绍，各景点下车后自由参观。司机在车内等候，按出发时间前往下一站。司机可使用日语·英语。"),
        ("Q5. 出发前怎么联系？", "预订完成后，请留下您常用的即时通讯账号（WhatsApp·LINE·KakaoTalk），我们最推荐WhatsApp。出发前一天，我们会建立线上旅行群（群聊），群里有司机和我们的负责人，会发送当天的行程安排和接送信息。出发当天早上，司机会按约定时间到住宿（或札幌站集合地点）门口来接。"),
        ("Q6. 餐费和门票包含吗？", "四季彩之丘门票已包含。富田农场·青池·白须瀑布均为免费入场。餐食不含，午餐时间（约1小时）在附近餐厅自行点单结账即可。除餐食外，当地没有任何额外费用。"),
        ("Q7. 取消退款规定？", "以出行日为准，提前3天及之前通知：100%全额退款。以出行日为准，提前2天至当天通知：不可退款。※ 出行日以当地（日本）时间为准。"),
        ("Q8. 薰衣草什么时候最好看？", "通常6月底到8月初是盛花期，开花时间会因当年天气有所浮动。即使过了薰衣草季，四季彩之丘整个夏天都有应季花卉，任何时间都能欣赏花田。"),
    ],
    "faq_closing": "■ 如有其他疑问，请随时咨询",
    "pickup_radius_km": 3,
    "minimum_departure": 4,
    "included_ticket": "四季彩之丘门票",
    "refund_summary": "以出行日为准，提前3天及之前通知：100%全额退款。以出行日为准，提前2天至当天通知：不可退款。※ 出行日以当地（日本）时间为准。不成团也无损退款。",
}

KR["editorial"] = {
    "page_title": "삿포로 출발 후라노·비에이 소그룹 1일 투어",
    "skip": "본문으로 바로가기",
    "hero_alt": "팜 토미타의 보랏빛 라벤더와 여름 꽃밭",
    "primary_cta": "일정과 포함 내용 보기",
    "secondary_cta": "먼저 픽업 범위 보기",
    "benefits_title": "아침의 수고를 덜고, 여름의 색에 더 오래",
    "benefits_intro": "결정에 필요한 네 가지 조건을 먼저 확인해 보세요.",
    "benefit_titles": ("숙소 앞 픽업", "4인 소그룹", "입장권 포함", "미성사 전액 환불"),
    "pain_title": "집합 장소를 찾아 뛰는 아침 대신",
    "pain_body": "전통적인 대형 버스 투어는 이른 시간에 지정 장소로 이동하고, 짧은 체류 시간에 맞춰 서둘러야 할 수 있습니다. 이 투어는 숙소 가까이에서 시작하고 소그룹 리듬으로 움직여 사진과 관람에 더 집중할 수 있습니다.",
    "people_alt": "후라노 꽃밭 사이를 걷는 여행객들",
    "pickup_title": "삿포로에서 시작하는 하루의 동선",
    "pickup_intro": "정확한 내비게이션 지도가 아닌, 하루의 이동 순서를 보여 주는 안내도입니다.",
    "route_label": "삿포로에서 후라노와 비에이를 거쳐 돌아오는 안내 동선",
    "route_stops": ("삿포로", "팜 토미타", "사계채의 언덕", "청의 호수", "시라히게 폭포", "삿포로 귀환"),
    "itinerary_title": "예정 시간을 따라 읽는 여덟 장면",
    "itinerary_intro": "관광과 이동 시간을 함께 확인하세요. 당일 도로 상황에 따라 시간은 앞뒤로 달라질 수 있습니다.",
    "tomita_note": "이 페이지의 가장 선명한 장면. 약 60분 동안 라벤더 밭을 자유롭게 둘러봅니다.",
    "road_label": "차창으로 이어지는 제트코스터 로드의 오르내림",
    "road_note": "차창 감상 구간 · 하차 없음",
    "included_badge": "입장권 포함",
    "lunch_note": "라벤더 소프트크림은 현지에서 선택할 수 있는 간식 예시이며, 점심이나 투어 포함 식사는 아닙니다.",
    "softserve_alt": "팜 토미타의 라벤더 소프트크림",
    "shikisai_alt": "사계채의 언덕에 펼쳐진 여러 색의 꽃밭",
    "blue_pond_alt": "자작나무 사이로 보이는 비에이 청의 호수",
    "shirahige_alt": "비에이 강으로 흘러내리는 시라히게 폭포",
    "included_title": "포함 범위와 현장 운영",
    "included_heading": "포함",
    "included_items": ("사계채의 언덕 입장권",),
    "not_included_heading": "불포함",
    "not_included_items": ("식사", "개인 소비"),
    "service_heading": "차량과 안내",
    "service_items": (
        "당일 성사 인원에 맞춰 승합차를 배차합니다.",
        "일본어·영어 가능 기사와 번역 앱을 지원합니다.",
        "주요 지점에서 짧게 안내한 뒤 자유롭게 관람합니다.",
    ),
    "cancellation_title": "계획이 바뀔 때의 환불 기준",
    "refund_early_title": "여행일 3일 전까지",
    "refund_early_body": "통보 시 100% 전액 환불",
    "refund_late_title": "여행일 2일 전부터 당일까지",
    "refund_late_body": "통보 시 환불 불가",
    "formation_title": "4인 미성사",
    "formation_body": "미리 안내 후 수수료 없이 전액 환불",
    "weather_title": "안전상 운행 불가한 악천후",
    "weather_body": "출발 전 안내 후 전액 환불",
    "local_time_note": "여행일은 현지 일본 시각을 기준으로 합니다.",
    "closing_title": "마지막까지, 조건은 선명하게",
    "closing_body": "소그룹의 리듬으로 후라노와 비에이의 여름을 만나고, 돌아오는 길까지 부담을 덜어 보세요.",
    "guarantees": ("4인 소그룹", "삿포로역 3km 내 숙소 픽업", "미성사 시 전액 환불"),
    "closing_itinerary": "일정 다시 보기",
    "back_to_top": "맨 위로",
    "sources": "사진 출처와 라이선스",
    "route_disclaimer": "노선 개요 · 실제 운행 경로와 다를 수 있습니다.",
}

ZH["editorial"] = {
    "page_title": "札幌出发 富良野·美瑛小团一日游",
    "skip": "跳到正文",
    "hero_alt": "富田农场紫色薰衣草与夏日花田",
    "primary_cta": "查看行程与包含内容",
    "secondary_cta": "先看接送范围",
    "benefits_title": "少一点清晨奔波，多一点北海道夏色",
    "benefits_intro": "先看清决定是否适合您的四个条件。",
    "benefit_titles": ("住宿门口接送", "4人小团", "门票已包含", "不成团全额退款"),
    "pain_title": "不用一早赶去集合点",
    "pain_body": "传统大巴团通常需要清晨前往固定集合点，并在紧凑的停留节奏里匆忙拍照。这个行程从住宿附近开始，以小团节奏移动，把更多注意力留给拍照和游览。",
    "people_alt": "游客走在富良野花田之间",
    "pickup_title": "从札幌出发的一日动线",
    "pickup_intro": "这不是精确导航地图，而是帮助理解当天移动顺序的路线示意。",
    "route_label": "从札幌前往富良野和美瑛后返回的路线示意",
    "route_stops": ("札幌", "富田农场", "四季彩之丘", "青池", "白须瀑布", "返回札幌"),
    "itinerary_title": "沿预计时间阅读八段旅程",
    "itinerary_intro": "请同时查看游览与移动时间。当天时间可能会因路况前后浮动。",
    "tomita_note": "全页最鲜明的一幕。约60分钟自由欣赏薰衣草花田。",
    "road_label": "从车窗看云霄飞车之路上下延伸",
    "road_note": "车窗观赏路段·不下车",
    "included_badge": "门票包含",
    "lunch_note": "薰衣草冰淇淋只是当地可自由选择的点心示例，不代表午餐或任何餐食包含在团费内。",
    "softserve_alt": "富田农场薰衣草冰淇淋",
    "shikisai_alt": "四季彩之丘多彩花田",
    "blue_pond_alt": "白桦树之间的美瑛青池",
    "shirahige_alt": "流入美瑛川的白须瀑布",
    "included_title": "费用范围与现场服务",
    "included_heading": "包含",
    "included_items": ("四季彩之丘门票",),
    "not_included_heading": "不包含",
    "not_included_items": ("餐食", "个人消费"),
    "service_heading": "车辆与服务",
    "service_items": (
        "按当天成团人数安排商务车。",
        "提供日语/英语司机与翻译app支持。",
        "抵达主要景点后做简短说明，再自由参观。",
    ),
    "cancellation_title": "计划变化时的退款标准",
    "refund_early_title": "出行日前3天及之前",
    "refund_early_body": "通知可100%全额退款",
    "refund_late_title": "出行日前2天至当天",
    "refund_late_body": "通知不可退款",
    "formation_title": "未达到4人成团",
    "formation_body": "提前通知，并免手续费全额退款",
    "weather_title": "恶劣天气导致安全上无法成行",
    "weather_body": "出发前通知并全额退款",
    "local_time_note": "出行日以当地（日本）时间为准。",
    "closing_title": "到最后，条件依然清楚",
    "closing_body": "以小团节奏走进富良野与美瑛的夏天，也让回程更轻松。",
    "guarantees": ("4人小团", "札幌站3km内住宿接送", "不成团全额退款"),
    "closing_itinerary": "再看行程",
    "back_to_top": "返回顶部",
    "sources": "照片来源与许可",
    "route_disclaimer": "路线概览·可能与实际行车路径不同。",
}


def build_all(output_dir: Path) -> dict[str, str]:
    """Render the Chinese, Korean, and bilingual pages into *output_dir*."""
    from tools.furano_renderer import render_bilingual, render_single

    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "zh": ("index.html", render_single(ZH, "zh-CN")),
        "kr": ("wireframe_kr.html", render_single(KR, "ko")),
        "bi": ("bilingual.html", render_bilingual(KR, ZH)),
    }
    for _, (filename, html) in outputs.items():
        (output_dir / filename).write_text(html, encoding="utf-8", newline="\n")
    return {key: filename for key, (filename, _) in outputs.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "furano",
        help="Output directory (default: <repo>/furano)",
    )
    args = parser.parse_args()
    written = build_all(args.output)
    for key, filename in written.items():
        print(f"Wrote {key}: {args.output / filename}")


if __name__ == "__main__":
    main()
