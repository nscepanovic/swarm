#!/usr/bin/env python3
"""
Racuna agregate iz content/profiles/*/posts.jsonl i stampa markdown izvestaj.

    python3 infra/x_stats.py              # svi nalozi
    python3 infra/x_stats.py hivebits     # jedan

Postoji da agent NE bi racunao sam. Brojke se racunaju ovde, agent ih samo
tumaci. Sve sto agent tvrdi mora da se vidi u ovom izlazu.
"""
import json, re, statistics as st, sys
from collections import Counter, defaultdict
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = ROOT / "content" / "profiles"
MIN_VIEWS = 20      # ispod ovoga je sum
MIN_BUCKET = 4      # manje od ovoga nije obrazac nego slucajnost


def load(slug, kind="posts"):
    f = PROFILES / slug / f"{kind}.jsonl"
    rows = [json.loads(l) for l in f.read_text().splitlines() if l.strip()] if f.exists() else []
    return [r for r in rows if not r["is_retweet"] and r["views"] and r["views"] >= MIN_VIEWS]


def fmt_of(r):
    """Samo medij. Pozicija u threadu je zasebna dimenzija — vidi pos_of."""
    if "video" in r["media_types"]:
        return "video"
    if r["media_types"]:
        return "slika"
    return "samo tekst"


def pos_of(r):
    """Pocetak threada i nastavak threada su dve razlicite stvari.
    Nastavak je odgovor na sopstveni post: X ga skoro nikome ne prikazuje u
    feedu. Ako se mesaju u jednu kantu 'thread', nastavci obore medijanu i
    izgleda kao da threadovi ne rade."""
    if not r["in_self_thread"]:
        return "samostalan"
    return "thread: pocetak" if r["id"] == r["conversation_id"] else "thread: nastavak"


def len_of(r):
    c = r["chars"]
    return "<120" if c < 120 else "120-220" if c < 220 else "220-320" if c < 320 else "320+"


# Publika se cita iz content/audience-active-times.md, a taj grafikon je u
# CEST. Sati se zato ispisuju u obe zone, da se ne konvertuje napamet.
DAYS = ["pon", "uto", "sre", "cet", "pet", "sub", "ned"]


def _dt(r):
    return parsedate_to_datetime(r["created_at"])


def hour_of(r):
    h = _dt(r).hour
    return f"{h:02d}h UTC = {(h + 2) % 24:02d}h CEST"


def day_of(r):
    d = _dt(r)
    # +2h moze da prebaci post u sledeci dan po CEST-u
    return DAYS[((d.hour + 2) // 24 + d.weekday()) % 7]


# Teme. Gruba heuristika po kljucnim recima, prvi pogodak pobedjuje — da bi
# "teme po dosegu" bile reproducibilne, a ne procena agenta. Kad se doda nova
# linija sadrzaja, dodaj je ovde, inace pada u "ostalo".
TOPICS = [
    ("bee fact friday", r"bee fact friday"),
    ("dogadjaj / dokaz uzivo", r"\b(summit|booth|main stage|roadshow|hackathon|demo day|"
                              r"moneymotion|ethbelgrade|breakpoint|conference)\b"
                              r"|beehives are (officially )?here"),
    ("ICO / raise / token", r"\bico\b|\$nectar|\braise\b|\braising\b|oversubscrib"
                                r"|\bcontributions?\b|\brefund|\ballocation|\braise goal\b"
                                r"|hive is (already )?\d+%|\bpre-?sale\b"),
    ("proizvod / hardver", r"\bnode\b|\bhardware\b|\bsensors?\b|\bdevice\b|tokeniz"),
    ("intervju / citat osnivaca", "[“”\"]"),
    ("edukacija / odrzivost", r"did you know|\bhappy \w+ day\b|pesticide|biodiversity"
                              r"|\bplanet\b|sustainab|pollinat|apitherapy"),
]


def topic_of(r):
    t = r["text"].lower()
    for name, pattern in TOPICS:
        if re.search(pattern, t):
            return name
    return "ostalo"


def target_of(r):
    """Kome smo odgovorili, grupisano po velicini naloga."""
    f = r.get("reply_to_followers") or 0
    if f >= 100_000:
        return "odgovor nalogu 100k+"
    if f >= 10_000:
        return "odgovor nalogu 10-100k"
    return "odgovor nalogu <10k"


def replies_section(slug):
    # samo odgovori tudjim postovima; odgovori na sopstveni post su nastavci
    # threada i mere se gore, u tabeli "Po poziciji u threadu"
    rows = [r for r in load(slug, "replies") if r.get("is_reply_to_other")]
    out = ["**Odgovori tudjim postovima — kolika je vidljivost odgovora**", ""]
    if len(rows) < MIN_BUCKET:
        return out + [f"Samo {len(rows)} upotrebljivih odgovora — premalo za obrazac.", ""]
    out += [f"- odgovora u analizi: **{len(rows)}** | medijalni views: "
            f"**{st.median(r['views'] for r in rows):,.0f}**", ""]
    out += table(rows, target_of, "Odgovori po velicini naloga kome se odgovara")
    tgt = defaultdict(list)
    for r in rows:
        tgt[r.get("reply_to_handle") or "?"].append(r)
    out += ["**Odgovori po nalogu (samo oni sa n >= 3)**", "",
            "| nalog | n | med. views |", "|---|---:|---:|"]
    named = [(k, v) for k, v in tgt.items() if len(v) >= 3]
    for k, v in sorted(named, key=lambda kv: -st.median(x["views"] for x in kv[1])):
        out.append(f"| @{k} | {len(v)} | {st.median(x['views'] for x in v):,.0f} |")
    if not named:
        out.append("| — nijedan nalog nema 3+ odgovora | | |")
    out.append("")
    return out


def table(rows, keyfn, title, by_key=False):
    buckets = defaultdict(list)
    for r in rows:
        buckets[keyfn(r)].append(r)

    lines = [f"**{title}**", "", "| | n | med. views | med. bookmarks | med. replies |",
             "|---|---:|---:|---:|---:|"]
    order = (lambda kv: kv[0]) if by_key else (lambda kv: -st.median(x["views"] for x in kv[1]))
    for k, v in sorted(buckets.items(), key=order):
        mark = "" if len(v) >= MIN_BUCKET else " ⚠"
        lines.append(f"| {k}{mark} | {len(v)} | {st.median(x['views'] for x in v):,.0f} "
                     f"| {st.median(x['bookmarks'] for x in v):.1f} | {st.median(x['replies'] for x in v):.1f} |")
    lines.append("")
    return lines


def profile_report(slug):
    meta = json.loads((PROFILES / slug / "meta.json").read_text())
    rows = load(slug)
    out = [f"## @{meta['handle']}  ({meta.get('bucket')})", ""]
    if len(rows) < MIN_BUCKET:
        out += [f"Samo {len(rows)} upotrebljivih postova - premalo za obrazac.", ""]
        return out

    fol = meta.get("followers") or 1
    mv = st.median(r["views"] for r in rows)
    out += [
        f"- pratilaca: **{fol:,}** | postova u analizi: **{len(rows)}**",
        f"- medijalni views: **{mv:,.0f}** | **views po pratiocu: {mv/fol:.2f}**",
        f"- medijalno bookmarks: **{st.median(r['bookmarks'] for r in rows):.0f}** "
        f"| replies: **{st.median(r['replies'] for r in rows):.0f}**",
    ]
    days = max((max(_dt(r) for r in rows) - min(_dt(r) for r in rows)).days, 1)
    out += [f"- raspon: **{days} dana** ({min(_dt(r) for r in rows):%Y-%m-%d} → "
            f"{max(_dt(r) for r in rows):%Y-%m-%d}) | tempo: **{len(rows) / days * 7:.1f} "
            f"postova nedeljno**", ""]
    out += table(rows, fmt_of, "Po formatu (medij)")
    out += table(rows, pos_of, "Po poziciji u threadu")
    out += table(rows, lambda r: f"{pos_of(r)} + {fmt_of(r)}", "Pozicija × medij")
    # Nastavci threada su po pravilu kratki link-stubovi bez uredjivacke
    # odluke o duzini i temi. Da ne bi lazno oborili kantu "<120" i temu,
    # duzina i teme se racunaju bez njih.
    real = [r for r in rows if pos_of(r) != "thread: nastavak"]
    out += table(rows, len_of, "Po duzini teksta (SVE, ukljucujuci nastavke threada)")
    out += table(real, len_of, "Po duzini teksta (bez nastavaka threada — ovo koristi)")
    out += table(real, topic_of, "Po temi (bez nastavaka threada)")
    out += table(rows, hour_of, "Po satu objave (kad smo MI objavljivali, ne kad je publika budna)")
    out += table(rows, day_of, "Po danu objave (isto — kad smo mi objavljivali)")
    out += table(rows, lambda r: f"{_dt(r):%Y-%m}", "Po mesecu (da se trend razdvoji od nivoa)",
                 by_key=True)
    out += replies_section(slug)

    out += ["**Najbolji postovi (po views)**", ""]
    for r in sorted(rows, key=lambda r: r["views"], reverse=True)[:5]:
        out += [f"- `{r['views']:,}` views, `{r['bookmarks']}` bm, `{r['replies']}` repl "
                f"— {pos_of(r)} / {fmt_of(r)}, {r['chars']} zn. — {r['url']}",
                f"  > {r['text'][:260].strip()}", ""]
    # Bookmark je najposteniji signal kvaliteta (lajk je refleks), a ne mora
    # da ide uz views — zato zasebna lista, ne samo top po views.
    out += ["**Najvise bookmarkova (sta se cuva, a ne samo vidi)**", ""]
    for r in sorted(rows, key=lambda r: (-r["bookmarks"], -r["views"]))[:5]:
        out += [f"- `{r['bookmarks']}` bm na `{r['views']:,}` views "
                f"— {pos_of(r)} / {fmt_of(r)}, tema: {topic_of(r)} — {r['url']}",
                f"  > {r['text'][:200].strip()}", ""]
    out += ["**Najslabiji (isti format kao najbolji, da se vidi razlika)**", ""]
    for r in sorted(rows, key=lambda r: r["views"])[:3]:
        out += [f"- `{r['views']:,}` views — {pos_of(r)} / {fmt_of(r)}, {r['chars']} zn.",
                f"  > {r['text'][:180].strip()}", ""]
    return out


def main():
    slugs = sys.argv[1:] or sorted(p.name for p in PROFILES.iterdir() if (p / "posts.jsonl").exists())
    out = ["# X analiza — sirovi agregati", "",
           f"Prag: >= {MIN_VIEWS} views, retweetovi izbaceni. ⚠ = uzorak manji od {MIN_BUCKET}, ne zakljucuj iz njega.",
           "", "## Uporedna tabela", "",
           "| nalog | pratioci | n | med. views | views/pratilac | med. bm |",
           "|---|---:|---:|---:|---:|---:|"]
    for s in slugs:
        m = json.loads((PROFILES / s / "meta.json").read_text())
        rows = load(s)
        if not rows:
            continue
        fol = m.get("followers") or 1
        mv = st.median(r["views"] for r in rows)
        out.append(f"| @{m['handle']} | {fol:,} | {len(rows)} | {mv:,.0f} | **{mv/fol:.2f}** "
                   f"| {st.median(r['bookmarks'] for r in rows):.0f} |")
    out += ["", "_views/pratilac je jedina metrika koja se sme porediti izmedju naloga_", ""]
    for s in slugs:
        out += profile_report(s)
    print("\n".join(out))


if __name__ == "__main__":
    main()
