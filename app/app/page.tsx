"use client";
import { useCallback, useEffect, useState } from "react";
import type { Payload, Post, Track } from "../lib/data.ts";
import GrowthChart, { label } from "../components/GrowthChart.tsx";

declare global {
  interface Window { Telegram?: { WebApp?: { initData: string; colorScheme?: string; ready(): void; expand(): void } } }
}

type State =
  | { kind: "loading" }
  | { kind: "outside" }
  | { kind: "denied"; id?: number }
  | { kind: "error"; msg: string }
  | { kind: "ok"; data: Payload };

const nf = new Intl.NumberFormat("sr-Latn");
const nf2 = new Intl.NumberFormat("sr-Latn", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const DAYS = ["ned", "pon", "uto", "sre", "čet", "pet", "sub"];
const fmtDate = (d: string) => {
  if (!d) return "bez datuma";
  const dt = new Date(`${d}T12:00:00`);
  return `${DAYS[dt.getDay()]} ${String(dt.getDate()).padStart(2, "0")}.${String(dt.getMonth() + 1).padStart(2, "0")}.`;
};
const fmtAge = (h: number) => (h < 48 ? `${nf.format(Math.round(h * 10) / 10)} h` : `${Math.floor(h / 24)} d`);

const STATUS: Record<string, [string, string]> = {
  draft: ["✎", "nacrt"],
  approved: ["✓", "odobreno"],
  scheduled: ["◷", "zakazano"],
  published: ["●", "objavljeno"],
};

export default function Page() {
  const [state, setState] = useState<State>({ kind: "loading" });
  const [tab, setTab] = useState<"plan" | "stats" | "agents">("plan");

  const load = useCallback(async () => {
    const wa = window.Telegram?.WebApp;
    if (!wa?.initData) return setState({ kind: "outside" });
    try {
      const r = await fetch("/api/data", { headers: { "x-telegram-init-data": wa.initData }, cache: "no-store" });
      if (r.status === 401) return setState({ kind: "error", msg: "Potpis nije prosao. Zatvori i otvori ponovo iz bota." });
      if (r.status === 403) return setState({ kind: "denied", id: (await r.json()).id });
      if (!r.ok) return setState({ kind: "error", msg: `Server je vratio ${r.status}.` });
      setState({ kind: "ok", data: await r.json() });
    } catch {
      setState({ kind: "error", msg: "Nema veze sa serverom." });
    }
  }, []);

  useEffect(() => {
    const wa = window.Telegram?.WebApp;
    wa?.ready();
    wa?.expand();
    if (wa?.colorScheme) document.documentElement.dataset.theme = wa.colorScheme;
    // ?tab=stats iz linka: alarm iz bota vodi pravo na statistiku
    const t = new URLSearchParams(location.search).get("tab");
    if (t === "plan" || t === "stats" || t === "agents") setTab(t);
    load();
  }, [load]);

  if (state.kind === "loading") return <p className="notice">Ucitavam…</p>;
  if (state.kind === "outside")
    return <div className="notice"><strong>Otvori kroz Telegram</strong>Ova stranica radi samo iz bota @hb_swarm_bot.</div>;
  if (state.kind === "denied")
    return <div className="notice"><strong>Nemas pristup</strong>{state.id ? `Tvoj Telegram ID: ${state.id}` : null}</div>;
  if (state.kind === "error") return <div className="notice"><strong>Nesto nije u redu</strong>{state.msg}</div>;

  const d = state.data;
  const at = new Date(d.generatedAt);
  return (
    <div className="wrap">
      <header className="top">
        <div className="brand">
          <h1>🐝 Swarm</h1>
          <span>
            <small>osvezeno {at.getHours()}:{String(at.getMinutes()).padStart(2, "0")} </small>
            <button className="refresh" onClick={() => { setState({ kind: "loading" }); load(); }}>Osvezi</button>
          </span>
        </div>
        <nav className="tabs" role="tablist">
          {([["plan", "Plan"], ["stats", "Statistika"], ["agents", "Agenti"]] as const).map(([k, t]) => (
            <button key={k} role="tab" aria-selected={tab === k} onClick={() => setTab(k)}>{t}</button>
          ))}
        </nav>
      </header>
      {tab === "plan" && <PlanTab posts={d.posts} />}
      {tab === "stats" && <StatsTab data={d} />}
      {tab === "agents" && <AgentsTab data={d} />}
    </div>
  );
}

function PostCard({ p }: { p: Post }) {
  const [glyph, name] = STATUS[p.status] ?? ["•", p.status];
  return (
    <article className="card">
      <div className="meta">
        <span className="badge"><span aria-hidden>{glyph}</span>{name}</span>
        <span>{fmtDate(p.date)}{p.time ? ` · ${p.time}` : ""}</span>
        <span>@{p.account}</span>
      </div>
      <h3>{p.title}</h3>
      {p.text && <p className="post-text">{p.text}</p>}
      {p.media && <div className="media">Uz post: {p.media}</div>}
      {p.stats && (
        <div className="stats">
          <span><strong>{nf.format(p.stats.views)}</strong> views</span>
          <span><strong>{nf.format(p.stats.likes)}</strong> likes</span>
          <span><strong>{nf.format(p.stats.replies)}</strong> odgovora</span>
          <span><strong>{nf.format(p.stats.bookmarks)}</strong> bm</span>
          <span>posle {fmtAge(p.stats.ageH)}</span>
          <a href={p.stats.url} target="_blank" rel="noreferrer">Otvori na X</a>
        </div>
      )}
    </article>
  );
}

function PlanTab({ posts }: { posts: Post[] }) {
  const next = posts.filter((p) => p.status === "approved" || p.status === "scheduled");
  const drafts = posts.filter((p) => p.status === "draft");
  const done = posts.filter((p) => p.status === "published").reverse();
  return (
    <section>
      <h2>Sledece</h2>
      {next.length ? next.map((p) => <PostCard key={p.file} p={p} />) : <p className="empty">Nista nije zakazano.</p>}
      <h2>Nacrti</h2>
      {drafts.length ? drafts.map((p) => <PostCard key={p.file} p={p} />) : <p className="empty">Nema nacrta.</p>}
      <h2>Objavljeno</h2>
      {done.length ? done.map((p) => <PostCard key={p.file} p={p} />) : <p className="empty">Jos nista.</p>}
    </section>
  );
}

function StatsTab({ data }: { data: Payload }) {
  const recent: Track[] = data.tracks.slice(0, 4);
  return (
    <section>
      <h2>Nalozi</h2>
      <div className="tiles">
        {data.accounts.map((a) => (
          <div className="tile" key={a.handle}>
            <div className="label">@{a.handle} · {a.role}</div>
            <div className="value">{nf.format(a.followers)}</div>
            <div className="sub">
              pratilaca · med. {a.medianViews30d === null ? "—" : nf.format(a.medianViews30d)} views u 30 dana
              {a.medianViews30d !== null && a.followers ? ` (${nf2.format(a.medianViews30d / a.followers)} po pratiocu)` : ""}
            </div>
          </div>
        ))}
      </div>

      <h2>Rast postova</h2>
      <div className="chart-card">
        <div className="title">Views po satima od objave</div>
        <div className="subtitle">Poslednja {recent.length} pracena posta, poravnata na trenutak objave.</div>
        <GrowthChart tracks={recent} />
      </div>

      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Post</th><th>Nalog</th><th className="num">Starost</th><th className="num">Views</th><th className="num">Likes</th><th className="num">Odg.</th><th className="num">BM</th></tr>
          </thead>
          <tbody>
            {data.tracks.map((t) => {
              const l = t.points.at(-1)!;
              return (
                <tr key={t.id}>
                  <td className="txt"><a href={t.url} target="_blank" rel="noreferrer">{label(t)}</a></td>
                  <td>@{t.handle}</td>
                  <td className="num">{fmtAge(l.ageH)}</td>
                  <td className="num">{nf.format(l.views)}</td>
                  <td className="num">{nf.format(l.likes)}</td>
                  <td className="num">{nf.format(l.replies)}</td>
                  <td className="num">{nf.format(l.bookmarks)}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function AgentsTab({ data }: { data: Payload }) {
  return (
    <section>
      <h2>Agenti</h2>
      {data.agents.map((a) => (
        <article className="card" key={a.name}>
          <div className="agent-name">{a.name}</div>
          <div className="meta" style={{ marginTop: 4 }}>
            {a.model && <span>model: {a.model}</span>}
            {a.tools && <span>alati: {a.tools}</span>}
          </div>
          <p style={{ margin: "8px 0 4px" }}>{a.description}</p>
          <div className="md" dangerouslySetInnerHTML={{ __html: a.usageHtml }} />
        </article>
      ))}
      <h2>Kako traziti od Claude-a</h2>
      <div className="card md" dangerouslySetInnerHTML={{ __html: data.askHtml }} />
      <h2>Alati</h2>
      <div className="card md" dangerouslySetInnerHTML={{ __html: data.toolsHtml }} />
      <h2>Uskoro</h2>
      <div className="card md" dangerouslySetInnerHTML={{ __html: data.soonHtml }} />
    </section>
  );
}
