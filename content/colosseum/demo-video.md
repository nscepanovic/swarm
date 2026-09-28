# Demo video - scenario v2 (2026-09-28)

INTERNO. Colosseum trazi **demo video do 3 minuta** koji pokazuje
proizvod (colosseum.com/hackathon, hackathon.md). Zuri ocenjuje startap,
ne kod napisan u roku (Nemanja, 2026-09-28): demo je dokaz da proizvod
postoji, ne dokaz rada tokom takmicenja. Kriterijumi iz pravila koje demo
pokriva: (a) Functionality i (d) UX (kako blockchain pravi bolji UX).

**Proizvod u demo-u je kosnica, ne tegla** (v3). Demo pokazuje ono sto
postoji: kosnice sa farme uzivo i tok kupovine kosnice na lancu.

**Pravilo: sve sto se vidi mora da radi.** Nema mockupa, nema Figme, nema
"ovo ce raditi". Ako neki korak ne postoji do snimanja, izbacuje se iz
videa, ne glumi se.

Ciljna duzina: 2:30. Bez muzike preko glasa. Ekran plus Nemanjin glas;
Nemanja u kadru samo na pocetku i kraju. Kadar sa farme (kosnice, senzor
ispod kosnice) samo ako snimak postoji na Drive-u i zaveden je u
`materials/index.md`.

---

## Sta video pokazuje, redom

### 0:00-0:15 Uvod (Nemanja u kadru, ako moze kod kosnica)

"This is HiveBits. Beekeepers sell hives, not honey. I will show you a
real hive, live, and how you buy one. Everything you see here is running."

### 0:15-0:55 Kosnica uzivo

Ekran: stranica jedne kosnice sa nase farme, bez logovanja.

Koraci koji se vide:
1. Kosnica ima identitet: ID, pcelinjak, pcelar, datum postavljanja.
   `[lokacija se ne prikazuje dok Nemanja ne kaze]`
2. Zivi podaci sa senzora: tezina, temperatura, vlaga, sa grafikom za
   poslednje dane. Vreme poslednjeg ocitavanja se vidi.
3. Link na zapis kosnice na Solani (explorer).
4. Kratak rez: ista kosnica na terenu, senzor ispod nje (ako snimak
   postoji).

Glas: "This is one hive from our farm. It has an ID, a beekeeper and a
record on Solana. The sensor under it sends weight, temperature and
humidity. You see the colony working, right now. No wallet needed to
look."

`[koje kosnice imaju ziv senzor danas, i gde je dashboard: Nemanja, #8]`

### 0:55-1:45 Kupovina kosnice

Ekran: telefon ili laptop.

Koraci koji se vide:
1. Lista kosnica na prodaju (nase, ili pcelar iz mreze koji je pristao).
2. Kupac bira kosnicu: vidi cenu, sta dobija (med ili prinos), pcelara.
3. Placanje. `[kako kupac placa: novcanik (Phantom Connect), kartica,
   oba - #25]`
4. Potvrda: kupljena kosnica se pojavljuje u nalogu kupca, sa istim ID-jem
   i istim zivim podacima.
5. Transakcija na Solana exploreru: vlasnistvo ili zapis kupovine na
   lancu.

Glas: "Now you buy it. Pick a hive, see the price, the beekeeper and what
you get. Pay. The hive is yours, same ID, same live data, and the
purchase is on Solana. Here is the transaction."

### 1:45-2:10 Novac pcelaru

Ekran: nalog pcelara, pa explorer.

Koraci koji se vide:
1. Nalog pcelara pokazuje prodatu kosnicu i iznos u USDC (cena minus 5%,
   ili puna cena ako je 5% dodato kupcu).
2. Transakcija isplate na exploreru.
3. 5% HiveBits-a na posebnoj adresi.

Glas: "The beekeeper gets USDC for the hive, before the season. Here is
the transaction. Here is our 5%."

`[ako isplata ide kroz escrow, tako i reci; ne glumiti "instant" - #26]`
`[ako 5% ne vazi za kosnice, izbaciti tacku 3 - #33]`

### 2:10-2:25 Dokaz da je ovo vec prodato

Ekran: javni post ili futard.io stranica prodaje 300 kosnica.

Glas: "We did this first with our own 300 hives. Sold on MetaDAO in 27
hours. Now it is a platform, for every beekeeper."

Ovo nije demo koda, nego 10-15 sekundi dokaza. Ako zuri trazi demo
proizvoda samo, ovaj deo se skracuje na jednu recenicu.

### 2:25-2:40 Zavrsetak (Nemanja u kadru)

"A real hive, live data, bought on Solana, beekeeper paid. Code is at
[repo]. Thank you."

`[repo javan ili ne: #22]`

---

## Sta mora da postoji za ovaj video

| # | Funkcija | Kriterijum | Uslov za snimanje? |
|---|---|---|---|
| 1 | Javna stranica kosnice sa ID-jem i zivim podacima sa senzora (tezina, temperatura, vlaga) | (a), (d) | da |
| 2 | Zapis kosnice na Solani (NFT, program ili hash podataka), link na explorer | (a), (c) | da |
| 3 | Lista kosnica na prodaju i izbor jedne | (a) | da |
| 4 | Placanje koje radi (bilo koji nacin) | (a), (f) | da |
| 5 | Kupljena kosnica u nalogu kupca, zapis kupovine na lancu | (a), (d) | da |
| 6 | Isplata pcelaru u USDC, vidljiva na exploreru | (d), (b) | pozeljno |
| 7 | Podela 5% na nasu adresu | (f) | pozeljno, ako 5% vazi za kosnice |
| 8 | Phantom Connect za prijavu kupca | (e) | pozeljno |
| 9 | Javan repo | (e) | odluka Nemanje |

Ako 1, 2 ili 4 ne rade do snimanja, video pokazuje ono sto radi i u
prijavi se posteno pise sta je gotovo. Ne snima se korak koji ne postoji.

Izbaceno iz v1 (2026-09-24): pcelar dodaje seriju meda, QR na tegli,
kupac skenira teglu. Tegla dolazi posle kosnice (deck v3, slajd 7).

## Pitanja za Nemanju (i u open-questions.md)

- Sta od tabele vec radi danas: stranica kosnice sa zivim senzorom,
  zapis na Solani, kupovina? (#8, #21)
- Kako kupac placa? (#25)
- Isplata pcelaru odmah ili escrow? (#26)
- Oblik zapisa kosnice na lancu? (#32)
- Repo javan? (#22)
