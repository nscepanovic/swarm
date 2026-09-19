# content/

Pipeline za X sadrzaj. Cetiri koraka, svaki se verifikuje pre sledeceg.

## 1. Povlacenje (bez AI)

`profiles.json` -> lista naloga. `bucket` je `self`, `hivebits` ili `ecosystem`.
`user_id` se sam upise pri prvom pokretanju i posle se ne placa ponovo.

    python3 infra/x_fetch.py                # svi nalozi, 100 tweetova
    python3 infra/x_fetch.py hivebits       # samo jedan
    python3 infra/x_fetch.py --max 300      # dublji backfill

Izlaz: `profiles/<slug>/posts.jsonl` + `meta.json`. Refresh azurira metrike
starih postova i dodaje nove; nista se ne gubi.

Kljucevi su u `swarm/.env` (chmod 600), nikad u ovim fajlovima.

## 2. Analiza -> playbook

Agent `x-analyst` cita `profiles/` i odrzava `playbook-personal.md` i
`playbook-hivebits.md`.

Agregate racuna `python3 infra/x_stats.py` — agent ih samo tumaci, ne racuna.

Pravilo: apsolutni brojevi se NE porede izmedju naloga razlicite velicine.
Jedina metrika koja se sme porediti izmedju naloga je **views po pratiocu**.
Drugo pravilo: pocetak threada i nastavak threada su razliciti formati i ne
smeju u istu kantu — pocetak ide u feed, nastavak skoro niko ne vidi.

## 3. Materijali

`materials/inbox/` -> sve sirovo: PDF, slike kosnica, sensor podaci, press.
Kad materijal izadje u postu, fajl se premesta u `materials/used/`.
Namerno premestanje fajla, a ne ledger - ledger se raziđe sa stvarnoscu.

## 4. Postovi

Svaki post je jedan `.md` fajl sa zaglavljem koje cita swarm aplikacija
(swarm.hivebits.io). Polja su obavezna, prazna vrednost je `""`:

    ---
    date: "2026-09-18"        # dan objave; "" dok nije odredjen
    time: "18:00"             # CEST
    account: "hivebits_io"    # ili "0xbeesmart"
    status: "draft"           # draft | approved | scheduled | published
    media: "Nemanja Clip #10.mp4"
    tweet_id: ""              # upisuje se kad post izadje; povezuje ga sa pracenjem
    title: "kratak opis"
    ---

Folder prati status: `drafts/`, `approved/` (i scheduled), `published/`.

### Stari opis toka

`posts/drafts/` -> `approved/` -> `published/`
`published/` nije arhiva reda radi: sprecava ponavljanje tema i vraca se
nazad u korak 2 kao podatak o tome sta je od naseg proslo.
