# 테라피잡(therapyjob.club) — 완성본 제작 청사진

> 전국 마사지 구인구직·로드샵 채용·업소매매 플랫폼. 이 문서 하나로 동일한 사이트를 다른 도메인/업종에 그대로 재현할 수 있도록 모든 구성을 정리한다.

---

## 0. 한눈에 보는 사이트 개요

| 항목 | 값 |
|---|---|
| 총 페이지 | **166개 HTML** |
| 광역시도 | 서울(25) · 경기(31) · 인천(10) · 부산(16) = **82 행정구** |
| 업종 | 5종 (스웨디시·아로마·타이·로미로미·스포츠) |
| 매니저 국적 | 6종 (한국·중국·태국·베트남·러시아·일본) |
| 매거진 | 7편 / 공지사항 4편 |
| 광고 상세 | 22건 (VVIP 4·VIP 6·프리미엄 12) |
| 업소매매 매물 | 12건 (+ 매물 상세 12페이지) |
| 정책 | 3편 (개인정보·약관·청소년보호) |
| 기술 스택 | **순수 HTML + 인라인 CSS/JS + Python 생성기**, 의존성 0 (빌드용 Pillow만) |
| 백엔드 | Cloudflare Pages Functions (광고문의 폼 → Telegram 봇) |
| 외부 자원 요청 | 0개 (폰트·아이콘·이미지 인라인 SVG, 배너만 WebP) |

**핵심 철학**: 빌드 도구·프레임워크 없음. Python으로 데이터→HTML 일괄 생성. 단일 HTML = 단일 요청 = 최소 LCP. `content-visibility`로 렌더 스킵.

---

## 1. 기술 스택 & 파일 구조

### 1.1 생성 스크립트 (`scripts/`)
```
data.py             (70KB)  — 모든 데이터 단일 소스 (회사·업종·국적·지역·매거진·공지·광고·매물·가격)
district_profiles.py (61KB) — 82개 행정구 고유 프로필 (랜드마크·교통·고객층·시장·전략·강세업종)
templates.py        (32KB)  — 공통: CSS_BASE, head(), header_html(), footer_html(), page(), 헬퍼
ads.py              (27KB)  — 광고 시스템: 등급별 카드 렌더·필터·상세페이지·promo bar
pages_core.py      (226KB)  — 메인·About·Contact·Pricing·Reviews·정책·광고상품·업소매매·공지
pages_hubs.py       (53KB)  — 구인허브·업종채용·구직허브·업종구직·관리사·매거진
pages_locations.py  (52KB)  — 지역허브·광역4·행정구82
build.py            (17KB)  — 통합 빌더 + sitemap/sitemap1/rss/robots/manifest/favicon/og
```

### 1.2 빌드 방법
```bash
python3 scripts/build.py   # 루트에 166 HTML + 정적파일 일괄 생성·미니파이
```
- 데이터만 바꾸면 전 페이지 자동 재생성
- `minify_html()`: JSON-LD 1줄화 + CSS 압축 + 태그간 공백 제거

### 1.3 출력 디렉토리 구조
```
/index.html
/jobs/{swedish,aroma,thai,lomilomi,sports}/
/seekers/{동일 5종}/
/locations/{seoul,gyeonggi,incheon,busan}/{행정구}/
/therapists/{korean,chinese,thai,vietnamese,russian,japanese}/
/magazine/{slug}/  · /notices/{slug}/
/ad/{공고ID}/  · /shop-sale/  · /shop-sale/{매물ID}/
/recruitment-pricing/ · /shop-sale-pricing/ · /pricing-ads/ · /contact-ads/
/pricing/ · /reviews/ · /about/ · /contact/
/policy/{privacy,terms,youth}/
/functions/api/contact-ads.js  (Cloudflare Pages Function)
robots.txt · sitemap.xml · sitemap1.xml · rss.xml · site.webmanifest · favicon.svg · assets/
```

---

## 2. 디자인 시스템

### 2.1 컬러 토큰 (쿨 블루 — 신뢰감)
```css
:root{
  --bg:#0a0e1a;          /* 페이지 배경 (다크) */
  --surface:#121828;     /* 카드 */
  --surface-2:#1a2236;   /* 카드 그라데이션 끝 */
  --line:rgba(255,255,255,.08);
  --text:#eef2fb; --muted:#a0a8be; --dim:#6c7490;
  --blue-1:#7bb0ff; --blue-2:#5b9bff; --blue-3:#2c54a8; --blue-deep:#1b3a78;
  --grad:linear-gradient(135deg,#7bb0ff 0%,#5b9bff 45%,#2c54a8 100%);
  --grad-soft:linear-gradient(135deg,rgba(123,176,255,.14),rgba(44,84,168,.06));
  --gold:#d6b274;        /* VVIP·강조용 골드 */
}
```
> 업종 전환 시 `--blue-*`/`--grad`만 교체하면 톤 전체 변경. (의료·IT=쿨블루 / 친환경=세이지그린 / 럭셔리=골드)

광고 등급 색: **VVIP 골드(#d4af37→#f4d29c)** · **VIP 블루(--grad)** · **프리미엄 그레이(#a0a8be→#6c7490)**

### 2.2 폰트 (시스템 폰트 우선 — 다운로드 0)
```css
body{font-family:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  line-height:1.65;letter-spacing:-.01em}
.serif{font-family:"Cormorant Garamond","Noto Serif KR",Georgia,serif;font-weight:300;font-style:italic}
```
- 본문 한글 가독: line-height 1.65~1.78, letter-spacing -.01em
- `.serif`(이탤릭 세리프)는 숫자/제목 강조용 (히어로 "한 줄.", 랭킹 넘버)

### 2.3 타이포 스케일
| 용도 | 크기 |
|---|---|
| h1 히어로 | `clamp(36px,5.5vw,60px)` ~ `clamp(40px,6.5vw,76px)`, 800, letter-spacing -.038em |
| h2 섹션 | `clamp(28px,4vw,46px)`, letter-spacing -.03em |
| h3 카드 | 16~22px, 800 |
| 본문 | 13.5~15px, line-height 1.7~1.85 |
| 라벨/kicker | 11~12px, letter-spacing .18~.22em, uppercase |

### 2.4 레이아웃
```css
.wrap{max-width:1240px;margin:0 auto;padding:120px 24px}  /* 모바일 80px 18px */
.note-text{max-width:660px}   /* 한글 가독 폭 */
```

---

## 3. 공통 컴포넌트

### 3.1 헤더 (스티키 + 모바일 햄버거)
```
[로고 T그라데이션 + 테라피잡] ... [구인공고▼ 구직▼ 지역▼ 관리사▼ 급여 매거진 공지사항 사례 광고상품▼ 업소매매] [광고문의 골드버튼]
```
- 드롭다운 5개: 구인공고(업종5+전체보기), 구직(업종5+전체보기), 지역(광역4), 관리사(국적6), 광고상품(채용공고/업소매매)
- **광고문의** = 골드 pill (`.cta-gold`)
- **모바일(≤1100px)**: 44×44 햄버거 버튼(배경·테두리), 슬라이드 패널, 링크 클릭 시 자동 닫힘
- 링크 텍스트는 설명형 ("구인공고 전체 보기" — Lighthouse 권고)

### 3.2 헤더 직하 promo bar (전 페이지, /shop-sale/ 제외)
```
[업소매매] 마사지샵 양도 매물 등록 · 1개월 10만원 · 익명 게재 · 매수자 1:1 매칭  [지금 등록 →]
```
다크 골드 그라데이션 바, 클릭 → /shop-sale/

### 3.3 노트 카드 (.note-card) — 본문 핵심 블록
```html
<div class="note-card"><div class="note-num">01</div><div class="note-content">
  <h3 class="note-title">제목</h3><div class="note-text"><p>문장</p></div>
</div></div>
```
- 좌측 그라데이션 바 hover fade-in, translateY(-2px), 번호는 Cormorant 이탤릭

### 3.4 광고 카드 3등급 (.ad-card)
- **VVIP**: 골드 대형, 상단 골드라인, 큰 랭킹넘버, 회사명·혜택·일급 풀노출
- **VIP**: 블루 중형, First Content Break
- **프리미엄**: 그레이 컴팩트, 하단
- 그리드 클래스 `.ad-grid-{tier}`, **모바일 2열**(@720px)

### 3.5 기타
- 가격카드(.price-card): 상단 1px 그라데이션, hover translateY(-3px)
- FAQ: 네이티브 `<details>` + JSON-LD FaqPage 1:1
- reveal(.reveal): IntersectionObserver fade-in (threshold .12, rootMargin 80px)
- 푸터 5단: 4컬럼링크 / 고객센터·이메일·운영 / 회사정보 6필드 / 정책링크 / 카피라이트

---

## 4. 페이지별 구성 + 타이틀/디스크립션 패턴

> 모든 title·description은 페이지마다 100% 고유. head()가 canonical·og·twitter·hreflang·JSON-LD 자동 생성.

### 4.1 메인 (`/`)
- **title**: `테라피잡 | 마사지 구인구직·알바 채용정보` (23자, ≤40)
- **desc**: `전국 82개 행정구 마사지 관리사 구인구직. 채용 공고 5,820여건 매일 갱신·평균 47시간 매칭. 직업정보제공사업 신고 합법 플랫폼.` (76자, ≤80)
- **네이버 권고**: title ≤40자, desc ≤80자 필수
- 메인에만 `naver-site-verification`·`google-site-verification` 메타
- **구성**: 히어로(글래스 예약카드+플로팅칩) → 마키띠 → **VVIP광고** → 업종별 채용현황 → **VIP광고** → 지역별 채용현황 → HOW IT WORKS 4단계 → **프리미엄광고** → 운영팀(WHO·HOW·WHY) → FAQ 6 → CTA
- **광고 hybrid 배치**: 등급 사이에 콘텐츠 분산 (구글 intrusive-ads 회피)

### 4.2 광역 지역 (`/locations/{region}/`) ×4
- **title**: `{지역} 마사지 구인구직 — {N}개 행정구 채용 정보 | 테라피잡`
- **구성**: 히어로(통계: 행정구수·공고수·운영샵) → **VVIP광고** → 행정구 카드그리드(.dist-grid, 모바일2열) → **VIP광고** → 지역별 SEO 콘텐츠 5섹션(권역별단가·알바3패턴·트렌드·신규가이드·FAQ) → **프리미엄광고**
- 각 광역 SEO 콘텐츠 100% 고유 (서울=강남vs강북 단가지수, 경기=1기vs2기신도시, 인천=송도외국인, 부산=해운대vs서면)
- **JSON-LD**: Organization+WebSite+BreadcrumbList+Place+CollectionPage+Article+FAQPage

### 4.3 행정구 (`/locations/{region}/{district}/`) ×82 ★도어웨이 회피 핵심
- **title**: `{지역} {구} 마사지 구인구직 — {랜드마크} 권역 채용·일급 시세 | 테라피잡`
- **desc**: `{지역} {구} 로드샵 마사지 관리사 채용. {시장특성 90자} 동별 샵 분포·일급 시세·매칭 사례 수록.`
- **고유화 방식**: `district_profiles.py`에 구별 실데이터 — `land`(랜드마크), `metro`(지하철), `customer`(고객층), `market`(시장특성 2~3문장), `strategy`(정착전략), `svc`(강세업종), `v`(0~3 프로즈변형)
- **구성**: 히어로(운영샵수·고객층·강세업종) → VVIP → 권역한눈에(동별로드샵분포·상권교통·고객층수요·추천업종) → VIP → 필드노트(시장요약·정착전략·안전포인트·데이터출처) → 프리미엄 → 업종별시세(강세업종순) → FAQ6(고객층·업종·교통·야간비중·로드샵·신규입직) → 매칭후기6(랜드마크·고객층 반영) → CTA
- **v변형**: 섹션 제목·구조를 4종으로 분기해 구조 차별화
- **JSON-LD**: AdministrativeArea+LocalBusiness(aggregateRating)+FAQPage+ItemList(Review6)+BreadcrumbList
- **결과**: 95%→편집콘텐츠 70% 유사도 (핵심 콘텐츠 고유)

### 4.4 업종 채용 (`/jobs/{slug}/`) ×5
- **title**: `{업종} 마사지 관리사 구인공고 — {N}건 모집 중 | 테라피잡`
- **구성**: 히어로(평균일급·월환산·공고수) → VVIP → 업종특성4(시장개요·역량·근무패턴·교통식대) → VIP → 기타공고샘플 → 프리미엄 → FAQ5 → CTA
- **JSON-LD**: Service+JobPosting(baseSalary·hiringOrg·jobLocation)+FAQPage+BreadcrumbList

### 4.5 업종 구직 (`/seekers/{slug}/`) ×5
- **title**: `{업종} 마사지 구직 가이드 — 적성·체력·수입·면접 완벽 정리 | 테라피잡`
- **고유화**: `SEEKER_DETAIL` — 업종별 적성/체력/수입/주의점/커리어/면접질문3 (전부 다름)
- **구성**: 히어로 → 적성·체력·수입·단점·커리어 5카드 → 업종 고유 면접FAQ → CTA
- **JSON-LD**: Article+FAQPage

### 4.6 관리사 국적 (`/therapists/{slug}/`) ×6
- **title**: `{국적} 마사지 관리사 채용 — 선호 업종·평균 단가·체류 조건 | 테라피잡`
- **고유화**: `THERAPIST_DETAIL` — 국적별 비자/선호업종/시장트렌드/단가전략
- **구성**: 히어로(평균단가·수요) → 강점·선호업종·체류자격·단가전략 4카드 → CTA

### 4.7 매거진 (`/magazine/{slug}/`) ×7
- **title**: `{글제목} | 테라피잡 매거진`
- 글 목록: salary-guide-2026, interview-tips, contract-checklist, newbie-roadmap, shop-vs-freelance, safe-workplace, newcomer-shop-guide
- **구성**: 헤더(태그·읽기시간·날짜) → 목차(TOC) → 본문 노트카드 N → **내부링크 강화 섹션(롱테일 H2 + 3~4 링크)** → 매거진더보기
- **JSON-LD**: Article(author=운영팀·datePublished·dateModified)+BreadcrumbList

### 4.8 공지사항 (`/notices/{slug}/`) ×4
- 글: southeast-asia-scam(긴급), prostitution-monitoring(중요), newcomer-safety, fraud-report-channel
- **구성**: 우선도뱃지+카테고리 → 목차 → 본문 → **내부링크 강화(롱테일 H2)** → 다른공지3
- 안전·법령 콘텐츠 = E-E-A-T(Trust)·YMYL 신호. 실 신고채널 번호·법령 인용

### 4.9 광고 상세 (`/ad/{공고ID}/`) ×22
- **title**: `[{샵명}] {공고제목} · {지역} | 테라피잡`
- **구성**: 좌측본문(모집안내·혜택·근무조건·우대) + 우측 sticky카드(일급·샵·근무시간·모집인원·계약·정산) → 지원절차4 → FAQ5 → 같은업종공고4
- **지원 = #apply 앵커**(전화연결 X, 이메일 mailto만)
- **JSON-LD**: JobPosting 풀스택 (구글 Jobs 노출)

### 4.10 업소매매 (`/shop-sale/` + `/shop-sale/{ID}/` ×12)
- **목록**: 3단 필터(지역/구·시·군 cascade/업종) + 매물카드 12(매매중·상권라벨·권리금·총금액·월세·보증금·**월매출·월순익**)
- **상세 title**: `{매물제목} — 권리금 {N}만원·월매출 {범위} | 테라피잡 업소매매`
- **상세 구성**: 히어로(상태·평수·월매출골드박스·가격4분할·샘플안내) → 매물정보12필드 → 매물특징(행정구프로필주입) → 매수전체크 → 관련매물4
- **JSON-LD**: Product+Offer+additionalProperty 8필드
- 매수문의 = 매물 카드 직접 클릭(운영자 거치지 않음)

### 4.11 가격/광고 페이지
- `/recruitment-pricing/` — 채용공고 광고 VVIP/VIP/프리미엄 × 1·6·12개월 (44/20/13만~)
- `/shop-sale-pricing/` — 업소매매 등록 1·2·12개월 (10/15/33만)
- `/pricing-ads/` — 종합 안내(노출위치 SVG목업 6개 + 두 상품 요약)
- `/contact-ads/` — 광고문의 폼(성명·연락처·지역·등급·메시지 + honeypot) → Pages Function → Telegram
- **JSON-LD**: Service+OfferCatalog+FAQPage

### 4.12 기타
- `/pricing/` 급여시세표, `/reviews/` 매칭사례, `/about/` 운영팀·데이터방법론, `/contact/` 고객센터
- `/policy/{privacy,terms,youth}/` 정책 3종

---

## 5. SEO·E-E-A-T (구글 2026 기준)

### 5.1 head 메타 (전 페이지 공통, head() 자동)
charset·viewport·theme-color·format-detection·robots(index,follow,max-image-preview:large)·googlebot·referrer·title·description·author·canonical·hreflang(ko-KR,x-default)·og(type/site_name/locale/title/desc/url/image 1200×630)·twitter(summary_large_image)·favicon.svg·manifest·**RSS alternate 링크**

### 5.2 JSON-LD 풀스택 (@graph)
- 전역: Organization(legalName·taxID·address·founder·email) + WebSite(SearchAction)
- 페이지별: WebPage/CollectionPage/Article/Service/JobPosting/Product/LocalBusiness/AdministrativeArea/Place/FAQPage/BreadcrumbList/ItemList+Review/AggregateRating/OfferCatalog+Offer

### 5.3 E-E-A-T 4신호
1. **Experience**: 1차 데이터 — "23,700건 매칭 로그·412건 샵 인터뷰"·구별 현장조사
2. **Expertise**: 자문 트레이너 실명·경력 (박지연 KSPO)
3. **Authoritativeness**: 운영팀 실명 (김세영·이도윤)·책임 영역
4. **Trust**: 사업자정보 6필드 푸터·합법 신고번호·안전 공지·법령 인용

### 5.4 도어웨이 회피 (★중요)
- 행정구 82개: 구별 실 랜드마크·교통·고객층·시장특성·전략으로 차별화 (지역명 치환 금지)
- 업종/국적: 항목별 고유 상세 데이터(SEEKER_DETAIL·THERAPIST_DETAIL)
- 내부 유사도 목표: 편집 콘텐츠 70% 이하

### 5.5 내부 링크
- 블로그(매거진·공지) 하단: 롱테일 H2(40자) + 핵심 링크 3~4개 (지역/업종/관련글/공지)
- 롱테일 H2 예: "마사지 관리사 월급 얼마? 강남·분당·해운대 권역별 일급 시세 2026 비교"

### 5.6 robots.txt (빠른 색인 튜닝)
```
User-agent: * → Allow / (Disallow /api/ /admin/)
Googlebot/Image/News/Storebot/Google-Extended → Allow
Yeti·NaverBot → Allow + Crawl-delay 1   (네이버 빠른 수집)
Daum/Daumoa·Bingbot/msnbot → Allow
GPTBot·OAI-SearchBot·ChatGPT-User·ClaudeBot·PerplexityBot·Applebot → Allow  (AI 검색)
Sitemap: /sitemap.xml + /sitemap1.xml   (이중화)
Host: 도메인
```
> Cloudflare가 `Content-Signal: search=yes,ai-train=no` 자동 주입(무해, AI학습 거부). 끄려면 대시보드 AI Crawl Control.

### 5.7 sitemap·rss
- sitemap.xml + **sitemap1.xml**(동일 미러, 구글 파싱오류 백업)
- 우선순위: `/` 1.0 / 광역·업종·구인허브 0.9~0.95 / 행정구 0.8 / 광고상세 0.7~0.95(등급별) / 매거진·공지 0.75~0.9 / 정책 0.3
- **rss.xml**: 매거진7+공지4=11건, RFC822 pubDate, atom:self → 네이버 RSS 제출 시 색인 가속

---

## 6. 성능 최적화 (Core Web Vitals)

1. **CSS·JS 전부 인라인** — 외부요청 0
2. **content-visibility:auto** + contain-intrinsic-size — 뷰포트 밖 카드/푸터 렌더 스킵 (LCP 50~70%↓)
   - `.note-card,.job-card,.price-card,details,.ad-card.ad-*,.shop-card,.site-footer`
3. **이미지 lazy** (`loading="lazy"`) + WebP/`<picture>` (배너 1.6MB→54KB)
4. **requestIdleCallback** — IntersectionObserver·드롭다운 핸들러 idle 로드
5. **시스템 폰트** — 다운로드 0, FOIT/FOUT 없음
6. **HTML 미니파이** + JSON-LD 1줄화
7. **@media(hover:none)** backdrop-filter 제거 / **prefers-reduced-motion** 애니 끔
8. **width/height 명시** — CLS 0

---

## 7. 광고 비즈니스 모델

### 7.1 채용공고 광고 3등급
| 등급 | 위치 | 슬롯 | 1개월 | 6개월 | 12개월 |
|---|---|---|---|---|---|
| VVIP | Hero 직하 최상단 | 4업체 | 44만 | 88만 | 110만 |
| VIP | First Content Break | 12업체 | 20만 | 45만 | 55만 |
| 프리미엄 | 하단 | 무제한 | 13만 | 20만 | 25만 |
- 같은 등급 내 **선등록순**. 슬롯 부족 시 타지역/업종 backfill
- 노출 데이터: VVIP 월4.2~5.8만회·CTR3.4% / VIP 2.2~3.2만·2.6% / 프리미엄 0.8~1.4만·1.1%

### 7.2 업소매매 매물 등록
- 1개월 10만 / 2개월 15만(BEST·25%↓) / 12개월 33만(72%↓)
- 익명 게재(동까지만 공개), 매수자 1:1 매칭, 거래수수료 0원

### 7.3 광고문의 → Telegram 연동
- `/contact-ads/` 폼 → `functions/api/contact-ads.js`(Pages Function) → Telegram 봇1+봇2
- 환경변수(Pages 설정): `TELEGRAM_BOT_TOKEN_1/CHAT_ID_1`(필수), `_2`(선택), `ALLOWED_ORIGIN`
- honeypot + 서버측 길이/패턴 검증

---

## 8. 회사 정보 (data.py COMPANY)
```
상호: YH LAB (테라피잡)  · 대표: 김수환
사업자등록번호: 815-26-00585
직업정보제공사업 신고: J1802020260002
주소: 경기도 파주시 청석로 268
고객센터: 0508-202-4690 (평일 10:00~19:00)
이메일: help@therapyjob.club  · 개인정보책임자: 김수환
도메인: therapyjob.club
```
> 전화번호는 **광고문의·사용법 안내용**(헤더CTA·푸터). 채용 지원·매수 문의에는 전화 직접 연결하지 않음(폼/매물클릭).

---

## 9. 배포 (Cloudflare Pages)

1. GitHub 레포 → Cloudflare Pages 연결 (빌드 명령 없음, 정적 파일 서빙)
2. 커스텀 도메인 연결 + www→root 301
3. Pages 환경변수에 Telegram 토큰 5개 등록
4. **Google Search Console**: sitemap.xml 제출 + URL 색인 요청
5. **네이버 서치어드바이저**: sitemap.xml + **rss.xml** 제출 (RSS가 색인 가속)
6. (선택) Cloudflare Content Signals 유지/해제

---

## 10. 재사용 워크플로우 (다른 사이트 제작 시)

1. 이 MD + `scripts/` 전체 복사
2. `data.py` COMPANY·업종·국적·지역 데이터 교체
3. `district_profiles.py` 새 지역 실데이터 작성 (★도어웨이 회피 — 지역별 고유 랜드마크 필수)
4. `--blue-*`/`--grad` 컬러 토큰 1~2개 교체로 톤 변경
5. SEEKER_DETAIL·THERAPIST_DETAIL·MAGAZINE_BODIES·NOTICE_BODIES 콘텐츠 교체
6. 가격표(PRICING_ADS·SHOP_SALES) 조정
7. `python3 scripts/build.py` → 전 페이지 자동 생성
8. 검증: title/canonical 100% 고유, JSON-LD 유효, broken link 0, 페이지 유형별 유사도 측정
9. 도메인 연결 → robots/sitemap/rss 제출

> **핵심 한 줄**: 데이터(data.py + district_profiles.py)와 템플릿(templates.py + pages_*.py)을 분리해, 데이터만 바꾸면 수백 페이지가 고유 콘텐츠로 자동 생성되는 구조. 도어웨이를 피하는 건 "지역별 진짜 고유 데이터"에 달려 있다.
