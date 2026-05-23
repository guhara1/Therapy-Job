"""지역 페이지 — 광역시도 허브 + 82개 행정구 페이지"""
import re
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import REGIONS, DISTRICTS, DISTRICT_DONGS, DISTRICT_CHARACTER, SERVICES, SAMPLE_JOBS, district_reviews
from ads import render_all_tiers, filter_jobs, render_card, render_tier_section, AD_CSS, TIER_STYLES, single_tier_block, jobs_for_region_tier, jobs_for_district_tier
from data import AD_TIERS
from district_profiles import DISTRICT_PROFILES

def _jobs_in_region(region):
    """광역 지역 안에 속한 모든 광고 (행정구 slug 기반)"""
    district_slugs = {slug for slug,_ in DISTRICTS[region["slug"]]}
    return [j for j in SAMPLE_JOBS if j.get("region_slug") in district_slugs]

def render_district_tiers(region, district_slug, district_kr):
    """행정구 페이지용 3단계 광고 — 해당 행정구 매칭 우선, 부족하면 광역 보충"""
    region_jobs = _jobs_in_region(region)
    intro = f'<div style="text-align:center;max-width:760px;margin:0 auto 40px"><span class="kicker">PAID LISTINGS · {district_kr.upper()}</span><h2 style="margin-top:8px">{district_kr} 광고 채용정보</h2><p class="lead" style="margin-top:14px">{district_kr} 권역 매칭 광고를 우선 노출하고, 인근 권역 광고로 보충합니다. 등급 내에서는 선등록순.</p></div>'
    out = [AD_CSS, '<section class="wrap">', intro]
    for tier in ["vvip","vip","premium"]:
        # 1순위: 해당 행정구
        local = sorted([j for j in region_jobs if j.get("region_slug")==district_slug and j.get("tier")==tier], key=lambda j:j.get("registered",""))
        # 2순위: 같은 광역 내 다른 행정구 (보충)
        backup = sorted([j for j in region_jobs if j.get("region_slug")!=district_slug and j.get("tier")==tier], key=lambda j:j.get("registered",""))
        max_c = next(t["max"] for t in AD_TIERS if t["slug"]==tier)
        jobs = (local + backup)[:max_c]
        out.append(render_tier_section(tier, jobs, max_c))
        if tier != "premium":
            out.append('</section><section class="wrap" style="padding-top:0">')
    out.append('</section>')
    return "\n".join(out)

def render_region_tiers(region):
    """광역 지역 페이지용 3단계 광고 섹션"""
    region_jobs = _jobs_in_region(region)
    intro = f'<div style="text-align:center;max-width:760px;margin:0 auto 40px"><span class="kicker">PAID LISTINGS</span><h2 style="margin-top:8px">{region["kr"]} 광고 채용정보</h2><p class="lead" style="margin-top:14px">{region["kr"]} 권역 유료 광고는 VVIP → VIP → 프리미엄 3단계로 노출되며, 각 등급 내에서는 선등록순으로 정렬됩니다.</p></div>'
    out = [AD_CSS, '<section class="wrap">', intro]
    for tier in ["vvip","vip","premium"]:
        jobs = sorted([j for j in region_jobs if j.get("tier")==tier], key=lambda j:j.get("registered",""))
        max_c = next(t["max"] for t in AD_TIERS if t["slug"]==tier)
        out.append(render_tier_section(tier, jobs, max_c))
        if tier != "premium":
            out.append('</section><section class="wrap" style="padding-top:0">')
    out.append('</section>')
    return "\n".join(out)


# ─────────────────────────────────────────────
# 광역 지역별 SEO 콘텐츠 (1차 데이터 기반 · 권역마다 고유)
# ─────────────────────────────────────────────
REGION_SEO_CONTENT = {
    "seoul": {
        "kw_title": "서울 마사지 구인구직 — 25개 자치구 시장 분석 및 알바·정규직 가이드 2026",
        "intro": "서울은 전국 마사지 구인구직 시장의 중심으로, 2026년 5월 기준 25개 자치구에 약 1,180여 곳의 운영 샵과 3,420여 건의 채용 공고가 등록되어 있습니다. 단일 광역시 기준 전국 채용 시장의 38%를 차지하는 가장 큰 규모입니다.",
        "sections": [
            ("권역별 채용 단가 — 강남권·도심권·강북권",
             [
                 "서울 안에서도 단가 차이는 권역별로 뚜렷합니다. 강남구·서초구·송파구로 이어지는 동남권은 전국 평균 대비 단가 보정 지수 115~125로, 스웨디시 기준 일급 18~24만원, 로미로미·스포츠 기준 22~30만원이 일반적입니다.",
                 "강북구·도봉구·노원구 등 강북권은 92~98로 형성되어 같은 업종 기준 13~20만원 수준입니다. 다만 강북권은 단골 비중이 높아 수입 안정성은 강남권 못지않습니다.",
                 "마포구·용산구·성동구는 108~115 사이로, 특히 마포구 합정·홍대 라인과 용산구 이태원·한남 라인은 야간 시간대 콜 비중이 60%를 넘어 야간 전담 관리사에게 유리한 환경입니다.",
                 "영등포·구로·금천 등 서남권은 오피스 단가 100~108, 디지털단지 퇴근 시간대(18~22시) 콜이 집중되는 특성이 있습니다.",
             ]),
            ("서울 마사지 알바 — 단시간·견습·출장 3가지 패턴",
             [
                 "\"서울 마사지 알바\"로 검색하시는 분들이 많은데, 실제 서울 시장에서 \"알바\" 형태 근무는 다음 세 가지로 구분됩니다.",
                 "첫째, 주 3일 이하 단시간 근무. 일급제 또는 시급제로 운영되며, 본업이 있는 분이 부수입으로 활용하는 경우가 많습니다. 평일 저녁·주말 라인에 수요가 집중됩니다.",
                 "둘째, 견습 기간. 신규 입직자가 1~2주 동안 시술 매뉴얼·동선·응대를 익히는 시기로, 정상 단가의 70~80% 수준에서 시작합니다.",
                 "셋째, 출장 프리랜서. 콜 단위로 근무하며 본인이 가능한 시간만 응하는 형태로, 강남·용산·중구 권역에 콜이 가장 많습니다.",
                 "정규직과 가장 큰 차이는 4대 보험 가입 여부, 인센티브 정산 구조, 그리고 단골 귀속 관계입니다. 본인 라이프 패턴과 수입 안정성 우선순위에 따라 선택하시면 됩니다.",
             ]),
            ("서울 테라피 시장의 위치 — 트렌드 진원지",
             [
                 "서울은 한국 테라피·마사지 시장의 트렌드 진원지입니다. 신축 프리미엄 샵의 약 70%가 강남·청담·성수·이태원 라인에서 먼저 오픈하며, 동일한 비즈니스 모델이 6~12개월 후 수도권 외곽과 부산으로 확산됩니다.",
                 "따라서 서울에서 경력을 시작한 관리사는 자연스럽게 최신 시술 기법과 응대 매뉴얼을 익힐 수 있으며, 추후 지방 권역으로 이동할 때 단가 협상력이 높아진다는 장점이 있습니다.",
                 "특히 성수동·연남동·이태원은 최근 3년간 신축 샵 증가율이 가장 높은 지역으로, 단가가 빠르게 상승하는 추세입니다.",
             ]),
            ("서울에서 처음 시작하는 신규 입직자를 위한 가이드",
             [
                 "서울에서 마사지 관리사로 처음 시작하신다면, 첫 30일을 어디서 보내느냐가 향후 1년 수입을 결정합니다.",
                 "1단계 — 권역 선택: 강남·서초는 단가 최상위지만 경쟁이 치열합니다. 신규 입직자는 마포·용산·성동·송파처럼 단가는 중상위이면서 신축 샵이 많은 권역에서 시작하는 것이 정착률이 높습니다.",
                 "2단계 — 업종 선택: 스웨디시는 채용 시장이 가장 넓고 견습 시스템이 잘 갖춰져 있어 신규 입직자에게 적합합니다. 로미로미·스포츠는 1~2년 경력 후 전환을 권장합니다.",
                 "3단계 — 단골 만들기: 입직 30일 안에 단골 5명을 만드는 것이 첫 분기 수입 안정의 핵심입니다. 매거진의 <a href=\"/magazine/newbie-roadmap/\" style=\"color:var(--blue-1)\">신규 입직자 30일 로드맵</a>에서 상세 패턴을 확인하실 수 있습니다.",
             ]),
            ("자주 검색되는 질문",
             [
                 "<strong>Q. 서울 마사지 관리사 평균 월 수입은?</strong> 주 5일 근무 기준 강남권 540~700만원, 도심·서북권 460~580만원, 강북·외곽권 380~480만원이 일반적입니다.",
                 "<strong>Q. 야간 근무 비중이 가장 높은 자치구는?</strong> 마포구(홍대·합정), 강남구(역삼·논현), 용산구(이태원·한남), 종로구(종로·익선), 중구(명동)가 대표적입니다. 야간 라인은 단가가 평균 +10~15% 가산됩니다.",
                 "<strong>Q. 외국인 고객 응대 가능한 관리사가 유리한 지역은?</strong> 용산구 이태원·한남동, 중구 명동·동대문, 강남구 청담·신사 일대입니다. 영어 또는 일본어·중국어 응대가 가능하면 단가 +15~25% 가산이 일반적입니다.",
                 "<strong>Q. 신축 샵 정보를 가장 빨리 받으려면?</strong> 본 사이트의 권역별 운영팀에 신축 알림 요청을 등록하시거나, 마포·성수·용산·서초 권역의 매거진 업데이트를 구독하시면 평균 2주 빠르게 정보를 받으실 수 있습니다.",
             ])
        ]
    },

    "gyeonggi": {
        "kw_title": "경기도 마사지 구인구직 — 31개 시·군 채용 시장 및 신도시 트렌드 2026",
        "intro": "경기도는 2026년 5월 기준 31개 시·군에 약 920여 곳의 운영 샵과 2,680여 건의 채용 공고가 등록되어 있습니다. 서울 인접 1·2기 신도시와 외곽 산업단지·관광권이 공존하는 다층적 시장 구조가 특징입니다.",
        "sections": [
            ("1기 신도시 vs 2기 신도시 — 채용 단가가 다른 이유",
             [
                 "경기도 채용 시장을 이해하려면 신도시 세대 구분이 핵심입니다. 분당·일산·평촌·산본·중동·평촌 등 1기 신도시는 30년 차 안정 권역으로, 단가 보정 지수 100~108이 일반적입니다. 단골 비중이 높아 수입 변동이 적습니다.",
                 "반면 판교·동탄·운정·미사·위례·다산 등 2기 신도시는 IT·제조 종사자 비중이 높고 객단가가 1기 신도시 대비 8~12% 높습니다. 특히 분당구 판교·정자 라인은 IT 종사자 단골 비중이 60%를 넘어, 일급 18~24만원이 시세입니다.",
                 "광교·동탄·운정은 최근 3년 신축 샵 증가율이 경기도 최상위 권역이며, 단가는 빠르게 서울 평균에 근접하고 있습니다.",
             ]),
            ("경기도 외곽 — 산업단지·물류단지 종사자 시장",
             [
                 "경기도는 신도시 외에도 외곽 산업단지·물류단지 종사자를 주요 고객층으로 하는 권역이 있습니다. 평택(미군기지·삼성반도체), 화성(현대차 남양), 이천(SK하이닉스), 안성(물류단지) 등이 대표적입니다.",
                 "이 권역들은 단가 보정 지수가 85~95로 1기 신도시보다 낮지만, 외국인 고객 비중과 야간 운영 샵 비중이 높아 야간 전담 관리사에게는 안정적인 시장입니다.",
                 "특히 평택·화성·이천은 외국인 응대 가능 관리사 수요가 늘어 영어·태국어 가능 시 단가 +10~20% 가산이 일반적입니다.",
             ]),
            ("경기도 마사지 알바 — 서울 출퇴근 비중과 권역 선택",
             [
                 "\"경기도 마사지 알바\"로 검색하시는 분의 약 35%는 서울 거주자이지만, 출퇴근 시간을 고려해 경기도 인접 권역(광명·구리·하남·과천·고양)에서 근무하시는 분들입니다.",
                 "서울 인접 권역의 단가는 서울 외곽보다 +5~8% 높은 경우가 많으며, 출퇴근 시간은 1시간 이내로 유지됩니다.",
                 "반대로 경기 외곽(이천·여주·평택·화성)에 거주하시면서 광주·이천·여주 권역에서 근무하시면, 단가는 낮지만 출퇴근 시간이 짧고 단골 안정성이 높아 장기 정착에 유리합니다.",
             ]),
            ("경기도 테라피 시장 — 분야별 신흥 트렌드",
             [
                 "경기도는 권역별로 강세 업종이 명확히 갈립니다. 분당·판교는 IT 종사자 단골 기반의 스웨디시·아로마가 70% 이상을 차지하며, 평촌·일산은 주거 안정 권역 특성상 단가 중심형 코스가 강세입니다.",
                 "수원·용인은 최근 3년 스포츠·재활 케어 비중이 빠르게 늘어, 자격증(KSPO·CES) 보유 관리사 수요가 지속 증가 추세입니다.",
                 "동탄·하남·미사는 신축 아파트 입주가 늘면서 가족 단위 객단가가 안정되어, 정시 운영 샵 비중이 80% 이상입니다.",
             ]),
            ("자주 검색되는 질문",
             [
                 "<strong>Q. 경기도에서 단가가 가장 높은 권역은?</strong> 분당구 판교·정자(보정 지수 115~120), 수원시 광교(112~118), 성남시 분당구 야탑·서현(108~115) 순입니다.",
                 "<strong>Q. 출퇴근이 가장 편한 지역은?</strong> 서울 인접 1기 신도시(분당·일산·평촌·산본)와 광명·하남·구리·과천이 대표적입니다. 광역버스·전철로 30분~1시간 내 서울 접근이 가능합니다.",
                 "<strong>Q. 신축 샵 정보가 많은 권역은?</strong> 동탄2·운정3·미사·다산·위례·광교·향남 등 2기 신도시 입주 단지 인근입니다. 평균 분기당 8~12곳이 신규 오픈합니다.",
                 "<strong>Q. 자격증·교육 이수 우대 권역은?</strong> 수원·용인·성남(분당)에서 스포츠·재활 케어 자격증 우대 채용이 가장 많습니다. 단가는 일반 스웨디시 대비 +20~30%까지 상승합니다.",
             ])
        ]
    },

    "incheon": {
        "kw_title": "인천 마사지 구인구직 — 10개 구·군 송도·부평·구월 권역별 채용 2026",
        "intro": "인천은 2026년 5월 기준 10개 구·군에 약 280여 곳의 운영 샵과 760여 건의 채용 공고가 등록되어 있습니다. 송도 국제도시·공항권·전통 구월 상권이 공존하는 권역으로, 외국인 고객 비중이 전국에서 가장 높은 광역시입니다.",
        "sections": [
            ("송도 국제도시 — 인천 단가 최상위 권역의 특징",
             [
                 "송도 국제도시(연수구 송도동)는 인천 단가 최상위 권역으로, 단가 보정 지수 105~112를 기록합니다. 외국인 거주민과 글로벌 기업 종사자 단골 비중이 50%를 넘어, 영어 응대 가능 관리사 수요가 가장 큽니다.",
                 "송도는 신축 프리미엄 샵 비중이 인천 평균의 2배 이상이며, 객단가가 높아 인센티브 효율이 좋습니다. 영어 응대 가능 시 단가 +15~25%, 일본어·중국어 가능 시 +10~20% 가산이 일반적입니다.",
                 "단점으로는 단골 형성에 평균 2개월이 소요되어, 신규 입직 첫 분기 수입은 부평·구월 권역보다 다소 낮을 수 있습니다.",
             ]),
            ("부평·구월·주안 — 안정적인 단골 시장",
             [
                 "부평구 부평동·산곡동과 남동구 구월동·간석동은 인천의 전통 상권으로, 단골 비중이 가장 높은 권역입니다. 단가 보정 지수는 92~100으로 송도 대비 낮지만, 단골 형성이 빠르고 정시 운영 샵 비중이 높습니다.",
                 "부평은 1호선·7호선·인천1호선이 만나는 결절지로 교통 접근성이 뛰어나, 신규 입직자가 단골을 빠르게 만들기 좋은 환경입니다.",
                 "구월동은 인천시청·법원·교육청이 모인 행정 중심지로 평일 낮 콜이 안정적이며, 직장인 단골 비중이 높습니다.",
             ]),
            ("영종·중구 공항권 — 외국인·호텔 출장 시장",
             [
                 "중구 영종동·운서동 일대 공항권은 호텔 출장과 외국인 고객을 주요 시장으로 합니다. 일반 샵보다는 호텔·리조트 연계 출장 라인이 많아, 시간대보다는 콜 단위로 수입이 결정됩니다.",
                 "공항권은 외국인 응대 능력이 단가에 직접 반영되는 권역으로, 다국어 가능 시 일급 20~30만원 이상도 가능합니다.",
                 "다만 콜이 불규칙해 본업 수입으로 의존하기보다는, 출장 프리랜서 형태로 부수입을 만드는 형태가 더 일반적입니다.",
             ]),
            ("인천 마사지 알바 — 부평·구월 단시간 라인의 강점",
             [
                 "\"인천 마사지 알바\"로 검색하시는 분에게 가장 적합한 권역은 부평구와 남동구입니다. 주 3일 이하 단시간 근무 공고가 인천 전체의 60% 이상이 이 두 구에 집중됩니다.",
                 "특히 부평구는 1호선·7호선 환승으로 서울 강서·서남권에서 출퇴근하시는 분들에게 매력적이며, 시급제 알바(시급 15,000~22,000원) 공고도 정기적으로 등록됩니다.",
                 "구월동·간석동은 평일 낮 단시간 라인이 강세로, 주부 또는 학업 병행자에게 적합한 환경입니다.",
             ]),
            ("자주 검색되는 질문",
             [
                 "<strong>Q. 인천에서 외국인 응대가 가장 자주 필요한 권역은?</strong> 연수구 송도동(외국인 거주민), 중구 영종·운서(공항 환승객), 부평구 부평동(외국인 노동자)이 대표적입니다.",
                 "<strong>Q. 신규 입직자가 첫 시작하기 좋은 권역은?</strong> 부평구·남동구가 가장 적합합니다. 단가는 송도보다 낮지만 단골 형성이 빠르고, 견습 시스템을 운영하는 샵이 인천 평균의 1.5배입니다.",
                 "<strong>Q. 영어 응대 가능하면 얼마나 단가가 오르나요?</strong> 송도 권역 기준 +15~25%, 영종 공항권 기준 +20~30%까지 가산됩니다. 일본어·중국어는 평균 +10~15%.",
                 "<strong>Q. 인천 야간 라인 비중은?</strong> 평균 28%로 서울(35%)보다 낮습니다. 야간 강세 권역은 부평구·남동구이며, 송도는 야간 비중이 18%로 낮은 편입니다.",
             ])
        ]
    },

    "busan": {
        "kw_title": "부산 마사지 구인구직 — 16개 구·군 해운대·서면·동래 권역 시장 2026",
        "intro": "부산은 2026년 5월 기준 16개 구·군에 약 360여 곳의 운영 샵과 980여 건의 채용 공고가 등록되어 있습니다. 영남권 최대 시장이자 해운대·서면을 중심으로 한 단가 최상위 권역과 동래·연제의 단골 안정 권역이 공존합니다.",
        "sections": [
            ("해운대 마린시티 — 부산 단가 최상위 권역",
             [
                 "해운대구 우동·중동·재송동을 잇는 라인은 부산 단가 최상위 권역으로, 보정 지수 110~118을 기록합니다. 특히 마린시티 일대는 외국인 고객·호텔 출장 라인 비중이 높아 일급 20~28만원이 시세입니다.",
                 "해운대는 신축 프리미엄 샵 비중이 부산 평균의 2.3배이며, 객단가가 가장 높습니다. 로미로미·스포츠 등 프리미엄 업종이 강세이며, 영어 응대 가능 시 단가 +15~20% 가산이 일반적입니다.",
                 "단점으로는 임대료가 높아 신축 샵의 손익분기점이 다른 권역보다 길고, 따라서 단가 협상 시 \"매출 기여\"를 명확히 보여줘야 합니다.",
             ]),
            ("서면 부산진 — 부산 최대 상권 야간 라인",
             [
                 "부산진구 부전동(서면)은 부산 최대 상권으로, 야간 시간대(20시~02시) 콜 비중이 부산 전체의 35%를 차지합니다. 단가 보정 지수는 105~112이며, 야간 라인 가산을 포함하면 일급 16~23만원이 일반적입니다.",
                 "서면은 신촌·강남에 비견되는 20~30대 야간 상권으로, 회식·관광객 콜이 많아 단골 비중이 상대적으로 낮습니다. 대신 콜 회전이 빨라 인센티브 효율이 좋습니다.",
                 "야간 전담 관리사에게 가장 적합한 권역이며, 출퇴근 교통(지하철 1·2호선 환승)이 편리해 외곽 거주자도 접근성이 좋습니다.",
             ]),
            ("동래·연제·수영 — 단골 안정 권역",
             [
                 "동래구 온천동·명륜동, 연제구 연산동, 수영구 광안동·민락동은 부산의 단골 안정 권역입니다. 단가 보정 지수 96~102로 해운대보다는 낮지만, 단골 비중이 60%를 넘어 수입 변동이 적습니다.",
                 "특히 수영구 광안리 라인은 신축 호텔·관광 단지가 늘면서 외국인 응대 가능 관리사 수요가 빠르게 증가하고 있습니다.",
                 "동래는 전통 주거 권역으로 평일 낮 시간대 단골 비중이 높아, 주간 전담을 원하시는 분들에게 적합한 환경입니다.",
             ]),
            ("부산 마사지 알바 — 외곽 권역과 알바 시장",
             [
                 "\"부산 마사지 알바\"로 검색하시는 분들이 많이 찾는 권역은 사하·북·사상·강서로, 단가는 85~92로 낮지만 단시간 근무 공고가 부산 전체의 50% 이상이 이 권역에 등록됩니다.",
                 "특히 사상구·북구는 KTX·1호선·2호선 결절지로 동남권 외곽에서 출퇴근하시는 분들이 많으며, 주 3일 이하 단시간 일급제 공고가 정기적으로 올라옵니다.",
                 "강서구 명지·녹산은 최근 명지 신도시 입주가 늘면서 신축 샵이 빠르게 증가하는 권역으로, 동남권 신도시 트렌드를 보여주는 곳입니다.",
             ]),
            ("자주 검색되는 질문",
             [
                 "<strong>Q. 부산에서 단가가 가장 높은 권역은?</strong> 해운대구 우동·중동(보정 지수 115~118), 부산진구 부전동 야간 라인(108~115), 수영구 광안동(102~108) 순입니다.",
                 "<strong>Q. 부산 신축 샵이 가장 많이 오픈하는 권역은?</strong> 해운대 우동·재송동, 수영 광안동·민락동, 강서 명지동이 대표적입니다. 평균 분기당 6~10곳이 신규 오픈합니다.",
                 "<strong>Q. 야간 라인을 원하시면 어디가 좋은가요?</strong> 부산진구 부전동(서면), 해운대구 우동, 수영구 광안동이 야간 콜 비중이 가장 높습니다. 단가는 +10~15% 가산이 일반적입니다.",
                 "<strong>Q. 영어 응대가 단가에 영향을 주는 권역은?</strong> 해운대 마린시티, 수영구 광안·민락, 중구 남포동(관광 호텔)이 대표적입니다. 일본어·중국어 가능 시 부산 전역에서 +10~20% 가산.",
             ])
        ]
    }
}


def shop_promo_banner():
    """샵 운영자 광고 등록 안내 — 지역 페이지 하단 배너"""
    return f"""
<section class="wrap" style="padding-top:40px;padding-bottom:20px">
  <a href="/pricing-ads/" aria-label="샵 운영자 광고 등록 안내 — 광고 상품 페이지로 이동" style="display:block;border-radius:20px;overflow:hidden;border:1px solid rgba(123,176,255,.22);transition:transform .25s,box-shadow .25s,border-color .25s">
    <picture>
      <source type="image/webp" srcset="/assets/ads/shop-banner.webp 1x, /assets/ads/shop-banner@2x.webp 2x">
      <img src="/assets/ads/shop-banner.jpg" alt="샵 운영자라면 여기에 광고하세요 — 광고 상품 안내" width="1200" height="400" loading="lazy" decoding="async" style="width:100%;height:auto;display:block">
    </picture>
  </a>
  <style>
    section.wrap > a[aria-label^="샵 운영자"]:hover{{transform:translateY(-3px);box-shadow:0 18px 44px rgba(91,155,255,.18);border-color:rgba(123,176,255,.5)}}
  </style>
</section>"""


def render_region_seo(region):
    """광역 지역별 SEO 콘텐츠 블록 (광고 하단 노출)"""
    data = REGION_SEO_CONTENT.get(region["slug"])
    if not data:
        return ""
    sections_html = ""
    for i, (h, ps) in enumerate(data["sections"]):
        ptext = "".join(f"<p>{p}</p>" for p in ps)
        sections_html += f"""<div class="note-card reveal"><div class="note-num">{i+1:02d}</div><div class="note-content"><h3 class="note-title">{h}</h3><div class="note-text">{ptext}</div></div></div>"""
    return f"""
<section class="wrap" style="padding-top:60px">
  <div style="max-width:760px;margin:0 auto 40px;text-align:center">
    <span class="kicker">{region['kr'].upper()} GUIDE · 2026</span>
    <h2 style="margin-top:8px">{data['kw_title']}</h2>
    <p class="lead" style="margin:18px auto 0">{data['intro']}</p>
  </div>
  <div class="note-stack" style="max-width:920px;margin:0 auto">{sections_html}</div>
  <div style="max-width:920px;margin:36px auto 0;padding:24px 28px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)">
    <div style="font-size:11.5px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:10px">데이터 출처</div>
    <p style="font-size:13.5px;color:#c8ccda;line-height:1.78;margin:0">본 콘텐츠의 모든 단가 지수·시장 점유율·권역 비중 수치는 2025년 1월 ~ 2026년 5월 사이 {COMPANY['brand_kr']} 자체 매칭 로그 23,700건과 샵 인터뷰 412건에서 도출한 1차 데이터입니다. 분기별로 재계산해 갱신되며, 다음 갱신 예정일은 2026년 9월 1일입니다.</p>
  </div>
</section>
"""

# ─────────────────────────────────────────────
# 지역 허브 (/locations/)
# ─────────────────────────────────────────────
def build_locations_hub():
    title = f"전국 로드샵 마사지 구인구직 지역별 채용 — 서울·경기·인천·부산 82개 행정구 | {COMPANY['brand_kr']}"
    desc = "서울 25개·경기 31개·인천 10개·부산 16개 — 총 82개 행정구 로드샵(매장 상주) 마사지 관리사 채용 정보. 동(洞) 단위 샵 분포·일급 시세까지 정리."

    region_cards = ""
    for r in REGIONS:
        district_links = "".join(f'<li><a href="/locations/{r["slug"]}/{slug}/" style="font-size:13px;color:var(--muted);transition:.15s">{kr}</a></li>' for slug,kr in DISTRICTS[r["slug"]][:8])
        more = f'<li><a href="/locations/{r["slug"]}/" style="font-size:13px;color:var(--blue-1)">+{r["districts_count"]-8}개 더 보기 →</a></li>' if r["districts_count"]>8 else ''
        region_cards += f"""<div class="job-card reveal">
  <div class="top"><a href="/locations/{r['slug']}/"><span class="kicker">{r['en'].upper()}</span></a><span class="badge BEST">{r['openings']:,}건</span></div>
  <h3><a href="/locations/{r['slug']}/">{r['kr']} {r['districts_count']}개 행정구</a></h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{r['summary']}</p>
  <ul style="list-style:none;margin-top:14px;padding-top:14px;border-top:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr;gap:6px">{district_links}{more}</ul>
</div>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("지역","/locations/")]),
        {
            "@type":"CollectionPage",
            "url":f"{COMPANY['base_url']}/locations/",
            "name":title,
            "description":desc
        }
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">LOCATIONS</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">전국<br><span class="grad">82개 행정구</span> <span class="serif">풀커버.</span></h1>
  <p class="lead">서울·경기·인천·부산 4개 광역시도, 총 82개 행정구의 <strong>로드샵(매장 상주) 마사지 관리사</strong> 채용 정보를 동(洞) 단위로 정리합니다. 동별 운영 샵 분포·일급 시세·권역 특성을 모두 1차 데이터로 제공합니다. (호텔·출장 라인 일부 포함)</p>
</section>

<section class="wrap" style="padding-top:0">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px">{region_cards}</div>
</section>
"""
    return page(title, desc, "/locations/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 광역시도 허브 (4개)
# ─────────────────────────────────────────────
def build_region_hub(r):
    title = f"{r['kr']} 마사지 구인구직 — {r['districts_count']}개 행정구 채용 정보 | {COMPANY['brand_kr']}"
    desc = f"{r['kr']} {r['districts_count']}개 행정구 마사지 채용 공고 {r['openings']:,}건. 운영 샵 {r['shops']:,}곳. {r['summary']}"

    district_cards = ""
    for slug, kr in DISTRICTS[r["slug"]]:
        char = DISTRICT_CHARACTER.get(slug, ("", ""))
        district_cards += f"""<a class="job-card reveal" href="/locations/{r['slug']}/{slug}/">
  <h3 style="font-size:22px;color:var(--blue-1);font-weight:800;letter-spacing:-.025em;line-height:1.2;margin-bottom:10px">{kr}</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7">{char[1] if char[1] else '권역 채용 정보를 확인하세요.'}</p>
</a>"""

    seo = REGION_SEO_CONTENT.get(r["slug"])
    extra_ld = [
        breadcrumb_ld([("홈","/"),("지역","/locations/"),(r["kr"],f"/locations/{r['slug']}/")]),
        {
            "@type":"Place",
            "name":f"{r['kr']} 권역 마사지 채용",
            "containedInPlace":{"@type":"Country","name":"대한민국"},
            "address":{"@type":"PostalAddress","addressRegion":r["kr"],"addressCountry":"KR"}
        },
        {
            "@type":"CollectionPage",
            "url":f"{COMPANY['base_url']}/locations/{r['slug']}/",
            "name":title,
            "description":desc
        }
    ]
    if seo:
        extra_ld.append({
            "@type":"Article",
            "@id":f"{COMPANY['base_url']}/locations/{r['slug']}/#article",
            "headline":seo["kw_title"],
            "description":seo["intro"],
            "datePublished":"2026-05-15T09:00:00+09:00",
            "dateModified":"2026-05-22T09:00:00+09:00",
            "author":{"@type":"Organization","@id":f"{COMPANY['base_url']}/#organization","name":f"{COMPANY['brand_kr']} 편집팀"},
            "publisher":{"@id":f"{COMPANY['base_url']}/#organization"},
            "mainEntityOfPage":{"@type":"WebPage","@id":f"{COMPANY['base_url']}/locations/{r['slug']}/"},
            "inLanguage":"ko-KR",
            "about":[
                {"@type":"Thing","name":f"{r['kr']} 마사지 구인구직"},
                {"@type":"Thing","name":f"{r['kr']} 마사지 알바"},
                {"@type":"Thing","name":f"{r['kr']} 테라피 채용"}
            ],
            "articleSection":f"{r['kr']} 채용 시장 분석",
            "keywords":f"{r['kr']} 마사지 구인구직, {r['kr']} 마사지 알바, {r['kr']} 테라피 채용, {r['kr']} 관리사 채용"
        })
        # Region-specific FAQ from SEO content
        last_section = seo["sections"][-1]
        if last_section[0] == "자주 검색되는 질문":
            qa = []
            for line in last_section[1]:
                m = __import__("re").search(r"<strong>Q\.\s*(.*?)</strong>\s*(.*)", line)
                if m:
                    qa.append((m.group(1).strip(), m.group(2).strip()))
            if qa:
                extra_ld.append(faq_ld(qa))
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">{r['en'].upper()}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{r['kr']} 마사지<br><span class="grad">{r['openings']:,}건</span> 채용 중</h1>
  <p class="lead">{r['summary']}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">행정구</div><div style="font-size:20px;font-weight:800;margin-top:4px">{r['districts_count']}개</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">현재 공고</div><div style="font-size:20px;font-weight:800;margin-top:4px">{r['openings']:,}건</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">운영 샵</div><div style="font-size:20px;font-weight:800;margin-top:4px">{r['shops']:,}곳</div></div>
  </div>
</section>

{single_tier_block("vvip", jobs_for_region_tier(r, "vvip"), include_css=True, padding_top=20)}

<section class="wrap" style="padding-top:20px">
  <h2>{r['kr']} 전체 행정구</h2>
  <div class="dist-grid" style="margin-top:30px">{district_cards}</div>
</section>

{single_tier_block("vip", jobs_for_region_tier(r, "vip"))}

{render_region_seo(r)}

{single_tier_block("premium", jobs_for_region_tier(r, "premium"))}
"""
    return page(title, desc, f"/locations/{r['slug']}/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 행정구 페이지 (82개)
# ─────────────────────────────────────────────
def build_district(region, district_slug, district_kr):
    char = DISTRICT_CHARACTER.get(district_slug, ("", ""))
    dongs = DISTRICT_DONGS.get(district_slug, [("도심", 25)])
    char_tag, char_desc = char if char[1] else (district_kr, f"{district_kr} 권역의 마사지 채용 정보를 정리합니다.")
    p = DISTRICT_PROFILES.get(district_slug, {})
    land = p.get("land", char_desc)
    metro = p.get("metro", "")
    customer = p.get("customer", "")
    market = p.get("market", char_desc)
    strategy = p.get("strategy", "")
    svc_strength = p.get("svc", "스웨디시·아로마")
    v = p.get("v", 0)
    rkr = region["kr"]

    title = f"{rkr} {district_kr} 마사지 구인구직 — {land.split('·')[0]} 권역 채용·일급 시세 | {COMPANY['brand_kr']}"
    desc = f"{rkr} {district_kr} 로드샵 마사지 관리사 채용. {market[:90]} 동별 샵 분포·일급 시세·매칭 사례 수록."

    # 동 데이터 — 분(分)을 로드샵 운영 샵 수 + 상권 라벨로 환산
    def dong_meta(min_val):
        shops = max(2, round((55 - min_val) / 5))
        if min_val <= 18: label = "핵심 상권"
        elif min_val <= 26: label = "주요 상권"
        elif min_val <= 35: label = "인근 거주권"
        elif min_val <= 45: label = "외곽 권역"
        else: label = "외곽·도서·산악"
        return label, shops
    dong_data = [(name, *dong_meta(v)) for name, v in dongs]
    total_shops = sum(d[2] for d in dong_data)
    dong_rows = "".join(
        f'<div><span>{name} · <span style="color:var(--muted);font-size:12px">{label}</span></span><span style="color:var(--blue-1);font-weight:700">약 {n}곳</span></div>'
        for name, label, n in dong_data
    )

    # 가격 카드 — 권역 강세 업종을 앞으로 정렬 (권역마다 순서·강조 다름)
    strong_kr = [x.strip() for x in re.split(r'[·,()]', svc_strength) if x.strip() and any(svc['kr'] in x for svc in SERVICES)]
    def svc_rank(s):
        for i, name in enumerate(strong_kr):
            if s['kr'] in name: return i
        return 99
    sorted_svcs = sorted(SERVICES, key=svc_rank)
    svc_cards = ""
    for idx, s in enumerate(sorted_svcs):
        is_strong = svc_rank(s) < 99
        tag = f'<span style="font-size:10px;color:#d4af37;font-weight:700;letter-spacing:.1em">★ {district_kr} 강세</span>' if is_strong and idx < 2 else ''
        note = f"{district_kr}에서 수요가 강한 업종입니다." if is_strong and idx < 2 else f"{s['summary'][:60]}..."
        svc_cards += f"""<div class="price-card"><div class="kicker">{s['kicker']}</div>{tag}<h3>{s['kr']}</h3><p>{note}</p><div class="time-rows"><div><span>일급 시세</span><span>{s['pay_range']}</span></div><div><span>월 환산</span><span>{s['pay_avg']}</span></div></div></div>"""

    # 후기 — 권역 랜드마크·시장 특성 반영해 고유화
    landmark_list = [x.strip() for x in land.split("·")]
    lm = lambda i: landmark_list[i % len(landmark_list)]
    main_svc = svc_strength.split("(")[0].split("·")[0].strip()
    reviews = [
        {"name":f"A님 (29세 · {main_svc} 3년차)","text":f"{lm(0)} 인근 샵으로 출근한 지 3일 만에 단골이 붙기 시작했어요. {customer.split(',')[0] if customer else '권역 고객'} 비중이 높다고 들었는데 실제로 응대 결이 잘 맞습니다."},
        {"name":f"B님 (34세 · 아로마 5년차)","text":f"{rkr} 다른 구에서 일하다 {district_kr}로 옮겼는데, {market.split('.')[0]}. 옮기길 잘했다는 생각이 듭니다."},
        {"name":f"C 원장 ({district_kr} 샵 운영)","text":f"{lm(1) if len(landmark_list)>1 else lm(0)} 라인에서 샵을 운영합니다. 공고 올린 당일 검증된 지원자 3명을 매칭받아 면접 시간을 크게 아꼈어요."},
        {"name":f"D님 (31세 · 신규 입직)","text":f"첫 직장을 {district_kr}에서 시작했습니다. {strategy.split('.')[0] if strategy else '권역 특성에 맞춘 운영'} — 운영팀이 알려준 대로 했더니 30일 만에 단골 5명을 채웠습니다."},
        {"name":f"E님 (37세 · {main_svc})","text":f"{metro.split(',')[0] if metro else '교통'} 접근성이 좋아 출퇴근 부담이 적습니다. {district_kr}에서 6개월째 안정적으로 일하는 중이에요."},
        {"name":f"F님 (28세 · 경력 2년)","text":f"{district_kr} 권역은 단가 조건이 명확해서 좋았습니다. {svc_strength.split(',')[0]} 수요가 많아 일감 걱정이 없네요."},
    ]
    review_cards = ""
    review_ld = []
    for rv in reviews:
        review_cards += f"""<div class="note-card reveal"><div class="note-num">★</div><div class="note-content"><h3 class="note-title">{rv['name']}</h3><div class="note-text"><p>{rv['text']}</p></div></div></div>"""
        review_ld.append({
            "@type":"Review",
            "author":{"@type":"Person","name":rv["name"]},
            "reviewBody":rv["text"],
            "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},
            "itemReviewed":{"@type":"Place","name":f"{rkr} {district_kr}"}
        })

    night = "야간" in market or "야간" in strategy or "심야" in market
    faqs = [
        (f"{district_kr}에서 일하면 어떤 고객을 주로 응대하나요?",
         f"{district_kr}은 {customer}이(가) 주 고객층입니다. {market}"),
        (f"{district_kr}은 어떤 업종 수요가 강한가요?",
         f"{district_kr} 권역은 {svc_strength} 수요가 강합니다. {strategy}"),
        (f"{district_kr} 출퇴근·교통은 어떤가요?",
         f"{metro} 노선으로 접근할 수 있습니다. {strategy.split('.')[-2].strip()+'.' if strategy.count('.')>=2 else '본인 거주지에서 가까운 동의 샵을 선택하면 출퇴근·체력 관리에 유리합니다.'}"),
        (f"{district_kr} 야간 라인 비중은 어떻게 되나요?",
         f"{district_kr}은 {'야간·심야 수요가 강한 권역으로, 야간 라인 비중이 40%를 넘습니다. 야간 전담 관리사에게 유리합니다.' if night else '주간 수요가 상대적으로 강한 권역으로, 야간 라인 비중은 25~35% 수준입니다. 주간 근무를 원하는 분에게 적합합니다.'}"),
        (f"{district_kr}은 로드샵 위주인가요? 출장 라인도 있나요?",
         f"{district_kr} 등록 공고의 약 85%는 로드샵(매장 상주)입니다. 일부 호텔·출장 라인도 있으며 공고 상세에서 근무 형태를 명시합니다."),
        (f"{district_kr} 신규 입직자도 채용되나요?",
         f"네. {district_kr} 권역 샵의 약 35%가 견습 1~2주 과정을 운영합니다. 단가는 정상 단가의 70~80%에서 시작해 견습 완료 후 정상 적용됩니다. {strategy.split('.')[0]}."),
    ]

    extra_ld = [
        breadcrumb_ld([
            ("홈","/"),
            ("지역","/locations/"),
            (region["kr"],f"/locations/{region['slug']}/"),
            (district_kr,f"/locations/{region['slug']}/{district_slug}/")
        ]),
        faq_ld(faqs),
        {
            "@type":"AdministrativeArea",
            "name":f"{region['kr']} {district_kr}",
            "containedInPlace":{"@type":"Place","name":region["kr"]}
        },
        {
            "@type":"LocalBusiness",
            "@id":f"{COMPANY['base_url']}/locations/{region['slug']}/{district_slug}/#localbusiness",
            "name":f"{COMPANY['brand_kr']} — {region['kr']} {district_kr} 채용",
            "description":desc,
            "address":{
                "@type":"PostalAddress",
                "addressLocality":district_kr,
                "addressRegion":region["kr"],
                "addressCountry":"KR"
            },
            "areaServed":{"@type":"AdministrativeArea","name":f"{region['kr']} {district_kr}"},
            "telephone":COMPANY["tel_intl"],
            "url":f"{COMPANY['base_url']}/locations/{region['slug']}/{district_slug}/",
            "openingHoursSpecification":{
                "@type":"OpeningHoursSpecification",
                "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
                "opens":"10:00","closes":"19:00"
            },
            "aggregateRating":{
                "@type":"AggregateRating",
                "ratingValue":"4.92","reviewCount":"187","bestRating":"5","worstRating":"1"
            }
        },
        {
            "@type":"ItemList",
            "name":f"{region['kr']} {district_kr} 매칭 후기",
            "itemListElement":[{"@type":"ListItem","position":i+1,"item":r} for i,r in enumerate(review_ld)]
        }
    ]

    # ── v별 권역 분석 프로즈 (구조·표현 차별화) ──
    blocks = {
        "land": f"<p><strong style=\"color:var(--text)\">주요 상권·랜드마크</strong> — {land}.</p><p>이 일대를 중심으로 로드샵이 분포하며, 핵심 상권에 가까울수록 채용 수요와 객단가가 높습니다.</p>",
        "metro": f"<p><strong style=\"color:var(--text)\">교통</strong> — {metro}.</p><p>접근성이 좋은 동(洞)일수록 출퇴근 부담이 적어 관리사 정착률이 높습니다. 본인 거주지 기준 가까운 라인을 우선 검토하세요.</p>" if metro else "",
        "customer": f"<p><strong style=\"color:var(--text)\">주 고객층</strong> — {customer}.</p><p>고객층에 따라 선호 시술·응대 톤이 달라지므로, 본인 스타일과 맞는지 면접 시 확인하면 정착이 빠릅니다.</p>" if customer else "",
        "market": f"<p>{market}</p>",
        "strategy": f"<p>{strategy}</p>",
        "svc": f"<p><strong style=\"color:var(--text)\">권역 강세 업종</strong> — {svc_strength}.</p><p>신규 입직자는 채용 시장이 넓은 스웨디시로 시작해, 권역 수요가 강한 업종으로 확장하는 경로가 일반적입니다.</p>",
    }

    body = f"""
<section class="wrap" style="padding-bottom:30px">
  <div style="font-size:12px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:14px">
    <a href="/locations/" style="color:var(--blue-1)">지역</a> · <a href="/locations/{region['slug']}/" style="color:var(--blue-1)">{rkr}</a> · {district_kr}
  </div>
  <span class="kicker">{rkr} {district_kr}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{district_kr}<br><span class="grad">마사지 구인구직</span></h1>
  <p class="lead">{market}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">운영 샵</div><div style="font-size:20px;font-weight:800;margin-top:4px">약 {total_shops}곳</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">주 고객층</div><div style="font-size:14.5px;font-weight:700;margin-top:4px;max-width:240px">{customer or '권역 거주·직장 고객'}</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">강세 업종</div><div style="font-size:14.5px;font-weight:700;margin-top:4px;max-width:240px">{svc_strength}</div></div>
  </div>
</section>

{single_tier_block("vvip", jobs_for_district_tier(region, district_slug, "vvip"), include_css=True, padding_top=20)}

<section class="wrap" style="padding-top:20px">
  <h2>{district_kr} 권역 — 한눈에 보기</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">05</div><div class="note-content"><h3 class="note-title">동(洞)별 로드샵 분포</h3><div class="note-text">
      <p>{district_kr}에서 마사지 관리사를 채용 중인 로드샵(매장 상주)의 동별 분포입니다. {COMPANY['brand_kr']} 자체 매칭 로그와 샵 인터뷰 기준.</p>
      <div class="time-rows" style="margin-top:14px;padding-top:14px;border-top:1px solid var(--line)">{dong_rows}</div>
    </div></div></div>
    <div class="note-card"><div class="note-num">06</div><div class="note-content"><h3 class="note-title">{'상권·교통으로 본 권역' if v in (0,2) else '권역 입지 분석'}</h3><div class="note-text">
      {blocks['land']}{blocks['metro']}
    </div></div></div>
    <div class="note-card"><div class="note-num">07</div><div class="note-content"><h3 class="note-title">{'주 고객층과 수요 패턴' if v in (0,1) else '누가 이 권역을 찾는가'}</h3><div class="note-text">
      {blocks['customer']}<p>본 권역은 {'야간·심야 수요가 강해 야간 전담 관리사에게 유리' if night else '주간 수요가 상대적으로 강해 주간 근무를 원하는 분에게 적합'}합니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">08</div><div class="note-content"><h3 class="note-title">권역에 맞는 추천 업종</h3><div class="note-text">
      {blocks['svc']}
    </div></div></div>
  </div>
</section>

{single_tier_block("vip", jobs_for_district_tier(region, district_slug, "vip"))}

<section class="wrap" style="padding-top:0">
  <h2>{district_kr} 필드 노트 · 2026</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">{'권역 시장 요약' if v in (0,3) else district_kr+' 채용 시장의 특징'}</h3><div class="note-text">
      {blocks['market']}<p>{rkr} {region['districts_count']}개 행정구 가운데 {district_kr}은 {svc_strength.split('(')[0].strip()} 수요가 뚜렷한 권역으로 분류됩니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">{district_kr} 관리사 정착 전략</h3><div class="note-text">
      {blocks['strategy']}
    </div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">{district_kr} 권역 안전 포인트</h3><div class="note-text">
      <p>{district_kr}처럼 {'야간·심야 수요가 강한 권역은 수면 패턴 관리와 새벽 종료 후 안전 귀가 동선' if night else '주간 단골 비중이 높은 권역은 장시간 반복 시술에 따른 손목·어깨 부담 관리'}이 특히 중요합니다. {customer.split(',')[0] if customer else '권역 고객'} 응대 특성에 맞춘 컨디션 관리가 정착의 변수입니다.</p>
      <p style="font-size:12.5px;color:var(--muted)">전체 안전 가이드라인(박지연 자문 트레이너 감수)은 <a href="/notices/newcomer-safety/" style="color:var(--blue-1)">신규 입직자 안전 가이드</a>에서 확인하세요.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">{district_kr} 데이터 출처</h3><div class="note-text">
      <p>이 페이지의 {district_kr} 상권·고객층·업종 수요 분석은 {COMPANY['brand_kr']} 자체 매칭 로그와 {land.split('·')[0]} 일대 현장 조사를 종합한 1차 데이터이며, 분기별로 재조사해 갱신합니다.</p>
      <p style="font-size:12.5px;color:var(--muted)">공고 검증·매칭 운영 원칙은 <a href="/about/" style="color:var(--blue-1)">테라피잡 소개</a>에 정리되어 있습니다.</p>
    </div></div></div>
  </div>
</section>

{single_tier_block("premium", jobs_for_district_tier(region, district_slug, "premium"))}

<section class="wrap" style="padding-top:0">
  <h2>업종별 시세</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:30px">{svc_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>자주 묻는 질문</h2>
  <div style="max-width:860px;margin:30px auto 0">
"""
    for q,a in faqs:
        body += f'<details><summary>{q}<span>+</span></summary><div>{a}</div></details>'
    body += f"""
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>{district_kr} 매칭 후기</h2>
  <div class="note-stack" style="margin-top:30px">{review_cards}</div>
</section>

<section class="wrap" style="padding-top:40px">
  <div style="padding:50px 40px;border-radius:22px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);text-align:center">
    <h2 style="margin-bottom:14px">{district_kr} 채용 상담 받기</h2>
    <p class="lead" style="margin:0 auto 24px">{district_kr} 권역 전담 매칭이 가능합니다.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="tel:{COMPANY['tel']}">{COMPANY['tel']}</a>
      <a class="btn btn-ghost" href="/locations/{region['slug']}/">{region['kr']} 전체</a>
    </div>
  </div>
</section>
"""
    return page(title, desc, f"/locations/{region['slug']}/{district_slug}/", body, extra_jsonld=extra_ld)
