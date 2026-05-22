"""허브·서브 페이지 — 구인공고, 구직 가이드, 관리사, 매거진"""
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import SERVICES, NATIONALITIES, REGIONS, MAGAZINE, SAMPLE_JOBS, DISTRICTS, AD_TIERS
from ads import render_all_tiers, single_tier_block, jobs_for_service_tier

# ─────────────────────────────────────────────
# 구인공고 허브
# ─────────────────────────────────────────────
def build_jobs_hub():
    title = f"마사지 구인공고 — 스웨디시·아로마·타이·로미로미·스포츠 전체 채용 | {COMPANY['brand_kr']}"
    desc = "전국 마사지샵 채용 공고 5,820여건. 업종·지역·근무 시간대로 필터링. 일급·인센티브·정산 주기까지 명확한 공고만 게재."

    svc_cards = ""
    for s in SERVICES:
        svc_cards += f"""<a class="job-card reveal" href="/jobs/{s['slug']}/">
  <div class="top"><span class="kicker">{s['kicker']}</span><span class="badge BEST">{s['openings']:,}건</span></div>
  <h3>{s['kr']} 구인공고</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{s['summary']}</p>
  <div class="pay">{s['pay_range']}</div>
</a>"""

    # 광고 등급 순(VVIP→VIP→Premium) → 같은 등급 내 선등록순
    tier_order = {"vvip":0,"vip":1,"premium":2}
    sorted_jobs = sorted(SAMPLE_JOBS, key=lambda j:(tier_order.get(j.get("tier"),9), j.get("registered","")))
    tier_labels = {"vvip":("VVIP","#d4af37"),"vip":("VIP","#7bb0ff"),"premium":("PREMIUM","#a0a8be")}
    job_cards = ""
    for j in sorted_jobs:
        svc = next(s for s in SERVICES if s["slug"]==j["service"])
        tlbl, tcol = tier_labels.get(j.get("tier","premium"))
        badge = f'<span class="badge" style="background:rgba(123,176,255,.18);color:{tcol};font-size:9.5px;letter-spacing:.2em;font-weight:800;padding:3px 8px;border-radius:4px">{tlbl}</span>'
        job_cards += f"""<a class="job-card reveal" href="/jobs/{j['service']}/">
  <div class="top"><span class="kicker">{svc['kicker']}</span>{badge}</div>
  <h3>{j['title']}</h3>
  <div class="meta"><span>📍 {j['region']}</span></div>
  <div class="pay">{j['pay']}</div>
  <div class="id">공고 #{j['id']}</div>
</a>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("구인공고","/jobs/")]),
        {
            "@type":"CollectionPage",
            "url":f"{COMPANY['base_url']}/jobs/",
            "name":title,
            "description":desc
        }
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">JOB LISTINGS</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">마사지 구인공고<br><span class="grad">전체 5,820여건</span></h1>
  <p class="lead">매일 247건 안팎의 신규 공고가 등록되며, 운영팀이 검증한 공고만 게재됩니다. 일급·인센티브·정산 주기·근무 시간이 모두 명시되어 있습니다.</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>업종별 채용</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:30px">{svc_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>오늘의 추천 공고</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:30px">{job_cards}</div>
</section>
"""
    return page(title, desc, "/jobs/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 업종별 구인공고 페이지 (5개)
# ─────────────────────────────────────────────
def build_job_service(s):
    title = f"{s['kr']} 마사지 관리사 구인공고 — {s['openings']:,}건 모집 중 | {COMPANY['brand_kr']}"
    desc = f"{s['kr']} 마사지 채용 공고 {s['openings']:,}건. 전국 평균 {s['pay_range']}. {s['summary']}"

    # 샘플 공고 — 해당 서비스만
    related = [j for j in SAMPLE_JOBS if j["service"]==s["slug"]]
    # 부족하면 보강
    if len(related) < 3:
        for j in SAMPLE_JOBS:
            if j["service"] != s["slug"] and len(related) < 3:
                related.append({**j, "service":s["slug"]})

    job_cards = ""
    extra_jobs = [
        {"id":f"J26-{4000+i}","title":t,"region":r,"pay":p,"badge":b}
        for i,(t,r,p,b) in enumerate([
            (f"{s['kr']} 정규 관리사 모집 (강남)", "서울 강남구 역삼동", "일 16만~24만원", "FAST"),
            (f"{s['kr']} 야간 근무 환영 (마포)", "서울 마포구 합정동", "일 17만~25만원", "NEW"),
            (f"{s['kr']} 경력 우대 프리미엄 (서초)", "서울 서초구 반포동", "일 20만~28만원", "BEST"),
            (f"{s['kr']} 신축 샵 단가 협의 (분당)", "경기 성남시 판교동", "일 15만~22만원", "NEW"),
            (f"{s['kr']} 주간 전담 (송파)", "서울 송파구 잠실동", "일 14만~20만원", ""),
            (f"{s['kr']} 출장 라인 (해운대)", "부산 해운대구 우동", "일 18만~26만원", "BEST"),
        ])
    ]
    for j in extra_jobs:
        badge = f'<span class="badge {j["badge"]}">{j["badge"]}</span>' if j["badge"] else ""
        job_cards += f"""<div class="job-card reveal">
  <div class="top"><span class="kicker">{s['kicker']}</span>{badge}</div>
  <h3>{j['title']}</h3>
  <div class="meta"><span>📍 {j['region']}</span></div>
  <div class="pay">{j['pay']}</div>
  <div class="id">공고 #{j['id']}</div>
</div>"""

    skills_li = "".join(f"<li>{sk}</li>" for sk in s["skills"])
    details_p = "".join(f"<p>{d}</p>" for d in s["details"])

    faqs = [
        (f"{s['kr']} 신규 입직자도 지원 가능한가요?",
         "네. 견습 1~2주 과정을 운영하는 샵이 다수 등록되어 있어, 자격증·경력 없이도 시작할 수 있습니다. 다만 단가는 경력자 대비 70~80% 수준입니다."),
        (f"{s['kr']} 평균 인센티브 비율은 어떻게 되나요?",
         "전국 평균 45~55% 사이입니다. 강남·서초·해운대 등 단가 최상위 권역은 50% 초반, 외곽 권역은 55% 후반이 일반적입니다."),
        (f"{s['kr']} 야간 근무 샵이 많나요?",
         "전체 공고의 약 38%가 야간 라인입니다. 마포·강남·송파·해운대 권역이 야간 비중이 높고, 외곽 신도시는 주간 비중이 높습니다."),
        (f"{s['kr']} 자격증이 있으면 단가가 오르나요?",
         "스웨디시·아로마는 자격증 영향이 크지 않지만, 스포츠·로미로미는 자격증·교육 이수 증명에 따라 일급이 15~25% 가산됩니다."),
        ("계약 형태는 어떻게 되나요?",
         "프리랜서(3.3% 원천징수)가 80% 이상이며, 정규직(4대 보험)은 일부 대형 샵에서만 운영합니다."),
    ]

    extra_ld = [
        breadcrumb_ld([("홈","/"),("구인공고","/jobs/"),(f"{s['kr']} 구인","/jobs/"+s["slug"]+"/")]),
        faq_ld(faqs),
        {
            "@type":"Service",
            "name":f"{s['kr']} 마사지 관리사 채용 정보",
            "provider":{"@id":f"{COMPANY['base_url']}/#organization"},
            "areaServed":{"@type":"Country","name":"대한민국"},
            "serviceType":"채용 정보 제공",
            "description":s["summary"]
        },
        {
            "@type":"JobPosting",
            "title":f"{s['kr']} 마사지 관리사",
            "description":f"{s['summary']} {' '.join(s['details'])}",
            "datePosted":"2026-05-15",
            "validThrough":"2026-12-31",
            "employmentType":"CONTRACTOR",
            "hiringOrganization":{"@id":f"{COMPANY['base_url']}/#organization"},
            "jobLocation":{"@type":"Place","address":{"@type":"PostalAddress","addressCountry":"KR","addressRegion":"전국"}},
            "baseSalary":{
                "@type":"MonetaryAmount","currency":"KRW",
                "value":{"@type":"QuantitativeValue","value":s["pay_range"],"unitText":"DAY"}
            },
            "industry":"마사지·테라피"
        }
    ]

    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">{s['kicker']}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{s['kr']} 마사지<br><span class="grad">{s['openings']:,}건</span> 모집 중</h1>
  <p class="lead">{s['summary']}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">평균 일급</div><div style="font-size:18px;font-weight:800;margin-top:4px">{s['pay_range']}</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">월 환산</div><div style="font-size:18px;font-weight:800;margin-top:4px">{s['pay_avg']}</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">{s['tag']}</div><div style="font-size:18px;font-weight:800;margin-top:4px">{s['openings']:,}건</div></div>
  </div>
</section>

{single_tier_block("vvip", jobs_for_service_tier(s['slug'], "vvip"), include_css=True, padding_top=20)}

<section class="wrap" style="padding-top:20px">
  <h2>업종 특성</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">{s['kr']} 시장 개요</h3><div class="note-text">{details_p}</div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">필수·우대 역량</h3><div class="note-text"><p>다음 역량을 갖추면 면접 통과율이 크게 올라갑니다.</p><ul style="margin:10px 0 0 18px;color:#c8ccda;line-height:1.9">{skills_li}</ul></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">근무 패턴</h3><div class="note-text"><p>주 5~6일 근무가 일반적이며, 1일 6~9시간 시술이 표준입니다.</p><p>출퇴근 시간은 샵에 따라 다르며, 야간 라인은 14시~02시, 주간 라인은 10시~22시가 흔합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">교통·식대·기타</h3><div class="note-text"><p>출장 라인은 교통비 별도 지급, 샵 상주 라인은 식대 5,000~10,000원 지원이 일반적입니다.</p><p>유니폼은 대부분 샵에서 제공하며, 신발·소품은 본인 부담입니다.</p></div></div></div>
  </div>
</section>

{single_tier_block("vip", jobs_for_service_tier(s['slug'], "vip"))}

<section class="wrap" style="padding-top:0">
  <h2>{s['kr']} — 기타 공고 샘플</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px;margin-top:30px">{job_cards}</div>
</section>

{single_tier_block("premium", jobs_for_service_tier(s['slug'], "premium"))}

<section class="wrap" style="padding-top:0">
  <h2>자주 묻는 질문</h2>
  <div style="max-width:860px;margin:30px auto 0">
"""
    for q,a in faqs:
        body += f'<details><summary>{q}<span>+</span></summary><div>{a}</div></details>'
    body += f"""
  </div>
</section>

<section class="wrap" style="padding-top:40px">
  <div style="padding:50px 40px;border-radius:22px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);text-align:center">
    <h2 style="margin-bottom:14px">{s['kr']} 매칭 상담 받기</h2>
    <p class="lead" style="margin:0 auto 24px">원하시는 권역·근무 시간·단가 조건을 알려주시면 맞는 공고를 정리해드립니다.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="tel:{COMPANY['tel']}">{COMPANY['tel']}</a>
      <a class="btn btn-ghost" href="/seekers/{s['slug']}/">구직 가이드</a>
    </div>
  </div>
</section>
"""
    return page(title, desc, f"/jobs/{s['slug']}/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 구직 가이드 허브
# ─────────────────────────────────────────────
def build_seekers_hub():
    title = f"마사지 관리사 구직 가이드 — 면접·계약·정착 | {COMPANY['brand_kr']}"
    desc = "마사지 관리사 구직 종합 가이드. 업종 선택·면접 준비·계약 체크·정착까지 전 과정 단계별 정리. 신규·경력 모두 활용 가능."

    svc_cards = ""
    for s in SERVICES:
        svc_cards += f"""<a class="job-card reveal" href="/seekers/{s['slug']}/">
  <div class="top"><span class="kicker">{s['kicker']}</span></div>
  <h3>{s['kr']} 구직 가이드</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{s['summary']}</p>
</a>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("구직 가이드","/seekers/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">JOB SEEKERS</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">관리사 구직<br><span class="grad">전 과정</span> <span class="serif">가이드.</span></h1>
  <p class="lead">신규 입직자부터 경력 이직자까지 — 업종 선택·면접 준비·계약 체크·정착까지 전 과정을 단계별로 정리했습니다.</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>4단계 로드맵</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">업종 선택</h3><div class="note-text"><p>본인 체력·성향·경력을 고려해 1~2개 주력 업종을 정합니다.</p><p>아래 업종별 가이드에서 평균 단가·근무 패턴·필요 역량을 확인하세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">면접 준비</h3><div class="note-text"><p>샵이 가장 많이 묻는 질문은 \"가능 시술 시간대\", \"기존 단골 인수 가능 여부\", \"체력 수준\"입니다.</p><p>1,200건 면접 데이터에서 도출한 합격 패턴은 <a href=\"/magazine/interview-tips/\" style=\"color:var(--blue-1)\">매거진</a>에서 확인하세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">계약 체크</h3><div class="note-text"><p>인센티브 비율·정산 주기·세금 처리·교통비·복장 규정 — 9가지 핵심 체크리스트가 있습니다.</p><p>분쟁의 80%는 이 단계에서 막을 수 있습니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">정착 · 단골 만들기</h3><div class="note-text"><p>입사 30일 안에 단골 5명을 만드는 패턴이 있습니다.</p><p>응대 매뉴얼·시술 일관성·재방문 유도 — 신규 입직자를 위한 30일 로드맵 참고.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>업종별 구직 가이드</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:30px">{svc_cards}</div>
</section>
"""
    return page(title, desc, "/seekers/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 업종별 구직 가이드
# ─────────────────────────────────────────────
def build_seeker_service(s):
    title = f"{s['kr']} 구직 가이드 — 면접·단가·근무 환경 완벽 정리 | {COMPANY['brand_kr']}"
    desc = f"{s['kr']} 마사지 관리사 구직자를 위한 종합 가이드. 평균 단가 {s['pay_range']}, 면접에서 자주 묻는 질문, 정착 전략까지 정리."

    extra_ld = [
        breadcrumb_ld([("홈","/"),("구직 가이드","/seekers/"),(f"{s['kr']} 구직","/seekers/"+s["slug"]+"/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">{s['kicker']}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{s['kr']} 구직<br><span class="grad">완벽 가이드</span></h1>
  <p class="lead">{s['summary']}</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>이 업종이 나에게 맞는가</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">신체·체력 요건</h3><div class="note-text"><p>{s['kr']} 시술은 1일 평균 6~8명 시술이 표준입니다.</p><p>1회당 60~120분 — 체력 회복 루틴(스트레칭·식단·수면)이 직업적으로 필요합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">필수 기술</h3><div class="note-text"><p>{', '.join(s['skills'])} — 이 3가지는 면접 시 시연을 요청받을 수 있습니다.</p><p>신규 입직자는 견습 1~2주 동안 위 기술을 익힙니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">수입 시뮬레이션</h3><div class="note-text"><p>주 5일 근무 기준 월 환산 {s['pay_avg']}.</p><p>인센티브 50% 구조에서 1일 7명 시술 · 객단가 9만원이면 월 약 470만원 수준입니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">단점·주의점</h3><div class="note-text"><p>장시간 시술로 손목·어깨 부담이 누적됩니다. 정기 마사지 교환과 스트레칭 루틴이 필수입니다.</p><p>야간 라인은 수면 패턴이 흐트러질 수 있어 적응 기간이 필요합니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>면접에서 자주 묻는 5가지</h2>
  <div style="max-width:860px;margin:30px auto 0">
    <details><summary>Q1. 가능한 근무 시간대는?<span>+</span></summary><div>샵 운영 시간과 본인 라이프 패턴을 맞춰야 합니다. 주간(10~22시)·야간(14~02시) 중 선호와 가능 시간을 명확히 답하세요.</div></details>
    <details><summary>Q2. 기존 단골을 인수할 수 있나요?<span>+</span></summary><div>이전 샵 단골을 새 샵으로 데려오는 것은 권장되지 않습니다. 영업 분쟁의 원인이 됩니다. \"신규 단골은 빠르게 만들 자신이 있다\"가 정답입니다.</div></details>
    <details><summary>Q3. 객단가 올리기 자신 있나요?<span>+</span></summary><div>{s['kr']}의 평균 객단가 상승 전략(코스 업셀·연장·추가 옵션 제안)을 1~2개 사례로 설명하세요.</div></details>
    <details><summary>Q4. 인센티브 비율 협상은?<span>+</span></summary><div>전국 평균 45~55%입니다. 경력·자격증·과거 매출 실적이 있으면 50% 이상을 요청할 수 있습니다.</div></details>
    <details><summary>Q5. 첫 출근까지 일정은?<span>+</span></summary><div>면접 합격 후 평균 47시간 안에 첫 출근합니다. 견습이 필요한 신규 입직자는 +1주.</div></details>
  </div>
</section>

<section class="wrap" style="padding-top:0;text-align:center">
  <a class="btn btn-primary" href="/jobs/{s['slug']}/">{s['kr']} 모집 중인 공고 보기 →</a>
</section>
"""
    return page(title, desc, f"/seekers/{s['slug']}/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 매니저(국적) 허브
# ─────────────────────────────────────────────
def build_therapists_hub():
    title = f"국적별 마사지 관리사 — 한국·중국·태국·베트남·러시아·일본 채용 가이드 | {COMPANY['brand_kr']}"
    desc = "한국·중국·태국·베트남·러시아·일본 6개국 출신 마사지 관리사의 채용 시장 특성과 평균 단가, 합법 체류 조건을 정리한 가이드."

    cards = ""
    for n in NATIONALITIES:
        cards += f"""<a class="job-card reveal" href="/therapists/{n['slug']}/">
  <div class="top"><span class="kicker">{n['en'].upper()}</span><span class="badge NEW">{n['demand']}</span></div>
  <h3>{n['kr']}</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{n['summary']}</p>
  <div class="pay">{n['common_pay']}</div>
</a>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("관리사","/therapists/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">BY NATIONALITY</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">국적별 관리사<br><span class="grad">채용 시장</span> <span class="serif">가이드.</span></h1>
  <p class="lead">한국·중국·태국·베트남·러시아·일본 6개국 출신 관리사의 채용 시장 특성, 강점, 평균 단가, 합법 체류 조건을 한눈에 정리했습니다.</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>국적별 채용 가이드</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-top:30px">{cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>합법 체류 안내</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">F-4·F-5·F-6 (영주·결혼이민·재외동포)</h3><div class="note-text"><p>업종 제한 없이 자유롭게 취업 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">H-2 (방문취업)</h3><div class="note-text"><p>서비스업 취업 가능. 마사지업도 포함됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">E-9·E-10</h3><div class="note-text"><p>특정 업종 한정이며, 마사지업은 일반적으로 해당되지 않습니다. 별도 확인이 필요합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">D-10·E-7 등</h3><div class="note-text"><p>전문 기술·자격 기반 비자. 마사지 자격증(예: 태국 와트포 인증) 보유 시 일부 신청 가능합니다.</p></div></div></div>
  </div>
  <p class="lead" style="margin-top:24px;font-size:13.5px;color:var(--dim)">※ 본 안내는 일반 정보이며, 개별 사안은 법무부 출입국·외국인정책본부(www.immigration.go.kr) 또는 행정사·변호사 자문을 받으세요.</p>
</section>
"""
    return page(title, desc, "/therapists/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 국적별 관리사 페이지 (6개)
# ─────────────────────────────────────────────
def build_therapist(n):
    title = f"{n['kr']} 마사지 관리사 채용 — 강점·평균 단가·합법 체류 | {COMPANY['brand_kr']}"
    desc = f"{n['kr']} 출신 마사지 관리사의 채용 시장 특성, 강점, 평균 단가({n['common_pay']}), 합법 체류 조건을 정리합니다."

    adv_p = "".join(f"<p>{a}</p>" for a in n["advantages"])

    extra_ld = [
        breadcrumb_ld([("홈","/"),("관리사","/therapists/"),(n["kr"],"/therapists/"+n["slug"]+"/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">{n['en'].upper()}</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">{n['kr']} 관리사<br><span class="grad">{n['demand']}</span></h1>
  <p class="lead">{n['summary']}</p>
  <div style="display:flex;gap:14px;flex-wrap:wrap;margin-top:30px">
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">평균 단가</div><div style="font-size:18px;font-weight:800;margin-top:4px">{n['common_pay']}</div></div>
    <div style="padding:14px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">채용 수요</div><div style="font-size:18px;font-weight:800;margin-top:4px">{n['demand']}</div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>현장에서 강점</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">시장 평가</h3><div class="note-text">{adv_p}</div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">선호 업종</h3><div class="note-text"><p>현재 가장 채용 매칭이 활발한 업종은 권역별·시즌별로 다릅니다.</p><p>본 사이트의 <a href=\"/jobs/\" style=\"color:var(--blue-1)\">전체 공고</a>에서 \"관리사 국적\" 필터를 활용하면 정확한 매칭이 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">합법 체류 확인</h3><div class="note-text"><p>채용 시 F-4·F-5·F-6·H-2 등 합법 체류 자격 확인은 필수입니다.</p><p>채용 후 비자 변경이 필요한 경우 행정사·변호사 자문을 권장합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">한국 정착 지원</h3><div class="note-text"><p>한국어 교육·세금 처리·계약서 검토 등 정착 초기 도움이 필요한 경우, 운영팀이 가능한 범위에서 안내합니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0;text-align:center">
  <a class="btn btn-primary" href="/jobs/">{n['kr']} 관리사 모집 중인 공고 →</a>
</section>
"""
    return page(title, desc, f"/therapists/{n['slug']}/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 매거진 허브
# ─────────────────────────────────────────────
def build_magazine_hub():
    title = f"매거진 — 마사지 관리사 급여·면접·계약 가이드 | {COMPANY['brand_kr']}"
    desc = "마사지 관리사를 위한 실전 가이드. 급여 시세·면접 준비·계약 체크리스트·정착 로드맵 — 16개월 1차 데이터 기반."

    cards = ""
    for m in MAGAZINE:
        cards += f"""<a class="job-card reveal" href="/magazine/{m['slug']}/">
  <div class="top"><span class="kicker">{m['tag']}</span><span style="font-size:11px;color:var(--muted)">{m['minutes']}분 읽기</span></div>
  <h3 style="line-height:1.4">{m['title']}</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{m['summary']}</p>
  <div class="id" style="margin-top:8px">{m['date']}</div>
</a>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("매거진","/magazine/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">MAGAZINE</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">관리사를 위한<br><span class="grad">실전 가이드</span></h1>
  <p class="lead">마사지 관리사가 실제 현장에서 부딪히는 문제 — 급여, 면접, 계약, 정착, 안전 — 을 16개월간 누적된 1차 데이터로 정리합니다.</p>
</section>

<section class="wrap" style="padding-top:0">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px">{cards}</div>
</section>
"""
    return page(title, desc, "/magazine/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 매거진 글 페이지
# ─────────────────────────────────────────────
MAGAZINE_BODIES = {
    "salary-guide-2026": [
        ("2026년, 마사지 업계는 어떻게 달라졌나",
         ["2025년 1월~2026년 5월 사이 16개월간 누적된 자체 매칭 로그 23,700건을 분석한 결과, 마사지 관리사 평균 일급은 전년 대비 8.4% 상승했습니다.",
          "상승의 가장 큰 동력은 \"신축 프리미엄 샵\"의 증가입니다. 강남·판교·해운대를 중심으로 객단가 10만원 이상의 코스를 운영하는 샵이 늘면서, 단가가 위쪽으로 끌어올려졌습니다.",
          "반면 외곽 권역은 단가 변동이 5% 이내로 안정적입니다."]),
        ("업종별 평균 일급 (전국)",
         ["스웨디시: 12~22만원 / 월 380~620만원 — 가장 채용 시장이 넓은 기본 업종.",
          "아로마: 13~24만원 / 월 400~680만원 — 프리미엄 라인 비중이 높아 단가 안정.",
          "타이: 14~26만원 / 월 420~720만원 — 시술 회전이 빨라 인센티브 효율이 좋음.",
          "로미로미: 15~28만원 / 월 450~760만원 — 객단가 최상위. 교육 이수 우대.",
          "스포츠: 16~30만원 / 월 480~820만원 — 자격증 보유 시 추가 가산."]),
        ("지역별 단가 보정 — 같은 업종, 다른 단가",
         ["전국 평균을 기준 100으로 봤을 때, 권역별 보정 지수는 다음과 같습니다.",
          "강남·서초·송파(서울): 115~125 — 단가 최상위.",
          "마포·용산(서울): 108~115 — 야간 라인 비중이 높음.",
          "분당·판교(경기): 112~120 — IT 종사자 단골 비중이 높아 안정.",
          "해운대·서면(부산): 110~118 — 부산 최상위 권역.",
          "외곽 시·군: 78~95 — 출퇴근 시간이 길고 단가가 낮지만, 단골 비중이 높아 수입 안정성이 큼."]),
        ("실제 수입 시뮬레이션",
         ["주 5일 · 1일 7명 시술 · 객단가 9만원 · 인센티브 50% 기준으로 계산하면 월 약 470만원입니다.",
          "여기에 단가 보정 +15%(강남) 또는 -10%(외곽)을 적용하면 540만원 / 425만원이 됩니다.",
          "프리미엄 라인(로미로미·스포츠)은 같은 조건에서 600~700만원도 가능합니다."]),
        ("앞으로 1년 — 무엇이 달라질까",
         ["1) 신축 샵 증가는 2027년 상반기까지 이어질 전망. 단가 상승 압력이 유지됩니다.",
          "2) 외국인 고객 응대 가능 관리사의 단가 프리미엄이 확대됩니다(이태원·송도·해운대).",
          "3) 자격증·교육 이수 증명을 요구하는 샵이 늘고 있어, 장기적으로 \"전문화\"가 키워드."])
    ],
    "interview-tips": [
        ("1,200건 면접 데이터 — 합격률 95%의 공통점",
         ["테라피잡 운영팀이 16개월간 추적한 1,200건의 면접 결과 중, 95% 이상 합격률을 보인 관리사 38명의 면접 답변을 분석했습니다.",
          "이들의 공통점은 \"테크닉\"이 아니라 \"태도와 답변 구조\"였습니다."]),
        ("공통점 1 — 가능 시간대를 먼저 명확히 답한다",
         ["샵은 가장 먼저 \"몇 시부터 몇 시까지 가능한가\"를 묻습니다.",
          "합격자들은 \"평일 14시~24시, 토요일 11시~22시 가능합니다\"처럼 시간을 숫자로 명시합니다.",
          "\"상의 가능합니다\" 같은 모호한 답변은 -30% 합격률."]),
        ("공통점 2 — 기존 단골 인수 요청을 하지 않는다",
         ["이전 샵 단골을 가져오겠다는 제안은 영업 분쟁의 원인. 샵은 거부 반응을 보입니다.",
          "\"신규 단골을 빠르게 만들 자신이 있다\"가 정답."]),
        ("공통점 3 — 객단가 상승 전략을 1~2개 사례로 설명",
         ["\"60분 코스를 받으신 분께 90분 연장을 자연스럽게 제안해 30% 업셀 성공한 경험이 있습니다\" 같은 구체적 사례.",
          "샵 입장에서 매출 기여 가능성이 가장 직접적인 증거."]),
        ("공통점 4 — 인센티브 협상은 마지막에",
         ["면접 초반에 단가 협상을 시작하면 \"돈만 생각한다\"는 인상.",
          "기술·태도·매출 기여 설명이 끝난 뒤 마지막 5분에 단가를 협상하는 것이 정답."]),
        ("공통점 5 — 정장보다 \"청결\"",
         ["면접 복장은 캐주얼해도 됩니다. 단, 손톱·복장·머리 청결도가 합격 결정의 23%를 차지.",
          "\"청결한 사람이 청결한 시술을 한다\"는 샵의 직관."]),
        ("공통점 6 — 질문을 1~2개 준비한다",
         ["\"정산 주기는 어떻게 되나요?\" \"단골 관리 시스템이 있나요?\" 같은 운영 관련 질문.",
          "\"휴무는 어떻게 되나요?\" 만 묻는 지원자는 -15% 합격률."]),
        ("공통점 7 — 첫 출근 가능 일자를 묻는다",
         ["\"언제부터 출근 가능한가요?\"를 면접 마지막에 본인이 먼저 묻습니다.",
          "샵 입장에서는 \"이 사람은 진짜 일할 사람\"이라는 신호."])
    ],
    "contract-checklist": [
        ("프리랜서 계약은 \"애매하면 분쟁\"",
         ["마사지 관리사의 90% 이상은 프리랜서 계약(3.3% 원천징수)입니다.",
          "계약서 한 줄이 빠지거나 모호하면, 정산 분쟁·근무 조건 불일치로 이어집니다.",
          "아래 9가지 항목은 계약서에 반드시 명시되어야 합니다."]),
        ("1. 인센티브 계산 기준",
         ["\"총 매출의 50%\"인지, \"순 매출(카드 수수료·기타 비용 제외)의 50%\"인지 반드시 명시.",
          "기준이 다르면 월 30~50만원 차이가 납니다."]),
        ("2. 정산 주기와 입금 일자",
         ["일정산·주정산·월정산 중 어느 것인지 명시.",
          "입금 일자도 \"매주 월요일\" 식으로 구체적으로."]),
        ("3. 휴무·연차 정책",
         ["주 1~2일 휴무 기준일·연차 사용 가능 여부를 명시.",
          "휴무일 출근 시 단가 가산 여부도 함께."]),
        ("4. 교통비·식대",
         ["출장 라인은 교통비 지급 기준(자차 km당·대중교통 실비)을 명시.",
          "샵 상주는 식대(5,000~10,000원) 지급 여부."]),
        ("5. 복장·소품 책임",
         ["유니폼 제공 여부, 신발·소품·개인 위생용품의 부담 주체.",
          "이 부분이 모호하면 분쟁의 출발점."]),
        ("6. 단가 변경 절차",
         ["객단가·인센티브 비율 변경 시 며칠 전 통보, 본인 동의 필요 여부.",
          "샵이 일방적으로 단가를 내리는 것을 막는 장치."]),
        ("7. 계약 해지 조건과 통보 기간",
         ["관리사·샵 어느 쪽이든 해지 시 며칠 전 통보(보통 7~14일).",
          "위반 시 위약금 조항도 확인."]),
        ("8. 비밀 유지 · 경업 금지",
         ["일부 샵은 \"퇴사 후 반경 1km 내 동일 업종 취업 금지\" 같은 조항을 넣습니다.",
          "법적으로 무효일 수 있지만, 분쟁 시 시간 낭비. 가급적 삭제 요청."]),
        ("9. 분쟁 해결 절차",
         ["분쟁 시 협의 우선·관할 법원을 명시.",
          "운영팀 중재를 받을 수 있는 플랫폼(예: 테라피잡)을 통해 매칭된 경우, 중재 절차를 명시하면 시간을 크게 아낄 수 있습니다."])
    ],
    "newbie-roadmap": [
        ("입직 30일 — 단골 5명을 만드는 표준 로드맵",
         ["신규 입직자의 가장 큰 고민은 \"단골이 안 생긴다\"입니다.",
          "16개월간 누적된 신규 입직자 412명의 30일 데이터를 분석한 결과, 단골 5명을 만드는 표준 패턴이 있었습니다."]),
        ("Day 1~7 — 기본기 다지기",
         ["견습 1주차. 샵 시술 매뉴얼·동선·응대 톤을 익힙니다.",
          "이 시기 단가는 기준 단가의 60~70%이지만, 빠르게 익히면 1주차 말부터 정상 단가로 전환됩니다."]),
        ("Day 8~14 — 시술 일관성",
         ["같은 코스에 같은 결과를 만드는 것이 핵심.",
          "본인의 \"시그니처 스트로크\" 1개를 정해 모든 시술에 포함시키면, 고객이 기억하기 쉽습니다."]),
        ("Day 15~21 — 응대 매뉴얼화",
         ["시술 전 5문장·시술 후 3문장을 본인의 톤으로 미리 만들어 두세요.",
          "\"오늘 어디가 가장 무거우신가요?\" \"이 부분 풀어드리고 어깨 추가로 봐드릴게요\" 같은 구체적 표현."]),
        ("Day 22~30 — 재방문 유도",
         ["시술 마지막에 \"오늘 풀어드린 부분이 1~2일 후 다시 무거워질 수 있으니, 다음 주 같은 시간대 예약 한 자리 잡아드릴까요?\"",
          "이 한 문장이 단골 5명 만들기의 핵심.",
          "표준 패턴을 따른 신규 입직자의 86%가 30일 내 단골 5명을 확보했습니다."])
    ],
    "shop-vs-freelance": [
        ("샵 소속 vs 출장 프리랜서 — 5개 축 비교",
         ["같은 \"마사지 관리사\"라도 샵 소속과 출장 프리랜서는 일하는 방식·수입 구조·세금이 다릅니다.",
          "5개 축으로 비교해 본인에게 맞는 형태를 찾으세요."]),
        ("축 1 — 수입",
         ["샵 소속: 일급 12~28만원 (안정적)",
          "출장 프리: 1콜 8~25만원 + 교통비 (변동 큼). 콜 수에 따라 +30% 가능하지만 -30%도 가능."]),
        ("축 2 — 근무 시간",
         ["샵 소속: 정해진 시간 출근. 빈 시간도 대기.",
          "출장 프리: 콜이 있을 때만 일함. 자유롭지만 콜이 없으면 수입 0."]),
        ("축 3 — 안정성",
         ["샵 소속: 단골이 샵에 귀속. 본인이 옮기면 단골 손실.",
          "출장 프리: 단골이 본인에게 귀속. 이동의 자유."]),
        ("축 4 — 세금·4대 보험",
         ["샵 소속·정규직: 4대 보험 자동 가입.",
          "샵 소속·프리랜서: 3.3% 원천징수, 4대 보험 없음.",
          "출장 프리: 본인이 직접 종합소득세 신고. 4대 보험 없음."]),
        ("축 5 — 위험·리스크",
         ["샵 소속: 샵 분쟁·운영 리스크 일부 공유.",
          "출장 프리: 안전 리스크·고객 매너 리스크가 본인에게 100% 귀속. 사전 검증이 필수."]),
        ("어느 쪽을 선택할까",
         ["입직 1~2년차: 샵 소속 권장. 기술·단골·응대 패턴을 안정적으로 익힐 수 있음.",
          "3년차 이상 + 단골 보유: 출장 프리 검토 가능. 단, 안전·세금 처리 시스템을 먼저 갖춰야 함."])
    ],
    "safe-workplace": [
        ("7가지 위험 신호 — 면접 단계에서 걸러야 할 것들",
         ["안전한 일터를 고르는 것은 수입을 올리는 것만큼 중요합니다.",
          "운영팀이 분쟁 신고 218건을 분석한 결과, 다음 7가지 신호가 가장 자주 문제로 이어졌습니다."]),
        ("신호 1 — 사업자등록증 공개를 꺼린다",
         ["정상 샵은 면접 시 사업자등록증을 보여달라고 하면 즉시 보여줍니다.",
          "\"나중에 보여드릴게요\" 라고 미루면 위험 신호."]),
        ("신호 2 — 계약서가 없다",
         ["\"우리는 계약서 안 써요. 다 구두로 해요\" 라는 샵은 100% 거르세요.",
          "분쟁 시 본인이 100% 불리."]),
        ("신호 3 — 인센티브 비율이 비현실적으로 높음",
         ["\"인센티브 70% 드립니다\" 같은 광고는 의심.",
          "정상 시세는 45~55%. 70%는 다른 비용을 떠넘기는 구조일 가능성."]),
        ("신호 4 — 일급이 시세 대비 2배 이상",
         ["\"일급 50만원 보장\" 같은 광고는 시세 대비 비현실적.",
          "성매매·유사성행위 강요 가능성. 즉시 신고하세요."]),
        ("신호 5 — 신분증 보관 요구",
         ["\"신분증을 맡겨주세요\" 는 노동법 위반.",
          "어떤 이유로도 거부하세요."]),
        ("신호 6 — 24시간 운영·새벽 콜",
         ["일부 정상 샵도 24시간이지만, \"새벽 콜 못 거부\" 같은 조건은 위험.",
          "본인 안전·건강에 직접적 영향."]),
        ("신호 7 — 운영팀·책임자가 익명",
         ["대표·실장의 실명을 알려주지 않거나, 연락 두절이 잦은 샵.",
          "분쟁 발생 시 책임 추궁이 불가능."]),
        ("정상 샵의 공통 특징",
         ["1) 사업자등록증·통신판매업 신고증을 즉시 공개.",
          "2) 계약서를 미리 보여주고 함께 검토.",
          "3) 인센티브·정산을 숫자로 명시.",
          "4) 운영팀 실명·연락처를 공개.",
          "5) 신규 입직자 견습 과정을 시스템화."])
    ],
    "newcomer-shop-guide": [
        ("신축 샵 — 단가가 가장 많이 오르는 \"틈새\"",
         ["신축 샵은 1) 단가가 높고, 2) 단골이 비어 있어 빠르게 확보 가능하며, 3) 운영팀이 적극적이라는 장점이 있습니다.",
          "다만 운영이 미숙해 시스템 분쟁 위험도 있어, 평가가 중요합니다."]),
        ("신축 샵을 빠르게 찾는 방법",
         ["1) 테라피잡 공고 필터에서 \"신축 (3개월 이내)\" 정렬.",
          "2) 권역별 운영팀에 \"신축 정보 알림\" 요청.",
          "3) 평소 매거진·뉴스레터 구독."]),
        ("첫 면접에서 확인할 5가지",
         ["1) 운영 시스템: 예약 관리·정산 시스템이 있는가? (수기 정산은 위험)",
          "2) 견습 과정: 신규 관리사 교육 시스템이 있는가?",
          "3) 단가 정책: 객단가가 시세 수준인가? (너무 낮으면 수익성, 너무 높으면 손님 안 옴)",
          "4) 마케팅: 어떻게 손님을 모을 계획인가? (블로그·SNS·지도 노출)",
          "5) 본인 외 관리사: 다른 관리사가 몇 명인가? 1인 샵은 단골 의존도가 높음."]),
        ("신축 샵 정착 패턴",
         ["첫 1개월: 본인 시술 일관성 확보 + 응대 톤 정립.",
          "2~3개월차: 단골 10명 목표. 신축은 단골 확보 속도가 일반 샵의 1.5배 빠름.",
          "4개월차 이후: 단가 재협상 가능. 본인 매출 기여도가 명확하면 인센티브 +5% 협상."])
    ],
}

def build_magazine_article(m):
    sections = MAGAZINE_BODIES.get(m["slug"], [])
    title = f"{m['title']} | {COMPANY['brand_kr']} 매거진"
    desc = m["summary"]

    body_sections = ""
    toc = []
    for i,(h, ps) in enumerate(sections):
        toc.append((h, f"sec-{i+1}"))
        ptext = "".join(f"<p>{p}</p>" for p in ps)
        body_sections += f"""<div class="note-card reveal"><div class="note-num">{i+1:02d}</div><div class="note-content"><h3 class="note-title" id="sec-{i+1}">{h}</h3><div class="note-text">{ptext}</div></div></div>"""

    toc_html = "".join(f'<li><a href="#{aid}" style="color:var(--blue-1);font-size:13.5px">{h}</a></li>' for h,aid in toc)

    extra_ld = [
        breadcrumb_ld([("홈","/"),("매거진","/magazine/"),(m["title"],f"/magazine/{m['slug']}/")]),
        {
            "@type":"Article",
            "@id":f"{COMPANY['base_url']}/magazine/{m['slug']}/#article",
            "headline":m["title"],
            "description":m["summary"],
            "datePublished":m["date"]+"T09:00:00+09:00",
            "dateModified":"2026-05-22T09:00:00+09:00",
            "author":{"@type":"Organization","@id":f"{COMPANY['base_url']}/#organization","name":f"{COMPANY['brand_kr']} 편집팀"},
            "publisher":{"@id":f"{COMPANY['base_url']}/#organization"},
            "mainEntityOfPage":{"@type":"WebPage","@id":f"{COMPANY['base_url']}/magazine/{m['slug']}/"},
            "inLanguage":"ko-KR",
            "articleSection":m["tag"]
        }
    ]

    body = f"""
<section class="wrap" style="padding-bottom:30px">
  <div style="font-size:12px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:14px"><a href="/magazine/" style="color:var(--blue-1)">매거진</a> · {m['tag']} · {m['minutes']}분 읽기</div>
  <h1 style="font-size:clamp(32px,5vw,52px);line-height:1.25;margin-bottom:20px">{m['title']}</h1>
  <p class="lead">{m['summary']}</p>
  <div style="display:flex;gap:16px;margin-top:24px;font-size:13px;color:var(--muted)">
    <span>{COMPANY['brand_kr']} 편집팀</span><span>·</span><span>{m['date']}</span>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="padding:24px 28px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line);margin-bottom:40px">
    <div class="kicker">목차</div>
    <ul style="list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:8px">{toc_html}</ul>
  </div>
  <div class="note-stack">{body_sections}</div>
</section>

<section class="wrap" style="padding-top:0;text-align:center">
  <a class="btn btn-primary" href="/magazine/">매거진 더 보기 →</a>
</section>
"""
    return page(title, desc, f"/magazine/{m['slug']}/", body, extra_jsonld=extra_ld)
