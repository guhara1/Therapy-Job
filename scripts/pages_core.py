"""핵심 페이지 생성 — 메인, About, Contact, Pricing, Reviews, Policy"""
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import SERVICES, NATIONALITIES, REGIONS, MAGAZINE, SAMPLE_JOBS, TEAM, DISTRICTS, AD_TIERS

# ─────────────────────────────────────────────
# 메인 페이지
# ─────────────────────────────────────────────
def build_index():
    title = f"{COMPANY['brand_kr']} — 전국 마사지 구인구직 1번지 | 스웨디시·아로마·타이·로미로미·스포츠"
    desc = f"마사지 관리사 구인구직 · 전국 82개 행정구 · 5,820여건 채용 공고 · 매일 업데이트. 샵·관리사 연결 평균 47시간. 직업정보제공사업 신고 {COMPANY['job_info_reg']}."

    # ─── 광고 3단계 (VVIP / VIP / 프리미엄) ───
    # 같은 등급 내 선등록순 (registered 오름차순 → 먼저 등록된 공고가 위)
    def tier_cards(tier_slug, layout="grid"):
        tier = next(t for t in AD_TIERS if t["slug"]==tier_slug)
        jobs = sorted(
            [j for j in SAMPLE_JOBS if j.get("tier")==tier_slug],
            key=lambda x: x["registered"]
        )[:tier["max"]]
        cards = ""
        for idx, j in enumerate(jobs):
            svc = next(s for s in SERVICES if s["slug"]==j["service"])
            perks = "".join(f'<span class="ad-perk">{p}</span>' for p in j.get("perks",[]))
            if tier_slug == "vvip":
                cards += f"""<a class="ad-card ad-vvip reveal" href="/jobs/{j['service']}/">
  <div class="ad-rank">#{idx+1:02d}</div>
  <div class="ad-tier-label">VVIP</div>
  <div class="ad-body">
    <div class="ad-meta-top"><span class="kicker">{svc['kicker']}</span><span class="ad-id">공고 #{j['id']}</span></div>
    <h3 class="ad-title">{j['title']}</h3>
    <div class="ad-shop">{j['shop']}</div>
    <div class="ad-meta-row"><span>📍 {j['region']}</span></div>
    <div class="ad-perks">{perks}</div>
    <div class="ad-pay-row"><span class="ad-pay">{j['pay']}</span><span class="ad-arrow">상세 →</span></div>
  </div>
</a>"""
            elif tier_slug == "vip":
                cards += f"""<a class="ad-card ad-vip reveal" href="/jobs/{j['service']}/">
  <div class="ad-rank-sm">#{idx+1:02d}</div>
  <div class="ad-meta-top"><span class="kicker">{svc['kicker']}</span><span class="ad-tier-label-sm">VIP</span></div>
  <h3 class="ad-title-sm">{j['title']}</h3>
  <div class="ad-shop-sm">{j['shop']} · {j['region']}</div>
  <div class="ad-perks">{perks}</div>
  <div class="ad-pay-row"><span class="ad-pay-sm">{j['pay']}</span><span class="ad-id">#{j['id']}</span></div>
</a>"""
            else:  # premium
                cards += f"""<a class="ad-card ad-premium reveal" href="/jobs/{j['service']}/">
  <div class="ad-meta-top"><span class="kicker" style="font-size:10px">{svc['kicker'].split(' · ')[0]}</span><span class="ad-tier-label-xs">PREMIUM</span></div>
  <h3 class="ad-title-xs">{j['title']}</h3>
  <div class="ad-meta-row"><span>{j['region']}</span></div>
  <div class="ad-pay-row"><span class="ad-pay-xs">{j['pay']}</span><span class="ad-id">#{j['id']}</span></div>
</a>"""
        return cards

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

<style>
.ad-card{{display:block;border-radius:18px;padding:24px 26px;transition:.25s;position:relative;overflow:hidden}}
.ad-card:hover{{transform:translateY(-3px)}}
.ad-perk{{display:inline-block;padding:3px 9px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid var(--line);font-size:11px;color:var(--muted);margin-right:6px;margin-top:4px}}
.ad-pay-row{{display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding-top:14px;border-top:1px solid var(--line)}}
.ad-arrow{{font-size:12px;color:var(--blue-1);font-weight:700}}
.ad-id{{font-size:10.5px;color:var(--dim);letter-spacing:.06em}}
.ad-meta-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}}
.ad-meta-row{{font-size:12.5px;color:var(--muted);margin-top:4px}}
/* VVIP — 골드, 대형 */
.ad-vvip{{background:linear-gradient(135deg,#1a1410 0%,#2a1f12 100%);border:1px solid rgba(212,175,55,.35);box-shadow:0 8px 28px rgba(0,0,0,.4)}}
.ad-vvip::before{{content:"";position:absolute;left:0;top:0;right:0;height:3px;background:linear-gradient(90deg,#d4af37,#f4d29c,#d4af37)}}
.ad-vvip:hover{{border-color:rgba(212,175,55,.7);box-shadow:0 14px 38px rgba(212,175,55,.18)}}
.ad-vvip .ad-rank{{position:absolute;top:18px;right:22px;font-family:"Cormorant Garamond",serif;font-size:38px;font-style:italic;font-weight:300;color:rgba(212,175,55,.5);line-height:1}}
.ad-vvip .ad-tier-label{{display:inline-block;padding:5px 12px;background:linear-gradient(135deg,#d4af37,#f4d29c);color:#1a1410;font-size:10.5px;letter-spacing:.22em;font-weight:800;border-radius:5px;margin-bottom:14px}}
.ad-vvip .ad-title{{font-size:20px;font-weight:800;letter-spacing:-.022em;line-height:1.35;margin-bottom:6px;color:#f4d29c}}
.ad-vvip .ad-shop{{font-size:13.5px;color:#d4af37;font-weight:600;margin-bottom:8px}}
.ad-vvip .ad-pay{{font-size:18px;font-weight:800;color:#f4d29c}}
.ad-vvip .kicker{{color:#d4af37}}
/* VIP — 블루, 중형 */
.ad-vip{{background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid rgba(123,176,255,.32)}}
.ad-vip::before{{content:"";position:absolute;left:0;top:0;right:0;height:2px;background:var(--grad)}}
.ad-vip:hover{{border-color:rgba(123,176,255,.6);box-shadow:0 12px 32px rgba(91,155,255,.15)}}
.ad-vip .ad-rank-sm{{position:absolute;top:18px;right:22px;font-family:"Cormorant Garamond",serif;font-size:28px;font-style:italic;font-weight:300;color:rgba(123,176,255,.45);line-height:1}}
.ad-vip .ad-tier-label-sm{{display:inline-block;padding:3px 10px;background:var(--grad);color:#fff;font-size:10px;letter-spacing:.2em;font-weight:800;border-radius:4px}}
.ad-vip .ad-title-sm{{font-size:17px;font-weight:800;letter-spacing:-.02em;line-height:1.4;margin:8px 0 4px}}
.ad-vip .ad-shop-sm{{font-size:12.5px;color:var(--muted);margin-bottom:6px}}
.ad-vip .ad-pay-sm{{font-size:15px;font-weight:800;color:var(--blue-1)}}
/* 프리미엄 — 그레이, 컴팩트 */
.ad-premium{{background:var(--surface);border:1px solid var(--line);padding:18px 20px}}
.ad-premium:hover{{border-color:rgba(160,168,190,.4)}}
.ad-premium .ad-tier-label-xs{{font-size:9.5px;letter-spacing:.2em;font-weight:700;color:var(--dim);padding:2px 7px;border:1px solid var(--line);border-radius:4px}}
.ad-premium .ad-title-xs{{font-size:14.5px;font-weight:700;line-height:1.4;margin:6px 0 4px;color:var(--text)}}
.ad-premium .ad-pay-xs{{font-size:13.5px;font-weight:700;color:var(--text)}}
.ad-premium .ad-pay-row{{margin-top:10px;padding-top:10px}}
/* 등급 섹션 헤더 */
.ad-section-head{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:30px;flex-wrap:wrap;gap:14px}}
.ad-section-head h2{{margin-bottom:6px}}
.ad-section-sub{{font-size:13px;color:var(--muted);letter-spacing:.06em}}
.ad-section-order{{font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;padding:6px 12px;border:1px solid var(--line);border-radius:999px;color:var(--muted)}}
</style>

<section class="wrap" style="padding-bottom:30px">
  <div class="ad-section-head">
    <div>
      <span class="kicker" style="color:#d4af37">VVIP · 최상단 노출</span>
      <h2>VVIP 채용정보</h2>
      <div class="ad-section-sub">메인 페이지 최상단 단독 영역 · 등록 순서대로 노출</div>
    </div>
    <span class="ad-section-order" style="color:#d4af37;border-color:rgba(212,175,55,.4)">선등록순 정렬</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px">{tier_cards("vvip")}</div>
</section>

<section class="wrap" style="padding-top:0;padding-bottom:30px">
  <div class="ad-section-head">
    <div>
      <span class="kicker" style="color:var(--blue-1)">VIP · 우선 노출</span>
      <h2>VIP 채용정보</h2>
      <div class="ad-section-sub">메인 페이지 두 번째 영역 · 등록 순서대로 노출</div>
    </div>
    <span class="ad-section-order" style="color:var(--blue-1);border-color:rgba(123,176,255,.4)">선등록순 정렬</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px">{tier_cards("vip")}</div>
</section>

<section class="wrap" style="padding-top:0">
  <div class="ad-section-head">
    <div>
      <span class="kicker" style="color:var(--muted)">PREMIUM · 기본 노출</span>
      <h2>프리미엄 채용정보</h2>
      <div class="ad-section-sub">메인 페이지 세 번째 영역 · 등록 제한 없음</div>
    </div>
    <span class="ad-section-order">등록 제한 없음</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px">{tier_cards("premium")}</div>
  <div style="text-align:center;margin-top:44px">
    <a class="btn btn-ghost" href="/jobs/">전체 공고 보기 →</a>
    <a class="btn btn-primary" href="/contact/" style="margin-left:8px">광고 등록 문의 →</a>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <div style="text-align:center;max-width:760px;margin:0 auto 60px">
    <span class="kicker">BY SERVICE</span>
    <h2>업종별 채용 현황</h2>
    <p class="lead" style="margin:18px auto 0">5개 핵심 업종의 평균 일급 시세와 현재 모집 중인 공고 수를 한눈에 정리했습니다.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px">{svc_cards}</div>
</section>

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
