@echo off
REM Sunday 11:30 AM refresh. Usage: sunday_refresh.bat [new_projections.csv] [new_DKSalaries.csv]
REM Edit dfs_status_2026-11-15.json first (inactives, practice, QB starters), then run this.
set PY=C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe
cd /d D:\WKP\Fantasy-Football\dfs
if not "%~1"=="" set DFS_PROJ=%~1
if not "%~2"=="" set DFS_SAL=%~2
"%PY%" dfs_load.py
"%PY%" dfs_build.py > D:\WKP\data\dfs-friend\build_output_latest.txt
type D:\WKP\data\dfs-friend\build_output_latest.txt
