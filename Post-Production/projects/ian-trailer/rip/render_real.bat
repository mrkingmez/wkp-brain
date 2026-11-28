@echo off
REM Renders the center-tear W1 rip (rip_center.py) from the two real stills. Auto-versions: picks the next vN that has no file yet.
REM Optional arg: force a version number, e.g. render_real.bat 5. Old v1 (rip.py, diagonal falling halves) is never overwritten.
set PIC=P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Pictures
set RC=P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut
set N=%1
if not "%N%"=="" goto go
set N=2
:loop
if exist "%RC%\Ian-Trailer-W1-Rip-3s-16x9-v%N%-*" (
  set /a N+=1
  goto loop
)
:go
set OUT=%RC%\Ian-Trailer-W1-Rip-3s-16x9-v%N%-center-silent.mp4
echo Rendering %OUT%
C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe "%~dp0rip_center.py" --a "%PIC%\W1a-together.png" --b "%PIC%\W1b-caught.png" --out "%OUT%" --frames-dir "D:\WKP\scratch\rip-center-frames-v%N%"
