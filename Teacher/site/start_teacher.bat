@echo off
cd /d "%~dp0"
title Teacher course server
if not exist ".venv\Scripts\python.exe" (
  echo The .venv folder is missing. See README.md, section "First-time setup".
  pause
  exit /b 1
)
echo Building the site...
".venv\Scripts\python.exe" -m mkdocs build --quiet
if errorlevel 1 (
  echo Build failed. Nothing started.
  pause
  exit /b 1
)
echo Starting the server. Keep this window open while she is learning.
".venv\Scripts\python.exe" serve.py
echo.
pause
