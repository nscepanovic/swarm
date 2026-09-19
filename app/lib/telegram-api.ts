import { env } from "./config.ts";

export async function tg(method: string, body: Record<string, unknown>) {
  const token = env().TELEGRAM_BOT_TOKEN;
  if (!token) throw new Error("nema TELEGRAM_BOT_TOKEN");
  const r = await fetch(`https://api.telegram.org/bot${token}/${method}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
  });
  return r.json() as Promise<{ ok: boolean; description?: string; result?: unknown }>;
}
