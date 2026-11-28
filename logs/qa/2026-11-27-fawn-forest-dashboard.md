# QA: Fawn Forest dashboard (2026-11-27), verdict PASS WITH NOTES
Product: D:\WKP\software\fawn-forest-dashboard\ (code and UI). Checker: qa-director. Nothing edited.

## Ran myself
- tests\test_dashboard.py: 20 tests OK (python -I). tests\test_hardening.py: 5 tests OK.
- slop_check on static\app.js, index.html, README.md: clean, exit 0. Em dash count 0 in all six source/doc files. (Mechanical pass only, judgment read done by eye on UI copy: plain, no AI-tell phrases seen.)
- Live server localhost:8790: POST/PUT/DELETE return 405, Host evil.com returns 403, path traversal returns 404.
- Code grep: no os.environ/getenv, no socket/urllib/requests/subprocess; only open(..., "r"); only network call is app.js fetch("/api/state") to itself. CSP is default-src 'self'.
- Screenshots jarvis.png and ares.png viewed.

## Checklist
- Read-only: PASS. No write calls, 4 fixed files and JSON routes only.
- No order/trade controls: PASS. Only source switch and theme switch buttons.
- No keys or env reads: PASS. (insider card text names SEC_USER_AGENT as a name only.)
- No outbound network: PASS.
- PAPER ONLY badge both skins: PASS (screenshots, and .paper-badge uses --warn which both themes define).
- DEMO DATA banner both skins: PASS (sticky banner, hardcoded amber, not themed).
- Honesty / NOT AVAILABLE with source: PASS. Crypto says NOT BUILT with design path, config hash and last scan fall back to NOT AVAILABLE with source named.
- LOW SAMPLE: PASS ("LOW SAMPLE: 26 of 50 trades", and 22 of 50 for Zac ledger).
- Checklist 0 of 7: PASS in both skins, all 7 FAIL from data\go-live-checklist.json.
- README: PASS, plain steps for bat and PowerShell, phone, reading guide, limits, $0 cost.
- 3 demo numbers vs demo-out\scorecard.md: MATCH. Main closed 26, wins 11 of 26 = 42.3 percent, avg R 0.200 (0.20); net P and L 1540.11 (1.54 percent); haircut 15 bps 214.69 and 30 bps -1773.44; counted decisions 39. All from API demo state.

## Notes (none block)
1. End date mismatch in demo view: dashboard shows END DATE 2026-12-24 (read from config.yaml, which matches config line 59) beside an ENDED tag, while the demo scorecard says last day 2026-12-04. Both are traceable, but a demo screen showing a live config date next to the demo "ended" flag can confuse. Fix idea: in demo mode label the date "config end date (live plan)" or hide it.
2. Checklist item 1 note says "0 of 50, 0 of 20 on 2026-11-26" while the evidence line under it in demo shows "39 of 50 counted decisions, 22 of 20 closed Zac-ledger trades". Demo numbers beside live-dated notes read as a contradiction, and "22 of 20" looks like an error (it is over goal, true). Suggest the evidence line say "demo evidence" and "22 (goal 20)".
3. Checklist file is hand-edited and dated 2026-11-26; no staleness warning on the page if it ages. Low risk, suggest an as-of age flag.
4. Mobile: 390 px shot is cropped by headless Edge, real-phone check NOT DONE. README already says localhost only, phone not set up.
5. README "Known limits" still says "Checked in a real browser: NOT YET by the builder", now out of date after screenshots. Update the line.
6. Heat map labels are truncated ("SKIP mean reve...") in both skins, cosmetic.
7. Folder is untracked in git (new). Commit is Jarvis/Zac's step. __pycache__ present, ensure gitignored.

## Not verified
LIVE mode with a real watch-week log (none exists yet), real-phone layout, other browsers.
