# Lessons: software-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\software-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Follow the honesty rule: never report a number, status or file you did not retrieve | evidence: root CLAUDE.md | NEW

## Lessons
- 2026-11-24 | Mine failures into a rule table with a quoted evidence line per rule and a test that opens each source file; testers found damaged-input crashes, so test bad history and empty input early | evidence: software\prompt-preflight tester report, qa log 2026-11-24-prompt-preflight.md | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
- 2026-11-26 | When a sibling research file is promised but missing, run the bench yourself and say so; pass the retrieved facts verbatim into the architect brief so design cites caveats | evidence: crypto-api-and-data-sources-2026-11-26.md absent, data-sourcing report, DESIGN.md | NEW
- 2026-11-26 | Before building a logger plus book, order state save before log writes and test a mid-scan crash replay, and put the plan's devils-advocate amendments in the build checklist on day one | evidence: tester F4, qa N4 on wkt-alpaca-watcher | NEW
- 2026-11-26 | Run the read-only smoke BEFORE finalising a feed-dependent build: it showed IEX hourly bars span 08:00 to 16:00 ET, which the plan and README had wrong; add a session filter and report real response shapes | evidence: smoke-preflight.json, wkt-alpaca-watcher session_bars | NEW
- 2026-11-26 | Iterate dicts in sorted order and test a crash-and-resume run against an uninterrupted run line for line; JSON reload reorders dicts and silently swapped ids | evidence: TestCrashSafety, engine sorted(bk[...]) | NEW
- 2026-11-27 | For a dashboard over another tool's files, read every field defensively (as_dict, num, clean NaN at output) and run a fuzz pass for reshaped input before handoff; the tester found 11 crash paths and a NaN that killed the response | evidence: fawn-forest-dashboard tester report 2026-11-27 | NEW
- 2026-11-27 | Pass element children as nodes, not through a text helper, and put theme tokens in one file; a label helper printed "[object HTMLSpanElement]" | evidence: app.js label(), tester screenshot | NEW
- 2026-11-27 | A test that loops until a fake clock says closed must give the fake a closing step, or it spins forever; and never taskkill python.exe by name when other agents run python, stop by PID after listing command lines | evidence: wkt-alpaca-watcher TestEarlyCloseEndRule hang, killed PID 24448 only | NEW
- 2026-11-27 (insider scanner v0.2.0): bash heredocs choke on apostrophes, write patch scripts with the Write tool. Source files are CRLF, so mutation patterns with newlines need \r\n. An append-only ledger needs a stable id and retraction lines from day one (tester F1). Check the guard order in main for every mode, and require tzdata for ZoneInfo on Windows.
- 2026-11-27 (watcher changes 4 and 5): a stale demo-out can make a bug look reproducible when it is not, so rerun the demo on the PRE-fix code before claiming a before number. Full suite was 5 min alone and 25 min with four runs at once: test a snapshot copy in scratch while editing, and do not start more than two heavy runs together. | evidence: wkt-alpaca-watcher CHANGES-2026-11-26.md | NEW
- 2026-11-27 (watcher changes 6 to 8): a new guard that reads a state field adds a new crash path when it runs earlier than the old reader (tester N1: _expired reads signal_bar_t even with no bars), so wrap every new reader of persisted fields on day one; when an order says "same as main" check main actually has that rule first (main had no date expiry, only the gap cancel) and report the mismatch. A test meant to fail on old code must isolate its rule (the month limit hid the rolling-window case until I set it to 99). Snapshot-copy plus two parallel full suites kept each run under 14 min. | evidence: tester-pass4, qa-pass4, CHANGES-2026-11-26.md | NEW
