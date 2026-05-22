/**
 * Cloudflare Pages Function — 광고문의 폼 → Telegram 봇 2채널 전송
 *
 * 엔드포인트: https://<your-site>/api/contact-ads
 * 자동 배포: git push 하면 Pages가 자동으로 함수까지 빌드·배포
 *
 * 환경 변수 (Pages 프로젝트 > 설정 > 변수 및 암호):
 *   - TELEGRAM_BOT_TOKEN_1   (필수, Secret)
 *   - TELEGRAM_CHAT_ID_1     (필수, Secret 또는 일반 텍스트)
 *   - TELEGRAM_BOT_TOKEN_2   (선택, Secret)
 *   - TELEGRAM_CHAT_ID_2     (선택)
 *   - ALLOWED_ORIGIN         (선택, 기본 *) — 추가 보안 원할 시 도메인 명시
 */

export async function onRequestPost(context) {
  const { request, env } = context;
  const origin = env.ALLOWED_ORIGIN || "*";
  const headers = corsHeaders(origin);

  let data;
  try {
    data = await request.json();
  } catch (e) {
    return json({ ok: false, error: "invalid_json" }, 400, headers);
  }

  // honeypot — 봇이 채우면 정상 응답하되 발송은 스킵
  if (data.website) {
    return json({ ok: true }, 200, headers);
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

  if (!name || name.length < 2) return json({ ok: false, error: "name_required" }, 400, headers);
  if (!phone || !/^[0-9\-+\s()]{8,25}$/.test(phone)) return json({ ok: false, error: "phone_invalid" }, 400, headers);
  if (!region) return json({ ok: false, error: "region_required" }, 400, headers);
  if (!message || message.length < 5) return json({ ok: false, error: "message_required" }, 400, headers);

  // Telegram HTML 메시지
  const text =
    `🔔 <b>테라피잡 광고문의 신규 접수</b>\n\n` +
    `👤 <b>성명</b>: ${esc(name)}\n` +
    `📞 <b>연락처</b>: <code>${esc(phone)}</code>\n` +
    `📍 <b>지역</b>: ${esc(region)}\n` +
    (tier ? `🏷️ <b>희망 등급</b>: ${esc(tier)}\n` : ``) +
    `\n💬 <b>메시지</b>\n<pre>${esc(message)}</pre>\n` +
    `\n────────────────\n` +
    `🕒 ${esc(ts)}\n` +
    (page ? `📄 페이지: <code>${esc(page)}</code>\n` : ``) +
    (referrer ? `↩️ 유입: ${esc(referrer)}\n` : ``);

  const t1 = env.TELEGRAM_BOT_TOKEN_1;
  const c1 = env.TELEGRAM_CHAT_ID_1;
  if (!t1 || !c1) {
    return json({ ok: false, error: "server_not_configured", detail: "TELEGRAM_BOT_TOKEN_1 또는 TELEGRAM_CHAT_ID_1 환경변수가 비어있습니다." }, 500, headers);
  }

  const r1 = await sendTelegram(t1, c1, text);

  const t2 = env.TELEGRAM_BOT_TOKEN_2;
  const c2 = env.TELEGRAM_CHAT_ID_2;
  let r2 = { ok: true, skipped: true };
  if (t2 && c2) {
    r2 = await sendTelegram(t2, c2, text);
  }

  if (!r1.ok && !r2.ok) {
    return json({ ok: false, error: "telegram_failed", detail: { r1, r2 } }, 502, headers);
  }
  return json({ ok: true, sent: { bot1: r1.ok, bot2: r2.ok || r2.skipped } }, 200, headers);
}

export async function onRequestOptions(context) {
  const origin = context.env.ALLOWED_ORIGIN || "*";
  return new Response(null, { status: 204, headers: corsHeaders(origin) });
}

// GET 등 다른 메서드는 거부
export async function onRequest(context) {
  if (context.request.method === "POST") return onRequestPost(context);
  if (context.request.method === "OPTIONS") return onRequestOptions(context);
  return new Response("Method Not Allowed", { status: 405 });
}

function esc(s) {
  return String(s).replace(/[<>&"]/g, (c) => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;" }[c]));
}

async function sendTelegram(token, chatId, text) {
  try {
    const resp = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
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
    Vary: "Origin",
  };
}

function json(obj, status, headers) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...headers },
  });
}
