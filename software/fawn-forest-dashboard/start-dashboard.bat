@echo off
REM Starts the Fawn Forest Investments dashboard (paper only, read-only) and opens it.
cd /d D:\WKP\software\fawn-forest-dashboard
start "" http://localhost:8790
"C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe" -I server.py
pause
