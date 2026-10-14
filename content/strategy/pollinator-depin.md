# Kuce za divlje oprasivace sa senzorima (DePIN za oprasivace)

Istrazeno 2026-10-14 na Nemanjin zahtev. Interno, ne ide na X.
Ideja (Nemanja, 14.10): ljudi stalno pitaju za indoor kosnice, to ne radimo.
Umesto toga: outdoor "kosnice" za druge oprasivace, sa senzorima, kao dodatni
DePIN sloj koji pomaze da se oprasivaci razumeju i zastite. Povod: dosta
ljudi se zali da pcelarstvo ugrozava druge oprasivace. Plan: pitati Superteam
da pogura anketu, videti koliko ljudi bi se prijavilo, pa odluciti.

Sve cene dole su iz javnih listinga (Alibaba, Made-in-China, JLCPCB, Ecowitt,
maloprodaja), ne iz ponuda. Pre bilo kakve odluke o Kini treba 3 prave
ponude sa uzorkom. Brojke o HiveBits-u (tim, razvoj, koliko senzora imamo)
ovde nema, njih daje Nemanja.

---

## 1. Kratko

1. **Nauka je na strani ideje.** Da pcele konkurisu divljim oprasivacima
   nije "zalba", nego nalaz: eksperiment na ostrvu Giannutri (2025) pokazao
   je da zatvaranje kosnica na 11 sati dnevno dize nektar za oko 60% i polen
   za oko 30% na najposecenijim biljkama, a divlje pcele na ostrvu opadaju
   ([Pasquali i dr., Current Biology 2025](https://www.nationalgeographic.com/animals/article/honeybees-wild-bees-competition-flowers-island)).
   U Francuskoj gusto pcelarstvo smanjuje pojavu divljih pcela za 55%, efekat
   do 1.1 km od pcelinjaka ([Henry i Rodet 2018](https://hal.inrae.fr/hal-02622677)).
   Pcelar koji ovo javno priznaje i meri je redak. To je ugao.
2. **"Kosnica" za divlje oprasivace ne postoji.** Postoje dve stvari: kuca za
   solitarne pcele (Osmia, "bee hotel", naucno "trap nest") i kutija za
   bumbare. Oko 75% divljih pcela gnezdi u zemlji i nikakva kuca im ne
   pomaze ([MacIvor i Packer 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4364699)).
   Prvi proizvod treba da bude kuca za Osmiu: jeftina, poznata, naucno
   prihvacena metoda.
3. **Hoteli bez podataka su problem, i to je nas argument.** Toronto, 600
   hotela, 3 godine: u njima je bilo vise osa nego pcela, a cetvrtina
   stanara su unesene vrste. Zakljucak autora: hoteli se prodaju bez ijednog
   podatka da pomazu. Senzor i kamera odgovaraju bas na to: ko se useljava,
   kad, i da li uopste.
4. **Niko nema zivi DePIN za oprasivace.** Najblizi je Plan Bee Labs
   (pre-seed, "nodovi sa infrastrukturom za gnezdjenje + data marketplace"),
   bez dokaza da radi. 3Bee (Italija, €5M Series A) prodaje Polly kucu za
   Osmiu (€59 maloprodaja, firmama min. 5 adopcija) i ima "tehnoloski Polly"
   sa senzorom kvaliteta vazduha, bez kripta. Wildbiene+Partner (Svajcarska)
   ima 30.000+ kupaca kuca za Osmiu (2018) po CHF 120-200, bez senzora.
   Trziste za kucu postoji; trziste za podatke iz kuce jos niko nije napravio.
5. **Cena iz Kine (procena, 500 kom):** kuca + klima senzori + solar oko
   **$20-30** po jedinici; sa kamerom **$40-60**; sa pravom 7-u-1 meteo
   stanicom **$80-120**. Jednokratno: CE/RED $3-8K ako radio nije vec
   sertifikovan modul, prevoz $70-200 po kubiku. Detalji u sekciji 6.
6. **Najveci rizik nije hardver nego kupac podataka.** EU monitoring
   oprasivaca (EU-PoMS, obavezan od 2027) koristi transekte i zamke, ne kuce.
   Biodiversity krediti i TNFD traze podatke, ali metodologije su po
   stanistu, ne po oprasivacu. Danas niko ne placa za "occupancy kuce za
   Osmiu u dvoristu". Helium lekcija iz revenue-streams.md vazi i ovde:
   token bez dolarskog kupca ne drzi uredjaj upaljen.
7. **Preporuka:** da, uraditi anketu kroz Superteam, ali pre Kine napraviti
   10-20 jedinica rucno od gotovih modula (sekcija 8). Kina ima smisla tek
   sa MOQ 500, a to je odluka koja trazi i kupca i sezonu.

---

## 2. Sta je proizvod, tacno

| | Kuca za solitarne pcele (Osmia) | Kutija za bumbare |
|---|---|---|
| Sta je | Blok sa cevcicama 6-10 mm, "bee hotel", naucno "trap nest" | Kutija 20-30 cm sa ulazom, gnezdi se jedna matica |
| Ko se useli | Osmia, Megachile, plus ose i paraziti | Bombus, retko (nizak procenat zauzetosti u praksi) |
| Sezona | Mart do jun (Osmia), onda miruje do sledeceg proleca | April do avgust |
| Odrzavanje | Cevcice se menjaju ili ciste svake godine, inace paraziti | Ciscenje posle sezone |
| Sta senzor moze da meri | Temperatura i vlaga u bloku, broj ulaza/izlaza, slika cevcica (zauzetost), zvuk | Temperatura u gnezdu (termoregulacija), tezina, zvuk |
| Naucna osnova | Standardna metoda, koristi se od 1950-ih na svim kontinentima ([Staab i dr. 2018](https://fis.leuphana.de/en/publications/trap-nests-for-bees-and-wasps-to-analyse-trophic-interactions-in-/)) | BumbleBEEP sistem (temperatura, tezina, zvuk) ([Ecological Entomology 2025](https://www.citedrive.com/en/discovery/scpbumblebeepscp-a-sensor-system-for-bumblebee-colony-monitoring/)) |
| Preporuka | **Prvi proizvod.** Jeftina, radi, ljudi je znaju | Kasnije, zauzetost je nepredvidiva, prazna kutija je los sadrzaj |

Bitno za komunikaciju: ne zvati je "kosnica". Kosnica je za koloniju. Ovo je
"pollinator house" ili "nesting node". I ne obecavati bumbare.

---

## 3. Nauka: da li pcelarstvo ugrozava druge oprasivace

Kratko: konkurencija za cvetove je dokazana skoro u svakom istrazivanju.
Efekat na populacije divljih pcela je dokazan u manje radova, ali novi
eksperimenti su sve jasniji.

- Sistematski pregled (Mallinger i dr. 2017): 53% studija o konkurenciji
  nalazi negativan efekat na divlje pcele, 28% nema efekta, 19% mesano.
  Vecina meri posredno, ne direktno brojnost ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5722319/)).
- Wojcik i dr. 2018: 83 studije, preklapanje izvora hrane nadjeno u 100%
  studija koje su ga merile ([Entomology Today](https://entomologytoday.org/2018/06/18/more-research-needed-to-better-balance-honey-bees-and-native-bees/)).
- Henry i Rodet 2018, Francuska, mediteranska makija: gusto pcelarstvo
  smanjuje pojavu divljih pcela za 55% i njihov uspeh u skupljanju nektara
  za 50%. Efekat 600-1.100 m oko pcelinjaka. Zanimljivo: i same pcele
  skupljaju manje (nektar -44%, polen -36%) ([HAL INRAE](https://hal.inrae.fr/hal-02622677)).
- Pariz (Ropars i dr. 2019): sto vise kosnica u okolini, manje poseta
  divljih oprasivaca. Krupne solitarne pcele pogodjene na 500 m, bumbari na
  1.000 m ([PLoS ONE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6742366/)).
- Svajcarska (WSL 2022): broj kosnica u 14 gradova udvostrucen 2012-2018
  (3.139 na 6.370), u vecini gradova nema dovoljno cvetova za njih
  ([WSL](https://www.wsl.ch/en/news/beekeeping-in-cities-may-harm-wild-bees-and-honeybees/)).
- Giannutri 2025 (gore): prvi eksperiment sa "ukljuci/iskljuci" pcelama na
  celom ostrvu. Najjaci argument.

Sta iz ovoga sledi za nas: HiveBits je pcelarska firma. Da pcelar sam meri
uticaj svojih pcela na komsije je prica koju niko u ekosistemu nema. Ali ako
se uradi bez podataka, to je greenwashing i publika koja se zali ce to prva
reci. Senzor je ono sto pravi razliku izmedju "jos jedan bee hotel" i
"merimo".

---

## 4. Problem sa hotelima za pcele (i zasto je to nas argument)

MacIvor i Packer, Toronto, 2015: oko 600 hotela pracena 3 godine, preko
27.000 pcela i osa. Unesene vrste pcela na 32.9% lokacija i 47.1% svih
pcela. Ose cesce od pcela. Zakljucak: hoteli se promovisu "bez ijednog
podatka da imaju pozitivan efekat", a mogu da pojacaju invazivne vrste
([PLoS ONE 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4364699)).

Sta kasnija nauka kaze da se radi: neobradjeno tvrdo drvo, rupe pravog
precnika, zamena cevcica svake godine, prava lokacija (sunce, zaklon)
([WLGF pregled](https://wlgf.org/gardening-for-wildlife/attracting-different-wildlife-groups/attracting-insects/bee-hotels-what-does-recent-science-tell-us/)).

Za nas to znaci dve stvari:
1. Kuca iz Kine za $3 je upravo ono sto nauka kritikuje (bambus, lepak,
   bez ciscenja). Ako idemo u Kinu, specifikacija mora da bude: izmenjivi
   drveni blokovi ili papirne cevcice, 6-10 mm, bez lepka u kanalima.
2. Senzor je odgovor na kritiku "ne znamo sta se u njima desava". Kamera
   koja slika cevcice jednom dnevno daje zauzetost. Brojac na ulazu daje
   aktivnost. To je podatak koji danas nema skoro niko u velikom broju.

---

## 5. Ko to vec radi

| Ko | Sta | Cena / skala | Kripto | Status |
|---|---|---|---|---|
| [3Bee Polly](https://oasi.3bee.com/en/adopt-a-bee) (Italija) | Drvena kuca za Osmiu, PEFC, 20 stanara; "tehnoloski Polly" sa senzorom kvaliteta vazduha; app; firme usvajaju kao ESG | €59 maloprodaja; firme min. 5 adopcija; 3Bee ukupno €5M Series A, 10.000 pcelara, 500+ brendova | ne | zivo |
| [3Bee Spectrum](https://cordis.europa.eu/project/id/101144456) | Bioakusticki senzor, broji i klasifikuje insekte po zvuku, ide u "Biodiversity Index" | nema javne cene | ne | zivo, EU projekat |
| [Wildbiene+Partner](https://www.csmonitor.com/World/Europe/2018/0619/One-answer-to-the-bee-crisis-Turn-everyone-into-backyard-breeders) (Zurich) | BeeHome kuca za Osmiu + kokoni; kupac svake jeseni salje blok nazad, oni ociste i vrate sa novim kokonima; iznajmljuju pcele farmerima | CHF 120 (mala, 100 rupa) do CHF 200; 30.000 kupaca i 300 farmera 2018 | ne | zivo, 13 godina |
| [AirBeeNBee](https://www.hackster.io/jennifer-leavey/airbeenbee-c0ea63) (Hackster) | DIY hotel sa Seeed SenseCAP K1100: temp, vlaga, kvalitet vazduha, AI kamera za vrstu i zauzetost | kit $99-120 | ne | hobi projekat |
| [Oslo prirodnjacki muzej](https://www.raspberrypi.com/news/smart-bee-hotel-features-11-raspberry-pis/) | Hotel sa 11 Raspberry Pi: 10 kamera uzivo + senzori | n/a | ne | izlozba |
| [osmiaCAM](https://www.citedrive.com/en/discovery/osmiacam-a-low-cost-imaging-monitoring-system-for-linking-solitary-bee-foraging-nest-provisioning-and-environmental-sensitivity/) (Kalifornija) | Open source kamera sistem za trap nests, nedelje neprekidnog pracenja | "low-cost", bez brojke | ne | nauka |
| [Freiburg, Wittmann 2024](https://www.nature.uni-freiburg.de/ressourcen/publikationen-pdfs/wittmann-et-al-2024) | Raspberry Pi + YOLOv5 na Osmia hotelu, 78% preciznost, uputstvo za replikaciju | n/a | ne | nauka |
| [UKCEH AMI](https://nora.nerc.ac.uk/id/eprint/542184/) | Kamera zamka za insekte, open source, oko 200 jedinica u 30+ zemalja | n/a | ne | nauka |
| [Plan Bee Labs](https://directory.plnetwork.io/teams/clwfup0vr001wuy028nv9c7eq) | "Decentralizovana mreza za divlje oprasivace": nodovi sa gnezdima, IoT, ML, data marketplace | pre-seed, "raising funds" | da (plan) | nema dokaza da radi |
| [Ambios](https://www.theblock.co/news/business/2024-05-07-solana-depin-ambient-funding-token-acquires-planetwatch-292971) (Solana) | DePIN za kvalitet vazduha, preuzeo PlanetWatch | n/a | da | zivo, nije oprasivaci |
| [BugDex](https://ethglobal.com/showcase/bugdex-zbiu3) | Mobilna app, slikaj insekta, stake token | hakaton 2025 | da | nejasno |

Zakljucak: kuca za Osmiu kao proizvod ima dokazano trziste (W+P, 3Bee).
Senzorizovana kuca postoji samo kao nauka i hobi. DePIN za oprasivace
postoji samo kao ideja (Plan Bee Labs). Prostor je prazan, ali prazan moze
da znaci i "niko nije nasao ko placa".

---

## 6. Koliko kosta iz Kine

Procena po jedinici za porudzbinu od 500 komada, FOB Kina, bez prevoza,
carine, sertifikacije i razvoja. Tri nivoa.

### Nivo A: kuca + klima + brojac (bez kamere)

| Deo | Procena $/kom | Osnova |
|---|---|---|
| Drvena kuca za Osmiu, izmenjivi blok | 3-6 | Alibaba listinzi: Qingdao Kulu $1-5, Xiamen Xingjiayu $4-4.5, Cao County $2-3, Jinan Hony $3, Qingdao Enjoy $4.9-6, svi MOQ 500 ([Alibaba](https://www.alibaba.com/countrysearch/CN/bee-hotel.html)); Made-in-China $2.35-6.35 MOQ 500. Kvalitetniji blok (tvrdo drvo, izmenjiv) ide ka gornjoj granici |
| MCU sa radiom (ESP32-C3 ili ESP32-WROOM-32) | 2-4.5 | JLCPCB: ESP32-WROOM-32 $4.17-4.25 na 550-1100 kom ([JLCPCB](https://api.jlcpcb.com/partdetail/C6244703)); C3 je jeftiniji |
| Temp/vlaga senzor (SHT30 ili BME280) | 1-3 | SHT31 cip ~HK$28 (oko $3.6) na 1000+ ([RS](https://hken.rs-online.com/web/p/temperature-humidity-sensor-ics/2626177?gb=s)); SHT30 i GY moduli iz Kine $1-2 |
| IR brojac na ulazu (break-beam par) | 1-2 | standardni deo, procena |
| Solar 2W 6V + 18650 + punjac | 3-5 | panel $0.8-1.2 MOQ 100 ([Alibaba](https://electronics.alibaba.com/product/2-w-solar-panel)); 18650 2600mAh $0.7-1.6 MOQ 100 ([Alibaba](https://electronics.alibaba.com/product/zhuoneng-batteri)); TP4056 modul ispod $0.5 |
| PCB + montaza | 4-7 | JLCPCB: setup $25-50 po seriji, $0.0017 po lemnom spoju, X-ray $0.31/kom na 201-500 ([JLCPCB](https://api.jlcpcb.com/help/article/pcb-assembly-price)); komponente dominiraju |
| IP65 kutija za elektroniku, kablovi | 2-3 | standardna ABS kutija |
| **Ukupno nivo A** | **16-30** | |

### Nivo B: nivo A + kamera (zauzetost cevcica, slika dnevno)

| Deo | Procena $/kom | Osnova |
|---|---|---|
| ESP32-S3 + OV2640 (umesto obicnog MCU) | 9-14 | ESP32-S3-CAM ploce $12-14 pojedinacno ([eBay Shenzhen](https://www.ebay.com/itm/355486123949)); OV2640 sam $2.45 na 1000 kom ([Kunkune](https://kunkune.co.uk/shop/uncategorized/1000pcs-ov2640-camera-module)) |
| Veci solar (5W) + 2x 18650 | 5-8 | kamera trosi vise |
| microSD + nosac | 1-2 | |
| Ostalo iz nivoa A (kuca, senzor, brojac, PCB, kutija) | 11-21 | |
| **Ukupno nivo B** | **26-45**, realno **40-60** sa rezervom za lose procene | |

Napomena: kamera iznutra trazi osvetljenje i staklo ispred cevcica, sto je
mehanicki najtezi deo i najveci razlog da prva serija ne ide iz Kine nego
rucno.

### Nivo C: nivo B + prava meteo stanica (vetar, kisa, UV)

| Deo | Procena $/kom | Osnova |
|---|---|---|
| 7-u-1 spoljni senzor (Fine Offset tip, kao Ecowitt WS69) | 35-50 OEM procena | Ecowitt WS69 maloprodaja $63.99, GW3002 gateway + WS69 $118.99 ([Ecowitt](https://shop.ecowitt.com/en-de/collections/2025-christmas-promotion/products/ws69)); OEM je obicno 50-70% maloprodaje, nije proveren |
| Integracija (433/915 MHz prijem na nasem nodu ili njihov gateway) | 5-15 | |
| **Ukupno nivo C** | **80-120** | |

Alternativa za nivo C: ne kupovati stanicu po nodu. Jedna stanica po
lokaciji (farma, grad) i 10-50 jeftinih nodova oko nje. Vreme se ne menja
na 50 metara, zauzetost gnezda se menja. To obara prosek po nodu na nivo A
ili B.

### Prenos podataka (po nodu)

| Opcija | Dodatni trosak | Za koga |
|---|---|---|
| WiFi domacina | 0 | gradske baste, balkoni, firme; zavisi od lozinke domacina, to je operativni problem |
| LoRa (SX1262 modul) + gateway | +5-8 po nodu, gateway $100-200 po lokaciji | farma, polje; Ebyte E22-900M22S $5.25 maloprodaja ([RobotShop](https://www.robotshop.com/products/botstore-e22-900m22s-ebyte-tcxo-22dbm-6500m-sx1262-900mhz-new-lora-module-smd-wireless-transceiver-module-1)), Fanstel LR62E £6.91 na 1000 ([Mouser](https://www.mouser.co.uk/c/rf-wireless/wireless-modules/sub-ghz-modules/?m=Fanstel)) |
| Helium (LoRaWAN) | isto kao LoRa, bez svog gateway-a gde ima pokrivenosti | Solana prica se sama pise, ali pokrivenost u Srbiji je nepoznata, proveriti |
| NB-IoT / LTE-M | +10-15 + SIM | gde nema nista drugo |

### Jednokratni troskovi

| Stavka | Procena | Osnova |
|---|---|---|
| CE / RED (radio) | $3.000-8.000, 6-12 nedelja | [Alibaba seller blog](https://seller.alibaba.com/blogs/2026/southeast-asia/electronics/ce-certification-european-compliance-guide-alibaba-b2b); sa vec sertifikovanim modulom (Espressif, Ebyte) pada na EMC testiranje $400-800 do $2.000-4.000 |
| Kalup za plasticno kuciste | $3.000-10.000 | izbeci u prvoj seriji: drvo + standardna IP kutija |
| Prevoz LCL Kina-Evropa | $70-200 po kubiku + 30-50% na razne takse | [Suaid](https://suaidglobal.com/insights/lcl-cost-per-cbm/), [ExFreight](https://www.exfreight.com/?p=19482); 1 kubik je oko 60-100 kuca, znaci $2-4 po jedinici |
| Carina u Srbiju (drvo + elektronika) | nije proveren | treba spediter |
| Razvoj firmware-a, backend, app | ne mogu da procenim | Nemanja zna tim i sta vec imamo od senzora za kosnice; deo se verovatno nasledjuje |
| Uzorci pre serije (3 dobavljaca x 2 kom + prevoz) | $300-600 | |

### Primer racuna (procena, ne ponuda)

| Serija | Nivo | Hardver | Jednokratno | Ukupno |
|---|---|---|---|---|
| 20 kom, rucno, gotovi moduli (bez Kine) | B | 20 x $60-90 = $1.200-1.800 | 0 (moduli su vec sertifikovani) | **$1.200-1.800** |
| 500 kom, Kina | A | 500 x $16-30 = $8.000-15.000 | $5.000-12.000 (CE, uzorci, prevoz) | **$13.000-27.000** |
| 500 kom, Kina | B | 500 x $40-60 = $20.000-30.000 | $5.000-12.000 | **$25.000-42.000** |

Da se uporedi: W+P prodaje kucu bez senzora za CHF 120-200, 3Bee za €59.
Nivo B za $50 hardvera moze da se proda za €100-150 i da zaradi, ako ima ko
da kupi.

---

## 7. DePIN: ko placa za podatke

Ovo je pitanje koje odlucuje da li je ovo DePIN ili samo lep proizvod.

- **Nauka i drzava:** EU-PoMS, obavezan monitoring oprasivaca od prolece
  2027, radi sa placenim strucnjacima na transektima i zamkama za moljce, ne
  sa kucama ([BC Europe](https://www.bc-europe.eu/documents/laufen2025/Aidan%20Whitfield-%20Nature%20Restoration%20Regulation%20GBI%20EUPoMS.pdf)).
  Istrazivaci bi nase podatke uzeli, ali ne bi platili.
- **Firme (ESG, TNFD):** broj firmi sa TNFD izvestajima prosao 1.000 u
  2026 ([Carbon Pulse](https://carbon-pulse.com/552769/?site=nbp)).
  Biodiversity krediti postoje, ali metrike su po stanistu (DEFRA metrika),
  ne po oprasivacu. 3Bee ovo resava tako sto firmi prodaje adopciju kuce +
  izvestaj, ne podatke. **To je jedini dokazani kupac: firma koja kupuje
  pricu i izvestaj, ne CSV.**
- **Pojedinci:** W+P ima 30.000 kupaca kuca. Ljudi placaju da imaju pcele u
  basti, ne da daju podatke. Senzor je za njih sadrzaj (vidim svoju kucu u
  app-u), ne prihod.
- **Token:** Helium zivi jer ima 70.000 kupaca u dolarima
  (revenue-streams.md, sekcija 4). Nagrada u $NECTAR za uptime ima smisla
  samo kao dodatak, ne kao razlog.

Sta iz ovoga sledi: ne obecavati "data marketplace". Javno se ovo moze
predstaviti kao: mreza kuca za divlje oprasivace koju zajednica drzi, sa
podacima koji su javni, i sa $NECTAR za one koji drze node upaljen. Kupac u
dolarima je ista firma kao za korporativnu kosnicu (revenue-streams.md,
pravac 2): kuca za oprasivace je jeftinija ulaznica od kosnice za firmu
koja hoce biodiverzitet u ESG izvestaju, a bez pcelara i bez uboda.

---

## 8. Predlog kako da se testira

**Faza 0: anketa (Superteam + X).** Pre bilo kakve kupovine. Pitanja koja
daju odluku, ne lajkove:
1. Gde si (grad, selo, balkon, basta, firma)?
2. Da li bi drzao kucu za divlje pcele u dvoristu i prijavio sta se desava?
3. Da li bi platio za nju, i koliko (0 / do €50 / do €100 / vise), ili bi je
   uzeo samo besplatno uz obavezu da je drzi upaljenu?
4. Imas li WiFi na mestu gde bi stajala?

Prag za "ima smisla" nije nauka, nego Nemanjina odluka. Predlog za razgovor,
nije brojka za objavu: ako bar nekoliko desetina ljudi ostavi adresu i bar
deo njih kaze da bi platio, prva serija od 20 se isplati kao sadrzaj i test.
Ako svi hoce besplatno, to je ESG proizvod za firme, ne za zajednicu.

**Faza 1: 10-20 jedinica rucno, bez Kine.** Gotovi moduli (ESP32-S3 kamera
ploca, SHT30, panel, 18650), kuce od domaceg stolara ili W+P stila sa
izmenjivim blokom. Pola na nasoj farmi (uporedjenje sa kosnicama u blizini:
to je bas ono sto nauka meri, uticaj pcelinjaka na divlje pcele na 500-1000
m), pola kod ljudi iz ankete. Sezona: Osmia leti od marta, znaci kuce moraju
da budu postavljene do kraja februara da bi prva sezona dala podatke.
Rucna serija kosta $1.200-1.800 hardvera.

**Faza 2: Kina, tek posle jedne sezone.** MOQ 500, nivo A ili B, po
specifikaciji iz sekcije 4 (izmenjivi blokovi, bez lepka, pravi precnici).
Tada se znaju: koliko kuca se stvarno useli, koliko nodova pregovori sezonu
na solaru, koliko puta domacin promeni WiFi lozinku.

---

## 9. Rizici

- **Sezona.** Osmia je aktivna 2-3 meseca. Ostalih 9 meseci node meri samo
  temperaturu prazne kuce. Sadrzaj i "uptime" nagrada moraju to da uzmu u
  obzir.
- **Prazne kuce.** Deo kuca se nece useliti prve godine (lokacija, hrana,
  nema populacije u blizini). W+P to resava tako sto daje kokone sa kucom.
  Kokoni Osmie se prodaju, ali prenos preko granice je regulatorno pitanje.
- **Ose i paraziti.** Toronto rezultat. Bez godisnjeg ciscenja kuca postaje
  izvor parazita. Treba servis (W+P model) ili uputstvo + podsetnik u app-u.
- **Kradja i vandalizam** na javnim mestima; elektronika od $50 na drvetu.
- **WiFi zavisnost** kod domacina. LoRa resava, ali trazi gateway po
  lokaciji.
- **Greenwashing optuzba.** Pcelar koji prodaje "zastitu od pcelarstva".
  Jedini odgovor su javni podaci i to da prve kuce stoje na nasoj farmi,
  pored nasih kosnica.
- **Rasprsena paznja.** Rejz je zatvoren uz obecanje: zemljiste, kontejneri,
  kosnice (CLAUDE.md). Ovo je nova linija. Faza 0 kosta samo anketu, faza 1
  nekoliko hiljada dolara i jedan mesec inzenjera; faza 2 je prava odluka.

---

## 10. Pitanja za Nemanju

1. Sta tacno imamo od sopstvenih senzora za kosnice (MCU, radio, backend)?
   Ako je ESP32 + LoRa, nivo A je skoro isti hardver u drugoj kutiji.
2. Da li je Helium pokrivenost u Srbiji proverena? Ako postoji, prica
   "Solana DePIN na Solana DePIN-u" ide sama.
3. Ko je kupac u dolarima: firma (ESG adopcija), pojedinac (kupi kucu), ili
   niko (besplatno, placa se iz marketinga)? Od ovoga zavisi nivo A/B/C.
4. Da li prve kuce idu na farmu pored kosnica? To je jedino mesto gde se
   "uticaj pcelarstva na oprasivace" stvarno meri, i jedini odgovor na
   greenwashing.

---

## Izvori koji nisu linkovani gore

- Mallinger, Gaines-Day, Gratton 2017, systematic review: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5722319/
- Aarhus workshop 2022, stanje istrazivanja u Evropi: https://coloss.org/articles/9073/
- MacIvor i Packer 2015, Toronto hoteli: https://pmc.ncbi.nlm.nih.gov/articles/PMC4364699
- Pasquali i dr. 2025, Giannutri (Current Biology 35, 1576-1590, doi:10.1016/j.cub.2025.02.048): https://www.nationalgeographic.com/animals/article/honeybees-wild-bees-competition-flowers-island
- Henry i Rodet 2020, distanca umesto gustine: https://hal.inrae.fr/hal-02914825
- 3Bee Spectrum opis: https://blog.3bee.com/en/voices-from-the-oases-3bees-playlist-for-biodiversity
- 3Bee Polly tehnoloski, firme: https://3bee.com/en/esg/company-shelters
- Wildbiene+Partner: https://www.newlyswissed.com/wildbiene-partner-bees/
- BeeOmetrics / BeeOtel (FAO Agritech Observatory, uredjaj za automatsko pracenje divljih pcela): https://agritechobservatory.review.fao.org/en/beeometrics
- Valarm / LA Natural History Museum, hoteli sa senzorima mikroklime: https://www.valarm.net/?p=2684
- Plan Bee Labs, drugi listing: https://directoryv2.dev.plnetwork.io/projects/clwg2mokb0038rc02f1x5m57t
- DePIN kao okvir (arXiv): https://arxiv.org/pdf/2405.16495
- SenseCAP K1100 cena: https://elecena.pl/product/27037143/rss
- Kineske meteo stanice, listinzi: https://www.hengko.com/reasonable-price-china-manufacturer-outdoor-solar-powered-wireless-weather-station-agriculture-with-wind-products/
- BME280 cip cene: https://www.cytechsystems.com.cn/de/product/bme280
- Hardver IoT troskovi, pregled: https://hubble.com/community/comparisons/the-real-cost-of-building-iot-hardware-a-breakdown/
- South Downs biodiversity krediti, TNFD: https://www.southdowns.gov.uk/?p=72106
- Alveole, kosnice i TNFD/GRESB (komercijalni izvor): https://www.alveole.com/blog/how-rooftop-beehives-support-esg-and-biodiversity-goals

---

## 11. Kako se predstavlja investitorima (14.10, Nemanja: ovo je novi rejz)

Pet delova, svaki jedna do dve recenice:
1. Problem: pcelarstvo steti divljim pcelama, nauka potvrdjuje, niko ne meri.
2. Sta gradimo: kucice za divlje pcele sa senzorima, prvo pored nasih
   kosnica, posle kod ljudi i firmi; podaci javni, uredjaji u HiveBits mrezi.
3. Zasto mi: kosnice, senzori, tim i 150 ulagaca vec postoje; isti sistem u
   manjoj kutiji.
4. Sta novac radi: prva serija, postavljanje, app za domacina. Broj jedinica
   i iznos daje Nemanja.
5. Sta investitor dobija: kroz $NECTAR, kao u prvom rejzu, plus vise
   uredjaja u mrezi.

Predlog teksta (engleski, Nemanjin glas, zagrade popunjava Nemanja):

    We are raising again. This time for wild bees.

    People say beekeeping is bad for wild bees. New research says they are
    right. We are beekeepers, so we decided to measure it, not argue about it.

    We build small houses for wild bees with sensors inside. Same system as
    our hives, smaller box. First ones go next to our own hives. Then to
    people and companies who want one. All data is public and every house is
    a device in the HiveBits network.

    We already have the farm, the sensors, the team and 150 people who funded
    us. This is the next step, not a new company.

    The money goes to the first [N] houses, installing them, and the app
    where you see your house live.

    Raise: [amount], through [platform], in $NECTAR, same terms as before.
    Link below.

---

## 12. Biznis model (14.10)

| Model | Ko placa i za sta | Dokaz | Za nas |
|---|---|---|---|
| 1. Firme, ESG adopcija | Firma usvoji kucice, dobije izvestaj, pricu za zaposlene, ESG dokument; placa godisnje | 3Bee: min. 5 adopcija po firmi, 500+ brendova | Najjaci. Jeftinija ulaznica od korporativne kosnice, isti kupac. Senzor i javni podaci su razlika od 3Bee |
| 2. Pojedinci, kucica + godisnji servis | Kupi kucicu, svake jeseni salje blok na ciscenje, dobija nove kokone; placa kucicu i servis | Wildbiene+Partner: CHF 120-200, 30.000 kupaca, 13 godina | Drugi korak, trazi logistiku i uzgoj kokona |
| 3. Oprasivanje vocnjaka Osmiom | Vocar placa kucice sa kokonima u vreme cvetanja | W+P iznajmljuje pcele za 300 farmera; Osmia je komercijalni oprasivac za jabuku i badem | Prirodno uz nase farmere, ali sezonski servis, ne mreza |
| 4. Prodaja podataka | Niko standardno | Nema dokaza; Plan Bee Labs obecao marketplace, nema proizvoda | Ne graditi na ovome. Podaci cine model 1 vrednijim, nisu proizvod |

Model za nas: firma placa godisnje za kucice koje stoje kod nje ili kod
ljudi iz zajednice, dobija zivi dashboard i izvestaj. Domacin ne placa,
dobija $NECTAR za uptime. Mi drzimo kucice, servis i podatke. Prihod po
firmi je godisnji i ponavlja se, svaka kucica je uredjaj u mrezi. Pojedinci
(model 2) dolaze kad kucice vec stoje i ljudi ih vide.

---

## 13. DePIN model: sta kupac dobija (14.10)

Kupac je operater noda. Dobija stvar koju vidi, nagradu koju meri i status
koji pokazuje. Covek i firma se razlikuju samo u trecem.

Odmah:
- kucica sa senzorima + prvi stanari (kokoni Osmie), da prva sezona ne bude prazna
- kucica u app-u: temperatura, vlaga, vreme, ulasci/izlasci, slika cevcica (zatvorena cevcica = gnezdo)
- identitet kucice na lancu: ime, lokacija, datum, vlasnik (kao kosnica u mrezi)

Nedeljno i sezonski:
- $NECTAR za uptime i podatke (kao Helium za pokrivenost); dodatak za useljenje i izleganje
- poruke iz kucice ("prva pcela usla", "pet cevcica zatvoreno"), to je ono sto ljudi dele
- kucica na mapi mreze pored nasih kosnica i tudjih kucica

Godisnje:
- servis: salje blok, dobija ocisceno + nove kokone; bez toga kucica postaje gnezdo parazita, i to je razlog da ostane u mrezi
- firma dodatno: ESG izvestaj (kucice, gnezda, nove pcele, vrste), stranica za zaposlene sa zivim prikazom, "pollinator host" oznaka

Odakle nagrade: firme placaju godisnje za izvestaj i adopciju; deo ide u
pool iz kog se placaju kucice kod ljudi u blizini te firme. Covek u
dvoristu zaradjuje jer firma u gradu placa za podatke iz tog grada. Nagrada
ima pokrice u dolarima, ne samo u emisiji.

Sta kupac ne dobija: med i proizvode; prihod od prodaje podataka
pojedinacno; garanciju useljenja prve godine (zato idu kokoni).

---

## 14. Podaci: sta se prati i kome se prodaje (14.10)

Sta se prati:

| Spolja | Unutra | Izvedeno (to se prodaje) |
|---|---|---|
| temperatura, vlaga, pritisak | temperatura i vlaga u bloku | sati leta dnevno prema vremenu |
| svetlo, UV | ulasci/izlasci (brojac) | prvi let, kraj sezone |
| kisa, vetar (opciono) | slika cevcica dnevno (zauzetost, nova gnezda) | gnezda i nove pcele po sezoni |
| | zvuk (kasnije) | vrste, paraziti |

Meteo podaci objasnjavaju aktivnost, nisu proizvod.

Zasto sami meteo podaci ne prolaze: WeatherXM, 9.000+ stanica, licenca za
podatke 2025: jedini ponudjac WeatherXM sam, po minimumu; prihod od stanica
i prikljucenja, ne od podataka
(https://paragraph.xyz/@weatherxm/2025-data-license-winner). Nubila, 18.000
stanica, bez imenovanog kupca
(https://9o1hbtdj3x.depinhub.io/news/nubila-revolutionizing-real-time-weather-data-for-ai-applications-23641).

Ko kupuje podatke o oprasivacima danas:
1. Brendovi hrane i trgovci sa obavezama u lancu: M&S trogodisnja saradnja
   sa AgriSound senzorima, Importaco test u vocnjacima badema
   (https://www.freshplaza.com/europe/article/9829740/pollination-monitoring-trial-launched-in-spanish-and-portuguese-almond-orchards/).
   Najblizi kupac.
2. Vocari: da li je bilo dovoljno leta u nedelji cvetanja (BeeHero kupac).
3. Agro kompanije sa programima za oprasivace: Syngenta Operation
   Pollinator meri senzorima, Bayer placa razvoj senzora
   (https://www.farminguk.com/news/three-year-research-project-looks-at-sensor-technology-for-improved-monitoring-of-insect-pests_45004.html).
4. Firme za ESG (sekcija 12).
5. Sertifikati i nature krediti, kasnije: Bee Better Certified trazi
   gnezdilista i proverava godisnje
   (https://xerces.org/blog/bee-better-certifiedtm-creating-better-places-for-bees);
   EU testira nature kredite do kraja 2027.

Model: ne prodaju se redovi iz baze nego "izvestaj o oprasivacima za mesto
X", pretplata po lokaciji, godisnje, zivi prikaz + izvestaj na kraju sezone.
Kupac: brend, vocar, firma. Kucice kod ljudi su mreza koja izvestaj pravi i
dobija $NECTAR iz pretplate. Istrazivaci dobijaju podatke besplatno, to daje
kredibilitet izvestaju.
