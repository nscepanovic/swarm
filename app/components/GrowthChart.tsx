"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import type { Track } from "../lib/data.ts";

const nf = new Intl.NumberFormat("sr-Latn");
const H = 240;
const M = { top: 12, right: 14, bottom: 26, left: 44 };

// Okrugle podele ose: 0 / 500 / 1.000, nikad 0 / 437 / 874.
function niceStep(max: number, target: number) {
  const raw = max / target;
  const mag = 10 ** Math.floor(Math.log10(raw || 1));
  return [1, 2, 2.5, 5, 10].map((m) => m * mag).find((s) => s >= raw) ?? raw;
}

// Vrednost u trenutku t; van posmatranog opsega nema vrednosti (ne izmisljamo).
function valueAt(t: Track, age: number): number | null {
  const p = t.points;
  if (!p.length || age < p[0].ageH - 0.01 || age > p[p.length - 1].ageH + 0.01) return null;
  for (let i = 1; i < p.length; i++) {
    if (age <= p[i].ageH) {
      const a = p[i - 1], b = p[i];
      const f = b.ageH === a.ageH ? 1 : (age - a.ageH) / (b.ageH - a.ageH);
      return Math.round(a.views + f * (b.views - a.views));
    }
  }
  return p[p.length - 1].views;
}

export function label(t: Track) {
  const d = new Date(t.createdAt);
  return `${String(d.getDate()).padStart(2, "0")}.${String(d.getMonth() + 1).padStart(2, "0")}. ${t.text.replace(/\s+/g, " ").slice(0, 34)}…`;
}

export default function GrowthChart({ tracks }: { tracks: Track[] }) {
  const box = useRef<HTMLDivElement>(null);
  const [w, setW] = useState(360);
  const [hover, setHover] = useState<number | null>(null); // indeks u snaps

  useEffect(() => {
    if (!box.current) return;
    const ro = new ResizeObserver(([e]) => setW(Math.max(260, e.contentRect.width)));
    ro.observe(box.current);
    return () => ro.disconnect();
  }, []);

  const g = useMemo(() => {
    const maxAge = Math.min(72, Math.max(6, ...tracks.flatMap((t) => t.points.map((p) => p.ageH))));
    const xStep = [1, 2, 3, 6, 12, 24].find((s) => maxAge / s <= 6) ?? 24;
    const xMax = Math.ceil(maxAge / xStep) * xStep;
    const maxViews = Math.max(10, ...tracks.flatMap((t) => t.points.filter((p) => p.ageH <= xMax).map((p) => p.views)));
    const yStep = niceStep(maxViews, 4);
    const yMax = Math.ceil(maxViews / yStep) * yStep;
    const iw = w - M.left - M.right, ih = H - M.top - M.bottom;
    const x = (a: number) => M.left + (a / xMax) * iw;
    const y = (v: number) => M.top + ih - (v / yMax) * ih;
    const snaps = [...new Set(tracks.flatMap((t) => t.points.filter((p) => p.ageH <= xMax).map((p) => Math.round(p.ageH * 10) / 10)))].sort((a, b) => a - b);
    return { xMax, xStep, yMax, yStep, x, y, iw, ih, snaps };
  }, [tracks, w]);

  if (!tracks.length) return <p className="empty">Jos nema pracenih postova.</p>;

  const onMove = (e: React.PointerEvent<SVGSVGElement>) => {
    const r = e.currentTarget.getBoundingClientRect();
    const age = ((e.clientX - r.left - M.left) / g.iw) * g.xMax;
    let best = 0;
    g.snaps.forEach((s, i) => { if (Math.abs(s - age) < Math.abs(g.snaps[best] - age)) best = i; });
    setHover(best);
  };
  const onKey = (e: React.KeyboardEvent) => {
    if (e.key === "ArrowRight") setHover((h) => Math.min(g.snaps.length - 1, (h ?? -1) + 1));
    else if (e.key === "ArrowLeft") setHover((h) => Math.max(0, (h ?? g.snaps.length) - 1));
    else if (e.key === "Escape") setHover(null);
    else return;
    e.preventDefault();
  };

  const age = hover !== null ? g.snaps[hover] : null;
  const hx = age !== null ? g.x(age) : 0;
  const yTicks = Array.from({ length: Math.round(g.yMax / g.yStep) + 1 }, (_, i) => i * g.yStep);
  const xTicks = Array.from({ length: Math.round(g.xMax / g.xStep) + 1 }, (_, i) => i * g.xStep);

  return (
    <>
      <div className="legend">
        {tracks.map((t, i) => (
          <span key={t.id}><i className="key" style={{ background: `var(--series-${i + 1})` }} />{label(t)}</span>
        ))}
      </div>
      <div className="plot" ref={box}>
        <svg
          height={H} viewBox={`0 0 ${w} ${H}`} role="img" tabIndex={0}
          aria-label="Views po satima od objave; strelicama levo i desno kroz tacke merenja"
          onPointerMove={onMove} onPointerDown={onMove} onPointerLeave={() => setHover(null)}
          onKeyDown={onKey} onBlur={() => setHover(null)}
        >
          {yTicks.map((v) => (
            <g key={v}>
              <line x1={M.left} x2={w - M.right} y1={g.y(v)} y2={g.y(v)} stroke={v === 0 ? "var(--axis)" : "var(--grid)"} strokeWidth={1} />
              <text x={M.left - 8} y={g.y(v)} dy="0.32em" textAnchor="end" fontSize={11} fill="var(--muted)" style={{ fontVariantNumeric: "tabular-nums" }}>{nf.format(v)}</text>
            </g>
          ))}
          {xTicks.map((a) => (
            <text key={a} x={g.x(a)} y={H - 8} textAnchor="middle" fontSize={11} fill="var(--muted)">{a}h</text>
          ))}
          {tracks.map((t, i) => {
            const pts = t.points.filter((p) => p.ageH <= g.xMax);
            if (!pts.length) return null;
            const d = pts.map((p, j) => `${j ? "L" : "M"}${g.x(p.ageH).toFixed(1)},${g.y(p.views).toFixed(1)}`).join("");
            const last = pts[pts.length - 1];
            return (
              <g key={t.id}>
                <path d={d} fill="none" stroke={`var(--series-${i + 1})`} strokeWidth={2} strokeLinejoin="round" strokeLinecap="round" />
                <circle cx={g.x(last.ageH)} cy={g.y(last.views)} r={4} fill={`var(--series-${i + 1})`} stroke="var(--surface)" strokeWidth={2} />
              </g>
            );
          })}
          {age !== null && (
            <g pointerEvents="none">
              <line x1={hx} x2={hx} y1={M.top} y2={M.top + g.ih} stroke="var(--axis)" strokeWidth={1} />
              {tracks.map((t, i) => {
                const v = valueAt(t, age);
                return v === null ? null : <circle key={t.id} cx={hx} cy={g.y(v)} r={4} fill={`var(--series-${i + 1})`} stroke="var(--surface)" strokeWidth={2} />;
              })}
            </g>
          )}
        </svg>
        {age !== null && (
          <div className="tip" style={hx > w / 2 ? { right: w - hx + 10 } : { left: hx + 10 }}>
            <div className="head">{nf.format(age)} h od objave</div>
            {tracks.map((t, i) => {
              const v = valueAt(t, age);
              return (
                <div className="row" key={t.id}>
                  <i className="key" style={{ background: `var(--series-${i + 1})` }} />
                  <strong>{v === null ? "—" : nf.format(v)}</strong>
                  <span>{label(t)}</span>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </>
  );
}
