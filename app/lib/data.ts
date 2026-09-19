import fs from "node:fs";
import path from "node:path";
import { SWARM_ROOT } from "./config.ts";
import { renderMarkdown } from "./markdown.ts";

const C = (...p: string[]) => path.join(SWARM_ROOT, ...p);
const readText = (f: string) => { try { return fs.readFileSync(f, "utf8"); } catch { return ""; } };
const readJson = <T,>(f: string, fallback: T): T => { try { return JSON.parse(fs.readFileSync(f, "utf8")); } catch { return fallback; } };
const jsonl = (f: string) => readText(f).split("\n").filter((l) => l.trim()).flatMap((l) => { try { return [JSON.parse(l)]; } catch { return []; } });

// ---------------------------------------------------------------- postovi

export type Post = {
  file: string; status: string; date: string; time: string; account: string;
  title: string; media: string; tweetId: string; text: string;
  stats: { views: number; likes: number; replies: number; bookmarks: number; ageH: number; url: string } | null;
};

function frontmatter(src: string): [Record<string, string>, string] {
  if (!src.startsWith("---\n")) return [{}, src];
  const end = src.indexOf("\n---", 4);
  if (end < 0) return [{}, src];
  const fm: Record<string, string> = {};
  for (const line of src.slice(4, end).split("\n")) {
    const m = line.match(/^([a-z_]+):\s*(.*?)\s*$/i);
    if (m) fm[m[1]] = m[2].replace(/^"(.*)"$/, "$1");
  }
  return [fm, src.slice(end + 4)];
}

// Tekst posta je sekcija "## POST" do prve linije "---" ili sledeceg naslova.
// U fajlovima je tekst prelomljen na 80 kolona, pa se redovi unutar pasusa spajaju.
function postText(body: string): string {
  const lines = body.split("\n");
  const start = lines.findIndex((l) => /^## POST\b/.test(l));
  if (start < 0) return "";
  const out: string[] = [];
  for (const l of lines.slice(start + 1)) {
    if (l.trim() === "---" || /^## /.test(l)) break;
    if (/^\s*\[.*\]\s*$/.test(l)) continue; // [VIDEO: ...], [SLIKA]
    out.push(l);
  }
  return out.join("\n").trim().split(/\n\s*\n/).map((p) => p.split("\n").map((s) => s.trim()).join(" ")).join("\n\n");
}

export function loadPosts(latest: Map<string, Track>): Post[] {
  const posts: Post[] = [];
  for (const folder of ["drafts", "approved", "published"]) {
    const dir = C("content", "posts", folder);
    let files: string[] = [];
    try { files = fs.readdirSync(dir).filter((f) => f.endsWith(".md")); } catch { continue; }
    for (const f of files) {
      const [fm, body] = frontmatter(readText(path.join(dir, f)));
      const t = fm.tweet_id ? latest.get(fm.tweet_id) : undefined;
      const last = t?.points.at(-1);
      posts.push({
        file: `${folder}/${f}`,
        status: fm.status || (folder === "drafts" ? "draft" : folder === "published" ? "published" : "approved"),
        date: fm.date ?? "", time: fm.time ?? "", account: fm.account ?? "",
        title: fm.title ?? f.replace(/\.md$/, ""), media: fm.media ?? "", tweetId: fm.tweet_id ?? "",
        text: postText(body),
        stats: t && last ? { views: last.views, likes: last.likes, replies: last.replies, bookmarks: last.bookmarks, ageH: last.ageH, url: t.url } : null,
      });
    }
  }
  return posts.sort((a, b) => (a.date || "9999").localeCompare(b.date || "9999") || a.time.localeCompare(b.time));
}

// ---------------------------------------------------------------- pracenje

export type Point = { ageH: number; views: number; likes: number; replies: number; bookmarks: number };
export type Track = { id: string; handle: string; url: string; text: string; createdAt: string; points: Point[] };

export function loadTracking(): Map<string, Track> {
  const by = new Map<string, Track>();
  for (const r of jsonl(C("content", "tracking.jsonl"))) {
    if (!r?.id) continue;
    const t: Track = by.get(r.id) ?? { id: r.id, handle: r.handle, url: r.url, text: r.text ?? "", createdAt: r.created_at, points: [] };
    t.points.push({ ageH: r.age_h, views: r.views ?? 0, likes: r.likes ?? 0, replies: r.replies ?? 0, bookmarks: r.bookmarks ?? 0 });
    by.set(r.id, t);
  }
  for (const t of by.values()) {
    t.points.sort((a, b) => a.ageH - b.ageH);
    // isti snimak dvaput (npr. dva pokretanja u istom minutu) ne sme da pravi cik-cak
    t.points = t.points.filter((p, i, a) => i === 0 || p.ageH - a[i - 1].ageH > 0.05);
  }
  return by;
}

// ---------------------------------------------------------------- nalozi

export type Account = { handle: string; role: string; followers: number; medianViews30d: number | null; postsIn30d: number };

export function loadAccounts(): Account[] {
  const out: Account[] = [];
  const cutoff = Date.now() - 30 * 86400_000;
  for (const [slug, role] of [["hivebits", "brend"], ["nemanja", "osnivac"]] as const) {
    const meta = readJson<{ handle?: string; followers?: number }>(C("content", "profiles", slug, "meta.json"), {});
    const rows = jsonl(C("content", "profiles", slug, "posts.jsonl")).filter(
      (r) => !r.is_retweet && r.views >= 20 && (r.thread_position ?? 1) <= 1 && Date.parse(r.created_at) >= cutoff,
    );
    const views = rows.map((r) => r.views as number).sort((a, b) => a - b);
    const median = views.length ? views[Math.floor(views.length / 2)] : null;
    out.push({ handle: meta.handle ?? slug, role, followers: meta.followers ?? 0, medianViews30d: median, postsIn30d: views.length });
  }
  return out;
}

// ---------------------------------------------------------------- agenti

export type Agent = { name: string; description: string; model: string; tools: string; usageHtml: string };

function sections(md: string): Map<string, string> {
  const map = new Map<string, string>();
  let name = "";
  let buf: string[] = [];
  for (const line of md.split("\n")) {
    const m = line.match(/^## (.+)$/);
    if (m) { if (name) map.set(name, buf.join("\n")); name = m[1].trim(); buf = []; }
    else if (name) buf.push(line);
  }
  if (name) map.set(name, buf.join("\n"));
  return map;
}

export function loadAgents(): { agents: Agent[]; toolsHtml: string; askHtml: string; soonHtml: string } {
  const usage = sections(readText(C("context", "agents.md")));
  const agents: Agent[] = [];
  let files: string[] = [];
  try { files = fs.readdirSync(C(".claude", "agents")).filter((f) => f.endsWith(".md")); } catch {}
  for (const f of files) {
    const [fm] = frontmatter(readText(C(".claude", "agents", f)));
    const name = fm.name || f.replace(/\.md$/, "");
    agents.push({ name, description: fm.description ?? "", model: fm.model ?? "", tools: fm.tools ?? "", usageHtml: renderMarkdown(usage.get(name) ?? "") });
  }
  return {
    agents,
    toolsHtml: renderMarkdown(usage.get("Alati") ?? ""),
    askHtml: renderMarkdown(usage.get("Kako traziti od Claude-a") ?? ""),
    soonHtml: renderMarkdown(usage.get("Uskoro") ?? ""),
  };
}

// ---------------------------------------------------------------- sve

export function loadAll() {
  const tracking = loadTracking();
  return {
    generatedAt: new Date().toISOString(),
    posts: loadPosts(tracking),
    tracks: [...tracking.values()].sort((a, b) => Date.parse(b.createdAt) - Date.parse(a.createdAt)),
    accounts: loadAccounts(),
    ...loadAgents(),
  };
}
export type Payload = ReturnType<typeof loadAll>;
