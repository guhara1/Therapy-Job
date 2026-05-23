# 광고문의 폼 → Telegram 봇 설정 가이드

테라피잡의 `/contact-ads/` 광고문의 폼은 정적 사이트에서 직접
텔레그램으로 전송할 수 없어, Cloudflare Worker(서버리스 프록시)를 통해
전달합니다. 본 가이드는 한 번만 따라하면 영구 작동합니다.

소요 시간: **5~10분**.

---

## 1. 텔레그램 봇 만들기 (텔레그램 앱에서)

### 봇 1 생성
1. 텔레그램에서 `@BotFather` 검색 후 대화 시작
2. `/newbot` 명령 입력
3. 봇 이름 (예: `TherapyJob Ads 1`) → 봇 username (예: `therapyjob_ads_1_bot`)
4. 발급된 **토큰** 복사 (예: `123456:ABC-DEF1234...`)
5. 본인 텔레그램에서 `@therapyjob_ads_1_bot` 검색 → `/start` 입력 (반드시 한 번 메시지 보내야 봇이 발송 가능)

### Chat ID 확인
1. 텔레그램에서 `@userinfobot` 검색 → 대화 시작 → `/start`
2. 화면에 표시된 **본인 ID 숫자** 복사 (예: `123456789`)
3. 이 숫자가 봇 1의 `TELEGRAM_CHAT_ID_1`

### 봇 2 (선택 — 다른 사람이나 그룹 채팅으로 동시 발송하려면)
- 위 과정을 한 번 더 반복
- 또는 동일 봇이 그룹 채팅에도 발송하려면: 그룹에 봇 초대 → 그룹 정보에서 chat_id 확인 (음수, 예: `-100123...`)

---

## 2. Cloudflare Worker 배포

### A. Cloudflare 대시보드 접속
1. https://dash.cloudflare.com 로그인 (Pages 쓰시는 계정 동일)
2. 좌측 메뉴에서 **Workers & Pages** 클릭
3. **Create application** → **Create Worker**
4. 이름: `therapyjob-contact` (또는 원하는 이름)
5. **Deploy** 클릭 (기본 hello-world로 일단 배포됨)

### B. Worker 코드 교체
1. 방금 만든 Worker 클릭 → **Edit code**
2. 기본 코드 전체 삭제
3. 이 레포의 `workers/contact-ads.js` 파일 내용을 통째로 복사 → 붙여넣기
4. 우측 상단 **Deploy** 클릭

### C. 환경 변수 추가
1. Worker 페이지에서 **Settings** 탭 → **Variables and Secrets**
2. **+ Add** 버튼으로 다음 4개(또는 5개) 추가, **Type을 모두 Secret**으로 선택:

| 변수명 | 값 | 비고 |
|---|---|---|
| `TELEGRAM_BOT_TOKEN_1` | 봇 1 BotFather 토큰 | 필수 |
| `TELEGRAM_CHAT_ID_1` | 봇 1 chat_id 숫자 | 필수 |
| `TELEGRAM_BOT_TOKEN_2` | 봇 2 토큰 | 선택 (한 채널만이면 비워둬도 됨) |
| `TELEGRAM_CHAT_ID_2` | 봇 2 chat_id | 선택 |
| `ALLOWED_ORIGIN` | `https://therapyjob.club` | 선택 (배포 도메인이 다르면 그에 맞춤) |

3. 저장 후 자동 재배포됨

### D. Worker URL 확인
- Worker 페이지 상단에 표시: `https://therapyjob-contact.<당신의서브도메인>.workers.dev`
- 이 URL을 복사

---

## 3. 사이트 코드에 Worker URL 연결

1. `scripts/pages_core.py` 파일 검색 → `WORKER_URL` 찾기
2. 기본값 `https://therapyjob-contact.workers.dev/`를 본인의 Worker URL로 교체
   ```js
   var WORKER_URL = "https://therapyjob-contact.YOUR-SUBDOMAIN.workers.dev/";
   ```
3. `python3 scripts/build.py` 재실행
4. `git add . && git commit -m "광고문의 Worker URL 연결" && git push`
5. Cloudflare Pages가 자동 재배포 (1~2분)

---

## 4. 테스트

1. 배포된 사이트 `https://therapyjob.club/contact-ads/` 접속
2. 폼 작성 후 **광고문의 보내기** 클릭
3. 텔레그램에서 봇 1(또는 봇 1+2)에게 메시지 도착 확인
4. 화면에 ✓ 성공 메시지 표시 확인

---

## 5. 문제 해결

### "전송에 일시적인 오류가 발생했습니다"가 뜬다
- Worker 페이지 → **Logs** → **Begin log stream** → 폼 다시 제출 → 에러 메시지 확인
- 흔한 원인:
  - 봇이 `/start`를 받지 못함 → 봇과 1:1 대화창에서 `/start` 한 번 입력
  - chat_id가 잘못됨 → `@userinfobot`으로 다시 확인
  - 토큰 오타 → BotFather에서 다시 복사

### 봇이 그룹에 보내는 경우
- 그룹 chat_id는 보통 `-100`으로 시작하는 음수
- 봇을 관리자(또는 메시지 발송 권한 있는) 멤버로 추가 필요

### Worker가 호출되지 않음
- 브라우저 콘솔(F12) → Network 탭 → 폼 제출 후 Worker 호출 확인
- CORS 에러면 `ALLOWED_ORIGIN` 변수가 배포 도메인과 일치하는지 확인

### 비용
- Cloudflare Worker 무료 플랜: **하루 100,000 요청까지 무료**
- 광고문의 폼 트래픽은 한참 못 미치므로 사실상 평생 무료
- 봇 1+2 동시 발송 = 1 요청으로 카운트

---

## 보안

- ✅ 봇 토큰은 Worker 환경변수(Secret)에 저장 — 클라이언트 코드에 노출 안 됨
- ✅ `ALLOWED_ORIGIN`으로 다른 도메인의 호출 차단
- ✅ honeypot 필드 + 서버 측 길이/포맷 검증으로 봇 스팸 차단
- ⚠️ 본 워커 코드는 rate-limit이 없습니다. 스팸 폭주 시 Cloudflare의 **Rate Limiting Rules**를 별도로 적용 권장 (분당 N건).
