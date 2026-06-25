# Installation en 10 minutes — Mémoire vivante de l'Allié

## Version simple pour la cliente

Ouvre Claude Code dans ton projet, donne-lui ce repo, puis colle :

```text
Installe ce pack Ally Memory Skills dans mon projet :
https://github.com/tex-spec/ally-memory-skills

Je veux que mon Allié IA puisse :
- retrouver le fil quand je dis "retrouve le fil" ;
- garder les informations utiles des dernières 24h ;
- produire un résumé quotidien ;
- conserver durablement mes règles, préférences, offres et clients importants ;
- ne jamais dire "c'est fait" sans preuve.

Installe les skills, crée la mémoire locale, ajoute la règle dans CLAUDE.md, puis teste avec une capture, une recherche et un résumé.
```

C'est tout.

Si Claude Code demande où trouver le pack, donne-lui :

```text
https://github.com/tex-spec/ally-memory-skills
```

## Ce que Claude Code doit faire

1. Cloner le repo dans un dossier temporaire ou dans le projet.
2. Depuis la racine du projet client, lancer l'installateur du repo cloné.
3. Copier les skills dans `~/.claude/skills`.
4. Créer `.ally-memory/` dans le projet client.
5. Copier les scripts dans `.ally-memory/scripts/`.
6. Ajouter la règle mémoire dans `CLAUDE.md`.
7. Tester :

```bash
python3 .ally-memory/scripts/capture.py --text "Sophie veut lancer son atelier en septembre" --kind decision
python3 .ally-memory/scripts/search.py "Sophie atelier"
python3 .ally-memory/scripts/digest.py
```

Important : ne lance pas `./install.sh` après t'être placé dans le dossier `ally-memory-skills`, sinon `.ally-memory/` risque d'être créée dans le repo cloné au lieu du projet client. Reste dans la racine du projet client et lance plutôt :

```bash
git clone https://github.com/tex-spec/ally-memory-skills.git .ally-memory-pack
bash .ally-memory-pack/install.sh
```

## Si la cliente veut comprendre

Le système a trois étages :

- **Mémoire 24h** : garde le fil vivant.
- **Résumé quotidien** : range la journée.
- **Mémoire durable** : garde ce qui compte vraiment.

La cliente n'a pas besoin de comprendre la technique pour l'utiliser.
