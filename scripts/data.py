"""테라피잡 데이터 모델 — 모든 페이지 생성을 위한 단일 소스"""

# ─────────────────────────────────────────────
# 회사 정보
# ─────────────────────────────────────────────
COMPANY = {
    "brand_kr": "테라피잡",
    "brand_en": "TherapyJob",
    "legal_name": "YH LAB",
    "ceo": "김수환",
    "biz_reg": "815-26-00585",
    "job_info_reg": "J1802020260002",
    "address": "경기도 파주시 청석로 268",
    "tel": "0508-202-4690",
    "tel_intl": "+82-508-202-4690",
    "tel_hours": "평일 10:00 ~ 19:00",
    "email": "help@therapyjob.club",
    "privacy_officer": "김수환",
    "domain": "therapyjob.club",
    "base_url": "https://therapyjob.club",
    "tagline_short": "전국 마사지 구인구직 1번지",
    "tagline_long": "샵과 관리사를 연결하는 가장 빠른 길.",
}

# ─────────────────────────────────────────────
# 업종 (5종)
# ─────────────────────────────────────────────
SERVICES = [
    {
        "slug": "swedish", "kr": "스웨디시", "en": "Swedish",
        "kicker": "OIL · 전신 릴렉스",
        "tag": "전국 채용 1위 업종",
        "pay_range": "일급 12만~22만원",
        "pay_avg": "월 380만~620만원",
        "openings": 1840,
        "summary": "전신 오일 트리트먼트의 대표 업종. 신규 입직자도 1주 교육으로 현장 투입 가능합니다.",
        "details": [
            "샵의 60% 이상이 스웨디시 메뉴를 기본으로 운영해, 채용 시장이 가장 넓습니다.",
            "초보자는 견습 1~2주, 경력자는 즉시 배차됩니다.",
            "프리랜서 계약이 일반적이며 인센티브 비율은 45~55% 사이가 시세입니다.",
        ],
        "skills": ["스트로크 5종", "에플라지·페트리사지", "오일 블렌딩 기초"],
    },
    {
        "slug": "aroma", "kr": "아로마", "en": "Aroma",
        "kicker": "ESSENTIAL · 향·심신",
        "tag": "감성 케어 강세",
        "pay_range": "일급 13만~24만원",
        "pay_avg": "월 400만~680만원",
        "openings": 1120,
        "summary": "에센셜 오일 블렌딩이 핵심. 디퓨저·향 설계 감각이 있는 분에게 유리합니다.",
        "details": [
            "프리미엄 라인 비중이 높아 단가가 상대적으로 높습니다.",
            "고정 단골 비율이 높아 안정적인 수입을 기대할 수 있습니다.",
            "야간보다 낮 시간대 예약이 많은 샵이 늘고 있어 라이프 패턴 선택지가 넓습니다.",
        ],
        "skills": ["블렌딩 차트", "차크라·림프", "톤타치 설계"],
    },
    {
        "slug": "thai", "kr": "타이", "en": "Thai",
        "kicker": "DRY · 스트레칭",
        "tag": "체력 좋은 분 환영",
        "pay_range": "일급 14만~26만원",
        "pay_avg": "월 420만~720만원",
        "openings": 760,
        "summary": "건식 스트레칭과 압. 라인콜로 시술량이 많아 체력 좋은 분께 적합합니다.",
        "details": [
            "건식 시술로 옷 갈아입는 시간이 짧아 회전이 빠릅니다.",
            "120분 코스 비중이 높아 객단가가 안정적입니다.",
            "태국 정통 라인은 별도 자격증을 우대하는 샵이 늘고 있습니다.",
        ],
        "skills": ["스트레칭 시퀀스", "압·체중 분산", "무릎·팔꿈치 활용"],
    },
    {
        "slug": "lomilomi", "kr": "로미로미", "en": "Lomi Lomi",
        "kicker": "HAWAII · 리듬케어",
        "tag": "프리미엄 라인",
        "pay_range": "일급 15만~28만원",
        "pay_avg": "월 450만~760만원",
        "openings": 380,
        "summary": "팔뚝·전완을 활용한 리듬 케어. 객단가가 가장 높은 프리미엄 라인입니다.",
        "details": [
            "교육 과정을 별도로 이수한 관리사를 선호하는 샵이 많습니다.",
            "1인당 시술 수는 적지만 단가가 높아 고정 수입이 안정적입니다.",
            "강남·청담·해운대 같은 럭셔리 상권에 채용이 집중됩니다.",
        ],
        "skills": ["하와이안 시퀀스", "전완·팔뚝 압", "호흡 동기화"],
    },
    {
        "slug": "sports", "kr": "스포츠", "en": "Sports",
        "kicker": "DEEP · 재활케어",
        "tag": "전문성 우대",
        "pay_range": "일급 16만~30만원",
        "pay_avg": "월 480만~820만원",
        "openings": 290,
        "summary": "근막·근육 회복 케어. KSPO·CES 등 자격증 우대 채용이 많습니다.",
        "details": [
            "재활·운동선수 케어 경험이 있으면 우대 폭이 큽니다.",
            "남성 고객 비중이 60% 이상으로 차분한 응대 역량이 필요합니다.",
            "낮 시간대 운영 샵이 많아 야간 근무가 어려운 분께 적합합니다.",
        ],
        "skills": ["근막 이완", "트리거 포인트", "수동 가동 범위 평가"],
    },
]

# ─────────────────────────────────────────────
# 매니저 국적 (6종)
# ─────────────────────────────────────────────
NATIONALITIES = [
    {
        "slug": "korean", "kr": "한국인", "en": "Korean",
        "flag_color": "#cd2e3a",
        "demand": "전국 평균 1.2배",
        "summary": "응대·소통이 매끄럽고 한국식 손기술이 강점. 모든 업종에서 가장 채용 수요가 높습니다.",
        "advantages": [
            "고객 응대·예약 변경 대응이 빠릅니다.",
            "사무 처리·매출 입력 등 부수 업무 적응이 빠릅니다.",
            "단골 관리에 능숙해 재방문율이 높습니다.",
        ],
        "common_pay": "일급 13만~25만원 (업종별 상이)",
    },
    {
        "slug": "chinese", "kr": "중국 동포·중국인", "en": "Chinese",
        "flag_color": "#de2910",
        "demand": "수도권 1.5배",
        "summary": "정통 추나·발마사지 기술 보유자가 많아, 타이·발마사지 라인에서 강세입니다.",
        "advantages": [
            "추나·지압 강도 조절이 정교합니다.",
            "장시간 시술 체력이 좋습니다.",
            "F-4·F-6 등 합법 체류 확인 시 채용이 빠릅니다.",
        ],
        "common_pay": "일급 12만~22만원",
    },
    {
        "slug": "thai", "kr": "태국인", "en": "Thai",
        "flag_color": "#a51931",
        "demand": "타이마사지 전문",
        "summary": "정통 태국 마사지의 본고장 출신. 라인콜이 많은 샵에서 선호합니다.",
        "advantages": [
            "스트레칭·압 시퀀스가 정통 와트포 스타일입니다.",
            "고객이 \"진짜 태국\" 경험을 원할 때 매칭 1순위입니다.",
            "E-9·H-2 등 합법 체류 우대.",
        ],
        "common_pay": "일급 14만~26만원",
    },
    {
        "slug": "vietnamese", "kr": "베트남인", "en": "Vietnamese",
        "flag_color": "#da251d",
        "demand": "최근 3년 채용 +220%",
        "summary": "차분한 응대와 정성스러운 손길로 단골 형성률이 높습니다.",
        "advantages": [
            "한국어 학습 의지가 높아 정착이 빠릅니다.",
            "근무 출퇴근 정시 준수율이 높습니다.",
            "팀워크 분위기에 잘 어울립니다.",
        ],
        "common_pay": "일급 11만~20만원",
    },
    {
        "slug": "russian", "kr": "러시아·CIS", "en": "Russian / CIS",
        "flag_color": "#0033a0",
        "demand": "프리미엄 라인",
        "summary": "외국인 고객·프리미엄 호텔 출장 라인에 강세. 영어 응대가 가능한 자원입니다.",
        "advantages": [
            "영어 응대로 외국인 고객 매칭 가능.",
            "스파·럭셔리 라인 경력자가 많습니다.",
            "체격이 좋아 딥티슈에 강점.",
        ],
        "common_pay": "일급 16만~30만원",
    },
    {
        "slug": "japanese", "kr": "일본인", "en": "Japanese",
        "flag_color": "#bc002d",
        "demand": "감성 라인 1순위",
        "summary": "섬세한 응대·청결도가 강점. 아로마·일식 리츄얼 라인에서 강세입니다.",
        "advantages": [
            "응대 매뉴얼 준수율이 가장 높습니다.",
            "도구·복장 청결 관리 우수.",
            "외국인 고객 응대도 가능합니다.",
        ],
        "common_pay": "일급 15만~28만원",
    },
]

# ─────────────────────────────────────────────
# 지역 데이터
# ─────────────────────────────────────────────
REGIONS = [
    {
        "slug": "seoul", "kr": "서울", "en": "Seoul",
        "districts_count": 25,
        "openings": 3420,
        "shops": 1180,
        "summary": "전국 채용 시장의 38%를 차지하는 최대 권역. 강남·서초·송파 라인이 단가 최상위입니다.",
    },
    {
        "slug": "gyeonggi", "kr": "경기", "en": "Gyeonggi",
        "districts_count": 31,
        "openings": 2680,
        "shops": 920,
        "summary": "수원·성남·고양·용인 등 1기 신도시 라인이 안정적이며, 평택·화성은 신축 샵이 늘고 있습니다.",
    },
    {
        "slug": "incheon", "kr": "인천", "en": "Incheon",
        "districts_count": 10,
        "openings": 760,
        "shops": 280,
        "summary": "송도·부평·구월 라인 채용이 활발합니다. 공항권은 외국인 고객 응대 가능자 우대.",
    },
    {
        "slug": "busan", "kr": "부산", "en": "Busan",
        "districts_count": 16,
        "openings": 980,
        "shops": 360,
        "summary": "해운대·서면 라인은 단가 최상위, 동래·연제는 단골 비중이 높습니다.",
    },
]

# 82개 행정구
DISTRICTS = {
    "seoul": [
        ("gangnam", "강남구"), ("gangdong", "강동구"), ("gangbuk", "강북구"),
        ("gangseo", "강서구"), ("gwanak", "관악구"), ("gwangjin", "광진구"),
        ("guro", "구로구"), ("geumcheon", "금천구"), ("nowon", "노원구"),
        ("dobong", "도봉구"), ("dongdaemun", "동대문구"), ("dongjak", "동작구"),
        ("mapo", "마포구"), ("seodaemun", "서대문구"), ("seocho", "서초구"),
        ("seongdong", "성동구"), ("seongbuk", "성북구"), ("songpa", "송파구"),
        ("yangcheon", "양천구"), ("yeongdeungpo", "영등포구"), ("yongsan", "용산구"),
        ("eunpyeong", "은평구"), ("jongno", "종로구"), ("jung", "중구"),
        ("jungnang", "중랑구"),
    ],
    "gyeonggi": [
        ("suwon", "수원시"), ("seongnam", "성남시"), ("goyang", "고양시"),
        ("yongin", "용인시"), ("bucheon", "부천시"), ("ansan", "안산시"),
        ("anyang", "안양시"), ("namyangju", "남양주시"), ("hwaseong", "화성시"),
        ("pyeongtaek", "평택시"), ("uijeongbu", "의정부시"), ("siheung", "시흥시"),
        ("paju", "파주시"), ("gimpo", "김포시"), ("gwangmyeong", "광명시"),
        ("gwangju-si", "광주시"), ("gunpo", "군포시"), ("hanam", "하남시"),
        ("osan", "오산시"), ("icheon", "이천시"), ("yangju", "양주시"),
        ("anseong", "안성시"), ("guri", "구리시"), ("pocheon", "포천시"),
        ("uiwang", "의왕시"), ("yeoju", "여주시"), ("yangpyeong", "양평군"),
        ("dongducheon", "동두천시"), ("gapyeong", "가평군"), ("gwacheon", "과천시"),
        ("yeoncheon", "연천군"),
    ],
    "incheon": [
        ("jung-gu", "중구"), ("dong-gu", "동구"), ("michuhol", "미추홀구"),
        ("yeonsu", "연수구"), ("namdong", "남동구"), ("bupyeong", "부평구"),
        ("gyeyang", "계양구"), ("seo-gu", "서구"), ("ganghwa", "강화군"),
        ("ongjin", "옹진군"),
    ],
    "busan": [
        ("jung-gu-busan", "중구"), ("seo-gu-busan", "서구"), ("dong-gu-busan", "동구"),
        ("yeongdo", "영도구"), ("busanjin", "부산진구"), ("dongnae", "동래구"),
        ("nam-gu", "남구"), ("buk-gu", "북구"), ("haeundae", "해운대구"),
        ("saha", "사하구"), ("geumjeong", "금정구"), ("gangseo-busan", "강서구"),
        ("yeonje", "연제구"), ("suyeong", "수영구"), ("sasang", "사상구"),
        ("gijang", "기장군"),
    ],
}

# 행정구별 동(洞) 샘플 (도착 시간 데이터용 — 각 행정구당 4~6개)
DISTRICT_DONGS = {
    "gangnam": [("역삼동", 14), ("삼성동", 18), ("논현동", 16), ("청담동", 20), ("대치동", 22), ("개포동", 26)],
    "gangdong": [("천호동", 18), ("길동", 22), ("둔촌동", 24), ("암사동", 28), ("성내동", 20)],
    "gangbuk": [("미아동", 26), ("수유동", 28), ("우이동", 32), ("번동", 24)],
    "gangseo": [("화곡동", 22), ("등촌동", 26), ("염창동", 24), ("가양동", 28), ("마곡동", 20)],
    "gwanak": [("신림동", 20), ("봉천동", 22), ("남현동", 26)],
    "gwangjin": [("자양동", 16), ("구의동", 18), ("중곡동", 22), ("화양동", 14)],
    "guro": [("구로동", 22), ("신도림동", 18), ("개봉동", 26), ("오류동", 28)],
    "geumcheon": [("가산동", 24), ("독산동", 26), ("시흥동", 30)],
    "nowon": [("상계동", 30), ("중계동", 28), ("하계동", 26), ("월계동", 24)],
    "dobong": [("창동", 28), ("쌍문동", 32), ("방학동", 30), ("도봉동", 34)],
    "dongdaemun": [("청량리동", 18), ("전농동", 20), ("답십리동", 22), ("장안동", 24)],
    "dongjak": [("상도동", 20), ("노량진동", 18), ("사당동", 22), ("흑석동", 24)],
    "mapo": [("합정동", 16), ("망원동", 18), ("성산동", 20), ("연남동", 14), ("상수동", 16)],
    "seodaemun": [("연희동", 18), ("홍은동", 24), ("남가좌동", 22), ("북아현동", 20)],
    "seocho": [("서초동", 14), ("반포동", 16), ("잠원동", 18), ("방배동", 20), ("양재동", 22)],
    "seongdong": [("성수동", 14), ("왕십리동", 16), ("금호동", 18), ("옥수동", 20)],
    "seongbuk": [("정릉동", 24), ("성북동", 22), ("길음동", 20), ("종암동", 22)],
    "songpa": [("잠실동", 14), ("문정동", 18), ("가락동", 20), ("방이동", 16), ("석촌동", 18)],
    "yangcheon": [("목동", 18), ("신정동", 22), ("신월동", 24)],
    "yeongdeungpo": [("여의도동", 14), ("당산동", 18), ("문래동", 20), ("영등포동", 16)],
    "yongsan": [("이태원동", 12), ("한남동", 14), ("후암동", 16), ("청파동", 18)],
    "eunpyeong": [("불광동", 24), ("응암동", 26), ("녹번동", 22), ("진관동", 30)],
    "jongno": [("종로1가", 14), ("청운동", 18), ("혜화동", 16), ("부암동", 22)],
    "jung": [("명동", 12), ("을지로동", 14), ("필동", 16), ("회현동", 14)],
    "jungnang": [("면목동", 22), ("상봉동", 20), ("중화동", 24), ("묵동", 26)],
    # 경기
    "suwon": [("영통동", 22), ("인계동", 18), ("권선동", 24), ("정자동", 20)],
    "seongnam": [("분당구 정자동", 18), ("수내동", 16), ("판교동", 20), ("야탑동", 22)],
    "goyang": [("일산동구 장항동", 22), ("일산서구 주엽동", 24), ("화정동", 20), ("백석동", 18)],
    "yongin": [("수지구 풍덕천동", 20), ("기흥구 보정동", 22), ("처인구 김량장동", 28)],
    "bucheon": [("중동", 18), ("상동", 20), ("부천동", 22), ("소사본동", 24)],
    "ansan": [("고잔동", 22), ("선부동", 24), ("사동", 26), ("부곡동", 28)],
    "anyang": [("평촌동", 18), ("범계동", 20), ("관양동", 22)],
    "namyangju": [("다산동", 24), ("호평동", 26), ("진접읍", 30), ("별내동", 22)],
    "hwaseong": [("동탄동", 22), ("향남읍", 28), ("봉담읍", 26)],
    "pyeongtaek": [("비전동", 26), ("팽성읍", 32), ("송탄", 28)],
    "uijeongbu": [("의정부동", 22), ("호원동", 24), ("민락동", 26)],
    "siheung": [("정왕동", 24), ("배곧동", 22), ("연성동", 26)],
    "paju": [("운정동", 26), ("교하동", 24), ("문산읍", 32)],
    "gimpo": [("장기동", 22), ("운양동", 24), ("사우동", 26)],
    "gwangmyeong": [("철산동", 18), ("하안동", 20), ("소하동", 24)],
    "gwangju-si": [("경안동", 26), ("오포읍", 28), ("초월읍", 32)],
    "gunpo": [("산본동", 20), ("당동", 22)],
    "hanam": [("미사동", 20), ("덕풍동", 22), ("신장동", 24)],
    "osan": [("오산동", 24), ("세교동", 26)],
    "icheon": [("창전동", 28), ("부발읍", 32)],
    "yangju": [("덕정동", 28), ("회천동", 30)],
    "anseong": [("공도읍", 30), ("당왕동", 28)],
    "guri": [("교문동", 20), ("인창동", 22)],
    "pocheon": [("소흘읍", 30), ("신읍동", 34)],
    "uiwang": [("내손동", 22), ("고천동", 24)],
    "yeoju": [("여흥동", 32), ("점동면", 38)],
    "yangpyeong": [("양평읍", 32), ("용문면", 38)],
    "dongducheon": [("생연동", 28), ("지행동", 30)],
    "gapyeong": [("가평읍", 36), ("청평면", 32)],
    "gwacheon": [("중앙동", 18), ("별양동", 20)],
    "yeoncheon": [("전곡읍", 38), ("연천읍", 42)],
    # 인천
    "jung-gu": [("운서동", 22), ("영종동", 24), ("신포동", 18)],
    "dong-gu": [("송림동", 22), ("화수동", 24)],
    "michuhol": [("주안동", 18), ("관교동", 20), ("학익동", 22)],
    "yeonsu": [("송도동", 20), ("연수동", 22), ("동춘동", 24)],
    "namdong": [("구월동", 18), ("간석동", 20), ("논현동", 22), ("만수동", 24)],
    "bupyeong": [("부평동", 18), ("산곡동", 20), ("부개동", 22)],
    "gyeyang": [("계산동", 22), ("작전동", 24)],
    "seo-gu": [("청라동", 22), ("검단동", 28), ("당하동", 26)],
    "ganghwa": [("강화읍", 42), ("길상면", 48)],
    "ongjin": [("북도면", 52), ("연평면", 60)],
    # 부산
    "jung-gu-busan": [("남포동", 18), ("광복동", 16)],
    "seo-gu-busan": [("아미동", 22), ("동대신동", 20)],
    "dong-gu-busan": [("초량동", 18), ("수정동", 20)],
    "yeongdo": [("동삼동", 24), ("청학동", 22)],
    "busanjin": [("부전동", 18), ("전포동", 20), ("양정동", 22)],
    "dongnae": [("온천동", 20), ("명륜동", 22), ("사직동", 24)],
    "nam-gu": [("대연동", 20), ("용호동", 24), ("문현동", 22)],
    "buk-gu": [("화명동", 24), ("덕천동", 26), ("구포동", 22)],
    "haeundae": [("우동", 16), ("좌동", 20), ("중동", 18), ("재송동", 22)],
    "saha": [("하단동", 24), ("괴정동", 22), ("당리동", 26)],
    "geumjeong": [("장전동", 24), ("부곡동", 26), ("구서동", 22)],
    "gangseo-busan": [("명지동", 26), ("녹산동", 32), ("대저동", 28)],
    "yeonje": [("연산동", 18), ("거제동", 20)],
    "suyeong": [("광안동", 16), ("민락동", 18), ("남천동", 20)],
    "sasang": [("괘법동", 22), ("주례동", 24), ("학장동", 26)],
    "gijang": [("기장읍", 32), ("정관읍", 36)],
}

# 행정구별 특징 (간단 키워드 — 페이지 차별화용)
DISTRICT_CHARACTER = {
    "gangnam": ("프리미엄 강세", "오피스 + 고급 주거가 결합한 최상위 단가 권역"),
    "gangdong": ("강동·하남 동선", "천호·둔촌 재건축과 함께 신축 샵이 늘고 있는 권역"),
    "gangbuk": ("주거 안정", "재방문 단골 비중이 높은 차분한 권역"),
    "gangseo": ("마곡 신흥", "마곡 업무지구 확장으로 점심·퇴근 시간대 콜이 늘고 있음"),
    "gwanak": ("서울대 인근", "젊은 1인 가구 비중이 높은 권역"),
    "gwangjin": ("건대·자양 동선", "20~30대 활동이 활발한 야간 강세 권역"),
    "guro": ("디지털단지 동선", "구로디지털·신도림 IT 종사자 콜이 많음"),
    "geumcheon": ("가산디지털 단지", "퇴근 시간대 IT 종사자 콜이 집중"),
    "nowon": ("학원·주거 권역", "주거 안정 권역으로 평일 낮 콜이 안정적"),
    "dobong": ("외곽 주거", "도착시간이 다소 길지만 단골 비중이 높음"),
    "dongdaemun": ("청량리·전농 동선", "구도심 재정비 권역으로 신축 샵 증가"),
    "dongjak": ("노량진·사당 동선", "교통 결절지로 권역 간 이동 콜이 많음"),
    "mapo": ("홍대·합정 동선", "20~30대 야간 콜이 가장 집중되는 권역"),
    "seodaemun": ("신촌·연희 동선", "대학가 + 주거 혼합 권역"),
    "seocho": ("법조·강남 인접", "강남 다음으로 단가가 높은 권역"),
    "seongdong": ("성수·서울숲 동선", "신흥 트렌드 권역, 객단가 상승 중"),
    "seongbuk": ("성북·길음 동선", "재정비 신축 + 전통 주거 혼합"),
    "songpa": ("잠실·문정 동선", "롯데월드타워·법조타운 + 신축 아파트 권역"),
    "yangcheon": ("목동 학원가", "주거 안정 권역으로 평일 낮 콜이 많음"),
    "yeongdeungpo": ("여의도 + 영등포", "오피스 + 신축 아파트가 결합한 권역"),
    "yongsan": ("이태원·한남 동선", "외국인 고객 콜이 가장 많은 권역"),
    "eunpyeong": ("연신내·불광 동선", "주거 안정 + 교통 결절지"),
    "jongno": ("도심 + 한옥마을", "관광 + 오피스 혼합 권역"),
    "jung": ("명동·을지로", "관광 + 호텔 콜이 집중되는 권역"),
    "jungnang": ("면목·상봉 동선", "주거 안정 권역으로 단골 비중이 높음"),
    "suwon": ("영통·인계 동선", "광교·영통 신도시 + 구도심 혼합"),
    "seongnam": ("판교·분당 동선", "IT 업종 종사자 콜이 가장 많은 권역"),
    "goyang": ("일산 동·서 라인", "1기 신도시 안정 권역"),
    "yongin": ("수지·기흥 동선", "분당 인접 신축 아파트 권역"),
    "bucheon": ("중동·상동 동선", "1기 신도시 + 송내 라인 안정"),
    "ansan": ("고잔·중앙 동선", "외국인 고객 비중이 높은 권역"),
    "anyang": ("평촌·범계 동선", "1기 신도시 안정 권역"),
    "namyangju": ("다산·별내 동선", "신축 신도시 콜이 증가"),
    "hwaseong": ("동탄 신도시", "2기 신도시 콜이 가장 빠르게 늘고 있음"),
    "pyeongtaek": ("미군기지·산업단지", "외국인 + 산업단지 종사자 콜"),
    "uijeongbu": ("의정부·민락 동선", "신축 아파트 권역으로 안정 콜"),
    "siheung": ("정왕·배곧 동선", "외국인 + 신도시 혼합 권역"),
    "paju": ("운정·교하 동선", "신도시 + LCD 산업단지"),
    "gimpo": ("장기·운양 동선", "한강신도시 안정 권역"),
    "gwangmyeong": ("철산·하안 동선", "서울 인접 안정 권역"),
    "gwangju-si": ("경안·오포 동선", "성남 인접 신흥 권역"),
    "gunpo": ("산본 신도시", "1기 신도시 안정 권역"),
    "hanam": ("미사·덕풍 동선", "스타필드·신축 아파트 권역"),
    "osan": ("오산·세교 동선", "신축 아파트 + 산업단지 혼합"),
    "icheon": ("부발·창전 동선", "물류단지 종사자 콜"),
    "yangju": ("회천·덕정 동선", "신축 아파트 안정 권역"),
    "anseong": ("공도·당왕 동선", "물류단지 + 신축 아파트"),
    "guri": ("교문·인창 동선", "서울 인접 안정 권역"),
    "pocheon": ("소흘·신읍 동선", "외곽 주거 안정 권역"),
    "uiwang": ("내손·고천 동선", "안양 인접 안정 권역"),
    "yeoju": ("여흥 도심", "외곽 주거 권역"),
    "yangpyeong": ("양평읍 중심", "전원·외곽 권역"),
    "dongducheon": ("생연·지행 동선", "신축 아파트 권역"),
    "gapyeong": ("가평·청평 동선", "관광·휴양 권역"),
    "gwacheon": ("정부청사 권역", "공무원 종사자 콜이 안정적"),
    "yeoncheon": ("전곡 도심", "외곽 권역"),
    "jung-gu": ("영종·송월 동선", "공항 + 신도시 혼합"),
    "dong-gu": ("송림·화수 동선", "재정비 진행 권역"),
    "michuhol": ("주안·관교 동선", "구도심 안정 권역"),
    "yeonsu": ("송도 국제도시", "신축 + 외국인 고객 권역"),
    "namdong": ("구월·간석 동선", "인천 행정 + 상권 중심"),
    "bupyeong": ("부평·산곡 동선", "1호선·7호선 교통 결절지"),
    "gyeyang": ("계산·작전 동선", "주거 안정 권역"),
    "seo-gu": ("청라·검단 동선", "신도시 콜이 빠르게 증가"),
    "ganghwa": ("강화 도심", "외곽·관광 권역"),
    "ongjin": ("도서 권역", "출장 가능 샵이 제한적"),
    "jung-gu-busan": ("남포·광복 동선", "관광·구도심 권역"),
    "seo-gu-busan": ("아미·동대신 동선", "재정비 진행 권역"),
    "dong-gu-busan": ("초량·수정 동선", "구도심 + 호텔 권역"),
    "yeongdo": ("동삼·청학 동선", "해안 권역"),
    "busanjin": ("서면 상권", "부산 최대 상권 + 야간 강세"),
    "dongnae": ("온천·명륜 동선", "전통 주거 + 단골 비중 높음"),
    "nam-gu": ("대연·용호 동선", "경성대·부경대 + 신축 아파트"),
    "buk-gu": ("화명·덕천 동선", "낙동강변 신축 아파트"),
    "haeundae": ("해운대·우동·좌동", "부산 최상위 단가 권역"),
    "saha": ("하단·괴정 동선", "외곽 주거 권역"),
    "geumjeong": ("부곡·장전 동선", "부산대 인근 권역"),
    "gangseo-busan": ("명지 신도시", "신축 아파트 콜이 늘고 있는 권역"),
    "yeonje": ("연산·거제 동선", "부산 행정 중심 권역"),
    "suyeong": ("광안·민락 동선", "광안리 + 마린시티 인접"),
    "sasang": ("주례·괘법 동선", "교통 결절지"),
    "gijang": ("기장·정관 동선", "신도시 + 외곽 권역"),
}

# ─────────────────────────────────────────────
# 매거진 글
# ─────────────────────────────────────────────
MAGAZINE = [
    {
        "slug": "regional-trend-2026-h1",
        "title": "2026 상반기 신축 마사지샵 트렌드 — 강남·판교·해운대·동탄 권역 분석",
        "summary": "16개월간 매칭 로그 23,700건과 2026년 1~5월 신축 오픈 64곳을 직접 교차 검증한 권역별 단가·트렌드 보고서.",
        "tag": "GUIDE · TREND",
        "minutes": 9,
        "date": "2026-05-25",
    },
    {
        "slug": "salary-guide-2026",
        "title": "2026 마사지 관리사 급여 가이드 — 업종·지역별 최신 시세",
        "summary": "스웨디시·아로마·타이·로미로미·스포츠 5종의 2026년 전국 평균 급여와 지역별 단가 차이를 정리합니다.",
        "tag": "GUIDE · SALARY",
        "minutes": 8,
        "date": "2026-05-10",
    },
    {
        "slug": "interview-tips",
        "title": "샵 면접에서 95% 합격한 관리사들의 공통점 7가지",
        "summary": "1,200건 면접 데이터에서 도출한, 합격률이 압도적으로 높은 관리사들의 공통 패턴.",
        "tag": "GUIDE · INTERVIEW",
        "minutes": 6,
        "date": "2026-04-22",
    },
    {
        "slug": "contract-checklist",
        "title": "프리랜서 계약 전 반드시 확인할 9가지",
        "summary": "인센티브 비율·정산 주기·세금 처리·교통비·복장 규정까지, 분쟁을 막는 체크리스트.",
        "tag": "GUIDE · CONTRACT",
        "minutes": 7,
        "date": "2026-04-08",
    },
    {
        "slug": "newbie-roadmap",
        "title": "신규 입직자를 위한 30일 로드맵 — 입사부터 첫 단골까지",
        "summary": "교육 1주, 견습 2주, 실전 1주 — 30일 안에 단골 5명을 만드는 단계별 가이드.",
        "tag": "GUIDE · NEWBIE",
        "minutes": 9,
        "date": "2026-03-25",
    },
    {
        "slug": "shop-vs-freelance",
        "title": "샵 소속 vs 출장 프리랜서, 무엇이 나에게 맞을까",
        "summary": "수입·근무 시간·안정성·세금 5개 축으로 두 방식을 비교 분석합니다.",
        "tag": "GUIDE · CAREER",
        "minutes": 7,
        "date": "2026-03-12",
    },
    {
        "slug": "safe-workplace",
        "title": "안전한 일터를 고르는 법 — 7가지 위험 신호",
        "summary": "면접·계약·근무 단계에서 미리 걸러야 할 위험 신호와 정상 샵의 공통 특징.",
        "tag": "GUIDE · SAFETY",
        "minutes": 6,
        "date": "2026-02-28",
    },
    {
        "slug": "newcomer-shop-guide",
        "title": "신규 오픈 샵을 어떻게 찾고, 어떻게 평가할까",
        "summary": "신축 샵 채용 정보를 빠르게 잡는 방법과, 첫 면접에서 확인해야 할 운영 시스템.",
        "tag": "GUIDE · NEW SHOP",
        "minutes": 7,
        "date": "2026-02-14",
    },
]

# ─────────────────────────────────────────────
# 광고 공고 — 3단계 (VVIP / VIP / 프리미엄)
# 같은 등급 내에서는 선등록순 정렬 (등록일 오름차순)
# ─────────────────────────────────────────────
SAMPLE_JOBS = [
    # ─── VVIP (최상단, 대형 카드, 최대 4건) ───
    {"id":"J26-3801","tier":"vvip","registered":"2026-05-18","title":"강남 프리미엄 스웨디시샵 정규 관리사","region":"서울 강남구 역삼동","region_slug":"gangnam","service":"swedish","pay":"일 18만~24만원","shop":"라움 스파","perks":["인센티브 55%","주 5일 · 야간","숙소 지원"],"hours":"14:00 ~ 24:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"일정산"},
    {"id":"J26-3812","tier":"vvip","registered":"2026-05-19","title":"청담동 럭셔리 스파 로미로미 채용","region":"서울 강남구 청담동","region_slug":"gangnam","service":"lomilomi","pay":"일 22만~30만원","shop":"엘리시안 스파","perks":["인센티브 50%","주간 전담","교통비 별도"],"hours":"11:00 ~ 22:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3825","tier":"vvip","registered":"2026-05-20","title":"해운대 마린시티 로미로미","region":"부산 해운대구 우동","region_slug":"haeundae","service":"lomilomi","pay":"일 20만~28만원","shop":"오션 테라피","perks":["일정산","외국인 고객 라인","숙소 지원"],"hours":"12:00 ~ 23:00","positions":4,"contract":"프리랜서 (3.3%)","settle":"일정산"},
    {"id":"J26-3833","tier":"vvip","registered":"2026-05-21","title":"분당 판교 아로마 전문 관리사","region":"경기 성남시 판교동","region_slug":"seongnam","service":"aroma","pay":"일 19만~26만원","shop":"파인 아로마","perks":["인센티브 52%","주정산","평일 낮 강세"],"hours":"10:00 ~ 22:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"주정산"},

    # ─── VIP (중단, 중형 카드, 6~8건) ───
    {"id":"J26-3841","tier":"vip","registered":"2026-05-15","title":"잠실 송파 타이마사지 경력 우대","region":"서울 송파구 잠실동","region_slug":"songpa","service":"thai","pay":"일 17만~26만원","shop":"실론 타이","perks":["인센티브 50%","주 5일"],"hours":"13:00 ~ 24:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3848","tier":"vip","registered":"2026-05-16","title":"성수동 신축 스포츠케어 관리사","region":"서울 성동구 성수동","region_slug":"seongdong","service":"sports","pay":"일 19만~28만원","shop":"리얼 리커버리","perks":["KSPO 우대","주간 라인"],"hours":"10:00 ~ 21:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3855","tier":"vip","registered":"2026-05-17","title":"송도 국제도시 스웨디시 정규","region":"인천 연수구 송도동","region_slug":"yeonsu","service":"swedish","pay":"일 15만~22만원","shop":"송도 웰니스","perks":["외국인 응대","주 5일"],"hours":"11:00 ~ 23:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3863","tier":"vip","registered":"2026-05-18","title":"홍대 합정 야간 아로마 관리사","region":"서울 마포구 합정동","region_slug":"mapo","service":"aroma","pay":"일 18만~25만원","shop":"문라이트 아로마","perks":["야간 전담","교통비 별도"],"hours":"18:00 ~ 04:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"일정산"},
    {"id":"J26-3871","tier":"vip","registered":"2026-05-19","title":"서면 부산진 스웨디시 즉시 출근","region":"부산 부산진구 부전동","region_slug":"busanjin","service":"swedish","pay":"일 16만~23만원","shop":"부산 라움","perks":["일정산","숙소 지원"],"hours":"12:00 ~ 24:00","positions":4,"contract":"프리랜서 (3.3%)","settle":"일정산"},
    {"id":"J26-3878","tier":"vip","registered":"2026-05-20","title":"수원 영통 신축 프리미엄 라인","region":"경기 수원시 영통동","region_slug":"suwon","service":"swedish","pay":"일 17만~24만원","shop":"광교 스파","perks":["주간 전담","주 5일"],"hours":"10:00 ~ 22:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"주정산"},

    # ─── 프리미엄 (하단, 컴팩트 카드, 등록 제한 없음) ───
    {"id":"J26-3902","tier":"premium","registered":"2026-05-10","title":"강서 화곡 스웨디시 주간 근무","region":"서울 강서구 화곡동","region_slug":"gangseo","service":"swedish","pay":"일 14만~20만원","shop":"화곡 테라피","perks":["주간"],"hours":"10:00 ~ 20:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3908","tier":"premium","registered":"2026-05-11","title":"부평 산곡 타이 경력 우대","region":"인천 부평구 산곡동","region_slug":"bupyeong","service":"thai","pay":"일 15만~22만원","shop":"부평 타이","perks":["주 5일"],"hours":"12:00 ~ 23:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3914","tier":"premium","registered":"2026-05-12","title":"일산 백석 아로마 관리사","region":"경기 고양시 백석동","region_slug":"goyang","service":"aroma","pay":"일 14만~21만원","shop":"일산 아로마","perks":["주간"],"hours":"11:00 ~ 22:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3919","tier":"premium","registered":"2026-05-13","title":"동래 온천동 스웨디시","region":"부산 동래구 온천동","region_slug":"dongnae","service":"swedish","pay":"일 13만~20만원","shop":"온천 스파","perks":["단골 인수"],"hours":"11:00 ~ 23:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3923","tier":"premium","registered":"2026-05-14","title":"노원 상계 야간 라인","region":"서울 노원구 상계동","region_slug":"nowon","service":"swedish","pay":"일 15만~21만원","shop":"상계 테라피","perks":["야간"],"hours":"18:00 ~ 03:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3927","tier":"premium","registered":"2026-05-15","title":"안양 평촌 스포츠 케어","region":"경기 안양시 평촌동","region_slug":"anyang","service":"sports","pay":"일 16만~22만원","shop":"평촌 스포츠","perks":["주간"],"hours":"10:00 ~ 21:00","positions":1,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3931","tier":"premium","registered":"2026-05-16","title":"용산 한남 외국인 라인","region":"서울 용산구 한남동","region_slug":"yongsan","service":"aroma","pay":"일 17만~24만원","shop":"한남 부티크","perks":["외국인 응대"],"hours":"12:00 ~ 23:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3935","tier":"premium","registered":"2026-05-17","title":"중구 명동 호텔 출장","region":"서울 중구 명동","region_slug":"jung","service":"swedish","pay":"일 16만~22만원","shop":"명동 스파","perks":["출장 라인"],"hours":"14:00 ~ 02:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"일정산"},
    {"id":"J26-3939","tier":"premium","registered":"2026-05-18","title":"광안리 수영 아로마","region":"부산 수영구 광안동","region_slug":"suyeong","service":"aroma","pay":"일 14만~21만원","shop":"광안 아로마","perks":["주간"],"hours":"11:00 ~ 22:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3943","tier":"premium","registered":"2026-05-19","title":"미사 하남 신축 샵","region":"경기 하남시 미사동","region_slug":"hanam","service":"swedish","pay":"일 15만~21만원","shop":"미사 웰니스","perks":["신축"],"hours":"10:00 ~ 22:00","positions":3,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3947","tier":"premium","registered":"2026-05-20","title":"구로 디지털단지 퇴근 라인","region":"서울 구로구 구로동","region_slug":"guro","service":"swedish","pay":"일 14만~20만원","shop":"구로 라움","perks":["야간"],"hours":"17:00 ~ 02:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
    {"id":"J26-3951","tier":"premium","registered":"2026-05-21","title":"동탄 신도시 프리미엄","region":"경기 화성시 동탄동","region_slug":"hwaseong","service":"aroma","pay":"일 16만~22만원","shop":"동탄 아로마","perks":["신축"],"hours":"11:00 ~ 22:00","positions":2,"contract":"프리랜서 (3.3%)","settle":"주정산"},
]

# 광고 등급 정의
AD_TIERS = [
    {
        "slug":"vvip","name":"VVIP 채용정보",
        "kicker":"TOP TIER · 최상단 노출",
        "desc":"메인 페이지 최상단 단독 노출 · 모든 페이지 헤더 배너 · PC·모바일 전용 위치",
        "order":"선등록순",
        "accent_color":"#d4af37",
        "border_color":"rgba(212,175,55,.4)",
        "max":4,
    },
    {
        "slug":"vip","name":"VIP 채용정보",
        "kicker":"PRIORITY · 우선 노출",
        "desc":"메인 페이지 두 번째 영역 노출 · PC·모바일 광고 위치 · 카테고리 페이지 상단",
        "order":"선등록순",
        "accent_color":"#7bb0ff",
        "border_color":"rgba(123,176,255,.4)",
        "max":12,
    },
    {
        "slug":"premium","name":"프리미엄 채용정보",
        "kicker":"STANDARD · 기본 노출",
        "desc":"메인 페이지 세 번째 영역 노출 · PC·모바일 광고 위치 · 등록 제한 없음",
        "order":"등록 제한 없음",
        "accent_color":"#a0a8be",
        "border_color":"rgba(160,168,190,.3)",
        "max":12,
    },
]

# ─────────────────────────────────────────────
# 공지사항 (/notices/)
# ─────────────────────────────────────────────
NOTICES = [
    {
        "slug":"southeast-asia-scam",
        "title":"동남아 해외 취업 사기 주의보 — 캄보디아·미얀마·라오스 사례 급증",
        "summary":"고액 일급을 미끼로 한 동남아 마사지·서비스업 취업 사기가 증가하고 있습니다. 항공권 무료·여권 압수·강제 노동·인신매매 위험이 확인되어 외교부·경찰청 합동 경보가 발령된 사안을 정리합니다.",
        "category":"안전",
        "category_color":"#ff6b6b",
        "priority":"긴급",
        "date":"2026-05-18",
        "minutes":7,
    },
    {
        "slug":"prostitution-monitoring",
        "title":"성매매업소 등록·노출 모니터링 강화 안내 (2026-05 시행)",
        "summary":"성매매방지법·청소년보호법·직업안정법에 따라 성매매·유사성행위를 암시하는 채용 공고와 광고를 영구 차단합니다. 검증 절차·신고 채널·법적 처벌 안내를 정리합니다.",
        "category":"법령",
        "category_color":"#7bb0ff",
        "priority":"중요",
        "date":"2026-05-12",
        "minutes":6,
    },
    {
        "slug":"newcomer-safety",
        "title":"신규 입직자 안전 가이드 — 첫 출근 전 반드시 확인할 7가지",
        "summary":"마사지 업종 신규 입직자가 첫 출근 전 반드시 확인해야 할 안전 체크리스트. 사업자등록증·계약서·인센티브 구조·신분증 보관 거부 등 분쟁의 80%를 사전에 차단할 수 있는 항목들입니다.",
        "category":"안전",
        "category_color":"#9fd9b8",
        "priority":"일반",
        "date":"2026-05-05",
        "minutes":5,
    },
    {
        "slug":"fraud-report-channel",
        "title":"부정 공고·광고 신고 채널 안내",
        "summary":"단가 과장·노동관계법령 위반·성매매 암시·미성년자 채용 시도 등 부정 공고를 발견하신 분을 위한 신고 채널과 후속 조치 절차를 안내합니다. 익명 신고가 가능하며 신고자는 보호됩니다.",
        "category":"운영",
        "category_color":"#d4af37",
        "priority":"일반",
        "date":"2026-04-28",
        "minutes":4,
    },
]


# ─────────────────────────────────────────────
# 업소 매매 샘플 매물 (/shop-sale/)
# ─────────────────────────────────────────────
SHOP_SALES = [
    {
        "id":"S26-001","status":"매매중","title":"강남 역삼동 프리미엄 스웨디시 스파 양도",
        "region_slug":"seoul","region_kr":"서울","district_slug":"gangnam","district_kr":"강남구",
        "location_sub":"역삼역 3번 출구 도보 5분",
        "service":"swedish","service_kr":"스웨디시",
        "size_pyeong":52,"deposit":5000,"key_money":8000,"total":13000,"rent":220,
        "monthly_revenue":"4,500 ~ 5,200만원","monthly_profit":"1,800 ~ 2,200만원",
        "registered":"2026-05-15","feature":"신규 인테리어 · 단골 65%",
    },
    {
        "id":"S26-002","status":"매매중","title":"홍대 합정 야간 아로마샵 양도",
        "region_slug":"seoul","region_kr":"서울","district_slug":"mapo","district_kr":"마포구",
        "location_sub":"합정역 7번 출구 도보 3분",
        "service":"aroma","service_kr":"아로마",
        "size_pyeong":38,"deposit":3000,"key_money":5000,"total":8000,"rent":180,
        "monthly_revenue":"3,200 ~ 3,800만원","monthly_profit":"1,200 ~ 1,500만원",
        "registered":"2026-05-16","feature":"야간 단골 유지 · 권리 보장",
    },
    {
        "id":"S26-003","status":"상담중","title":"잠실 송파 스포츠 케어샵 매매",
        "region_slug":"seoul","region_kr":"서울","district_slug":"songpa","district_kr":"송파구",
        "location_sub":"잠실새내역 인근 오피스권",
        "service":"sports","service_kr":"스포츠",
        "size_pyeong":42,"deposit":4000,"key_money":6000,"total":10000,"rent":200,
        "monthly_revenue":"3,800 ~ 4,200만원","monthly_profit":"1,500 ~ 1,800만원",
        "registered":"2026-05-12","feature":"KSPO 자격 트레이너 인계 가능",
    },
    {
        "id":"S26-004","status":"매매중","title":"분당 판교 IT단지 스웨디시 양도",
        "region_slug":"gyeonggi","region_kr":"경기","district_slug":"seongnam","district_kr":"성남시",
        "location_sub":"판교역 7번 출구 도보 7분",
        "service":"swedish","service_kr":"스웨디시",
        "size_pyeong":48,"deposit":3500,"key_money":5500,"total":9000,"rent":195,
        "monthly_revenue":"3,500 ~ 4,200만원","monthly_profit":"1,400 ~ 1,700만원",
        "registered":"2026-05-14","feature":"IT 단골 비중 70% · 평일 강세",
    },
    {
        "id":"S26-005","status":"매매중","title":"수원 영통 신축 아로마샵 양도",
        "region_slug":"gyeonggi","region_kr":"경기","district_slug":"suwon","district_kr":"수원시",
        "location_sub":"영통역 2번 출구 인근",
        "service":"aroma","service_kr":"아로마",
        "size_pyeong":35,"deposit":2500,"key_money":4000,"total":6500,"rent":150,
        "monthly_revenue":"2,800 ~ 3,300만원","monthly_profit":"1,100 ~ 1,300만원",
        "registered":"2026-05-13","feature":"신축 1년차 · 인테리어 양호",
    },
    {
        "id":"S26-006","status":"매매중","title":"송도 국제도시 로미로미 프리미엄 스파",
        "region_slug":"incheon","region_kr":"인천","district_slug":"yeonsu","district_kr":"연수구",
        "location_sub":"송도 센트럴파크 도보 5분",
        "service":"lomilomi","service_kr":"로미로미",
        "size_pyeong":55,"deposit":5000,"key_money":7000,"total":12000,"rent":230,
        "monthly_revenue":"4,200 ~ 5,000만원","monthly_profit":"1,700 ~ 2,100만원",
        "registered":"2026-05-11","feature":"외국인 단골 40% · 영어 응대",
    },
    {
        "id":"S26-007","status":"매매중","title":"해운대 마린시티 럭셔리 스파 매매",
        "region_slug":"busan","region_kr":"부산","district_slug":"haeundae","district_kr":"해운대구",
        "location_sub":"센텀시티역 인근 오션뷰",
        "service":"swedish","service_kr":"스웨디시",
        "size_pyeong":44,"deposit":5000,"key_money":7500,"total":12500,"rent":240,
        "monthly_revenue":"4,500 ~ 5,500만원","monthly_profit":"1,800 ~ 2,300만원",
        "registered":"2026-05-10","feature":"호텔 인접 · 외국인 고객",
    },
    {
        "id":"S26-008","status":"상담중","title":"서면 부산진 타이마사지샵 양도",
        "region_slug":"busan","region_kr":"부산","district_slug":"busanjin","district_kr":"부산진구",
        "location_sub":"서면역 2번 출구 도보 4분",
        "service":"thai","service_kr":"타이",
        "size_pyeong":32,"deposit":2000,"key_money":3500,"total":5500,"rent":130,
        "monthly_revenue":"2,200 ~ 2,800만원","monthly_profit":"900 ~ 1,200만원",
        "registered":"2026-05-09","feature":"야간 라인 · 회전율 우수",
    },
    {
        "id":"S26-009","status":"매매중","title":"강서 화곡 주간 스웨디시샵 양도",
        "region_slug":"seoul","region_kr":"서울","district_slug":"gangseo","district_kr":"강서구",
        "location_sub":"화곡역 4번 출구 도보 6분",
        "service":"swedish","service_kr":"스웨디시",
        "size_pyeong":28,"deposit":1500,"key_money":3000,"total":4500,"rent":120,
        "monthly_revenue":"2,000 ~ 2,500만원","monthly_profit":"800 ~ 1,000만원",
        "registered":"2026-05-08","feature":"주간 단골 안정 · 1인 운영 가능",
    },
    {
        "id":"S26-010","status":"매매중","title":"일산 백석 아로마샵 양도",
        "region_slug":"gyeonggi","region_kr":"경기","district_slug":"goyang","district_kr":"고양시",
        "location_sub":"백석역 1번 출구 도보 5분",
        "service":"aroma","service_kr":"아로마",
        "size_pyeong":36,"deposit":2500,"key_money":4000,"total":6500,"rent":145,
        "monthly_revenue":"2,500 ~ 3,000만원","monthly_profit":"1,000 ~ 1,250만원",
        "registered":"2026-05-07","feature":"1기 신도시 단골 안정",
    },
    {
        "id":"S26-011","status":"매매중","title":"부평 구월 발마사지 전문점 양도",
        "region_slug":"incheon","region_kr":"인천","district_slug":"bupyeong","district_kr":"부평구",
        "location_sub":"부평역 6번 출구 도보 3분",
        "service":"thai","service_kr":"타이·발마사지",
        "size_pyeong":24,"deposit":1500,"key_money":2500,"total":4000,"rent":100,
        "monthly_revenue":"1,800 ~ 2,200만원","monthly_profit":"750 ~ 950만원",
        "registered":"2026-05-06","feature":"환승 결절지 · 회전 빠름",
    },
    {
        "id":"S26-012","status":"매매중","title":"성수동 신축 로미로미 부티크 매매",
        "region_slug":"seoul","region_kr":"서울","district_slug":"seongdong","district_kr":"성동구",
        "location_sub":"성수역 2번 출구 도보 4분",
        "service":"lomilomi","service_kr":"로미로미",
        "size_pyeong":40,"deposit":4000,"key_money":6500,"total":10500,"rent":210,
        "monthly_revenue":"3,800 ~ 4,400만원","monthly_profit":"1,500 ~ 1,800만원",
        "registered":"2026-05-05","feature":"신축 6개월차 · 트렌드 권역",
    },
]


# ─────────────────────────────────────────────
# 광고 상품 가격표 (/pricing-ads/)
# ─────────────────────────────────────────────
PRICING_ADS = [
    {
        "slug":"vvip","name":"VVIP 채용정보",
        "tagline":"사이트 최상단 노출 고정 · 4개 업체 한정",
        "position":"메인페이지·업종·지역 페이지 최상단 (Hero 직하)",
        "color":"#d4af37","border":"rgba(212,175,55,.4)",
        "bg":"linear-gradient(135deg,#1a1410 0%,#2a1f12 100%)",
        "label_bg":"linear-gradient(135deg,#d4af37,#f4d29c)",
        "label_text":"#1a1410",
        "max_slots":4,
        "features":[
            "사이트 최상단 노출 고정 (메인·업종·지역 페이지)",
            "골드 톤 대형 카드 + 업체전용 특수 배너",
            "광고 상세 페이지 단독 생성 (/ad/공고번호/)",
            "구글 채용 검색(Google Jobs) JobPosting 스키마 자동 등록",
            "분기별 광고 효과 리포트 제공",
            "4개 업체만 입점 가능 — 선착순 배정",
        ],
        "pricing":[
            {"period":"1개월","price":440000,"per_month":440000},
            {"period":"6개월","price":880000,"per_month":146667},
            {"period":"12개월","price":1100000,"per_month":91667},
        ],
    },
    {
        "slug":"vip","name":"VIP 채용정보",
        "tagline":"콘텐츠 직후 우선 노출 · 12개 업체 한정",
        "position":"메인페이지·업종·지역 페이지 First Content Break (콘텐츠 1개 직후)",
        "color":"#5b9bff","border":"rgba(123,176,255,.4)",
        "bg":"linear-gradient(135deg,#121828,#1a2236)",
        "label_bg":"linear-gradient(135deg,#7bb0ff,#2c54a8)",
        "label_text":"#fff",
        "max_slots":12,
        "features":[
            "메인·업종·지역 페이지 First Content Break 노출",
            "블루 톤 중형 카드 + 전용 배너",
            "광고 상세 페이지 단독 생성 (/ad/공고번호/)",
            "구글 채용 검색 JobPosting 스키마 등록",
            "12개 업체만 입점 가능 — 선등록순 정렬",
        ],
        "pricing":[
            {"period":"1개월","price":200000,"per_month":200000},
            {"period":"6개월","price":450000,"per_month":75000},
            {"period":"12개월","price":550000,"per_month":45833},
        ],
    },
    {
        "slug":"premium","name":"프리미엄 채용정보",
        "tagline":"가성비 좋은 상품 · 등록 제한 없음",
        "position":"메인페이지·업종·지역 페이지 하단 영역",
        "color":"#a0a8be","border":"rgba(160,168,190,.3)",
        "bg":"linear-gradient(135deg,#13131a,#1a1a23)",
        "label_bg":"linear-gradient(135deg,#a0a8be,#6c7490)",
        "label_text":"#0a0e1a",
        "max_slots":None,
        "features":[
            "메인·업종·지역 페이지 하단 영역 노출",
            "그레이 톤 컴팩트 카드 + 전용 배너",
            "광고 상세 페이지 단독 생성 (/ad/공고번호/)",
            "구글 채용 검색 JobPosting 스키마 등록",
            "등록 제한 없음 — 누구나 즉시 신청 가능",
        ],
        "pricing":[
            {"period":"1개월","price":130000,"per_month":130000},
            {"period":"6개월","price":200000,"per_month":33333},
            {"period":"12개월","price":250000,"per_month":20833},
        ],
    },
]

# ─────────────────────────────────────────────
# 운영팀·자문 (E-E-A-T)
# ─────────────────────────────────────────────
TEAM = [
    {"name":"김세영","role":"수도권 운영팀장","credit":"채용 컨설팅 12년 · 누적 매칭 1.8만건"},
    {"name":"박지연","role":"채용 자문 트레이너","credit":"KSPO 스포츠마사지 트레이너 · 재활케어 8년"},
    {"name":"이도윤","role":"부산·영남 운영팀장","credit":"호텔 스파 운영 10년 · 부산 샵 네트워크 400+"},
]

# 후기 (구인구직 사례 — 행정구 페이지에서 변주)
def district_reviews(district_kr, service_kr):
    return [
        {"name":"A님 (28세, 스웨디시 경력 3년)","text":f"{district_kr} 샵 면접을 테라피잡으로 본 지 3일 만에 출근 시작했습니다. 인센티브 조건이 명확해서 좋았어요."},
        {"name":"B님 (34세, 아로마 경력 5년)","text":f"{district_kr} 권역 신축 샵 정보를 빠르게 받아 단가 좋은 곳으로 옮겼습니다. 정산 주기도 친절히 설명해주셨어요."},
        {"name":"C님 (31세, 타이 경력 2년)","text":f"이전 샵에서 정산 분쟁이 있었는데 {district_kr} 새 샵으로 옮긴 뒤 6개월째 깔끔하게 운영 중입니다."},
        {"name":"D 원장 (샵 운영)","text":f"{district_kr}에서 샵을 운영하는데, 공고 올린 당일 3명 지원받았습니다. 검증된 분들만 매칭되어 만족합니다."},
        {"name":"E님 (29세, 로미로미)","text":f"프리미엄 라인 채용 정보가 가장 정리 잘된 곳입니다. {district_kr} 일대 단가 비교도 한눈에 가능해요."},
        {"name":"F님 (37세, 스포츠)","text":f"{district_kr} 권역에서 자격증 우대 샵을 찾기 어려웠는데, 필터로 바로 정렬돼서 시간을 많이 아꼈습니다."},
    ]


# ─────────────────────────────────────────────
# 업종별 구직 가이드 고유 콘텐츠 (/seekers/{slug}/)
# ─────────────────────────────────────────────
SEEKER_DETAIL = {
    "swedish": {
        "fit":"오일을 이용한 전신 흐름 시술이라 손기술 진입 장벽이 가장 낮은 업종입니다. 표준 스트로크 5종만 익히면 견습 1주 내 현장 투입이 가능해, 신규 입직자의 70% 이상이 스웨디시로 첫 직장을 시작합니다.",
        "body":"1일 6~9명 시술이 표준이며, 전신 오일 시술 특성상 체중을 실어 미는 동작이 많아 손목·전완 근지구력이 핵심입니다. 오일로 미끄러지듯 진행하므로 타이·스포츠보다 관절 부담은 적은 편입니다.",
        "income":"주 5일 기준 월 380만~620만원. 채용 시장이 가장 넓어 일감 끊김 걱정이 적고, 인센티브 45~55% 구조에서 1일 7명·객단가 8.5만원이면 월 약 450만원이 안정적으로 나옵니다.",
        "caution":"진입이 쉬운 만큼 경쟁자도 많습니다. '에플라지→페트리사지→딥 스트로크'로 이어지는 본인만의 시그니처 흐름을 만들어야 단가 협상에서 차별화됩니다.",
        "career":"스웨디시로 1~2년 기본기를 다진 뒤, 향 설계가 강점이면 아로마로, 체력·전문성을 살리면 스포츠로 확장하는 경로가 일반적입니다.",
        "interview":[
            ("스트로크 시퀀스를 시연해 주세요","면접에서 가장 흔한 요청입니다. 에플라지(쓸기)→페트리사지(주무르기)→프릭션(마찰) 순서를 손에 익혀 막힘없이 보여주세요."),
            ("오일 양 조절은 어떻게 하나요","고객 피부 타입·체모량에 따른 오일 양 조절 기준을 설명하면 실무 경험을 인정받습니다."),
            ("60분 코스 동선을 어떻게 짜나요","등→다리 후면→다리 전면→팔→복부→마무리의 시간 배분을 분 단위로 답하면 좋습니다."),
        ],
    },
    "aroma": {
        "fit":"에센셜 오일 블렌딩과 향 설계가 핵심이라, 후각이 예민하고 감성적 응대에 강한 분에게 맞습니다. 시술 강도보다 '분위기와 향의 경험'을 파는 업종이라 프리미엄 단골 형성률이 높습니다.",
        "body":"시술 강도는 스웨디시보다 부드러워 체력 부담은 중간 수준입니다. 다만 블렌딩 차트·차크라·림프 흐름을 이해해야 하고, 디퓨저·캔들 등 공간 연출까지 관리하는 손이 더 갑니다.",
        "income":"주 5일 기준 월 400만~680만원. 프리미엄 라인 비중이 높아 객단가가 스웨디시보다 높고, 고정 단골 비율이 커서 수입 변동이 가장 적은 업종입니다.",
        "caution":"향에 대한 고객 호불호가 분명해, 첫 상담에서 선호 향·알레르기를 정확히 파악하지 못하면 재방문으로 이어지지 않습니다. 블렌딩 노트 기록 습관이 필수입니다.",
        "career":"아로마 경력은 스파·호텔 웰니스 라인으로 확장하기 좋습니다. 국제 아로마테라피 자격(IFA·NAHA)을 더하면 프리미엄 단가를 받을 수 있습니다.",
        "interview":[
            ("블렌딩 차트를 설명해 주세요","탑·미들·베이스 노트 구성과 대표 오일(라벤더·베르가못·프랑킨센스)의 효능을 답하면 전문성을 인정받습니다."),
            ("불면 고객에게 어떤 향을 추천하나요","라벤더·캐모마일·마조람 조합과 그 이유를 설명하면 좋습니다."),
            ("공간 연출은 어떻게 하나요","조도·디퓨저·음악까지 '향의 경험'을 설계하는 관점을 보여주세요."),
        ],
    },
    "thai": {
        "fit":"건식 스트레칭과 체중을 이용한 압이 핵심이라, 체력과 유연성이 뛰어난 분에게 맞습니다. 옷을 입은 채 진행해 회전이 빠르고, 라인콜이 많은 샵에서 선호도가 높습니다.",
        "body":"5개 업종 중 체력 소모가 가장 큽니다. 무릎·팔꿈치·발을 이용한 압과 파트너 스트레칭이 많아 본인의 코어·하체 근력이 시술 품질을 좌우합니다. 1일 6~8명이 한계선입니다.",
        "income":"주 5일 기준 월 420만~720만원. 옷 갈아입는 시간이 짧아 회전이 빨라 인센티브 효율이 좋고, 120분 코스 비중이 높아 객단가가 안정적입니다.",
        "caution":"체력 소모가 커서 본인 몸 관리가 곧 수입입니다. 정통 와트포 스타일을 요구하는 샵이 늘어, 태국 현지 수료증이나 정통 시퀀스 숙련도가 단가에 직결됩니다.",
        "career":"타이는 정통 자격(와트포)을 더하면 '진짜 태국' 프리미엄 라인으로 갈 수 있고, 스포츠 스트레칭과 결합해 재활 라인으로도 확장 가능합니다.",
        "interview":[
            ("기본 스트레칭 시퀀스를 보여주세요","코브라·나비·트위스트 등 파트너 스트레칭을 안정적으로 시연할 수 있어야 합니다."),
            ("체중을 어떻게 분산하나요","무릎·팔꿈치·발 압의 강도 조절과 본인 체중 분산 원리를 설명하세요."),
            ("120분 코스 구성은","발→다리→등→어깨→스트레칭 마무리의 시간 배분을 답하면 좋습니다."),
        ],
    },
    "lomilomi": {
        "fit":"전완(팔뚝)을 파도처럼 흘려 쓰는 하와이안 리듬 케어로, 시술의 '예술성'을 중시하는 분에게 맞습니다. 객단가가 가장 높은 프리미엄 라인이라 교육 이수자를 선호합니다.",
        "body":"전완·팔꿈치를 길게 흘려 쓰는 동작이 많아 어깨·등 근지구력이 중요합니다. 호흡과 동작을 동기화하는 리듬감이 핵심이라, 기계적 반복이 아닌 흐름 감각을 익히는 데 시간이 걸립니다.",
        "income":"주 5일 기준 월 450만~760만원. 1인당 시술 수는 적지만 객단가가 가장 높아 고정 수입이 안정적입니다. 강남·청담·해운대 등 럭셔리 상권에 채용이 집중됩니다.",
        "caution":"별도 교육 과정(로미로미 워크숍) 이수를 요구하는 샵이 많아 진입 장벽이 있습니다. 신규 입직자가 바로 시작하기는 어렵고, 보통 스웨디시·아로마 경력 후 전환합니다.",
        "career":"로미로미는 하이엔드 스파·리조트·호텔 웰니스의 핵심 라인입니다. 교육 이수와 경력을 쌓으면 강사·트레이너로도 진출할 수 있습니다.",
        "interview":[
            ("전완 스트로크를 시연해 주세요","팔뚝을 길게 흘려 쓰는 하와이안 시퀀스의 리듬감을 보여주는 것이 핵심입니다."),
            ("교육 이수 경험이 있나요","로미로미 워크숍·자격 과정 이수 여부가 프리미엄 라인 채용의 핵심 기준입니다."),
            ("호흡 동기화란 무엇인가요","고객 호흡에 동작 리듬을 맞추는 원리를 설명하면 깊이를 인정받습니다."),
        ],
    },
    "sports": {
        "fit":"근막·근육 회복에 초점을 둔 딥티슈 케어로, 해부학 지식과 전문성을 갖춘 분에게 맞습니다. KSPO·CES 등 자격증 보유 시 우대 폭이 가장 크고, 남성 고객 비중이 60%를 넘습니다.",
        "body":"트리거 포인트·근막 이완에 강한 압이 필요해 손가락·엄지·팔꿈치 근력이 중요합니다. 강도가 세지만 시술 시간이 부위 집중형이라 타이보다 전신 체력 소모는 적습니다.",
        "income":"주 5일 기준 월 480만~820만원. 5개 업종 중 단가 최상위이며, 자격증·재활 경험에 따라 일급이 15~25% 가산됩니다. 낮 시간대 운영 샵이 많아 야간 부담이 적습니다.",
        "caution":"해부학·근육 지식이 부족하면 통증을 악화시킬 위험이 있어, 전문 교육이 사실상 필수입니다. 운동선수·재활 고객 응대 경험이 단가를 크게 좌우합니다.",
        "career":"스포츠 케어는 재활 트레이너·물리치료 보조·운동선수 전담 등 전문직 경로로 확장하기 가장 좋은 업종입니다. 자격증을 쌓을수록 단가 상한이 높아집니다.",
        "interview":[
            ("트리거 포인트를 어떻게 찾나요","승모근·견갑거근 등 주요 근육의 트리거 포인트 위치와 이완 기법을 설명하면 전문성을 인정받습니다."),
            ("보유 자격증이 있나요","KSPO 스포츠마사지·CES 등 자격증과 재활 경험이 채용·단가의 핵심 기준입니다."),
            ("근막 이완 원리를 설명해 주세요","근막 제한과 가동 범위 회복의 관계를 해부학 용어로 답하면 좋습니다."),
        ],
    },
}


# ─────────────────────────────────────────────
# 국적별 관리사 고유 콘텐츠 (/therapists/{slug}/)
# ─────────────────────────────────────────────
THERAPIST_DETAIL = {
    "korean": {
        "visa":"국적 제한이 없어 모든 업종·지역에 자유롭게 취업할 수 있습니다. 별도 체류 자격 확인이 불필요해 채용 절차가 가장 빠릅니다.",
        "svc_pref":"전 업종에서 수요가 고르나, 특히 응대·예약 변경 대응이 중요한 프리미엄 스파(강남·청담·해운대)와 단골 관리 비중이 큰 주거 권역에서 선호도가 높습니다.",
        "trend":"한국인 관리사는 사무 처리·매출 입력·고객 컴플레인 대응까지 가능해, 1인 운영 샵이나 신축 샵의 '믿고 맡길 수 있는' 핵심 인력으로 채용되는 경우가 많습니다. 단가 협상력도 가장 높습니다.",
        "tip":"한국인 관리사는 단골 관리·재방문 유도 역량이 곧 단가입니다. 응대 매뉴얼을 본인 톤으로 정립하고 단골 데이터를 체계적으로 관리하면 프리미엄 라인 진입이 빠릅니다.",
    },
    "chinese": {
        "visa":"F-4(재외동포)·F-5(영주)·F-6(결혼이민) 보유 시 업종 제한 없이 취업 가능하며, H-2(방문취업)도 서비스업 취업이 허용됩니다. 채용 시 체류 자격 원본 확인이 필수입니다.",
        "svc_pref":"정통 추나·지압·발마사지 기술 보유자가 많아 타이·발마사지 라인에서 강세입니다. 수도권(구로·대림·안산)과 부산 일부 권역에서 채용 수요가 평균 1.5배 높습니다.",
        "trend":"중국 동포 관리사는 지압 강도 조절이 정교하고 장시간 시술 체력이 좋아, 회전이 빠른 발마사지·타이 전문점에서 선호됩니다. 한국어 응대가 가능하면 단가가 추가로 올라갑니다.",
        "tip":"추나·지압 강점을 살려 발마사지·타이 전문점을 우선 공략하세요. F-4/F-6 등 체류 자격을 명확히 갖추면 채용 속도가 크게 빨라집니다.",
    },
    "thai": {
        "visa":"E-9·H-2 등 합법 체류 자격이 우대되며, 정통 타이 자격(와트포 인증) 보유 시 D-10·E-7 비자 신청이 일부 가능합니다. 체류 자격은 법무부 출입국 확인이 필요합니다.",
        "svc_pref":"정통 태국 마사지의 본고장 출신으로 타이마사지 라인에서 최우선 매칭됩니다. 라인콜이 많은 타이 전문점과 '진짜 태국' 경험을 내세우는 프리미엄 샵에서 채용이 집중됩니다.",
        "trend":"태국인 관리사는 와트포 스타일의 스트레칭·압 시퀀스가 정통이라, 타이 전문점에서 대체 불가능한 인력으로 평가됩니다. 정통 자격을 갖추면 단가 상한이 크게 높아집니다.",
        "tip":"정통 타이 시퀀스 숙련도가 곧 경쟁력입니다. 와트포 수료증이나 태국 현지 경력을 증빙할 수 있으면 프리미엄 타이 라인에서 최고 단가를 받을 수 있습니다.",
    },
    "vietnamese": {
        "visa":"F-6(결혼이민)·F-4 보유자가 많으며, 합법 체류 자격 확인 후 채용됩니다. 한국어 학습 의지가 높아 정착 후 비자 안정성이 좋은 편입니다.",
        "svc_pref":"차분한 응대와 정성스러운 손길로 스웨디시·아로마 주거 권역 단골 형성에 강합니다. 최근 3년 채용이 +220% 늘며 수도권 신도시 신축 샵에서 수요가 빠르게 증가하고 있습니다.",
        "trend":"베트남 관리사는 출퇴근 정시 준수율이 높고 팀워크 적응이 빨라, 다인 운영 신축 샵에서 선호됩니다. 한국어 능력이 향상될수록 단골 응대 폭이 넓어져 단가가 상승합니다.",
        "tip":"차분한 응대 강점을 살려 주거 권역 스웨디시·아로마 라인에서 단골을 빠르게 만드세요. 한국어 응대 역량을 키우면 단가와 재방문율이 함께 올라갑니다.",
    },
    "russian": {
        "visa":"F-2·F-5·F-6 또는 전문 인력 비자 보유자가 많으며, 외국인 고객 응대가 가능한 영어·러시아어 역량이 핵심 자산입니다. 체류 자격은 채용 전 반드시 확인합니다.",
        "svc_pref":"외국인 고객·프리미엄 호텔 출장 라인에서 강세입니다. 체격이 좋아 딥티슈·스포츠 케어에 강점이 있고, 이태원·한남·송도·해운대 등 외국인 밀집 권역에 채용이 집중됩니다.",
        "trend":"러시아·CIS 관리사는 영어 응대로 외국인 고객을 직접 매칭할 수 있어, 스파·럭셔리 라인에서 단가 가산 폭이 가장 큽니다(+16~30만원). 호텔 웰니스 경력자 수요가 특히 높습니다.",
        "tip":"영어 응대 + 딥티슈 강점을 외국인 밀집 권역(이태원·송도·해운대)에 집중하세요. 호텔·스파 경력을 증빙하면 프리미엄 라인에서 최고 단가를 받을 수 있습니다.",
    },
    "japanese": {
        "visa":"F-6(결혼이민)·F-4 또는 전문 비자 보유자가 많으며, 합법 체류 자격 확인 후 채용됩니다. 응대 매뉴얼 준수율이 높아 채용 후 정착이 안정적입니다.",
        "svc_pref":"섬세한 응대와 청결도가 강점이라 아로마·일식 리츄얼 라인에서 강세입니다. 감성 케어를 중시하는 프리미엄 스파와 일본인·외국인 고객 응대 라인에서 1순위로 매칭됩니다.",
        "trend":"일본인 관리사는 응대 매뉴얼 준수·도구 청결 관리가 업계 최고 수준으로 평가됩니다. 아로마·감성 라인에서 단골 충성도가 높아, 객단가 높은 프리미엄 샵에서 안정적 수입을 올립니다.",
        "tip":"섬세한 응대·청결 강점을 아로마·일식 리츄얼 라인에 집중하세요. 일본어 응대가 가능하면 일본인 관광객·거주민 단골을 독점적으로 확보할 수 있습니다.",
    },
}
