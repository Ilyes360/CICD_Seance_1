$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
  throw "Virtualenv introuvable: $python"
}

& $python -m ruff check . @args

