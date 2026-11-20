# Lessons: qa-media

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\qa-media.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | scratch\qa\ does not exist until first use; create it | evidence: system reset path check 2026-11-19 | NEW

## Lessons
- 2026-11-19 | For a black-background overlay file, decode the whole file to 64x36 gray rawvideo once and score every stop against every source in Python; it is faster and stronger than per-frame ssim, and blackdetect and freezedetect then only need classifying against stop windows | evidence: AKT stringout QA, 36 of 36 stops matched in about 2 min | NEW
- 2026-11-19 | In Python report strings write Windows paths in raw strings, a bare \a in D:\WKP\scratch\akt-qa becomes a BEL character | evidence: AKT QA report first draft | NEW
