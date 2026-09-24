# Sta nam treba da pobedimo (v1, 2026-09-24)

Mapa kriterijuma zurija na nase stanje. Cinjenice o hakatonu su u
`hackathon.md`, pobednici u `winners.md` i `winners-full.md`, propali u
`competition.md`, trziste u `market.md`. Ovaj fajl ne ponavlja izvore, on
kaze sta fali. Delovi oznaceni `[ceka: <fajl>]` se popunjavaju kad to
istrazivanje stigne.

## Kratko

1. Rok je **12.10.2026 23:59 PT**. Ostalo je 18 dana.
2. Ne biramo track. Solana track (10 nagrada po $10K) plus opsti fond
   (Grand Champion $30K, 20 po $15K). Pobeda u bilo cemu daje intervju za
   akcelerator ($250K).
3. Najveca rupa nije deck. **Zuri gleda rad tokom takmicenja, a
   marketplace jos ne postoji kao demo.** Farma, senzori i rejz su raniji
   rad i vrede kao dokaz, ne kao proizvod koji se ocenjuje.
4. Druga rupa: **traction marketplace-a je nula** (nijedna prodaja preko
   platforme, pcelari bez potvrdjenog pristanka). Ono sto imamo ($200K+ od
   kosnica, $140K pre-seed) je traction firme, ne platforme. Deck mora da
   to razdvoji posteno, jer zuri to prepozna.
5. Sta imamo, a skoro niko na Colosseum-u nije imao: sopstvenu
   proizvodnju, prihod, zatvoren pre-seed i zajednicu koja je vec ulozila.

## Mapa: sedam kriterijuma sa sajta

| # | Kriterijum | Imamo (potvrdjeno, izvor) | Fali | Ko resava |
|---|---|---|---|---|
| 1 | Founder + Market Fit | Nemanja pcelar + 10 god. inzenjering i IoT; Sinisa vodi farmu; Eduardo pcelar (deck.md slajd 11) | Nista bitno. Ovo je nasa najjaca karta, mora da bude u prvih 20 sekundi videa. | deck |
| 2 | Insight | "Ljudi ne znaju sta jedu", 46% uzoraka uvoznog meda u EU pod sumnjom (OLAF/JRC, deck.md slajd 2) | **Recenica kategorije** te jacine kao BORE.FI ili Pencil (winners.md). Jos nije napisana. | deck |
| 3 | Product + Execution | Farma se gradi (javno), senzori postoje (stari rad) | **Demo marketplace-a do 12.10**: pcelar, serija, kupovina, isplata u USDC. Sta od toga vec ima u kodu (open-questions #8) | Nemanja + dev |
| 4 | Potential Market Size | Zapremine US i EU (USDA, CBI, deck.md slajd 7) sa placeholderima | Bottom-up formula sa brojkama `[ceka: market.md]` | researcher, pa deck |
| 5 | Founder Communication | Nemanja govori prosto i direktno (CLAUDE.md, prednost) | Pitch video 2 do 3 min i demo video do 3 min, snimljeni. Scenario postoji (pitch-video.md), snimka nema. | Nemanja |
| 6 | Viability | 5% od prodaje, pcelar bira ko snosi (news.md 24.09) | Cena pcelaru naspram maloprodaje, da se vidi da 5% ima od cega da se uzme `[ceka: market.md]`. Poredjenje sa provizijama Etsy, Amazon, CrowdFarming `[ceka: market.md]` | researcher, Nemanja (#6) |
| 7 | Traction | $140K pre-seed za 27h, oversubscribed; $200K+ od kosnica; sell out svake sezone (deck.md slajd 6, javni postovi) | **Traction platforme:** broj pcelara koji su rekli da, prva serija na platformi, prvi kupac ili B2B razgovor (#1, #11) | Nemanja |

## Mapa: sest kriterijuma iz pravila (PDF, sekcija 8)

Ovo je pravno obavezujuci spisak i tri stavke nisu u sedam sa sajta.

| Kriterijum | Stanje | Sta treba |
|---|---|---|
| (a) Functionality, kvalitet koda | Nepoznato sta postoji (#8) | Radna aplikacija u demo videu, ne mockup. Repo koji se moze pokrenuti. |
| (b) Potential Impact, TAM i uticaj na ekosistem | Delimicno (slajd 7) | Isto kao #4 gore, plus recenica sta Solana dobija: pravi proizvodjaci i pravi kupci koji placaju u USDC, ne jos jedan DeFi protokol. |
| (c) Novelty | Nijedan ziv marketplace za pcelinje proizvode na blockchainu, ni na Colosseum-u ni na drugim lancima (competition.md 24.09, samo testnet prototipovi) | Formulacija: "prvi ziv marketplace za pcelinje proizvode na blockchainu", ne "niko ne povezuje kupce i pcelare" (Pollenity to radi bez kripta). |
| (d) UX, kako blockchain pravi bolji UX | Nista napisano | Jedna konkretna stvar koju kupac dobije zbog Solane: skenira teglu, vidi seriju, kosnicu i pcelara; pcelar dobije novac odmah. Bez toga je "blockchain radi verifikacije" prazno. |
| (e) Open-source, kompozabilnost | **GitHub org hivebits ima 0 javnih repoa** (hackathon.md) | Odluka Nemanje: repo marketplace-a javan pre 12.10, ili makar javan deo (program, SDK). Integracija sa sponzorima sa liste resursa (Phantom Connect za onboarding kupca, Reflect ili USDC za isplatu) se racuna kao kompozabilnost. |
| (f) Business Plan i sposobnost tima | Pre-seed zatvoren, farma u izgradnji, 5% model | Plan posle hakatona: sta se radi sa $250K ako udjemo (bez rokova koje Nemanja nije potvrdio). |

## Sta pobednici imaju, a mi nemamo

`[ceka: winners-full.md]`. Iz winners.md (23.09) vec znamo: recenica
kategorije, brojka koristi za proizvodjaca (CargoBill "2x"), i kod RWA
pobednika prinos za investitora, ne prodavnica.

## Sta propali imaju zajednicko, a mi ne smemo

Iz competition.md (23.09 i dopuna 24.09, ukupno 34 projekta):

- Od 23 novih (marketplace fizicke robe, RWA robe, agri DePIN): 16 mrtvih,
  3 nejasna, 4 ziva. Nijedan u akceleratoru. Tri od cetiri ziva su izbacila
  kripto sa sajta i prodaju samu robu (Seedlot kafa, Koffibinz app za
  uzgajivace kafe, Pastora udeli u stoci). Jedini koji je ostao kripto je
  ORO (tokenizovano zlato, $1.5M pre-seed). Uzorak od 4, zapazanje, ne
  pravilo: zive su stvari sa pravom robom ili pravim proizvodjacima iza.
- **Svih 23 je imalo pitch video, 12 tehnicki demo, nijedan link na radnu
  aplikaciju.** Radna aplikacija sa linkom nas izdvaja od celog skupa.
- **Ziv direktan konkurent: nema.** Ni na Colosseum-u ni na drugim lancima
  (samo prototipovi: HoneyChain na Sepolia testnetu, Colmena DAO,
  Agrocylo). Najblizi po modelu: AgroX, B2B berza poljoprivrednih
  proizvoda u Maleziji, provizija 5% (nije potvrdjeno da je isti tim kao
  na Colosseum-u). Najblizi po temi, van kripta: Pollenity (Bugarska),
  senzori u kosnici plus "Adopt-a-Hive" pretplata gde kupac dobija med iz
  konkretne kosnice.
- **Nase stare prijave** (Cypherpunk, Frontier) su obe pitchovale
  suvlasnistvo tokenizovane farme sa prinosom za ulagace. Nijedna nije
  pominjala marketplace, spoljne pcelare ni kupce. Marketplace je stvarno
  novo, i deck to sme da kaze.

**Ispravke koje deck mora da postuje:**
- Ne "jedini sa sopstvenom proizvodnjom" (Cacao Gold, Pastora, UrbanGro su
  imali ili tvrde da imaju). Tacno je: "jedini sa pcelarskom proizvodnjom".
- Ne "niko ne povezuje kupce sa pcelarima" (Pollenity to radi, bez kripta).
  Tacno je: "nema zivog marketplace-a za pcelinje proizvode na blockchainu".

## Lista za Nemanju, po redosledu vaznosti

1. **Registracija.** Da li je tim registrovan na colosseum.com za World's
   Fair, i ko je u timu. Bez toga nista drugo ne vazi.
2. **Demo do 12.10.** Sta od marketplace-a moze da radi za demo video:
   pcelar dodaje seriju, kupac kupuje, isplata u USDC, zapis serije na
   Solani. Ako nista ne postoji, to je prvi posao, pre decka.
3. **Repo javan ili ne.** Open-source je kriterijum u pravilima.
4. **Pcelari.** Koliko ljudi u Brazilu, Teksasu, Montrealu i Hrvatskoj je
   reklo da. Jedan snimak ili poruka od svakog vredi vise od broja.
5. **Cena.** Koliko pcelar dobije po kg u rinfuzi, koliko bi preko nas.
6. **Ask.** Sta trazimo na kraju: akcelerator, partneri, oba.
7. **"Znacajan kapital".** FAQ kaze da je hakaton za startape bez
   znacajnog spoljnog kapitala. $140K se prijavljuje otvoreno; ako hoces
   sigurnost, jedno pitanje na hello@colosseum.com.

## Sta radimo mi (agenti), bez cekanja

- researcher: winners-full.md, competition.md dopuna, market.md (u toku).
- deck: v2 posle istrazivanja, sa recenicom kategorije, UX recenicom,
  traction razdvojen na firmu i platformu, mapa kriterijuma po slajdu.
- deck: scenario demo videa do 3 minuta, uz pitch video.
