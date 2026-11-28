# Lessons: wwd-run-sheet

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\wwd-run-sheet.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Read D:\WKP\WWD\STANDARDS.md and the SOPs before a WWD job; STANDARDS still said 4 s clips after Zac changed the rule, and the job was rebuilt twice | evidence: logs\wwd-director.md 2026-11-19, feedback-clip-length.md | NEW
- 2026-11-19 | Never use the same picture twice in one video and never hold a picture over 7 s | evidence: WWD\CLAUDE.md lock 2026-10-19 | CONFIRMED
- 2026-11-19 | No on-screen actor name tags; write run-sheet notes in plain words | evidence: memory\feedback-no-actor-tags.md | NEW
- 2026-11-19 | One timeline-order run sheet, revise in place, never a second dated copy; name it Edit Run Sheet | evidence: wwd-run-sheet spec 2026-10-26, SOP-Output ruling 2 and 3 | NEW
- 2026-11-19 | Every run sheet gets a LIKE AND SUBSCRIBE stop; never build a new Spoiler Alert | evidence: memory\topics\wwd-skill-formats.md 2026-10-20 | NEW
- 2026-11-19 | About half the picture stops get a designed transition, Cross Dissolve on 3 at most | evidence: WWD\CLAUDE.md 2026-10-14 | NEW

## Lessons
- 2026-11-23 | When a facts file gives a timecode for a spoken claim, open the transcript and cut from the block that holds the claim, not the block that answers it (Hades was 22:20 not 22:24, the daughters claim began at 26:41 not 26:56) | evidence: Percy Jackson S3 sheet Still open 1 and 2 | NEW
- 2026-11-23 | Never put a solo cam or a designed move on a block the facts file recommends trimming; mark the stop CONDITIONAL and say it goes with the trim | evidence: Percy Jackson S3 sheet stop 30 | NEW
- 2026-11-23 | When a clip and a picture sit on the same line, the clip owns it and the picture becomes a named spare, then recount designed share before lint | evidence: Percy Jackson S3 sheet, annabeth-percy-winter-dance.png spared, designed share 13 of 28 | NEW
- 2026-11-23 | Build the sheet from a data file plus a generator that checks every phrase count, in-block time, Said copy and file path, then fix the data, not the output | evidence: D:\WKP\scratch\pj3-runsheet\build.py, 0 problems | NEW
- 2026-11-23 | The lint only measured pictures with numbered file names; patched to accept named files so the 7 s check is real | evidence: lint_run_sheet.py edit 2026-11-23 | EDITED
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
