# Demo video - scenario v1 (2026-09-24)

INTERNO. Colosseum trazi **demo video do 3 minuta** koji pokazuje
proizvod (colosseum.com/hackathon, hackathon.md). Zuri ocenjuje
Functionality (kriterijum (a) iz pravila: koliko dobro radi, kvalitet
koda) i UX (kriterijum (d): kako blockchain pravi bolji UX). Od 23
slicnih prijava na Colosseum-u nijedna nije dala link na radnu aplikaciju
(competition.md); radna aplikacija sa linkom nas izdvaja.

**Pravilo za ovaj video: sve sto se vidi mora da radi.** Nema mockupa,
nema Figme, nema "ovo ce raditi". Ako neki korak ne postoji do snimanja,
taj korak se izbacuje iz videa, ne glumi se.

Ciljna duzina: 2:30. Bez muzike preko glasa. Ekran plus Nemanjin glas;
Nemanja u kadru samo na pocetku i kraju.

---

## Sta video pokazuje, redom

### 0:00-0:15 Uvod (Nemanja u kadru)

"This is the HiveBits marketplace. I will show you the full loop: a
beekeeper lists a batch, a buyer scans the jar and buys it, the beekeeper
gets paid in USDC, and the record is on Solana. Everything you see here
is running."

### 0:15-0:55 Pcelar dodaje seriju

Ekran: nalog pcelara (nas sopstveni, farma HiveBits, ili Nemanjin licni
pcelinjak; ne tudji dok taj pcelar ne pristane).

Koraci koji se vide:
1. Pcelar ulogovan, vidi svoj profil: ime, region, status "verified".
2. "New batch": vrsta meda, kolicina, berba (mesec, godina), cena po tegli.
3. Pcelar bira: 5% na njegov teret ili dodato na cenu. Ekran pokazuje
   koliko dobija po tegli u oba slucaja.
4. "Publish": zapis serije ide na Solanu. Prikazati potpis transakcije i
   link na explorer.
5. Aplikacija vraca QR kod za tu seriju (za nalepnicu na tegli).

Glas: "The beekeeper adds a batch: what honey, how much, which harvest,
his price. He chooses who pays the 5%. When he publishes, the batch record
goes on Solana, here is the transaction. And he gets a QR code for the
jar."

### 0:55-1:35 Kupac skenira i kupuje

Ekran: telefon (snimak ekrana telefona ili kamera preko ramena).

Koraci koji se vide:
1. Kamera telefona skenira QR sa tegle (prava tegla, prava nalepnica).
2. Otvara se stranica serije bez logovanja i bez novcanika: pcelar,
   region, berba, vrsta meda, link na zapis na Solani. Za seriju sa nase
   farme: i podaci iz kosnice (temperatura, vlaga, tezina), ako su vezani.
3. "Buy": kolicina, adresa, placanje. `[Nemanja: kako kupac placa u
   demo-u: novcanik (Phantom Connect), kartica, ili oba]`
4. Potvrda kupovine.

Glas: "The buyer scans the jar. No app to install, no wallet to look. He
sees who made it, where, which harvest, and the record on Solana. On
honey from our own farm he also sees the hive data. He buys."

### 1:35-2:05 Isplata pcelaru u USDC

Ekran: nazad na nalog pcelara, pa explorer.

Koraci koji se vide:
1. Nalog pcelara pokazuje prodaju i iznos u USDC (cena minus 5%, ili puna
   cena ako je 5% dodato kupcu).
2. Transakcija isplate na Solana exploreru: USDC stigao na adresu
   pcelara. Vreme transakcije se vidi.
3. Kratko: 5% HiveBits-a na posebnoj adresi, da se vidi da model radi.

Glas: "The moment the buyer pays, the beekeeper gets USDC. Here is the
transaction. No bank in between. Here is our 5%."

`[ako isplata ide sa zadrskom (escrow do isporuke), tako i reci; ne
glumiti "instant" ako nije]`

### 2:05-2:25 Zapis na Solani

Ekran: explorer ili nas prikaz on-chain podataka.

Koraci koji se vide:
1. Zapis serije: koja polja su na lancu (pcelar, region, berba, kolicina,
   hash podataka), a koja van lanca (slike, opis).
2. Ista serija, isti ID, na tegli, u aplikaciji i na exploreru.

Glas: "This is the batch record on Solana. The same ID is on the jar, in
the app and on chain. Anyone can check it, without us."

### 2:25-2:40 Zavrsetak (Nemanja u kadru)

"That is the loop. Beekeeper, jar, buyer, USDC, Solana. Code is at
[repo]. Thank you."

`[repo javan ili ne: Nemanja odlucuje, open-questions #22]`

---

## Sta mora da postoji u kodu za ovaj video

Minimum, bez koga se video ne snima u ovom obliku:

| # | Funkcija | Kriterijum koji pokriva | Mora do 12.10? |
|---|---|---|---|
| 1 | Nalog pcelara sa statusom "verified" (moze rucno postavljen) | (a) Functionality | da |
| 2 | Kreiranje serije i zapis serije na Solanu (program ili makar memo/NFT sa hash-om podataka) | (a), (c) Novelty | da |
| 3 | QR kod po seriji i javna stranica serije bez logovanja | (d) UX | da |
| 4 | Kupovina sa placanjem (bilo koji nacin koji radi) | (a), (f) Business Plan | da |
| 5 | Isplata pcelaru u USDC na Solani, transakcija vidljiva na exploreru | (d) UX, (b) Impact | da |
| 6 | Podela 5% na nasu adresu | (f) | pozeljno |
| 7 | Podaci iz kosnice vezani za seriju sa nase farme | dokaz (DePIN), ne uslov | pozeljno |
| 8 | Phantom Connect za prijavu kupca | (e) kompozabilnost | pozeljno |
| 9 | Javan repo | (e) Open-source | odluka Nemanje |

Ako 2, 4 ili 5 ne rade do snimanja, video pokazuje ono sto radi i u
prijavi se posteno pise sta je gotovo. Ne snima se korak koji ne postoji.

## Pitanja za Nemanju (i u open-questions.md)

- Sta od tabele iznad vec postoji u kodu, danas? (#8)
- Kako kupac placa u demo-u: novcanik, kartica, oba? (#25)
- Da li isplata pcelaru ide odmah ili posle isporuke? (#26)
- Koja serija se snima: nasa farma, tvoj pcelinjak, ili pcelar koji je
  pristao? (#27)
- Da li repo ide javno pre 12.10? (#22)
