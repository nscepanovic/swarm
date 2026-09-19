#!/usr/bin/env python3
"""
Trazi trendove u koje HiveBits moze da se ukljuci, i javlja na Telegram.

    python3 infra/x_trends.py            # proveri i posalji
    python3 infra/x_trends.py --dry-run  # samo ispisi, bez slanja i bez stanja

Trend ovde znaci: ljudi ucestvuju tako sto QUOTE-uju post ("I like solana",
"I'm all in on Solana"). Znak za to je mnogo quote-ova, i u apsolutnom broju
i u odnosu na lajkove. Obican post sa puno lajkova nije trend.

Nalozi i pragovi su u content/trends.json. Jedan request po nalogu.
Svaki trend se javlja tacno jednom (content/.trend_state.json).
Uz to belezi koliko je RapidAPI requestova ostalo u mesecu i upozori kad je malo.
"""
import json, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from x_fetch import ROOT, full_text, resolve_id, unwrap, user_of, walk_entries
import notify

CONFIG = ROOT / "content" / "trends.json"
STATE = ROOT / "content" / ".trend_state.json"
LOW_BUDGET = 150


def read_env():
    env = {}
    for line in (ROOT / ".env").read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def call(path, params, key, host):
    """Kao x_fetch.api, ali vraca i koliko je requestova ostalo."""
    url = f"https://{host}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"x-rapidapi-key": key, "x-rapidapi-host": host})
    with urllib.request.urlopen(req, timeout=45) as r:
        left = r.headers.get("x-ratelimit-requests-remaining")
        return json.loads(r.read().decode()), (int(left) if left and left.isdigit() else None)


def candidates(payload, handle, cfg, now):
    items, _ = walk_entries(payload)
    out = []
    for it in items:
        tw = unwrap(it)
        if not tw:
            continue
        lg = tw.get("legacy", {})
        if lg.get("retweeted_status_result") or lg.get("in_reply_to_status_id_str"):
            continue
        if (user_of(tw).get("handle") or "").lower() != handle.lower():
            continue
        age = (now - parsedate_to_datetime(lg["created_at"])).total_seconds() / 3600
        if age > cfg["window_hours"]:
            continue
        quotes, likes = lg.get("quote_count", 0), max(lg.get("favorite_count", 0), 1)
        if quotes < cfg["min_quotes"] or quotes / likes < cfg["min_quote_ratio"]:
            continue
        out.append({
            "id": lg["id_str"], "handle": handle, "text": full_text(tw, lg),
            "quotes": quotes, "likes": lg.get("favorite_count", 0),
            "views": int(tw.get("views", {}).get("count") or 0), "age_h": age,
            "quoted_id": lg.get("quoted_status_id_str"),
        })
    return out


def message(t):
    text = t["text"] if len(t["text"]) <= 280 else t["text"][:277] + "..."
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    lines = [
        "🔥 <b>Trend na X</b>",
        f"@{t['handle']}: {esc(text)}",
        f"{notify.fmt(t['quotes'])} quote-ova · {notify.fmt(t['likes'])} lajkova · "
        f"{notify.fmt(t['views'])} views · pre {t['age_h']:.0f}h",
        f"https://x.com/{t['handle']}/status/{t['id']}",
        "",
        "Ljudi ucestvuju tako sto quote-uju. Za predlog posta posalji botu: trend + link.",
    ]
    return "\n".join(lines)


def main():
    dry = "--dry-run" in sys.argv
    env = read_env()
    key, host = env["RAPIDAPI_KEY"], env.get("RAPIDAPI_X_HOST", "twitter241.p.rapidapi.com")
    token, chat = env.get("TELEGRAM_BOT_TOKEN"), env.get("TELEGRAM_CHAT_ID")
    cfg = json.loads(CONFIG.read_text())
    state = json.loads(STATE.read_text()) if STATE.exists() else {"sent": []}
    now = datetime.now(timezone.utc)

    found, left, cfg_changed = [], None, False
    for acc in cfg["accounts"]:
        if not acc.get("user_id"):
            acc["user_id"] = resolve_id(acc["handle"], key, host)
            cfg_changed = True
        payload, left = call("/user-tweets", {"user": acc["user_id"], "count": 20}, key, host)
        found += candidates(payload, acc["handle"], cfg, now)
    if cfg_changed and not dry:
        CONFIG.write_text(json.dumps(cfg, indent=2) + "\n")

    stamp = now.strftime("%Y-%m-%d %H:%M")
    print(f"{stamp}  kandidata: {len(found)}  RapidAPI preostalo: {left}")
    new = [t for t in sorted(found, key=lambda t: -t["quotes"]) if t["id"] not in state["sent"]]
    for t in new:
        print(f"  @{t['handle']} {t['quotes']}q {t['text'][:60]!r}")
        if not dry and notify.send(message(t), token, chat):
            state["sent"].append(t["id"])

    if left is not None and left < LOW_BUDGET and state.get("low_budget_warned") != now.strftime("%Y-%m"):
        print(f"  malo requestova: {left}")
        if not dry and notify.send(f"⚠️ RapidAPI: ostalo jos {left} requestova ovog meseca.", token, chat):
            state["low_budget_warned"] = now.strftime("%Y-%m")

    state["sent"] = state["sent"][-200:]
    state["rapidapi_left"], state["checked_at"] = left, stamp
    if not dry:
        STATE.write_text(json.dumps(state, indent=2) + "\n")


if __name__ == "__main__":
    main()
