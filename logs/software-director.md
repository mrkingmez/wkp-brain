## 2026-11-11 | software-director | CFB data sources: data-sourcing bench run, report in research\fantasy, SW-2026-11-11-01 queued, nothing built.

## 2026-11-12 | cfb-espn-snapshot (SW-2026-11-11-01 A)
Built software\cfb-espn-snapshot\espn_snapshot.py on top of the existing cfb_snapshot.py (imports it, no copy). 10 offline tests pass. Live run 2026-11-12: 121 games, 61 lines, 57 final, 12 calls. Tester pass launched. Not scheduled, not pushed.
2026-11-16 software-director: ARES dashboard plan + mockup delivered to D:\WKP\ARES and D:\WKP Reports\Ares Dashboard Plan. Plan only, nothing built or renamed.
- 2026-11-26 software-director: crypto watcher design done (DESIGN.md).

## 2026-11-27 Fawn Forest dashboard (software-director)
Built `D:\WKP\software\fawn-forest-dashboard\` (ffdata.py, server.py, static\, tests\, README, start-dashboard.bat). Stdlib only, 127.0.0.1:8790, GET only. Added JARVIS/ARES theme switch (themes.css tokens). Tests: test_dashboard.py 20 OK, test_hardening.py 5 OK. software-tester PASS WITH NOTES (label pill bug, NaN path, 11 crash paths, Host parsing, overflow: all fixed and retested). qa-director PASS WITH NOTES (`logs\qa\2026-11-27-fawn-forest-dashboard.md`), notes 1, 2, 5 fixed. Not done: real phone check, LIVE mode with a real watch-week log. Decisions FFDASH-2026-11-27-01, -02. I wrote the code myself (no software-engineer bench handoff) because the layer was small and cross-cutting; testers were independent.
