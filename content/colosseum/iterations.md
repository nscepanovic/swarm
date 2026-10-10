# Iteracije

## v1 - 2026-09-22

Slides: "Colosseum 2026 - v1 - 2026-09-22" (decks folder).

- Prva kompletna verzija, 12 slajdova, speaker notes na svakom.
- Struktura po Pixar pitchu (obavezno od 2026-09-22): Problem, zasto danas
  ne radi (F1-F4), resenje (usko: samo marketplace za pcelinje proizvode),
  zasto bolje (A1-A4, par za svaku manu), traction, trziste bottom-up +
  susedna trzista. Posle: konkurencija, biznis model, Solana, tim, ask.
- Prvi nacrt je imao zaseban slajd "What is new since Frontier"; spojeno u
  traction (Pixar korak 5), jer je to dokaz, ne prica za sebe.
- Pitch je platforma, ne farma. Farma, zakup kosnice i senzori su dokaz
  (slajdovi 5 i 6). Novac ulagaca jasno vezan za farmu kao dobavljaca #1.
- Izbaceno iz starih deckova: ">80% fake" i "7 in 10 fake" (zamenjeno sa
  46% "suspected", OLAF/JRC), "$70B bee products" (bez izvora), apiterapija,
  "1,000 beehives", lokacija farme, sve projekcije sa rokovima.
- Trziste: bottom-up formula sa vidljivim placeholderima; potvrdjene
  zapremine (USDA/NHB 688.6M lb US 2024, CBI 363K t EU uvoz 2022), ~$2.7T
  agri kao susedno. IMARC ~$10B samo za proveru.
- Konkurencija iz Colosseum Copilota (munch, agrichain, agriverse, laviem,
  farmtrust, rizoma; bez nagrada) + AgriDex sa weba; pobednici u blizini
  (home-harvest, cargobill) samo u deck.md.
- Dizajn: bela pozadina, crni naslov, jedan zuti akcenat (Nemanja: brze je
  bolje).
- Najslabiji: slajd 6 (traction). Marketplace se ocenjuje po ponudi i
  prihodu, a broj pcelara, pristanak i prihod nisu potvrdjeni.

## v2 - 2026-09-24

Fajl: `content/colosseum/Colosseum 2026 - v2 - 2026-09-24.pptx` (Nemanja
prevlaci u decks folder). v1 nije stigao na Drive, pa nema rucnih izmena
za spajanje.

- Hakaton je Crypto World's Fair (rok 12.10.2026 23:59 PT), track-ovi po
  ekosistemu. Deck se pise za zuri koji bira 21 najbolji proizvod ukupno,
  ne samo Solana track (winners-full.md: u akcelerator ulazi vrh plasmana).
- Recenica kategorije napisana i stavljena na cover i u prvu recenicu
  govora: "the global farmers' market for honey: you know the beekeeper
  behind every jar, and he gets almost three times more for it."
- Jezik: consumer kao glavni, RWA (prava proizvodnja) i DePIN (senzori)
  kao dokaz ispod. Wolt poredjenje izbaceno, "farmers' market" radi isti
  posao bez objasnjenja.
- Slajd 2: dodat uvid "46M US households buy honey, 3% online" (NielsenIQ).
- Slajd 3: F4 dobio brojku, 2,9x (USDA NASS mart 2026: $2,45/lb pakeru
  naspram $7,15/lb direktno) i Hrvatsku (€2,5 naspram €7-8/kg). Nemanja
  potvrdjuje iz prakse.
- Slajd 4: "first live marketplace for bee products on a blockchain"
  (competition.md, nijedan ziv ni na jednom lancu), USDC odmah pri prodaji.
- Slajd 6: traction razdvojen na Company ($140K pre-seed, $200K+, farma)
  i Platform (cetiri regiona; placeholderi za prve pcelare, prvu seriju,
  prvu prodaju; "built during the hackathon"). Dve ranije prijave
  navedene otvoreno, FAQ trazi prijavu ranijeg rada.
- Slajd 7: US bottom-up sa primarnim brojkama (46,2M x $18,15 = $839M, 5%
  = $42M), raw honey 45% i raste; EU uvoz ispravljen sa CBI 363K t na
  Eurostat/EC 175K t (2024). Drugi proizvod i geografija ostaju odluka
  Nemanje, sa preporukom researcher-a u izvorima.
- Slajd 8: konkurencija prepisana po ispravkama iz competition.md: "only
  one with bee production" (ne "own production"), "no live marketplace"
  (ne "nobody connects"); dodati prezivele (ORO, Seedlot, Pastora),
  Pollenity, Etsy/Amazon, "no food or agri project in the accelerator".
- Slajd 9: 5%, pcelar bira ko snosi; poredjenje Etsy 6,5% + ~3%, Amazon
  Grocery 8-15%, CrowdFarming 22%.
- Slajd 10: prepisan za UX kriterijum iz pravila: kupac skenira teglu i
  vidi seriju i pcelara bez novcanika; pcelar dobije USDC odmah; Phantom
  Connect i USDC/Reflect sa liste resursa kao mogucnost; placeholder za
  javan repo.
- Slajd 11: "third Colosseum entry" otvoreno (pobednici se vracaju).
- Slajd 12: akcelerator kao cilj, $250K placeholder bez rokova.
- Dodata tabela "Pokrivenost kriterijuma" (7 sa sajta + 6 iz pravila) na
  kraj deck.md.
- Nov fajl `demo-video.md`: scenario demo videa do 3 min (pcelar dodaje
  seriju, kupac skenira i kupuje, USDC isplata, zapis na Solani) sa tabelom
  sta mora da postoji u kodu.
- `pitch-video.md` skracen na oko 2:40 po novoj strukturi.
- `infra/deck_build.py`: red "Source:" u "Na slajdu" ide kao sitan sivi
  footer; font 20pt kad slajd ima 6 tacaka.
- Najslabiji: i dalje slajd 6 (traction platforme je nula dok Nemanja ne
  da prvu brojku) i slajd 4 (zuri gleda rad tokom takmicenja, a demo jos
  ne postoji). Deck to kaze posteno umesto da sakriva.

## v3 - 2026-09-28

Fajl: `content/colosseum/Colosseum 2026 - v3 - 2026-09-28.pptx` (Nemanja
prevlaci u decks folder). v1 i v2 nisu na Drive-u (pretraga decks foldera
28.09), pa nema rucnih izmena za spajanje.

Sve po Nemanjinim ispravkama od 2026-09-28 (what-it-takes.md, vrh).

- Recenica kategorije je Nemanjina, doslovno: "HiveBits: the platform where
  beekeepers sell hives, not honey. We sold the first 300 in 27 hours."
  Cover i prva recenica govora. v2 "global farmers' market for honey"
  izbacena.
- Naslov price je prodaja, ne rejz: "300 hives sold in 27 hours", $140K na
  MetaDAO, oversubscribed. "Pre-seed raised" nema nigde. Ostali dokazi
  ($200K+, sell out) ostaju sa istim izvorima.
- Proizvod je kosnica, ne tegla (slajd 4): senzor, identitet, zapis na
  Solani, med ili prinos kupcu, novac pcelaru pre sezone.
- Slajd 3: nova mana F3 "money comes last" (pcelar placa sezonu unapred,
  naplacuje posle berbe); v2 F3 "proof is for experts" spojen u A1. Par
  A3 "hive sold before the season" ima dokaz (300 za 27 sati).
- Slajd 6: traction vise nije podeljen na firmu i platformu. Prodaja 300
  kosnica JE prodaja proizvoda koji platforma prodaje. Izbaceno "built
  during the hackathon" i "what works by 12.10" (startup takmicenje).
- Slajd 7: skala je isti proizvod, tri kupca: sledeci kontejner (one
  container, one sale), firme (3Bee: 500+ brendova, 10.000 pcelara, €5M
  Series A), pcelari iz mreze; med ($839M US, 5% = $42M) kao proizvod
  tih kosnica; AgriDex B2B kao horizont. Maslinovo ulje i EU uvoz skinuti
  sa slajda, u rezervi.
- Slajd 8: konkurencija su sad adopt-a-hive firme van lanca (3Bee,
  Pollenity, Honeyverse $249) i nijedan drugi projekat na Colosseum-u koji
  prodaje kosnice (Copilot 28.09, samo `hivebits`; najblizi `agrotoken`).
  "On any chain" skinuto dok researcher ne proveri (R2).
- Slajd 9: 5% na prodaju na platformi, nase kosnice (mi smo prodavac),
  cena kosnice za firme kao placeholder.
- Slajd 10: prvi argument je da je prodaja vec prosla na Solani.
- Slajd 11-12: "sold", ne "raised"; ask trazi pcelare koji prodaju kosnice
  i firme koje hoce kosnicu.
- `demo-video.md` v2: kosnica uzivo i kupovina kosnice na lancu; tegla, QR
  i serija izbaceni.
- `pitch-video.md` v3: isti tok, bez "built during this hackathon".
- `open-questions.md`: reseni #21, #24, #28, #29; novi #31-#38 i #30b;
  pitanja za researcher-a R1 (bottom-up za kosnice) i R2 (kosnice na
  drugim lancima).
- Najslabiji: slajd 7. Skala kroz kosnice nema bottom-up brojku (fali broj
  kolonija i cena kosnice), pa TAM stoji na medu, a kosnica je dokazana
  samo jednom prodajom (nasom) plus 3Bee kao tudji dokaz modela.

## v4 - 2026-10-10

Fajl: `content/colosseum/Colosseum 2026 - v4 - 2026-10-10.pptx`. Pravi ga
`infra/deck_build_v4.py` (ne cita deck.md; tekst slajdova je u skripti).

Nova struktura je Nemanjina (`MY-DECK-PROPOSAL`, 09.10): opsti marketplace,
"Buy food from trusted farmers", primer mleko u Bosni. Stil prati njegov
Google Slides "Colosseum Deck V1 - Marketplace" (tamna pozadina, zuti
naslovi). deck.md i pitch-video.md NISU uskladjeni sa v4.

- 1-5: kopija njegovih slajdova. Izmene: slajd 4 dobio "HiveBits, about
  $0.75 per liter" na luku i "$0.51, not $0.34" / "$0.75, not $1.09";
  slajd 5 dobio podnaslov "Our sensors track the farm".
- 6-11 novi: prodaja 300 kosnica, go to market, konkurencija, trziste i
  B2B, tim, ask.
- Nepotvrdjeno: $0.73 (procena), $0.51 i $0.75 (racunica: dostava 2x
  nedeljno, 400 l po turi); broj pcelara u mrezi; nijedan B2B kupac;
  sta se radi sa $250K. Ikonice su Noto Emoji (Apache 2.0), u infra/deck_icons/.

Izmene istog dana, po Nemanjinim odlukama (10.10): "raised", ne "sold"
(slajd 6 je sad "$140K raised in 27 hours", za farmu od 300 kosnica);
novac po isporuci, zakljucan na Solani u stablecoinu (slajd 5); "trusted
farmer" nije definisan, na slajdu pise samo "We start with farmers we
know"; $250K izbacen, ask kaze "more farmers, and better ways to check
them"; slajd 8 kaze da nijedan farmerski marketplace nije dobio nagradu
(Copilot, 10.10) umesto "11 projekata".

## v5 - 2026-10-10

Fajl: `content/colosseum/Colosseum 2026 - v5 - 2026-10-10.pptx`, pravi ga
`infra/deck_build_v5.py`. v4 ostaje kao fajl. deck.md i pitch-video.md
NISU uskladjeni.

Nemanjin novi ugao (10.10): najjaci adut je rejz, a marketplace ima tri
koraka: kupovina, zakup ili kupovina unapred, ulaganje u proizvodnju.

- 1: "$243K offered by 150 people in 27 hours. We asked for $140K."
  (brojke sa MetaDAO stranice, news.md 10.10). "The first community owned
  farm" su Nemanjine reci, "first" nije provereno.
- 2-4: njegovi slajdovi; "Buy food from trusted farmers." je sad naslov
  slajda 4.
- 5: tri koraka, treci nosi "We did this first".
- 6: zasto verovati farmi (zajednica je vlasnik, senzor, novac zakljucan
  na Solani u stablecoinu do isporuke).
- 7: drugi korak GTM-a je druga farma finansirana preko nas.
- 9: zarada (naknada pri finansiranju farme + 5% od prodaje), $103K
  ponudjeno a neprimljeno, B2B.
- 10: tim i ask zajedno.
- Pretpostavke koje Nemanja nije potvrdio: naknada pri finansiranju farme
  (bez procenta), "funded the same way we funded ours", "the community
  owns the farm". Cene mleka $0.73, $0.51, $0.75 su i dalje procena.
- Eduardo Rigon izbacen sa slajda o timu u v4 i v5 (Nemanja, 10.10: nije deo tima).

## v6 - 2026-10-10

Fajl: `content/colosseum/Colosseum 2026 - v6 - 2026-10-10.pptx`, pravi ga
`infra/deck_build_v6.py`. v5 ostaje. Nemanja je trazio da deck prati dva
teksta: Kevin Hale (YC), "How to design a better pitch deck", i
"Nail your startup pitch: use Pixar's story structure".

- YC: jedna ideja po slajdu, ideja pise kao recenica u naslovu na vrhu,
  krupan bold tekst, bez sitnih sivih redova i fusnota. Izvori i ograde
  su u beleskama. 9 slajdova za video plus dodatak od 3.
- Pixar: 2 Once upon a time (Do you know what you eat?), 3 And every day
  (farmer dobija trecinu), 4-5 Until one day (resenje i tri koraka),
  6 because of that (zasto je bolje), 7 because of that (traction),
  8 Until finally (trziste, $839M x 5% = $42M).
- Rejz je i na naslovnom (pitch iz snage) i kao korak 5; Pixar ga stavlja
  samo na 5.
- Sa slajda 3 skinuta srednja cena $0.73 (procena). Na slajdu 4 cene nose
  "about". GTM, konkurencija i zarada su u dodatku.

## v7 - 2026-10-10

Fajl: `content/colosseum/Colosseum 2026 - v7 - 2026-10-10.pptx`, pravi ga
`infra/deck_build_v7.py`. `deck.md` i `pitch-video.md` su ponovo
uskladjeni (prvi put od v3). v6 ostaje kao fajl.

Nemanjin pivot (10.10): "we started as a community owned farm but we found
a way to expand". Najjaci adut je da smo ubedili ljude da uloze. Platforma:
(1) isto to za druge farme, uz proveru i licenciranje farmi, ne samo
skupljanje novca; (2) rentanje kosnice, krave i slicnog sa farmi koje
onbordujemo, farma ne mora da bude finansirana preko nas; (3) prodaja
pojedinacnih proizvoda. U sustini zajednicko vlasnistvo nad proizvodnjom,
farma je prvi slucaj.

- 1: cover po Nemanji ("cover je ok"): "We started as the first community
  owned farm. We found a way to repeat it. 150 people offered $243K in 27
  hours."
- 3: isti primer mleka, nova poenta: "The farmer does not set his price.
  The one who pays him does." To vezuje mleko za rejz bez novog slajda.
- 4: resenje je nacin na koji smo finansirali nasu farmu: ljudi je
  finansiraju i poseduju, farmer prodaje njima. Platforma to ponavlja.
- 5: tri koraka u Nemanjinom redosledu: own, rent, buy. "We did step 1
  first." (v6 je imao buy, rent, invest.)
- 6: zasto verovati farmi: provera i licenca (novo, Nemanjin odgovor na
  "sta radite vi, a sta MetaDAO"), senzori, Solana drzi novac.
- 7: traction dobio "$103K had no farm to go to. Yet." (iz v5 beleski na
  slajd): dokaz traznje za platformom, ne samo za nasom farmom.
- 8: "Honey first. Then milk. Then anything that produces." Med bottom-up
  ostaje jedina brojka; sirina je jedna recenica, bez nabrajanja.
- 9: ask je druga farma (Nemanja 10.10: razgovora ni sa kim nije bilo).
  $250K nema.
- Dodatak: zarada u tri mesta (naknada pri finansiranju, deo od rentanja,
  5% od prodaje), GTM sa "any farm can join for renting and buying",
  konkurencija bez CrowdFarminga (Nemanja: ne idu na slajd).
- Nepotvrdjeno i bez brojke: naknada pri finansiranju (#39), deo od
  rentanja (#40), "first community owned farm" (#41), sta tacno znaci
  provera i licenca (#42). Cene mleka $0.34 i $1.09 su iz dva izvora i dva
  datuma, sirovo naspram preradjenog; beleska na slajdu 3 kaze kako se to
  izgovara.
- Najslabiji: slajd 8. Prica je o vlasnistvu nad proizvodnjom, a jedina
  brojka trzista je med. Druga slabost: korak 2 i 3 na slajdu 5 nemaju
  nijednu transakciju.

Izmene istog dana, po Nemanjinim ispravkama (10.10, posle prve v7):
- Slajd 3 naslov nosi obe strane: "You never see the farmer. And he does
  not set his price." (zatvara skok sa slajda 2 na 3).
- Slajd 4: "Anyone can invest in a farm and own it." Mi ne prodajemo
  vlasnicima, oni su vlasnici; prihod farme ide njima na lancu; "they know
  what they eat because they own the farm". Ideja od prvog dana: bilo ko
  moze da ulozi u proizvodnju hrane.
- Slajd 6: senzori su samo nasa farma (za druge ne znamo kako), pa nisu
  obecanje platforme; "novac zakljucan do isporuke" nema smisla za
  ulaganje, skinuto sa slajda, u A1 samo za rentanje i kupovinu. Umesto
  toga: vlasnistvo i prihod na Solani, otvoreno svima (post 07.09).

## v8 - 2026-10-10

Fajl: `content/colosseum/Colosseum 2026 - v8 - 2026-10-10.pptx`, pravi ga
`infra/deck_build_v8.py`. `deck.md` i `pitch-video.md` uskladjeni.

Nemanja (10.10): "nisam siguran da mogu da ti verujem dalje jer vidim da
mesas ono sto je bio rejz, ono sto radimo i ono sto treba da bude iduci
korak." Odatle pravilo tri kolone (A desilo se, B radi danas, C sledece),
upisano u deck.md i u `.claude/agents/deck.md`. Nemanja izabrao pravac 1
(platforma, skaliranje ulaganja na profitabilne grane poljoprivrede, plus
rentanje i prodaja) umesto pravca 2 (samo rentanje i prodaja).

- 1: recenica kategorije "The platform where people own the farm. We did
  it first." Rejz ispod kao dokaz.
- 4: samo sto se desilo, proslo vreme: "150 people own our farm. What it
  makes goes to them, on Solana." Luk je "150 owners", "Done. September
  2026, on MetaDAO."
- 5: platforma kao C: "We are building the platform that repeats it."
  Own, rent, buy. "Step 1 is done once, with our farm. Steps 2 and 3 come
  next."
- 6: zasto mi, ne launchpad: biramo farme koje zaradjuju i proveravamo
  ih; dokaz su cinjenice iz A (rasprodato svake sezone, $200K+ od kosnica,
  sopstveni senzori napravljeni). Skinuto: "sensors show you the farm
  live", "Solana shows who owns it" kao obecanje platforme.
- 8: "Then other farms that make money" (pravac 1), ne "anything that
  produces".
- 9: upotreba novca jedna recenica, bez iznosa: platforma i druga farma
  kroz proces. Predlog agenta, ceka potvrdu (#46).
- Dodatak dobio A1 "Done, and next": tri kolone na slajdu, ujedno
  prijava ranijeg rada koju FAQ trazi.
- Kolona B je prazna dok Nemanja ne odgovori na pet pitanja (#45, #8).
  Kad odgovori, delovi slajda 5 i 6 prelaze u sadasnje vreme.
- Najslabiji: slajd 5. Platforma je buducnost i deck to kaze. Popravlja se
  demo videom i kolonom B, ne tekstom.
