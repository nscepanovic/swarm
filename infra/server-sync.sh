#!/usr/bin/env bash
# Salje podatke koje server prikupi (pracenje, nedeljni fetch) nazad u git,
# da ih vide i laptop i cloud sesije.
#
# Server je JEDINI pisac za:
#   content/tracking.jsonl
#   content/profiles/*/posts.jsonl, replies.jsonl, meta.json
# Laptop ove fajlove samo cita. Zato nema konflikata.
#
# Pokrece se iz crona dva puta dnevno, ne posle svakog merenja - inace bi
# istorija gita bila puna "tracking" commitova.
set -euo pipefail
cd "$(dirname "$0")/.."

git pull -q --rebase --autostash
git add content/tracking.jsonl content/profiles/ content/profiles.json 2>/dev/null || true
if git diff --cached --quiet; then
  echo "$(date -u +%FT%TZ) nista novo"
  exit 0
fi
git commit -q -m "data: pracenje i profili $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q
echo "$(date -u +%FT%TZ) poslato: $(git log -1 --format=%h)"
