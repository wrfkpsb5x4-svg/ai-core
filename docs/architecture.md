# Architecture — AI Core

## Vue d'ensemble

AI Core est le dépôt central pour les systèmes IA de Company #744879. Il sert de socle pour les projets LLM, l'évaluation des modèles et le durcissement des agents IA.

## Structure

```
src/ai_core/     Code source principal
tests/           Suite de tests (pytest)
docs/            Documentation technique
.github/         Configuration CI (GitHub Actions)
```

## Conventions

- **Langage** : Python 3.11+
- **Formatage** : black (line-length 100)
- **Lint** : ruff (règles E, F, I, B, UP)
- **Typage** : mypy --strict
- **Commits** : Conventional Commits (feat:, fix:, refactor:, docs:, test:, ci:)
- **Branches** : main (protégée) + feature/*, fix/*, hotfix/*

## CI

La CI s'exécute à chaque push et PR : lint, formatage, typage, tests.

## Workflow de contribution

1. Créer une branche `feature/*` ou `fix/*` depuis `main`.
2. Coder, tester, valider localement (`pytest`, `ruff check`, `black --check`, `mypy`).
3. Ouvrir une PR avec une description claire.
4. La CI doit être verte et la PR approuvée avant merge.