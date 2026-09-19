import crypto from "node:crypto";

export type TgUser = { id: number; first_name?: string; username?: string };

/**
 * Provera podataka koje Telegram mini app salje (window.Telegram.WebApp.initData).
 * Telegram ih potpisuje HMAC-om izvedenim iz tokena bota, pa ih niko bez
 * tokena ne moze falsifikovati: https://core.telegram.org/bots/webapps
 *
 * Vraca korisnika samo ako je potpis ispravan i podaci nisu stariji od maxAgeSec.
 */
export function verifyInitData(initData: string, botToken: string, maxAgeSec = 24 * 3600): TgUser | null {
  if (!initData || !botToken) return null;
  const params = new URLSearchParams(initData);
  const hash = params.get("hash");
  if (!hash || !/^[0-9a-f]{64}$/.test(hash)) return null;

  const secret = crypto.createHmac("sha256", "WebAppData").update(botToken).digest();
  const matches = (exclude: string[]) => {
    const dcs = [...params.entries()]
      .filter(([k]) => !exclude.includes(k))
      .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0))
      .map(([k, v]) => `${k}=${v}`)
      .join("\n");
    const calc = crypto.createHmac("sha256", secret).update(dcs).digest();
    const given = Buffer.from(hash, "hex");
    return calc.length === given.length && crypto.timingSafeEqual(calc, given);
  };
  // Novije verzije Telegrama dodaju i polje `signature`. Oba nacina racunanja su
  // HMAC nasim tokenom, pa je prolaz bilo kog dokaz autenticnosti.
  if (!matches(["hash"]) && !matches(["hash", "signature"])) return null;

  const authDate = Number(params.get("auth_date"));
  if (!authDate || Date.now() / 1000 - authDate > maxAgeSec) return null;

  try {
    const user = JSON.parse(params.get("user") ?? "");
    return typeof user?.id === "number" ? (user as TgUser) : null;
  } catch {
    return null;
  }
}

/** Samo za testove: pravi potpisane podatke kao sto bi ih Telegram poslao. */
export function signInitData(fields: Record<string, string>, botToken: string): string {
  const secret = crypto.createHmac("sha256", "WebAppData").update(botToken).digest();
  const dcs = Object.entries(fields).sort(([a], [b]) => (a < b ? -1 : 1)).map(([k, v]) => `${k}=${v}`).join("\n");
  const hash = crypto.createHmac("sha256", secret).update(dcs).digest("hex");
  return new URLSearchParams({ ...fields, hash }).toString();
}
