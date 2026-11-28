# Lessons: wwd-clip-scout

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\wwd-clip-scout.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Read D:\WKP\WWD\STANDARDS.md and the SOPs before a WWD job; STANDARDS still said 4 s clips after Zac changed the rule, and the job was rebuilt twice | evidence: logs\wwd-director.md 2026-11-19, feedback-clip-length.md | NEW
- 2026-11-19 | Never use the same picture twice in one video and never hold a picture over 7 s | evidence: WWD\CLAUDE.md lock 2026-10-19 | CONFIRMED
- 2026-11-19 | No on-screen actor name tags; write run-sheet notes in plain words | evidence: memory\feedback-no-actor-tags.md | NEW
- 2026-11-19 | Cut clips 6 to 8 s, 12 s max, inside one shot, muted, on a spoken line; no total cap, report total seconds | evidence: memory\feedback-clip-length.md (Zac 2026-11-19) | CONFIRMED
- 2026-11-19 | Pull clip stock (official trailer and clips, Premiere Ready, shot map) the day after recording so the post-transcript step only cuts | evidence: SOP-WWD-Review-Workflow step 2 | NEW

## Lessons
- 2026-11-23 | Do not trust scene detection on dark or fast footage (Sneak Peek garage, trailer fights missed cuts at scores under 0.1); verify every candidate with a 6 fps strip over the clip plus 0.5 s each side before calling it one shot | evidence: Percy-Jackson-S3-E1-2-Clip-Scout.md, 4 false spans rejected by frames | NEW
- 2026-11-23 | Long uninterrupted shots live in the episode Sneak Peek or scene clip, not in trailers (trailers gave 1 usable shot in 275 s); pull the Sneak Peek first for clip stock | evidence: same report, 4 of 5 clips from Sneak Peek | NEW
- 2026-11-23 | Check the season and book title in a handoff against the official upload titles; Percy Jackson handoff said Sea of Monsters for a Season 3 video, flagged not assumed | evidence: same report, flag section | NEW
- 2026-11-23 | Python on this box is only at the Python312 path (the PATH python is the Store stub); use it with -I and numpy for frame work, ffmpeg for decoding | evidence: cut.py in D:\WKP\scratch\pj3 | NEW
- 2026-11-23 | Lightning and flash frames fool shot detectors; a "cut" pair that returns to the same framing is a flash, so compare framing across the flash at full rate before rejecting a long shot (the Curse Teaser 15 s stone shot was wrongly logged as 5 s pieces) | evidence: Percy-Jackson-S3-E1-2-Clip-Placements.md, cu-6.png and cu-14.png | NEW
- 2026-11-23 | Fetch the official YouTube caption file (yt-dlp --skip-download --write-auto-subs) to learn who speaks and what the scene is before matching clips to host lines; it named Annabeth and the Maine rescue mission and made the one honest match | evidence: scratch\pj3b\subs\sn.en.vtt | NEW
- 2026-11-23 | Word-position timing inside a host block is only an estimate; say so in the report and never present it as heard sync | evidence: same placements report, C01 row | NEW
- 2026-11-23 | A shot of an unnamed actor under a line about a named character needs an identity check by Zac; hold it, do not cut it into the folder | evidence: Curse Teaser stone shot held for Luke line | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
