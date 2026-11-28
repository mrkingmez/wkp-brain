# Lessons: software-tester

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\software-tester.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Follow the honesty rule: never report a number, status or file you did not retrieve | evidence: root CLAUDE.md | NEW

## Lessons
- 2026-11-24 | When testing a history/state file, test text garbage and binary garbage separately, the first crash hides the second | evidence: prompt-preflight test, binary byte crashed before JSONDecodeError was reached | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
- 2026-11-26 | When a loop treats 'None' as 'market closed', test a single transient failure mid-run; and test crash-between-writes by replaying a scan from a pre-scan state snapshot | evidence: wkt-alpaca-watcher F1 and F4, logs/qa/2026-11-26-wkt-alpaca-watcher-tester.md | NEW
- 2026-11-26 | Before blaming a loop test, check that a patched time.sleep still reaches a function whose default arg was bound at def time; and test restart-after-close separately from run-through-close | evidence: wkt watcher pass 2, old loop case hung, E3 end rule not applied after Friday after-close restart | NEW
- 2026-11-27 | When a tool writes append-only result files, test two runs in a row (a cluster that disappears, an id that moves) and read the file the scorer reads, not the in-memory result; also test every mode with an output folder inside the forbidden folder using a FAKE forbidden folder in scratch | evidence: wkt-insider-scanner F1 (stale and double COUNTED records) and F2 (--score wrote config-history inside the fake watcher folder before the guard), docs/TESTER-REPORT-2026-11-27.md | NEW
- 2026-11-27 | When a change adds a check before an existing guarded code path, test it with the guarded precondition absent (no bars, empty list); the new early call can crash where the old path was skipped | evidence: wkt-alpaca-watcher pass 4 N1, _expired crashed on bad signal_bar_t with no bars, base did not, logs/qa/2026-11-27-wkt-alpaca-watcher-tester-pass4.md | NEW
