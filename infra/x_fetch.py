#!/usr/bin/env python3
"""
Povlaci tweetove sa X preko RapidAPI (twitter241) i pise normalizovan JSONL.

    python3 infra/x_fetch.py                 # svi nalozi iz profiles.json
    python3 infra/x_fetch.py hivebits        # samo jedan slug
    python3 infra/x_fetch.py --max 200       # dublji backfill

Ulaz:  content/profiles.json
Izlaz: content/profiles/<slug>/posts.jsonl   (jedan tweet po liniji)
       content/profiles/<slug>/meta.json     (followers, kad je povuceno)

Agent NIKAD ne zove ovo direktno u petlji - ovo je cisto I/O, bez AI.
"""
import json, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "content" / "profiles.json"
OUTDIR = ROOT / "content" / "profiles"
PAGE_SIZE = 20          # sto API vraca po requestu
RATE_SLEEP = 0.25       # 5 req/s hard limit na Basic planu
DEFAULT_MAX = 100

requests_used = 0


def load_env():
    env = {}
    envfile = ROOT / ".env"
    if envfile.exists():
        for line in envfile.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    key = os.environ.get("RAPIDAPI_KEY") or env.get("RAPIDAPI_KEY")
    host = os.environ.get("RAPIDAPI_X_HOST") or env.get("RAPIDAPI_X_HOST", "twitter241.p.rapidapi.com")
    if not key:
        sys.exit("RAPIDAPI_KEY nije nadjen (ni u okruzenju ni u swarm/.env)")
    return key, host


def api(path, params, key, host):
    global requests_used
    url = f"https://{host}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "x-rapidapi-key": key,
        "x-rapidapi-host": host,
        "Content-Type": "application/json",
    })
    time.sleep(RATE_SLEEP)
    requests_used += 1
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode())


# ---------------------------------------------------------------- parsiranje

def walk_entries(payload):
    """Timeline je ugnjezden GraphQL. Tweetovi sede na dva mesta:
    TimelineTimelineItem (samostalni post) i TimelineTimelineModule.items[]
    (thread / konverzacija). Vracamo i bottom cursor za paginaciju."""
    tweets, cursor = [], None
    result = payload.get("result", payload)
    timeline = result.get("timeline") or result.get("timeline_v2", {}).get("timeline") or {}
    for instr in timeline.get("instructions", []):
        entries = instr.get("entries") or []
        if instr.get("type") == "TimelineAddToModule":
            entries = instr.get("moduleItems") or []
        for entry in entries:
            content = entry.get("content") or entry.get("item") or {}
            etype = content.get("entryType") or content.get("__typename")
            if etype == "TimelineTimelineCursor":
                if content.get("cursorType") == "Bottom":
                    cursor = content.get("value")
            elif etype == "TimelineTimelineItem":
                tweets.append(content.get("itemContent", {}))
            elif etype == "TimelineTimelineModule":
                for it in content.get("items", []):
                    tweets.append(it.get("item", {}).get("itemContent", {}))
    return [t for t in tweets if t.get("itemType") == "TimelineTweet"], cursor


def unwrap(item_content):
    r = item_content.get("tweet_results", {}).get("result", {})
    if r.get("__typename") == "TweetWithVisibilityResults":
        r = r.get("tweet", {})
    return r if r.get("__typename") == "Tweet" else None


def user_of(tweet):
    u = tweet.get("core", {}).get("user_results", {}).get("result", {})
    legacy = u.get("legacy", {})
    return {
        "id": u.get("rest_id"),
        # screen_name je u novijim odgovorima izvan legacy - gledamo oba
        "handle": u.get("core", {}).get("screen_name") or legacy.get("screen_name"),
        "followers": (u.get("legacy", {}) or {}).get("followers_count"),
    }


def full_text(tweet, legacy):
    """Postovi duzi od 280 karaktera dolaze u note_tweet, a legacy.full_text
    je onda odsecen. Bez ovoga svaki duzi post ulazi u analizu kao krnj."""
    note = (tweet.get("note_tweet", {})
                 .get("note_tweet_results", {})
                 .get("result", {}))
    return note.get("text") or legacy.get("full_text", "")


def normalize(tweet, target_id):
    legacy = tweet.get("legacy", {})
    if not legacy:
        return None
    if legacy.get("user_id_str") != target_id:
        return None  # tudji tweet uvucen kroz konverzaciju

    text = full_text(tweet, legacy)
    ents = legacy.get("entities", {})
    media = (legacy.get("extended_entities", {}).get("media")
             or ents.get("media") or [])
    views = tweet.get("views", {}).get("count")
    views = int(views) if views and str(views).isdigit() else None

    likes = legacy.get("favorite_count", 0)
    replies = legacy.get("reply_count", 0)
    reposts = legacy.get("retweet_count", 0)
    quotes = legacy.get("quote_count", 0)
    bookmarks = legacy.get("bookmark_count", 0)

    def rate(n):
        return round(n / views, 5) if views else None

    user = user_of(tweet)
    return {
        "id": legacy.get("id_str"),
        "url": f"https://x.com/{user['handle']}/status/{legacy.get('id_str')}",
        "created_at": legacy.get("created_at"),
        "text": text,
        "lang": legacy.get("lang"),
        "chars": len(text),

        "is_reply": bool(legacy.get("in_reply_to_status_id_str")),
        "is_retweet": "retweeted_status_result" in tweet or text.startswith("RT @"),
        "is_quote": bool(legacy.get("is_quote_status")),
        "in_self_thread": bool(legacy.get("self_thread")),
        "conversation_id": legacy.get("conversation_id_str"),

        "media_types": sorted({m.get("type") for m in media if m.get("type")}),
        "has_link": bool(ents.get("urls")),
        "hashtags": [h.get("text") for h in ents.get("hashtags", [])],
        "mentions": [m.get("screen_name") for m in ents.get("user_mentions", [])],

        "views": views,
        "likes": likes,
        "replies": replies,
        "reposts": reposts,
        "quotes": quotes,
        "bookmarks": bookmarks,

        # apsolutni brojevi se ne mogu porediti izmedju naloga razlicite
        # velicine - samo ovi racio brojevi smeju u analizu
        "engagement_rate": rate(likes + replies + reposts + quotes + bookmarks),
        "community_rate": rate(replies + bookmarks + quotes),

        "author_followers": user.get("followers"),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


# ---------------------------------------------------------------- fetch

def resolve_id(handle, key, host):
    data = api("/user", {"username": handle}, key, host)
    u = (data.get("result", {}).get("data", {}).get("user", {}).get("result")
         or data.get("result", {}).get("user", {}).get("result")
         or {})
    rid = u.get("rest_id")
    if not rid:
        sys.exit(f"Ne mogu da razresim handle @{handle}. Odgovor: {json.dumps(data)[:400]}")
    return rid


def fetch_profile(entry, key, host, max_tweets):
    slug, handle = entry["slug"], entry["handle"]
    uid = entry.get("user_id") or resolve_id(handle, key, host)
    entry["user_id"] = uid  # kesiramo, lookup se ne placa dvaput

    collected, cursor, followers = {}, None, None
    while len(collected) < max_tweets:
        params = {"user": uid, "count": PAGE_SIZE}
        if cursor:
            params["cursor"] = cursor
        payload = api("/user-tweets", params, key, host)
        items, cursor = walk_entries(payload)
        if not items:
            break
        before = len(collected)
        for it in items:
            tw = unwrap(it)
            if not tw:
                continue
            rec = normalize(tw, uid)
            if rec:
                collected[rec["id"]] = rec
                followers = followers or rec.get("author_followers")
        if len(collected) == before or not cursor:
            break

    outdir = OUTDIR / slug
    outdir.mkdir(parents=True, exist_ok=True)

    # merge sa postojecim: stare metrike se prepisuju novim (tweet stari,
    # brojke rastu), stari tweetovi van ovog prozora ostaju
    posts = outdir / "posts.jsonl"
    merged = {}
    if posts.exists():
        for line in posts.read_text().splitlines():
            if line.strip():
                old = json.loads(line)
                merged[old["id"]] = old
    merged.update(collected)
    mark_threads(merged)
    ordered = sorted(merged.values(), key=lambda r: int(r["id"]), reverse=True)
    posts.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in ordered) + "\n")

    (outdir / "meta.json").write_text(json.dumps({
        "slug": slug, "handle": handle, "user_id": uid,
        "bucket": entry.get("bucket", "benchmark"),
        "followers": followers,
        "total_posts_stored": len(merged),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }, indent=2) + "\n")

    print(f"  @{handle:<20} novih/azuriranih: {len(collected):>3}   ukupno u fajlu: {len(merged):>4}   followers: {followers}")


def walk_modules(payload):
    """Kao walk_entries, ali cuva grupisanje po modulu. Za /user-replies je
    bitno: modul je [tweet na koji se odgovara, nas odgovor], pa iz redosleda
    unutar grupe vadimo kome je odgovoreno."""
    groups, cursor = [], None
    result = payload.get("result", payload)
    timeline = result.get("timeline") or result.get("timeline_v2", {}).get("timeline") or {}
    for instr in timeline.get("instructions", []):
        for entry in instr.get("entries", []) or []:
            content = entry.get("content", {})
            etype = content.get("entryType") or content.get("__typename")
            if etype == "TimelineTimelineCursor":
                if content.get("cursorType") == "Bottom":
                    cursor = content.get("value")
            elif etype == "TimelineTimelineItem":
                ic = content.get("itemContent", {})
                if ic.get("itemType") == "TimelineTweet":
                    groups.append([ic])
            elif etype == "TimelineTimelineModule":
                items = [it.get("item", {}).get("itemContent", {}) for it in content.get("items", [])]
                items = [i for i in items if i.get("itemType") == "TimelineTweet"]
                if items:
                    groups.append(items)
    return groups, cursor


def fetch_replies(entry, key, host, max_replies):
    """Odgovori drugima. /user-tweets ih uopste ne vraca, a za rast community-ja
    su najvazniji - to je mehanizam kojim mali nalog dolazi do tudje publike."""
    slug, uid = entry["slug"], entry["user_id"]
    collected, cursor = {}, None
    while len(collected) < max_replies:
        params = {"user": uid, "count": PAGE_SIZE}
        if cursor:
            params["cursor"] = cursor
        groups, cursor = walk_modules(api("/user-replies", params, key, host))
        if not groups:
            break
        before = len(collected)
        for group in groups:
            parsed = [unwrap(i) for i in group]
            for idx, tw in enumerate(parsed):
                if not tw:
                    continue
                rec = normalize(tw, uid)
                if not rec or not rec["is_reply"]:
                    continue
                parent = next((p for p in reversed(parsed[:idx]) if p), None)
                if parent:
                    pu = user_of(parent)
                    plg = parent.get("legacy", {})
                    rec["reply_to_handle"] = pu.get("handle")
                    rec["reply_to_followers"] = pu.get("followers")
                    rec["reply_to_text"] = full_text(parent, plg)[:400]
                    rec["reply_to_likes"] = plg.get("favorite_count")
                rec["is_reply_to_other"] = rec.get("reply_to_handle", "").lower() != entry["handle"].lower()
                collected[rec["id"]] = rec
        if len(collected) == before or not cursor:
            break

    out = OUTDIR / slug / "replies.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    merged = {}
    if out.exists():
        for line in out.read_text().splitlines():
            if line.strip():
                o = json.loads(line); merged[o["id"]] = o
    merged.update(collected)
    ordered = sorted(merged.values(), key=lambda r: int(r["id"]), reverse=True)
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in ordered) + "\n")
    others = sum(1 for r in merged.values() if r.get("is_reply_to_other"))
    print(f"  @{entry['handle']:<20} odgovora: {len(merged):>3}   od toga drugima: {others:>3}")


def mark_threads(records):
    """X-ov self_thread flag je nepouzdan - nastavak sopstvenog threada cesto
    stigne samo kao obican reply. Grupisemo po conversation_id: ako autor ima
    vise od jednog posta u istoj konverzaciji, to je thread, i numerisemo ga.
    Bitno jer je thread format koji se u analizi mora gledati kao celina."""
    from collections import defaultdict
    groups = defaultdict(list)
    for r in records.values():
        if not r["is_retweet"]:
            groups[r["conversation_id"]].append(r)
    for conv, rows in groups.items():
        rows.sort(key=lambda r: int(r["id"]))
        is_thread = len(rows) > 1
        for i, r in enumerate(rows, 1):
            r["in_self_thread"] = is_thread
            r["thread_position"] = i if is_thread else None
            r["thread_length"] = len(rows) if is_thread else None
            # odgovor nekom drugom, a ne nastavak sopstvenog threada
            r["is_reply_to_other"] = r["is_reply"] and not is_thread and conv != r["id"]


def main():
    args = [a for a in sys.argv[1:]]
    skip_replies = "--no-replies" in args
    if skip_replies:
        args.remove("--no-replies")
    max_tweets = DEFAULT_MAX
    if "--max" in args:
        i = args.index("--max")
        max_tweets = int(args[i + 1])
        del args[i:i + 2]

    if not CONFIG.exists():
        sys.exit(f"Nema {CONFIG}. Napravi ga (vidi primer u README).")
    all_profiles = json.loads(CONFIG.read_text())
    selected = ([p for p in all_profiles if p["slug"] in args or p["handle"] in args]
                if args else all_profiles)
    if not selected:
        sys.exit(f"Nijedan profil ne odgovara: {args}")

    key, host = load_env()
    print(f"Povlacim {len(selected)} profil(a), do {max_tweets} tweetova po profilu\n")
    for p in selected:
        try:
            fetch_profile(p, key, host, max_tweets)   # upisuje user_id u p
            if not skip_replies:
                fetch_replies(p, key, host, max_tweets)
        except Exception as e:
            print(f"  @{p['handle']:<20} GRESKA: {type(e).__name__}: {e}")

    # selected drzi reference na objekte iz all_profiles, pa su kesirani
    # user_id vec unutra - snimamo ceo config nazad
    CONFIG.write_text(json.dumps(all_profiles, indent=2) + "\n")
    print(f"\nPotroseno requesta: {requests_used}  (Basic plan: 1000/mesec)")


if __name__ == "__main__":
    main()
