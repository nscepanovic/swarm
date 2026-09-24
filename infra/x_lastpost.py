#!/usr/bin/env python3
"""Poslednji sopstveni post, pratioci i broj postova za X naloge.

Za proveru da li je projekat ziv (konkurencija, Colosseum). Isti RapidAPI
kao x_fetch.py, 2 zahteva po nalogu. Mesecna kvota je zajednicka sa
serverskim pracenjem, pa ne proveravaj vise od nekoliko desetina naloga.

    python3 infra/x_lastpost.py handle1 handle2 ...
    python3 infra/x_lastpost.py --json handle1 ...
"""
import sys, json, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import x_fetch as xf

xf.RATE_SLEEP = 0.4


def check(handle, key, host):
    data = xf.api("/user", {"username": handle}, key, host)
    u = (data.get("result", {}).get("data", {}).get("user", {}).get("result")
         or data.get("result", {}).get("user", {}).get("result") or {})
    uid = u.get("rest_id")
    if not uid or u.get("__typename") == "UserUnavailable":
        return {"handle": handle, "status": "nalog ne postoji ili suspendovan"}
    leg = u.get("legacy", {})
    payload = xf.api("/user-tweets", {"user": uid, "count": 10}, key, host)
    items, _ = xf.walk_entries(payload)
    dates = []
    for it in items:
        t = (it.get("tweet_results") or {}).get("result") or {}
        t = t.get("tweet") or t
        lg = t.get("legacy", {})
        if lg.get("user_id_str") != uid or not lg.get("created_at"):
            continue  # retvitovi i tudji postovi se ne racunaju
        dates.append(dt.datetime.strptime(lg["created_at"], "%a %b %d %H:%M:%S %z %Y"))
    return {
        "handle": handle,
        "status": "ok",
        "last_post": max(dates).strftime("%Y-%m-%d") if dates else None,
        "followers": leg.get("followers_count") or u.get("followers_count"),
        "posts": leg.get("statuses_count"),
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        sys.exit(__doc__)
    key, host = xf.load_env()
    out = []
    for h in args:
        h = h.lstrip("@")
        try:
            out.append(check(h, key, host))
        except Exception as e:  # jedan los nalog ne rusi ostale
            out.append({"handle": h, "status": f"greska: {str(e)[:80]}"})
    if as_json:
        print(json.dumps(out, indent=1, ensure_ascii=False))
    else:
        for r in out:
            print(f"@{r['handle']}\t{r.get('last_post') or r['status']}\t{r.get('followers','')}\t{r.get('posts','')}")
    print(f"# RapidAPI zahteva: {xf.requests_used}", file=sys.stderr)


if __name__ == "__main__":
    main()
