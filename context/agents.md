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

## Telegram

Pisi botu `@hb_swarm_bot` kao sto pises ovde. Odgovara stalna Claude
sesija na serveru, sa istim pravilima i agentima.

- `desilo se: ...` upise u `content/news.md`, commit i push
- `novi materijal na Drive-u` zavede ga u indeks
- `post za danas` predlozi post iz playbook-a i news-a
- `pusti x-analyst` pokrene analizu

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
