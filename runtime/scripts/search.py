#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

def score(text, terms):
    low = text.lower()
    return sum(1 for term in terms if term in low)

def read_events(root):
    events = []
    for path in sorted((root / "live" / "events").glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            expires_at = event.get("expires_at")
            if expires_at:
                try:
                    if datetime.fromisoformat(expires_at) < datetime.now(timezone.utc):
                        continue
                except ValueError:
                    pass
            events.append(event)
    return events

def read_markdown(root):
    items = []
    for folder in ["daily", "long-term"]:
        for path in sorted((root / folder).glob("*.md")):
            items.append({"kind": folder, "source": str(path), "text": path.read_text(encoding="utf-8")[:2000]})
    return items

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()
    root = Path.cwd() / ".ally-memory"
    terms = [t.lower() for t in args.query.split() if len(t) > 2]
    ranked = []
    for item in read_events(root) + read_markdown(root):
        s = score(item.get("text", ""), terms)
        if s:
            ranked.append((s, item))
    ranked.sort(key=lambda pair: pair[0], reverse=True)
    if not ranked:
        print("Aucun résultat trouvé dans .ally-memory.")
        return
    for s, item in ranked[: args.limit]:
        text = " ".join(item.get("text", "").split())
        print(f"- [{item.get('kind')}] {text[:500]} (score {s})")

if __name__ == "__main__":
    main()

