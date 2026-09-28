# Tehnologija: preporuka (v2, 2026-09-28)

Agent u koraku 1 (`steps.md`) prati ovo, osim ako u `progress.md` napise
razlog za drugacije. Uslovi iz steps.md vaze: web, telefon prvo, hostuje
se na nasem serveru, Stripe i Solana biblioteke postoje, mapa ima gotov
nacin.

## Zasto v2

Nemanja (28.09): Next.js mu se vec obio o glavu, hakovani su kroz modul.
Javni razlozi koji to potvrdjuju: Next.js middleware bypass (CVE-2025-29927,
mart 2025), React2Shell (CVE-2025-55182, decembar 2025, RCE bez prijave
kroz Server Actions, aktivno iskoriscavano), AVIF RCE (avgust 2026); npm
crv Shai-Hulud (septembar i novembar 2025, april 2026) koji se siri kroz
`preinstall` skripte. Zakljucak: novac, tajne i lanac ne idu u Node
proces sa hiljadu zavisnosti.

## Stek

| Sloj | Izbor | Zasto |
|---|---|---|
| Server: API, admin, placanja, poslovi, lanac | **Go** (stdlib router, pgx, stripe-go zvanicni, gagliardetto/solana-go) | jedan binarni fajl, desetak zavisnosti, nema install skripti; Stripe ima zvanicni Go SDK |
| Front: javni deo, kupac, pcelar | **SvelteKit** sa SSR za javne strane (deljenje na X, QR) | manji od Next-a, bez Server Actions; front ne drzi nijednu tajnu ni pristup bazi |
| Admin | Go, server-renderovan HTML + HTMX | najosetljiviji deo bez npm-a |
| Baza | Postgres (pgx, migracije kao SQL fajlovi) | jedna baza za sve, i merenja senzora |
| Prijava | magic link (sopstvena, u Go-u) + Sign in with Solana (potpis poruke) | bez spoljnog auth servisa |
| Kartice | Stripe Checkout + Stripe Connect Express, webhook | kartica, Apple/Google Pay, isplata pcelaru |
| USDC | wallet-standard na frontu + Solana Pay (QR); potvrda transakcije u Go-u | povezan novcanik ili QR |
| Zapisi na lancu | v1: Memo transakcija sa hash-om zapisa (kosnica, serija, dnevna potvrda senzora); Hive Pass kao Token-2022 mint sa metapodacima | sve moze iz Go-a; Metaplex Core kasnije kao izolovan mali servis sa vrucim novcanikom |
| Poslovi | tabela u Postgresu + Go worker (ili River) | bez Redisa |
| Mapa | MapLibre GL + OpenFreeMap plocice | bez Mapbox racuna |
| Slike | S3-kompatibilan storage (Hetzner Object Storage ili R2) | isti provajder kao server |
| Email | Resend | jednostavan API |
| Hosting | Docker na hb-ch-01, Cloudflare ispred | Dockerfile obrazac postoji |
| Testovi | Go test za novac i provizije; Playwright e2e za kupovinu | |

Cena ovog izbora: dva jezika, agent sporiji, Solana biblioteke u Go-u
tanje nego u TypeScript-u. Prihvaceno zbog bezbednosti.

Sta ne: Next.js (razlozi gore), Supabase/Firebase, poseban admin alat,
sopstveni Anchor program u v1, Mapbox, Redis.

## Bezbednosna pravila (vaze bez obzira na stek)

Incident na hb-01 (avgust 2026) je bio SSH kljuc na deploy nalogu, sto
nijedan framework ne resava. Zato:

1. npm samo na frontu. Lockfile, `npm ci`, `ignore-scripts=true` u
   `.npmrc`. Renovate sa minimalnom starosti paketa 7 dana (cooldown).
   Bez `postinstall` u sopstvenom kodu.
2. Najmanje zavisnosti. Svaka nova se opravdava jednom recenicom u
   `progress.md`. Pregled zavisnosti (npm audit, govulncheck) u CI.
3. Tajne nikad u repou ni u Docker slici; samo env na serveru, citljiv
   samo servisnom korisniku. Stripe webhook secret, Resend kljuc, DB
   lozinka, kljuc vruceg novcanika.
4. Vruci novcanik platforme drzi samo nedeljnu potrosnju. Treasury je
   hladan. Isplate u USDC iznad praga traze admin potvrdu.
5. Docker: non-root korisnik, read-only fajl sistem, bez privilegija,
   portovi vezani na 127.0.0.1 (vec u daemon.json), Cloudflare ispred.
6. Admin na posebnom hostname-u, sa dodatnom zastitom (Cloudflare Access
   ili IP lista) pored prijave.
7. Deploy kljucevi po serveru, rotacija, nikad deljeni sa laptopa.
   `authorized_keys` svih korisnika proverava cron jednom dnevno i javlja
   na Telegram ako se promene.
8. Logovi prijava, admin akcija i isplata se cuvaju van servera
   (Cloudflare Logs ili objekat storage), da se vide i posle upada.
9. Backup baze dnevno, van servera, sa probom vracanja jednom mesecno.
