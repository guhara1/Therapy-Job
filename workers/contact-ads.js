/**
 * Cloudflare Worker — 테라피잡 광고문의 폼 → Telegram 봇 2채널 전송
 *
 * 배포 방법은 workers/README.md 참고.
 *
 * 환경 변수 (Cloudflare Workers > Settings > Variables and Secrets):
 *   - TELEGRAM_BOT_TOKEN_1   (필수)  봇 1의 BotFather 토큰
 *   - TELEGRAM_CHAT_ID_1     (필수)  봇 1이 보낼 chat_id (또는 채널 @username)
 *   - TELEGRAM_BOT_TOKEN_2   (선택)  봇 2의 BotFather 토큰
 *   - TELEGRAM_CHAT_ID_2     (선택)  봇 2가 보낼 chat_id
 *   - ALLOWED_ORIGIN         (선택)  허용 도메인 (기본 https://therapyjob.club)
 *
 * 같은 봇이 두 채팅(개인·그룹)으로 보내고 싶다면 TOKEN_2를 비우고
 * 코드 내부에서 동일 토큰으로 2번 호출하도록 수정하셔도 됩니다.
 */

const DEFAULT_ALLOWED = "https://therapyjob.club";

export default {
  async fetch(request, env) {
    const origin = env.ALLOWED_ORIGIN || DEFAULT_ALLOWED;

    // CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders(origin) });
    }
    if (request.method !== "POST") {
      return json({ ok: false, error: "method_not_allowed" }, 405, origin);
    }

    // Origin 검사 — 다른 도메인에서의 호출 차단
    const reqOrigin = request.headers.get("Origin") || "";
    if (origin !== "*" && reqOrigin && reqOrigin !== origin) {
      // 로컬 테스트(파일·localhost)는 Origin 비어있을 수 있어 허용
      return json({ ok: false, error: "forbidden_origin" }, 403, origin);
    }

    let data;
    try {
      data = await request.json();
    } catch (e) {
      return json({ ok: false, error: "invalid_json" }, 400, origin);
    }

    // 필드 검증
    const name = (data.name || "").toString().trim().slice(0, 30);
    const phone = (data.phone || "").toString().trim().slice(0, 25);
    const region = (data.region || "").toString().trim().slice(0, 20);
    const tier = (data.tier || "").toString().trim().slice(0, 20);
    const message = (data.message || "").toString().trim().slice(0, 1500);
    const page = (data.page || "").toString().slice(0, 200);
    const referrer = (data.referrer || "").toString().slice(0, 200);
    const ts = (data.ts || new Date().toISOString()).toString().slice(0, 30);

    if (!name || name.length < 2) return json({ ok: false, error: "name_required" }, 400, origin);
    if (!phone || !/^[0-9\-+\s()]{8,25}$/.test(phone)) return json({ ok: false, error: "phone_invalid" }, 400, origin);
    if (!region) return json({ ok: false, error: "region_required" }, 400, origin);
    if (!message || message.length < 5) return json({ ok: false, error: "message_required" }, 400, origin);

    // honeypot (혹시 클라에서 누락된 경우 한 번 더 차단)
    if (data.website) return json({ ok: true }, 200, origin); // 봇에게는 정상처럼 응답

    // Telegram 메시지 포맷 (HTML)
    const escape = (s) => String(s).replace(/[<>&"]/g, (c) => ({"<":"&lt;",">":"&gt;","&":"&amp;","\"":"&quot;"}[c]));
    const text =
      `🔔 <b>테라피잡 광고문의 신규 접수</b>\n\n` +
      `👤 <b>성명</b>: ${escape(name)}\n` +
      `📞 <b>연락처</b>: <code>${escape(phone)}</code>\n` +
      `📍 <b>지역</b>: ${escape(region)}\n` +
      (tier ? `🏷️ <b>희망 등급</b>: ${escape(tier)}\n` : ``) +
      `\n💬 <b>메시지</b>\n<pre>${escape(message)}</pre>\n` +
      `\n────────────────\n` +
      `🕒 ${escape(ts)}\n` +
      (page ? `📄 페이지: <code>${escape(page)}</code>\n` : ``) +
      (referrer ? `↩️ 유입: ${escape(referrer)}\n` : ``);

    // 봇 1로 전송
    const t1 = env.TELEGRAM_BOT_TOKEN_1;
    const c1 = env.TELEGRAM_CHAT_ID_1;
    if (!t1 || !c1) {
      return json({ ok: false, error: "server_not_configured" }, 500, origin);
    }
    const r1 = await sendTelegram(t1, c1, text);

    // 봇 2로 전송 (설정된 경우만)
    const t2 = env.TELEGRAM_BOT_TOKEN_2;
    const c2 = env.TELEGRAM_CHAT_ID_2;
    let r2 = { ok: true, skipped: true };
    if (t2 && c2) {
      r2 = await sendTelegram(t2, c2, text);
    }

    // 최소 1개는 성공해야 ok
    if (!r1.ok && !r2.ok) {
      return json({ ok: false, error: "telegram_failed", detail: { r1, r2 } }, 502, origin);
    }
    return json({ ok: true, sent: { bot1: r1.ok, bot2: r2.ok || r2.skipped } }, 200, origin);
  },
};

async function sendTelegram(token, chatId, text) {
  const url = `https://api.telegram.org/bot${token}/sendMessage`;
  try {
    const resp = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: chatId,
        text,
        parse_mode: "HTML",
        disable_web_page_preview: true,
      }),
    });
    const data = await resp.json();
    return { ok: data.ok === true, raw: data };
  } catch (e) {
    return { ok: false, error: String(e) };
  }
}

function corsHeaders(origin) {
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
}

function json(obj, status, origin) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...corsHeaders(origin),
    },
  });
}
