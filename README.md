# AI Core

Repository central pour les systèmes IA de Company #744879.

## Description

AI Core est le socle technique pour les projets LLM, l'évaluation des modèles et le durcissement des agents IA. Il fournit une structure de projet Python propre, une CI fonctionnelle et des conventions de code claires.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Usage

```python
from ai_core.main import run

result = run()
print(result)  # {'status': 'ok', 'config': {'name': 'ai-core', 'version': '0.1.0', 'debug': False}}
```

## Tests

```bash
pytest --cov=src/
```

## CI

La CI (GitHub Actions) s'exécute à chaque push et pull request :
- **Lint** : ruff
- **Formatage** : black --check
- **Typage** : mypy --strict
- **Tests** : pytest --cov

## Contribution

1. Créer une branche `feature/*` ou `fix/*` depuis `main`.
2. Valider localement : `ruff check src/ tests/`, `black --check src/ tests/`, `mypy src/`, `pytest`.
3. Ouvrir une pull request avec une description claire.
4. La CI doit être verte et la PR approuvée avant merge.

## Conventions

| Domaine | Convention |
| --- | --- |
| Formatage | black (line-length 100) |
| Lint | ruff (E, F, I, B, UP) |
| Typage | mypy --strict |
| Commits | Conventional Commits (feat:, fix:, refactor:, docs:, test:, ci:) |
| Branches | main (protégée) + feature/*, fix/*, hotfix/* |