# Teacher course site (family use, home network only)

A small course website. It runs on this PC only when you start it. It costs nothing and uses no AI tokens.

## Start (one click)
Double-click `D:\WKP\Teacher\site\start_teacher.bat`. It builds the site, then starts the server. Keep the black window open. The window prints the address, for example `http://192.168.68.53:8800/`. Open that address on any device on the home Wi-Fi.

## Stop (one click)
Close the black window, or double-click `stop_teacher.bat`. Details are in `STOP-INSTRUCTIONS.txt`.

## One-time step for you: let her devices reach it (firewall)
Nothing was changed on this PC. Until you run this, only this PC can open the site, and Windows may ask you to allow it the first time. To allow her phone or laptop, open PowerShell as Administrator and paste exactly this (one line). It allows the port on the Private network profile only:

    New-NetFirewallRule -DisplayName "Teacher course 8800" -Direction Inbound -Protocol TCP -LocalPort 8800 -Profile Private -Action Allow

To remove it later:

    Remove-NetFirewallRule -DisplayName "Teacher course 8800"

Also check that Windows calls your home Wi-Fi a Private network (Settings, Network, the Wi-Fi name, Network profile type: Private). Never port-forward on the router.

The PC's address can change. In the router's settings, give this PC a fixed (reserved) address. That is your step, nothing here changes it.

## What it keeps
Quiz results and practice-done marks (lesson, kind, score, pass or fail, date and time) go to `D:\WKP\Teacher\data\progress.json`. That folder is gitignored. Nothing is sent to the internet.

## The progress viewer is OFF
Her consent has not been asked yet. In `config.json`, `progress_viewer_enabled` is `false`. The file is still written. Ask her first. Only after she says yes, set it to `true` and restart; the viewer is then `/progress-view` on the site.

## Settings (`config.json`)
- `port`: 8800
- `bind_address`: `auto` picks this PC's private home-network address (10.x, 172.16 to 31.x, 192.168.x). The server refuses public addresses and refuses all-addresses. Tailscale addresses (100.x) are not used.
- `progress_viewer_enabled`: false
- `unlock_enabled`: true (lessons open in order). Lesson N+1 and the next module open after the quiz is passed (2 of 3) or the practice button is pressed. Set to `false` and restart to open everything. It is a soft lock in the browser, for a family site, not security. If the check for finished lessons cannot reach the server, nothing is locked.

## First-time setup (already done on this PC)
A private Python environment is in `.venv` (MkDocs Material 9.8.1, installed with pip, free, MIT). To rebuild it: `python -m venv .venv`, then `.venv\Scripts\python.exe -m pip install mkdocs-material`.

## Editing lessons
Lessons are Markdown in `docs\`. Quiz questions are in `docs\assets\quizzes.js`. Start again to rebuild.

## Known limits
- Only module 1, lesson 1 is written, with its practice. Modules 2 to 4 are placeholders. Because an unwritten module cannot be finished, Modules 3, 4 and 5 stay locked until the ones before them exist. Set `unlock_enabled` to `false` to look at them.
- Module 5 (Advanced track) is a links page to the free MIT-licensed course "AI Engineering from Scratch". A copy is in `D:\WKP\Teacher\vendor\` (gitignored, never run, nothing installed). The site links to GitHub, it does not serve the copy.
- `/unlock-state` gives the learner's browser only the list of finished lessons. It is not the progress viewer, which stays off.
- Quiz results are stored by lesson only, with no student name (one learner).
- No password. Anyone on the home network who knows the address can open it.
- Material for MkDocs prints a notice that it reaches end of life on 2027-05-05 (fixes continue until then). Fine for a family site.
