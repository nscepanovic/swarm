# Apiary: game design

**Version:** v0.3 · 2026-09-19 (English translation of `design.md`)
**For:** the game developer (engine and art style already exist) and Nemanja
**Status:** third draft. Open questions are at the end.

Items marked `[to verify]` are beekeeping facts that Nemanja (a beekeeper)
confirms before they go into the game.

---

## 0. Decisions

- **Audience: kids and adults.** One game, two levels (see principle 6).
- **Game language: English.**
- **Bee venom (apitoxin) and apitherapy are in the game**, through the
  Venom Healer hero (section 12).
- **Several hive types, each with its own benefits** (section 7). The
  developer picks the final list.
- **Several heroes** for players with different skills and preferences
  (section 12).
- **A game is a game.** Gamified and imaginative, but educational (section 3).

## 1. In one sentence

The player becomes a beekeeper: sets up an apiary, looks after colonies
through the seasons, makes and sells honey and other products in town, and
along the way learns how bees live, why they matter, and what threatens them.

## 2. Principles

1. **Knowledge unlocks progress, not only money.** Better equipment, new
   products and new places open when the player finishes a lesson and shows
   they understand it. Money alone is not enough.
2. **Learn by doing.** Not by reading text, but by making a decision: open
   the hive, look at the frame, decide what the problem is. The right
   decision gives a good result.
3. **Consequences are real and delayed.** Like real beekeeping: a mistake
   in August (varroa) shows up in February (dead colony). The game then
   explains the link.
4. **Failure is a lesson, not the end.** A colony can die. The player gets
   an explanation why, and carries on.
5. **Bees are not alone.** Pesticides, pollution, drought and disease are
   part of the world. The player does not fix everything alone: they
   convince people and work with other beekeepers.
6. **One game, two levels.** Same world and rules, but the player chooses
   how much the game helps:
   - *Guided* (kids and beginners): the mentor points out what to look at,
     fewer things are simulated (no diseases at first), mistakes are
     explained right away.
   - *Real Beekeeper* (adults): full simulation, delayed consequences, the
     mentor helps only when called.
   The level can be changed later.
7. **Imaginative in form, true in substance.** The world is a fairy tale,
   bees talk, pollution is a grey mist that eats colors. But everything the
   game teaches about bees is true, and **magic never solves a real
   problem**: there is no potion that cures varroa. Varroa is handled like
   in real life, the game just makes it fun.

## 3. The game: fun and magic

Everything else in this document is *what* the game teaches. This section
is *why people play*. Every system after this one also has a "Why it's fun"
line.

### A world that blooms

The region is called **Bloomvale** `[working title]`. At the start the world
is pale, half the map is grey. **More bees and flowers, more color.** Around
every healthy apiary the map comes alive: flowers grow, trees get fruit,
birds arrive. The player literally sees bees pollinating the world.
*What they learn:* no pollination, no fruit; a large part of our food
depends on pollinators `[to verify wording and number before it goes in]`.

The opposite: **Grey Mist** comes from the factory and from fields sprayed
while in bloom. Where it falls, color disappears and bees get weak. The mist
is not beaten with a sword, but with what works in real life: convince the
farmer, collect evidence, plant bee-friendly plants. Every solution brings
back some color.

### Bee companion

Every player has a **bee companion** that flies after them and talks. It is
the mentor's voice: gives tips, comments, jokes. The player names it. It
grows with the player (new look as they level up). In *Guided* it talks more,
in *Real Beekeeper* only when called.
*What they learn:* the bee talks about itself in first person ("In summer I
only live a few weeks, so I work fast!" `[to verify]`). Kids remember
stories, not tables.

### Beedex

A card collection. Every new thing the player discovers becomes a card:
flower, honey type, hive type, disease, pest, bee job (cleaner, nurse,
guard, forager...). Every card has one true, interesting fact and a rarity
(common, rare, legendary). Collect a full set, get a reward.
*What they learn:* this is an encyclopedia the player builds themselves.

### Mini games

The main actions are short mini games, the same idea as the math tasks in
the existing game:

| Mini game | How it plays | What they learn |
|---|---|---|
| **Queen Hunt** | find the queen on a frame among hundreds of bees, against the clock | what queen, drone and worker look like |
| **Frame Reader** | look at a frame and say what you see: eggs, brood, honey, pollen, queen cells | reading a frame, hive inspection |
| **Mite Spotter** | find varroa mites on bees and in brood | varroa, how infestation is measured |
| **Swarm Chase** | a swarm flew out! follow it on the map and catch it before it leaves | why bees swarm, how a swarm is caught |
| **Honey Harvest** | rhythm game: uncapping, extracting, straining | harvest steps, honey ripeness |
| **Waggle Dance** | read the bee's dance: direction and distance to flowers | the waggle dance, how bees communicate |
| **Hive Defense** | wasps and hornets attack at the end of summer; narrow the entrance, set traps | robbing, protecting a weak colony |
| **Blind Tasting** | guess the honey type by color, taste, crystallization | honey types, quality |

### Reward loop

- **XP and levels** for every action, with a clear "ding!" moment.
- **Daily quests** on the town Bounty Board: "Catch a swarm", "Deliver 3
  jars of linden honey", "Teach the farmer to spray in the evening".
- **Achievements and badges:** "First honey", "Wintered all colonies",
  "Saved 10 fields from the mist".
- **Hive painting and decorations:** hives in colors and patterns,
  decorations for the apiary. The player expresses themselves.
  *What they learn:* beekeepers paint hives in different colors so bees find
  their own home more easily `[to verify]`.
- **Rare events:** golden swarm, a rare flower that blooms once a year,
  legendary queen.

### Big events (whole server)

- **Winter as a survival challenge.** Before winter players prepare their
  colonies. In spring it is counted who kept them all. Rewards and glory.
- **Hornet invasion** (boss event): players defend apiaries together.
- **The Grey Factory** (server boss): players together collect evidence,
  convince the town and plant flowers until the factory changes. When it
  falls, a whole part of the map gets its color back.
- **Honey Fair and Flower Festival:** seasonal events with competitions.

## 4. World and map

Same isometric style as the existing game. One region to start, with:

| Place | What is there | Why it exists |
|---|---|---|
| Player's land | empty plot where they build the apiary | start of the game |
| Black locust (acacia) forest | blooms in May | main spring nectar flow |
| Linden trees (avenue, forest) | bloom in June | summer flow |
| Sunflower fields | bloom in July | big summer flow; most spraying happens here (see 10) |
| Rapeseed fields | bloom in April | early flow, also sprayed |
| Meadows, orchards | early spring | colony build-up after winter |
| River, stream | water | bees need water; an apiary near water is better |
| Factory | pollutes air and water around it | a problem the player solves |
| Town (one or more) | market, co-op, lab, beekeepers' association, vet | selling, orders, learning |

**Flight radius.** Bees forage mostly within about 3 km of the hive
`[to verify for the game: use 3 km as the rule, show it as a circle on the
map]`. When choosing an apiary spot the player sees the circle and what
blooms inside it. First lesson: **the place decides the honey.**

**More flows, more honey types.** Each flow gives its own honey, with its
own color, taste and price: acacia, linden, meadow, sunflower (and
rapeseed). A player who knows what blooms where and when can have several
honey types in one year. This is the main reason to learn the bloom
calendar.

**Migratory beekeeping (advanced).** Later in the game the player moves
hives from one flow to the next as they bloom: acacia, then linden, then
sunflower. Real beekeepers do this to get more honey types. It is done with
an **apiary container** that is moved as a whole. This is the advanced part
of the game: it needs knowledge, experience and reputation, and unlocks only
after the player masters beekeeping in one place.

## 5. Calendar and time

The game goes through the seasons. Each season has its own work:

| Period | What happens in nature | Beekeeper's work |
|---|---|---|
| Winter (Dec-Feb) | colony in a winter cluster, no flying | don't open hives; listen, weigh; repair equipment, build frames, learn |
| Early spring (Mar) | first cleansing flight, first pollen | first inspection on a warm day, check queen and food |
| Spring (Apr-May) | fast build-up, fruit trees, rapeseed, acacia | add space, prevent swarming, first harvest |
| Summer (Jun-Jul) | linden, sunflower | harvest, migration, watch out for spraying |
| Late summer (Aug) | flow ends | varroa treatment after the last harvest |
| Autumn (Sep-Nov) | getting ready for winter | feeding, queen check, narrow the entrance, protect from mice and wasps |

How long a game year lasts is an open question (see the end). Proposal: one
season plays in a few hours, so the player sees the effect of one season's
decisions in the next.

## 6. The colony (heart of the game)

Every hive is a colony with a state the player does not see directly. They
see it only when they open the hive and look at the frames. This is on
purpose: **inspection is a skill.**

**State stored per hive:**
- number of bees (a strong summer colony is tens of thousands, much less in winter)
- queen: present / missing, age, laying quality
- brood: eggs, larvae, capped brood, pattern (solid or spotty)
- food: honey and pollen in frames
- varroa: infestation level
- disease: none / one of the diseases from section 10
- swarming pressure: grows when crowded and with lots of food
- temper: calm or aggressive bees
- space: number of boxes and frames

**Hive inspection (main interaction):**
The player opens the hive and pulls out frames one by one. Each frame shows
what is on it. The task is to recognize what they see, and that is the
learning, same as the math tasks in the existing game:

| Task | What the player learns |
|---|---|
| Find the queen among the bees | what queen, drone and worker look like |
| Are there eggs? | eggs mean the queen was there a few days ago, even without seeing her |
| Solid or spotty brood? | spotty brood means a problem (queen, disease) |
| Queen cells at the bottom of the frame or in the middle? | swarm cells or queen replacement: different decisions |
| Varroa test (powdered sugar or alcohol wash) | how infestation is measured, and when to treat |
| How many frames are covered? | when to add space, and when not |

**Bee development** (goes into a lesson and is used in the simulation):
queen 16 days, worker 21 days, drone 24 days from egg to emergence
`[to verify: Nemanja confirms numbers before they go in]`.

**Inspection rule:** the hive is not opened in rain, cold weather or winter.
If the player does it, the colony suffers. That is how they learn when work
is allowed.

## 7. Apiary and equipment

**Placing the apiary.** The player picks a spot on their land and gets a
site score: sun, shelter from wind, water nearby, what blooms in range,
distance from roads and houses. Hive entrances do not face a path where
people walk.

**Hive types.** There are several and each brings something different, like
gear in an RPG: the player picks a hive for how they like to play. The
developer decides the final list and look. The benefits below are real
differences between these hives, turned into bonuses:

| Hive | In-game bonus | In-game drawback | Real difference |
|---|---|---|---|
| **Langstroth-Root (LR)** | boxes are easy to add and swap, best for migration and trading parts | more lifting during inspection | modular, most widespread, standard parts |
| **Dadant-Blatt** | stronger and calmer colonies, better wintering | heavy, slower to move | large brood chamber |
| **AZ (Alberti-Žnideršič)** | inspect without lifting boxes, ideal for a container or bee house | slower inspection, not for open field | worked from the back, like a cabinet `[to verify]` |
| **Top-bar** | cheap, natural comb, easy for kids and beginners | less honey | comb without wired frames |
| **Observation hive (glass)** | colony visible live; bonus for Beedex and school visits | no honey | for education and exhibitions |
| **Skep (legendary)** | collector's item in the town museum | cannot be inspected | old frameless hive; the beekeeper could not inspect the colony `[to verify]` |

*Why it's fun:* the choice has consequences, like choosing a weapon. The
Wandering Keeper needs LR or AZ, the Queen Whisperer Dadant-Blatt, a kid a
top-bar.
*What they learn:* why different hives exist and what a frame is.

**Equipment and what unlocks it:**

| Equipment | What it does | Unlocked by |
|---|---|---|
| Bee suit and gloves | fewer stings during inspection | from the start (basic), better after a lesson |
| Smoker | calmer bees during inspection | lesson "How to approach a hive" |
| Hive tool | pulling frames | from the start |
| Queen excluder | clean honey without brood in the honey box | queen lesson |
| Feeder | feeding in spring and autumn | lesson "Winter" |
| Extractor (manual, then electric) | getting honey out | first harvest |
| Wax melter | wax from old frames and cappings | wax lesson |
| Pollen and propolis traps | new products | lessons on those products |
| Apiary container | migratory beekeeping | advanced: knowledge + experience + reputation, migration lesson |

## 8. Products

| Product | How it is made in the game | What affects quality |
|---|---|---|
| Honey (acacia, linden, sunflower, meadow) | harvest after a flow | flow type, ripeness (capped honey), cleanliness, residues |
| Wax | melting cappings and old frames | cleanliness, whether treatments were used |
| Propolis | scraping or a trap | later in the game |
| Pollen | pollen trap at the entrance | don't overdo it, the colony needs it |
| Swarms and queens | sold to other players | advanced |
| Royal jelly | advanced, needs special training | later |
| Bee venom (apitoxin) | special device at the hive entrance, bees leave venom and don't die `[to verify description]` | Venom Healer only, see section 12 |

**Honey ripeness.** Unripe (uncapped) honey has too much water and can
ferment. A player who harvests too early gets worse honey, and the town lab
shows them why. The legal limit for water in honey is 20% `[to verify]`.

**Crystallization.** Acacia honey stays liquid for a long time, rapeseed
honey crystallizes fast. A customer asking "why did my honey turn solid" is
a chance to educate the customer, not a player mistake.

**Pollination service** (later in the game). An orchard or plantation calls
the beekeeper to bring hives while the trees bloom, and pays for it. The
first such job is **almond pollination**, then other fruit. Almonds bloom
very early, so the colony must already be strong at the end of winter: a
player who prepared well for winter can take the job, others can't. It
teaches that pollination is worth more than honey: without bees, no fruit.
`[to verify: when almonds bloom in our region]`

## 9. Town, trade and orders

- **Market:** the player sells what they have. Price depends on type and quality.
- **Orders:** an NPC asks for "5 jars of acacia by the end of spring" or
  "wax for candles". A finished order gives money and reputation.
- **Lab:** honey analysis (water, residues, origin). Certified honey is worth
  more. This is where the player learns the factory or spraying is ruining
  their honey.
- **Beekeepers' association:** lessons, competitions, other players.
- **Vet:** disease diagnosis, mandatory reporting of some diseases.

## 10. Problems and dangers

### For bees

In the game these problems come as **events** with a clear sign on the map
(icon above the hive, the bee companion gets worried), not as a hidden number.

| Problem | How it appears | What the player does | What they learn |
|---|---|---|---|
| Varroa | always present, grows through summer | measures, treats at the right time | the biggest colony killer; treat after the last harvest, not before |
| American foulbrood | rare, from bought frames or robbing | recognizes it, calls the vet, burns | must be reported; spores last for years `[to verify]` |
| Nosema, chalkbrood | weak colony, bad weather | strengthens colony, replaces queen | a weak colony is a sick colony |
| Swarming | crowded, lots of food, spring | adds space, makes an artificial swarm | a swarm takes half the bees and most of that year's honey |
| Robbing and wasps | late summer | narrows entrance, doesn't spill honey | a strong colony defends itself, a weak one can't |
| Mice in winter | autumn | puts a mouse guard on the entrance | small things before winter save the colony |
| Drought | summer | water, migration | no water and no flowers, no honey |
| **Pesticide spraying** | farmer sprays in bloom, during the day | finds dead bees in front of the hive, goes to talk to him | see quest line below |
| **Factory** | pollutes the area around it | lab shows residues, apiary gets weaker | see quest line below |

**Quest line "The neighbor is spraying".** The main place for this is the
**sunflower fields**, because that is where most spraying happens and
sunflower is also a big flow. The people who grow crops are an audience to
educate, not enemies. The farmer NPC sprays at noon while the crop is in
bloom. The player finds dead bees in the morning, goes to him and talks.
The options are not "defeat him" but convince him with facts:
- spray in the evening, when bees don't fly
- don't spray while the plant is in bloom
- tell beekeepers a day ahead so they can close the hives
- switch to organic protection (longer quest line)
- understand that he needs bees too: sunflower pollinated by bees gives more
  seed `[to verify wording]`
The wrong approach (shouting, threats) closes cooperation for a while. The
right approach changes the NPC's behavior for the whole map, which helps
other players too.

**Quest line "The factory".** The player notices weaker colonies and worse
honey analysis around the factory. They can move the apiary (short-term
fix), or collect evidence (analyses from many beekeepers), team up with
other players and push for change (long-term fix, a shared server goal).
They learn that bees are a **bioindicator**: what shows up in honey is also
in the environment.

### For people (dangers from bees)

| Situation | What the player learns |
|---|---|
| Inspection without a suit or smoke | stings hurt, bees defend themselves when disturbed |
| Working in rain, with strong smells, fast movements | when and how to approach a hive |
| A visitor is stung, face swells, hard to breathe | this is an allergic reaction and an emergency: call an ambulance, don't wait |
| The player is stung: how to remove the stinger | scrape it out, don't squeeze `[to verify]` |
| A child walks up to the hives | how to explain to kids that bees are not scary if we leave them alone |

This comes through NPC situations, not warning text.

## 11. Progress: knowledge, experience, reputation

Three separate things:
- **Knowledge** = finished lessons. Lessons come from NPCs (old beekeeper,
  vet, association). A lesson is finished by a task in the game, not a
  paper quiz. Example: "Swarming" is finished when the player recognizes
  swarm cells and makes an artificial swarm.
- **Experience** = seasons the colonies survived, successful inspections.
- **Reputation** in town = finished orders, honey quality, helping others.

Unlocks need a combination. The electric extractor needs money and
experience. Migration needs knowledge and reputation.

**Starting knowledge tree:**
1. Bee life (queen, worker, drone) → unlocks frame inspection
2. How to approach a hive → smoker, better suit
3. Flows and blooming → flow map, choosing a site
4. Swarming → artificial swarm, second hive
5. Varroa → test and treatment
6. Harvest and honey ripeness → extractor, selling
7. Winter → feeder, preparation
8. Pesticides and pollution → quests with the farmer and the factory
9. Dangers and first aid → quests with visitors
10. Wax, propolis, pollen → new products
11. Migration and container (advanced) → migratory beekeeping, pollination service
12. Apitherapy (Venom Healer hero) → bee venom, working with patients

## 12. Heroes

All players have an apiary and learn the basics. A hero is a
**specialization**: what the player likes doing most. It gives its own
quests, its own equipment and its own way to earn, and teaches one part of
beekeeping deeper. The existing game already has classes (e.g. "Monk"), so
this is the same system.

Each hero has its own skill tree, its own look and its own special mini game.

Heroes depend on each other. This is the main reason for multiplayer: nobody
can do everything alone.

| Hero | For a player who likes | Special work | What they learn deeper | Needs from others |
|---|---|---|---|---|
| **Queen Whisperer** (queen breeder) | details, biology | raises queens, selects calm and healthy lines, sells queens | queen development, what a good colony is | Hive Alchemist for health |
| **Honey Merchant** (trader) | trade, people | orders from several towns, packaging, labels, better prices | honey types, quality, crystallization, how to spot fake honey | honey from other players |
| **Hive Alchemist** (researcher, lab) | analysis, puzzles | microscope, lab, disease diagnosis, varroa counts | diseases, varroa, why colonies die | samples from other beekeepers |
| **Meadow Warden** (nature protector) | stories, convincing people | quests with farmers and the factory, plants bee-friendly plants | pesticides, bioindicators, why bees matter for food | evidence (analyses) from the Hive Alchemist |
| **Hivesmith** (builder) | making things | builds hives, frames, equipment, later containers, sells to others | hive parts, why measurements matter (bee space) `[to verify]` | wax and orders |
| **Venom Healer** (apitherapist) | health, people | bee venom, propolis, working with patients in town | what apitherapy is, safety, allergy | products from other beekeepers |
| **Wandering Keeper** (migratory, advanced) | travel, big jobs | migratory beekeeping, pollination service (almonds) | bloom calendar, pollination | container from the Hivesmith |

**Venom Healer, content rules.** Apitherapy is part of the game, but the
game teaches, it does not promise:
- The player first finishes lesson 12 and the first aid lesson (9).
- Every patient first gets an allergy test. Skipping it is a mistake the
  game punishes (allergic reaction, ambulance).
- Patient NPCs tell their own experience ("it helped me"); the game itself
  does not claim that bee venom cures any disease.
- In town the Venom Healer works together with a doctor NPC.

**For kids:** Hivesmith, Meadow Warden and Honey Merchant are the easiest to
start with. Venom Healer is only in *Real Beekeeper*.
`[to check with developer: can a player take a second specialization later]`

## 13. NPCs

| NPC | Role |
|---|---|
| Old beekeeper (mentor) | leads the first lessons, comments on mistakes |
| Farmer | sprays; later an ally |
| Vet | diseases, mandatory reporting |
| Lab technician | honey analysis |
| Market customers | orders, questions about honey (educating the customer) |
| Factory director | long quest line |
| Teacher with kids | the player teaches a class about bees: the player becomes the teacher |
| Doctor | works with the Venom Healer, sends patients, watches safety |
| Patients | quests for the Venom Healer |

## 14. Multiplayer and competition

Competition measures **good beekeeping, not amount of honey**:
- **Honey Fair** (in town, once a season): quality is judged, not amount.
  The lab judges, not players.
- **Season leaderboard:** share of colonies that survived winter, health,
  finished lessons.

Cooperation, because real beekeeping works this way:
- **Varroa spreads between neighboring apiaries.** If a neighbor doesn't
  treat, your colonies get infested too. Treating at the same time in the
  whole area works better. A natural reason for players to talk.
- Selling and trading swarms and queens between players.
- Shared server goals: changing the farmer's behavior, the factory.
- Heroes trade services and products (section 12).

Competition per hero too: best queen breeder, best honey at the fair, the
Meadow Warden who changed the most fields.

## 15. First playable version

Small enough to build, big enough to show the game works:

- one map: player's land, acacia, meadow, one field, river, one town
- one season: spring (March to end of acacia)
- up to 3 hives per player, two hive types (to show the choice matters)
- hive inspection with tasks: queen, eggs, brood, queen cells, space
- mini games: Queen Hunt, Frame Reader, Swarm Chase, Honey Harvest
- bee companion, Beedex (first ~20 cards), Bounty Board, levels
- world blooming around the apiary (no Grey Factory yet, only mist from the field)
- hive painting
- lessons 1-4 and 6
- one product: honey (meadow and acacia), selling at the market, orders
- NPCs: mentor, farmer ("The neighbor is spraying" on the rapeseed field,
  since sunflower only blooms in summer), customer
- multiplayer on the map like the existing game, no competition yet
- both levels (*Guided* and *Real Beekeeper*), since they only change how
  much the mentor helps
- two heroes: Honey Merchant and Meadow Warden. Both use systems that are
  already in the first version (market, "The neighbor is spraying"); one is
  about trade and one about people, so it shows heroes change the game

Not in the first version: summer (linden, sunflower), winter and autumn,
varroa, diseases, factory, migration, pollination service (almonds), other
products, the fair, other heroes.

## 16. Open questions

**For Nemanja:**
1. Confirm everything marked `[to verify]`.
2. Is the hero list right: anything extra, anything missing?

**For the developer:**
1. How long is a day and a season in the game? Does the engine have time and seasons?
2. Can the engine keep changing state while the player is offline
   (colony grows, varroa grows)?
3. How many players on one map, and can they see other players' apiaries?
4. How do NPC quests work in the existing game: can a task be "click the
   right thing in the picture" (for frame inspection)?
5. Which hive types do we use and how do they look (your call)? Proposal in section 7.
6. Classes in the existing game: can they carry their own quests, equipment
   and unlocks? Can a player change or add a specialization?
