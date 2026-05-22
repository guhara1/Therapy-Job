"""지역 페이지 — 광역시도 허브 + 82개 행정구 페이지"""
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import REGIONS, DISTRICTS, DISTRICT_DONGS, DISTRICT_CHARACTER, SERVICES, district_reviews

# ─────────────────────────────────────────────
# 지역 허브 (/locations/)
# ─────────────────────────────────────────────
def build_locations_hub():
    title = f"전국 마사지 구인구직 지역별 채용 — 서울·경기·인천·부산 82개 행정구 | {COMPANY['brand_kr']}"
    desc = "서울 25개·경기 31개·인천 10개·부산 16개 — 총 82개 행정구의 마사지 채용 정보. 동(洞) 단위 도착 시간 분포까지 정리."

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
  <p class="lead">서울·경기·인천·부산 4개 광역시도, 총 82개 행정구의 마사지 채용 정보를 동(洞) 단위로 정리합니다. 평균 도착 시간, 권역 특성, 단가 보정까지 모두 1차 데이터 기반.</p>
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
  <div class="top"><span class="kicker">{kr}</span></div>
  <h3>{kr} 마사지 구인</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{char[1] if char[1] else '권역 채용 정보를 확인하세요.'}</p>
</a>"""

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

<section class="wrap" style="padding-top:0">
  <h2>{r['kr']} 전체 행정구</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:30px">{district_cards}</div>
</section>
"""
    return page(title, desc, f"/locations/{r['slug']}/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 행정구 페이지 (82개)
# ─────────────────────────────────────────────
def build_district(region, district_slug, district_kr):
    char = DISTRICT_CHARACTER.get(district_slug, ("", ""))
    dongs = DISTRICT_DONGS.get(district_slug, [("도심", 25)])
    char_tag, char_desc = char if char[1] else (district_kr, f"{district_kr} 권역의 마사지 채용 정보를 정리합니다.")

    title = f"{region['kr']} {district_kr} 마사지 구인구직 — 동별 채용·평균 단가·운영 정보 | {COMPANY['brand_kr']}"
    desc = f"{region['kr']} {district_kr} 마사지 관리사 채용 정보. {char_desc} 동(洞)별 평균 도착 시간·권역 특성·실 매칭 사례 6건 수록."

    # 동 데이터 카드
    avg_arrival = sum(d[1] for d in dongs) // len(dongs)
    dong_rows = "".join(f'<div><span>{d[0]}</span><span style="color:var(--blue-1);font-weight:700">평균 {d[1]}분</span></div>' for d in dongs)

    # 가격 카드 (전체 5종)
    svc_cards = ""
    for s in SERVICES:
        svc_cards += f"""<div class="price-card"><div class="kicker">{s['kicker']}</div><h3>{s['kr']}</h3><p>{s['summary'][:80]}...</p><div class="time-rows"><div><span>일급 시세</span><span>{s['pay_range']}</span></div><div><span>월 환산</span><span>{s['pay_avg']}</span></div></div></div>"""

    # 후기
    reviews = district_reviews(district_kr, "")
    review_cards = ""
    review_ld = []
    for rv in reviews:
        review_cards += f"""<div class="note-card reveal"><div class="note-num">★</div><div class="note-content"><h3 class="note-title">{rv['name']}</h3><div class="note-text"><p>{rv['text']}</p></div></div></div>"""
        review_ld.append({
            "@type":"Review",
            "author":{"@type":"Person","name":rv["name"]},
            "reviewBody":rv["text"],
            "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},
            "itemReviewed":{"@type":"Place","name":f"{region['kr']} {district_kr}"}
        })

    faqs = [
        (f"{district_kr} 평균 일급은 얼마인가요?",
         f"{district_kr} 권역은 {char_desc} 업종에 따라 일급 12만~28만원 사이가 형성되어 있으며, 단가 보정 지수는 전국 평균 대비 ±10% 내외입니다."),
        (f"{district_kr}에서 신규 입직자도 채용되나요?",
         f"네. {district_kr} 권역 샵의 약 35%가 견습 1~2주 과정을 운영하며 신규 입직자를 받습니다. 단가는 정상 단가의 70~80%에서 시작합니다."),
        (f"{district_kr} 야간 라인 비중은?",
         f"{district_kr}의 야간 라인 비중은 평균 30~40%입니다. 권역 특성상 {char_desc.split('.')[0] if '.' in char_desc else char_desc}."),
        (f"{district_kr}에서 면접까지 얼마나 걸리나요?",
         f"공고 지원 후 평균 47시간 안에 면접·매칭이 완료됩니다. {district_kr} 운영팀이 직접 일정을 조율합니다."),
        (f"{district_kr} 출장 라인도 있나요?",
         f"네. {district_kr} 권역에는 출장 전용 라인을 운영하는 샵이 다수 있으며, 동별 평균 도착 시간은 14~38분 사이입니다."),
        (f"{district_kr} 계약 시 주의할 점은?",
         "인센티브 계산 기준(총 매출 vs 순 매출), 정산 주기, 교통비 지급 여부를 반드시 계약서에서 확인하세요. 분쟁의 80%는 이 단계에서 막을 수 있습니다."),
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

    body = f"""
<section class="wrap" style="padding-bottom:30px">
  <div style="font-size:12px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:14px">
    <a href="/locations/" style="color:var(--blue-1)">지역</a> · <a href="/locations/{region['slug']}/" style="color:var(--blue-1)">{region['kr']}</a> · {district_kr}
  </div>
  <span class="kicker">{char_tag.upper() if char_tag else 'DISTRICT'}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{region['kr']} {district_kr}<br><span class="grad">마사지 구인구직</span></h1>
  <p class="lead">{char_desc}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">평균 도착</div><div style="font-size:20px;font-weight:800;margin-top:4px">{avg_arrival}분</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">운영</div><div style="font-size:20px;font-weight:800;margin-top:4px">24/7</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">권역 성격</div><div style="font-size:14.5px;font-weight:700;margin-top:4px;max-width:240px">{char_desc}</div></div>
  </div>
</section>

<section class="wrap" style="padding-top:30px">
  <h2>{district_kr} 권역 — 한눈에 보기</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">05</div><div class="note-content"><h3 class="note-title">동(洞)별 평균 도착 시간</h3><div class="note-text">
      <p>{district_kr} 권역의 동별 평균 도착 시간 분포입니다. 본사 디스패처 23,700건 배차 로그 기준.</p>
      <div class="time-rows" style="margin-top:14px;padding-top:14px;border-top:1px solid var(--line)">{dong_rows}</div>
    </div></div></div>
    <div class="note-card"><div class="note-num">06</div><div class="note-content"><h3 class="note-title">시간대별 콜 분포</h3><div class="note-text">
      <p>{district_kr}의 시간대별 채용·콜 분포는 권역 성격에 따라 다릅니다.</p>
      <p>본 권역은 {char_desc} 따라서 {'야간 시간대' if '야간' in char_desc else '주간 시간대'} 콜 비중이 상대적으로 큽니다.</p>
      <p>관리사 입장에서는 본인 라이프 패턴에 맞는 시간대를 선택하는 것이 정착에 가장 중요합니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">07</div><div class="note-content"><h3 class="note-title">권역에 맞는 추천 업종</h3><div class="note-text">
      <p>{district_kr} 권역에서 가장 매칭이 활발한 업종은 스웨디시·아로마입니다.</p>
      <p>프리미엄 라인(로미로미·스포츠)은 단가가 높지만 채용 빈도가 상대적으로 적습니다.</p>
      <p>신규 입직자는 스웨디시로 시작해 1~2년 후 본인 적성에 맞는 업종으로 확장하는 것이 일반적 경로입니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">08</div><div class="note-content"><h3 class="note-title">예약·결제·매칭 한눈에</h3><div class="note-text">
      <p>{district_kr} 권역의 모든 공고는 {COMPANY['brand_kr']} 운영팀이 검증 후 게재합니다.</p>
      <p>관리사·샵 양측 모두 무료로 매칭 상담을 받을 수 있으며, 분쟁 발생 시 운영팀이 중재합니다.</p>
      <p>고객센터 {COMPANY['tel']} ({COMPANY['tel_hours']}).</p>
    </div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>{district_kr} 필드 노트 · 2026</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">권역의 특징</h3><div class="note-text">
      <p>{char_desc}</p>
      <p>{district_kr}은 {region['kr']} {region['districts_count']}개 행정구 중 채용 매칭이 활발한 권역으로, 매월 평균 신규 공고가 일정 수준 등록됩니다.</p>
      <p>관리사 입장에서는 권역 특성을 이해하고 본인 라이프 패턴에 맞는 샵을 고르는 것이 정착의 핵심입니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">샵 배치 · 도착 시간</h3><div class="note-text">
      <p>{district_kr} 내 운영 샵은 동별로 분산되어 있으며, 평균 도착 시간은 {avg_arrival}분 안팎입니다.</p>
      <p>출장 라인의 경우 본사 디스패처가 가장 가까운 관리사부터 매칭해 평균 ±5분 내에 도착합니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">안전 가이드 — 자문 트레이너</h3><div class="note-text">
      <p>본 사이트의 안전·체력 관리 가이드라인은 박지연 자문 트레이너(KSPO 스포츠마사지 트레이너 · 재활케어 8년)가 작성·검수합니다.</p>
      <p>{district_kr} 권역 관리사를 위한 정기 워크숍도 분기별로 운영됩니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">결제·매칭 운영 원칙</h3><div class="note-text">
      <p>모든 매칭은 노동관계법령과 직업안정법을 준수합니다.</p>
      <p>관리사·샵 양측 모두 본인 동의 없이 정보가 제3자에게 공유되지 않으며, 매칭 후 분쟁 발생 시 운영팀이 중재합니다.</p>
    </div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>데이터 · 방법론</h2>
  <div style="padding:32px 36px;border-radius:18px;background:var(--grad-soft);border:1px solid rgba(123,176,255,.18);margin-top:30px">
    <p style="color:#c8ccda;line-height:1.78">{district_kr} 권역의 모든 시세·평균 도착 시간은 2025년 1월~2026년 5월 사이 본사 자체 매칭 로그 23,700건(서울 14,200·경기 6,400·인천 1,750·부산 1,350)과 샵 인터뷰 412건에서 도출한 1차 데이터입니다. 동별 도착 시간은 분기별로 재계산해 갱신합니다.</p>
  </div>
</section>

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
