# CICD_Seance_1 (Django API Etudiants)

## Setup / Installation de l'environnement

### Prerequis

- Python 3.13+
- PowerShell (Windows)
- Git (optionnel, pour versionning)

### 1) Cloner le projet

```powershell
git clone https://github.com/Ilyes360/CICD_Seance_1.git
cd CICD_Seance_1
```

### 2) Creer et activer l'environnement virtuel

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation:

```powershell
powershell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
```

### 3) Installer les dependances

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Verifier l'installation

```powershell
python --version
python -m pytest -q
python -m ruff check --config config\lint\ruff.toml .
```

### 5) Lancer l'API en local

```powershell
.\scripts\start-server.ps1
```

Puis ouvrir:

- http://127.0.0.1:8000/api/etudiants/

## Architecture actuelle

- `server/`: point de demarrage Django (`manage.py`)
- `config/project/`: configuration Django (`settings`, `urls`, `asgi`, `wsgi`)
- `config/lint/`: configuration outillage (`ruff.toml`)
- `src/app/`: modele metier (`Etudiant`)
- `src/data/`: stockage en memoire (tableau JSON) + reset des donnees
- `src/routes/`: endpoints API, separes par methode HTTP (`GET`, `POST`, `PUT`, `DELETE`)
- `tests/`: tests automatises (`pytest`) separes par type d'endpoint

## Lancement (PowerShell)

Demarrer le serveur:

```powershell
.\scripts\start-server.ps1
# ou:
venv\Scripts\python server\manage.py runserver
```

Choisir host/port:

```powershell
.\scripts\start-server.ps1 0.0.0.0:8000
```

Si l'execution des scripts PowerShell est bloquee:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-server.ps1
```

## Endpoints exposes

Base URL locale: `http://127.0.0.1:8000`

- `GET /api/etudiants/`
- `POST /api/etudiants/`
- `GET /api/etudiants/<id>/`
- `PUT /api/etudiants/<id>/`
- `DELETE /api/etudiants/<id>/`
- `GET /api/etudiants/stats/`
- `GET /api/etudiants/search/?term=<valeur>`

## Contrats API (principaux retours)

### GET liste et detail

- `GET /api/etudiants/` -> `200` + tableau JSON
- `GET /api/etudiants/<id>`:
  - `200` si trouve
  - `404` si inexistant
  - `400` si id invalide (ex: `abc`)

### POST creation

`POST /api/etudiants/`:

- `201` + etudiant cree avec `id` auto-genere
- `400` si body invalide, champ obligatoire manquant, valeur invalide
- `409` si email deja utilise

Contraintes metier:

- `firstName` et `lastName`: min 2 caracteres
- `email`: format valide + unicite
- `grade`: nombre entre 0 et 20
- `field`: `informatique`, `mathematiques`, `physique`, `chimie`

### PUT modification

`PUT /api/etudiants/<id>/`:

- `200` + etudiant modifie
- `404` si id inexistant
- `400` si id invalide ou donnees invalides
- `409` si email deja utilise par un autre etudiant

### DELETE suppression

`DELETE /api/etudiants/<id>/`:

- `200` + message de confirmation
- `404` si id invalide ou inexistant

### GET stats et recherche

- `GET /api/etudiants/stats/` -> `200` + objet:
  - `totalStudents`
  - `averageGrade` (arrondi a 2 decimales)
  - `studentsByField`
  - `bestStudent`
- `GET /api/etudiants/search/?term=...`:
  - `200` + tableau des etudiants dont nom/prenom contient le terme (insensible a la casse)
  - `400` si `term` absent ou vide

## Tests automatises

Lancer les tests:

```powershell
.\scripts\test.ps1
# ou:
venv\Scripts\python -m pytest
```

Organisation:

- `tests/conftest.py`: reset automatique des donnees avant chaque test
- `tests/test_students_get_api.py`
- `tests/test_students_post_api.py`
- `tests/test_students_put_api.py`
- `tests/test_students_delete_api.py`

## Lint

```powershell
.\scripts\lint.ps1
# ou:
venv\Scripts\python -m ruff check --config config\lint\ruff.toml .
```

