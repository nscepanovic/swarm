import crypto from "node:crypto";
import { env, allowedIds } from "../../../lib/config.ts";
import { tg } from "../../../lib/telegram-api.ts";

export const dynamic = "force-dynamic";

// Telegram webhook. Dve provere:
// 1. zahtev mora doneti tajni kljuc koji smo zadali pri setWebhook - inace
//    nije od Telegrama i odbija se
// 2. posiljalac mora biti na listi odobrenih - inace se poruka CUTKE
//    ignorise: bot nikome van liste ne odgovara i nista ne otkriva
export async function POST(req: Request) {
  const e = env();
  const secret = e.TELEGRAM_WEBHOOK_SECRET ?? "";
  const got = req.headers.get("x-telegram-bot-api-secret-token") ?? "";
  const ok = secret.length > 0 && got.length === secret.length &&
    crypto.timingSafeEqual(Buffer.from(got), Buffer.from(secret));
  if (!ok) return new Response("forbidden", { status: 403 });

  const update = await req.json().catch(() => null);
  const msg = update?.message;
  const from = msg?.from;
  // Telegramu uvek 200, da ne ponavlja isporuku - i za odbijene
  if (!from || !allowedIds().has(String(from.id)) || msg.chat?.type !== "private") {
    return Response.json({ ok: true });
  }

  const appUrl = e.SWARM_APP_URL;
  if (appUrl) {
    await tg("sendMessage", {
      chat_id: msg.chat.id,
      text: "Swarm: plan postova, statistika i agenti.",
      reply_markup: { inline_keyboard: [[{ text: "Otvori Swarm", web_app: { url: appUrl } }]] },
    });
  }
  return Response.json({ ok: true });
}
