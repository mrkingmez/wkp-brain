@echo off
rem Runs every prompt-preflight test. Python path: set PREFLIGHT_PY, or edit nothing and use "python" on PATH.
rem (The real interpreter path is in D:\WKP\LOCAL-PATHS.md, section Tools.)
cd /d "%~dp0.."
if not defined PREFLIGHT_PY set PREFLIGHT_PY=python
"%PREFLIGHT_PY%" -m unittest discover -s tests -v
echo exit code %ERRORLEVEL%
