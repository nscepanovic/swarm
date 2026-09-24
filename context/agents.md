# Agenti i alati

Ovaj fajl cita swarm aplikacija (tab "Agenti"). Sekcija `## <ime-agenta>`
se prikazuje uz karticu tog agenta iz `.claude/agents/`. Kad dodas agenta,
dodaj mu i sekciju ovde.

## x-analyst

**Kad:** jednom nedeljno, najbolje ponedeljak ujutru, posle nedeljnog
refresha podataka (server ga radi nedeljom u 20h).

**Kako:** u bilo kojoj Claude sesiji (laptop, server, telefon) reci:

```
pusti x-analyst
```

Agent pokrene `x_stats.py`, procita `CLAUDE.md` i satnice publike, i
prepise oba playbook-a (`playbook-hivebits.md`, `playbook-personal.md`).

**Sta vraca:** 5-10 redova: najjaci nalaz, i gde podaci nisu dovoljni za
zakljucak. Ne izmislja brojke; svaka tvrdnja mora da se vidi u izlazu skripte.

## game-designer

**Kad:** kad imas novu ideju, inspiraciju ili feedback od developera igre.

**Kako:** "pusti game-designer" i napisi sta je novo. Slike inspiracije
stavi na Drive, u folder `hivebits/Swarm`.

**Sta vraca:** novu verziju `game/design.md`, unos u `game/iterations.md`,
i 3-5 redova: sta je promenjeno i koja pitanja ceka.

## secretary

**Kad:** kad Nemanja kaze "plan za danas", "sta imam ove nedelje" ili
"podseti me u 17h da ...".

**Kako:** u Telegramu, obicnim recima. Sesija upise podsetnik u
`content/reminders.json`; `infra/remind.py` (cron, svakih 5 minuta, bez AI-ja)
posalje poruku na Telegram kad dodje vreme.

**Sta vraca:** kratak plan (Danas / Ceka tebe / Sledece) iz `news.md`, nacrta i
podsetnika. Vremena daje Nemanja; predlozi se oznacavaju kao predlozi.
Kalendar se cita samo ako je Google Calendar konektor odobren u sesiji.

## Telegram

Pisi botu `@hb_swarm_bot` kao sto pises ovde. Odgovara stalna Claude
sesija na serveru, sa istim pravilima i agentima.

- `desilo se: ...` upise u `content/news.md`, commit i push
- `novi materijal na Drive-u` zavede ga u indeks
- `post za danas` predlozi post iz playbook-a i news-a
- `pusti x-analyst` pokrene analizu
- `podseti me u 17h da ...` upise podsetnik (agent `secretary`)
- `plan za danas` plan iz news.md, nacrta i podsetnika

Kad Claude trazi dozvolu za nesto, poruka stize sa dugmicima Allow / Deny.

## Alati

Skripte bez AI-ja. Server ih pokrece sam; rucno samo kad treba.

- `x_fetch.py` povlaci postove i odgovore sa svih naloga iz `profiles.json`.
  Server: nedeljom 20h.
- `x_trends.py` trazi trendove na @solana (postovi koje ljudi masovno
  quote-uju) i javi na Telegram. Server: svaki dan 8:30 i 17:30.
  Nalozi i pragovi su u `content/trends.json`.
- `x_stats.py` racuna agregate za playbook. Koristi ga `x-analyst`.
- `x_track.py` prati krivu rasta svezih postova i salje Telegram alarme.
  Server: jednom dnevno u 22h, samo postovi mladji od 3 dana (posle toga
  vise ne rastu bitno; ukupne brojke osvezi nedeljni x_fetch).
- `remind.py` salje podsetnike iz `content/reminders.json` na Telegram.
  Server: svakih 5 minuta.
- `server-sync.sh` salje prikupljene podatke nazad u git. Server: 13:40 i 23:40.

## Kako traziti od Claude-a

Obicnim recima, u bilo kojoj sesiji:

- `ima novog materijala na Drive-u` - zavede ga u indeks i predlozi post
- `kako stoji danasnji post` - kriva rasta i poredjenje sa prethodnim
- `napravi plan za sledecu nedelju` - predlog postova iz materijala
- `pusti x-analyst` - osvezi playbook-ove

## Uskoro

- `/x-post` - komanda koja pise predlog posta po playbook-u, u formatu
  koji ova aplikacija cita

## press

**Kad:** kad neko trazi press kit ili materijal za novinare.

**Kako:** reci `pusti press`. Agent cita samo javne postove, `news.md` i
dokumenta koja mu Nemanja da, i pise `content/press/press-kit.md`.

**Sta vraca:** kratak izvestaj: sta je u kitu, sta fali (lista "Treba od
Nemanje") i sta da proveri pre slanja. Svaka brojka, datum i mesto ima izvor;
bez izvora ide u listu onoga sto fali. Ne salje nista nikome.

## deck

**Kad:** priprema za Colosseum. Kad imas novu cinjenicu za pitch, kad je
deck u Slides-u promenjen i hoces misljenje, ili kad hoces novu verziju.

**Kako:** reci `pusti deck` i sta je novo. Agent cita `news.md`, tvoje
deckove sa Drive-a (Google Slides) i Colosseum Copilot za konkurenciju.

**Sta vraca:** `content/colosseum/deck.md` (tekst po slajdu, sa izvorom uz
svaku brojku), scenario pitch videa i listu pitanja za tebe. Kad trazis novu
verziju, pravi novi Slides fajl na Drive-u; tvoje fajlove ne menja. Sve je
interno dok ne kazes da je ideja javna.

## researcher

**Kad:** kad treba cinjenica o Colosseum-u (pobednici, propali projekti,
akcelerator) ili o trzistu (pcelinji proizvodi, susedni proizvodi), i kad
agent `deck` upise pitanje za njega u `open-questions.md`.

**Kako:** reci `pusti researcher` i sta treba. Koristi Colosseum Copilot
i web. Ne dira HiveBits brojke, samo tudje i trzisne.

**Sta vraca:** fajl u `content/colosseum/` (`winners-full.md`,
`competition.md`, `market.md`, `what-it-takes.md`) sa linkom uz svaku
brojku, i 5-8 redova: najjaci nalaz i sta nije proverio.

## Modeli po agentu (odluka 2026-09-24)

| Agent | Model | Zasto |
|---|---|---|
| deck | fable | Najskuplji ulog (pobeda, akcelerator). Najjaci model. |
| researcher | opus | Mnogo izvora, mora da razdvoji tvrdnju od cinjenice. |
| press | opus | Pise za novinara, verifikuje svaku cinjenicu. |
| game-designer | opus | Kreativan rad, nije hitan. |
| x-analyst | sonnet | Cita izlaz skripte i prepisuje playbook. |
| secretary | sonnet | Plan dana iz tri fajla. |

Menja se u frontmatteru agenta (`model:`), ovde je samo pregled.
