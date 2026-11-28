# Lessons: qa-media

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\qa-media.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | scratch\qa\ does not exist until first use; create it | evidence: system reset path check 2026-11-19 | NEW

## Lessons
- 2026-11-19 | For a black-background overlay file, decode the whole file to 64x36 gray rawvideo once and score every stop against every source in Python; it is faster and stronger than per-frame ssim, and blackdetect and freezedetect then only need classifying against stop windows | evidence: AKT stringout QA, 36 of 36 stops matched in about 2 min | NEW
- 2026-11-19 | In Python report strings write Windows paths in raw strings, a bare \a in D:\WKP\scratch\akt-qa becomes a BEL character | evidence: AKT QA report first draft | NEW
- 2026-11-26 | When a plan json exists, still map every cam run to the isolated mic tracks and compute the wrong-speaker fraction yourself; ebur128 stereo of a dual-mono voice reads 3 dB higher than the mono downmix, so run per-window loudness on the stereo file | evidence: Percy v3 QA, mono windows read -17 and stereo -14 | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
