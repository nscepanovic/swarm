# Pobednici Colosseum hakatona: sirok pregled i sta je bilo posle

Provereno 2026-09-24. Agent `researcher`.

Izvori:
- **Colosseum Copilot** (prijave i nagrade za Renaissance 2024, Radar 2024,
  Breakout 2025, Cypherpunk 2025): svih 293 nagradjenih projekata povuceno
  kroz `/search/projects` (`winnersOnly`), detalji kroz `/projects/by-slug`.
  Copilot nema Frontier 2026 ni Hyperdrive 2023.
- **Frontier 2026**: blog https://blog.colosseum.com/announcing-the-winners-of-the-solana-frontier-hackathon/
  i stranice projekata na colosseum.com/arena/projects/<slug> (tamo pise
  sajt, zemlja i kategorija koju tim sam bira).
- **Akcelerator**: portfolio https://colosseum.com/companies (74 firme:
  C1 10, C2 13, C3 10, C4 11, C5 21, plus 9 strateskih investicija) i
  https://blog.colosseum.com/announcing-colosseums-accelerator-cohort-5/ (29.06.2026).
- **Sta je bilo posle**: GitHub (commits.atom i GitHub API, datum poslednjeg
  commita i datum pravljenja repoa), HTTP status sajta (curl), web pretraga
  za rejz. X nalozi uglavnom nisu provereni (vidi "Sta nije provereno").

Napomene za citanje:
- "Recenica iz prijave" je prva recenica opisa koji Copilot cuva, doslovno,
  skracena na ~130 znakova. Em dash iz originala je zamenjen zarezom.
- "Traction (tim navodi)" je samo ono sto tim sam pise u opisu. To je
  tvrdnja tima, ne proverena cinjenica. Copilot cuva opis, ne ceo formular
  prijave, pa "nije navedeno u opisu" ne znaci da tim nije imao traction.
- "Akcelerator" iz Copilota znaci da je tim kasnije postao firma u portfoliju,
  ponekad preko drugog hakatona (primer: Unruggable je HM na Renaissance, a u
  akcelerator ulazi tek kao Grand Prize na Cypherpunku, C4).
- "GitHub danas" je datum poslednjeg commita na grani koju GitHub prikazuje.
  404 znaci da je repo privatan ili obrisan; kod firmi iz akceleratora to
  najcesce znaci da je kod presao u privatni repo, ne da je projekat mrtav.

## Kratko

1. **Plasman odlucuje o akceleratoru, ne track.** Od 293 nagradjena projekta
   (Copilot, 4 hakatona) u akcelerator je uslo: 1. mesto 16/26, 2. mesto 13/26,
   3. mesto 6/26, 4. i 5. mesto po 2/26, Honorable Mention 10/141, Grand Prize
   4/4. Na Frontieru, prvom hakatonu bez track-ova, 19 od 26 glavnih
   pobednika (Grand Champion + 25) uslo je u C5; od 16 HM nijedan.
2. **RWA, Consumer i DePIN track vise ne postoje.** Frontier (apr 2026) je
   ukinuo sve track-ove, a Crypto World's Fair ima track-ove po ekosistemu
   (vidi `hackathon.md`). Pitanje je sad kojim jezikom se predstavljamo, ne
   gde se prijavljujemo.
3. **Zuri nagradjuje novac koji se krece kroz proizvod.** 10 od 12 Consumer
   pobednika na 1-3. mestu (2024-2025) i 8 od 8 Frontier pobednika u
   kategoriji Consumer imaju mehaniku trgovanja, kladjenja, predikcije ili
   ulaganja. Svih 8 RWA pobednika na vrhu su finansijski instrumenti ili infrastruktura (krediti,
   prinos, likvidacija, oracle). Svi RWA projekti vezani za fizicku proizvodnju
   (solar, nafta, fosili, krovovi, n=4) stali su na Honorable Mention.
4. **Marketplace fizicke robe nikad nije bio iznad 5. mesta.** Najblizi nama:
   Nomu (5. Consumer, Cypherpunk), pa ponovo pobednik na Frontieru sa novim
   proizvodom i $1M+ GMV, pa C5. store.fun i WearTre: samo HM.
5. **Traction pri prijavi: od nule do stotina hiljada dolara prometa.**
   Home Harvest je 3. u DePIN-u sa repoom opisanim kao "Shell for colosseum
   entry"; Clawpump i DashX na Frontieru navode ~$650K prihoda i $400K+
   mesecno. Traction nije dovoljan sam: ReFi Hub ($491K ulozeno, 18+ meseci)
   i Surgepay ($105K za 30 dana) dobili su samo HM.

## Tabela 1: brojke po track-u (Copilot, 2024-2025)

Prijave po track-u su iz Copilot `/filters`; projekat moze biti u vise
track-ova, pa je stopa priblizna. "Placanja" spaja Payments (Radar),
Stablecoins (Breakout, Cypherpunk) i DeFi & Payments (Renaissance, gde je
vecina pobednika cist DeFi).

| Track | Hakaton | Prijava | Nagradjenih | Stopa | Tim (raspon, medijana) | Kasnije u akceleratoru |
|---|---|---|---|---|---|---|
| RWA | Cypherpunk | 263 | 7 | 2,7% | 1-4, 2 | 0/7 |
| Consumer | Renaissance | 554 | 15 | 2,7% | 1-6, 3 | 2/15 |
| Consumer | Radar | 867 | 8 | 0,9% | 1-6, 2 | 2/8 |
| Consumer | Breakout | 923 | 11 | 1,2% | 1-8, 2 | 3/11 |
| Consumer | Cypherpunk | 1.090 | 12 | 1,1% | 1-8, 2 | 4/12 |
| DePIN | Renaissance | 127 | 12 | 9,4% | 1-15, 3,5 | 3/12 |
| DePIN | Radar | 163 | 7 | 4,3% | 2-5, 4 | 1/7 |
| DePIN | Breakout | 187 | 9 | 4,8% | 1-6, 2 | 0/9 |
| Placanja | Renaissance | 355 | 21 | 5,9% | 1-6, 3 | 2/21 |
| Placanja | Radar | 324 | 9 | 2,8% | 1-4, 3 | 1/9 |
| Placanja | Breakout | 214 | 15 | 7,0% | 1-4, 3 | 5/15 |
| Placanja | Cypherpunk | 271 | 8 | 3,0% | 1-4, 2 | 3/8 |
| Glavne nagrade | sva 4 | - | 15 | - | 1-11, 2 | 5/15 |

Izvor: Copilot `/filters` i `/projects/by-slug`, 2026-09-24.

## Tabela 2: akcelerator po plasmanu (svih 293 nagradjenih, Copilot)

| Plasman | Nagradjenih | Kasnije u akceleratoru |
|---|---|---|
| Grand Prize | 4 | 4 |
| 1. mesto u track-u | 26 | 16 |
| 2. mesto | 26 | 13 |
| 3. mesto | 26 | 6 |
| 4. mesto | 26 | 2 |
| 5. mesto | 26 | 2 |
| 6. mesto (Breakout univerzitetske) | 7 | 0 |
| Honorable Mention | 141 | 10 |
| Public Goods, Climate, Mobile, University | 11 | 1 |

Frontier 2026 (blog + portfolio): Grand Champion i 25 "top" pobednika = 26,
od toga 19 u C5. 16 HM, od toga 0 u C5. Public Goods (Zoneless) u C5. C5
ukupno ima 21 firmu; jedina koja nije sa Frontier liste je Laso Finance.

## Tabela 3: Frontier 2026 (apr-maj 2026, bez track-ova, 2.857 prijava)

Nagrade: Grand Champion $30.000; "20 standout teams" po $10.000 po stranici
hakatona (https://colosseum.com/frontier), a blog kaze da su posle dodali jos
pet timova. Iznos po projektu na stranicama projekata nije upisan, pa ga
ovde ne pisemo. Kategoriju bira tim sam pri prijavi.

| Projekat | Nagrada | Kategorija (tim bira) | Zemlja | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | C5 | Sajt danas | Pitch video |
|---|---|---|---|---|---|---|---|---|---|
| [CrowdBrain](https://colosseum.com/projects/explore/crowdbrain) | Grand Prize | DePIN | Georgia | 2 | "CrowdBrain is a vertically integrated robotics work network." | nije navedeno u opisu | da | [200](https://crowdbrain.ai/) | [link](https://youtu.be/tI7T3X5IRT8) |
| [Clawpump](https://colosseum.com/projects/explore/clawpump) | Top 25 | AI Platforms / Agents | United States | 2 | "The house of agentic finance." | "We processed $65M+ volume. 3K+ agents. ~$650K in rev" | da | [nije provereno](https://agents.clawpump.tech/) | [link](https://youtu.be/JvCu5Z_UCBE) |
| [Nomu](https://colosseum.com/projects/explore/nomu-1) | Top 25 | AI Platforms / Agents | United Arab Emirates | 4 | "Nomu is the first supply chain autopilot for consumer brands We're 4 builders from SwissBorg, Alibaba, Uni of Oxford & 42 Blockcha..." | "selling 1M in blind boxes w/ MonkeDAO & dVIN" (Cypherpunk proizvod) | da | [200 (preusmerava na nomu.store)](https://www.nomu.dev/) | [link](https://youtu.be/T8xDHGzF7-c) |
| [Bench](https://colosseum.com/projects/explore/bench) | Top 25 | Consumer Apps | Germany | 2 | "Bench is a platform for Opportunity Markets." | nije navedeno u opisu | ne | [200](https://bench.markets) | [link](https://youtu.be/KzThM5inxZM) |
| [Cesto (Prev Lomen)](https://colosseum.com/projects/explore/cesto-(prev-lomen)) | Top 25 | Consumer Apps | United Kingdom | 5 | "At Cesto, we enable retail investors to go from idea to trade in one click." | nije navedeno u opisu | da | [200](https://cesto.co) | [link](https://www.youtube.com/watch?v=K403sxMa4D0) |
| [JK Index](https://colosseum.com/projects/explore/jk-index) | Top 25 | Consumer Apps | United States | 2 | "The JK Index is a collector-first truth layer for trading cards." | nije navedeno u opisu | da | [200](https://jkindex.io) | [link](https://youtu.be/FS4BMr0ol2w) |
| [Mentioned](https://colosseum.com/projects/explore/mentioned) | Top 25 | Consumer Apps | Northern Ireland | 2 | "Wherever words are spoken, a mention market can be built." | nije navedeno u opisu | ne | [200](https://www.mentioned.market/) | [link](https://www.youtube.com/watch?v=j3bUhq7j7t4) |
| [One Arena](https://colosseum.com/projects/explore/one-arena) | Top 25 | Consumer Apps | Japan | 2 | "Battle and profit with onchain trading cards." | nije navedeno u opisu | da | [200](https://www.onearena.xyz/) | [link](https://www.loom.com/share/23519b1b9d1042b2b5bdac95db452b1a) |
| [Peaks](https://colosseum.com/projects/explore/peaks) | Top 25 | Consumer Apps | United States | 2 | "Peaks is the consumer app for investing in any idea." | nije navedeno u opisu | da | [200](https://peaks.trade) | [link](https://youtu.be/PjcMm6bq6KU) |
| [TRADED.GG](https://colosseum.com/projects/explore/traded.gg) | Top 25 | Consumer Apps | Indonesia | 1 | "Traded: The Onchain TCG Super App.Think OpenSea meets FOMO, built for the tokenized card era." | "Search, Radar, Alerts, and Collection are live today" | da | [200](https://traded.gg) | [link](https://youtube.com/shorts/Y3gm5wvyOOQ) |
| [WeLikeSports](https://colosseum.com/projects/explore/welikesports) | Top 25 | Consumer Apps | United States | 3 | "WeLikeSports is building the next great fantasy sports platform." | nije navedeno u opisu | da | [200](https://welikesports.com/) | [link](https://www.youtube.com/watch?v=02NsuZcko3Q) |
| [Flovia](https://colosseum.com/projects/explore/flovia) | Top 25 | Data & Analytics | United States | 4 | "Flovia is the growth analytics & intelligence for machine-paid APIs." | nije navedeno u opisu | da | [nije provereno](https://www.flovia402.com/) | [link](https://www.loom.com/share/68a7cd7b5ec94036804c0fd21888b02e) |
| [YieldCompass](https://colosseum.com/projects/explore/yieldcompass) | Top 25 | Data & Analytics | Mauritius | 2 | "We’re building the Moody’s of Solana DeFi." | nije navedeno u opisu | ne | [nije provereno](https://yieldcompass.fi/) | [link](https://www.loom.com/share/ecf22a9a07214f0fb5a367907b56204b) |
| [Dr. Fraudsworths' Fantastical Finance Factory](https://colosseum.com/projects/explore/dr.-fraudsworths'-fantastical-finance-factory) | Top 25 | DeFi | United Kingdom | 1 | "Fraudsworth is a novel approach to creating a new kind of non-sovereign store of value." | nije navedeno u opisu | da | [nije provereno](https://fraudsworth.fun) | [link](https://youtu.be/BtfWYYlukpY) |
| [Dropset](https://colosseum.com/projects/explore/dropset) | Top 25 | DeFi | United States | 1 | "DASMAC (dasmac.com) is building Dropset, a fully onchain central limit order book on Solana L1: the real infrastructure behind the..." | nije navedeno u opisu | da | nije provereno | [link](https://www.youtube.com/@dasmac_com) |
| [Memetic Machines / War Machine](https://colosseum.com/projects/explore/memetic-machines-war-machine) | Top 25 | DeFi | Malaysia | 3 | "WARMACHINE.FUN is programmable news that turns high-frequency geopolitical events into tradeable YES/NO markets structured within ..." | nije navedeno u opisu | ne | [nije provereno](https://warmachine.fun/) | [link](https://www.youtube.com/watch?v=ZcqaQ32kH2I) |
| [Senthos](https://colosseum.com/projects/explore/senthos) | Top 25 | DeFi | United States | 2 | "Senthos is a Solana-native structured-product protocol for prediction markets." | nije navedeno u opisu | da | [nije provereno](https://senthos.xyz/) | [link](https://youtu.be/D41bJcQ7lwI) |
| [DashX](https://colosseum.com/projects/explore/dashx-1) | Top 25 | FinTech | India | 2 | "DashX is the stablecoin infra for compliant cross border payments, aimed for emerging markets like India." | "Processing $400K+/month and doubling MoM" | da | [200](https://dashx.xyz) | [link](https://youtu.be/5VwLyFpi6aw) |
| [KinnectFi](https://colosseum.com/projects/explore/kinnectfi) | Top 25 | FinTech | United States | 2 | "KinnectFi is a dual-jurisdiction neobank designed for the 10-million-strong Philippine diaspora." | nije navedeno u opisu | da | [ne odgovara](https://kinnectfi.me/) | [link](https://youtu.be/vnLTYbmrCS8) |
| [stablecorp](https://colosseum.com/projects/explore/stablecorp) | Top 25 | FinTech | Germany | 3 | "StableCorp is the business infrastructure for remote founders earning in stablecoins." | nije navedeno u opisu | da | [200 (mystablecorp.xyz)](https://mystablecorp.com) | [link](https://youtu.be/un1Nbsn2FFI) |
| [The Syndicate](https://colosseum.com/projects/explore/the-syndicate) | Top 25 | Gaming | United Kingdom | 3 | "You run a crew. Your crew earns money while you sleep. The Syndicate is a no-token, skill-weighted, provably auditable mafia card " | nije navedeno u opisu | da | [nije provereno](https://thesyndicate.games) | [link](https://youtu.be/nvI9xx_EMeE) |
| [Crafts](https://colosseum.com/projects/explore/crafts-1) | Top 25 | Real World Assets (RWA) | Germany | 4 | "Crafts is a Solana platform for Stakeholder Token Offerings: a new way for startups to raise with equity-linked tokens." | nije navedeno u opisu | ne | [403 (Cloudflare provera)](https://crafts.dev/) | [link](https://youtu.be/4HIgikZlpb8) |
| [Housd](https://colosseum.com/projects/explore/housd) | Top 25 | Real World Assets (RWA) | Germany | 2 | "housd is the onchain vault for residential real estate credit." | nije navedeno u opisu | da | [200](https://housd.finance/) | [link](https://www.loom.com/share/19523c259aea43c7815366c2277004e7) |
| [ODL (On-Demand Liquidity)](https://colosseum.com/projects/explore/odl-(on-demand-liquidity)) | Top 25 | Real World Assets (RWA) | United States | 1 | "ODL is a RWA liquidator platform allowing liquidator funds to buy discounted RWAs and re-sell them to TradFi buyers initially focu..." | nije navedeno u opisu | da | [200](https://rwaodl.com) | [link](https://youtu.be/88UeTrR8_gs) |
| [Sudont](https://colosseum.com/projects/explore/sudont) | Top 25 | Security Tools | United States | 1 | "The bare-metal execution firewall and local RPC for Solana." | nije navedeno u opisu | ne | [nije provereno](https://sudont.xyz) | [link](https://www.loom.com/share/8d10d5f2f2384133b5b0f63897fb098f) |
| [Alpha Group Trading](https://colosseum.com/projects/explore/alpha-group-trading) | Top 25 | Social / SocialFi | United States | 1 | "Alpha is a mobile trading app where groups of friends trade, chat and collaborate." | "Currently in closed beta" | ne | [200](https://alpha-labs.trade/) | [link](https://www.loom.com/share/bdb6d071ca1e4d2b9374e3f732c833d6) |
| [IOChain](https://colosseum.com/projects/explore/iochain) | University Award | DePIN | Ireland {Republic} | 1 | "AI is racing to build new data centres while the GPUs we already have sit at 5% utilisation." | nije navedeno u opisu | ne | [200](https://www.iochain.dev) | [link](https://youtu.be/JFipqMqOm04) |
| [Zoneless](https://colosseum.com/projects/explore/zoneless) | Public Goods Award | Developer Infrastructure | United Kingdom | 1 | "Zoneless is an open-source alternative to Stripe Connect using USDC on Solana." | nije navedeno u opisu | da | [nije provereno](https://zoneless.com) | [link](https://www.loom.com/share/882950ca0b3e48598748437fd9e32031) |
| [Arete](https://colosseum.com/projects/explore/arete) | HM | AI Platforms / Agents | United Kingdom | 3 | "Code is increasingly written by agents, but Solana's SDKs, RPCs, and tooling were built for humans." | nije navedeno u opisu | ne | [nije provereno](https://arete.run) | [link](https://www.loom.com/share/a30c4d2b406843cebe9c4da48a73d239) |
| [Portara](https://colosseum.com/projects/explore/portara) | HM | AI Platforms / Agents | Hong Kong | 2 | "The infrastructure layer for AI to reliably control trading across all financial products including Solana." | nije navedeno u opisu | ne | [nije provereno](https://portara.xyz) | [link](https://youtube.com/shorts/pYZP-spiwlY) |
| [Hobba](https://colosseum.com/projects/explore/hobba-1) | HM | DeFi | Croatia | 2 | "Hobba is a prime broker for onchain loans." | nije navedeno u opisu | ne | [nije provereno](https://hobba.io) | [link](https://www.loom.com/share/15c830824e2d4d30be8a0a943b51b2f6) |
| [Kestrel Protocol](https://colosseum.com/projects/explore/kestrel-protocol) | HM | DeFi | Canada | 2 | "Active DeFi strategies packaged into liquid tokens you simply hold." | nije navedeno u opisu | ne | nije provereno | [link](https://www.youtube.com/watch?v=-QAJTxsld9Q) |
| [ordr.trade](https://colosseum.com/projects/explore/ordr.trade) | HM | DeFi | India | 4 | "A fully on chain order book exchange leveraging ACE on Solana that gives market makers their own private accounts, cheap repricing..." | nije navedeno u opisu | ne | [nije provereno](https://www.ordr.trade/) | [link](https://youtu.be/hKRRqPOiH-g) |
| [Ride Markets](https://colosseum.com/projects/explore/ride-markets) | HM | DeFi | Poland | 3 | "Ride Markets is an onchain prop firm built on futarchy." | "Live on Solana mainnet with two funds running in private beta" | ne | [nije provereno](https://ride.markets) | [link](https://www.loom.com/share/cd1dd4865114429cac8cf07c68e0fbd5) |
| [Almanac](https://colosseum.com/projects/explore/almanac) | HM | Developer Infrastructure | Canada | 2 | "Almanac is an MCP that gives AI agents optimized recipes for navigating websites." | nije navedeno u opisu | ne | [nije provereno](https://almanac.boilerroom.tech/) | [link](https://www.youtube.com/watch?v=NxDWFuZh4ck&t) |
| [Latinum](https://colosseum.com/projects/explore/latinum) | HM | Developer Infrastructure | Ireland {Republic} | 1 | "Formal verification for smart contracts." | nije navedeno u opisu | ne | [nije provereno](https://latinum.ai/) | [link](https://youtu.be/MCIl858wQUE) |
| [riven](https://colosseum.com/projects/explore/riven) | HM | Payments & Remittance | India | 1 | "Riven is the financial control layer for humans and AI agents on Solana." | nije navedeno u opisu | ne | [200](https://beta.riven.cash) | [link](https://youtu.be/VmsIGFi8wTw) |
| [Ryvo Network](https://colosseum.com/projects/explore/ryvo-network) | HM | Payments & Remittance | Georgia | 1 | "Ryvo is a non-custodial clearing layer for high-frequency machine payments on Solana." | nije navedeno u opisu | ne | [200](https://ryvo.network) | [link](https://www.loom.com/share/46ed15bf1dc54421b4075498f4c27142) |
| [Surgepay: WhatsApp first remittance. US → India. In Seconds. No Fees. Google Rates](https://colosseum.com/projects/explore/surgepay:-whatsapp-first-remittance.-us-india.-in-seconds.-no-fees.-google-rates) | HM | Payments & Remittance | Singapore | 4 | "Surgepay lets you send money from the US to India on WhatsApp." | "$105K moved in 30 days. 80% repeat" | ne | [200](https://www.surgepay.money/) | [link](https://www.loom.com/share/6048cb1530e44d94858281e6f2e4afad) |
| [BORE.OIL](https://colosseum.com/projects/explore/bore.oil) | HM | Real World Assets (RWA) | Canada | 1 | "BORE.OIL tokenizes real oil royalties on Solana, built natively on the Solana Developer Platform (SDP)." | partnerstvo sa proizvodjacem nafte sa TSXV berze | ne | [borefi.com ne odgovara](https://www.borefi.com) | [link](https://youtu.be/G0m_jLXr55Q) |
| [Jurassic Finance](https://colosseum.com/projects/explore/jurassic-finance) | HM | Real World Assets (RWA) | Serbia | 3 | "Dinosaur fossils have quietly become one of the financially best performing alternative assets on the planet." | nije navedeno u opisu | ne | [200](https://jurassic.finance/) | [link](https://www.youtube.com/watch?v=JmleY4cfpn8) |
| [ReFi Hub](https://colosseum.com/projects/explore/refi-hub-2) | HM | Real World Assets (RWA) | Canada | 5 | "ReFi Hub tokenizes operating solar plants on Solana." | "$491K deployed, 14% realized IRR, 18+ months, zero defaults" | ne | [200](https://www.refihub.io/) | [link](https://www.loom.com/share/b4b7452c85574a95811de18d40b779f5) |
| [Nora Finance](https://colosseum.com/projects/explore/nora-finance) | HM | Stablecoins | Brazil | 3 | "Brazilian Real stablecoin infrastructure for neobanks, ramps, DeFi protocols, and tokenized asset issuers." | nije navedeno u opisu | ne | [200](https://www.nora.finance/) | [link](https://www.youtube.com/watch?v=eAVDgc-v66s) |
| [Encrypt](https://colosseum.com/projects/explore/encrypt) | HM | ZK / Crypto Research | United Kingdom | 1 | "Encrypt is the most advanced FHE (Fully Homomorphic Encryption) network, built for Solana with state-of-the-art cryptography resea..." | "live on Solana devnet" | ne | [nije provereno](https://encrypt.xyz) | [link](https://youtu.be/k-a2gqUU_fM) |

## Tabela 4: pobednici po track-u (Copilot, 2024-2025)

Linkovi na Colosseum stranice, GitHub i pitch video su iz Copilota.

### RWA


**Cypherpunk (sept 2025)** (n=7)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Autonom - Unleashing RWAs in Solana](https://colosseum.com/projects/explore/autonom-unleashing-rwas-in-solana) | 1st - RWAs | 25.000 | 2 | "Apart from Ostium (one standalone perp DEX), RWAs and particularly equities haven’t really hit perps or at least not in Solana." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/28d00e8aaee94d7cb680f6786488c47b) |
| [BORE.FI](https://colosseum.com/projects/explore/bore.fi-1) | 2nd - RWAs | 20.000 | 2 | "The world is full of wonderfully boring, cash flowing, profitable businesses." | nije navedeno u opisu | ne | [2026-02-23](https://github.com/RentityTT/borefi) | [link](https://www.loom.com/share/5a90b4c6c9b64f78af110097ac04d158) |
| [Legasi](https://colosseum.com/projects/explore/legasi) | 3rd - RWAs | 15.000 | 2 | "Legasi brings institutional-grade, long-term lending to the digital age through crypto-backed Lombard loans." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=00IXBqJhUaA) |
| [Pencil Finance](https://colosseum.com/projects/explore/pencil-finance-1) | 4th - RWAs | 10.000 | 1 | "Pencil Finance is the first DeFi protocol to bring real-world student loans on-chain, creating a new yield-bearing asset class bac..." | nije navedeno u opisu | ne | [2025-10-28](https://github.com/zvy22606/pencil-finance-contract-solana) | [link](https://www.loom.com/share/5b5ab5e7298043f190ba80a3f193a542) |
| [Watchtower](https://colosseum.com/projects/explore/watchtower) | 5th - RWAs | 5.000 | 1 | "Enabling onchain asset-backed financing for space infrastructure projects" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/3a1976629dae43fa8ec314743b428190) |
| [VitalFi](https://colosseum.com/projects/explore/vitalfi) | HM - RWAs | - | 4 | "VitalFi is a Solana-based DeFi protocol that tokenizes Brazilian medical receivables, allowing users to deposit USDT into transpar..." | nije navedeno u opisu | ne | [2025-10-30](https://github.com/credit-markets/cypherpunk) | [link](https://youtu.be/UgupRFrYzd8) |
| [CREAM](https://colosseum.com/projects/explore/cream) | HM - RWAs | - | 2 | "CREAM is a Decentralized Energy Grid on Solana." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=Ebl7QcO5bjA) |

### Consumer


**Renaissance (mart 2024)** (n=15)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Banger](https://colosseum.com/projects/explore/banger) | 1st - Consumer Apps | 30.000 | 2 | "Buy and sell tweets while supporting creators, having fun, and making money." | nije navedeno u opisu | C1 (Banger) | 404 (privatan ili obrisan) | [link](https://youtu.be/XdKEDNxxkyY) |
| [WootzApp Browser](https://colosseum.com/projects/explore/wootzapp-browser) | 2nd - Consumer Apps | 20.000 | 1 | "WootzApp is the Browser that Pays you for helping Generative AI!" | nije navedeno u opisu | ne | [2025-10-05](https://github.com/wootzapp/wootz-browser) | [link](https://www.loom.com/share/21c164d55dc044e4813d2305e0a67100) |
| [Chomp](https://colosseum.com/projects/explore/chomp) | 3rd - Consumer Apps | 15.000 | 6 | "Chomp, a gamified social consensus platform that gets you best-in-class insights." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/11ba13128c1245059699d4e68a7d268b?sid=97ce3d0d-f9dc-4cb0-9d80-baa5341299c7) |
| [Movement](https://colosseum.com/projects/explore/movement) | 4th - Consumer Apps | 10.000 | 2 | "Memecoins are absolutely blowing up, but it’s too hard for most people to get started." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=zRezAA2xA8w) |
| [DePlan](https://colosseum.com/projects/explore/deplan) | 5th - Consumer Apps | 5.000 | 4 | "The sustainable internet with no subscriptions." | nije navedeno u opisu | ne | [org](https://github.com/orgs/deplan-xyz/repositories), repo nije proveren | [link](https://vimeo.com/931008211) |
| [LET'S COOK](https://colosseum.com/projects/explore/let's-cook) | HM - Consumer Apps | - | 3 | "LET'S COOK is a comprehensive MemeFi platform." | nije navedeno u opisu | ne | [2025-03-01](https://github.com/daoplays/LetsCook) | [link](https://docs.google.com/presentation/d/1rAOY-GljEr28bX7NI6kGGdhRMUKmawwFw6JpuZHiphQ/edit?usp=sharing) |
| [Unruggable](https://colosseum.com/projects/explore/unruggable-1) | HM - Consumer Apps | - | 3 | "Unruggable is a security/privacy focused soft/hard wallet designed specifically for solana that protects users from the most commo..." | nije navedeno u opisu | C4 (Unruggable) | [2024-10-09](https://github.com/hogyzen12/unruggable) | [link](https://www.loom.com/share/85d542954c5c436c997bba28606ebf8e?sid=e339c305-43fd-4bfd-b1e3-a8a4d388fb25) |
| [K3N](https://colosseum.com/projects/explore/k3n) | HM - Consumer Apps | - | 3 | "K3N is a marketplace for digital marketing services specifically designed for the Web3 ecosystem." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/dAXnVdnYV-Y) |
| [WearTre](https://colosseum.com/projects/explore/weartre) | HM - Consumer Apps | - | 3 | "WearTre is a marketplace mobile app with web3 integration where individuals, brands, projects, influencers, local shops can list, ..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=VmCG2zb6P-U) |
| [Trekn](https://colosseum.com/projects/explore/trekn-1) | HM - Consumer Apps | - | 6 | "Trekn is a decentralized social mapping platform that lets you earn by sharing and contributing valuable data of places in your lo..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/a_taYNd9ZZQ?feature=shared) |
| [Aloy](https://colosseum.com/projects/explore/aloy) | HM - Consumer Apps | - | 2 | "Aloy is a loyalty platform for the ONDC network built using Solana for the future of e-commerce in India." | nije navedeno u opisu | ne | [2024-04-09](https://github.com/abhishekraj2506/aloy-renaissance) | [link](https://www.youtube.com/watch?v=rBwwuwoYDDQ) |
| [Fastmind](https://colosseum.com/projects/explore/fastmind) | HM - Consumer Apps | - | 4 | "The AI productivity app that decentralizes accountability using voice activated smart contracts." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://docsend.com/view/z6npfptzecmehvr3) |
| [SyncLink](https://colosseum.com/projects/explore/synclink-1) | HM - Consumer Apps | - | 1 | "SyncLink streamlines your Solana experience by offering seamless multi-wallet management and dApp connectivity, all through a user..." | nije navedeno u opisu | ne | [org](https://github.com/SyncLink-renaissance), repo nije proveren | [link](https://pitch.com/v/synclink-xyab8u) |
| [GCaller](https://colosseum.com/projects/explore/gcaller-1) | HM - Consumer Apps | - | 3 | "GCaller is a decentralised caller ID and spam protection platform, rewarding users to identify spam!" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://dub.sh/gcaller) |
| [Oridion](https://colosseum.com/projects/explore/oridion) | HM - Consumer Apps | - | 1 | "Simple application that adds a buffer between your public and private wallets." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/9d4d147123dc4f568da24a84bcd41287?sid=13aff9b6-558f-4c73-a7ee-ab463a4cc548) |

**Radar (sept 2024)** (n=8)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Pregame](https://colosseum.com/projects/explore/pregame) | 1st - Consumer | 25.000 | 1 | "A platform that lets you bet against anyone online in a trustless manner." | nije navedeno u opisu | C2 (Pregame) | 404 (privatan ili obrisan) | [link](https://www.tella.tv/video/trustless-peer-to-peer-betting-c2fs) |
| [Trenches.top](https://colosseum.com/projects/explore/trenches.top) | 2nd - Consumer | 20.000 | 3 | "Trenches dot top is the first platform to tokenize the reputation of memecoins alpha callers on Solana It’s pretty simple, alpha c..." | nije navedeno u opisu | C2 (Trenches.Top) | 404 (privatan ili obrisan) | [link](https://bit.ly/Trenches_top_Colosseum) |
| [Genesis](https://colosseum.com/projects/explore/genesis) | 3rd - Consumer | 15.000 | 6 | "🪙 Fractional & Tokenized IP investing" | nije navedeno u opisu | ne | [2025-02-28](https://github.com/d-reader-organization/genesis-web) | [link](https://drive.google.com/file/d/1FgFlGzUDb-nbXUc4IwfF9v5U3pmrFOuV/view?usp=sharing) |
| [Fanplay](https://colosseum.com/projects/explore/fanplay) | 4th - Consumer | 10.000 | 1 | "Fanplay is creating The Degen's Playground, a wild space featuring social prediction markets, live hamster racing, social wagering..." | "3M+ views on social, 100K site visits, 10K wallets created, and 10K transactions" | ne | [2025-04-08](https://github.com/Periondao/sol-fanplay) | [link](https://www.loom.com/share/76efba52a26b4749b00c82cdcbf5fc7f) |
| [Wink](https://colosseum.com/projects/explore/wink) | 5th - Consumer | 5.000 | 6 | "Wink is a transaction marketplace that allows users to create, engage, and monetize decentralized applications (dApps) on Solana t..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/BGSRcORXKPU) |
| [Blinkord](https://colosseum.com/projects/explore/blinkord) | HM - Consumer | - | 2 | "Blinkord is a platform and tool which helps Discord community owners enable Solana interactions directly within their Discord serv..." | nije navedeno u opisu | ne | [2026-08-15](https://github.com/dimitrov-d/blinkord) | [link](https://www.youtube.com/watch?v=ieCwnTNxcvc) |
| [Alora](https://colosseum.com/projects/explore/alora) | HM - Consumer | - | 2 | "A platform that lets people form groups around the podcasts they love." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/87a24d7dcae446b4bc0af41593be267d?sid=7054e66c-39cd-486b-9877-c8ffbbb818a5) |
| [HYPE3](https://colosseum.com/projects/explore/hype3) | HM - Consumer | - | 2 | "Create a free token pre-launch with auto refund below 85 $SOL raise." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.dropbox.com/scl/fi/e0n5d0pqiaxzff72n2qjj/colosseum-3mins.mp4?rlkey=217ule6hkv0re6fmj2ddxaqrt&e=1&dl=0) |

**Breakout (apr 2025)** (n=11)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Trepa](https://colosseum.com/projects/explore/trepa) | 1st - Consumer Apps | 25.000 | 5 | "Trepa is a sentiment prediction mobile app." | nije navedeno u opisu | C3 (Trepa) | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=pAucQK_BrMY) |
| [Melee Markets](https://colosseum.com/projects/explore/melee-markets) | 2nd - Consumer Apps | 20.000 | 8 | "Melee is a viral market platform blending PumpFun-style speculation with Polymarket-style prediction markets." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/lUFJZ-2vQwI) |
| [TypeX Keyboard](https://colosseum.com/projects/explore/typex-keyboard) | 3rd - Consumer Apps | 15.000 | 2 | "TypeX is a keyboard app that transforms user input value into on-chain assets, offering a seamless trading experience and aiming t..." | nije navedeno u opisu | C3 (TypeX Keyboard) | [2025-05-15](https://github.com/TypeX-Keyboard/android) | [link](https://youtu.be/N7M2nbpToWs) |
| [Glympse.fun](https://colosseum.com/projects/explore/glympse.fun) | 4th - Consumer Apps | 10.000 | 3 | "Glympse.fun is fantasy sports for Web2 attention, where creators earn as others bet on their performance." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/f9883f15bfd142269ab42eec59218edc?sid=f9317c22-7566-433a-8905-ad5e362702ec) |
| [Deks](https://colosseum.com/projects/explore/deks) | 5th - Consumer Apps | 5.000 | 4 | "Deks is a platform that simplifies crypto onboarding for communities through digital gift cards, physical cards, and seamless fiat..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=CS3mDnziAMY&ab_channel=Deks) |
| [ClipStake](https://colosseum.com/projects/explore/clipstake) | University Prize - Consumer Apps | 2.500 | 2 | "ClipStake is a launchpad that enables content creators to raise funds for their video projects by tokenizing their future ad reven..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/xZuw1SDrkIw) |
| [Poll - Bet With Friends](https://colosseum.com/projects/explore/poll-bet-with-friends) | HM - Consumer Apps | 5.000 | 1 | "Bet on anything against friends with iMessage and Apple Pay." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/11027b6582c048a885cc384c8bea685e?sid=17f1b8a4-afcf-497d-b5d2-ea4cc1201e0c) |
| [store.fun (e-commerce marketplace on solana)](https://colosseum.com/projects/explore/store.fun-(e-commerce-marketplace-on-solana)) | HM - Consumer Apps | 5.000 | 1 | "Fast, on-chain shopping with SOL payments, and zero signups." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/97c5084b388142a2a600306e9be631d9?sid=81ec4b86-4ed1-4ee9-bfce-65d676f45c82) |
| [deplay](https://colosseum.com/projects/explore/deplay-1) | HM - Consumer Apps | 5.000 | 1 | "Spotify on Solana, turning every listener into a launchpad." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1085018165) |
| [Riverboat](https://colosseum.com/projects/explore/riverboat) | HM - Consumer Apps | 5.000 | 2 | "A blueprint for decentralized liquidity and multiple outcomes in prediction markets" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1085070289/d9916572ea?ts=0&share=copy) |
| [grid.wtf](https://colosseum.com/projects/explore/grid.wtf) | HM - Consumer Apps | 5.000 | 2 | "Figma for Trading. The Grid is building a new way to interact with financial markets, where anyone can create their own trading in" | nije navedeno u opisu | C2 (AlphaFC) | 404 (privatan ili obrisan) | [link](https://vimeo.com/1084426892?share=copy) |

**Cypherpunk (sept 2025)** (n=12)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Capitola](https://colosseum.com/projects/explore/capitola) | 1st - Consumer Apps | 25.000 | 1 | "Capitola is a prediction markets meta-aggregator that enables users to trade all events at the best price." | nije navedeno u opisu | C4 (Capitola Labs) | 404 (privatan ili obrisan) | [link](https://youtu.be/dlZzcUcGkH0) |
| [Superfan](https://colosseum.com/projects/explore/superfan) | 2nd - Consumer Apps | 20.000 | 1 | "Superfan is a meta-record label, turning fan belief into artist credit through futarchy curation." | nije navedeno u opisu | C4 (Superfan) | [2025-10-23](https://github.com/kevinknielsen/superfan-core) | [link](https://www.loom.com/share/616bb4a6dba94d1faeaae8465a13463d) |
| [Fora](https://colosseum.com/projects/explore/fora) | 3rd - Consumer Apps | 15.000 | 2 | "Fora is a group chat based trading platform and prediction market protocol" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/1fb0051360f448fa97bf922bb00c8eeb) |
| [toaster.trade](https://colosseum.com/projects/explore/toaster.trade) | 4th - Consumer Apps | 10.000 | 2 | "TikTok of casual trading for Solana, powered by Hyperliquid" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/a0facf4c80e0430e8578a8dc3faed259) |
| [Nomu](https://colosseum.com/projects/explore/nomu) | 5th - Consumer Apps | 5.000 | 4 | "Nomu is the marketplace where you can buy products early and get rewarded when they sell." | nije navedeno u opisu | C5 (Nomu) | 404 (privatan ili obrisan) | [link](https://youtu.be/nsXlkmtBurY) |
| [DOLERO](https://colosseum.com/projects/explore/dolero) | HM - Consumer Apps | - | 2 | "A decentralized 1v1 card game inspired by Blackjack mechanics; fully on-chain." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1130256136) |
| [Pyro](https://colosseum.com/projects/explore/pyro) | HM - Consumer Apps | - | 2 | "Pyro is a sponsorship marketplace on Solana that connects Pump.fun livestreamers with Web3 brands." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1132388099?share=copy&fl=sv&fe=ci) |
| [SeekerOS: Agentic Operating System for the Solana Seeker](https://colosseum.com/projects/explore/seekeros:-agentic-operating-system-for-the-solana-seeker) | HM - Consumer Apps | - | 1 | "The Solana phone promised freedom." | nije navedeno u opisu | ne | [2025-10-31](https://github.com/Nelis-sol/seekeros) | [link](https://www.loom.com/share/57bb62cbe012412685aad028f0cd2e4e) |
| [FEELS.FUN](https://colosseum.com/projects/explore/feels.fun) | HM - Consumer Apps | - | 3 | "FEELS is building the first mathematically unruggable DEX on Solana, addressing the catastrophic 98.6% failure rate of token launc..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=W4dWKi_NH5s) |
| [Ralli Sports](https://colosseum.com/projects/explore/ralli-sports) | HM - Consumer Apps | - | 8 | "Ralli Sports is a fantasy sports app that provides novel ways to play fantasy against your friends." | nije navedeno u opisu | C1 (Banger) | [2025-12-23](https://github.com/RalliSports/mono) | [link](https://www.loom.com/share/aa7ea577d221432d8ccd8fdca68a4379) |
| [TBD](https://colosseum.com/projects/explore/tbd-1) | HM - Consumer Apps | - | 3 | "- TBD’s mission is to build the market-leading protocol to collect, predict, and surface human sentiment - TBD has two major compo..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/6f1f731514ac4f608dbacfe44081bed2) |
| [here.](https://colosseum.com/projects/explore/here.) | HM - Consumer Apps | - | 2 | "Seeker-exclusive social: capture timestamped photos, optionally add GPS proof, auto-mint to Solana, and earn when your posts drive..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/VLCC3gDor3g) |

### DePIN


**Renaissance (mart 2024)** (n=12)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [BlockMesh Network](https://colosseum.com/projects/explore/blockmesh-network) | 1st - DePin | 30.000 | 2 | "BlockMesh, an innovative, open and secure network that allows you to easily monetize your excess bandwidth." | nije navedeno u opisu | C1 (BlockMesh) | 404 (privatan ili obrisan) | [link](https://docs.google.com/presentation/d/16yqwxWx3vHPVmdpsko9U76sAowi9L-8yrc9wmfwEIok/edit?usp=sharing) |
| [DeCharge](https://colosseum.com/projects/explore/decharge) | 2nd - DePin | 20.000 | 9 | "DeCharge revolutionises EV charging with DePIN technology, offering globally compatible, lightweight hardware for affordable acces..." | nije navedeno u opisu | C1 (DeCharge) | [2024-04-08](https://github.com/drprk/DeCharge1.0) | [link](https://drive.google.com/drive/folders/1-Dq4HaaE2s8fP3JZQJNgAnPF3Pp2aLe0?usp=sharing) |
| [dBunker](https://colosseum.com/projects/explore/dbunker) | 3rd - DePin | 15.000 | 2 | "dBunker is a DePIN Financial Derivatives Platform with an open ecosystem designed to solve the challenges of broader user particip..." | nije navedeno u opisu | C1 (DBunker) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/4399e4b78a764697a90334eefa7bdf18?sid=132450aa-f1d3-4dea-b3b4-551f049f3eca) |
| [CHRO+](https://colosseum.com/projects/explore/chro%2B) | 4th - DePin | 10.000 | 4 | "CHRO+ is creating a decentralized health database to accelerate breakthroughs in predictive, preventive and personalized medicine." | nije navedeno u opisu | ne | [2024-05-22](https://github.com/haruom/chroplus-solana-web) | [link](https://youtu.be/63IMGeum9t8) |
| [Pomerene](https://colosseum.com/projects/explore/pomerene) | 5th - DePin | 5.000 | 3 | "DePIN for International Trade" | nije navedeno u opisu | ne | [2025-03-30](https://github.com/russell-brouillard/hack-api) | [link](https://www.loom.com/share/29b5a92b516749259cd8c18aec7bb0d7?sid=6c5aa2b1-a67f-449c-9f48-d7876693c5f9) |
| [Soltera](https://colosseum.com/projects/explore/soltera) | HM - DePin | - | 2 | "Smart Metering-as-a-Service provider of Advanced Metering Infrastructure Smart Grid Solution in the Philippines." | nije navedeno u opisu | ne | nema | [link](https://drive.google.com/file/d/1r2XIJv5Cmdui9h19dXk-arI3n7R6_Ow0/view?usp=drive_link) |
| [Repl](https://colosseum.com/projects/explore/repl) | HM - DePin | - | 4 | "Repl is building the first unifying trust layer for DePIN networks." | nije navedeno u opisu | ne | [2024-04-08](https://github.com/tancehao/psol_staking) | [link](https://drive.google.com/drive/folders/18MMxNqBS4R0b50kOt8eAPbwP0bADcVc3?usp=sharing) |
| [Hajime AI](https://colosseum.com/projects/explore/hajime-ai) | HM - DePin | - | 3 | "Hajime is a transformative P2P EdgeAI computing network -- A Robot Network fortified with our innovative knowledge sharing and com..." | nije navedeno u opisu | ne | [org](https://github.com/HajimeAI), repo nije proveren | [link](https://youtu.be/isd_7K0VS9k) |
| [SkyTrade - Drones Radar and Air-Rights Marketplace](https://colosseum.com/projects/explore/skytrade-drones-radar-and-air-rights-marketplace) | HM - DePin | - | 15 | "SkyTrade Radar picks up drone signals worldwide and allows you to view and monitor your surroundings for flying drones in real tim..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/U8Jlv9pEI2Q?si=WOleqioDCJGNKf1H) |
| [Blockride](https://colosseum.com/projects/explore/blockride) | HM - DePin | - | 5 | "Blockride is a mobility marketplace bringing equitable access to vehicle financing in Africa." | nije navedeno u opisu | ne | [org](https://github.com/BlockrideNFT-org), repo nije proveren | [link](https://docsend.com/view/5ximtmh26afhdh4r) |
| [CUDIS (From BeatBit Wellness Lab)](https://colosseum.com/projects/explore/cudis-(from-beatbit-wellness-lab)) | HM - DePin | - | 6 | "CUDIS - The first AI-empowered wearable DePIN product that enables data ownership." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/e9b7882d58b84e548ac8e351e73b6a4f?sid=aec84899-9866-409b-805e-2cfa6b282e3d) |
| [BloomSkyX](https://colosseum.com/projects/explore/bloomskyx) | HM - DePin | - | 1 | "The "Starlink" for Weather BloomSkyX is a decentralized AI-centric intelligent weather network." | nije navedeno u opisu | ne | nema | [link](https://www.loom.com/share/7a31fc156d174fdbaf03a56717f967c2?sid=f2362ceb-0cdb-4060-a1af-a711455df526) |

**Radar (sept 2024)** (n=7)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [SvachSakthi](https://colosseum.com/projects/explore/svachsakthi) | 1st - DePin | 25.000 | 2 | "An off-grid cooperative network for promoting Decentralized Renewable energy" | nije navedeno u opisu | C2 (GreenKWh) | nema | [link](https://drive.google.com/file/d/1XI0-9wEjClFWJywuRuJHkLSlorHnkr6e/) |
| [AdX.so - Next generation, decentralized ad exchange](https://colosseum.com/projects/explore/adx.so-next-generation-decentralized-ad-exchange) | 2nd - DePin | 20.000 | 2 | "AdX.so is a next generation decentralized ad exchange and ad network, built on a use-case optimized SVM." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.adx.so/#hackathon) |
| [Cura](https://colosseum.com/projects/explore/cura) | 3rd - DePin | 15.000 | 5 | "CURA introduces the first DePIN+Edge AI smart pet collar, transforming daily dog walks into rewarding experiences that contribute ..." | nije navedeno u opisu | ne | [2024-11-06](https://github.com/PEPALabs/cura_contract_client) | [link](https://www.loom.com/share/e51e4816bece4d338d50bc7b3f16faaa?sid=ca93d810-1af4-4f64-b8ba-753a9f23beae) |
| [NetSepio](https://colosseum.com/projects/explore/netsepio) | 4th - DePin | 10.000 | 4 | "Elevating global cybersecurity with Social DePIN, uniting the world and shattering the digital divide to make the internet safer f..." | nije navedeno u opisu | ne | [org](https://github.com/NetSepio), repo nije proveren | [link](https://www.youtube.com/watch?v=NhYoOdAV76g) |
| [Kiko Network](https://colosseum.com/projects/explore/kiko-network) | 5th - DePin | 5.000 | 2 | "Kiko Network is a DePIN network of user-owned weather stations which is designed to capture microclimate data at an unprecedented ..." | nije navedeno u opisu | ne | [2024-10-07](https://github.com/Kiko-Network/oauth-data) | [link](https://www.loom.com/share/fdba10ede5bf45938023f50706da7492?sid=22a5a072-19d0-47f0-bc46-2fcf94165b87) |
| [UNKOMON - Poop to Earn](https://colosseum.com/projects/explore/unkomon-poop-to-earn) | HM - DePin | - | 5 | "UNKOMON is a "Poop to Earn" project that combines DePIN and gaming." | "13K people joined the waitlist, and 5.6K followers were gained on X" | ne | [2024-11-26](https://github.com/BINARYMONSTERS/UNKOMON) | [link](https://youtu.be/loLgtJomIms) |
| [Pont Network](https://colosseum.com/projects/explore/pont-network) | HM - DePin | - | 4 | "Pont Network offers a revolutionary blockchain-based solution to transform record-keeping in the maritime industry." | nije navedeno u opisu | ne | [2024-11-27](https://github.com/Ceres-Blockchain-Solutions/pont-network) | [link](https://docsend.com/view/2cs3qgzvs3jgbrrb) |

**Breakout (apr 2025)** (n=9)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Decen Space](https://colosseum.com/projects/explore/decen-space) | 1st - DePin | 25.000 | 4 | "Decen Space makes satellite communication cheaper and easier." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/e9c08f8e1ce846e9af95727e352ac5c2?sid=d9c2c4fd-27db-43e3-bc19-0289cdd387b3) |
| [Crush](https://colosseum.com/projects/explore/crush) | 2nd - DePin | 20.000 | 1 | "Crush turns everyday receipts into liquid micro-assets; we’re the Hivemapper of consumer purchase data." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/7ef797b80b354f3aaf5b772e3fdaa455?sid=b8e5445e-83e1-4f48-9e5e-788dad73996d) |
| [Home Harvest](https://colosseum.com/projects/explore/home-harvest) | 3rd - DePin | 15.000 | 1 | "Home Harvest is a tech company, decentralising food production." | nije navedeno u opisu | ne | nema | [link](https://www.loom.com/share/c49b6cf54023422a94ddea83cd324545?sid=3993a39c-88dd-4748-b551-7ea6375de01e) |
| [SoulBoard](https://colosseum.com/projects/explore/soulboard) | 4th - DePin | 10.000 | 4 | "SoulBoard is a decentralized bridge between advertisers and real-world ad space owners, powered by DePIN and on-chain incentives." | nije navedeno u opisu | ne | [2026-01-13](https://github.com/Soulboard/Admojo-Solana) | [link](https://www.loom.com/share/5224cc0695e644d09a03cd787ae33eff?sid=905027d4-4d3a-4ab4-9362-dc9d23a6eacc) |
| [NovenGrid](https://colosseum.com/projects/explore/novengrid) | 5th - DePin | 5.000 | 3 | "The DePIN for renewable power generation and storage nodes." | nije navedeno u opisu | ne | [2025-05-16](https://github.com/NovenGrid/Colosseum) | [link](https://www.loom.com/share/975b902cef6147eca5f67e481da0012b) |
| [WayFi](https://colosseum.com/projects/explore/wayfi) | University Prize - DePin | 2.500 | 2 | "Decentralize Wifi Network on Solana" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=EN8P8vL5KNs) |
| [SOLYD](https://colosseum.com/projects/explore/solyd) | HM - DePin | 5.000 | 6 | "Physical products that pay you." | nije navedeno u opisu | ne | [2025-05-16](https://github.com/solydstore/minter_server_hackathon) | [link](https://youtu.be/ImV13PfqoDw) |
| [Green Energy Network (GEN)](https://colosseum.com/projects/explore/green-energy-network-(gen)) | HM - DePin | 5.000 | 2 | "GEN is a real-world energy DePIN infrastructure built on Solana." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/23c8202ed0084c57b32d278934af38cf?sid=e05c747f-51ed-4bc0-b883-4dbadc12332b) |
| [GeoSVM](https://colosseum.com/projects/explore/geosvm) | HM - DePin | 5.000 | 2 | "GeoSVM: A new paradigm for public blockchain networks and virtual machines -- making location and geospatial data verifiable and p..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1085040782/eb249b206a?share=copy) |

### Placanja


**Renaissance (mart 2024)** (n=21)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [URANI](https://colosseum.com/projects/explore/urani) | 1st - DeFi & Payments | 30.000 | 3 | "Solana's intent-based swap aggregator, bringing protection against toxic MEV at the application layer and ensuring secure trading ..." | nije navedeno u opisu | C1 (None) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/84014b7877ab42e6929c0f381cbb8cd1?sid=545d0aaa-57b6-424c-8b6e-8a3239d615d0) |
| [GLAM](https://colosseum.com/projects/explore/glam-1) | 2nd - DeFi & Payments | 20.000 | 4 | "GLAM is a decentralized on-chain asset management protocol on Solana that enables efficient management and operations of investmen..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/15b0e87e181c425682f89f620cfd707f?sid=49d8dbe9-f75e-44c3-9660-ae10926ced61) |
| [Nomad](https://colosseum.com/projects/explore/nomad) | 3rd - DeFi & Payments | 15.000 | 4 | "Nomad streamlines off ramping using existing TradFi rails." | nije navedeno u opisu | ne | [org](https://github.com/nomad-rails), repo nije proveren | [link](https://youtu.be/v4lzDaQ9UjU?si=oygWSRDICdHVd_cE) |
| [Ripe](https://colosseum.com/projects/explore/ripe-1) | 4th - DeFi & Payments | 10.000 | 2 | "Ripe enables everyday crypto payments in Southeast Asia." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/ypG_fLAMgxY) |
| [Exponent](https://colosseum.com/projects/explore/exponent) | 5th - DeFi & Payments | 5.000 | 3 | "Built by a team of three (ex Kamino, Solana, Raydium), Exponent is a derivatives protocol for trading the yield of DeFi products o..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://docsend.com/view/rgra8a9ed7pk2ej3) |
| [Asgard Finance](https://colosseum.com/projects/explore/asgard-finance) | HM - DeFi & Payments | - | 4 | "Command center for managing leverage on multiple solana based money markets." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://pitch.com/v/asgard---hackathon-arrmgq) |
| [Arcana Markets](https://colosseum.com/projects/explore/arcana-markets) | HM - DeFi & Payments | - | 3 | "A Solana DeFi Web Application backed by a token-vaults program, swap, and custom infrastructure." | nije navedeno u opisu | ne | [2024-06-29](https://github.com/arcana-markets/arcana-ui) | [link](https://www.loom.com/share/5106558c00204beabb3dab7702a83d7b?sid=92d5c0d6-a073-4e25-a988-751fa333e92c) |
| [Avici](https://colosseum.com/projects/explore/avici) | HM - DeFi & Payments | - | 2 | "A self-custodial, P2P, mobile first DEX for emerging markets" | nije navedeno u opisu | ne | nema | [link](https://www.loom.com/share/3d177a127c0649f59620ff1b74bb9e5a?sid=7bb09508-e772-439c-b5a7-abcb0d9f32b1) |
| [Facto](https://colosseum.com/projects/explore/facto) | HM - DeFi & Payments | - | 1 | "Facto is a decentralized credit platform built 100% onchain, directly connecting institutional borrowers and investors through cro..." | nije navedeno u opisu | ne | [2024-04-08](https://github.com/notuslabs/facto) | [link](https://www.loom.com/share/25f9f47a342549ae804689ef686aa4c2) |
| [StonksBot AI](https://colosseum.com/projects/explore/stonksbot-ai) | HM - DeFi & Payments | - | 1 | "AI-Powered Token Analytics and Trading Bot on Solana." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://docs.google.com/presentation/d/1EW4JqSKWdoEJyZ_SG6VP2ZIvuQoR49FDqaWe7ENNKPQ/edit?usp=sharing) |
| [Poe](https://colosseum.com/projects/explore/poe-1) | HM - DeFi & Payments | - | 1 | "Poe is a prediction poll that leverages the collective wisdom of its users to make predictions about future events." | nije navedeno u opisu | ne | [2024-10-08](https://github.com/ProofOfEstimate/poe-solana) | [link](https://www.canva.com/design/DAGBu4g7CwM/ov0soZCNN9v76GZd0QnjHQ/edit?utm_content=DAGBu4g7CwM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
| [RSRV](https://colosseum.com/projects/explore/rsrv) | HM - DeFi & Payments | - | 3 | "We're building the first step towards unsecured revolving debt for crypto." | nije navedeno u opisu | ne | [2024-04-09](https://github.com/myfridayio/rsrv) | [link](https://www.loom.com/share/587228517b874633aaa8e7fc54f5b313?sid=219c3f55-d1a1-47d8-ab99-656d221696e2) |
| [BullBot](https://colosseum.com/projects/explore/bullbot) | HM - DeFi & Payments | - | 5 | "BullBot uses cutting-edge AI models to monitor markets for you 24/7, be a caring companion to guide you through a complex and ofte..." | nije navedeno u opisu | ne | [org](https://github.com/BullBotAI), repo nije proveren | [link](https://www.youtube.com/watch?v=AUVLtIZQx0k) |
| [Carrot](https://colosseum.com/projects/explore/carrot) | HM - DeFi & Payments | - | 2 | "https://www.deficarrot.com/ Liquid Yield Tokens, a single token entry to an automated, optimized yield aggregator service, it cons..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://docsend.com/view/qetenjnyjbjm2xk2) |
| [Mocha](https://colosseum.com/projects/explore/mocha) | HM - DeFi & Payments | - | 2 | "Welcome to Mocha, a pioneering financial service crafted for the African continent." | nije navedeno u opisu | ne | [2024-06-30](https://github.com/christex-foundation/mocha) | [link](https://www.loom.com/share/61b7f28cb4c64a13bc06891ce7fd2821?sid=b9f4cb28-403a-4566-927a-59828426431d) |
| [Triad](https://colosseum.com/projects/explore/triad-1) | HM - DeFi & Payments | - | 3 | "Discover. Analyze. Invest! The easiest way to invest in the Solana ecosystem" | nije navedeno u opisu | ne | [org](https://github.com/triadxyz), repo nije proveren | [link](https://dannpl.notion.site/Triad-c24d4e1fc87c4918bd805a88bfdbd0cf) |
| [Credible Finance](https://colosseum.com/projects/explore/credible-finance) | HM - DeFi & Payments | - | 5 | "Credible facilitates lending and borrowing against tokenized RWAs." | "onboarded $1.7 million in RWAs" i "$100 million commitment" od developera iz Bahreina | C4 (Credible) | [org](https://github.com/crediblefinance), repo nije proveren | [link](https://www.loom.com/share/ec504334e9f74156b3baefece25a6c18?sid=12119fa1-9c9f-4411-9836-e30ffa725f17) |
| [BlindPay](https://colosseum.com/projects/explore/blindpay) | HM - DeFi & Payments | - | 1 | "We enable local and cross-border payments for web3 companies" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://blindpay.io/renaissance) |
| [HAKIFI - A Revolutionary Risk Management Protocol](https://colosseum.com/projects/explore/hakifi-a-revolutionary-risk-management-protocol) | HM - DeFi & Payments | - | 6 | "Hakifi is a decentralized hedging protocol leveraging blockchain technology to mitigate financial risks, particularly in the volat..." | nije navedeno u opisu | ne | [org](https://github.com/orgs/hakifi-project/repositories), repo nije proveren | [link](https://mega.nz/file/ZD1GhBbI#7wKpAOFVCaDqxca4HlTx0UDH5oZnsR7F2-SssFXLht8) |
| [Bestlend](https://colosseum.com/projects/explore/bestlend-1) | HM - DeFi & Payments | - | 1 | "Bestlend maximizes your lending and borrowing rates to save you time and money." | nije navedeno u opisu | ne | [2024-06-02](https://github.com/SC4RECOIN/bestlend) | [link](https://drive.google.com/file/d/1J5X_ZyNKs5EgjI5YEeOo8n2Qq87RSG0P/view?usp=sharing) |
| [RateX](https://colosseum.com/projects/explore/ratex) | HM - DeFi & Payments | - | 3 | "RateX is a margin yield trading and synthetic yield-bearing asset protocol." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/d8de5149f02f43c7b05983b283c73bf1?sid=61547bd4-0764-4aab-97eb-c80eb28236f8) |

**Radar (sept 2024)** (n=9)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [FxSwap](https://colosseum.com/projects/explore/fxswap) | 1st - Payments | 25.000 | 3 | "FxSwap is a DEX that allows for efficient swap between Forex." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/ff9789ff36864be2bee5f2cb4afaa225) |
| [Hylo](https://colosseum.com/projects/explore/hylo) | 2nd - Payments | 20.000 | 3 | "Hylo is building Better Internet Money with an autonomous, dual-token stablecoin system backed by Solana LSTs." | nije navedeno u opisu | C2 (Hylo) | 404 (privatan ili obrisan) | [link](https://vimeo.com/1017778466) |
| [Split Finance](https://colosseum.com/projects/explore/split-finance) | 3rd - Payments | 15.000 | 2 | "Split Finance enables Buy Now Pay Never payment solutions for customers, where they are able to finance their expenses through the..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.canva.com/design/DAGSPiVp6R0/ffTAP_LxNRS46sanNJoWrw/edit?utm_content=DAGSPiVp6R0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
| [RIBH FINANCE](https://colosseum.com/projects/explore/ribh-finance) | 4th - Payments | 10.000 | 2 | "Ribh is a better payment collection and Inventory re-stocking solution for SMEs in emerging markets." | nije navedeno u opisu | ne | [org](https://github.com/ribafinance), repo nije proveren | [link](https://www.loom.com/share/7a4cf7c2cf574c4eba5adff36d2dcb23?sid=83e38ce8-187e-43d1-a7e0-1a913c523573) |
| [Quartz](https://colosseum.com/projects/explore/quartz) | 5th - Payments | 5.000 | 2 | "Offramp without selling your assets" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/b26a871dbf1a4ff9af014f3e96fb5158?sid=ef66bbd1-6dc7-4e4a-92e3-c6edd28a28b9) |
| [Bando](https://colosseum.com/projects/explore/bando) | HM - Payments | - | 4 | "In our MVP we built a direct connection between the traditional Mexican fiat infrastructure and Solana." | nije navedeno u opisu | ne | [org](https://github.com/bandohq), repo nije proveren | [link](https://www.loom.com/share/36fe4bc5c4ef4a3a9bc9d347a3c9049f) |
| [Zerocut](https://colosseum.com/projects/explore/zerocut) | HM - Payments | - | 3 | "Zerocut is the business layer for DeFi, seamlessly integrating yield-generating capabilities into everyday business operations." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/fdf049e7f02f4ba18907eb32778c9d85?sid=51078e0f-f5b2-4dfc-ac8a-a58d63f2803f) |
| [POW Cards](https://colosseum.com/projects/explore/pow-cards) | HM - Payments | - | 1 | "POW Card is the first decentralized identity card inside of the Apple and Google Wallets." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://drive.google.com/file/d/1VSEQyPuedjK20SFHsVoA-YDG2-FpbZ-A/view?usp=sharing) |
| [LocalSolana](https://colosseum.com/projects/explore/localsolana) | HM - Payments | - | 3 | "LocalSolana is a decentralized P2P exchange where users can connect with each other and trade between fiat and crypto directly fro..." | nije navedeno u opisu | ne | [2025-02-03](https://github.com/openpeer/localsolana) | [link](https://www.loom.com/share/df2b17b627d4420a9087fd4caac48b2e) |

**Breakout (apr 2025)** (n=15)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [CargoBill](https://colosseum.com/projects/explore/cargobill) | 1st - Stablecoins | 25.000 | 3 | "CargoBill, is the stablecoin payments platform for supply chain." | nije navedeno u opisu | C3 (CargoBill) | 404 (privatan ili obrisan) | [link](https://vimeo.com/1085190844/7313f0d092?share=copy) |
| [Decal - Payments and Loyalty](https://colosseum.com/projects/explore/decal-payments-and-loyalty) | 2nd - Stablecoins | 20.000 | 2 | "Decal is a payments and digital loyalty platform, built on the Solana blockchain." | nije navedeno u opisu | C3 (Decal) | 404 (privatan ili obrisan) | [link](https://youtu.be/NdY9ZV5cVOM) |
| [LocalPay](https://colosseum.com/projects/explore/localpay) | 3rd - Stablecoins | 15.000 | 3 | "Enabling 160+ million of existing stablecoin holders to use their assets for day-to-day payments in the emerging markets." | nije navedeno u opisu | C3 (LocalPay) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/69e16541a69e4e2bb942904d1e98a158?sid=683e5328-d15a-474f-909d-3e7650a24f61) |
| [XELIO](https://colosseum.com/projects/explore/xelio) | 4th - Stablecoins | 10.000 | 3 | "Xelio is a global money transfer and payment platform that enables users to securely send and receive Stablecoins like USDC via SM..." | nije navedeno u opisu | C5 (Housd) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/608fec194598480d8cabc500638483db?sid=62322e5b-b3c1-4911-bf03-aec799b99327) |
| [Bagel](https://colosseum.com/projects/explore/bagel) | 5th - Stablecoins | 5.000 | 1 | "Bagel is a privacy-first, self-custodial “stealth-domain” wallet: every time someone sends funds to your yourname.bagel handle, th..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/8273d63fd5f64bc28a4eece69b970604?sid=3240be9c-050d-4d70-b856-915cd3464724) |
| [Paytos: Pay Tokens Over SMS](https://colosseum.com/projects/explore/paytos:-pay-tokens-over-sms) | University Prize - Stablecoins | 2.500 | 2 | "Paytos turns any phone into a stablecoin wallet." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/ca58c467c5ac4016988a41391a9189fa?sid=a073a158-1b85-481b-9c03-8287277894db) |
| [Pyra](https://colosseum.com/projects/explore/pyra) | HM - Stablecoins | 5.000 | 1 | "The US dollar has lost 24% of its value since 2020, while the S&P 500 has risen by over 64%." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/64bc1e1ed98f435d9ac4c62e771313af?sid=8507fd86-a05b-4b80-9a8e-c685cd414d29) |
| [NECTARFI](https://colosseum.com/projects/explore/nectarfi-1) | HM - Stablecoins | 5.000 | 4 | "We are nectarfi and we "convert stablecoin savings to colleteral"." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/SBRoEzu85G0) |
| [Remlo](https://colosseum.com/projects/explore/remlo) | HM - Stablecoins | 5.000 | 1 | "Remlo - The On-Chain Stablecoin Bank Remlo is a decentralized on-chain banking protocol built entirely on smart contracts." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/836bca9ba5d34005be3fa3fe42d265d4) |
| [BulkCredit](https://colosseum.com/projects/explore/bulkcredit) | HM - Stablecoins | 5.000 | 1 | "BulkCredit is built on Venta, a Solana-based POS system." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/39356a060e7b47f5b6c4689dce0a24e8?sid=f307e64a-0321-4136-ba96-ff8deb316db4) |
| [Umbra](https://colosseum.com/projects/explore/umbra) | HM - Stablecoins | 5.000 | 4 | "gMPC ☂️ We're building Umbra - A privacy layer for Solana, enabling encrypted, auditable on-chain transactions through Arcium’s Co..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/FYkeK4Ke_Hw) |
| [Adstream](https://colosseum.com/projects/explore/adstream) | HM - Stablecoins | 5.000 | 3 | "Adstream enables passive income streams through a tablet-based open ad network for ride sharing" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/HFpThZdiqE8) |
| [DOLLAR](https://colosseum.com/projects/explore/dollar) | HM - Stablecoins | 5.000 | 3 | "The fastest way to send, hold, and withdraw dollars, anywhere in the world." | nije navedeno u opisu | C4 (Credible) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/b277dea879614f10a734a12a3153274d?sid=dbdedcf6-e0bd-4be3-995d-22556f35a392) |
| [Gaian](https://colosseum.com/projects/explore/gaian-2) | HM - Stablecoins | 5.000 | 4 | "Gaian / Save Smart - Pay Easy We provide a gateway that lets crypto users scan any QR code to pay in stablecoins while merchants r..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/0c50a257906d40aca717712736b0f2d8) |
| [Amp Pay](https://colosseum.com/projects/explore/amp-pay) | HM - Stablecoins | 5.000 | 3 | "No SOL, No fees, No problem!" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/bh7hbrCahyM) |

**Cypherpunk (sept 2025)** (n=8)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [MCPay](https://colosseum.com/projects/explore/mcpay) | 1st - Stablecoins | 25.000 | 1 | "Charge for Model Context Protocol tools, data sources, and specialized agent capabilities using x402." | nije navedeno u opisu | C4 (Frames) | [2026-01-21](https://github.com/microchipgnu/MCPay) | [link](https://youtu.be/00LULE4sDJY) |
| [Credible Finance](https://colosseum.com/projects/explore/credible-finance-1) | 2nd - Stablecoins | 20.000 | 2 | "The first USD-INR remittance rail powered by stablecoins built for banks, fintechs, and businesses, offering a guaranteed minimum ..." | nije navedeno u opisu | C4 (Credible) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/c95da2598bc34332b9de6970ca99d410) |
| [Cloak / Solana Privacy Layer](https://colosseum.com/projects/explore/cloak-or-solana-privacy-layer) | 3rd - Stablecoins | 15.000 | 2 | "Privacy has become the last missing piece of the Solana ecosystem and Cloak is here to fill that gap." | nije navedeno u opisu | C4 (Cloak) | nema | [link](https://www.loom.com/share/d46a6ee19449467d815ab719e4ee6ccc) |
| [Mercantill](https://colosseum.com/projects/explore/mercantill) | 4th - Stablecoins | 10.000 | 1 | "Mercantill is enterprise banking infrastructure for AI agents." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://vimeo.com/1131934475) |
| [SP3ND](https://colosseum.com/projects/explore/sp3nd) | 5th - Stablecoins | 5.000 | 4 | "Buy anything with stablecoins 🛍️" | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/78d44d039e00476ca3ea9c11d0a3786c) |
| [CashmereLabs](https://colosseum.com/projects/explore/cashmerelabs-1) | HM - Stablecoins | - | 1 | "Middleware infrastructure for zero-slippage one-click native omnichain transfers." | nije navedeno u opisu | ne | [2025-09-05](https://github.com/cashmere-prod/contracts-prod) | [link](https://www.loom.com/share/ec99038dab044ce4bb1b9df9f49369fb?sid=33e94b3b-d991-46ea-b325-7e288448de36) |
| [Janus](https://colosseum.com/projects/explore/janus) | HM - Stablecoins | - | 3 | "Janus is a Solana-native tokenized credit protocol for global trade." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/OZ_yFmA4as4) |
| [Xeno Money](https://colosseum.com/projects/explore/xeno-money) | HM - Stablecoins | - | 3 | "Xeno is building the first truly parallel payment network to Visa and Mastercard." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://youtu.be/BqXgbia6TX4) |

### Glavne nagrade


**Renaissance (mart 2024)** (n=4)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [DeVolt](https://colosseum.com/projects/explore/devolt-1) | University Award | 10.000 | 5 | "DeVolt is a decentralized platform and protocol designed to facilitate the entry of new players into the electric fueling market." | nije navedeno u opisu | C4 (Cloak) | [org](https://github.com/devolthq), repo nije proveren | [link](https://youtu.be/GrCtolx6kp4) |
| [AquaSave](https://colosseum.com/projects/explore/aquasave) | Climate Award | 5.000 | 11 | "AquaSave is an innovative startup committed to addressing the global water crisis by creating an ecosystem that integrates a netwo..." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.youtube.com/watch?v=qo-Yb-1s34Y&t=3s) |
| [Ore](https://colosseum.com/projects/explore/ore) | Grand Prize | 50.000 | 1 | "Ore is a digital currency you can mine from anywhere, at home or on your phone." | nije navedeno u opisu | C1 (Ore) | [2026-09-14](https://github.com/hardhatchad/ore) | [link](https://www.loom.com/share/f41b35eed21944eab62acb6b545beafd) |
| [Zircon](https://colosseum.com/projects/explore/zircon) | Public Goods Award | 10.000 | 1 | "Challenges and guided courses for Solana developers." | nije navedeno u opisu | ne | [2024-12-30](https://github.com/joeymeere/zircon) | [link](https://docs.google.com/presentation/d/1SjV8B1LzSOK8TMl8R4_XTROZPABTAy1QwWCHZkAI_xc/edit?usp=sharing) |

**Radar (sept 2024)** (n=4)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Lexicon](https://colosseum.com/projects/explore/lexicon) | University Award | 10.000 | 2 | "Lexicon lets you use voice or text commands to interact with the blockchain." | nije navedeno u opisu | ne | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/1ec26e5e6bc24ebda16289906402f040?sid=947ac434-9163-4261-a865-cc828f7c68b7) |
| [Attest Protocol](https://colosseum.com/projects/explore/attest-protocol) | Public Goods Award | 10.000 | 1 | "We’re building https on the blockchain 🔐" | nije navedeno u opisu | ne | [2026-09-11](https://github.com/daccred/attest.so) | [link](https://vimeo.com/1017812238) |
| [ENDCOIN](https://colosseum.com/projects/explore/endcoin) | Climate Award | 5.000 | 3 | "WE ARE TAKING SOLANA MOBILE TO SPACE." | nije navedeno u opisu | ne | [2025-09-23](https://github.com/pulse-on-climate/endcoin-program) | [link](https://www.loom.com/share/5fbce35b02ff4ba985e9664b1a4b7ca5?sid=0b3459d0-23d2-4b21-9924-d39edc83521e) |
| [Reflect Protocol](https://colosseum.com/projects/explore/reflect-protocol) | Grand Prize | 50.000 | 1 | "Reflect Protocol: Fully On-Chain Decentralized Tokenized Hedging via Delta-Neutral Currencies Reflect Protocol is the first entire..." | nije navedeno u opisu | C2 (Reflect Money) | 404 (privatan ili obrisan) | [link](https://www.loom.com/share/f55a4b055b1643fbbbb7cf57358222db?sid=60c65004-56c5-4ca8-be45-76e8d9e66f0d) |

**Breakout (apr 2025)** (n=4)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [IDL Space](https://colosseum.com/projects/explore/idl-space) | Public Goods Award | 10.000 | 1 | "IDL Space is a Postman-like tool designed for Solana developers to seamlessly explore program interfaces, validate, test, and debu..." | nije navedeno u opisu | ne | [2025-11-07](https://github.com/williamwa/idlman) | [link](https://www.loom.com/share/64b14c5428c34bd2abb65315dd9154a6?sid=73256444-3f53-4a5b-b91a-c66a8d31b6f6) |
| [LootGO](https://colosseum.com/projects/explore/lootgo) | Mobile Award | 25.000 | 7 | "LootGO - The Real-World Crypto Treasure Hunt, aka." | nije navedeno u opisu | ne | [2025-05-17](https://github.com/loot-Go/lootgo.app) | [link](https://www.loom.com/share/57515e817f0943e5938606764546cb23) |
| [openSOL](https://colosseum.com/projects/explore/opensol) | University Award | 10.000 | 2 | "A no-code solution for builders to wireframe, design, or learn Solana development to build programs or dapps using simple blocks a..." | nije navedeno u opisu | ne | [2025-07-16](https://github.com/nathanliow/opensol) | [link](https://youtu.be/-1BOQbdPYVw) |
| [TAPEDRIVE](https://colosseum.com/projects/explore/tapedrive) | Grand Prize | 50.000 | 1 | "TAPEDRIVE makes it easy to read and write data on Solana." | nije navedeno u opisu | C3 (TAPEDRIVE) | [2026-09-10](https://github.com/tapedrive-io/tape) | [link](https://www.youtube.com/watch?v=FFamxXlo1uQ) |

**Cypherpunk (sept 2025)** (n=3)

| Projekat | Plasman | $ | Tim | Recenica iz prijave (doslovno) | Traction (tim navodi) | Akcelerator | GitHub danas | Pitch video |
|---|---|---|---|---|---|---|---|---|
| [Unruggable](https://colosseum.com/projects/explore/unruggable-3) | Grand Prize | 30.000 | 3 | "Existing hardware wallets are multi-chain, built for every chain, but optimised for none." | nije navedeno u opisu | C4 (Unruggable) | [2025-12-27](https://github.com/hogyzen12/unruggable-app) | [link](https://www.youtube.com/watch?v=cHmLIalGAcA) |
| [Samui Wallet](https://colosseum.com/projects/explore/samui-wallet) | Public Goods Award | 10.000 | 2 | "Samui is an open-source wallet and toolbox for Solana builders." | nije navedeno u opisu | ne | [2026-05-17](https://github.com/samui-build/samui-wallet) | [link](https://www.loom.com/share/89282739903b4cec854b5459b38eb8e0) |
| [Pythia](https://colosseum.com/projects/explore/pythia) | University Award | 10.000 | 6 | "We are building a prediction market for the ICM meta." | nije navedeno u opisu | ne | [2025-12-05](https://github.com/Eremeyen/pythia-opportunity-markets) | [link](https://vimeo.com/1132414526?share=copy&fl=sv&fe=ci) |

## Detalji: sta je bilo posle (projekti bliski nama i svi prvi plasmani iz relevantnih track-ova)

Sajt: HTTP status 2026-09-24. Rejz: samo gde postoji javni izvor.

| Projekat | Plasman | Akcelerator | Rejz / novac posle | Sajt danas | Napomena |
|---|---|---|---|---|---|
| Nomu | 5. Consumer, Cypherpunk; Top 25 Frontier | C5 | Colosseum ulaz u C5 (akcelerator daje $250K, https://colosseum.com/accelerator); iznos za Nomu nije objavljen | [nomu.dev](https://www.nomu.dev/) 200, preusmerava na nomu.store | Pivot sa "rewards pool" e-commerce na lanac snabdevanja za brendove. Portfolio: "$1M+ GMV since launch" (https://colosseum.com/companies/nomu, tim navodi). Na Cypherpunku tim iz Hrvatske, sad SAD. X @EatwithNomu suspendovan (provereno 2026-09-24), novi nalog @nomustores. Na Frontier je predat isti GitHub link kao na Cypherpunk. |
| Pencil Finance | 4. RWA, Cypherpunk | ne | Paket kredita od $1M finansirali Animoca Brands, Open Campus i NewCampus u julu 2025, ciklus zatvoren 2026 (https://decrypt.co/377494/pencil-finance-1-million-student-loan). To je kapital za kredite, ne equity rejz. | [pencilfinance.io](https://www.pencilfinance.io) 200 | Protokol radi na EDU Chain (Arbitrum Orbit), ne na Solani (isti izvor). Znaci: tim je u trenutku prijave vec imao $1M plasiranih kredita. |
| BORE.FI | 2. RWA, Cypherpunk; HM Frontier (BORE.OIL) | ne | nije nadjeno | borefi.com ne odgovara | Vratio se na Frontier sa tokenizacijom naftnih rojaltija, dobio samo HM. Repo BORE.OIL napravljen 2026-03-27, 10 dana pre pocetka Frontiera. |
| Autonom | 1. RWA, Cypherpunk | ne | Techstars Web3 2025 (https://www.autonom.cc/) | [autonom.cc](https://www.autonom.cc/) 200 | RWA oracle, ne tokenizacija. |
| Legasi | 3. RWA, Cypherpunk | ne | nije nadjeno | [legasi.io](https://www.legasi.io/en) 200 | Postojeca francuska firma za lombard kredite, osnovana 2023 (https://www.legasi.io/about). Dosli su sa firmom koja vec radi. |
| VitalFi | HM RWA, Cypherpunk | ne | nije nadjeno | [vitalfi.lat](https://vitalfi.lat/) 200 | Tokenizacija brazilskih medicinskih potrazivanja. |
| CREAM | HM RWA, Cypherpunk | ne | nije nadjeno | nije provereno | Solarni krovovi zajednice. |
| Home Harvest | 3. DePIN, Breakout | ne | nije nadjeno | nije nadjen | Vidi `competition.md`: repo "Shell for colosseum entry", posle tisina. |
| Decen Space | 1. DePIN, Breakout | ne | Crunchbase navodi pre-seed, iznos nije nadjen (https://www.crunchbase.com/organization/decen-space) | [decenspace.com](https://decenspace.com) 200 | Berlin. Mreza zemaljskih antena za satelite. |
| SvachSakthi / GreenKWh | 1. DePIN, Radar | C2 | nije potvrdjeno (jedan Substack pominje YC i Multicoin, bez primarnog izvora) | [svachsakthi.in](https://www.svachsakthi.in/) 200, [greenkwh.net](https://www.greenkwh.net/) 200 | Off-grid solarna zadruga, IoT senzori belezeni on-chain. |
| BlockMesh | 1. DePIN, Renaissance | C1 | $250K Colosseum (https://messari.io/project/blockmesh/fundraising) | blockmesh.xyz ne odgovara | Portfolio: "Acquired". PitchBook: preuzeo Perceptron Network 20.06.2025 (https://pitchbook.com/profiles/company/607164-22). |
| DeCharge | 2. DePIN, Renaissance | C1 | $2,5M seed, vodi Lemniscap, uz Colosseum, mart 2025 (https://knowstartup.com/news/decharge-raises-2-5-million-to-expand-its-blockchain-powered-ev-charging-network/); $150K kroz ReFi Hub za 19 punjaca (https://decrypt.co/340958/decharge-raises-150k-on-refi-hub-to-launch-the-worlds-first-depinfi-powered-ev-corridor) | nije provereno | Najjaci DePIN ishod u uzorku. Hardver + mreza + kapital za fizicku infrastrukturu. |
| CUDIS | HM DePIN, Renaissance | ne | $5M seed, vodi Draper Associates, sept 2024 (https://siliconangle.com/2024/09/18/cudis-raises-5m-blockchain-based-ai-powered-wearable-health-ring/) | nije provereno | Fizicki proizvod (prsten). Najveci rejz u uzorku dosao je od HM, ne od pobednika. |
| Kiko Network | 5. DePIN, Radar | ne | nije nadjeno | kiko.network ne odgovara | Poslednji commit 2024-10-07. |
| CrowdBrain | Grand Champion, Frontier | C5 | nije nadjeno | [crowdbrain.ai](https://crowdbrain.ai/) 200 | Kategorija DePIN. Gruzija, tim od 2. |
| CargoBill | 1. Stablecoins, Breakout | C3 | nije nadjeno osim akceleratora | [cargobill.co](https://www.cargobill.co) 200 | X @cargobilldotai postoji, 860 pratilaca (provereno 2026-09-24), datum poslednjeg posta nije proveren. |
| MCPay | 1. Stablecoins, Cypherpunk | C4 (Frames) | nije nadjeno | mcpay.tech preusmerava na frames.ag, 200 | Repo napravljen 2025-05-30, 4 meseca pre pocetka Cypherpunka. |
| Trepa | 1. Consumer, Breakout | C3 | $420K pre-seed, vodi Colosseum, uz Balaji Srinivasan (https://www.bitget.com/news/detail/12560604931145) | [trepa.io](https://trepa.io) 200 | Predikcija brojeva (GDP, zaposlenost). |
| Superfan | 2. Consumer, Cypherpunk | C4 | nije nadjeno | [superfan.one](https://www.superfan.one/) 200 | Pivot na "opinion markets" za muziku. Repo napravljen 2025-08-26, mesec pre pocetka hakatona. |
| Capitola | 1. Consumer, Cypherpunk | C4 | nije nadjeno | nije provereno | Portfolio: prvi proizvod je Vistadex (RFQ predikcioni marketi). |
| Pregame | 1. Consumer, Radar | C2 | nije nadjeno | nije provereno | P2P kladjenje. |
| Banger | 1. Consumer, Renaissance | C1 | nije nadjeno | nije nadjen | Marketplace za tweetove. Jedini "marketplace" sa 1. mestom; roba je digitalna. |
| Housd | Top 25 Frontier | C5 | nije nadjeno | [housd.finance](https://housd.finance/) 200 | Portfolio: "fully liquid 10% APY (real yield)". |
| ODL | Top 25 Frontier | C5 | nije nadjeno | [rwaodl.com](https://rwaodl.com) 200 | Likvidacija RWA ka TradFi kupcima. |
| Traded, JK Index, One Arena | Top 25 Frontier | C5 (sve tri) | nije nadjeno | 200 (sve tri) | Kolekcionarske karte (TCG): fizicki predmet, ocenjen i cuvan, trguje se on-chain. Najblizi "fizicka roba + trziste" pobednici posle Nomu. |
| ReFi Hub | HM Frontier | ne | nije nadjeno | [refihub.io](https://www.refihub.io/) 200 | Tim navodi "$491K deployed, 14% realized IRR". Isti ReFi Hub kroz koji je DeCharge skupio $150K. |
| Jurassic Finance | HM Frontier | ne | nije nadjeno | [jurassic.finance](https://jurassic.finance/) 200 | Srbija, fosili, pravna prava preko MetaDAO. Nalog iz nase liste ekosistema. |

## Sta iz ovoga sledi

Nalazi su gore. Ovo je tumacenje, sa velicinom uzorka uz svaku tvrdnju.

### 1. Sta razlikuje top 10 track-a ili top 21 ukupno od ostalih

- **Mesto na vrhu, ne nagrada uopste.** 1. i 2. mesto ulaze u akcelerator
  u 29 od 52 slucaja, HM u 10 od 141 (Copilot, n=293). Na Frontieru, gde je
  "top 25" isto sto i nova "top 21" kategorija, 19 od 26 je uslo u C5, HM
  0 od 16. Za World's Fair to znaci: cilj je opsti fond (Grand + 20). Koliko
  Colosseum bira iz ekosistemskih track nagrada (Solana, $10K, 10 mesta),
  nema podatka; to je nov format.
- **Novac koji se krece kroz proizvod.** Consumer 1-3. mesto 2024-2025: 10
  od 12 imaju trgovanje, kladjenje, predikciju ili ulaganje (izuzeci:
  WootzApp, Chomp). Frontier Consumer pobednici: 8 od 8. Placanja i RWA to
  imaju po definiciji.
- **Mali timovi.** Medijana tima je 2 u svih 149 relevantnih pobednika.
  Velicina tima ne pravi razliku.
- **Isti ljudi se vracaju i pobedjuju.** Unruggable: 4 prijave, od HM do
  Grand Prize i C4. Credible: HM, pa HM, pa 2. mesto i C4. Nomu: 5. mesto,
  pa Frontier i C5. BORE.FI: 2. mesto, pa HM. Treca prijava nije minus.
- **Traction sam nije dovoljan** (vidi 3), ali kod Frontier pobednika sa
  prihodom (Clawpump, DashX, Nomu, n=3) sva tri su u C5.

### 2. Koji jezik (RWA, Consumer, DePIN) zuri nagradjuje kod proizvoda kao nas

"Kao nas" ovde znaci: fizicka roba, proizvodjaci, stvarna imovina.

- **RWA jezik: nagradjuje se finansijski instrument, ne fizicka stvar.**
  Svih 8 RWA projekata na vrhu (Cypherpunk 1-5, Frontier ODL, Housd, Crafts)
  su finansijski instrumenti ili finansijska infrastruktura (prinos, krediti,
  likvidnost, oracle za cene). Sva 4 projekta vezana za fizicku
  proizvodnju (CREAM krovovi, BORE.OIL nafta, ReFi Hub solar, Jurassic
  fosili) dobila su HM, i to cak i ReFi Hub sa $491K ulozenog kapitala.
  Uzorak je mali (n=12). Cypherpunk RWA: 0 od 7 u akceleratoru.
- **DePIN jezik: nagradjuje se mreza fizickih cvorova, ali sve rede ulazi
  u akcelerator.** DePIN je imao najvisu stopu nagrade (4,3-9,4% prijava) i
  tri 1. mesta plus Frontier Grand Champion. Ishodi su najjaci u uzorku:
  DeCharge $2,5M seed, CUDIS $5M seed, BlockMesh preuzet. Ali akcelerator:
  C1 cetiri DePIN firme, C2 jedna, C3 nula, C4 nula, C5 jedna (CrowdBrain).
  Nasa DePIN prijava na Frontieru nije nagradjena (n=1, ne izvoditi pravilo).
- **Consumer jezik: nagradjuje se trgovanje, a fizicka roba prolazi samo
  uz brojku prodaje.** Marketplace fizicke robe nikad nije bio iznad 5.
  mesta (Nomu 5., store.fun HM, WearTre HM, n=3). Ali Nomu je jedini tim iz
  "fizicke trgovine" koji je stigao do akceleratora, i to posle drugog
  pokusaja, sa "$1M+ GMV". Na Frontieru su tri TCG projekta (fizicke karte,
  ocenjene, trguju se on-chain) sva usla u C5 (n=3).

### 3. Rad uradjen tokom hakatona

- **Raniji rad ne diskvalifikuje.** MCPay (1. Stablecoins, C4) ima repo
  napravljen 4 meseca pre hakatona; Superfan (2. Consumer, C4) mesec dana
  pre; Ralli (HM, C1) tri meseca pre. Nomu je na Frontier predao isti GitHub
  link kao na Cypherpunk i pobedio. Frontier pobednici Clawpump i DashX su
  vec imali proizvod u radu sa prometom.
- **Ali ono sto je pokazano je novo.** Nomu je na Frontieru pokazao novi
  proizvod (lanac snabdevanja), ne isti marketplace. BORE.FI je napravio novi
  repo za BORE.OIL 10 dana pre Frontiera. Repo-i Pencil, BORE.FI i VitalFi
  na Cypherpunku napravljeni su pri kraju hakatona (predaja koda, ne istorija
  rada).
- **Javni update-i na Colosseum-u nisu razlika.** Breakout i Cypherpunk:
  51 od 150 pobednika ima bar jedan update; od onih koji su posle usli u
  akcelerator, 7 od 27. Update ne skodi, ali ga pobednici uglavnom nemaju.
- Colosseum sam kaze (radionica, 08.05.2025,
  https://blog.colosseum.com/perfecting-your-hackathon-submission):
  "Projects that stand out typically demonstrate early traction,
  conversations with potential users." i "The accelerator emphasizes founder
  potential and adaptability over the hackathon submission itself."

### 4. Traction pri prijavi (raspon)

- Donja granica: nula. Home Harvest 3. mesto DePIN sa praznim repoom.
  Od 149 relevantnih pobednika u Copilotu, samo 3 u opisu navode brojku
  (Fanplay: 10K novcanika; Unkomon: 13K waitlist; Credible: $1,7M RWA).
- Gornja granica: stotine hiljada do milion dolara. Pencil: paket kredita od $1M
  finansiran u julu 2025, pre Cypherpunka (Decrypt). Frontier: Clawpump ~$650K prihoda,
  DashX $400K+ mesecno, Nomu $1M prodaje (sve "tim navodi").
- Trend: na Frontieru 5 od 44 pobednika i HM navodi brojku prometa, u
  2024-2025 3 od 149. Zuri vise ne vidi samo prototipove.

### 5. Akcelerator: koliko i po cemu se razlikuju

- Copilot: 54 od 293 nagradjenih (18%). Relevantni track-ovi: Placanja 11/53,
  Consumer 11/46, DePIN 4/28, RWA 0/7, glavne nagrade 5/15. Frontier: 20 od
  44 nagradjena (19 top + Public Goods).
- Po cemu se razlikuju: (a) plasman 1-2; (b) finansijska mehanika
  (predikcija, placanja, prinos); (c) spremnost na pivot: Superfan, MCPay
  (Frames), Nomu, Capitola (Vistadex) su u portfoliju sa drugim proizvodom
  od onog sa hakatona; (d) ponovljene prijave istog tima.
- Oni koji nisu usli, a imali su ishod: CUDIS ($5M), Pencil ($1M kapitala
  za kredite, Animoca). Akcelerator nije jedini put do novca.

### Preporuka (odvojeno od nalaza). Nemanja odlucuje.

**Consumer jezik kao glavni, RWA i DePIN kao dokaz ispod njega.** Tri razloga
iz podataka:
1. Jedini tim iz trgovine fizickom robom koji je stigao do akceleratora
   (Nomu) uspeo je sa consumer pricom i brojkom prodaje, i to u drugom
   pokusaju. Nasa situacija je najslicnija njihovoj.
2. RWA jezik za fizicku imovinu je u 4 od 4 slucaja stao na HM; na vrhu RWA
   su samo finansijski instrumenti. Ako pricamo RWA, mora da bude prinos, a
   to je pitch za $NECTAR, ne za marketplace.
3. DePIN je pobedjivao, ali akcelerator ga poslednje tri kohorte skoro ne
   uzima (1 od 42), a nasa DePIN prijava na Frontieru nije prosla.

Da bi consumer jezik radio, iz podataka slede dva uslova: (a) kroz proizvod
mora da se krece novac, sa brojkom (Nomu "GMV", DashX "$/mesec"); (b) mora
da postoji mehanika koju kupac ima osim kupovine (kod Nomu: udeo u uspehu
proizvoda; kod TCG pobednika: trgovanje). Senzori i kosnice su dokaz porekla
(DePIN), a proizvodnja je dokaz da imovina postoji (RWA); oba idu u deck kao
"zasto nama veruju", ne kao naslov.

Suprotan argument, posteno: DePIN ima najvecu stopu nagrade po prijavi i
najjace ishode posle (DeCharge, CUDIS). Ako Nemanja smatra da je mreza
pcelara sa senzorima jaca prica od marketplace-a, podaci to ne iskljucuju.

## Sta nije provereno ili nije nadjeno

- **X nalozi**: poslednji post nije proveren ni za jedan projekat. Projekat
  koristi RapidAPI plan sa 500 zahteva mesecno koji treba serverskom pracenju
  (ostalo oko 490), pa sam potrosio samo 4 zahteva (Nomu suspendovan, CargoBill
  postoji). Za ostale: nije provereno.
- **Sajtovi**: Copilot ne cuva sajt za hakatone pre Frontiera. Sajt je
  proveren samo gde je adresa nadjena u izvoru (GitHub, stranica projekta,
  pretraga). Domeni nisu pogadjani.
- **Rejz**: proveren samo za ~20 projekata iz tabele "Detalji". Za ostale
  nije proveren, sto ne znaci da ga nema.
- **Frontier iznosi** po projektu nisu upisani na stranicama projekata.
- **Ceo formular prijave** (pitanja o traction-u, GTM) nije dostupan; Copilot
  ima samo opis. Traction u tabelama je donja granica onoga sto su timovi
  rekli zuriju.
- **Frontier repo-i**: 15 od 15 proverenih kroz GitHub API danas vraca "Not
  Found" (privatni ili obrisani), pa za Frontier ne mozemo videti kad je kod
  pisan.
- **Hyperdrive 2023**: Copilot ga nema, nije obradjen.
- Veza Xelio (4. Stablecoins, Breakout) sa firmom u portfoliju: Copilot kaze
  Housd (C5), ali repo Stablecorp prijave je `usexelio/bizOS`. Nejasno.
- GreenKWh: tvrdnja o YC i Multicoin ulaganju je iz Substack teksta bez
  primarnog izvora, nije potvrdjena.

## Pitanja za Nemanju

1. Da li kroz marketplace do 12.10 moze da prodje prva stvarna prodaja
   (bilo koja brojka), posto je brojka prometa ono sto razlikuje Nomu na
   Frontieru od Nomu na Cypherpunku?
