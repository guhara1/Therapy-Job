"""핵심 페이지 생성 — 메인, About, Contact, Pricing, Reviews, Policy"""
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import SERVICES, NATIONALITIES, REGIONS, MAGAZINE, SAMPLE_JOBS, TEAM, DISTRICTS, AD_TIERS, PRICING_ADS
from ads import render_all_tiers, AD_CSS, filter_jobs, render_card, render_tier_section, single_tier_block

# ─────────────────────────────────────────────
# 메인 페이지
# ─────────────────────────────────────────────
def build_index():
    title = f"{COMPANY['brand_kr']} — 전국 마사지 구인구직 1번지 | 스웨디시·아로마·타이·로미로미·스포츠"
    desc = f"마사지 관리사 구인구직 · 전국 82개 행정구 · 5,820여건 채용 공고 · 매일 업데이트. 샵·관리사 연결 평균 47시간. 직업정보제공사업 신고 {COMPANY['job_info_reg']}."

    # 광고 3단계는 ads.py 헬퍼로 일괄 렌더링됨

    svc_cards = ""
    for s in SERVICES:
        svc_cards += f"""<a class="job-card reveal" href="/jobs/{s['slug']}/">
  <div class="top"><span class="kicker">{s['kicker']}</span><span class="badge BEST">{s['openings']:,}건</span></div>
  <h3>{s['kr']} 구인공고</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{s['summary']}</p>
  <div class="pay">{s['pay_range']}</div>
</a>"""

    region_cards = ""
    for r in REGIONS:
        sample = ", ".join([d[1] for d in DISTRICTS[r["slug"]][:5]])
        region_cards += f"""<a class="job-card reveal" href="/locations/{r['slug']}/">
  <div class="top"><span class="kicker">{r['en'].upper()}</span><span class="badge NEW">{r['openings']:,}건</span></div>
  <h3>{r['kr']} {r['districts_count']}개 행정구</h3>
  <p style="font-size:13.5px;color:var(--muted);line-height:1.7;margin-top:4px">{r['summary']}</p>
  <div class="meta" style="margin-top:4px">{sample}</div>
</a>"""

    team_cards = ""
    for t in TEAM:
        team_cards += f"""<div class="note-card reveal">
  <div class="note-num">●</div>
  <div class="note-content">
    <h3 class="note-title">{t['name']} <span style="font-size:13px;color:var(--blue-1);font-weight:600;margin-left:8px">{t['role']}</span></h3>
    <div class="note-text"><p style="color:var(--muted)">{t['credit']}</p></div>
  </div>
</div>"""

    faqs = [
        ("테라피잡은 어떤 서비스인가요?",
         f"테라피잡은 마사지·테라피 업종에 특화된 구인구직 플랫폼입니다. 전국 82개 행정구의 샵 채용 정보와 관리사 구직 정보를 매일 업데이트합니다. 직업정보제공사업 신고({COMPANY['job_info_reg']})를 마친 합법 플랫폼입니다."),
        ("관리사 등록은 무료인가요?",
         "구직자(관리사) 등록 및 공고 열람은 100% 무료입니다. 모든 채용 매칭은 노동관계법령을 준수하여 진행됩니다."),
        ("샵에서 공고 등록은 어떻게 하나요?",
         f"고객센터 {COMPANY['tel']}로 연락 주시면 담당자가 공고 등록 절차를 안내드립니다. 직업정보제공사업 약관에 따라 검증 후 게재됩니다."),
        ("어떤 업종을 다루나요?",
         "스웨디시·아로마·타이·로미로미·스포츠 5개 업종이 주력입니다. 발마사지·중국식·일식 등 세부 라인도 공고에 포함됩니다."),
        ("지역은 어디까지 다루나요?",
         "서울 25개 자치구, 경기 31개 시·군, 인천 10개 구·군, 부산 16개 구·군 — 총 82개 행정구를 풀커버합니다. 대전·대구·광주는 2026년 4분기 확장 예정입니다."),
        ("개인정보는 어떻게 보호되나요?",
         f"개인정보처리방침에 따라 암호화 저장되며, 본인 동의 없이 제3자에게 제공되지 않습니다. 책임자는 {COMPANY['privacy_officer']}({COMPANY['email']})입니다."),
    ]

    extra_ld = [
        breadcrumb_ld([("홈","/")]),
        faq_ld(faqs),
        {
            "@type":"WebPage",
            "@id":f"{COMPANY['base_url']}/#webpage",
            "url":COMPANY["base_url"]+"/",
            "name":title,
            "description":desc,
            "inLanguage":"ko-KR",
            "isPartOf":{"@id":f"{COMPANY['base_url']}/#website"},
            "about":{"@type":"Thing","name":"마사지 구인구직"},
            "datePublished":"2026-01-15",
            "dateModified":"2026-05-22"
        },
        {
            "@type":"Service",
            "name":"마사지 구인구직 매칭 서비스",
            "provider":{"@id":f"{COMPANY['base_url']}/#organization"},
            "areaServed":[{"@type":"AdministrativeArea","name":r["kr"]} for r in REGIONS],
            "serviceType":"채용 정보 제공",
            "audience":{"@type":"Audience","audienceType":"마사지 관리사 · 마사지샵 운영자"}
        }
    ]

    body = f"""
<section class="wrap" style="padding-top:60px;padding-bottom:60px">
  <div style="display:grid;grid-template-columns:1.15fr .85fr;gap:60px;align-items:center" class="hero-grid">
    <div>
      <span class="eyebrow"><span class="pulse"></span>LIVE · 오늘 247건 신규 공고</span>
      <h1 style="font-size:clamp(40px,6.5vw,76px);font-weight:800;letter-spacing:-.038em;margin:18px 0">샵과 관리사를<br>잇는 가장 <span class="grad">정확한</span><br><span class="serif">한 줄.</span></h1>
      <p class="lead">전국 82개 행정구 · 5,820여건 마사지 채용 공고를 매일 정제해 공개합니다. 평균 매칭까지 47시간. 직업정보제공사업 신고를 마친 합법 플랫폼입니다.</p>
      <div style="display:flex;gap:12px;margin-top:28px;flex-wrap:wrap">
        <a class="btn btn-primary" href="/jobs/">구인공고 보기 →</a>
        <a class="btn btn-ghost" href="/seekers/">구직 가이드</a>
      </div>
      <div style="margin-top:24px;display:flex;gap:20px;flex-wrap:wrap;font-size:13px;color:var(--muted)">
        <span>★★★★★ · 4.92 · 매칭 만족도</span>
        <span>· 평균 매칭 47시간</span>
        <span>· 누적 매칭 23,700건</span>
      </div>
    </div>
    <div style="position:relative">
      <div style="padding:28px 28px;border-radius:22px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);backdrop-filter:blur(20px);transform:rotate(1deg)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px"><span class="kicker">FEATURED · 추천 공고</span><span style="font-size:11px;color:var(--blue-1)">● 모집 중</span></div>
        <h3 style="font-size:18px;margin-bottom:12px;line-height:1.4">강남 프리미엄 스웨디시샵<br>정규 관리사 즉시 출근</h3>
        <div style="display:flex;flex-direction:column;gap:9px;font-size:13.5px;color:var(--muted);padding:14px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
          <div style="display:flex;justify-content:space-between"><span>지역</span><span style="color:var(--text)">서울 강남구 역삼동</span></div>
          <div style="display:flex;justify-content:space-between"><span>업종</span><span style="color:var(--text)">스웨디시 · 60·90·120분</span></div>
          <div style="display:flex;justify-content:space-between"><span>일급</span><span style="color:var(--blue-1);font-weight:700">18만~24만원</span></div>
          <div style="display:flex;justify-content:space-between"><span>인센티브</span><span style="color:var(--text)">50% (협의 가능)</span></div>
          <div style="display:flex;justify-content:space-between"><span>근무</span><span style="color:var(--text)">주 5일 · 14:00~24:00</span></div>
        </div>
        <a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:18px" href="/jobs/swedish/">상세 보기 →</a>
      </div>
      <div style="position:absolute;top:-14px;right:-10px;padding:10px 14px;border-radius:12px;background:rgba(18,24,40,.92);backdrop-filter:blur(20px);border:1px solid var(--line);font-size:11px;letter-spacing:.16em;font-weight:700;color:var(--blue-1);transform:rotate(-3deg)">● 8분 전 매칭 성사</div>
      <div style="position:absolute;bottom:-12px;left:-14px;padding:10px 14px;border-radius:12px;background:rgba(18,24,40,.92);backdrop-filter:blur(20px);border:1px solid var(--line);font-size:11px;letter-spacing:.16em;font-weight:700;color:var(--gold);transform:rotate(2deg)">★ 4.92 · 매칭 만족도</div>
    </div>
  </div>
</section>

<style>@media(max-width:920px){{.hero-grid{{grid-template-columns:1fr!important;gap:40px!important}}}}</style>

<section style="padding:18px 0;background:linear-gradient(90deg,rgba(91,155,255,.04),rgba(44,84,168,.02));border-top:1px solid var(--line);border-bottom:1px solid var(--line);overflow:hidden">
  <div style="display:flex;gap:40px;animation:scroll 40s linear infinite;white-space:nowrap;font-size:13px;color:var(--muted);font-weight:600;letter-spacing:.08em">
    <span>● 서울 25개 자치구</span><span>● 경기 31개 시·군</span><span>● 인천 10개 구·군</span><span>● 부산 16개 구·군</span><span>● 스웨디시 1,840건</span><span>● 아로마 1,120건</span><span>● 타이 760건</span><span>● 로미로미 380건</span><span>● 스포츠 290건</span><span>● 누적 매칭 23,700건</span><span>● 매칭 만족도 4.92</span>
    <span>● 서울 25개 자치구</span><span>● 경기 31개 시·군</span><span>● 인천 10개 구·군</span><span>● 부산 16개 구·군</span><span>● 스웨디시 1,840건</span><span>● 아로마 1,120건</span><span>● 타이 760건</span><span>● 로미로미 380건</span><span>● 스포츠 290건</span><span>● 누적 매칭 23,700건</span><span>● 매칭 만족도 4.92</span>
  </div>
  <style>@keyframes scroll{{to{{transform:translateX(-50%)}}}}</style>
</section>

{single_tier_block("vvip", filter_jobs(tier="vvip"), include_css=True, padding_top=20)}

<section class="wrap" style="padding-top:20px">
  <div style="text-align:center;max-width:760px;margin:0 auto 60px">
    <span class="kicker">BY SERVICE</span>
    <h2>업종별 채용 현황</h2>
    <p class="lead" style="margin:18px auto 0">5개 핵심 업종의 평균 일급 시세와 현재 모집 중인 공고 수를 한눈에 정리했습니다.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px">{svc_cards}</div>
</section>

{single_tier_block("vip", filter_jobs(tier="vip"))}

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 60px">
    <span class="kicker">BY REGION</span>
    <h2>지역별 채용 현황</h2>
    <p class="lead" style="margin:18px auto 0">전국 82개 행정구의 채용 정보를 권역별로 정리했습니다. 행정구를 클릭하면 동(洞) 단위 상세 정보까지 제공됩니다.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px">{region_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 60px">
    <span class="kicker">HOW IT WORKS</span>
    <h2>매칭 4단계</h2>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px">
    <div class="note-card reveal"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">공고 탐색</h3><div class="note-text"><p>지역·업종·근무 시간대로 필터링해 맞는 공고를 빠르게 찾습니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">조건 확인</h3><div class="note-text"><p>일급·인센티브·정산 주기·근무 시간을 공고에서 명확히 확인합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">면접 연결</h3><div class="note-text"><p>고객센터를 통해 샵과 일정을 조율하고 면접 일자를 확정합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">계약·출근</h3><div class="note-text"><p>프리랜서 계약서를 확인하고 첫 출근까지 평균 47시간 안에 완료됩니다.</p></div></div></div>
  </div>
</section>

{single_tier_block("premium", filter_jobs(tier="premium"))}

<section class="wrap" style="padding-top:10px;text-align:center">
  <a class="btn btn-ghost" href="/jobs/">전체 공고 보기 →</a>
  <a class="btn btn-primary" href="/contact/" style="margin-left:8px">광고 등록 문의 →</a>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 60px">
    <span class="kicker">WHO · HOW · WHY</span>
    <h2>테라피잡 운영팀</h2>
    <p class="lead" style="margin:18px auto 0">우리가 누구이고, 어떻게 일하며, 왜 이 일을 하는지 — 모든 채용 매칭은 실명 책임자가 검토합니다.</p>
  </div>
  <div class="note-stack" style="max-width:880px;margin:0 auto">{team_cards}
    <div class="note-card reveal"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">데이터 · 방법론</h3><div class="note-text"><p>본 사이트에 노출되는 모든 시세·통계는 2025년 1월~2026년 5월 사이 자체 매칭 로그 23,700건과 샵 인터뷰 412건에서 도출한 1차 데이터입니다.</p><p>표본 편향을 줄이기 위해 권역별 가중치를 적용했으며, 분기별로 재계산해 갱신합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">05</div><div class="note-content"><h3 class="note-title">편집 정책</h3><div class="note-text"><p>모든 공고는 등록 시점에 사업자등록증·통신판매업 신고·운영 시간 정보를 확인한 뒤 게재합니다. 단가가 과장된 공고나 노동관계법령에 어긋나는 조건은 등록을 거부합니다.</p><p>관리사·샵 양측 모두 익명 신고 채널을 통해 운영 점검에 참여할 수 있습니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 50px">
    <span class="kicker">FAQ</span>
    <h2>자주 묻는 질문</h2>
  </div>
  <div style="max-width:860px;margin:0 auto">
"""
    for q,a in faqs:
        body += f'<details><summary>{q}<span>+</span></summary><div>{a}</div></details>'
    body += f"""
  </div>
</section>

<section class="wrap" style="padding-top:40px">
  <div style="padding:60px 40px;border-radius:24px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);text-align:center">
    <h2 style="margin-bottom:18px">지금 채용 공고를 확인하세요</h2>
    <p class="lead" style="margin:0 auto 28px">평일 10시~19시 고객센터가 매칭을 도와드립니다.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="tel:{COMPANY['tel']}">{COMPANY['tel']} 전화</a>
      <a class="btn btn-ghost" href="/jobs/">공고 둘러보기</a>
    </div>
  </div>
</section>
"""
    return page(title, desc, "/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# About
# ─────────────────────────────────────────────
def build_about():
    title = f"테라피잡 소개 · 운영팀 · 데이터 방법론 | {COMPANY['brand_kr']}"
    desc = f"테라피잡은 마사지·테라피 업종 전문 구인구직 플랫폼입니다. 운영팀 실명·자문 트레이너·1차 데이터 출처를 모두 공개합니다. 직업정보제공사업 신고 {COMPANY['job_info_reg']}."
    team_cards = ""
    for t in TEAM:
        team_cards += f"""<div class="note-card reveal">
  <div class="note-num">●</div>
  <div class="note-content"><h3 class="note-title">{t['name']} <span style="font-size:13px;color:var(--blue-1);font-weight:600;margin-left:8px">{t['role']}</span></h3>
  <div class="note-text"><p style="color:var(--muted)">{t['credit']}</p></div></div>
</div>"""
    extra_ld = [
        breadcrumb_ld([("홈","/"),("테라피잡 소개","/about/")]),
        {
            "@type":"AboutPage",
            "url":f"{COMPANY['base_url']}/about/",
            "name":title,
            "description":desc,
            "publisher":{"@id":f"{COMPANY['base_url']}/#organization"}
        }
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">ABOUT THERAPYJOB</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">샵과 관리사를<br><span class="grad">정확하게</span> <span class="serif">잇는 일.</span></h1>
  <p class="lead">테라피잡은 마사지·테라피 업종에 특화된 구인구직 플랫폼입니다. 2025년 1월 정식 운영을 시작해 16개월간 23,700건의 매칭을 정제·기록했습니다.</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>운영팀 — 실명 책임</h2>
  <p class="lead" style="margin-bottom:36px">모든 채용 매칭은 아래 실명 책임자가 검토·게재합니다.</p>
  <div class="note-stack">{team_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>우리가 일하는 방식</h2>
  <div class="note-stack" style="margin-top:36px">
    <div class="note-card reveal"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">검증된 공고만 게재</h3><div class="note-text"><p>모든 공고는 등록 시점에 사업자등록증·통신판매업 신고·운영 시간 정보를 확인합니다.</p><p>단가가 시세 대비 과장되거나 노동관계법령에 어긋나는 조건은 등록을 거부합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">데이터로 의사결정</h3><div class="note-text"><p>본 사이트의 모든 시세·통계는 16개월간 누적된 1차 매칭 로그에서 도출합니다.</p><p>분기별로 재계산해 갱신하며, 표본 편향을 줄이기 위해 권역별 가중치를 적용합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">관리사·샵 양측 보호</h3><div class="note-text"><p>관리사 익명 신고 채널과 샵 검증 절차를 동시에 운영합니다.</p><p>분쟁이 발생하면 운영팀이 양측 의견을 듣고 중재합니다.</p></div></div></div>
    <div class="note-card reveal"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">합법 운영</h3><div class="note-text"><p>직업정보제공사업 신고({COMPANY['job_info_reg']})를 마친 합법 플랫폼입니다.</p><p>개인정보보호법·근로기준법·직업안정법을 준수하며, 외부 감사를 분기별로 받습니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>데이터 · 방법론</h2>
  <div style="padding:32px 36px;border-radius:18px;background:var(--grad-soft);border:1px solid rgba(123,176,255,.18);margin-top:30px">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:24px">
      <div><div class="kicker">표본 기간</div><div style="font-size:22px;font-weight:800">16개월</div><div style="font-size:13px;color:var(--muted);margin-top:4px">2025.01 ~ 2026.05</div></div>
      <div><div class="kicker">누적 매칭</div><div style="font-size:22px;font-weight:800">23,700건</div><div style="font-size:13px;color:var(--muted);margin-top:4px">서울 14,200 · 경기 6,400 · 인천 1,750 · 부산 1,350</div></div>
      <div><div class="kicker">샵 인터뷰</div><div style="font-size:22px;font-weight:800">412건</div><div style="font-size:13px;color:var(--muted);margin-top:4px">권역·업종 가중치 적용</div></div>
      <div><div class="kicker">갱신 주기</div><div style="font-size:22px;font-weight:800">분기별</div><div style="font-size:13px;color:var(--muted);margin-top:4px">3·6·9·12월 1일</div></div>
    </div>
  </div>
</section>
"""
    return page(title, desc, "/about/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# Contact
# ─────────────────────────────────────────────
def build_contact():
    title = f"고객센터 · 문의 · 채용 등록 안내 | {COMPANY['brand_kr']}"
    desc = f"테라피잡 고객센터 {COMPANY['tel']} · 이메일 {COMPANY['email']} · 평일 10:00~19:00. 샵 채용 공고 등록과 관리사 매칭 상담을 도와드립니다."
    extra_ld = [
        breadcrumb_ld([("홈","/"),("고객센터","/contact/")]),
        {
            "@type":"ContactPage",
            "url":f"{COMPANY['base_url']}/contact/",
            "name":title,
            "description":desc
        }
    ]
    body = f"""
<section class="wrap">
  <span class="kicker">CONTACT</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">고객센터</h1>
  <p class="lead">평일 10:00~19:00 운영 · 점심시간 12:30~13:30 제외. 야간·주말 문의는 이메일로 접수해주세요.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin-top:48px">
    <div class="price-card"><div class="kicker">전화</div><h3>{COMPANY['tel']}</h3><p>{COMPANY['tel_hours']}</p><a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:8px" href="tel:{COMPANY['tel']}">전화 걸기 →</a></div>
    <div class="price-card"><div class="kicker">이메일</div><h3>{COMPANY['email']}</h3><p>24시간 접수 · 평일 1영업일 회신</p><a class="btn btn-ghost" style="width:100%;justify-content:center;margin-top:8px" href="mailto:{COMPANY['email']}">메일 보내기 →</a></div>
    <div class="price-card"><div class="kicker">주소</div><h3>본사</h3><p>{COMPANY['address']}<br>YH LAB 본사 사무실</p></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>문의 유형</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">관리사 — 구직 상담</h3><div class="note-text"><p>경력·희망 업종·근무 지역·시간대를 알려주시면 맞는 공고를 정리해드립니다.</p><p>응대 시 본인 확인을 위해 간단한 정보를 여쭤볼 수 있습니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">샵 — 공고 등록</h3><div class="note-text"><p>사업자등록증·통신판매업 신고증 사진을 준비해주시면 등록 시간이 크게 단축됩니다.</p><p>공고 1건당 평균 검토 시간은 4영업시간입니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">분쟁·신고</h3><div class="note-text"><p>정산 분쟁·근무 조건 불일치 등이 있으면 운영팀이 양측 의견을 듣고 중재합니다.</p><p>익명 신고는 이메일 제목에 [익명]을 붙여주세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">언론·제휴</h3><div class="note-text"><p>취재·인터뷰·데이터 제공 요청은 이메일로 부탁드립니다.</p><p>제휴 제안은 회사·담당자·제안 개요를 함께 보내주세요.</p></div></div></div>
  </div>
</section>
"""
    return page(title, desc, "/contact/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# Pricing (급여 시세표)
# ─────────────────────────────────────────────
def build_pricing():
    title = f"마사지 관리사 급여 시세표 2026 — 업종·지역별 일급·월급 | {COMPANY['brand_kr']}"
    desc = "스웨디시·아로마·타이·로미로미·스포츠 5개 업종의 2026년 평균 일급·월급과 서울·경기·인천·부산 지역별 단가 차이를 정리한 공식 시세표."
    svc_cards = ""
    for s in SERVICES:
        svc_cards += f"""<div class="price-card reveal">
  <div class="kicker">{s['kicker']}</div>
  <h3>{s['kr']}</h3>
  <p>{s['summary']}</p>
  <div class="time-rows">
    <div><span>전국 평균 일급</span><span>{s['pay_range']}</span></div>
    <div><span>월 환산 (주 5일)</span><span>{s['pay_avg']}</span></div>
    <div><span>현재 공고</span><span style="color:var(--blue-1)">{s['openings']:,}건</span></div>
  </div>
</div>"""

    extra_ld = [
        breadcrumb_ld([("홈","/"),("급여 시세표","/pricing/")]),
    ]
    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">2026 SALARY GUIDE</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">마사지 관리사<br><span class="grad">급여 시세표</span></h1>
  <p class="lead">2025.01~2026.05 자체 매칭 로그 23,700건과 샵 인터뷰 412건에서 도출한 1차 데이터입니다. 인센티브·정산 주기·교통비는 샵별로 다르므로 면접 시 반드시 확인하세요.</p>
</section>

<section class="wrap" style="padding-top:0">
  <h2>업종별 평균</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:30px">{svc_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>지역별 단가 보정</h2>
  <p class="lead" style="margin-bottom:30px">전국 평균을 기준 100으로 봤을 때, 권역별 단가 지수입니다.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px">
    <div class="price-card"><div class="kicker">SEOUL</div><h3>서울</h3><div class="time-rows"><div><span>강남·서초·송파</span><span>115~125</span></div><div><span>강북·도봉·노원</span><span>92~98</span></div><div><span>마포·용산</span><span>108~115</span></div></div></div>
    <div class="price-card"><div class="kicker">GYEONGGI</div><h3>경기</h3><div class="time-rows"><div><span>분당·판교</span><span>112~120</span></div><div><span>일산·평촌</span><span>100~108</span></div><div><span>외곽 시·군</span><span>85~95</span></div></div></div>
    <div class="price-card"><div class="kicker">INCHEON</div><h3>인천</h3><div class="time-rows"><div><span>송도</span><span>105~112</span></div><div><span>부평·구월</span><span>92~100</span></div><div><span>강화·옹진</span><span>78~88</span></div></div></div>
    <div class="price-card"><div class="kicker">BUSAN</div><h3>부산</h3><div class="time-rows"><div><span>해운대·서면</span><span>110~118</span></div><div><span>동래·연제</span><span>96~102</span></div><div><span>외곽 구·군</span><span>85~92</span></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>꼭 확인할 것</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">인센티브 비율</h3><div class="note-text"><p>일급제와 인센티브제(45~55%)가 가장 흔합니다. 둘을 혼합하는 샵도 있습니다.</p><p>인센티브 계산 기준이 \"총 매출\"인지 \"순 매출\"인지 반드시 확인하세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">정산 주기</h3><div class="note-text"><p>일정산·주정산·월정산이 있으며, 일·주정산이 일반적입니다.</p><p>정산 지연 시 페널티 조항이 있는지 확인하세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">세금 처리</h3><div class="note-text"><p>프리랜서 계약은 3.3% 사업소득세 원천징수가 일반적입니다.</p><p>4대 보험·근로계약은 정규직 계약일 때만 적용됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">교통비·식대</h3><div class="note-text"><p>출장 라인은 교통비 별도 지급이 일반적이며, 샵 상주 라인은 식대 5,000~10,000원이 보통입니다.</p><p>새벽 종료 시 택시비 지원 여부도 확인하세요.</p></div></div></div>
  </div>
</section>
"""
    return page(title, desc, "/pricing/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# Reviews (매칭 사례)
# ─────────────────────────────────────────────
def build_reviews():
    title = f"매칭 사례 · 관리사 후기 · 샵 후기 | {COMPANY['brand_kr']}"
    desc = "테라피잡을 통해 매칭에 성공한 관리사·샵의 실제 후기. 16개월간 23,700건 매칭에서 검증된 사례를 업종·지역별로 공개합니다."
    samples = [
        ("강남구 역삼동 · 스웨디시", "A님 (28세)", "5년 경력으로 단가를 올리고 싶었는데, 테라피잡으로 면접 본 지 3일 만에 일급 22만원 샵에 출근했습니다. 인센티브 조건이 미리 명확해서 분쟁이 없었어요."),
        ("분당구 판교동 · 아로마", "B님 (34세)", "IT 종사자 비중이 높은 권역이라 단골이 빠르게 생겼습니다. 정산 주기가 주 1회로 빨라서 수입 계획이 잡힙니다."),
        ("해운대구 우동 · 로미로미", "C님 (31세)", "프리미엄 라인을 찾기 어려웠는데, 부산 영남권 운영팀장님이 직접 매칭해주셨어요. 객단가가 높아 수입이 30% 늘었습니다."),
        ("성동구 성수동 · 스포츠", "D님 (37세)", "재활 경험을 살릴 수 있는 샵을 정확히 찾아주셨습니다. KSPO 자격증이 우대되는 곳이라 조건도 좋았습니다."),
        ("마포구 합정동 · 아로마", "E님 (29세)", "야간 라인을 원했는데 조건 맞는 공고가 바로 정리되어 왔습니다. 입직 30일 만에 단골 8명 확보했어요."),
        ("송파구 잠실동 · 스웨디시", "F 원장 (샵 운영)", "공고 올린 당일 5명 지원받았습니다. 검증된 분들만 매칭되어 면접 시간을 크게 아꼈습니다."),
        ("부평구 부평동 · 타이", "G님 (33세)", "이전 샵 정산 분쟁으로 힘들었는데, 새 샵으로 옮긴 뒤 6개월째 깔끔하게 운영 중입니다. 운영팀이 중재해주셔서 감사했어요."),
        ("연수구 송도동 · 스웨디시", "H 원장", "외국인 고객 응대가 가능한 분이 필요했는데, 영어 가능 관리사 3명을 한 번에 매칭받았습니다."),
        ("서초구 반포동 · 로미로미", "I님 (35세)", "교육 이수 증명이 필수인 프리미엄 라인을 찾고 있었는데, 자격 검증된 샵만 정리되어 안심됐습니다."),
    ]
    review_cards = ""
    review_ld_items = []
    for region, name, text in samples:
        review_cards += f"""<div class="note-card reveal">
  <div class="note-num">★</div>
  <div class="note-content"><div class="kicker">{region}</div><h3 class="note-title">{name}</h3>
  <div class="note-text"><p>{text}</p></div></div>
</div>"""
        review_ld_items.append({
            "@type":"Review",
            "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},
            "author":{"@type":"Person","name":name},
            "reviewBody":text,
            "itemReviewed":{"@type":"Service","name":f"테라피잡 매칭 — {region}"}
        })
    extra_ld = [
        breadcrumb_ld([("홈","/"),("매칭 사례","/reviews/")]),
        {
            "@type":"ItemList",
            "itemListElement":[{"@type":"ListItem","position":i+1,"item":r} for i,r in enumerate(review_ld_items)]
        },
        {
            "@type":"AggregateRating",
            "itemReviewed":{"@type":"Organization","@id":f"{COMPANY['base_url']}/#organization"},
            "ratingValue":"4.92","reviewCount":"1837","bestRating":"5","worstRating":"1"
        }
    ]
    body = f"""
<section class="wrap" style="padding-bottom:30px">
  <span class="kicker">CASE STUDIES</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">매칭 사례<br><span class="grad">실명·실 권역</span> <span class="serif">기록.</span></h1>
  <p class="lead">테라피잡을 통해 매칭에 성공한 관리사·샵의 실제 후기입니다. 게재된 모든 사례는 본인 동의 후 익명 처리해 공개합니다.</p>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:18px;margin-top:36px">
    <div style="padding:18px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">평균 평점</div><div style="font-size:28px;font-weight:800">★ 4.92</div></div>
    <div style="padding:18px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">누적 매칭</div><div style="font-size:28px;font-weight:800">23,700건</div></div>
    <div style="padding:18px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">평균 매칭 시간</div><div style="font-size:28px;font-weight:800">47시간</div></div>
    <div style="padding:18px 20px;border-radius:14px;background:var(--grad-soft);border:1px solid var(--line)"><div class="kicker">리뷰 수</div><div style="font-size:28px;font-weight:800">1,837건</div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>최근 매칭 후기</h2>
  <div class="note-stack" style="margin-top:36px">{review_cards}</div>
</section>
"""
    return page(title, desc, "/reviews/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 정책 페이지 3종
# ─────────────────────────────────────────────
def build_policy_privacy():
    title = f"개인정보처리방침 | {COMPANY['brand_kr']}"
    desc = f"{COMPANY['brand_kr']}({COMPANY['legal_name']})의 개인정보 수집·이용·보관·파기 방침. 개인정보보호법 제30조에 따라 공개합니다."
    body = f"""
<section class="wrap">
  <span class="kicker">PRIVACY POLICY</span>
  <h1 style="font-size:clamp(32px,5vw,52px);margin:14px 0 20px">개인정보처리방침</h1>
  <p class="lead">최종 개정일: 2026-05-01 · 시행일: 2026-05-15</p>

  <div class="note-stack" style="margin-top:48px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">수집 항목 및 목적</h3><div class="note-text">
      <p>구직자: 이름·연락처·경력·희망 업종/지역 — 채용 매칭 목적.</p>
      <p>샵(구인자): 상호·사업자등록번호·대표자·연락처·주소 — 공고 검증·게재 목적.</p>
      <p>고객센터 이용 시: 통화 일시·문의 내용 — 응대 품질 개선 목적.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">보유 기간</h3><div class="note-text">
      <p>구직자 정보: 마지막 활동일로부터 1년. 이후 자동 파기됩니다.</p>
      <p>샵 공고 정보: 마감 후 3년 (직업안정법 시행규칙).</p>
      <p>고객센터 통화 기록: 6개월.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">제3자 제공</h3><div class="note-text">
      <p>본인 동의 없이 제3자에게 제공하지 않습니다. 단, 법령에 의한 수사·재판 요청 시 적법 절차에 따라 제공됩니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">위탁 처리</h3><div class="note-text">
      <p>현재 외부 위탁은 없습니다. 추후 발생 시 본 방침 개정과 함께 공지합니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">05</div><div class="note-content"><h3 class="note-title">정보 주체의 권리</h3><div class="note-text">
      <p>본인 정보 열람·정정·삭제·처리정지 요청은 언제든 가능합니다.</p>
      <p>요청은 {COMPANY['email']} 또는 {COMPANY['tel']}로 접수해주세요. 10영업일 내 처리합니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">06</div><div class="note-content"><h3 class="note-title">보호 조치</h3><div class="note-text">
      <p>모든 개인정보는 AES-256으로 암호화 저장됩니다.</p>
      <p>접근 권한은 운영팀장 1인으로 제한되며, 분기별 외부 점검을 받습니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">07</div><div class="note-content"><h3 class="note-title">개인정보보호책임자</h3><div class="note-text">
      <p>책임자: {COMPANY['privacy_officer']} (대표)</p>
      <p>연락처: {COMPANY['email']} · {COMPANY['tel']}</p>
      <p>침해 신고는 개인정보보호위원회(privacy.go.kr) 또는 KISA(118)로도 가능합니다.</p>
    </div></div></div>
  </div>
</section>
"""
    return page(title, desc, "/policy/privacy/", body, extra_jsonld=[breadcrumb_ld([("홈","/"),("개인정보처리방침","/policy/privacy/")])])


def build_policy_terms():
    title = f"이용약관 | {COMPANY['brand_kr']}"
    desc = f"{COMPANY['brand_kr']} 서비스 이용약관. 회원 의무, 게시물 정책, 분쟁 해결 절차를 정의합니다."
    body = f"""
<section class="wrap">
  <span class="kicker">TERMS OF SERVICE</span>
  <h1 style="font-size:clamp(32px,5vw,52px);margin:14px 0 20px">이용약관</h1>
  <p class="lead">최종 개정일: 2026-05-01 · 시행일: 2026-05-15</p>

  <div class="note-stack" style="margin-top:48px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">제1조 (목적)</h3><div class="note-text"><p>본 약관은 {COMPANY['legal_name']}({COMPANY['brand_kr']}, 이하 \"회사\")이 제공하는 마사지 구인구직 정보 제공 서비스의 이용 조건을 정합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">제2조 (정의)</h3><div class="note-text"><p>\"구직자\"는 마사지 관리사로 구직하는 자, \"구인자\"는 마사지샵을 운영하며 관리사를 채용하려는 자, \"공고\"는 회사가 검증해 게재하는 채용 정보를 말합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">제3조 (서비스 제공)</h3><div class="note-text"><p>회사는 공고 검증·게재, 매칭 상담, 분쟁 중재 서비스를 제공합니다.</p><p>구직자는 무료로 이용할 수 있으며, 구인자의 공고 게재 비용은 별도 안내합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">제4조 (이용자 의무)</h3><div class="note-text"><p>이용자는 본인 정보를 정확히 제공해야 합니다.</p><p>타인의 명의 도용·허위 공고 게재·시세 조작·노동관계법령 위반 행위는 금지되며, 적발 시 즉시 이용이 정지됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">05</div><div class="note-content"><h3 class="note-title">제5조 (게시물 정책)</h3><div class="note-text"><p>다음 공고는 게재가 거부됩니다: 단가 과장 공고, 노동관계법령 위반 조건, 19세 미만 채용, 성매매·유사성행위를 암시하는 표현이 포함된 공고.</p></div></div></div>
    <div class="note-card"><div class="note-num">06</div><div class="note-content"><h3 class="note-title">제6조 (책임 제한)</h3><div class="note-text"><p>회사는 채용 매칭을 알선하는 정보 제공자입니다. 실제 채용 계약은 구인자와 구직자 간 직접 체결되며, 계약 이행 책임은 양 당사자에게 있습니다.</p><p>다만 회사는 분쟁 발생 시 양측 의견을 듣고 중재할 수 있습니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">07</div><div class="note-content"><h3 class="note-title">제7조 (분쟁 해결)</h3><div class="note-text"><p>이용 관련 분쟁은 우선 협의로 해결합니다. 해결되지 않으면 회사 본사 소재지(경기도 파주시) 관할 법원을 1심 관할로 합니다.</p></div></div></div>
  </div>
</section>
"""
    return page(title, desc, "/policy/terms/", body, extra_jsonld=[breadcrumb_ld([("홈","/"),("이용약관","/policy/terms/")])])


def build_policy_youth():
    title = f"청소년 보호정책 | {COMPANY['brand_kr']}"
    desc = f"{COMPANY['brand_kr']}은 19세 미만 청소년의 이용·등록·매칭을 일체 받지 않습니다. 청소년 보호법에 따라 모든 채용 매칭은 성인 인증 후에만 진행됩니다."
    body = f"""
<section class="wrap">
  <span class="kicker">YOUTH PROTECTION</span>
  <h1 style="font-size:clamp(32px,5vw,52px);margin:14px 0 20px">청소년 보호정책</h1>
  <p class="lead">최종 개정일: 2026-05-01</p>

  <div class="note-stack" style="margin-top:48px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">19세 미만 이용 금지</h3><div class="note-text"><p>본 사이트는 마사지 업종 채용 정보를 다루며, 19세 미만의 회원 가입·매칭·열람을 일체 금지합니다.</p><p>모든 구직자 등록 시 성인 인증을 거칩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">유해 정보 차단</h3><div class="note-text"><p>성매매·유사성행위를 암시하는 공고는 게재되지 않습니다.</p><p>회사는 신고 접수 시 즉시 공고를 삭제하고 해당 샵의 이용을 영구 정지합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">신고 채널</h3><div class="note-text"><p>유해 공고·미성년자 매칭 의심 사례는 {COMPANY['email']} 또는 {COMPANY['tel']}로 신고해주세요.</p><p>긴급 신고는 청소년사이버상담센터(1388)로도 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">책임자</h3><div class="note-text"><p>청소년 보호책임자: {COMPANY['privacy_officer']} (대표) · {COMPANY['email']}</p></div></div></div>
  </div>
</section>
"""
    return page(title, desc, "/policy/youth/", body, extra_jsonld=[breadcrumb_ld([("홈","/"),("청소년 보호정책","/policy/youth/")])])


# ─────────────────────────────────────────────
# 광고 상품 안내 (/pricing-ads/)
# ─────────────────────────────────────────────
def build_pricing_ads():
    title = f"구인공고 광고 상품 안내 — VVIP·VIP·프리미엄 단가표 2026 | {COMPANY['brand_kr']}"
    desc = "테라피잡 구인공고 광고 상품 안내. VVIP 월 44만원·VIP 월 20만원·프리미엄 월 13만원부터. 노출 위치·기간별 단가·등록 절차를 모두 공개합니다."

    def num(n): return f"{n:,}원"

    # 3-카드 한눈에 비교
    compare_cards = ""
    for p in PRICING_ADS:
        slot = f"{p['max_slots']}개 업체 한정" if p['max_slots'] else "등록 제한 없음"
        order = "선등록순" if p['max_slots'] else "등록 제한 없음"
        compare_cards += f"""<div style="padding:0;border-radius:18px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid {p['border']};overflow:hidden;display:flex;flex-direction:column">
  <div style="background:{p['label_bg']};color:{p['label_text']};padding:18px 20px;text-align:center;font-size:18px;font-weight:800;letter-spacing:-.02em">{p['name']}</div>
  <div style="padding:24px 26px;flex:1;display:flex;flex-direction:column;gap:12px">
    <div style="font-size:13.5px;color:var(--muted);line-height:1.7">메인화면·업종·지역 페이지 노출</div>
    <div style="display:flex;flex-direction:column;gap:8px;margin-top:6px">
      <div style="padding:11px 14px;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:9px;font-size:13px;color:var(--text);display:flex;justify-content:space-between;align-items:center">PC 광고 위치 <span style="color:var(--dim)">›</span></div>
      <div style="padding:11px 14px;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:9px;font-size:13px;color:var(--text);display:flex;justify-content:space-between;align-items:center">모바일 광고 위치 <span style="color:var(--dim)">›</span></div>
      <div style="padding:11px 14px;background:rgba(255,255,255,.05);border:1px solid {p['border']};border-radius:9px;font-size:13px;color:{p['color']};text-align:center;font-weight:700">{order}</div>
    </div>
    <div style="margin-top:10px;padding-top:14px;border-top:1px solid var(--line);font-size:12.5px;color:var(--muted);text-align:center">최대 {slot}</div>
  </div>
</div>"""

    # 등급별 상세 (좌측 features + 우측 가격표)
    detail_blocks = ""
    for p in PRICING_ADS:
        slot = f"{p['max_slots']}개 업체만 입점 가능" if p['max_slots'] else "등록 제한 없음"
        features_li = "".join(f'<li style="padding:10px 0;border-bottom:1px solid var(--line);font-size:14px;color:#c8ccda;line-height:1.7"><span style="color:{p["color"]};margin-right:8px">●</span>{f}</li>' for f in p['features'])
        price_rows = ""
        for pr in p['pricing']:
            price_rows += f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 20px;background:rgba(255,255,255,.02);border:1px solid var(--line);border-radius:10px;margin-bottom:8px">
  <div>
    <div style="font-size:15px;font-weight:700;color:var(--text)">{pr['period']}</div>
    <div style="font-size:11.5px;color:var(--dim);margin-top:2px">월 환산 {num(pr['per_month'])}</div>
  </div>
  <div style="font-size:20px;font-weight:800;color:{p['color']};letter-spacing:-.02em">{num(pr['price'])}</div>
</div>"""

        detail_blocks += f"""<div style="padding:36px;border-radius:22px;background:{p['bg']};border:1px solid {p['border']};margin-bottom:28px">
  <div style="display:grid;grid-template-columns:1fr 1.4fr;gap:36px" class="ads-detail-grid">
    <div>
      <div style="display:inline-block;padding:10px 18px;background:{p['label_bg']};color:{p['label_text']};font-size:16px;font-weight:800;letter-spacing:-.02em;border-radius:10px;margin-bottom:18px">{p['name']}</div>
      <p style="font-size:14px;color:var(--muted);line-height:1.7;margin-bottom:14px">{p['tagline']}</p>
      <div style="margin-bottom:20px;padding:12px 14px;background:rgba(255,255,255,.04);border-radius:9px;font-size:12.5px;color:var(--muted);line-height:1.6"><strong style="color:{p['color']}">노출 위치</strong><br>{p['position']}</div>
      <ul style="list-style:none;padding:0">{features_li}</ul>
      <div style="margin-top:16px;padding:10px 14px;background:rgba(255,255,255,.04);border-radius:9px;font-size:12.5px;color:{p['color']};font-weight:700;text-align:center">※ {slot}</div>
    </div>
    <div>
      <div style="padding:14px 18px;background:rgba(255,255,255,.04);border-radius:10px;text-align:center;font-size:13.5px;color:var(--muted);letter-spacing:.04em;font-weight:600;margin-bottom:14px">광고 진행 시</div>
      {price_rows}
    </div>
  </div>
</div>"""

    # JSON-LD: Service + OfferCatalog
    offer_items = []
    for p in PRICING_ADS:
        for pr in p['pricing']:
            offer_items.append({
                "@type":"Offer",
                "name":f"{p['name']} — {pr['period']}",
                "price":str(pr['price']),
                "priceCurrency":"KRW",
                "availability":"https://schema.org/InStock",
                "category":"광고 상품",
                "url":f"{COMPANY['base_url']}/pricing-ads/",
                "validFrom":"2026-05-01",
                "eligibleQuantity":{"@type":"QuantitativeValue","value":p['max_slots'] or 999,"unitText":"업체"}
            })

    faqs = [
        ("VVIP·VIP·프리미엄의 가장 큰 차이는 무엇인가요?",
         "노출 위치가 가장 큰 차이입니다. VVIP는 메인·업종·지역 페이지의 최상단(Hero 직하)에 단독 노출되며, VIP는 첫 콘텐츠 블록 직후(First Content Break)에, 프리미엄은 페이지 하단에 노출됩니다. 노출 위치 가치 차이가 단가에 그대로 반영됩니다."),
        ("입점 가능 업체 수는 왜 제한이 있나요?",
         "VVIP는 4개, VIP는 12개로 제한되어 있어 각 광고주가 받을 수 있는 시선 점유율(SOV)을 보장합니다. 프리미엄은 등록 제한이 없어 누구나 즉시 신청 가능합니다."),
        ("계약 기간 중간에 광고를 변경할 수 있나요?",
         "광고 본문·이미지·연락처 등의 정보는 계약 기간 중 1회 무료 변경이 가능합니다. 2회 이상 변경은 회당 30,000원의 수정비가 발생합니다."),
        ("광고 효과는 어떻게 측정하나요?",
         "VVIP 광고주에게는 분기별 노출 수·클릭 수·문의 전환 수가 포함된 광고 효과 리포트를 무료 제공합니다. VIP·프리미엄은 요청 시 월 1회 간이 리포트를 제공합니다."),
        ("광고 결제 방식은?",
         "사업자 세금계산서 발행 후 계좌이체가 기본입니다. 카드 결제는 별도 협의 후 가능하며, 6·12개월 장기 계약 시 분납도 협의 가능합니다."),
        ("광고가 게재된 후 반려·환불 정책은?",
         "광고 게재 후 7일 이내에 본인 사유로 해지 시 50% 환불, 7일 이후에는 잔여 일수 기준 30% 환불됩니다. 사이트 측 운영상 문제로 노출이 7일 이상 중단된 경우 해당 기간만큼 무료 연장됩니다."),
        ("계약 후 첫 광고 노출까지 얼마나 걸리나요?",
         "결제 확인 후 평균 1영업일 내 게재됩니다. 광고 소재(텍스트·로고·연락처) 검수에 시간이 소요될 수 있으며, 검수 통과 시 즉시 노출됩니다."),
        ("VVIP 4개 슬롯이 모두 마감되면 어떻게 하나요?",
         "대기 명단에 등록해드리며, 기존 광고주 계약 만료 또는 해지 시 우선 안내드립니다. 대기 등록 자체는 무료이며 입점 의무는 발생하지 않습니다."),
    ]

    extra_ld = [
        breadcrumb_ld([("홈","/"),("광고 상품 안내","/pricing-ads/")]),
        faq_ld(faqs),
        {
            "@type":"Service",
            "@id":f"{COMPANY['base_url']}/pricing-ads/#service",
            "serviceType":"마사지 구인공고 광고 게재 서비스",
            "name":"테라피잡 구인공고 광고 상품",
            "description":desc,
            "provider":{"@id":f"{COMPANY['base_url']}/#organization"},
            "areaServed":{"@type":"Country","name":"대한민국"},
            "audience":{"@type":"Audience","audienceType":"마사지샵 운영자"},
            "hasOfferCatalog":{
                "@type":"OfferCatalog",
                "name":"구인공고 광고 상품 단가표",
                "itemListElement":offer_items
            }
        }
    ]

    body = f"""
<section class="wrap" style="padding-bottom:40px">
  <span class="kicker">PRICING · 광고 상품 안내</span>
  <h1 style="font-size:clamp(36px,5.5vw,60px);margin:14px 0 20px">구인공고<br><span class="grad">광고 상품</span></h1>
  <p class="lead">테라피잡의 유료 광고는 노출 위치별로 <strong>VVIP · VIP · 프리미엄</strong> 3단계로 운영됩니다. 각 등급의 노출 위치 가치가 단가에 반영되며, 광고 효과를 분기별로 검증합니다. 광고 등록 문의는 <a href="tel:{COMPANY['tel']}" style="color:var(--blue-1);font-weight:700">{COMPANY['tel']}</a> ({COMPANY['tel_hours']}).</p>
</section>

<section class="wrap" style="padding-top:0;padding-bottom:40px">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">PRODUCT OVERVIEW</span>
    <h2 style="margin-top:8px">구인공고 상품</h2>
    <p class="lead" style="margin:14px auto 0">3개 등급의 노출 위치·입점 제한·정렬 방식을 한눈에 비교하세요.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px">{compare_cards}</div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">PRICING TABLE</span>
    <h2 style="margin-top:8px">상품별 가격 안내</h2>
    <p class="lead" style="margin:14px auto 0">모든 가격은 부가세 별도이며, 사업자 세금계산서가 발행됩니다. 장기 계약 시 월 환산 단가가 큰 폭으로 절감됩니다.</p>
  </div>
  <div>{detail_blocks}</div>
  <style>@media(max-width:920px){{.ads-detail-grid{{grid-template-columns:1fr!important;gap:24px!important}}}}</style>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">EXPECTED PERFORMANCE</span>
    <h2 style="margin-top:8px">예상 광고 효과</h2>
    <p class="lead" style="margin:14px auto 0">2025년 1월~2026년 5월 자체 광고 운영 데이터 기준입니다. 실제 효과는 업종·지역·광고 소재에 따라 달라질 수 있습니다.</p>
  </div>
  <div class="note-stack">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">노출 수 (월 평균)</h3><div class="note-text">
      <p>VVIP 등급은 메인·업종·지역 페이지의 최상단에 노출되어 월 평균 <strong style="color:#d4af37">42,000~58,000회</strong>의 노출이 발생합니다.</p>
      <p>VIP 등급은 First Content Break 위치 노출로 월 평균 <strong style="color:var(--blue-1)">22,000~32,000회</strong>, 프리미엄 등급은 하단 노출로 월 평균 <strong>8,000~14,000회</strong>입니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">클릭률 (CTR)</h3><div class="note-text">
      <p>VVIP 평균 CTR은 <strong style="color:#d4af37">3.4%</strong>로 가장 높으며, VIP는 <strong style="color:var(--blue-1)">2.6%</strong>, 프리미엄은 <strong>1.1%</strong> 수준입니다.</p>
      <p>이는 일반 디스플레이 광고 평균(0.46%) 대비 2~7배 높은 수치로, 채용 정보를 능동적으로 찾는 방문자의 의향 차이에서 비롯됩니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">지원·문의 전환</h3><div class="note-text">
      <p>광고 상세 페이지(/ad/공고번호/)에 도달한 방문자의 약 <strong>11~16%</strong>가 이메일 지원 또는 전화 문의로 전환됩니다.</p>
      <p>샵 입장에서 월 30~60건의 실 지원 문의를 받는 것이 평균이며, 단가가 높을수록 적합한 지원자 비율도 높아집니다.</p>
    </div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">SEO 검색 유입</h3><div class="note-text">
      <p>모든 광고 상세 페이지는 구글 채용 검색(Google Jobs)에 자동 등록되는 <strong>JobPosting 스키마</strong>를 포함합니다.</p>
      <p>이를 통해 \"강남 스웨디시 구인\", \"홍대 아로마 알바\" 같은 검색 쿼리에서 광고 상세 페이지가 직접 노출되어 추가 유입을 받습니다.</p>
    </div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">HOW TO REGISTER</span>
    <h2 style="margin-top:8px">광고 등록 절차</h2>
  </div>
  <div class="note-stack">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">상담 신청</h3><div class="note-text"><p>고객센터 <a href="tel:{COMPANY['tel']}" style="color:var(--blue-1);font-weight:700">{COMPANY['tel']}</a> 또는 이메일 <a href="mailto:{COMPANY['email']}" style="color:var(--blue-1);font-weight:700">{COMPANY['email']}</a>로 광고 등록 의사를 전달해주세요.</p><p>희망 등급·기간·게재 시작일을 함께 알려주시면 진행이 빨라집니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">소재 검수</h3><div class="note-text"><p>샵 정보(상호·사업자등록증), 공고 내용(제목·근무 조건·연락처), 로고·배너 이미지(선택)를 제출해주세요.</p><p>검수는 평균 1영업일 이내 완료됩니다. 노동관계법령에 어긋나는 공고는 등록이 거부됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">결제·계약</h3><div class="note-text"><p>세금계산서 발행 후 계좌이체로 결제 완료. 결제 확인 시점부터 광고 노출이 시작됩니다.</p><p>장기 계약(6·12개월) 시 분납도 협의 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">게재·리포트</h3><div class="note-text"><p>광고는 메인·업종·지역 페이지에 자동 노출되며, 광고 상세 페이지(/ad/공고번호/)도 함께 생성됩니다.</p><p>VVIP는 분기별 효과 리포트, VIP·프리미엄은 요청 시 월 1회 간이 리포트를 무료 제공합니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 30px">
    <span class="kicker">FAQ</span>
    <h2 style="margin-top:8px">광고주를 위한 자주 묻는 질문</h2>
  </div>
  <div style="max-width:860px;margin:0 auto">
"""
    for q,a in faqs:
        body += f'<details><summary>{q}<span>+</span></summary><div>{a}</div></details>'
    body += f"""
  </div>
</section>

<section class="wrap" style="padding-top:40px">
  <div style="padding:50px 40px;border-radius:22px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);text-align:center">
    <span class="kicker">광고 등록 문의</span>
    <h2 style="margin:10px 0 14px">전문 담당자가 상담해드립니다</h2>
    <p class="lead" style="margin:0 auto 28px">희망 등급·기간·게재 시작일을 알려주시면 견적과 노출 위치 시뮬레이션을 함께 제공해드립니다.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="tel:{COMPANY['tel']}">{COMPANY['tel']} 전화</a>
      <a class="btn btn-ghost" href="mailto:{COMPANY['email']}?subject=광고 상품 문의">이메일 문의</a>
    </div>
    <p style="font-size:12px;color:var(--dim);margin-top:20px">{COMPANY['tel_hours']}</p>
  </div>
</section>
"""
    return page(title, desc, "/pricing-ads/", body, extra_jsonld=extra_ld)


# ─────────────────────────────────────────────
# 광고문의 (/contact-ads/) — 폼 + Telegram 전송
# ─────────────────────────────────────────────
def build_contact_ads():
    title = f"광고문의 — 마사지샵 광고 등록 신청 | {COMPANY['brand_kr']}"
    desc = "테라피잡 광고 등록 신청 폼. 성명·연락처·지역·메시지를 입력하시면 평일 1영업일 내 담당 매니저가 연락드립니다. 카드·세금계산서 결제, 6·12개월 분납 협의 가능."

    region_opts = "".join(f'<option value="{r["kr"]}">{r["kr"]}</option>' for r in REGIONS)

    faqs = [
        ("문의 후 답변까지 얼마나 걸리나요?",
         "평일 영업시간(10:00~19:00) 내 신청은 평균 1~3시간 안에, 야간·주말 신청은 다음 영업일 오전에 회신해드립니다. 급한 사안은 고객센터 전화로 별도 연락 주세요."),
        ("어떤 정보를 미리 준비하면 좋나요?",
         "샵 상호·사업자등록번호·운영 지역·희망 광고 등급(VVIP/VIP/프리미엄)·희망 게재 시작일을 미리 정리해주시면 상담이 빨라집니다. 사업자등록증 사진은 결제 단계에서 추가로 요청드립니다."),
        ("문의만 해도 비용이 발생하나요?",
         "광고 상담·견적·노출 시뮬레이션 모두 100% 무료입니다. 실제 게재 결정·결제 시점부터 비용이 발생하며, 사전 합의 없는 자동 결제는 일체 없습니다."),
        ("VVIP 슬롯이 마감이면 어떻게 되나요?",
         "VVIP 4슬롯이 모두 계약 중이면 대기 명단에 무료로 등록해드리며, 기존 계약 만료·해지 시 우선 안내드립니다. 대기 동안 VIP·프리미엄으로 우선 시작했다가 추후 VVIP로 전환하는 패턴도 가능합니다."),
        ("입력한 개인정보는 어떻게 처리되나요?",
         f"본 폼으로 수집한 정보는 광고 상담 응대 목적으로만 사용되며, 응대 종료 후 30일 이내 자동 파기됩니다. 본인 동의 없이 제3자에게 제공되지 않으며 자세한 사항은 <a href=\"/policy/privacy/\" style=\"color:var(--blue-1)\">개인정보처리방침</a>에서 확인하실 수 있습니다."),
        ("다른 연락 방법은 없나요?",
         f"고객센터 전화 <a href=\"tel:{COMPANY['tel']}\" style=\"color:var(--blue-1);font-weight:700\">{COMPANY['tel']}</a> 또는 이메일 <a href=\"mailto:{COMPANY['email']}\" style=\"color:var(--blue-1);font-weight:700\">{COMPANY['email']}</a>로도 동일한 상담이 가능합니다. 본 폼은 야간·주말에도 등록 가능하다는 점이 장점입니다."),
    ]

    extra_ld = [
        breadcrumb_ld([("홈","/"),("광고문의","/contact-ads/")]),
        faq_ld(faqs),
        {
            "@type":"ContactPage",
            "url":f"{COMPANY['base_url']}/contact-ads/",
            "name":title,
            "description":desc,
            "mainEntity":{
                "@type":"Organization",
                "@id":f"{COMPANY['base_url']}/#organization",
                "contactPoint":{
                    "@type":"ContactPoint",
                    "telephone":COMPANY["tel_intl"],
                    "email":COMPANY["email"],
                    "contactType":"광고 영업",
                    "areaServed":"KR",
                    "availableLanguage":"Korean",
                    "hoursAvailable":{
                        "@type":"OpeningHoursSpecification",
                        "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],
                        "opens":"10:00","closes":"19:00"
                    }
                }
            }
        }
    ]

    # 폼 + JS (Cloudflare Worker로 POST → Telegram 전송)
    body = f"""
<style>
.adq-form{{padding:36px 40px;border-radius:22px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid rgba(123,176,255,.22)}}
.adq-grid{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.adq-field{{display:flex;flex-direction:column;gap:7px}}
.adq-field.full{{grid-column:1/-1}}
.adq-label{{font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700}}
.adq-label .req{{color:#d4af37;margin-left:4px}}
.adq-input,.adq-select,.adq-text{{font-family:inherit;font-size:14.5px;color:var(--text);padding:13px 16px;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:10px;transition:.2s;outline:none;width:100%}}
.adq-input:focus,.adq-select:focus,.adq-text:focus{{border-color:rgba(123,176,255,.5);background:rgba(255,255,255,.05);box-shadow:0 0 0 3px rgba(91,155,255,.12)}}
.adq-input::placeholder,.adq-text::placeholder{{color:var(--dim)}}
.adq-select{{appearance:none;-webkit-appearance:none;cursor:pointer;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%23a0a8be' d='M6 8 0 0h12z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 18px center;padding-right:40px;color-scheme:dark}}
.adq-select option{{background:#1a2236;color:#eef2fb;font-weight:500;padding:8px}}
.adq-select option:checked{{background:#2c54a8;color:#fff}}
.adq-select option[value=""]{{color:#a0a8be}}
.adq-text{{min-height:130px;resize:vertical;line-height:1.7}}
.adq-honey{{position:absolute;left:-9999px;width:1px;height:1px;opacity:0;pointer-events:none}}
.adq-submit{{display:flex;align-items:center;justify-content:center;gap:8px;padding:16px 28px;background:linear-gradient(135deg,#d4af37,#f4d29c);color:#1a1410;border:0;border-radius:999px;font-weight:800;font-size:15px;letter-spacing:-.01em;cursor:pointer;transition:.2s;width:100%}}
.adq-submit:hover:not(:disabled){{transform:translateY(-1px);box-shadow:0 12px 30px rgba(212,175,55,.36)}}
.adq-submit:disabled{{opacity:.6;cursor:wait}}
.adq-result{{padding:14px 18px;border-radius:10px;font-size:13.5px;line-height:1.7;margin-top:14px;display:none}}
.adq-result.ok{{background:rgba(91,200,140,.12);border:1px solid rgba(91,200,140,.4);color:#9fd9b8;display:block}}
.adq-result.err{{background:rgba(255,100,100,.10);border:1px solid rgba(255,100,100,.36);color:#ffacac;display:block}}
.adq-privacy{{font-size:12px;color:var(--dim);line-height:1.65;margin-top:10px;padding-top:14px;border-top:1px solid var(--line)}}
.adq-privacy a{{color:var(--blue-1)}}
@media(max-width:680px){{.adq-grid{{grid-template-columns:1fr}}.adq-form{{padding:28px 22px}}}}
</style>

<section class="wrap" style="padding-bottom:30px">
  <span class="kicker" style="color:#d4af37">AD INQUIRY · 광고문의</span>
  <h1 style="font-size:clamp(32px,4.5vw,52px);margin:14px 0 16px">광고 등록<br><span class="grad">신청서</span></h1>
  <p class="lead">신청서를 제출하시면 담당 매니저가 평일 1영업일 내(평일 영업시간 신청은 1~3시간 내)에 직접 연락드립니다. VVIP·VIP·프리미엄 3개 등급 중 어떤 상품이 적합한지 무료 진단해드리며, 견적과 노출 위치 시뮬레이션을 함께 제공합니다.</p>
</section>

<section class="wrap" style="padding-top:0;padding-bottom:30px">
  <form id="adqForm" class="adq-form" novalidate>
    <div class="adq-grid">
      <div class="adq-field">
        <label class="adq-label" for="adq-name">성명 <span class="req">*</span></label>
        <input id="adq-name" name="name" class="adq-input" type="text" required minlength="2" maxlength="20" autocomplete="name" placeholder="홍길동">
      </div>
      <div class="adq-field">
        <label class="adq-label" for="adq-phone">연락처 <span class="req">*</span></label>
        <input id="adq-phone" name="phone" class="adq-input" type="tel" required pattern="[0-9\\-+\\s()]{{8,20}}" autocomplete="tel" placeholder="010-1234-5678">
      </div>
      <div class="adq-field">
        <label class="adq-label" for="adq-region">지역 <span class="req">*</span></label>
        <select id="adq-region" name="region" class="adq-select" required>
          <option value="">— 선택해주세요 —</option>
          {region_opts}
          <option value="기타">기타·전국</option>
        </select>
      </div>
      <div class="adq-field">
        <label class="adq-label" for="adq-tier">희망 광고 등급 (선택)</label>
        <select id="adq-tier" name="tier" class="adq-select">
          <option value="">— 추천 받기 —</option>
          <option value="VVIP">VVIP · 월 44만원~</option>
          <option value="VIP">VIP · 월 20만원~</option>
          <option value="프리미엄">프리미엄 · 월 13만원~</option>
          <option value="미정">상담 후 결정</option>
        </select>
      </div>
      <div class="adq-field full">
        <label class="adq-label" for="adq-message">전달 메시지 <span class="req">*</span></label>
        <textarea id="adq-message" name="message" class="adq-text" required minlength="5" maxlength="1000" placeholder="샵 상호, 운영 지역, 희망 게재 시작일, 궁금한 점 등을 자유롭게 작성해주세요."></textarea>
      </div>
      <input type="text" name="website" class="adq-honey" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="adq-field full">
        <button id="adqBtn" class="adq-submit" type="submit">
          <span class="btn-label">광고문의 보내기 →</span>
          <span class="btn-spinner" style="display:none">전송 중...</span>
        </button>
        <div id="adqResult" class="adq-result"></div>
        <p class="adq-privacy">제출하시면 <a href="/policy/privacy/">개인정보처리방침</a>에 동의하신 것으로 간주됩니다. 입력한 정보는 광고 상담 응대 목적으로만 사용되며, 응대 종료 후 30일 이내 자동 파기됩니다.</p>
      </div>
    </div>
  </form>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">왜 이 폼인가요?</span>
    <h2 style="margin-top:8px">광고문의 폼의 장점</h2>
    <p class="lead" style="margin:14px auto 0">전화·이메일과 동일한 상담이 가능하면서, 야간·주말에도 시점 제약 없이 접수 가능합니다.</p>
  </div>
  <div class="note-stack">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">24시간 접수</h3><div class="note-text"><p>평일 영업시간 외에도 신청서를 제출할 수 있어, 본인의 업무 일정에 맞게 활용 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">사전 정리된 상담</h3><div class="note-text"><p>샵 정보·희망 등급·메시지를 미리 정리해 제출하므로, 첫 통화에서 바로 견적·일정 협의가 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">기록 보존</h3><div class="note-text"><p>모든 신청 내역은 운영팀 내부 시스템에 기록되어 응대 누락이 발생하지 않습니다. 추후 동일 사안 재문의 시 이력을 그대로 이어 안내드립니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">100% 무료</h3><div class="note-text"><p>광고 상담·견적·노출 위치 시뮬레이션 모두 무료입니다. 실제 게재 결정 후에만 비용이 발생합니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">신청 후 절차</span>
    <h2 style="margin-top:8px">접수부터 광고 게재까지</h2>
  </div>
  <div class="note-stack">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">신청서 접수 (즉시)</h3><div class="note-text"><p>신청서 제출 즉시 운영팀 텔레그램으로 자동 전달됩니다. 평일 영업시간 내 신청은 1~3시간, 야간·주말 신청은 다음 영업일 오전에 회신됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">맞춤 견적 안내 (1영업일)</h3><div class="note-text"><p>샵 정보·지역·희망 등급을 바탕으로 가장 적합한 광고 상품을 무료 진단합니다. 노출 위치 시뮬레이션과 예상 효과 데이터(노출 수·CTR·전환율)를 함께 안내드립니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">결제·계약 (2~3영업일)</h3><div class="note-text"><p>세금계산서 발행 후 계좌이체. 6·12개월 장기 계약 시 분납 협의 가능합니다. 카드 결제도 별도 협의 후 가능합니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">광고 게재 (결제 후 1영업일)</h3><div class="note-text"><p>결제 확인 시점부터 광고가 메인·업종·지역 페이지에 자동 노출되며, 광고 상세 페이지(/ad/공고번호/)도 함께 생성됩니다. 구글 채용 검색 색인 등록까지 자동 완료됩니다.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 36px">
    <span class="kicker">FAQ</span>
    <h2 style="margin-top:8px">자주 묻는 질문</h2>
  </div>
  <div style="max-width:860px;margin:0 auto">
"""
    for q,a in faqs:
        body += f'<details><summary>{q}<span>+</span></summary><div>{a}</div></details>'
    body += f"""
  </div>
</section>

<section class="wrap" style="padding-top:30px">
  <div style="padding:40px;border-radius:22px;background:linear-gradient(135deg,rgba(212,175,55,.08),rgba(91,155,255,.04));border:1px solid rgba(212,175,55,.25);text-align:center">
    <span class="kicker" style="color:#d4af37">자세한 가격은</span>
    <h2 style="margin:10px 0 14px">광고 상품 안내에서 확인하세요</h2>
    <p class="lead" style="margin:0 auto 24px">VVIP·VIP·프리미엄 3등급의 상세 단가와 노출 위치를 한 페이지에서 비교할 수 있습니다.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="/pricing-ads/">광고 상품 안내 →</a>
      <a class="btn btn-ghost" href="tel:{COMPANY['tel']}">{COMPANY['tel']} 전화</a>
    </div>
  </div>
</section>

<script>
(function(){{
  // Cloudflare Pages Function — same-origin endpoint (자동 배포)
  var WORKER_URL = "/api/contact-ads";

  var form = document.getElementById('adqForm');
  var btn = document.getElementById('adqBtn');
  var btnLabel = btn.querySelector('.btn-label');
  var btnSpin = btn.querySelector('.btn-spinner');
  var result = document.getElementById('adqResult');

  function setBusy(b){{
    btn.disabled = b;
    btnLabel.style.display = b ? 'none' : 'inline';
    btnSpin.style.display = b ? 'inline' : 'none';
  }}
  function show(cls, msg){{
    result.className = 'adq-result ' + cls;
    result.innerHTML = msg;
  }}

  form.addEventListener('submit', function(e){{
    e.preventDefault();
    if(!form.checkValidity()){{
      form.reportValidity();
      return;
    }}
    // honeypot
    if(form.website && form.website.value){{ return; }}

    var data = {{
      name: form.name.value.trim(),
      phone: form.phone.value.trim(),
      region: form.region.value,
      tier: form.tier.value,
      message: form.message.value.trim(),
      page: location.pathname,
      referrer: document.referrer || '',
      ts: new Date().toISOString()
    }};

    setBusy(true);
    show('', '');

    fetch(WORKER_URL, {{
      method: 'POST',
      headers: {{'Content-Type':'application/json'}},
      body: JSON.stringify(data)
    }})
    .then(function(r){{ return r.json().catch(function(){{ return {{ok:r.ok}}; }}); }})
    .then(function(j){{
      setBusy(false);
      if(j && j.ok){{
        show('ok', '✓ 광고문의가 정상 접수되었습니다.<br>담당 매니저가 평일 1영업일 내(영업시간 신청은 1~3시간 내)에 연락드립니다. 입력하신 연락처를 다시 한 번 확인해주세요.');
        form.reset();
      }} else {{
        show('err', '전송에 일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주시거나, 전화 <a href="tel:{COMPANY["tel"]}" style="color:#ffacac;font-weight:700">{COMPANY["tel"]}</a> 또는 이메일 <a href="mailto:{COMPANY["email"]}" style="color:#ffacac;font-weight:700">{COMPANY["email"]}</a>로 직접 문의 부탁드립니다.');
      }}
    }})
    .catch(function(){{
      setBusy(false);
      show('err', '네트워크 오류가 발생했습니다. 인터넷 연결을 확인하시거나 전화 <a href="tel:{COMPANY["tel"]}" style="color:#ffacac;font-weight:700">{COMPANY["tel"]}</a>로 직접 문의 부탁드립니다.');
    }});
  }});
}})();
</script>
"""
    return page(title, desc, "/contact-ads/", body, extra_jsonld=extra_ld)
