@echo off
rem WKP nightly SYSTEM CHECK (proposed 2026-11-12, replaces nightly.bat once Zac says yes).
rem Order: pull, read-only system check, the old director-log rollup (kept), commit, push.
rem The checks are read-only. Safe fixes (scratch, TEMP, pycache, log rotation) run per machines.json, dry-run by default, kill switch D:WKPdatasystem-check-fixes.disabled. Exit 1 (YELLOW) and 2 (RED) do not stop the job.
cd /d D:\WKP
git pull || exit /b 1
C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\.claude\skills\wkp-system-check\scripts\system_check.py
claude -p "Use jarvis to roll up all director logs from the last 24 hours into logs\daily-rollup.md and add one line quoting logs\system-check\latest.txt. Queue anything blocked. Do not start new work."
git add -A
git commit -m "Nightly system check and rollup" || exit /b 0
git push
