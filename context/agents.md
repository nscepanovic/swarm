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

## Alati

Skripte bez AI-ja. Server ih pokrece sam; rucno samo kad treba.

- `x_fetch.py` povlaci postove i odgovore sa svih naloga iz `profiles.json`.
  Server: nedeljom 20h.
- `x_stats.py` racuna agregate za playbook. Koristi ga `x-analyst`.
- `x_track.py` prati krivu rasta svezih postova i salje Telegram alarme.
  Server: radnim danima 18-23h na sat, i svaki dan u 9h i 13h.
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
