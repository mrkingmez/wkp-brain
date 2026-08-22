@echo off
cd /d D:\WKP
git pull || exit /b 1
claude -p "Use jarvis to roll up all director logs from the last 24 hours into logs\daily-rollup.md. Queue anything blocked. Do not start new work."
git add -A
git commit -m "Nightly rollup" || exit /b 0
git push