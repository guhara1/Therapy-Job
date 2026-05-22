"""광고 시스템 — 등급별 카드 렌더링 + 상세 페이지 생성"""
from templates import page, breadcrumb_ld, faq_ld, COMPANY
from data import SAMPLE_JOBS, SERVICES, AD_TIERS, REGIONS, DISTRICTS

# 광고 인라인 CSS (모든 페이지에서 재사용)
AD_CSS = """
<style>
.ad-card{display:block;border-radius:18px;padding:24px 26px;transition:.25s;position:relative;overflow:hidden}
.ad-card:hover{transform:translateY(-3px)}
.ad-perk{display:inline-block;padding:3px 9px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid var(--line);font-size:11px;color:var(--muted);margin-right:6px;margin-top:4px}
.ad-pay-row{display:flex;justify-content:space-between;align-items:center;margin-top:14px;padding-top:14px;border-top:1px solid var(--line)}
.ad-arrow{font-size:12px;color:var(--blue-1);font-weight:700}
.ad-id{font-size:10.5px;color:var(--dim);letter-spacing:.06em}
.ad-meta-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.ad-meta-row{font-size:12.5px;color:var(--muted);margin-top:4px}
.ad-vvip{background:linear-gradient(135deg,#1a1410 0%,#2a1f12 100%);border:1px solid rgba(212,175,55,.35);box-shadow:0 8px 28px rgba(0,0,0,.4)}
.ad-vvip::before{content:"";position:absolute;left:0;top:0;right:0;height:3px;background:linear-gradient(90deg,#d4af37,#f4d29c,#d4af37)}
.ad-vvip:hover{border-color:rgba(212,175,55,.7);box-shadow:0 14px 38px rgba(212,175,55,.18)}
.ad-vvip .ad-rank{position:absolute;top:18px;right:22px;font-family:"Cormorant Garamond",serif;font-size:38px;font-style:italic;font-weight:300;color:rgba(212,175,55,.5);line-height:1}
.ad-vvip .ad-tier-label{display:inline-block;padding:5px 12px;background:linear-gradient(135deg,#d4af37,#f4d29c);color:#1a1410;font-size:10.5px;letter-spacing:.22em;font-weight:800;border-radius:5px;margin-bottom:14px}
.ad-vvip .ad-title{font-size:20px;font-weight:800;letter-spacing:-.022em;line-height:1.35;margin-bottom:6px;color:#f4d29c}
.ad-vvip .ad-shop{font-size:13.5px;color:#d4af37;font-weight:600;margin-bottom:8px}
.ad-vvip .ad-pay{font-size:18px;font-weight:800;color:#f4d29c}
.ad-vvip .kicker{color:#d4af37}
.ad-vip{background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid rgba(123,176,255,.32)}
.ad-vip::before{content:"";position:absolute;left:0;top:0;right:0;height:2px;background:var(--grad)}
.ad-vip:hover{border-color:rgba(123,176,255,.6);box-shadow:0 12px 32px rgba(91,155,255,.15)}
.ad-vip .ad-rank-sm{position:absolute;top:18px;right:22px;font-family:"Cormorant Garamond",serif;font-size:28px;font-style:italic;font-weight:300;color:rgba(123,176,255,.45);line-height:1}
.ad-vip .ad-tier-label-sm{display:inline-block;padding:3px 10px;background:var(--grad);color:#fff;font-size:10px;letter-spacing:.2em;font-weight:800;border-radius:4px}
.ad-vip .ad-title-sm{font-size:17px;font-weight:800;letter-spacing:-.02em;line-height:1.4;margin:8px 0 4px}
.ad-vip .ad-shop-sm{font-size:12.5px;color:var(--muted);margin-bottom:6px}
.ad-vip .ad-pay-sm{font-size:15px;font-weight:800;color:var(--blue-1)}
.ad-premium{background:var(--surface);border:1px solid var(--line);padding:18px 20px}
.ad-premium:hover{border-color:rgba(160,168,190,.4)}
.ad-premium .ad-tier-label-xs{font-size:9.5px;letter-spacing:.2em;font-weight:700;color:var(--dim);padding:2px 7px;border:1px solid var(--line);border-radius:4px}
.ad-premium .ad-title-xs{font-size:14.5px;font-weight:700;line-height:1.4;margin:6px 0 4px;color:var(--text)}
.ad-premium .ad-pay-xs{font-size:13.5px;font-weight:700;color:var(--text)}
.ad-premium .ad-pay-row{margin-top:10px;padding-top:10px}
.ad-section-head{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:30px;flex-wrap:wrap;gap:14px}
.ad-section-head h2{margin-bottom:6px}
.ad-section-sub{font-size:13px;color:var(--muted);letter-spacing:.06em}
.ad-section-order{font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;font-weight:700;padding:6px 12px;border:1px solid var(--line);border-radius:999px;color:var(--muted)}
.ad-empty{padding:30px;text-align:center;border:1px dashed var(--line);border-radius:14px;color:var(--muted);font-size:13.5px}
</style>
"""

TIER_STYLES = {
    "vvip":  {"color":"#d4af37","border":"rgba(212,175,55,.4)","label":"VVIP · 최상단 노출","name":"VVIP 채용정보","sub":"단독 영역 · 등록 순서대로 노출","order":"선등록순 정렬"},
    "vip":   {"color":"var(--blue-1)","border":"rgba(123,176,255,.4)","label":"VIP · 우선 노출","name":"VIP 채용정보","sub":"우선 영역 · 등록 순서대로 노출","order":"선등록순 정렬"},
    "premium":{"color":"var(--muted)","border":"var(--line)","label":"PREMIUM · 기본 노출","name":"프리미엄 채용정보","sub":"기본 영역 · 등록 제한 없음","order":"등록 제한 없음"},
}

def filter_jobs(tier=None, service=None, region_slug=None):
    """광고 필터링 → 선등록순 정렬"""
    jobs = list(SAMPLE_JOBS)
    if tier:
        jobs = [j for j in jobs if j.get("tier")==tier]
    if service:
        jobs = [j for j in jobs if j.get("service")==service]
    if region_slug:
        jobs = [j for j in jobs if j.get("region_slug")==region_slug]
    return sorted(jobs, key=lambda j: j.get("registered",""))

def render_card(j, idx=0):
    """광고 1건을 등급에 맞는 카드로 렌더"""
    svc = next(s for s in SERVICES if s["slug"]==j["service"])
    perks = "".join(f'<span class="ad-perk">{p}</span>' for p in j.get("perks",[]))
    tier = j.get("tier","premium")
    href = f"/ad/{j['id']}/"
    if tier == "vvip":
        return f"""<a class="ad-card ad-vvip reveal" href="{href}">
  <div class="ad-rank">#{idx+1:02d}</div>
  <span class="ad-tier-label">VVIP</span>
  <div class="ad-meta-top"><span class="kicker">{svc['kicker']}</span><span class="ad-id">공고 #{j['id']}</span></div>
  <h3 class="ad-title">{j['title']}</h3>
  <div class="ad-shop">{j['shop']}</div>
  <div class="ad-meta-row">📍 {j['region']}</div>
  <div class="ad-perks">{perks}</div>
  <div class="ad-pay-row"><span class="ad-pay">{j['pay']}</span><span class="ad-arrow">상세 →</span></div>
</a>"""
    if tier == "vip":
        return f"""<a class="ad-card ad-vip reveal" href="{href}">
  <div class="ad-rank-sm">#{idx+1:02d}</div>
  <div class="ad-meta-top"><span class="kicker">{svc['kicker']}</span><span class="ad-tier-label-sm">VIP</span></div>
  <h3 class="ad-title-sm">{j['title']}</h3>
  <div class="ad-shop-sm">{j['shop']} · {j['region']}</div>
  <div class="ad-perks">{perks}</div>
  <div class="ad-pay-row"><span class="ad-pay-sm">{j['pay']}</span><span class="ad-id">#{j['id']}</span></div>
</a>"""
    # premium
    return f"""<a class="ad-card ad-premium reveal" href="{href}">
  <div class="ad-meta-top"><span class="kicker" style="font-size:10px">{svc['kicker'].split(' · ')[0]}</span><span class="ad-tier-label-xs">PREMIUM</span></div>
  <h3 class="ad-title-xs">{j['title']}</h3>
  <div class="ad-meta-row">{j['region']}</div>
  <div class="ad-pay-row"><span class="ad-pay-xs">{j['pay']}</span><span class="ad-id">#{j['id']}</span></div>
</a>"""

def render_tier_section(tier, jobs, max_count=None):
    """등급별 섹션 1개 렌더 (헤드 + 카드 그리드)"""
    s = TIER_STYLES[tier]
    if max_count:
        jobs = jobs[:max_count]
    if not jobs:
        cards_html = f'<div class="ad-empty">현재 해당 카테고리·지역에 등록된 {s["name"]}이 없습니다. 광고 등록 문의: <a href="/contact/" style="color:var(--blue-1)">고객센터 →</a></div>'
    else:
        cards = "".join(render_card(j, i) for i,j in enumerate(jobs))
        if tier == "vvip":
            grid_min = "280px"
        elif tier == "vip":
            grid_min = "240px"
        else:
            grid_min = "220px"
        cards_html = f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax({grid_min},1fr));gap:14px">{cards}</div>'

    return f"""<div class="ad-section-head">
  <div>
    <span class="kicker" style="color:{s['color']}">{s['label']}</span>
    <h2>{s['name']}</h2>
    <div class="ad-section-sub">{s['sub']}</div>
  </div>
  <span class="ad-section-order" style="color:{s['color']};border-color:{s['border']}">{s['order']}</span>
</div>
{cards_html}"""

def render_all_tiers(service=None, region_slug=None, context_label=""):
    """3단계 광고 섹션 전체 (VVIP → VIP → 프리미엄)"""
    sections = []
    intro = f'<div style="text-align:center;max-width:760px;margin:0 auto 40px"><span class="kicker">PAID LISTINGS</span><h2 style="margin-top:8px">{context_label} 광고 채용정보</h2><p class="lead" style="margin-top:14px">유료 광고는 VVIP → VIP → 프리미엄 3단계로 노출되며, 각 등급 내에서는 선등록순으로 정렬됩니다.</p></div>' if context_label else ""
    out = [intro]
    out.append('<section class="wrap" style="padding-bottom:30px">')
    for tier in ["vvip","vip","premium"]:
        jobs = filter_jobs(tier=tier, service=service, region_slug=region_slug)
        max_c = next(t["max"] for t in AD_TIERS if t["slug"]==tier)
        out.append(render_tier_section(tier, jobs, max_c))
        if tier != "premium":
            out.append('</section><section class="wrap" style="padding-top:0;padding-bottom:30px">')
    out.append('</section>')
    return AD_CSS + "\n".join(out)


# ─────────────────────────────────────────────
# 광고 상세 페이지
# ─────────────────────────────────────────────
def build_ad_detail(j):
    svc = next(s for s in SERVICES if s["slug"]==j["service"])
    tier = j.get("tier","premium")
    tier_label = {"vvip":"VVIP","vip":"VIP","premium":"PREMIUM"}[tier]
    tier_color = TIER_STYLES[tier]["color"]
    tier_border = TIER_STYLES[tier]["border"]

    title = f"[{j['shop']}] {j['title']} · {j['region']} | {COMPANY['brand_kr']}"
    desc = f"{j['shop']} {j['title']}. 지역: {j['region']} · 일급: {j['pay']} · 근무: {j['hours']} · 모집인원 {j['positions']}명. 인센티브·정산·복지 상세."

    perks_html = "".join(f'<li style="padding:10px 14px;background:var(--surface);border:1px solid var(--line);border-radius:10px;font-size:13.5px"><span style="color:var(--blue-1);margin-right:6px">●</span>{p}</li>' for p in j["perks"])

    extra_ld = [
        breadcrumb_ld([
            ("홈","/"),
            ("구인공고","/jobs/"),
            (svc["kr"], f"/jobs/{svc['slug']}/"),
            (j["title"], f"/ad/{j['id']}/")
        ]),
        {
            "@type":"JobPosting",
            "@id":f"{COMPANY['base_url']}/ad/{j['id']}/#jobposting",
            "title":j["title"],
            "identifier":{"@type":"PropertyValue","name":COMPANY["brand_kr"],"value":j["id"]},
            "description":f"{j['shop']} {j['title']}. {svc['summary']} 근무 시간 {j['hours']}, 일급 {j['pay']}. 혜택: {', '.join(j['perks'])}.",
            "datePosted":j["registered"]+"T09:00:00+09:00",
            "validThrough":"2026-12-31T23:59:59+09:00",
            "employmentType":"CONTRACTOR" if "프리랜서" in j["contract"] else "FULL_TIME",
            "hiringOrganization":{
                "@type":"Organization","name":j["shop"],
                "sameAs":COMPANY["base_url"]
            },
            "jobLocation":{
                "@type":"Place",
                "address":{
                    "@type":"PostalAddress",
                    "addressLocality":j["region"].split(" ")[-1] if " " in j["region"] else j["region"],
                    "addressRegion":j["region"].split(" ")[0] if " " in j["region"] else "",
                    "addressCountry":"KR"
                }
            },
            "baseSalary":{
                "@type":"MonetaryAmount","currency":"KRW",
                "value":{"@type":"QuantitativeValue","value":j["pay"],"unitText":"DAY"}
            },
            "totalJobOpenings":j["positions"],
            "workHours":j["hours"],
            "industry":"마사지·테라피",
            "applicantLocationRequirements":{"@type":"Country","name":"대한민국"},
            "directApply":False
        }
    ]

    # 관련 공고 (같은 업종, 다른 ID, 최대 4건)
    related = [r for r in SAMPLE_JOBS if r["service"]==j["service"] and r["id"]!=j["id"]][:4]
    related_html = "".join(render_card(r, i) for i,r in enumerate(related))

    body = f"""
{AD_CSS}

<section class="wrap" style="padding-bottom:30px">
  <div style="font-size:12px;color:var(--muted);letter-spacing:.16em;text-transform:uppercase;font-weight:700;margin-bottom:18px">
    <a href="/" style="color:var(--blue-1)">홈</a> · <a href="/jobs/" style="color:var(--blue-1)">구인공고</a> · <a href="/jobs/{svc['slug']}/" style="color:var(--blue-1)">{svc['kr']}</a> · 공고 #{j['id']}
  </div>
  <div style="display:inline-flex;align-items:center;gap:10px;margin-bottom:18px">
    <span style="padding:5px 12px;background:{('linear-gradient(135deg,#d4af37,#f4d29c)' if tier=='vvip' else 'var(--grad)' if tier=='vip' else 'rgba(160,168,190,.16)')};color:{('#1a1410' if tier=='vvip' else '#fff' if tier=='vip' else 'var(--text)')};font-size:11px;letter-spacing:.22em;font-weight:800;border-radius:5px">{tier_label}</span>
    <span class="kicker" style="margin:0">{svc['kicker']}</span>
  </div>
  <h1 style="font-size:clamp(32px,5vw,52px);line-height:1.25;margin-bottom:14px;letter-spacing:-.028em">{j['title']}</h1>
  <div style="font-size:18px;color:{tier_color};font-weight:700;margin-bottom:8px">{j['shop']}</div>
  <div style="font-size:14px;color:var(--muted)">📍 {j['region']} · 공고 #{j['id']} · 등록 {j['registered']}</div>
</section>

<section class="wrap" style="padding-top:0;padding-bottom:40px">
  <div style="display:grid;grid-template-columns:1.5fr 1fr;gap:36px" class="ad-detail-grid">
    <div>
      <h2 style="font-size:24px;margin-bottom:18px">모집 안내</h2>
      <div class="note-text" style="max-width:none;font-size:15px;line-height:1.85;color:#c8ccda">
        <p>{j['shop']}에서 {svc['kr']} 전문 관리사를 모집합니다.</p>
        <p>{svc['summary']}</p>
        <p>본 공고는 {j['region']} 권역에서 운영되며, 인근 동(洞) 단위로 단골 고객이 안정적으로 분포되어 있습니다. 신규 입직자도 견습 1~2주 후 즉시 단가 정상 적용이 가능합니다.</p>
        <p>근무 시간은 {j['hours']}이며, 휴게 시간과 식사 시간이 별도로 보장됩니다. 모집 인원은 {j['positions']}명이며, 선착순 면접 후 채용이 마감됩니다.</p>
      </div>

      <h2 style="font-size:24px;margin:40px 0 18px">제공 혜택</h2>
      <ul style="list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px">{perks_html}</ul>

      <h2 style="font-size:24px;margin:40px 0 18px">근무 조건</h2>
      <div class="note-text" style="max-width:none;color:#c8ccda;line-height:1.85">
        <p><strong style="color:var(--text)">계약 형태</strong> · {j['contract']}. 4대 보험은 적용되지 않으며, 종합소득세는 본인 신고 또는 샵 위임 가능.</p>
        <p><strong style="color:var(--text)">정산</strong> · {j['settle']}. 정산일에 인센티브와 일급이 함께 입금됩니다.</p>
        <p><strong style="color:var(--text)">복장·도구</strong> · 유니폼은 샵에서 제공되며, 개인 위생용품(손 소독제·립밤·면봉)은 본인 부담입니다.</p>
        <p><strong style="color:var(--text)">교육</strong> · 신규 입직자는 견습 1~2주 동안 샵 시술 매뉴얼·응대 톤·동선을 익힙니다.</p>
      </div>

      <h2 style="font-size:24px;margin:40px 0 18px">우대 사항</h2>
      <div class="note-text" style="max-width:none;color:#c8ccda;line-height:1.85">
        <p>· {svc['kr']} 경력 1년 이상</p>
        <p>· 본인 시그니처 스트로크가 있는 분</p>
        <p>· 응대 매너·청결도 좋으신 분</p>
        <p>· 단가 협상은 면접 후 경력에 따라 조정됩니다.</p>
      </div>
    </div>

    <aside>
      <div style="position:sticky;top:90px;padding:28px;border-radius:18px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid {tier_border}">
        <div style="text-align:center;margin-bottom:20px">
          <div class="kicker" style="color:{tier_color}">일급</div>
          <div style="font-size:30px;font-weight:800;color:{tier_color};letter-spacing:-.02em;margin-top:6px">{j['pay']}</div>
        </div>
        <div style="display:flex;flex-direction:column;gap:12px;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)">
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">샵</span><span style="font-weight:700">{j['shop']}</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">업종</span><span style="font-weight:700">{svc['kr']}</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">지역</span><span style="font-weight:700;text-align:right">{j['region']}</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">근무시간</span><span style="font-weight:700">{j['hours']}</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">모집인원</span><span style="font-weight:700">{j['positions']}명</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">계약</span><span style="font-weight:700">{j['contract']}</span></div>
          <div style="display:flex;justify-content:space-between;font-size:13.5px"><span style="color:var(--muted)">정산</span><span style="font-weight:700">{j['settle']}</span></div>
        </div>
        <div style="margin-top:18px;display:flex;flex-direction:column;gap:10px">
          <a class="btn btn-primary" style="justify-content:center;width:100%" href="tel:{COMPANY['tel']}">{COMPANY['tel']} 지원</a>
          <a class="btn btn-ghost" style="justify-content:center;width:100%" href="mailto:{COMPANY['email']}?subject=공고 {j['id']} 지원">이메일 문의</a>
        </div>
        <p style="font-size:11.5px;color:var(--dim);margin-top:14px;text-align:center;line-height:1.65">고객센터 {COMPANY['tel_hours']}<br>지원 시 공고 번호 #{j['id']} 안내</p>
      </div>
    </aside>
  </div>
</section>
<style>@media(max-width:920px){{.ad-detail-grid{{grid-template-columns:1fr!important}}}}</style>

<section class="wrap" style="padding-top:0">
  <h2>지원 절차</h2>
  <div class="note-stack" style="margin-top:30px">
    <div class="note-card"><div class="note-num">01</div><div class="note-content"><h3 class="note-title">전화 또는 이메일로 문의</h3><div class="note-text"><p>고객센터 {COMPANY['tel']}로 전화 주시고, 공고 번호 <strong>#{j['id']}</strong>를 안내해주세요.</p><p>이메일은 {COMPANY['email']}로 제목에 공고 번호를 포함해 보내주세요.</p></div></div></div>
    <div class="note-card"><div class="note-num">02</div><div class="note-content"><h3 class="note-title">기본 정보 확인</h3><div class="note-text"><p>경력·희망 시작일·근무 가능 시간을 알려주시면 샵 측에 빠르게 전달됩니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">03</div><div class="note-content"><h3 class="note-title">면접 일정 확정</h3><div class="note-text"><p>샵과 직접 일정을 조율한 뒤 면접일이 확정됩니다. 평균 매칭 시간은 47시간입니다.</p></div></div></div>
    <div class="note-card"><div class="note-num">04</div><div class="note-content"><h3 class="note-title">계약 · 첫 출근</h3><div class="note-text"><p>프리랜서 계약서를 확인한 뒤 첫 출근 일정을 정합니다.</p><p>계약 시 인센티브 비율·정산 주기·교통비를 다시 한 번 확인하세요.</p></div></div></div>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>자주 묻는 질문</h2>
  <div style="max-width:860px;margin:30px auto 0">
    <details><summary>지원 시 자격증이 꼭 필요한가요?<span>+</span></summary><div>업종에 따라 다릅니다. {svc['kr']}의 경우 자격증보다는 경력과 시술 일관성을 더 중요하게 봅니다.</div></details>
    <details><summary>견습 기간 단가는 어떻게 되나요?<span>+</span></summary><div>견습 1~2주 동안은 정상 단가의 70~80% 수준에서 시작하며, 견습 완료 후 정상 단가로 전환됩니다.</div></details>
    <details><summary>야간·새벽 근무가 필수인가요?<span>+</span></summary><div>본 공고의 근무 시간은 {j['hours']}입니다. 시간대 조정이 필요하면 면접 시 협의 가능합니다.</div></details>
    <details><summary>다른 샵 단골을 데려와도 되나요?<span>+</span></summary><div>이전 샵 단골을 새 샵으로 이동시키는 것은 영업 분쟁의 원인이 됩니다. 신규 단골 확보를 권장합니다.</div></details>
    <details><summary>면접 합격까지 얼마나 걸리나요?<span>+</span></summary><div>평균 47시간 안에 면접·매칭이 완료됩니다. 본 공고는 선착순이므로 조기 마감될 수 있습니다.</div></details>
  </div>
</section>

<section class="wrap" style="padding-top:0">
  <h2>같은 업종 다른 공고</h2>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:30px">{related_html}</div>
</section>

<section class="wrap" style="padding-top:40px">
  <div style="padding:50px 40px;border-radius:22px;background:linear-gradient(135deg,rgba(91,155,255,.1),rgba(44,84,168,.04));border:1px solid rgba(123,176,255,.18);text-align:center">
    <div class="kicker" style="color:{tier_color}">{tier_label} 광고</div>
    <h2 style="margin:10px 0 14px">지금 #{j['id']} 공고에 지원하세요</h2>
    <p class="lead" style="margin:0 auto 24px">선착순 모집 · 모집 인원 {j['positions']}명</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-primary" href="tel:{COMPANY['tel']}">{COMPANY['tel']}</a>
      <a class="btn btn-ghost" href="/jobs/{svc['slug']}/">{svc['kr']} 전체 공고</a>
    </div>
  </div>
</section>
"""
    return page(title, desc, f"/ad/{j['id']}/", body, extra_jsonld=extra_ld)
