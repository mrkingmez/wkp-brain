# Lessons: trading-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\trading-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Investing\watch-week\ does not exist yet; create it when the watch week starts | evidence: system reset path check 2026-11-19 | NEW

## Lessons
- 2026-11-26 | Bash may not see user env vars set after the session started; load them from User scope into Process scope in a .ps1 wrapper and never print them | evidence: KeyError on first probe, run_probe.ps1 worked | NEW
- 2026-11-26 | Free Alpaca paper account gets IEX only; SIP returns 403, so always pass feed=iex and state it | evidence: request IDs in WATCH-WEEK-PLAN.md | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
- 2026-11-27 | When a ruling says build waits on conditions, order the ruling BEFORE the build, not in parallel; offline build is harmless but costs rework | evidence: insider scanner built before devils-advocate ruling, 11 amendments needed | NEW
