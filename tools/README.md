# 📦 Objectif

Ce script :
Vérifie que la version dans pyproject.toml correspond à celle demandée

- Crée un commit (si nécessaire)

- Tague le commit avec vX.Y.Z

- Push le tout proprement

- T’affiche un modèle de changelog pour ta release GitHub

# Comment l’utiliser

1. Place ce script dans : tools/release.py

2. Depuis la racine de ton projet :

```bash
python tools/release.py
```
⚠️ Tu dois avoir commit tous tes changements sauf le bump de version, que ce script va committer lui-même avec le tag.