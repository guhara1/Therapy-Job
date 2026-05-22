"""테라피잡 사이트 일괄 생성 — 모든 페이지·sitemap·robots·manifest"""
import os, sys, re, json
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from data import COMPANY, SERVICES, NATIONALITIES, REGIONS, MAGAZINE, DISTRICTS, SAMPLE_JOBS
from pages_core import build_index, build_about, build_contact, build_pricing, build_reviews, build_policy_privacy, build_policy_terms, build_policy_youth, build_pricing_ads
from pages_hubs import build_jobs_hub, build_job_service, build_seekers_hub, build_seeker_service, build_therapists_hub, build_therapist, build_magazine_hub, build_magazine_article
from pages_locations import build_locations_hub, build_region_hub, build_district
from ads import build_ad_detail

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# ─────────────────────────────────────────────
# 미니파이 (옵션 — 사이즈 축소)
# ─────────────────────────────────────────────
def minify_html(html):
    # JSON-LD 한 줄
    def jsonld(m):
        try:
            return f'<script type="application/ld+json">{json.dumps(json.loads(m.group(1)),ensure_ascii=False,separators=(",", ":"))}</script>'
        except: return m.group(0)
    html = re.sub(r'<script type="application/ld\+json">(.*?)</script>', jsonld, html, flags=re.S)
    # CSS 미니파이
    def css(m):
        c = m.group(1)
        c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
        c = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', c)
        c = re.sub(r'\s+', ' ', c)
        c = re.sub(r';}', '}', c)
        return f'<style>{c.strip()}</style>'
    html = re.sub(r'<style>(.*?)</style>', css, html, flags=re.S)
    # 태그 간 공백
    html = re.sub(r'>\s+<', '><', html)
    html = re.sub(r' {2,}', ' ', html)
    return html.strip()

def write_page(path, html, minify=True):
    out_dir = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(out_dir, exist_ok=True)
    fp = os.path.join(out_dir, "index.html")
    final = minify_html(html) if minify else html
    with open(fp, "w", encoding="utf-8") as f:
        f.write(final)
    return fp

def write_root(name, content):
    fp = os.path.join(ROOT, name)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    return fp

# ─────────────────────────────────────────────
# sitemap.xml
# ─────────────────────────────────────────────
def build_sitemap():
    today = "2026-05-22"
    urls = []
    def add(loc, lastmod=today, changefreq="weekly", priority="0.7"):
        urls.append((loc, lastmod, changefreq, priority))

    add("/", priority="1.0", changefreq="daily")
    add("/jobs/", priority="0.95", changefreq="daily")
    add("/seekers/", priority="0.9", changefreq="weekly")
    add("/therapists/", priority="0.85", changefreq="weekly")
    add("/locations/", priority="0.95", changefreq="weekly")
    add("/magazine/", priority="0.85", changefreq="weekly")
    add("/pricing/", priority="0.85", changefreq="weekly")
    add("/pricing-ads/", priority="0.9", changefreq="monthly")
    add("/reviews/", priority="0.8", changefreq="weekly")
    add("/about/", priority="0.75", changefreq="monthly")
    add("/contact/", priority="0.75", changefreq="monthly")

    for s in SERVICES:
        add(f"/jobs/{s['slug']}/", priority="0.9", changefreq="daily")
        add(f"/seekers/{s['slug']}/", priority="0.8")

    for n in NATIONALITIES:
        add(f"/therapists/{n['slug']}/", priority="0.75")

    for r in REGIONS:
        add(f"/locations/{r['slug']}/", priority="0.9", changefreq="weekly")
        for slug, _ in DISTRICTS[r["slug"]]:
            add(f"/locations/{r['slug']}/{slug}/", priority="0.8", changefreq="weekly")

    for m in MAGAZINE:
        add(f"/magazine/{m['slug']}/", priority="0.75", changefreq="monthly")

    # 광고 상세 (JobPosting — Google Jobs 노출 우선)
    for j in SAMPLE_JOBS:
        pri = "0.95" if j.get("tier")=="vvip" else "0.85" if j.get("tier")=="vip" else "0.7"
        add(f"/ad/{j['id']}/", priority=pri, changefreq="weekly")

    add("/policy/privacy/", priority="0.3", changefreq="yearly")
    add("/policy/terms/", priority="0.3", changefreq="yearly")
    add("/policy/youth/", priority="0.3", changefreq="yearly")

    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lm, cf, pr in urls:
        xml.append(f'  <url><loc>{COMPANY["base_url"]}{loc}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>')
    xml.append('</urlset>')
    return "\n".join(xml)

# ─────────────────────────────────────────────
# robots.txt
# ─────────────────────────────────────────────
def build_robots():
    return f"""User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/

User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: NaverBot
Allow: /

User-agent: Yeti
Allow: /

User-agent: Daum
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

Sitemap: {COMPANY['base_url']}/sitemap.xml
Host: {COMPANY['domain']}
"""

# ─────────────────────────────────────────────
# site.webmanifest
# ─────────────────────────────────────────────
def build_manifest():
    return json.dumps({
        "name": f"{COMPANY['brand_kr']} — 전국 마사지 구인구직",
        "short_name": COMPANY["brand_kr"],
        "description": COMPANY["tagline_long"],
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#0a0e1a",
        "theme_color": "#2c54a8",
        "lang": "ko-KR",
        "orientation": "portrait",
        "icons": [
            {"src":"/favicon.svg","sizes":"any","type":"image/svg+xml","purpose":"any"},
            {"src":"/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},
            {"src":"/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"}
        ]
    }, ensure_ascii=False, separators=(",", ":"))

# ─────────────────────────────────────────────
# favicon.svg (인라인 SVG 로고)
# ─────────────────────────────────────────────
def build_favicon_svg():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#7bb0ff"/>
<stop offset="50%" stop-color="#5b9bff"/>
<stop offset="100%" stop-color="#2c54a8"/>
</linearGradient>
</defs>
<rect width="64" height="64" rx="14" fill="url(#g)"/>
<text x="32" y="44" text-anchor="middle" font-family="Georgia,serif" font-size="38" font-weight="700" font-style="italic" fill="#fff">T</text>
</svg>"""

# ─────────────────────────────────────────────
# OG cover SVG (1200×630)
# ─────────────────────────────────────────────
def build_og_cover():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#0a0e1a"/>
<stop offset="100%" stop-color="#1b3a78"/>
</linearGradient>
<linearGradient id="grad" x1="0" y1="0" x2="1" y2="1">
<stop offset="0%" stop-color="#7bb0ff"/>
<stop offset="50%" stop-color="#5b9bff"/>
<stop offset="100%" stop-color="#2c54a8"/>
</linearGradient>
</defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<circle cx="980" cy="120" r="280" fill="url(#grad)" opacity=".18"/>
<circle cx="160" cy="500" r="180" fill="url(#grad)" opacity=".14"/>
<g transform="translate(80,180)">
<rect width="100" height="100" rx="24" fill="url(#grad)"/>
<text x="50" y="72" text-anchor="middle" font-family="Georgia,serif" font-size="62" font-weight="700" font-style="italic" fill="#fff">T</text>
</g>
<text x="80" y="370" font-family="-apple-system,Pretendard,Apple SD Gothic Neo,sans-serif" font-size="64" font-weight="800" fill="#eef2fb" letter-spacing="-2">테라피잡</text>
<text x="80" y="430" font-family="-apple-system,Pretendard,Apple SD Gothic Neo,sans-serif" font-size="34" font-weight="500" fill="#a0a8be" letter-spacing="-1">전국 마사지 구인구직 1번지</text>
<text x="80" y="490" font-family="-apple-system,Pretendard,Apple SD Gothic Neo,sans-serif" font-size="22" font-weight="400" fill="#7bb0ff" letter-spacing="-.5">therapyjob.co.kr · 82개 행정구 풀커버</text>
<line x1="80" y1="540" x2="1120" y2="540" stroke="#7bb0ff" stroke-opacity=".24" stroke-width="1"/>
<text x="80" y="580" font-family="-apple-system,Pretendard,Apple SD Gothic Neo,sans-serif" font-size="18" font-weight="600" fill="#a0a8be" letter-spacing="2">SWEDISH · AROMA · THAI · LOMI LOMI · SPORTS</text>
</svg>"""

# ─────────────────────────────────────────────
# 메인 빌드
# ─────────────────────────────────────────────
def main():
    minify = True
    count = 0

    print("→ 정적 자산")
    write_root("robots.txt", build_robots()); count += 1
    write_root("sitemap.xml", build_sitemap()); count += 1
    write_root("site.webmanifest", build_manifest()); count += 1
    write_root("favicon.svg", build_favicon_svg()); count += 1

    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    with open(os.path.join(ROOT, "assets", "og-cover.svg"), "w", encoding="utf-8") as f:
        f.write(build_og_cover())
    count += 1

    print("→ 메인 + 핵심 페이지")
    write_page("/", build_index(), minify); count += 1
    write_page("/about/", build_about(), minify); count += 1
    write_page("/contact/", build_contact(), minify); count += 1
    write_page("/pricing/", build_pricing(), minify); count += 1
    write_page("/pricing-ads/", build_pricing_ads(), minify); count += 1
    write_page("/reviews/", build_reviews(), minify); count += 1
    write_page("/policy/privacy/", build_policy_privacy(), minify); count += 1
    write_page("/policy/terms/", build_policy_terms(), minify); count += 1
    write_page("/policy/youth/", build_policy_youth(), minify); count += 1

    print("→ 구인공고 (1 + 5)")
    write_page("/jobs/", build_jobs_hub(), minify); count += 1
    for s in SERVICES:
        write_page(f"/jobs/{s['slug']}/", build_job_service(s), minify); count += 1

    print("→ 구직 가이드 (1 + 5)")
    write_page("/seekers/", build_seekers_hub(), minify); count += 1
    for s in SERVICES:
        write_page(f"/seekers/{s['slug']}/", build_seeker_service(s), minify); count += 1

    print("→ 관리사 (1 + 6)")
    write_page("/therapists/", build_therapists_hub(), minify); count += 1
    for n in NATIONALITIES:
        write_page(f"/therapists/{n['slug']}/", build_therapist(n), minify); count += 1

    print("→ 매거진 (1 + 7)")
    write_page("/magazine/", build_magazine_hub(), minify); count += 1
    for m in MAGAZINE:
        write_page(f"/magazine/{m['slug']}/", build_magazine_article(m), minify); count += 1

    print("→ 지역 (1 + 4 + 82)")
    write_page("/locations/", build_locations_hub(), minify); count += 1
    for r in REGIONS:
        write_page(f"/locations/{r['slug']}/", build_region_hub(r), minify); count += 1
        for slug, kr in DISTRICTS[r["slug"]]:
            write_page(f"/locations/{r['slug']}/{slug}/", build_district(r, slug, kr), minify); count += 1

    print(f"→ 광고 상세 ({len(SAMPLE_JOBS)})")
    for j in SAMPLE_JOBS:
        write_page(f"/ad/{j['id']}/", build_ad_detail(j), minify); count += 1

    print(f"\n✓ 총 {count}개 파일 생성 완료")

if __name__ == "__main__":
    main()
