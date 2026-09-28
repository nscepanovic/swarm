# HiveBits platforma: koraci za agenta

Verzija 1, 2026-09-28. Par sa `spec.md` (sta se gradi) i
`skills/hivebits-ui/SKILL.md` (kako izgleda).

Pravila za agenta koji ovo izvrsava:
- Jedan korak po sesiji. Korak je gotov kad su svi njegovi kriterijumi
  ispunjeni i kad se vidi u pregledacu, ne kad kod "postoji".
- Pre svakog koraka procitaj `spec.md` sekcije koje korak navodi i ceo
  `SKILL.md`. Posle koraka upisi u `progress.md` (napravi ga u prvom
  koraku): sta je uradjeno, sta je ostalo, sta je odluceno usput.
- Ne dodaj funkcije koje spec ne trazi. Ako nesto u specu ne moze ili
  nema smisla, napisi u `progress.md` pod "Pitanja" i uradi ostatak.
- Tekstove sa ekrana uzimaj doslovno iz `spec.md`. Ne izmisljaj brojke
  na sajtu (broj pcelara, kupaca); traka poverenja koristi samo tekst
  koji Nemanja da.
- Tehnologija je u `stack.md` (Go server, SvelteKit front, admin bez
  npm-a). Agent je prati; odstupanje trazi razlog u `progress.md`.
  Bezbednosna pravila iz `stack.md` vaze od koraka 1 (lockfile,
  ignore-scripts, cooldown paketa, tajne samo u env, non-root Docker).
- Svaki korak zavrsava sa: `npm run build` (ili ekvivalent) prolazi,
  osnovni testovi prolaze, screenshot glavnih ekrana u `screenshots/`.

---

## Korak 0: dizajn sistem i skill

Cilj: pre prvog ekrana postoje pravila i gradivni delovi, da svaki
sledeci korak izgleda isto.

Uradi:
1. Kopiraj `skills/hivebits-ui/SKILL.md` u `.claude/skills/hivebits-ui/`
   u repou aplikacije.
2. Napravi stranicu "/styleguide" (samo u razvoju) koja prikazuje: boje,
   tipografiju, dugmad (primarno, sekundarno, tiho, opasno; sva stanja),
   polja forme (obicno, sa greskom, onemoguceno), kartice (kosnica,
   proizvod, pcelar), oznake (Live, Verified, Sold out, In stock), prazna
   stanja, poruke greske, dijalog potvrde, toast.
3. Definisi tokene (boje, razmaci, radijusi, senke, fontovi) na jednom
   mestu, sa svetlom i tamnom temom.

Gotovo kad: "/styleguide" prikazuje sve iz tacke 2 u obe teme, na
telefonu i desktopu, i svaki element ima ime koje se posle koristi.

## Korak 1: temelj, podaci, prijava

Spec: sekcije 1, 5.1, 13.

Uradi:
1. Postavka po `stack.md`: Go servis, SvelteKit front, Postgres,
   Docker; `.npmrc` sa `ignore-scripts=true`, Renovate sa cooldown-om,
   CI sa govulncheck i npm audit. Zapisano u `progress.md`.
2. Model podataka za sve iz speca (User, Role, Beekeeper, Apiary, Hive,
   HiveSpot, Product, Batch, Order, OrderItem, Delivery, Payment, Payout,
   Update, Sensor, Reading, OnChainRecord, BusinessRequest, Problem,
   AuditLog, ContentBlock, Setting). Migracije. Seed sa jednim pcelarom
   (HiveBits farm), 3 kosnice, 4 proizvoda, 1 serija, laznim merenjima za
   7 dana.
3. Prijava emailom (kod ili link) i novcanikom (potpis poruke). Jedan
   nalog, vise nacina prijave. Sesija. Odjava.
4. Zastita ruta po ulozi (gost, kupac, pcelar, admin).
5. Osnovni layout: zaglavlje (logo, "Explore", prijava ili avatar),
   podnozje. Radi na telefonu.

Gotovo kad: mogu da se prijavim emailom i novcanikom, vidim svoj email
ili skracenu adresu u zaglavlju, odjavim se; seed podaci postoje u bazi;
ruta za admina vraca 403 kupcu.

## Korak 2: pcelar, prijava i dashboard (bez prodaje)

Spec: 6.1, 6.2 (Apiary, Settings, Payouts podesavanje), 8.2.

Uradi:
1. Javna strana "For beekeepers" (4.7) i forma "Apply" (6.1) sa nacrtom.
2. Admin: lista zahteva, Approve / Reject / Ask for more info sa porukom
   (email ide). Minimalni admin layout (meni, prijava za pozvane).
3. Pcelar dashboard: Apiary (profil, fotografije, tacna lokacija samo za
   nas, javna tacka na mapi biranjem klikom, regioni slanja, cena i rok
   dostave po regionu), Settings, Payouts podesavanje (USDC adresa sa
   validacijom, Stripe Connect onboarding dugme; moze mock dok ne stignu
   kljucevi).
4. Emailovi: prijava primljena, odobren, odbijen, trazi se jos.

Gotovo kad: novi pcelar se prijavi, admin ga odobri, pcelar popuni
Apiary sa javnom tackom koja nije njegova tacna lokacija, i doda USDC
adresu. Sve na telefonu.

## Korak 3: kosnice, proizvodi, serije

Spec: 2.1, 2.2, 6.2 (Hives, Products, Batches), 4.6 (QR).

Uradi:
1. Hives: lista, dodavanje, izmena, Publish, Pause, Sold out
   automatski. "Sta kupac dobija" kao lista redova. Broj mesta. Bez
   Payouts podesavanja nema Publish.
2. Products: lista, dodavanje, tipovi, stanje, regioni, rok slanja,
   veza sa kosnicom ili serijom. Upozorenje za Nuc i Queen.
3. Batches: pravljenje, PDF test, QR kod (PNG i PDF u tri velicine),
   javna strana serije.
4. On-chain: samo mesto u kodu (OnChainRecord sa statusom Pending) koje
   korak 9 puni. Pcelar vidi "Record pending".

Gotovo kad: pcelar objavi kosnicu sa 3 mesta i proizvod vezan za seriju,
QR sa serije otvara javnu stranu serije, Pause skida kosnicu sa liste.

## Korak 4: javni deo, mapa, strane

Spec: 4.1 do 4.5, 4.8.

Uradi:
1. Pocetna: mapa sa tackama pcelinjaka (samo javne tacke), kartice
   "Hives you can rent now", "From the beekeepers", "How it works", traka
   poverenja iz Content (admin), podnozje.
2. Explore: mapa + lista, prekidac, filteri, sortiranje, URL cuva
   filtere.
3. Apiary page, Hive page (sa "Live" blokom koji cita seed merenja),
   Product page. Sva stanja: sold out, bez senzora, senzor cuti.
4. "For business" strana sa formom "Request a quote" koja upisuje
   BusinessRequest i salje email adminu.
5. SEO osnove: naslov i opis po strani, deljenje na X sa slikom kosnice.

Gotovo kad: gost sa telefona nadje kosnicu preko mape za manje od 4
dodira, strana kosnice se otvara ispod 2 sekunde sa lenjim slikama,
mapa ne prikazuje nijednu tacnu lokaciju.

## Korak 5: kupovina karticom (Stripe)

Spec: 3, 5.2, 5.3, 5.4 (Orders, Addresses).

Uradi:
1. Tok "Rent this hive" i "Buy": prijava ako treba, ekran pregleda,
   ime na kosnici, adresa (obavezna za proizvod, opciona za kosnicu),
   provera regiona, rezervacija mesta na 15 minuta.
2. Stripe: kartica, Apple Pay, Google Pay. Webhook potvrde. Racun (PDF).
3. Ekran potvrde i email potvrde. Neuspeh i istek sa porukom.
4. Buyer dashboard: Orders, Addresses (My hives dolazi u koraku 7).
5. Provizija 5% po pravilu listinga ("I pay" / "Buyer pays"), zapisana na
   narudzbini.

Gotovo kad: test kartica kupi kosnicu i proizvod, mesto se smanji,
narudzbina i racun postoje, dupli klik ne pravi dve narudzbine, istekla
rezervacija oslobadja mesto.

## Korak 6: kupovina u USDC (Solana)

Spec: 3, 5.2 korak 4, 9 (placanje).

Uradi:
1. "Pay with USDC": sa povezanim novcanikom (potvrda transakcije) i bez
   njega (Solana Pay QR sa iznosom, referencom i tajmerom).
2. Potvrda transakcije na lancu pre nego sto narudzbina postane Paid;
   isti ekran potvrde kao kartica.
3. Devnet u razvoju, mainnet kao podesavanje u adminu.
4. Link na transakciju u Orders.

Gotovo kad: kupovina kosnice u USDC sa Phantom-om i preko QR koda prolazi
na devnetu, narudzbina je Paid tek posle potvrde, istek QR-a vraca kupca
na izbor nacina.

## Korak 7: narudzbine, isporuke, moja kosnica, update-i

Spec: 5.4 (My hives), 6.2 (Orders, Updates), 11.

Uradi:
1. Pcelar Orders: statusi, Shipped sa pracenjem, isporuke meda po
   kosnici, "Message buyer" (email preko platforme).
2. Buyer My hives: kartica po kosnici, privatni update-i, sledeca
   isporuka, "Report a problem".
3. Updates: pisanje sa fotografijama, javno ili samo za kupce, prikaz na
   Apiary i Hive strani i u My hives.
4. Emailovi iz sekcije 11 za kupca i pcelara, tekst iz Content.
5. Automatski Delivered posle N dana (podesavanje).

Gotovo kad: pcelar oznaci Shipped, kupac dobije email sa pracenjem i vidi
status; pcelar objavi update samo za kupce i gost ga ne vidi; kupac
prijavi problem i admin ga vidi u listi.

## Korak 8: admin panel u celini

Spec: 8.1 do 8.13.

Uradi: sve sekcije admina koje jos ne postoje: Overview, Listings sa
Feature i Unpublish, Sensors registar, Orders sa Refund (Stripe i USDC)
i rucnim statusima, Manual order, Payouts sa "Pay now" (Stripe Connect
transfer; USDC transfer sa treasury novcanika), Business requests,
Content (tekstovi i emailovi), On-chain lista sa Retry, Problems, Users
i Admins sa "View as", Settings. Audit log na svakoj akciji.

Gotovo kad: admin moze da napravi rucnu narudzbinu za firmu koja je
platila van sajta, refundira karticnu narudzbinu, isplati pcelara u USDC
na devnetu, promeni recenicu na pocetnoj bez koda, i svaka od tih akcija
je u audit logu sa imenom admina.

## Korak 9: zapisi na Solani

Spec: 9.

Uradi:
1. Zapis kosnice pri Publish, zapis serije pri pravljenju serije, Hive
   Pass pri placenoj kupovini kosnice (u novcanik kupca ili u cuvani
   novcanik platforme za kupca bez novcanika, sa "Claim to my wallet").
2. Sve u pozadini, sa redom za ponavljanje; kupovina nikad ne ceka
   lanac.
3. Linkovi na explorer na Hive, Batch i Orders stranama, recenice iz
   speca, bez heksova na ekranu.
4. Admin On-chain lista sa Retry.

Gotovo kad: na devnetu svaka objavljena kosnica i serija ima potvrdjen
zapis, kupac karticom vidi Hive Pass i moze da ga preuzme u Phantom, pad
RPC-a ne rusi kupovinu i ostavlja Pending sa Retry.

## Korak 10: senzori uzivo

Spec: 10, 4.4 Live blok, 8.4.

Uradi:
1. Ulaz za merenja (dokumentovan na jednoj strani, sa primerom) sa
   kljucem po senzoru.
2. Cuvanje istorije, zadnje merenje, grafik 7 i 30 dana, "Live" pravilo
   24h, stanje "No data since".
3. Dnevna potvrda (hash dnevnih merenja) kao OnChainRecord.
4. Admin Sensors: registar, dodela pcelaru, sirova merenja, Mark offline.

Gotovo kad: slanje merenja sa primerom iz dokumentacije se vidi na Hive
strani u roku od minuta, posle 24h bez merenja kosnica gubi "Live",
dnevna potvrda ima link na explorer.

## Korak 11: zavrsna provera i pustanje

Uradi:
1. Prodji ceo spec, sekcija po sekcija, i oznaci sta postoji, sta ne.
2. Prodji `SKILL.md` kontrolnu listu na svakom ekranu.
3. Testovi tokova: kupovina karticom, kupovina USDC, prijava pcelara do
   objave kosnice, refund, isplata.
4. Prazna baza: sajt ima smisla i bez ijednog pcelara (prazna stanja).
5. Terms, Privacy, FAQ iz Content. Kolacici i privatnost.
6. Merenje iz sekcije 14, vidljivo u admin Overview.
7. Uputstvo za pokretanje na serveru (jedna strana), backup baze,
   promenljive okruzenja bez vrednosti u repou.

Gotovo kad: sve iz tacaka 1 do 7 je u `progress.md` sa da/ne, i lista
"ne" je prazna ili ima razlog koji Nemanja odobri.

---

## Posle prve verzije (nije za sada)

Recenzije; vise valuta i jezika; $NECTAR popusti i nagrade; korporativni
paket samostalno; veza sa igrom i merch-om; Telegram obavestenja;
alarmi pcelaru sa senzora; korpa sa vise pcelara; mobilna aplikacija.
