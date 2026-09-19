import fs from "node:fs";
import path from "node:path";

// Aplikacija zivi u swarm/app, a podaci u swarm/content. Isti .env za sve.
export const SWARM_ROOT = process.env.SWARM_ROOT ?? path.resolve(process.cwd(), "..");

// Namerno bez kesiranja: kad se u .env doda nov odobren korisnik, vazi odmah,
// bez restarta. Fajl je sitan, citanje po zahtevu nista ne kosta.
export function env(): Record<string, string> {
  const out: Record<string, string> = {};
  try {
    for (const raw of fs.readFileSync(path.join(SWARM_ROOT, ".env"), "utf8").split("\n")) {
      const line = raw.trim();
      if (!line || line.startsWith("#") || !line.includes("=")) continue;
      const i = line.indexOf("=");
      out[line.slice(0, i).trim()] = line.slice(i + 1).trim();
    }
  } catch {
    // nema .env -> nema tokena -> svaki zahtev se odbija
  }
  for (const [k, v] of Object.entries(process.env)) if (v !== undefined) out[k] = v;
  return out;
}

export function allowedIds(): Set<string> {
  return new Set((env().ALLOWED_TELEGRAM_IDS ?? "").split(",").map((s) => s.trim()).filter(Boolean));
}
