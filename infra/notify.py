#!/usr/bin/env python3
"""
Telegram obavestenja za praceje postova. Bez AI-ja, ciste provere brojki,
pa moze da radi na serveru bez ikakvog troska.

Salje se SAMO kad se nesto desi, i svaki alarm ide tacno jednom po postu.
Stanje se pamti u content/.alert_state.json.
"""
import json, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "content" / ".alert_state.json"
THRESHOLDS = [500, 1000, 2000, 5000, 10000, 25000, 50000]
STALL_MIN_AGE_H = 3      # pre ovoga post jos hvata zalet, nije stao
SUMMARY_AGE_H = 24


def load_state():
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except json.JSONDecodeError:
            pass
    return {}


def save_state(state):
    STATE.write_text(json.dumps(state, indent=2) + "\n")


def send(text, token, chat_id):
    if not token or not chat_id:
        return False
    data = urllib.parse.urlencode({
        "chat_id": chat_id, "text": text,
        "parse_mode": "HTML", "disable_web_page_preview": "false",
    }).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/sendMessage", data=data)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode()).get("ok", False)
    except Exception as e:
        print(f"  TG greska: {type(e).__name__}: {e}")
        return False


def fmt(n):
    return f"{n:,}".replace(",", ".") if isinstance(n, int) else str(n)


def check(by_post, token, chat_id, dry_run=False):
    """by_post: {post_id: [snapshot, ...]} sortirano po starosti."""
    state = load_state()
    sent = 0

    for pid, snaps in by_post.items():
        snaps = sorted(snaps, key=lambda s: s["age_h"])
        last = snaps[-1]
        seen = state.setdefault(pid, [])
        views = last["views"] or 0
        head = last["text"][:70].replace("\n", " ").strip()
        line = (f"@{last['handle']} · {last['age_h']:.1f}h\n"
                f"<i>{head}...</i>\n"
                f"{fmt(views)} views · {fmt(last['likes'])} likes · "
                f"{fmt(last['replies'])} repl · {fmt(last['bookmarks'])} bm\n"
                f"{last['url']}")
        alerts = []

        if "new" not in seen:
            alerts.append(("new", f"🆕 <b>Nov post je ziv</b>\n\n{line}"))

        for t in THRESHOLDS:
            key = f"views:{t}"
            if views >= t and key not in seen:
                alerts.append((key, f"📈 <b>Presao {fmt(t)} views</b>\n\n{line}"))

        if len(snaps) > 1 and last["age_h"] >= STALL_MIN_AGE_H and "stalled" not in seen:
            prev = snaps[-2]
            if (views - (prev["views"] or 0)) <= 0:
                dt = last["age_h"] - prev["age_h"]
                alerts.append(("stalled",
                    f"⏸ <b>Rast stao</b> (0 views za {dt:.1f}h)\n\n{line}"))

        if last["age_h"] >= SUMMARY_AGE_H and "summary24" not in seen:
            first = snaps[0]
            alerts.append(("summary24",
                f"📊 <b>Presek na 24h</b>\n\n{line}\n\n"
                f"Prvi snimak bio na {first['age_h']:.1f}h: {fmt(first['views'] or 0)} views"))

        for key, text in alerts:
            if dry_run:
                print(f"  [dry-run] {key}: {text.splitlines()[0]}")
                sent += 1
            elif send(text, token, chat_id):
                print(f"  TG poslato: {key} za {pid}")
                seen.append(key)
                sent += 1

    if not dry_run:
        save_state(state)
    return sent
