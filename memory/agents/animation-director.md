# Lessons: animation-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\animation-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Follow the honesty rule: never report a number, status or file you did not retrieve | evidence: root CLAUDE.md | NEW

## Lessons
- 2026-11-24 | When a rendered check disagrees with a number you read from the scene, trust neither until you find why: the previs hand gap said 0.174 m while the picture showed about 0.6 m, and the cause was a parent offset bug | evidence: ANIMATION\previs\previs_lib.py root empty fix, Previs Method docx | NEW
- 2026-11-24 | For any layout previs, state each hand and each side in the card and let the report name the near hand and the holding hand per character, because a prompt that says the hand nearest the camera is wrong when the holding hand is the far one | evidence: ANIMATION\previs\renders\ian-garage-handoff-v1\REPORT.md | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
