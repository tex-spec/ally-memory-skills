#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(pwd)"
CLAUDE_SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
MEMORY_DIR="$PROJECT_DIR/.ally-memory"

mkdir -p "$CLAUDE_SKILLS_DIR"
cp -R "$ROOT/skills/"* "$CLAUDE_SKILLS_DIR/"

mkdir -p "$MEMORY_DIR/live/events" "$MEMORY_DIR/daily" "$MEMORY_DIR/long-term" "$MEMORY_DIR/scripts"
cp "$ROOT/runtime/scripts/"*.py "$MEMORY_DIR/scripts/"
chmod +x "$MEMORY_DIR/scripts/"*.py

if [ ! -f "$MEMORY_DIR/config.json" ]; then
  printf '%s\n' '{' '  "ttl_hours": 24,' '  "secret_policy": "never_store_raw_passwords_api_keys_or_payment_data"' '}' > "$MEMORY_DIR/config.json"
fi

touch "$PROJECT_DIR/CLAUDE.md"
if ! grep -q "Mémoire vivante de l'Allié" "$PROJECT_DIR/CLAUDE.md"; then
  cat >> "$PROJECT_DIR/CLAUDE.md" <<'MD'

## Mémoire vivante de l'Allié

Quand l'utilisateur dit "retrouve le fil", "souviens-toi", "où on en était", ou quand le contexte est flou :

1. Lire d'abord `.ally-memory/daily/`, puis chercher dans `.ally-memory/live/events/`.
2. Chercher aussi dans `.ally-memory/long-term/` si la question concerne une offre, un client, une préférence ou une règle.
3. Répondre avec le contexte retrouvé, puis la prochaine action utile.
4. Ne pas inventer une mémoire absente. Dire clairement si rien n'a été trouvé.

Après une session utile, proposer une synthèse courte : décisions, actions ouvertes, blocages, informations à garder durablement.

Ne jamais enregistrer de secret brut, mot de passe, clé API ou donnée bancaire.
MD
fi

echo "OK Ally Memory installé"
echo "Skills: $CLAUDE_SKILLS_DIR"
echo "Mémoire projet: $MEMORY_DIR"

