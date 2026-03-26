$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
  throw "Virtualenv introuvable: $python"
}

# Start Django server (passes the provided arguments to runserver)
& $python (Join-Path $PSScriptRoot "..\manage.py") runserver @args

