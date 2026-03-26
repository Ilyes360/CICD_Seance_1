$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot "..\venv\Scripts\python.exe"
if (-not (Test-Path $python)) {
  throw "Virtualenv introuvable: $python"
}

$ruffConfig = Join-Path $PSScriptRoot "..\config\lint\ruff.toml"
& $python -m ruff check --config $ruffConfig . @args

