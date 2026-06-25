#!/usr/bin/env python3
import argparse
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"(?i)(api[_-]?key|password|mot de passe|secret)\s*[:=]\s*\S+"),
    re.compile(r"\b\d{13,19}\b"),
]

def reject_secret(text):
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise SystemExit("Refus: secret potentiel détecté.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True)
    parser.add_argument("--kind", default="note", choices=["note", "decision", "action", "blocker", "client", "preference"])
    parser.add_argument("--source", default="manual")
    parser.add_argument("--ttl-hours", type=int, default=24)
    args = parser.parse_args()
    reject_secret(args.text)

    root = Path.cwd() / ".ally-memory"
    events_dir = root / "live" / "events"
    events_dir.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)
    event = {
        "ts": now.isoformat(),
        "expires_at": (now + timedelta(hours=args.ttl_hours)).isoformat(),
        "kind": args.kind,
        "source": args.source,
        "text": args.text.strip(),
    }
    path = events_dir / f"{now.date().isoformat()}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
    print(f"OK capturé: {path}")

if __name__ == "__main__":
    main()

