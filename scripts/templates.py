"""공통 HTML 조각 — 헤더, 푸터, CSS, JSON-LD 헬퍼"""
import json
from data import COMPANY, SERVICES, REGIONS, NATIONALITIES, DISTRICTS

# ─────────────────────────────────────────────
# 컬러 토큰 (쿨 블루)
# ─────────────────────────────────────────────
CSS_BASE = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0e1a;
  --surface:#121828;
  --surface-2:#1a2236;
  --line:rgba(255,255,255,.08);
  --text:#eef2fb;
  --muted:#a0a8be;
  --dim:#6c7490;
  --blue-1:#7bb0ff;
  --blue-2:#5b9bff;
  --blue-3:#2c54a8;
  --blue-deep:#1b3a78;
  --grad:linear-gradient(135deg,#7bb0ff 0%,#5b9bff 45%,#2c54a8 100%);
  --grad-soft:linear-gradient(135deg,rgba(123,176,255,.14),rgba(44,84,168,.06));
  --gold:#d6b274;
}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{
  background:var(--bg);color:var(--text);
  font-family:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  line-height:1.65;letter-spacing:-.01em;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
}
a{color:inherit;text-decoration:none}
img{max-width:100%;height:auto;display:block}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
.serif{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-weight:300;font-style:italic}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.wrap{max-width:1240px;margin:0 auto;padding:120px 24px}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--muted);font-weight:600}
.eyebrow .pulse{width:6px;height:6px;border-radius:50%;background:var(--blue-2);box-shadow:0 0 0 0 rgba(91,155,255,.7);animation:pulse 2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 10px rgba(91,155,255,0)}100%{box-shadow:0 0 0 0 rgba(91,155,255,0)}}
/* HEADER */
header{position:sticky;top:0;z-index:100;background:rgba(10,14,26,.78);backdrop-filter:blur(20px);border-bottom:1px solid var(--line)}
.nav{max-width:1240px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px;letter-spacing:-.02em}
.brand .logo-mark{width:36px;height:36px;border-radius:9px;background:var(--grad);display:flex;align-items:center;justify-content:center;color:#fff;font-family:"Cormorant Garamond",serif;font-weight:600;font-style:italic;font-size:22px}
.brand .brand-name{display:flex;flex-direction:column;line-height:1.1}
.brand .brand-name small{font-size:10px;letter-spacing:.18em;color:var(--muted);font-weight:500;text-transform:uppercase;margin-top:2px}
.menu{list-style:none;display:flex;align-items:center;gap:6px}
.menu>li{position:relative}
.menu>li>a,.menu>li>span{display:inline-block;padding:10px 14px;font-size:14px;color:var(--text);font-weight:500;cursor:pointer;border-radius:8px;transition:.2s}
.menu>li>a:hover,.menu>li>span:hover{background:rgba(255,255,255,.04);color:var(--blue-1)}
.submenu{position:absolute;top:100%;left:0;min-width:220px;background:rgba(18,24,40,.98);backdrop-filter:blur(20px);border:1px solid var(--line);border-radius:12px;padding:8px;list-style:none;opacity:0;visibility:hidden;transform:translateY(8px);transition:.2s;box-shadow:0 18px 44px rgba(0,0,0,.4)}
.menu>li:hover>.submenu,.menu>li:focus-within>.submenu{opacity:1;visibility:visible;transform:none}
.submenu a{display:block;padding:9px 12px;font-size:13.5px;color:var(--text);border-radius:7px;transition:.15s}
.submenu a:hover{background:rgba(91,155,255,.12);color:var(--blue-1)}
.cta-pill{background:var(--grad);color:#fff!important;padding:10px 18px!important;border-radius:999px;font-weight:700!important;font-size:13.5px!important;transition:.2s}
.cta-pill:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(91,155,255,.32)}
.cta-gold{background:linear-gradient(135deg,#d4af37,#f4d29c);color:#1a1410!important;padding:10px 16px!important;border-radius:999px;font-weight:800!important;font-size:13px!important;letter-spacing:-.01em;transition:.2s}
.cta-gold:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(212,175,55,.36)}
.toggle{display:none;font-size:24px;padding:6px 10px}
@media(max-width:1100px){
  .toggle{display:inline-block}
  .menu{position:fixed;inset:62px 0 auto 0;background:rgba(10,14,26,.98);backdrop-filter:blur(24px);flex-direction:column;align-items:stretch;padding:16px;gap:4px;max-height:calc(100vh - 62px);overflow:auto;border-bottom:1px solid var(--line);transform:translateY(-100%);transition:.3s}
  .menu.open{transform:none}
  .menu>li{width:100%}
  .menu>li>a,.menu>li>span{display:block;padding:14px 16px}
  .submenu{position:static;opacity:1;visibility:visible;transform:none;box-shadow:none;background:rgba(255,255,255,.03);margin-top:4px}
}
/* FOOTER */
.site-footer{background:#070a14;border-top:1px solid var(--line);margin-top:80px}
.footer-wrap{max-width:1240px;margin:0 auto;padding:80px 24px 40px}
.footer-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:48px;padding-bottom:48px;border-bottom:1px solid var(--line)}
.footer-grid h4{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:18px;font-weight:700}
.footer-grid ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.footer-grid a{font-size:13.5px;color:var(--text);opacity:.78;transition:.15s}
.footer-grid a:hover{opacity:1;color:var(--blue-1)}
.footer-brand p{font-size:13px;color:var(--muted);margin-top:14px;max-width:300px;line-height:1.7}
.footer-ops{padding:32px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:1fr 1fr 1fr;gap:24px}
.footer-ops .ops-block{padding:18px;border-radius:12px;background:var(--grad-soft);border:1px solid var(--line)}
.footer-ops .ops-block .label{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
.footer-ops .ops-block .val{font-size:16px;font-weight:700}
.footer-ops .ops-block .val a{color:var(--blue-1)}
.footer-ops .ops-block .sub{font-size:12px;color:var(--muted);margin-top:4px}
.company-info{padding:28px 0;border-bottom:1px solid var(--line);display:grid;grid-template-columns:repeat(3,1fr);gap:14px 28px}
.company-info dt{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);font-weight:600}
.company-info dd{font-size:13px;color:var(--text);margin-top:3px;opacity:.85}
.footer-policies{padding:24px 0;display:flex;flex-wrap:wrap;gap:8px 22px}
.footer-policies a{font-size:12.5px;color:var(--text);opacity:.7;transition:.15s}
.footer-policies a:hover{opacity:1;color:var(--blue-1)}
.footer-bottom{padding:20px 0 0;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:12px;color:var(--dim)}
@media(max-width:900px){
  .footer-grid{grid-template-columns:1fr 1fr;gap:32px}
  .footer-ops{grid-template-columns:1fr}
  .company-info{grid-template-columns:1fr 1fr}
}
@media(max-width:520px){
  .footer-grid{grid-template-columns:1fr}
  .company-info{grid-template-columns:1fr}
}
/* COMMON */
.btn{display:inline-flex;align-items:center;gap:8px;padding:14px 24px;border-radius:999px;font-weight:700;font-size:14.5px;transition:.2s}
.btn-primary{background:var(--grad);color:#fff}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(91,155,255,.32)}
.btn-ghost{background:rgba(255,255,255,.05);color:var(--text);border:1px solid var(--line)}
.btn-ghost:hover{background:rgba(255,255,255,.08);border-color:rgba(123,176,255,.32)}
.kicker{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--blue-1);font-weight:700;margin-bottom:14px}
h1,h2,h3{font-weight:800;letter-spacing:-.03em;line-height:1.15}
h2{font-size:clamp(28px,4vw,46px);margin-bottom:18px}
h3{font-size:20px}
.lead{font-size:16px;color:var(--muted);line-height:1.78;max-width:660px;margin-top:14px}
/* NOTE CARD */
.note-card{display:flex;gap:24px;padding:26px 28px;border-radius:18px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid var(--line);transition:.3s;overflow:hidden;position:relative}
.note-card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--grad);opacity:0;transition:.3s}
.note-card:hover::before{opacity:1}
.note-card:hover{transform:translateY(-2px);box-shadow:0 18px 44px rgba(0,0,0,.32);border-color:rgba(123,176,255,.28)}
.note-num{font-family:"Cormorant Garamond",serif;font-size:46px;font-weight:300;font-style:italic;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;line-height:1;min-width:60px}
.note-content{flex:1}
.note-title{font-size:19px;font-weight:800;margin-bottom:10px}
.note-text{max-width:660px}
.note-text p{margin:0 0 10px;color:#c8ccda;font-size:14.5px;line-height:1.78}
.note-stack{display:grid;gap:14px}
/* PRICE CARD */
.price-card{padding:24px;border-radius:16px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid var(--line);position:relative;transition:.25s;overflow:hidden}
.price-card::before{content:"";position:absolute;left:0;right:0;top:0;height:1px;background:var(--grad);opacity:0;transition:.25s}
.price-card:hover::before{opacity:1}
.price-card:hover{transform:translateY(-3px);border-color:rgba(123,176,255,.3)}
.price-card h3{margin:8px 0 6px}
.price-card .kicker{margin-bottom:6px}
.price-card p{font-size:13.5px;color:var(--muted);margin-bottom:14px}
.time-rows{display:flex;flex-direction:column;gap:8px;padding-top:12px;border-top:1px solid var(--line)}
.time-rows>div{display:flex;justify-content:space-between;font-size:14px}
.time-rows>div :first-child{color:var(--muted)}
.time-rows>div :last-child{font-weight:700}
.price-card.best{border-color:rgba(123,176,255,.4)}
.price-card.best::before{opacity:1}
.best-badge{position:absolute;top:14px;right:14px;padding:4px 10px;background:var(--grad);color:#fff;font-size:10px;letter-spacing:.16em;font-weight:700;border-radius:6px}
/* DETAILS */
details{padding:18px 22px;border-radius:12px;background:var(--surface);border:1px solid var(--line);margin-bottom:10px;transition:.2s}
details[open]{background:linear-gradient(135deg,var(--surface),var(--surface-2));border-color:rgba(123,176,255,.2)}
summary{list-style:none;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-weight:700;font-size:15px;gap:16px}
summary::-webkit-details-marker{display:none}
summary span{font-size:22px;color:var(--blue-1);font-weight:300;transition:.25s}
details[open] summary span{transform:rotate(45deg)}
details>div{padding-top:14px;color:#c8ccda;font-size:14px;line-height:1.78}
/* JOB CARD */
.job-card{padding:22px 24px;border-radius:16px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid var(--line);transition:.25s;display:flex;flex-direction:column;gap:10px}
.job-card:hover{transform:translateY(-3px);border-color:rgba(123,176,255,.3);box-shadow:0 16px 36px rgba(0,0,0,.32)}
.job-card .top{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.job-card .badge{font-size:10px;letter-spacing:.16em;padding:3px 8px;border-radius:5px;font-weight:700;flex-shrink:0}
.job-card .badge.NEW{background:rgba(91,155,255,.18);color:var(--blue-1)}
.job-card .badge.FAST{background:rgba(214,178,116,.18);color:var(--gold)}
.job-card .badge.BEST{background:var(--grad);color:#fff}
.job-card h3{font-size:16.5px;line-height:1.4}
.job-card .meta{display:flex;gap:14px;font-size:12.5px;color:var(--muted);flex-wrap:wrap}
.job-card .pay{font-size:14.5px;font-weight:700;color:var(--blue-1);margin-top:4px}
.job-card .id{font-size:11px;color:var(--dim);letter-spacing:.08em}
/* REVEAL */
.reveal{opacity:0;transform:translateY(20px);transition:.7s ease-out}
.reveal.in{opacity:1;transform:none}
/* MEDIA QUERY */
@media(max-width:720px){
  .wrap{padding:80px 18px}
  .note-card{flex-direction:column;gap:10px;padding:22px 20px}
  .note-num{font-size:38px;min-width:auto}
}
@media(hover:none){
  .glass,.floating{backdrop-filter:none!important}
}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  .reveal{opacity:1!important;transform:none!important}
}
/* content-visibility — 뷰포트 밖 요소 렌더 스킵 (지원 브라우저만 적용) */
@supports(content-visibility:auto){
  .note-card,.job-card,.price-card,details{content-visibility:auto;contain-intrinsic-size:auto 320px}
  details{contain-intrinsic-size:auto 80px}
  .ad-card.ad-vvip{content-visibility:auto;contain-intrinsic-size:auto 380px}
  .ad-card.ad-vip{content-visibility:auto;contain-intrinsic-size:auto 280px}
  .ad-card.ad-premium{content-visibility:auto;contain-intrinsic-size:auto 200px}
  .shop-card{content-visibility:auto;contain-intrinsic-size:auto 480px}
  .site-footer{content-visibility:auto;contain-intrinsic-size:auto 800px}
}
/* 내부 링크 섹션 (블로그 글 하단) */
.link-section{padding:30px 36px;border-radius:18px;background:linear-gradient(135deg,var(--surface),var(--surface-2));border:1px solid var(--line)}
.link-section .link-h2{font-size:20px;font-weight:800;letter-spacing:-.02em;margin-bottom:8px;line-height:1.4}
.link-section .link-intro{color:var(--muted);font-size:13.5px;margin-bottom:20px;line-height:1.7;max-width:680px}
.link-section .link-list{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:10px}
.link-section .link-list a{display:flex;align-items:center;gap:10px;color:#c8ccda;font-size:14px;font-weight:600;padding:14px 18px;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:10px;transition:.18s}
.link-section .link-list a::before{content:"→";color:var(--blue-1);font-weight:700;transition:transform .18s}
.link-section .link-list a:hover{color:var(--text);background:rgba(123,176,255,.08);border-color:rgba(123,176,255,.32)}
.link-section .link-list a:hover::before{transform:translateX(3px)}
@media(max-width:640px){.link-section{padding:24px 22px}.link-section .link-list{grid-template-columns:1fr}}
"""

# ─────────────────────────────────────────────
# 헤드 메타 빌더
# ─────────────────────────────────────────────
def head(title, description, path, og_image=None, extra_jsonld=None, schema_type="WebPage"):
    """공통 <head> 빌더 (canonical, og, json-ld 포함)"""
    canonical = f"{COMPANY['base_url']}{path}"
    og = og_image or f"{COMPANY['base_url']}/assets/og-cover.svg"
    parts = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">',
        '<meta name="theme-color" content="#0a0e1a">',
        '<meta name="format-detection" content="telephone=no">',
        '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">',
        '<meta name="googlebot" content="index,follow">',
        '<meta name="referrer" content="strict-origin-when-cross-origin">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{description}">',
        f'<meta name="author" content="{COMPANY["brand_kr"]} 편집팀">',
        f'<link rel="canonical" href="{canonical}">',
        f'<link rel="alternate" hreflang="ko-KR" href="{canonical}">',
        f'<link rel="alternate" hreflang="x-default" href="{canonical}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{COMPANY["brand_kr"]}">',
        '<meta property="og:locale" content="ko_KR">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{description}">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:image" content="{og}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{description}">',
        f'<meta name="twitter:image" content="{og}">',
        '<link rel="icon" type="image/svg+xml" href="/favicon.svg">',
        '<link rel="manifest" href="/site.webmanifest">',
        f'<style>{CSS_BASE}</style>',
    ]

    # JSON-LD 기본 (Organization + WebSite)
    org_ld = {
        "@context":"https://schema.org",
        "@graph":[
            {
                "@type":"Organization",
                "@id":f"{COMPANY['base_url']}/#organization",
                "name":COMPANY["brand_kr"],
                "alternateName":COMPANY["brand_en"],
                "legalName":COMPANY["legal_name"],
                "url":COMPANY["base_url"],
                "logo":f"{COMPANY['base_url']}/assets/og-cover.svg",
                "description":COMPANY["tagline_long"],
                "email":COMPANY["email"],
                "telephone":COMPANY["tel_intl"],
                "address":{
                    "@type":"PostalAddress",
                    "streetAddress":"청석로 268",
                    "addressLocality":"파주시",
                    "addressRegion":"경기도",
                    "postalCode":"10881",
                    "addressCountry":"KR"
                },
                "founder":{"@type":"Person","name":COMPANY["ceo"]},
                "taxID":COMPANY["biz_reg"],
                "areaServed":{"@type":"Country","name":"대한민국"}
            },
            {
                "@type":"WebSite",
                "@id":f"{COMPANY['base_url']}/#website",
                "url":COMPANY["base_url"],
                "name":COMPANY["brand_kr"],
                "publisher":{"@id":f"{COMPANY['base_url']}/#organization"},
                "inLanguage":"ko-KR",
                "potentialAction":{
                    "@type":"SearchAction",
                    "target":{"@type":"EntryPoint","urlTemplate":f"{COMPANY['base_url']}/search?q={{q}}"},
                    "query-input":"required name=q"
                }
            }
        ]
    }
    if extra_jsonld:
        if isinstance(extra_jsonld, list):
            org_ld["@graph"].extend(extra_jsonld)
        else:
            org_ld["@graph"].append(extra_jsonld)
    parts.append(f'<script type="application/ld+json">{json.dumps(org_ld,ensure_ascii=False,separators=(",", ":"))}</script>')
    return "\n".join(parts)

# ─────────────────────────────────────────────
# 헤더
# ─────────────────────────────────────────────
def header_html():
    svc_links = "".join(f'<li><a href="/jobs/{s["slug"]}/">{s["kr"]} 구인</a></li>' for s in SERVICES)
    seeker_links = "".join(f'<li><a href="/seekers/{s["slug"]}/">{s["kr"]} 구직</a></li>' for s in SERVICES)
    region_links = "".join(f'<li><a href="/locations/{r["slug"]}/">{r["kr"]} ({r["districts_count"]}개 구·시)</a></li>' for r in REGIONS)
    nat_links = "".join(f'<li><a href="/therapists/{n["slug"]}/">{n["kr"]}</a></li>' for n in NATIONALITIES)
    return f"""<header>
<nav class="nav" aria-label="주 메뉴">
  <a class="brand" href="/" aria-label="테라피잡 홈">
    <span class="logo-mark">T</span>
    <span class="brand-name">{COMPANY["brand_kr"]}<small>{COMPANY["brand_en"]}</small></span>
  </a>
  <button class="toggle" aria-expanded="false" aria-controls="primary-menu" onclick="document.getElementById('primary-menu').classList.toggle('open')">☰</button>
  <ul id="primary-menu" class="menu">
    <li><a href="/jobs/" aria-haspopup="true">구인공고</a><ul class="submenu">{svc_links}<li><a href="/jobs/">전체 보기</a></li></ul></li>
    <li><a href="/seekers/" aria-haspopup="true">구직</a><ul class="submenu">{seeker_links}<li><a href="/seekers/">전체 보기</a></li></ul></li>
    <li><a href="/locations/" aria-haspopup="true">지역</a><ul class="submenu">{region_links}</ul></li>
    <li><a href="/therapists/" aria-haspopup="true">관리사</a><ul class="submenu">{nat_links}</ul></li>
    <li><a href="/pricing/">급여</a></li>
    <li><a href="/magazine/">매거진</a></li>
    <li><a href="/notices/">공지사항</a></li>
    <li><a href="/reviews/">사례</a></li>
    <li><a href="/pricing-ads/">광고 상품</a></li>
    <li><a href="/shop-sale/">업소매매</a></li>
    <li><a class="cta-gold" href="/contact-ads/">광고문의</a></li>
  </ul>
</nav>
</header>"""

# ─────────────────────────────────────────────
# 푸터
# ─────────────────────────────────────────────
def footer_html():
    svc_links = "".join(f'<li><a href="/jobs/{s["slug"]}/">{s["kr"]} 구인</a></li>' for s in SERVICES)
    region_links = "".join(f'<li><a href="/locations/{r["slug"]}/">{r["kr"]}</a></li>' for r in REGIONS)
    return f"""<footer class="site-footer">
<div class="footer-wrap">
  <div class="footer-grid">
    <div class="footer-brand">
      <div class="brand">
        <span class="logo-mark">T</span>
        <span class="brand-name">{COMPANY["brand_kr"]}<small>{COMPANY["brand_en"]}</small></span>
      </div>
      <p>{COMPANY["tagline_long"]} 전국 마사지 구인구직 정보를 가장 정확하고 빠르게 정리합니다.</p>
    </div>
    <div>
      <h4>업종별 구인</h4>
      <ul>{svc_links}</ul>
    </div>
    <div>
      <h4>지역</h4>
      <ul>{region_links}<li><a href="/locations/">전국 행정구</a></li></ul>
    </div>
    <div>
      <h4>안내</h4>
      <ul>
        <li><a href="/about/">테라피잡 소개</a></li>
        <li><a href="/notices/">공지사항</a></li>
        <li><a href="/pricing-ads/">광고 상품 안내</a></li>
        <li><a href="/shop-sale/">업소 매매</a></li>
        <li><a href="/pricing/">급여 시세표</a></li>
        <li><a href="/magazine/">매거진</a></li>
        <li><a href="/reviews/">매칭 사례</a></li>
        <li><a href="/contact/">고객센터</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-ops">
    <div class="ops-block">
      <div class="label">고객센터</div>
      <div class="val"><a href="tel:{COMPANY['tel']}">{COMPANY['tel']}</a></div>
      <div class="sub">{COMPANY['tel_hours']}</div>
    </div>
    <div class="ops-block">
      <div class="label">이메일</div>
      <div class="val"><a href="mailto:{COMPANY['email']}">{COMPANY['email']}</a></div>
      <div class="sub">24시간 접수 · 평일 회신</div>
    </div>
    <div class="ops-block">
      <div class="label">운영</div>
      <div class="val">전국 82개 행정구</div>
      <div class="sub">서울·경기·인천·부산 풀커버리지</div>
    </div>
  </div>
  <dl class="company-info">
    <div><dt>상호</dt><dd>{COMPANY['legal_name']} ({COMPANY['brand_kr']})</dd></div>
    <div><dt>대표자</dt><dd>{COMPANY['ceo']}</dd></div>
    <div><dt>사업자등록번호</dt><dd>{COMPANY['biz_reg']}</dd></div>
    <div><dt>직업정보제공사업 신고번호</dt><dd>{COMPANY['job_info_reg']}</dd></div>
    <div><dt>사업장 주소</dt><dd>{COMPANY['address']}</dd></div>
    <div><dt>개인정보보호책임자</dt><dd>{COMPANY['privacy_officer']}</dd></div>
  </dl>
  <div class="footer-policies">
    <a href="/policy/privacy/">개인정보처리방침</a>
    <a href="/policy/terms/">이용약관</a>
    <a href="/policy/youth/">청소년 보호정책</a>
    <a href="/sitemap.xml">사이트맵</a>
    <a href="/contact/">고객센터</a>
  </div>
  <div class="footer-bottom">
    <span>© 2026 {COMPANY['legal_name']}. All rights reserved.</span>
    <span>본 사이트는 직업정보제공사업 신고를 마친 합법 플랫폼이며, 노동관계법령을 준수합니다.</span>
  </div>
</div>
</footer>"""

# ─────────────────────────────────────────────
# 페이지 셸 (전체 HTML 골격)
# ─────────────────────────────────────────────
PAGE_JS = """
<script>
function idle(fn){if('requestIdleCallback'in window){requestIdleCallback(fn,{timeout:1500});}else{setTimeout(fn,1);}}
idle(function(){
  if('IntersectionObserver'in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'80px'});
    document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
  } else { document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');}); }
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.getElementById('primary-menu')?.classList.remove('open');}});
});
</script>
"""

def global_banner(path):
    """모든 페이지 하단 배너 — 클릭 시 고객센터 전화 연결. /contact-ads/ 페이지는 자체 폼이 있어 제외."""
    if path.startswith("/contact-ads"):
        return ""
    return f"""
<section style="max-width:1240px;margin:60px auto 0;padding:0 24px">
  <a href="tel:{COMPANY['tel']}" aria-label="고객센터 {COMPANY['tel']} 전화 — 매수·매매·광고 문의" style="display:block;border-radius:20px;overflow:hidden;border:1px solid rgba(123,176,255,.22);transition:transform .25s,box-shadow .25s,border-color .25s">
    <picture>
      <source type="image/webp" srcset="/assets/ads/shop-banner.webp 1x, /assets/ads/shop-banner@2x.webp 2x">
      <img src="/assets/ads/shop-banner.jpg" alt="마사지 구인구직 — therapyjob.club · 지금 확인하기" width="1200" height="400" loading="lazy" decoding="async" style="width:100%;height:auto;display:block">
    </picture>
  </a>
  <style>section > a[aria-label^="고객센터"]:hover{{transform:translateY(-3px);box-shadow:0 20px 48px rgba(91,155,255,.20);border-color:rgba(123,176,255,.5)}}</style>
</section>
"""


def page(title, description, path, body, og_image=None, extra_jsonld=None):
    return f"""<!doctype html>
<html lang="ko">
<head>
{head(title, description, path, og_image, extra_jsonld)}
</head>
<body>
{header_html()}
<main>
{body}
</main>
{global_banner(path)}
{footer_html()}
{PAGE_JS}
</body>
</html>"""

# ─────────────────────────────────────────────
# Breadcrumb JSON-LD 헬퍼
# ─────────────────────────────────────────────
def breadcrumb_ld(items):
    """items = [(name, path), ...]"""
    return {
        "@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":i+1,"name":n,"item":f"{COMPANY['base_url']}{p}"}
            for i,(n,p) in enumerate(items)
        ]
    }

def faq_ld(qa_list):
    """qa_list = [(question, answer), ...]"""
    return {
        "@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
            for q,a in qa_list
        ]
    }


def internal_link_section(h2_title, intro, links):
    """블로그 글 하단 내부 링크 섹션 — 2~4개의 핵심 추천 자료.

    links: [(text, url), ...]
    """
    items = "".join(f'<li><a href="{url}">{text}</a></li>' for text, url in links)
    return f"""
<section class="wrap">
  <div class="link-section">
    <h2 class="link-h2">{h2_title}</h2>
    <p class="link-intro">{intro}</p>
    <ul class="link-list">{items}</ul>
  </div>
</section>"""
