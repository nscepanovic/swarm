# HiveBits platforma: specifikacija proizvoda

Verzija 1, 2026-09-28. Za: agenta koji gradi aplikaciju, i Nemanju.
Tehnologija se ovde ne bira. Ovo je sta aplikacija radi, za koga, ekran
po ekran, sa svim stanjima. Koraci za izvrsenje su u `steps.md`, pravila
dizajna u `skills/hivebits-ui/SKILL.md`.

Jezik interfejsa: engleski. Svaki tekst na ekranu je ovde napisan tako da
moze da se prekopira. Ton: prost, direktan, kako Nemanja govori
("We track the humidity, temperature and the weight."). Bez kripto zargona
na strani kupca; novcanik je opcija, ne uslov.

---

## 0. Jedna recenica

**HiveBits je platforma na kojoj pcelari prodaju kosnice, ne med.** Kupac
bira kosnicu na mapi, gleda je uzivo, plati karticom ili na Solani, i
dobija med sa te kosnice. Pcelar dobija skoro tri puta vise nego od otkupa.
Mi uzimamo 5%.

Pcelar na platformi radi dve stvari, i obe su ravnopravne (Nemanja,
28.09):
1. **daje kosnicu u zakup** (na godinu ili sezonu; to je ono sto pitch
   zove "sell hives"), i
2. **prodaje proizvode** (med, vosak, propolis, polen, matice, nukleuse).
Moze jedno, drugo ili oba. Nijedno nije uslov za drugo.

Prvi pcelar na platformi je nasa farma (300 kosnica, vec prodatih). Drugi
su pcelari iz mreze (Brazil, Teksas, Montreal, Hrvatska). Firme kupuju istu
kosnicu sa svojim imenom.

## 1. Ko koristi aplikaciju

| Uloga | Ko je | Sta hoce | Kako ulazi |
|---|---|---|---|
| **Gost** | bilo ko sa linka, sa X-a, sa QR koda na tegli | da vidi kosnice, pcelare i med, bez naloga | bez prijave |
| **Kupac** (Buyer) | pojedinac koji kupuje kosnicu ili proizvod | da izabere, plati, prati svoju kosnicu, dobije med | email ili novcanik |
| **Firma** (Business buyer) | kompanija, DAO, Solana projekat | kosnicu sa svojim imenom, podatke za svoj tim, med sa svojom etiketom | isti nalog kao kupac, sa profilom firme |
| **Pcelar** (Beekeeper) | pcelar sa pcelinjakom, ukljucujuci nasu farmu | da izlista kosnice i proizvode, dobije narudzbine, bude placen | email, prijava je zahtev koji admin odobrava |
| **Admin** | HiveBits tim | da odobrava, kontrolise, ispravlja, vidi sve | posebna prijava, samo pozvani |

Jedan nalog moze da bude i kupac i pcelar (Nemanja je oba). Uloga pcelara
se dodaje na nalog, ne pravi se drugi nalog.

## 2. Sta se prodaje

Tri vrste stvari. Prve dve su u prvoj verziji, treca kao zahtev za ponudu.

### 2.1 Kosnica u zakup (Hive)

Ono sto je vec prodato 300 puta. Kupac zakupi kosnicu na godinu dana
(ili na sezonu, pcelar bira) i dobija:
- stranicu svoje kosnice sa podacima uzivo ako kosnica ima senzor
  (tezina, temperatura, vlaga), fotografijama i porukama pcelara;
- med sa te kosnice, kolicinu koju pcelar napise (npr. 3 kg u dve isporuke);
- svoje ime na kosnici (opciono, pcelar pise ime na kosnicu i slika);
- zapis kupovine na Solani (Hive Pass), koji moze da preuzme u novcanik
  ili ostavi kod nas ako nema novcanik.

Jedna kosnica moze da ima vise kupaca (pcelar odredi koliko "mesta" ima
kosnica, npr. 1, 3 ili 5). Kad su sva mesta prodata, kosnica pise
"Sold out" i ostaje vidljiva.

### 2.2 Proizvod (Product)

Jednokratna kupovina: tegla meda, vosak, propolis, polen, maticna mlec,
svece, nukleus ili matica (ovo poslednje sa ogranicenjem regiona slanja).
Svaki proizvod pripada pcelaru i, ako pcelar hoce, konkretnoj kosnici ili
seriji (batch). Serija ima zapis na Solani kad se napravi.

### 2.3 Korporativna kosnica (Business hive)

Isti proizvod kao 2.1, ali paket za firmu: vise kosnica, logo na kosnici,
dashboard za tim, med sa etiketom firme, bilje posadjeno u ime firme.
U prvoj verziji: stranica sa opisom i forma "Request a quote" koja ide
adminu. Bez cena na sajtu. Prodaja ide rucno.

## 3. Novac

- **Cene** su u USD. Prikaz u EUR po kursu je opcija za kasnije.
- **Provizija:** 5% od cene. Pcelar bira pri svakom listingu: "I pay the
  5%" (kupac vidi cenu pcelara) ili "Buyer pays the 5%" (cena se uvecava
  za 5% na ekranu kupca, jasno prikazano kao "HiveBits fee").
- **Troskovi naplate** (kartica, mreza): ko ih snosi je odluka Nemanje,
  `[Nemanja odlucuje]`. Podrazumevano u ovom dokumentu: platforma ih
  snosi iz svojih 5%.
- **Placanje:** kartica preko Stripe-a (kartica, Apple Pay, Google Pay) ili
  USDC na Solani (povezani novcanik ili Solana Pay QR kod). Kupac bira na
  jednom ekranu, oba su ravnopravna dugmeta.
- **Isplata pcelaru:** podrazumevano u ovom dokumentu je zadrzavanje do
  isporuke (escrow): za proizvod se isplata oslobadja kad pcelar oznaci
  "Shipped" i prodje 7 dana bez prigovora; za kosnicu se isplata deli:
  pola pri kupovini, pola pri prvoj isporuci meda. Nemanja odlucuje da li
  je "odmah pri kupovini" ili ovako (open-questions #26). Aplikacija mora
  da podrzi oba, kao podesavanje u adminu.
- **Kako pcelar prima novac:** USDC na svoj Solana novcanik, ili bankovni
  racun preko Stripe Connect. Pcelar bira jedno ili oba; admin vidi.
  Kupovina karticom moze da se isplati pcelaru u USDC i obrnuto; platforma
  drzi razliku i konvertuje `[tehnicki detalj za kasnije, ali ekran ne
  sme da pretpostavlja da su valute vezane]`.
- **Povracaj novca:** admin pokrece, kroz isti kanal kojim je placeno.
  Pravila (kad se vraca) su tekst u adminu, ne kod.

## 4. Mapa i javni deo (bez prijave)

### 4.1 Pocetna strana

Prvo sto se vidi je **mapa sveta sa pcelinjacima**, ne tekst o nama.
Iznad mape jedna recenica i jedno dugme:

> **Rent the hive, not the jar.**
> Pick a hive, watch it live, get its honey.
> [ Explore hives ]

Na mapi: jedna tacka po pcelinjaku. Tacka pokazuje broj kosnica koje su
dostupne i da li pcelinjak ima senzore (ikona "live"). Klik na tacku
otvara karticu: ime pcelara, fotografija, region, "3 hives available,
2 products", dugme "See apiary".

Ispod mape, jedan red kartica: **"Hives you can rent now"** (najvise 6),
zatim red **"From the beekeepers"** (najnovije poruke sa kosnica, sa
fotografijom), zatim **"How it works"** u tri koraka sa jednom recenicom
svaki:
1. Pick a hive on the map.
2. Pay with card or USDC.
3. Watch it live and get its honey.

Zatim traka poverenja sa javnim cinjenicama (samo one koje su javne i sa
izvorom; tekst daje Nemanja): "300 hives sold in 27 hours", "Beekeepers
in Brazil, Texas, Montreal and Croatia". Nista sto nije objavljeno.

Podnozje: About, For beekeepers, For business, FAQ, Terms, Privacy, X,
Telegram.

**Lokacija na mapi nikad nije tacna.** Pcelinjaci se kradu. Pcelar
unese tacnu lokaciju samo za sebe i admina; na mapi se prikazuje tacka
koju pcelar sam izabere (npr. centar sela ili grada) ili automatski
pomerena i zaokruzena tacka u krugu od par kilometara. Ovo pise i u
formi za pcelara: "Your exact location is never shown. Pick a public
spot for the map."

### 4.2 Lista i filteri

Dugme "Explore hives" vodi na stranu sa mapom levo (ili gore na mobilnom)
i listom desno. Prekidac "Map / List". Filteri, sto manje:
- Country (lista zemalja koje imaju pcelinjak)
- What: Hives / Honey / Other products
- Available now (prekidac)
- Live data (prekidac; samo kosnice sa senzorom aktivnim u zadnjih 24h)

Sortiranje: Newest, Price, Beekeeper.

### 4.3 Strana pcelinjaka (Apiary page)

URL sa imenom pcelara. Sadrzaj, redom:
- Fotografija pcelinjaka preko cele sirine, ime pcelara, region, od kad
  pcelari, oznake: "Verified beekeeper" (admin odobrio), "Live data".
- Prica pcelara u njegovim recima (do 600 znakova, on pise).
- **Hives** (kartice): ime kosnice, fotografija, cena, "2 of 3 spots
  left" ili "Sold out", "Live" ikona ako ima senzor, dugme "Rent this hive".
- **Products** (kartice): naziv, fotografija, cena, "In stock" ili "Sold
  out", dugme "Buy".
- **Updates**: poruke pcelara sa fotografijama, najnovija gore, javne su
  (kupci vide i privatne poruke za svoju kosnicu, vidi 6.2).
- Mala mapa sa javnom tackom.

### 4.4 Strana kosnice (Hive page)

Ovo je najvaznija strana. Redom:
- Ime kosnice i fotografija (galerija).
- **Live** blok, ako ima senzor: tezina (kg), temperatura (°C), vlaga (%),
  poslednje merenje ("12 minutes ago"), i grafik zadnjih 7 dana za tezinu.
  Ako senzor ne javlja duze od 24h: "No data since 3 days" i nema "Live"
  oznake. Ako kosnica nema senzor: blok se ne prikazuje, nema praznog
  mesta.
- **What you get**, kako je pcelar napisao, kao lista (npr. "3 kg of honey
  in two deliveries", "Your name on the hive", "Updates from the beekeeper").
- **Price** i period ("$249 for one year", "Season 2027"), broj mesta.
- **Dugme "Rent this hive"** (jedina primarna akcija na strani). Ako je
  sold out: "Sold out" i link "See other hives from this beekeeper".
- Pcelar (mala kartica sa linkom na pcelinjak).
- **On Solana**: link na zapis kosnice na lancu ("Hive record"), jedna
  recenica: "This hive has a public record on Solana. Every purchase is
  written there." Bez adresa i heksova na ekranu, samo link.
- Updates za ovu kosnicu.

### 4.5 Strana proizvoda (Product page)

Fotografije, naziv, tip, tezina ili kolicina, cena, "In stock (12)",
opis pcelara, iz koje kosnice ili serije ("From hive Lipa 3, harvest
June 2026" ako je pcelar vezao), "Ships to: EU, US" (regioni koje je
pcelar izabrao), dugme "Buy". Ako serija ima zapis: link "Batch record".
Ako serija ima laboratorijski test: link na PDF, oznaka "Lab tested"
samo ako je fajl okacen.

### 4.6 QR kod na tegli

Svaka serija dobija javni link i QR kod koji pcelar stampa na etiketu.
Skeniranje otvara stranu serije: koja kosnica, koji pcelar, kad je
vrcano, zapis na lancu, dugme "Rent this hive" ili "Buy more from this
beekeeper". Ovo je ulaz za kupca koji nas ne zna.

### 4.7 For beekeepers (javna strana)

Jedna strana: sta pcelar dobija (skoro 3x cena, kupci iz celog sveta,
5% provizija, isplata u USDC ili na racun), kako radi u tri koraka,
dugme "Apply as a beekeeper". Bez obecanja o broju kupaca.

### 4.8 For business (javna strana)

Sta firma dobija (kosnica sa imenom, zivi podaci za tim, med sa
etiketom, bilje u ime firme), fotografije, forma "Request a quote":
ime firme, kontakt, koliko kosnica otprilike, poruka. Ide adminu na
email i u admin panel. Bez cena.

## 5. Kupac: nalog i kupovina

### 5.1 Prijava

Dva nacina, oba na jednom ekranu:
- **Email**: unese email, dobije link ili kod, bez lozinke.
- **Wallet**: "Connect wallet" (Phantom i ostali Solana novcanici;
  Phantom Connect za onboarding bez ekstenzije `[proveriti dostupnost]`).

Nalog nastaje pri prvoj prijavi. Ime i adresa se traze tek kad su
potrebni (pri kupovini), ne pri prijavi. Nalog sa emailom moze kasnije da
poveze novcanik, i obrnuto (u Settings).

### 5.2 Kupovina kosnice (tok)

1. Na strani kosnice klik "Rent this hive".
2. Ako nije prijavljen: ekran prijave (email ili wallet), pa nazad na tok.
3. **Ekran "Your hive"**: pregled (kosnica, pcelar, sta dobija, period,
   cena, provizija ako je na kupcu, ukupno). Polje "Name on the hive"
   (opciono, do 30 znakova) ako pcelar to nudi. Polje "Deliver honey to"
   (adresa; moze i kasnije: "I'll add the address later", jer med stize
   posle berbe). Zemlja isporuke mora da bude u regionima koje pcelar
   opsluzuje; ako nije, jasna poruka pre placanja: "This beekeeper ships
   to EU and US only."
4. **Ekran placanja**: dva dugmeta jednake vaznosti: "Pay with card" i
   "Pay with USDC". Kartica otvara Stripe (u aplikaciji ili redirect).
   USDC otvara: ako ima povezan novcanik, potvrdu transakcije; ako nema,
   Solana Pay QR kod sa iznosom i tajmerom (npr. 10 minuta), plus dugme
   "Connect wallet instead".
5. **Ekran potvrde**: "Hive Lipa 3 is yours." Sta sledi (tri reda: "You
   will get updates from Sinisa", "Honey ships after the harvest", "Your
   Hive Pass is on Solana"). Dugme "Go to my hive". Email potvrde stize
   odmah.
6. Ako placanje ne uspe ili istekne: ostaje na ekranu placanja sa
   porukom i mogucnoscu da proba drugi nacin. Mesto na kosnici je
   rezervisano dok traje placanje (npr. 15 minuta), pa se oslobadja.

### 5.3 Kupovina proizvoda (tok)

Isto kao 5.2, sa razlikama: kolicina; adresa je obavezna pre placanja;
cena dostave je ono sto pcelar napise po regionu (ili "Free shipping");
potvrda kaze "Sinisa will ship within X days" (X je ono sto pcelar
napise). Korpa sa vise proizvoda od istog pcelara: da, jednostavna.
Korpa sa vise pcelara: ne u prvoj verziji (svaka narudzbina je jedan
pcelar).

### 5.4 Moj nalog (Buyer dashboard)

Meni sa cetiri stavke, nista vise:
- **My hives**: kartica po kosnici: fotografija, live brojke, poslednja
  poruka pcelara, sledeca isporuka ("Honey: after summer harvest"), link
  na stranu kosnice sa privatnim porukama, "Hive Pass" (vidi na Solani /
  preuzmi u novcanik ako je kupljeno karticom).
- **Orders**: lista narudzbina proizvoda, status (Paid, Shipped sa
  brojem za pracenje, Delivered), racun (PDF), dugme "Report a problem"
  koje otvara poruku adminu.
- **Addresses**: adrese za isporuku.
- **Settings**: email, povezan novcanik, ime, obavestenja (email da/ne),
  profil firme (ime firme, logo, PIB ako treba za racun) za poslovne
  kupce, brisanje naloga.

## 6. Pcelar

### 6.1 Prijava pcelara (Apply)

Forma u jednom ekranu, cuva se kao nacrt:
- Ime i prezime, ime pcelinjaka ili brenda, zemlja, region.
- Koliko kosnica ima, od kad pcelari (slobodan tekst).
- Fotografije pcelinjaka (do 5) i jedna sa pcelarom.
- Kako je cuo za nas, ko ga preporucuje (opciono; "Nemanja" je validan
  odgovor).
- Da li ima senzore i koje (opciono).
- Kvacica: "I confirm I am allowed to sell honey in my country."
- Dugme "Send application".

Posle slanja: "Thanks. We read every application ourselves. You will hear
from us by email." Admin vidi zahtev, moze da odobri, odbije sa porukom,
ili trazi jos podataka (poruka na email). Odobren pcelar dobija email
"You are in" sa linkom na svoj dashboard.

### 6.2 Pcelar dashboard

Meni: Apiary, Hives, Products, Orders, Updates, Payouts, Settings.

**Apiary**: javni profil (ime, prica, fotografije), tacna lokacija (samo
za nas) i javna tacka na mapi (bira klikom), regioni slanja (lista
zemalja ili grupa: EU, US, Canada, Brazil...), cena i rok dostave po
regionu, "Verified" status (samo citanje).

**Hives**: lista kosnica sa statusom (Draft, Live, Sold out, Paused).
Dodavanje kosnice:
- Ime (npr. "Lipa 3"), fotografije (do 8), kratak opis.
- Tip kosnice (lista: Langstroth, Dadant, LR, AZ, other) `[lista je iz
  game/design.md sekcija 7, proveriti]`.
- Sta kupac dobija: lista stavki, pcelar dodaje red po red ("3 kg of
  honey", "Two deliveries", "Your name on the hive").
- Period: "One year from purchase" ili "Season YYYY" (pocetak i kraj).
- Cena, i ko placa 5%.
- Broj mesta (1 do 10).
- Senzor: "This hive has a sensor" i ID senzora iz liste koju je admin
  registrovao za ovog pcelara (vidi 8.4). Bez toga nema "Live".
- Dugme "Publish". Pri prvom Publish: pravi se zapis kosnice na Solani
  (u pozadini; pcelar vidi "Record created" kad prodje).
Pauziranje: kosnica se ne prodaje, ali kupci koji je imaju i dalje sve
vide.

**Products**: lista i dodavanje: naziv, tip (Honey, Beeswax, Propolis,
Pollen, Royal jelly, Candle, Nuc, Queen, Other), fotografije, opis,
tezina ili kolicina po komadu, cena, ko placa 5%, kolicina na stanju,
iz koje kosnice ili serije (opciono), rok slanja u danima, regioni (od
podrazumevanih iz Apiary, moze da suzi). Za Nuc i Queen: obavezan izbor
regiona, upozorenje da su ziva bica i da vaze pravila prevoza.

**Serije (Batches)**, unutar Products: pcelar pravi seriju (datum
vrcanja, kosnice iz kojih je, kolicina ukupno, opciono laboratorijski
test kao PDF). Serija dobija zapis na Solani i QR kod za stampu (PNG i
PDF, u tri velicine). Proizvod se vezuje za seriju.

**Orders**: lista sa statusima. Za proizvod: New (placeno) → Shipped
(pcelar unosi kurira i broj za pracenje, jedno polje slobodnog teksta ako
nema pracenja) → Delivered (kupac potvrdi ili automatski posle N dana).
Za kosnicu: New → Active (odmah po placanju) → deliveries: pcelar oznaci
"Honey shipped" za svaku isporuku sa brojem za pracenje. Svaki red ima
ime kupca, adresu, sta je kupljeno, sta je pcelar duzan (npr. "2 of 2
deliveries left"). Dugme "Message buyer" (jednostavna poruka preko
emaila, bez chata u aplikaciji).

**Updates**: pcelar pise poruku sa fotografijama ili kratkim videom, bira
"All my hives" ili konkretnu kosnicu, i "Public" ili "Only my buyers".
Ovo je ono sto kupac gleda izmedju berbi; aplikacija ga podseca (email
jednom nedeljno: "Your buyers haven't heard from you in 14 days").

**Payouts**: koliko je zaradjeno, koliko je na cekanju (escrow), koliko
isplaceno, lista isplata sa datumom i kanalom. Podesavanje: USDC adresa
(sa proverom da je validna Solana adresa) i/ili Stripe Connect
onboarding. Bez adrese ili Stripe naloga, kosnica ne moze na Publish
(poruka: "Add where we send your money first.").

**Settings**: email, ime, jezik `[kasnije]`, obavestenja.

## 7. Firma (poslovni kupac)

U prvoj verziji: kupuje isto kao kupac, ali u Settings ima profil firme
(ime, logo, adresa za racun). Kad ima profil firme, "My hives" prikazuje
logo firme i dugme "Share with my team" (javni link na stranu kosnice sa
imenom firme, bez prijave). Sve ostalo (vise kosnica, etiketa, bilje) ide
rucno kroz "Request a quote" i admin unosi narudzbinu rucno (8.6).

## 8. Admin panel

Poseban URL, prijava samo za pozvane (admin poziva admina). Sve akcije
ostavljaju trag (ko, kad, sta). Meni:

### 8.1 Overview
Brojke za danas i ukupno: prodate kosnice, prodati proizvodi, promet,
provizija, na cekanju za isplatu, novi zahtevi pcelara, otvoreni problemi.
Bez grafika u prvoj verziji, samo brojevi i liste "treba paznja".

### 8.2 Beekeepers
Lista svih (Applied, Approved, Rejected, Paused). Detalj: sve iz prijave,
tacna lokacija, isplate, kosnice, proizvodi, narudzbine. Akcije: Approve,
Reject (sa porukom), Ask for more info (sa porukom), Pause (sve mu ide u
Paused, kupci ne trpe), "View as beekeeper" (otvara njegov dashboard samo
za citanje, radi podrske).

### 8.3 Listings
Sve kosnice i proizvodi, filter po statusu i pcelaru. Akcije: Unpublish
(sa razlogom koji pcelar vidi), Feature (ide u "Hives you can rent now"
na pocetnoj), Edit (admin moze da ispravi tekst i cenu; trag ostaje).

### 8.4 Sensors
Registar senzora: ID, pcelar, kosnica, poslednje javljanje, status.
Admin dodaje senzor i dodeljuje ga pcelaru; tek onda pcelar moze da ga
veze za kosnicu. Prikaz sirovih zadnjih merenja radi provere. Rucno
"Mark offline" ako je senzor skinut.

### 8.5 Orders
Sve narudzbine i pretplate. Filter po statusu, pcelaru, kupcu, nacinu
placanja. Detalj: sve sto vide kupac i pcelar, plus podaci o placanju
(Stripe ID ili Solana transakcija), escrow stanje. Akcije: Refund (ceo
ili deo, sa razlogom), Release payout now (preskoci escrow), Cancel,
Change status (rucno, sa razlogom), Add note.

### 8.6 Manual order
Admin pravi narudzbinu rucno za firmu ili za kupca koji je platio van
platforme (npr. bankovnim transferom): bira kupca (ili pravi nalog po
emailu), kosnice ili proizvode, cenu, oznacava "Paid outside" sa
napomenom. Kupac dobija sve kao da je kupio kroz sajt.

### 8.7 Payouts
Sta je dospelo za isplatu po pcelaru, po kanalu (USDC, Stripe). Dugme
"Pay now" po pcelaru ili "Pay all due". Istorija sa transakcijama.
Podesavanje: escrow pravilo (odmah / posle isporuke / pola-pola), broj
dana za automatski Delivered.

### 8.8 Business requests
Lista zahteva sa "For business" forme, status (New, In talks, Won, Lost),
beleske, link na rucnu narudzbinu kad se dogovori.

### 8.9 Content
Tekstovi koje admin menja bez koda: recenice na pocetnoj, "How it works",
traka poverenja, FAQ, Terms, Privacy, tekst emailova (naslov i telo, sa
promenljivama kao {buyer_name}, {hive_name}).

### 8.10 On-chain
Lista svih zapisa (kosnice, serije, Hive Pass-ovi, potvrde senzora):
status (Pending, Confirmed, Failed), link na explorer, dugme "Retry".
Ako nesto padne, aplikacija za kupca radi dalje, a ovde se vidi sta treba
ponoviti.

### 8.11 Problems
Sve sto su kupci prijavili preko "Report a problem" i sve sto je sistem
oznacio (placanje proslo a zapis pao, senzor cuti, isporuka kasni preko
roka). Status i beleske.

### 8.12 Users i Admins
Lista naloga, pretraga po emailu ili novcaniku, "View as", Block. Lista
admina, poziv novog admina, uklanjanje.

### 8.13 Settings
Provizija (5%, promenljivo), ko snosi troskove naplate, valute, regioni
slanja (lista koju pcelari biraju), tipovi proizvoda, tipovi kosnica,
rezervacija mesta pri placanju (minuti), Solana mreza (devnet / mainnet),
Stripe kljucevi (samo indikacija da postoje, ne prikaz).

## 9. Solana: sta ide na lanac i zasto

Minimum koji ima smisla kupcu, nista vise:
1. **Zapis kosnice** kad pcelar objavi kosnicu: ID kosnice, pcelar,
   region (javna tacka), datum. Javno, link sa strane kosnice.
2. **Zapis serije** kad pcelar napravi seriju: iz kojih kosnica, datum
   vrcanja, kolicina, hash laboratorijskog testa ako postoji. Na QR kodu.
3. **Hive Pass** kupcu pri kupovini kosnice: potvrda da ovaj novcanik (ili
   nas cuvani novcanik za kupca bez novcanika) ima mesto na ovoj kosnici
   za ovaj period. Kupac koji je platio karticom moze kasnije "Claim to my
   wallet". Hive Pass nije prenosiv u prvoj verziji `[Nemanja odlucuje]`.
4. **Potvrde senzora**: jednom dnevno po kosnici, hash dnevnih merenja.
   Kupac to vidi kao "Data verified on Solana, daily". Ne svaka tacka.
5. **Placanje u USDC**: transakcija kupca ide u nas racun (treasury ili
   escrow racun), isplata pcelaru je nova transakcija. Kupac vidi svoju
   transakciju kao link u Orders.

Ono sto NE ide na lanac u prvoj verziji: licni podaci, adrese, tacne
lokacije, cene proizvoda, poruke. $NECTAR: ne u prvoj verziji, samo
mesto u dizajnu (buduci popust i nagrade), da se ne izmisljaju pravila
tokena koja nisu potvrdjena.

Sve on-chain radnje su u pozadini i nikad ne blokiraju kupca: ako zapis
padne, kupovina je i dalje vazeca, admin vidi "Retry".

## 10. Senzori: sta aplikacija ocekuje

Aplikacija ne pravi senzore. Ocekuje da spoljni sistem (farma) salje
merenja u jednostavnom obliku: ID senzora, vreme, tezina, temperatura,
vlaga, (opciono) zvuk ili aktivnost. Aplikacija cuva istoriju, prikazuje
zadnje merenje i grafik 7 i 30 dana, i racuna "Live" (javio se u zadnjih
24h). Sve ostalo (alarmi pcelaru, analize) je za kasnije. Ovaj interfejs
mora biti dokumentovan na jednoj strani da farma moze da ga poveze.

## 11. Obavestenja (email; Telegram kasnije)

Kupac: potvrda kupovine, racun, "Update from your beekeeper" (odmah ili
dnevni zbir, kupac bira), "Honey shipped" sa pracenjem, podsetnik da doda
adresu ako je nije dao pre berbe, istek perioda kosnice 30 dana pre sa
"Rent it again".
Pcelar: nova narudzbina, podsetnik za slanje (rok koji je sam napisao),
podsetnik za update (14 dana tisine), isplata poslata, zahtev odobren ili
odbijen.
Admin: novi pcelar, novi poslovni zahtev, prijavljen problem, pao zapis
na lancu, placanje bez ispunjenja.
Svi emailovi kratki, tekstualni, sa jednim dugmetom. Tekst u adminu (8.9).

## 12. Sta aplikacija NE radi u prvoj verziji

- Ne organizuje dostavu. Pcelar salje, mi ne dodirujemo robu.
- Nema chata u aplikaciji. Poruke idu emailom preko platforme.
- Nema korpe sa vise pcelara.
- Nema recenzija i ocena (dolazi kad ima dovoljno kupovina).
- Nema vise jezika i valuta (engleski, USD).
- Nema $NECTAR logike.
- Nema veze sa igrom ni merch-om (dolazi kad postoje).
- Nema mobilne aplikacije; web mora da radi savrseno na telefonu.
- Nema samostalne kupovine korporativnog paketa (ide kroz zahtev).

## 13. Kvalitet: sta mora da vazi na svakom ekranu

- Radi na telefonu prvo. Svaki tok se probije palcem, jednom rukom.
- Jedna primarna akcija po ekranu. Ostalo je sekundarno i tise.
- Svako stanje ima ekran: prazno ("No hives yet. Add your first hive."),
  ucitavanje, greska sa recenicom koju covek razume i sta da uradi.
- Nikad ne gubi unos: forme cuvaju nacrt.
- Brojke sa jedinicama (kg, °C, %), datumi kao "12 June 2026", vreme kao
  "12 minutes ago".
- Kripto reci samo tamo gde kupac bira USDC. Nigde "NFT", "mint", "on-chain"
  u glavnom toku; umesto toga "Hive Pass", "record on Solana".
- Fotografije su velike i prave (sa pcelinjaka). Bez ilustracija pcela iz
  stock biblioteka.
- Pristupacnost: kontrast, tastatura, alt tekst na svakoj fotografiji,
  velicina dodira 44px.
- Brzina: pocetna sa mapom se otvara ispod 2 sekunde na mobilnoj mrezi,
  slike se ucitavaju lenjo.
- Privatnost: tacna lokacija i adrese se vide samo kome treba.

## 14. Merenje uspeha

Aplikacija belezi (bez trecih strana koje prate korisnika): posete strane
kosnice, klik na "Rent this hive", zapoceta placanja, uspesna placanja
po nacinu, vreme od prijave pcelara do prve objavljene kosnice, broj
update-a po pcelaru mesecno, koliko kupaca otvori svoju kosnicu u nedelji.
Admin Overview ovo pokazuje kao brojeve.

## 15. Otvorene odluke (Nemanja)

Odluke koje aplikacija podrzava na oba nacina, a podrazumevano je
navedeno; Nemanja moze da promeni podesavanjem, ne kodom:
1. Isplata pcelaru: odmah ili escrow (podrazumevano escrow, 3. sekcija).
2. Ko snosi troskove naplate (podrazumevano platforma).
3. Hive Pass prenosiv ili ne (podrazumevano ne).
4. Broj mesta po kosnici najvise (podrazumevano 10).
5. Da li se na pocetnoj prikazuju cene (podrazumevano da).
