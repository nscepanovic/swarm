# Tehnologija: preporuka (2026-09-28)

Agent u koraku 1 (`steps.md`) prati ovo, osim ako u `progress.md` napise
razlog za drugacije. Uslovi iz steps.md vaze: web, telefon prvo, hostuje
se na nasem serveru, Stripe i Solana biblioteke postoje, mapa ima gotov
nacin.

| Sloj | Izbor | Zasto |
|---|---|---|
| Aplikacija | Next.js (App Router) + TypeScript | swarm app je vec Next 16; jedan jezik za front, API i admin; Docker ili Vercel |
| UI | Tailwind + shadcn/ui | tokeni iz SKILL.md se mapiraju direktno; pristupacne komponente |
| Baza | Postgres + Drizzle ORM | jedna baza za sve, i za merenja senzora (TimescaleDB kasnije ako treba) |
| Prijava | Better Auth (magic link) + Sign in with Solana | email bez lozinke i novcanik na istom nalogu, bez spoljnog servisa |
| Kartice | Stripe Checkout + Stripe Connect Express | kartica, Apple/Google Pay, isplata pcelaru na racun, webhook |
| USDC | Solana wallet-adapter + Solana Pay (QR) | povezan novcanik ili QR bez novcanika |
| Zapisi na lancu | Metaplex Core | kosnica, serija i Hive Pass kao Core asset-i; bez sopstvenog programa u v1 |
| Dnevna potvrda senzora | Memo transakcija sa hash-om dnevnih merenja | najprostije sto ispunjava spec 9.4 |
| Mapa | MapLibre GL + OpenFreeMap plocice | bez Mapbox racuna i limita; tihe boje |
| Slike | S3-kompatibilan storage (Hetzner Object Storage ili Cloudflare R2) | server je na Hetzneru; smanjivanje na klijentu pre slanja |
| Email | Resend | jednostavan API; sabloni iz admin Content-a |
| Pozadinski poslovi | pg-boss | red u Postgresu, bez Redisa; zapisi na lancu, isplate, podsetnici |
| Hosting | Docker na hb-ch-01; Vercel kao opcija | Dockerfile obrazac postoji u swarm app-u |
| Testovi | Vitest + Playwright | jedinicni za novac i provizije; e2e za kupovinu karticom i USDC |

Sta ne: Supabase/Firebase (Postgres drzimo sami), poseban admin alat
(admin je vezan za tokove), sopstveni Anchor program u v1 (Core pokriva;
program se doda kasnije bez seobe podataka), Mapbox (naplata po
ucitavanju), Redis (pg-boss pokriva).

Otvoreno: Metaplex Core naspram sopstvenog programa je jedina prava
dilema. Core dobija u v1 zbog cene i brzine.
