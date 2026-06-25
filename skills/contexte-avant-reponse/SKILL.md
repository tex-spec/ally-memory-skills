---
name: contexte-avant-reponse
description: Lire le contexte local avant de répondre quand la demande dépend d'un historique. Utiliser quand l'utilisateur dit "comme hier", "on reprend", "tu te souviens", "où on en était", "sur ce client", "sur cette offre", ou quand une réponse risquerait de s'appuyer sur un souvenir inventé.
---

# Contexte avant réponse

Vérifier le contexte réel avant de répondre.

## Workflow

1. Identifier les mots utiles : client, offre, projet, date, action.
2. Chercher dans la mémoire :

```bash
python3 .ally-memory/scripts/search.py "<mots utiles>"
```

3. Lire les fichiers pertinents dans `.ally-memory/daily/` ou `.ally-memory/long-term/`.
4. Répondre depuis ce qui a été retrouvé, ou nommer clairement l'hypothèse.

## Interdit

- Répondre "de mémoire" quand la mémoire locale peut être lue.
- Dire "je ne trouve pas" sans avoir cherché.
- Confondre une supposition avec un fait.
- Répéter un contexte ancien si un résumé plus récent existe.

