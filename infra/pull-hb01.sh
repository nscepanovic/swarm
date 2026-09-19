#!/usr/bin/env bash
# Povlaci prikupljene snimke sa servera i spaja ih sa lokalnim tracking.jsonl.
#   ./infra/pull-hb01.sh <ssh-host>
set -euo pipefail
HOST="${1:?Daj ssh host}"
REMOTE="${REMOTE_DIR:-/opt/hivebits-x}"
LOCAL="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp)"

rsync -av "$HOST:$REMOTE/content/tracking.jsonl" "$TMP"

python3 - "$TMP" "$LOCAL/content/tracking.jsonl" <<'PY'
import json, sys
from pathlib import Path
remote, local = Path(sys.argv[1]), Path(sys.argv[2])
rows = {}
for f in (local, remote):
    if f.exists():
        for line in f.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                rows[(r["id"], r["ts"])] = r     # isti snimak se ne duplira
out = sorted(rows.values(), key=lambda r: (r["created_at"], r["ts"]))
local.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n")
print(f"spojeno: {len(out)} snimaka u {local}")
PY
rm -f "$TMP"
