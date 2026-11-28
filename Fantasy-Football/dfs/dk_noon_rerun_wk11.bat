@echo off
REM Week 11 Sunday 11/22 noon rerun, clean full refresh + rebuild. Decision support only: never logs in, never enters, never spends.
REM Usage: dk_noon_rerun_wk11.bat "<fresh entries template csv>" ["Inactive One;Inactive Two"] [--drop-q]
REM  1) Zac downloads a FRESH entries template (Lineups > Edit Entries > Download) into D:\Draft Kings\Week 11\ (same entry IDs).
REM  2) Before running: update TB (and ARI) in D:\Draft Kings\Week 11\qbs_confirmed_week11.json, and in
REM     D:\WKP\data\ff-simulator\overrides_2026_wk11.json "qbs" block if the default QB is wrong (qb_check prints it).
REM  3) Output goes to D:\Draft Kings\Week 11\sun\ ; both checks in build_report.txt must say RESULT: PASS. Upload the file ending "- FILLED.csv".
set PY=C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe
set TEMPLATE=%~1
set OUTS=%~2
if "%TEMPLATE%"=="" (echo Give the fresh entries template path as the first argument. & exit /b 1)
cd /d D:\WKP\Fantasy-Football\dfs
if "%OUTS%"=="" (
  "%PY%" -I dk_own_build.py --week 11 --dk-salaries "D:\Draft Kings\Week 11\DKSalaries_week11.csv" --template "%TEMPLATE%" --outdir "D:\Draft Kings\Week 11\sun" %3
) else (
  "%PY%" -I dk_own_build.py --week 11 --dk-salaries "D:\Draft Kings\Week 11\DKSalaries_week11.csv" --template "%TEMPLATE%" --outdir "D:\Draft Kings\Week 11\sun" --out "%OUTS%" %3
)
echo.
echo Read D:\Draft Kings\Week 11\sun\build_report.txt, both checks must say RESULT: PASS.
