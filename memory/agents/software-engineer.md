# Lessons: software-engineer

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\software-engineer.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Follow the honesty rule: never report a number, status or file you did not retrieve | evidence: root CLAUDE.md | NEW

## Lessons
- 2026-11-24 | When a spec rule gives a trigger as a bare word list (hand, door, someone), test it against the real good set before coding it literally; bare "hand" would flag every prompt, so match verb forms and same-sentence context | evidence: software\prompt-preflight\checks.py PF04, PF05, PF10, PF11 notes in the build report | NEW
- 2026-11-24 | Put exact evidence quotes in the rule table as data and have a unit test grep each named file for them; this caught that the spec's counts (6 of 6 handoffs, joust run 3 to 6) did not match the files | evidence: software\prompt-preflight\tests\test_preflight.py test_every_quote_is_in_its_file | NEW
- 2026-11-24 | Write regexes and backslash code via the Write/Edit tool, not bash heredocs: a bash heredoc turned \b into a backspace char and silently disabled PF09 until a test listing exposed it | evidence: software\prompt-preflight\checks.py _TEXTY | NEW
- 2026-11-24 | Python source written through a bash heredoc loses backslash escapes (\b became backspace, \n became a real newline) even with a quoted delimiter; write any file containing backslashes with the Write or Edit tool, and grep the result for \x08 | evidence: software\prompt-preflight\checks.py _SIDE_CAMREL and tests test_preflight.py PF03 header test, caught by failing tests | REPEAT
- 2026-11-24 | When a noisy rule is narrowed, change the old tests that asserted the noise on purpose and list them in the CHANGELOG, not silently | evidence: PF09 tests for plate, reads, Letters on the wall | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
