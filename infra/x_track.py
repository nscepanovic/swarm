#!/usr/bin/env python3
"""
Prati svez post kroz vreme. Dopunjuje, ne prepisuje.

    python3 infra/x_track.py                  # snimi stanje + izvestaj
    python3 infra/x_track.py --days 3         # samo postovi mladji od 3 dana
    python3 infra/x_track.py --report         # samo izvestaj, bez API poziva

x_fetch.py prepisuje metrike pri svakom osvezavanju, pa se putanja gubi.
Ovaj skript dodaje red u content/tracking.jsonl pri svakom pokretanju, tako
da se vidi kako post raste. Bitno jer poredjenje sveze objavljenog posta sa
medijanom starih postova nije posteno - stari su imali mesece da nakupe views.
Ovde se poredi na ISTOJ STAROSTI.
"""
import json, sys, time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from x_fetch import (CONFIG, OUTDIR, api, load_env, normalize, unwrap,
                     walk_entries, PAGE_SIZE)
import notify

ROOT = Path(__file__).resolve().parent.parent
TRACK = ROOT / "content" / "tracking.jsonl"
CHECKPOINTS = [1, 3, 6, 12, 24, 48, 72, 168]   # sati


def age_hours(created_at, now=None):
    now = now or datetime.now(timezone.utc)
    return (now - parsedate_to_datetime(created_at)).total_seconds() / 3600


def snapshot(days, key, host):
    rows = []
    used = 0
    for entry in json.loads(CONFIG.read_text()):
        if entry.get("bucket") not in ("self", "hivebits"):
            continue
        uid = entry.get("user_id")
        if not uid:
            continue
        payload = api("/user-tweets", {"user": uid, "count": PAGE_SIZE}, key, host)
        used += 1
        items, _ = walk_entries(payload)
        now = datetime.now(timezone.utc)
        for it in items:
            tw = unwrap(it)
            if not tw:
                continue
            rec = normalize(tw, uid)
            if not rec or rec["is_retweet"]:
                continue
            h = age_hours(rec["created_at"], now)
            if h > days * 24:
                continue
            rows.append({
                "ts": now.isoformat(timespec="seconds"),
                "slug": entry["slug"], "handle": entry["handle"],
                "id": rec["id"], "url": rec["url"],
                "created_at": rec["created_at"], "age_h": round(h, 2),
                "views": rec["views"], "likes": rec["likes"],
                "replies": rec["replies"], "reposts": rec["reposts"],
                "bookmarks": rec["bookmarks"],
                "thread_position": rec.get("thread_position"),
                "chars": rec["chars"], "media": rec["media_types"],
                "text": rec["text"][:200],
            })
    with TRACK.open("a") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"snimljeno {len(rows)} postova, potroseno {used} requesta\n")
    return rows


def baseline(slug, target_age):
    """Koliko views ima tipican stari post ovog naloga u istoj starosti?
    Ne moze se izmeriti unazad (nemamo istoriju), pa se daje ukupni medijan
    kao gruba referenca, jasno obelezen kao takav."""
    import statistics as st
    f = OUTDIR / slug / "posts.jsonl"
    if not f.exists():
        return None
    rows = [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
    rows = [r for r in rows if not r["is_retweet"] and r["views"] and r["views"] >= 20
            and r.get("thread_position") != 2]
    return st.median(r["views"] for r in rows) if rows else None


def report():
    if not TRACK.exists():
        print("Nema jos snimaka. Pokreni bez --report da napravis prvi.")
        return
    rows = [json.loads(l) for l in TRACK.read_text().splitlines() if l.strip()]
    by_post = {}
    for r in rows:
        by_post.setdefault(r["id"], []).append(r)

    for pid, snaps in sorted(by_post.items(), key=lambda kv: kv[1][-1]["created_at"], reverse=True):
        snaps.sort(key=lambda r: r["age_h"])
        last = snaps[-1]
        print(f"@{last['handle']}  {last['url']}")
        print(f"  {last['text'][:90]!r}")
        print(f"  {'starost':>9} {'views':>8} {'likes':>7} {'repl':>6} {'bm':>5}")
        for s in snaps:
            print(f"  {s['age_h']:>7.1f}h {s['views'] or 0:>8,} {s['likes']:>7,} "
                  f"{s['replies']:>6,} {s['bookmarks']:>5,}")
        b = baseline(last["slug"], last["age_h"])
        if b and last["views"]:
            print(f"  medijan naloga (svih starosti, gruba referenca): {b:,.0f} views "
                  f"-> ovaj post je na {last['views']/b:.1f}x")
        if len(snaps) > 1:
            d = snaps[-1]["age_h"] - snaps[-2]["age_h"]
            dv = (snaps[-1]["views"] or 0) - (snaps[-2]["views"] or 0)
            print(f"  zadnji interval: +{dv:,} views za {d:.1f}h "
                  f"({'jos raste' if dv > 0 else 'stao'})")
        print()


def tg_creds():
    env = {}
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env.get("TELEGRAM_BOT_TOKEN"), env.get("TELEGRAM_CHAT_ID")


def grouped():
    if not TRACK.exists():
        return {}
    by = {}
    for line in TRACK.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            by.setdefault(r["id"], []).append(r)
    return by


def main():
    args = sys.argv[1:]
    days = 7
    if "--days" in args:
        i = args.index("--days"); days = float(args[i + 1]); del args[i:i + 2]
    quiet = "--quiet" in args          # za cron: bez izvestaja, samo TG
    dry = "--dry-run" in args

    if "--report" not in args:
        key, host = load_env()
        snapshot(days, key, host)

    if "--notify" in args or dry:
        token, chat = tg_creds()
        if not token or not chat:
            print("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID nisu u .env")
        else:
            n = notify.check(grouped(), token, chat, dry_run=dry)
            print(f"alarma poslato: {n}")

    if quiet:
        return
    report()
    nxt = ", ".join(f"{c}h" for c in CHECKPOINTS)
    print(f"Korisne tacke merenja posle objave: {nxt}")


if __name__ == "__main__":
    main()
