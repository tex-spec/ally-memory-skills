---
name: memoire-vivante
description: Retrouver, lire et alimenter la mémoire vivante locale de l'Allié IA dans `.ally-memory`. Utiliser quand l'utilisateur dit "retrouve le fil", "souviens-toi", "où on en était", "garde ça", "note ça", ou quand une information récente doit être conservée 24h dans un projet Claude Code standard.
---

# Mémoire vivante

Utiliser `.ally-memory/` comme carnet vivant 24h.

## Workflow

Pour retrouver :

```bash
python3 .ally-memory/scripts/search.py "<requête>"
```

Pour garder :

```bash
python3 .ally-memory/scripts/capture.py --text "<information>" --kind note
```

Choisir `--kind` : `note`, `decision`, `action`, `blocker`, `client`, `preference`.

## Règles

- Ne jamais stocker un secret brut, un mot de passe, une clé API ou une donnée bancaire.
- Ne pas garder tout le transcript. Garder seulement le fait utile.
- Si `.ally-memory/` n'existe pas, demander d'installer le pack Ally Memory Skills.
- Répondre avec ce qui a été retrouvé ou capturé, puis une prochaine action utile.
