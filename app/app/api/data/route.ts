import { env, allowedIds } from "../../../lib/config.ts";
import { verifyInitData } from "../../../lib/telegram-auth.ts";
import { loadAll } from "../../../lib/data.ts";

// Podaci se citaju iz fajlova pri svakom zahtevu: server ih puni cronom,
// pa kes bi samo pokazivao staro stanje.
export const dynamic = "force-dynamic";

export async function GET(req: Request) {
  const user = verifyInitData(req.headers.get("x-telegram-init-data") ?? "", env().TELEGRAM_BOT_TOKEN ?? "");
  if (!user) return Response.json({ error: "unauthorized" }, { status: 401 });
  // ID se vraca da bi odbijen korisnik znao sta da posalje za odobrenje
  if (!allowedIds().has(String(user.id))) return Response.json({ error: "forbidden", id: user.id }, { status: 403 });
  return Response.json(loadAll(), { headers: { "cache-control": "no-store" } });
}
