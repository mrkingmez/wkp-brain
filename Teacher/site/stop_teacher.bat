@echo off
cd /d "%~dp0"
if not exist "..\data\server.pid" (
  echo Teacher is not running, or it was already stopped.
  pause
  exit /b 0
)
set /p PID=<"..\data\server.pid"
taskkill /PID %PID% /F
del "..\data\server.pid" 2>nul
echo Teacher stopped.
pause
