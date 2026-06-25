#!/usr/bin/env python3
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

def main():
    root = Path.cwd() / ".ally-memory"
    today = datetime.now(timezone.utc).date().isoformat()
    events_path = root / "live" / "events" / f"{today}.jsonl"
    daily_dir = root / "daily"
    daily_dir.mkdir(parents=True, exist_ok=True)
    groups = defaultdict(list)
    if events_path.exists():
        for line in events_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            groups[event.get("kind", "note")].append(event.get("text", "").strip())
    out = daily_dir / f"{today}.md"
    sections = [("decision", "Décisions"), ("action", "Actions ouvertes"), ("blocker", "Blocages"), ("client", "Clients / prospects"), ("preference", "Préférences"), ("note", "Notes")]
    lines = [f"# Résumé du jour — {today}", ""]
    for key, title in sections:
        lines.append(f"## {title}")
        items = groups.get(key, [])
        lines.extend([f"- {item}" for item in items] or ["- Rien à signaler."])
        lines.append("")
    lines.append("## À proposer en mémoire durable")
    candidates = groups.get("preference", []) + groups.get("client", [])
    lines.extend([f"- {item}" for item in candidates] or ["- Aucun candidat évident."])
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK résumé créé: {out}")

if __name__ == "__main__":
    main()

