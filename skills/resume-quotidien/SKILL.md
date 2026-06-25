---
name: resume-quotidien
description: Produire un résumé quotidien depuis `.ally-memory/live/events/` vers `.ally-memory/daily/`. Utiliser en fin de journée, après une grosse session, quand l'utilisateur dit "résume la journée", "fais le digest", "range le bazar", ou pour préparer une reprise demain.
---

# Résumé quotidien

Transformer la mémoire 24h en page claire.

## Workflow

Lancer :

```bash
python3 .ally-memory/scripts/digest.py
```

Lire le fichier créé dans `.ally-memory/daily/YYYY-MM-DD.md`, puis répondre avec :

- décisions ;
- actions ouvertes ;
- blocages ;
- clients / prospects ;
- préférences ;
- candidats à mémoire durable.

Ne jamais transformer automatiquement une note en règle durable sans validation explicite.

