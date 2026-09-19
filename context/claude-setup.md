# Claude Code setup za HiveBits

Referentni fajl. Drzi ga na `~/hivebits/swarm/context/claude-setup.md`.

## Struktura na disku

```
~/hivebits/                    <- postojeci folder, ne diramo
├── ...ostale HiveBits stvari...
└── swarm/                     <- jedini folder odakle se pokrece Claude Code
    ├── .claude/
    │   ├── agents/            <- agenti za sve HiveBits repoe
    │   ├── commands/          <- /investor-update, /server-check
    │   ├── skills/
    │   └── settings.json      <- permissions, env, additionalDirectories
    ├── CLAUDE.md              <- pravila za ceo HiveBits
    ├── context/               <- tokenomics.md, roadmap.md, farm-status.md, ovaj fajl
    ├── dapp/                  <- git repo, ima svoj .claude/ i CLAUDE.md
    ├── firmware/              <- git repo, ima svoj .claude/ i CLAUDE.md
    └── infra/                 <- skripte za hb-01-nbg1
```

Plus `~/.claude/agents/` izvan svega, za agente koji nisu vezani za HiveBits.

`swarm/` nije git repo, samo kontejner. Svaki podfolder je svoj repo.

Repoi koji su vec negde drugde: simlinkuj ih unutra
(`ln -s ~/putanja/do/dapp ~/hivebits/swarm/dapp`) ili dodaj
`additionalDirectories` u `swarm/.claude/settings.json`.

## Kako se ucitava

Claude Code trazi `.claude/` uz put nagore od foldera u kom je pokrenut.
Pokrenes iz `swarm/dapp` i dobijes dapp agente + one iz `swarm/.claude/agents/`
+ globalne iz `~/.claude/agents/`. Isto vazi za CLAUDE.md, svi se nadovezuju.

## Agents vs skills vs commands

- `agents/` - svoj system prompt, svoj set alata, svoj model. Claude ga zove
  sam kad prepozna da treba, ili mu ti kazes. Za kad hoces izolovan kontekst
  ili ogranicene alate.
- `skills/` - procedura, "ovako se radi X". Claude je ucita kad zatreba.
- `commands/` - slash komanda koju ti kucas.

Vecina onoga sto prvo zatreba su commands i skills, ne agenti.

Format agenta (`.claude/agents/firmware-verifier.md`):

```markdown
---
name: firmware-verifier
description: Flesuje ESP32, cita serial, potvrdjuje da node radi
tools: Bash, Read
model: sonnet
---

Ti verifikujes firmware promene. Nikad ne prijavljuj uspeh
bez stvarnog serial outputa. Koraci: ...
```

Ne pisi ih rucno. `/agents` u Claude Code, opises sta hoces, on napise fajl.
Isto i `/statusline`, `/permissions`.

Pravi trigger za novi agent: kad drugi put u istoj nedelji objasnjavas
Claude-u isti postupak. Ne pre toga.

## Radni model

- Fable 5 + auto mode + `/effort xhigh` za ozbiljne stvari. Plan mode vise
  nije potreban.
- Verifikacija je stvar broj jedan. Dapp -> Claude in Chrome ekstenzija.
  Firmware -> skripta koja flesuje i cita serial log, pa
  `/goal "node se javlja na 60s bez WiFi dropa 30 minuta"`.
- Worktrees (`claude -w`) cim krenu paralelne stvari.
- `claude agents` iz `swarm/` da se vide sve sesije na jednom mestu.
- Context minimalism: ne trpaj context/ fajlove u svaki prompt, daj Claude-u
  nacin da ih povuce kad zatreba.

## Navika koja najvise vredi

Svaki put kad Claude pogresi, ne ispravljaj ga u chatu. Kazi mu da to upise
u CLAUDE.md ili da napravi skill. Ispravka u chatu resava jedan run, upisano
pravilo resava sve sledece.

## Kandidati za commands

- `/investor-update` - git log + server metrike + stanje kosnica -> update
- `/x-post`, `/tg-announce` - tvoj glas, kroz postojeci TG approval flow
- `/server-check` - SSH na hb-01-nbg1, memorija, procesi
- `/techdebt` - na kraju sesije

## Rutine

- `/schedule` u cloudu: jutarnji server health + pregled TG grupe
- `/loop` lokalno za duge stvari (babysit PR-ova, pracenje firmware testa)
- Routines sa GitHub triggerom: code review agenti na svaki PR

## Sta preskacemo za sada

Dynamic workflows i nested subagents. Skupi su, isplate se tek kod velikih
migracija ili batch fixeva.
