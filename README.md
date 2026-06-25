# Ally Memory Skills

Pack open source pour donner une mémoire vivante simple à un Allié IA dans Claude Code.

Usage visé : une cliente ouvre Claude Code, donne ce dossier, colle le prompt de `INSTALL.md`, et Claude installe le système.

Repo public :

```text
https://github.com/tex-spec/ally-memory-skills
```

## Inclus

- `memoire-vivante`
- `resume-quotidien`
- `memoire-durable`
- `contexte-avant-reponse`
- `preuve-avant-fait`

## Installation manuelle

Depuis la racine du projet client :

```bash
git clone https://github.com/tex-spec/ally-memory-skills.git
cd ally-memory-skills
./install.sh
```

Puis tester :

```bash
python3 .ally-memory/scripts/capture.py --text "Sophie veut lancer son atelier en septembre" --kind decision
python3 .ally-memory/scripts/search.py "Sophie atelier"
python3 .ally-memory/scripts/digest.py
```

## Limite V1

Ce pack pose le cœur mémoire portable. Il ne branche pas automatiquement Telegram, Slack, WhatsApp ou les emails.
