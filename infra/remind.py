#!/usr/bin/env python3
"""
Podsetnici na Telegram. Bez AI-ja, ciste provere vremena.

Cita content/reminders.json (pise ga samo Telegram sesija na serveru), salje
poruku kad dodje vreme i pamti poslato u content/.reminders_sent.json
(lokalno stanje, nije u gitu). Svaki podsetnik ide tacno jednom.

Format reminders.json, lista:
  {"id": "2026-09-22-objava", "due": "2026-09-22T17:00:00+02:00", "text": "Objavi X"}

Upotreba:
  python3 infra/remind.py            # posalji sve sto je dospelo
  python3 infra/remind.py --dry      # samo ispisi sta bi poslao
"""
import datetime as dt
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import notify
from x_track import tg_creds

ROOT = Path(__file__).resolve().parent.parent
REMINDERS = ROOT / "content" / "reminders.json"
SENT = ROOT / "content" / ".reminders_sent.json"
LATE_H = 6  # stariji od ovoga se salju sa oznakom da kasne


def load(path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError:
            print(f"  {path.name} nije ispravan JSON, preskacem")
    return default


def main():
    dry = "--dry" in sys.argv
    reminders = load(REMINDERS, [])
    sent = load(SENT, [])
    token, chat = tg_creds()
    if not dry and (not token or not chat):
        print("TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID nisu u .env")
        return 1
    now = dt.datetime.now(dt.timezone.utc)
    changed = False
    for r in reminders:
        rid = r.get("id")
        if not rid or rid in sent:
            continue
        try:
            due = dt.datetime.fromisoformat(r["due"])
        except (KeyError, ValueError):
            print(f"  {rid}: los 'due', preskacem")
            continue
        if due.tzinfo is None:
            print(f"  {rid}: 'due' bez vremenske zone, preskacem")
            continue
        if due > now:
            continue
        late_h = (now - due).total_seconds() / 3600
        text = "Podsetnik: " + html.escape(r.get("text", ""))
        if late_h > LATE_H:
            text += f"\n(kasni, bilo je zakazano {due.astimezone().strftime('%d.%m. %H:%M')})"
        print(f"  {rid}: {'DRY ' if dry else ''}salje ({late_h:.1f}h posle roka)")
        if dry:
            continue
        if notify.send(text, token, chat):
            sent.append(rid)
            changed = True
    if changed:
        SENT.write_text(json.dumps(sent, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
