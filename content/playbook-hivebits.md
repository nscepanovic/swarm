# Playbook — @hivebits_io

Izvor: `python3 infra/x_stats.py hivebits`, stanje 2026-09-17.
Uzorak: 133 posta (>=20 views, bez RT), 2026-02-09 → 2026-09-16, tempo 4.3
posta nedeljno. 5.921 pratilaca, medijalno **366 views = 0.06 po pratiocu**,
medijalno **0 bookmarkova**.

Svaka brojka ispod se vidi u izlazu `x_stats.py`. Kad se podaci osveze,
pusti skriptu ponovo i prepisi ovaj fajl — ne dopunjuj ga napamet.

---

## 0. Merenje je ispravljeno — stari zakljucak o threadovima je bio pogresan

`x_stats.py` je do sada gurao svaki post u threadu u jednu kantu "thread".
Ta kanta je mesala dve razlicite stvari: **pocetak threada** (post koji ide u
feed) i **nastavak threada** (odgovor na sopstveni post, koji X skoro nikome
ne prikazuje). Sada su razdvojeni i slika se okrece:

| pozicija | n | med. views | med. bm | med. repl |
|---|---:|---:|---:|---:|
| thread: pocetak | 28 | **1.051** | 0.0 | 5.0 |
| samostalan | 56 | 364 | 0.0 | 2.0 |
| thread: nastavak | 49 | **197** | 0.0 | 0.0 |

Pocetak threada je **najjaci** format na nalogu, a ne najslabiji. Ono sto
pada je nastavak. Isti odnos vidi se na svakom merenom nalogu:
@ripcarsio 1.993 → 388, @SuperteamBLKN 2.070 → 228, @JurassicFi 16.108 → 2.874.

**Oprez sa uzrocnoscu:** pocetke threada koristimo za velike objave (ICO,
milestone), a samostalne postove za sve ostalo. Podaci ne mogu da razdvoje
"format vuce" od "u tom formatu objavljujemo vaznije stvari". Sto NE vazi za
nastavke — tamo je nalaz cist: 49 nastavaka, medijalno 197 views, **0
bookmarkova, 0 odgovora**, bez ijednog izuzetka gore od 1.000 views.

---

## 1. Format — rangirano

Pozicija × medij, ceo uzorak:

| | n | med. views | med. bm |
|---|---:|---:|---:|
| pocetak threada + slika | 16 | **1.066** | 0.5 |
| pocetak threada + video | 10 | **1.044** | 0.0 |
| pocetak threada + samo tekst ⚠ | 2 | 950 | 1.0 |
| samostalan + samo tekst | 20 | 480 | 0.0 |
| samostalan + video | 10 | 446 | 1.0 |
| samostalan + slika | 26 | 332 | 0.0 |
| nastavak threada + tekst | 47 | **198** | 0.0 |

Samo medij, bez pozicije: video 830 (n=20), slika 364 (n=44), tekst 329 (n=69).

**Pravila:**
1. Post koji nosi vest ide kao **pocetak threada sa medijem**. Nastavak sme da
   postoji, ali se ne racuna kao post i u njega se ne stavlja nista sto mora
   da se vidi.
2. **Link ide u glavni post, ne u nastavak.** Tri najslabija posta na nalogu
   su tacno to: `Learn more about the raise ↓` (45 views),
   `Explore the hive, the hardware, and the token ↓` (47),
   `@0xBeeSmart @futarddotio Learn more on $NECTAR ↓` (61).
3. Ako je izbor izmedju slike i videa na pocetku threada — svejedno je
   (1.066 vs 1.044). Biraj po materijalu, ne po formatu.
4. Samostalan post sa slikom je najslabiji od svega sto nije nastavak (332,
   n=26). To je najveci pojedinacni format na nalogu i najlosije radi.

---

## 2. Duzina teksta

Merena bez nastavaka threada — nastavak je link-stub, nema uredjivacku odluku
o duzini i lazno je obarao kantu `<120`:

| | n | med. views |
|---|---:|---:|
| 120-220 zn. | 21 | **795** |
| 220-320 zn. | 25 | **767** |
| <120 zn. | 22 | 433 |
| 320+ zn. | 16 | **250** |

**Ciljaj 120-320 znakova.** 120-220 i 220-320 su prakticno izjednaceni, ne
cepaj dlaku izmedju njih. Ispod 120 gubi se pola dosega; preko 320 znakova je
najgora kanta na nalogu (250 views, n=16) — duga forma na ovom nalogu ne radi.

Ispravka ranijeg zakljucka: nije tacno da je "polovina izlaza ispod 120
znakova". 66 od 133 posta jesu ispod 120, ali 44 od njih su nastavci threada.
Stvarnih kratkih postova ima 22.

---

## 3. Hook — prva linija

Prve linije pet najgledanijih postova, doslovno:

- `The $NECTAR ICO is now live on @futarddotio` — 24.456 views, 12 bm
- `Tokenized beehives are coming to @Solana 🐝` — 20.672, 9 bm
- `Why did we choose to tokenize beehives on @Solana? 🍯` — 18.194, 4 bm
- `We asked the @solana community to fund a bee farm.` — 17.277, 4 bm
- `Raise goal reached in 1 day and 3 hours 🐝` — 12.812, 3 bm

Sto im je zajednicko, mereno na ovih pet: svaka je **cela recenica o promeni
stanja**, sa subjektom i glagolom, bez uvoda. Cetiri od pet imaju `@Solana`
ili `@futarddotio` u prvoj liniji. Nijedna ne pocinje pridevom, pozivom na
akciju ni pitanjem publici (jedino pitanje je "why did we", pitanje o nama).

Prve linije koje su izmereno pale: `Learn more about the raise ↓`,
`Explore the hive, the hardware, and the token ↓`, `Link:`, `gm` (612),
`Regarding recent news` (185).

**Pravilo:** prva linija sama mora da prenese vest. Ako se iz nje ne vidi sta
se desilo, post ne ide.

---

## 4. Vreme objave

Izvor je `content/audience-active-times.md` (X analytics, kad je publika
budna). Satnice su CEST/UTC+2 — potvrdjeno. `x_stats.py` tabela "po satu
objave" meri kad smo MI objavljivali i ne nadjacava ovaj izvor; sada ispisuje
obe zone da nema konverzije napamet.

- **Prvi termin: ponedeljak 18-19h ili 21-23h CEST** (16-17h / 19-21h UTC).
- **Drugi termin: utorak 13-16h ili 21-22h CEST** (11-14h / 19-20h UTC).
- Vecernji pojas **18-23h CEST** radi kroz celu radnu nedelju.
- **Nikad pre 12h CEST.** Mrtvo doba je 01-11h CEST.

Sta o tome kazu nase brojke, i gde se ne slazu:

- **Slazu se po satu.** Nas najbolji sat sa upotrebljivim uzorkom je
  17h UTC = **19h CEST** (n=12, med. 548) — tacno u pojasu koji analytics
  oznacava kao najsvetliji. Najveca kanta nam je 16h UTC = 18h CEST (n=30,
  med. 381), takodje unutar pojasa ali slabija od 19h.
- **Ne slazu se po danu.** Analytics kaze da je ponedeljak ubedljivo najjaci
  dan. Nasa tabela po danu daje ponedeljak na 332 views (n=24), ispod naseg
  sopstvenog medijana, a nedelju na 653 (n=13). **Veruj analytics-u** —
  nasa tabela meri sta smo objavljivali ponedeljkom (rutinski postovi tokom
  ICO nedelja), ne koliko publike ima ponedeljkom.
- **Izmeren promasaj:** 16 postova je objavljeno u 10-11h CEST (08h UTC n=11
  med. 346, 09h UTC n=5 med. 348) — usred mrtvog doba publike.

---

## 5. Teme, rangirane po dosegu

Bez nastavaka threada. Klasifikacija je po kljucnim recima u `x_stats.py`
(`TOPICS`) — ako uvedes novu liniju sadrzaja, dodaj je tamo, inace pada u
"ostalo".

| tema | n | med. views | med. bm | med. repl |
|---|---:|---:|---:|---:|
| ICO / raise / token | 14 | **2.958** | 1.0 | 9.0 |
| dogadjaj / dokaz uzivo | 5 | 1.312 | 1.0 | 12.0 |
| intervju / citat osnivaca | 7 | 1.045 | 0.0 | 4.0 |
| proizvod / hardver | 11 | 516 | 0.0 | 3.0 |
| ostalo | 32 | 404 | 0.0 | 2.0 |
| edukacija / odrzivost | 8 | 314 | 0.0 | 2.0 |
| bee fact friday | 7 | **254** | 0.0 | 1.0 |

Raspon od vrha do dna je 12x. Dogadjaj sa dokazom ima najvise odgovora po
postu (12) od svih tema — to je tema koja pravi razgovor, ne samo doseg.

---

## 6. Anti-obrasci — izmereno palo

1. **Nastavak threada kao nosilac informacije.** n=49, med. 197 views, 0 bm,
   0 odgovora. 37% svega sto objavljujemo zavrsi ovde. Ako ubrojis samo
   postove koji stvarno idu u feed, nas tempo nije 4.3 nego oko 2.7 nedeljno.
2. **"Bee Fact Friday".** 7 postova, med. 254 views, **0 bookmarkova kroz
   celu seriju**. Najslabija tema na nalogu. Serija se gasi ili se menja iz
   korena — u sadasnjem obliku je cist trosak.
3. **Edukacija / odrzivost bez nas u kadru.** n=8, med. 314. Praznicni i
   opsti postovi (`Happy Earth Day`, `Happy World Apitherapy Day`,
   `Happy Birthday, Solana!` 142 views) ne rade.
4. **Preko 320 znakova.** n=16, med. 250 — najgora kanta po duzini.
5. **Samostalan post sa slikom.** n=26, med. 332. Najveci pojedinacni format,
   ispod medijana naloga.
6. **Odgovori kao kanal.** 45 odgovora tudjim postovima, medijalno **39
   views**. Po velicini naloga kome se odgovara: <10k → **40** views (n=32),
   10-100k → 39 (n=7), 100k+ → 30 (n=6). Stojeca odluka da se ne odgovara
   velikim nalozima se potvrdjuje (30 views), ali se mora prosiriti:
   **odgovori nisu distribucija ni unutar ekosistema.** Razlike izmedju te
   tri kante prakticno nema — 40 i 30 views su oba nula. Ako se odgovara,
   odgovara se zbog odnosa sa tim nalogom, ne zbog dosega.
7. **Bookmarkovi.** Medijana naloga je 0 kroz 133 posta. Sva tri posta sa
   najvise bookmarkova su tema `ICO / raise / token` i sva tri su pocetak
   threada sa medijem: 12 bm / 24.456 views, 9 bm / 20.672, i — najvazniji —
   **7 bm na samo 3.851 views**, najbolji odnos cuvanja na nalogu:
   `What if you could own a piece of a real beekeeping operation - onchain?
   We generated $200K+ in revenue from beekeeping.`
   Ljudi cuvaju **ponudu izrecenu kao ponuda**, ne fakte o pcelama. To je
   jedini post koji je nadmasio svoj doseg po cuvanju i vredi ga ponoviti u
   varijacijama.

---

## 7. Referentni nalog: @JurassicFi

Najblizi uporediv nalog: 6.837 pratilaca prema nasih 5.921. Isti ekosistem,
isti tip proizvoda (RWA na Solani), ista mehanika (ICO). Razlika u jedinoj
uporedivoj metrici: **3.52 views po pratiocu prema nasih 0.06 — 59x.**

Kontrola da to nije efekat razlicitih perioda: po mesecima, u septembru 2026
@JurassicFi ima medijalno 11.298 views (n=8), mi 603 (n=65). Po pratiocu je
to 1.65 prema 0.10 — jaz ostaje ~16x i u istom mesecu, na nasem najboljem
mesecu. Problem je **distribucija**, ne kvalitet: nas engagement po vidjenom
postu nije katastrofalan, ali post skoro niko ne vidi.

Sta rade konkretno drugacije:

| | @hivebits_io | @JurassicFi |
|---|---|---|
| tempo | 4.3 posta / nedelji | **1.5 posta / nedelji** |
| udeo nastavaka threada | 49 od 133 (37%) | 7 od 35 (20%) |
| video | 20 od 133 (15%), med. 830 | **13 od 35 (37%), med. 47.674** |
| najjaci format | pocetak threada + slika, 1.066 | **samostalan + slika/video, 47.785 / 47.674** |
| duzina 120-220 | 21 postova, med. 795 | 10 postova, med. **59.788** |
| med. bookmarks | **0** | **11** |
| odgovori tudjim postovima | 45, med. 39 views | **79, med. 180 views** |

Pet stvari koje iz ovoga ulaze u nas rad:

1. **Manje postova, veci postovi.** Oni objavljuju trecinu naseg tempa.
   Prazan post nije besplatan — trosi doseg sledeceg.
2. **Video je njihov glavni format, kod nas sporedni.** 37% njihovih postova
   je video (med. 47.674) prema nasih 15% (med. 830).
3. **Kod njih samostalan post nosi, kod nas pocetak threada.** Njihov
   samostalan post ima 42.209 med. views, nastavak 2.874 — isto pravilo kao
   kod nas, samo dosledno sprovedeno: manje nastavaka, vise tezine u glavnom
   postu.
4. **Imenovani protagonista.** U 4 od 5 njihovih najgledanijih postova
   pojavljuje se **"Deaton"**, ime konkretnog fosila:
   `You have waited enough.` (466.249),
   `Deaton is the first ever tokenized dinosaur fossil, launching on @Solana`
   (180.040), `Dinosaurs on @Solana 🦖` (153.901),
   `Introducing Deaton, a museum-grade Triceratops Prorsus skull with 60-65%
   complete bone mass and all 3 original horns intact` (149.314).
   Mi nemamo ime — imamo kolicinu ("300 beehives"). Ovo je zapazanje na 5
   postova, ne merenje: tretiraj ga kao hipotezu koju vredi probati, ne kao
   dokazano pravilo.
5. **Odgovori im rade 4.6x bolje nego nama** (180 prema 39 med. views), i
   odgovaraju skoro duplo vise (79 prema 45), pretezno malim nalozima
   (60 od 79 odgovora ide nalozima <10k). Ni kod njih to nije glavni kanal,
   ali je razlika prevelika da se ignorise.

**Sto NE preuzimati:** njihov najveci post (466.249 views) je jednokratni
dogadjaj — prvi tokenizovani dinosaurus. Mi nemamo ekvivalent i nema smisla
praviti se da imamo.

---

## 8. Gde podaci ne daju odgovor

- **Raid grupa u @SuperteamBLKN se ne vidi u podacima.** Nijedan post nije
  obelezen kao raidovan, pa se ne moze izmeriti koliko raid nosi. Dok se ne
  belezi koji je post isao uz raid, tvrdnja "raid je poluga za doseg" ostaje
  odluka, a ne merenje. **Ovo je jedan podatak koji bi najvise promenio
  analizu** — dovoljno je polje `raid: true` pri objavi.
- **Zasto pocetak threada nadmasuje samostalan post** — format ili izbor
  teme, vidi tacku 0. Razdvaja se samo eksperimentom: objaviti vest jednom
  kao samostalan post, bez nastavka, i uporediti.
- **"Ostalo" je 32 od 84 posta** (med. 404). Skoro 40% sadrzaja nema temu
  koju klasifikacija prepoznaje. Dok se `TOPICS` ne dopuni, rang tema je
  nepotpun.
- **Nijedan A/B test ne postoji.** Sve gore je posmatrano, ne eksperiment.
  Vreme objave, duzina i tema se menjaju zajedno sa vaznoscu vesti.
