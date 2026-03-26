# CICD_Seance_1 (Django)

## Commands (PowerShell)

Start the Django server:

```powershell
.\scripts\start-server.ps1
# or:
venv\Scripts\python server\manage.py runserver
```

Optional: choose host/port:

```powershell
.\scripts\start-server.ps1 0.0.0.0:8000
```

If PowerShell blocks script execution:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-server.ps1
```

Run tests:

```powershell
.\scripts\test.ps1
# or:
venv\Scripts\python -m pytest
```

Run the linter (Ruff):

```powershell
.\scripts\lint.ps1
# or:
venv\Scripts\python -m ruff check --config config\lint\ruff.toml .
```

