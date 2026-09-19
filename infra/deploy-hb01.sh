#!/usr/bin/env bash
# Salje tracker na hb-01-nbg1 i postavlja cron. Pokrece se lokalno.
#
#   ./infra/deploy-hb01.sh <ssh-host>        npr. ./infra/deploy-hb01.sh hb-01-nbg1
#
# Na server ide samo ono sto trackeru treba: tri skripte, profiles.json, .env.
# NE ide 881MB videa, ne idu playbook-ovi, ne ide istorija postova.
set -euo pipefail

HOST="${1:?Daj ssh host, npr: ./infra/deploy-hb01.sh hb-01-nbg1}"
REMOTE="${REMOTE_DIR:-/opt/hivebits-x}"
LOCAL="$(cd "$(dirname "$0")/.." && pwd)"

echo "== provera python3 na $HOST =="
ssh "$HOST" 'python3 -c "import sys; print(sys.version.split()[0])"' \
  || { echo "python3 nije dostupan na serveru"; exit 1; }

echo "== pravim $REMOTE =="
ssh "$HOST" "mkdir -p $REMOTE/infra $REMOTE/content/profiles"

echo "== saljem fajlove =="
rsync -av \
  "$LOCAL/infra/x_fetch.py" "$LOCAL/infra/x_track.py" "$LOCAL/infra/notify.py" \
  "$HOST:$REMOTE/infra/"
rsync -av "$LOCAL/content/profiles.json" "$HOST:$REMOTE/content/"
# meta.json po nalogu treba za baseline racun; posts.jsonl ne treba
for d in "$LOCAL"/content/profiles/*/; do
  slug="$(basename "$d")"
  [ -f "$d/meta.json" ] || continue
  ssh "$HOST" "mkdir -p $REMOTE/content/profiles/$slug"
  rsync -a "$d/meta.json" "$HOST:$REMOTE/content/profiles/$slug/"
done

echo "== saljem .env (chmod 600) =="
rsync -av "$LOCAL/.env" "$HOST:$REMOTE/.env"
ssh "$HOST" "chmod 600 $REMOTE/.env"

echo "== postavljam cron =="
# Raspored je pravljen prema budzetu od 1000 requesta mesecno.
# Gusto merenje samo tamo gde se odlucuje: post izlazi 18-21h.
# Ukupno ~680 req/mesec, ostatak je rezerva za rucna povlacenja.
ssh "$HOST" "bash -s" <<REMOTE_EOF
set -e
PY=/usr/bin/python3
TRACK_EVE="13 18-23 * * 1-5 cd $REMOTE && \$PY infra/x_track.py --days 3 --notify --quiet >> $REMOTE/track.log 2>&1"
TRACK_DAY="13 9,13 * * * cd $REMOTE && \$PY infra/x_track.py --days 3 --notify --quiet >> $REMOTE/track.log 2>&1"
WEEKLY="0 20 * * 0 cd $REMOTE && \$PY infra/x_fetch.py --max 60 >> $REMOTE/fetch.log 2>&1"
(
  crontab -l 2>/dev/null | grep -v 'x_track.py' | grep -v 'x_fetch.py'
  echo "\$TRACK_EVE"
  echo "\$TRACK_DAY"
  echo "\$WEEKLY"
) | crontab -
echo "cron postavljen:"
crontab -l | grep -E 'x_track|x_fetch'
REMOTE_EOF

echo
echo "== test pokretanje na serveru =="
ssh "$HOST" "cd $REMOTE && python3 infra/x_track.py --days 2 --quiet && tail -3 content/tracking.jsonl | cut -c1-120"

cat <<TIP

Gotovo.

Podaci se skupljaju u  $HOST:$REMOTE/content/tracking.jsonl
Log                    $HOST:$REMOTE/track.log

Povuci ih lokalno kad se vratis:
  ./infra/pull-hb01.sh $HOST

Ugasi cron:
  ssh $HOST "crontab -l | grep -v x_track.py | crontab -"
TIP
