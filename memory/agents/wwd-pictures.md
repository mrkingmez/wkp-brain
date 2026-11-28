# Lessons: wwd-pictures

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\wwd-pictures.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Read D:\WKP\WWD\STANDARDS.md and the SOPs before a WWD job; STANDARDS still said 4 s clips after Zac changed the rule, and the job was rebuilt twice | evidence: logs\wwd-director.md 2026-11-19, feedback-clip-length.md | NEW
- 2026-11-19 | Never use the same picture twice in one video and never hold a picture over 7 s | evidence: WWD\CLAUDE.md lock 2026-10-19 | CONFIRMED
- 2026-11-19 | No on-screen actor name tags; write run-sheet notes in plain words | evidence: memory\feedback-no-actor-tags.md | NEW
- 2026-11-19 | Gap-fill pictures come from the title being reviewed, not other shows, unless a major feature point | evidence: memory\feedback-secondary-pictures.md (Zac 2026-11-10) | CONFIRMED
- 2026-11-19 | Cover every character with a real subplot, not just the leads | evidence: memory\topics\visual-media.md (Heat miss 2026-09-14) | NEW
- 2026-11-19 | IMDb blocks curl and WebFetch; use TMDb, Rotten Tomatoes and Commons, and log the block in TASKS the same run | evidence: agent-runs.md 2026-11-19 wwd-pictures row | CONFIRMED
- 2026-11-19 | If the _src delete is denied, log it in logs\wwd-director.md and TASKS.md instead of leaving it in the bench report | evidence: A Knight's Tale _src 23.9 MB left behind 2026-11-19 | NEW
- 2026-11-19 | Contain and fit, never crop | evidence: memory\topics\visual-media.md | NEW

## Lessons
- 2026-11-23 | Check the season against the book before pulling: the handoff said Season 3 was Sea of Monsters, it is Titan's Curse (Sea of Monsters is S2), and the first TMDb id I tried was a different show; confirm title and show name on the page before downloading anything | evidence: Percy-Jackson-S3-E1-2-Picture-Pull.md, TMDb id 103540 vs 138501 | NEW
- 2026-11-23 | For a new streaming release go to the studio press kit first (press.disneyplus.com media-kits): captions name actor and episode, which gives sure tags when IMDb and TMDb S3 backdrops are blocked or missing; TMDb episode stills are the same shots, so check them against press by eye | evidence: 18 of 18 stills tagged from captions, 7 TMDb stills all twins | NEW
- 2026-11-23 | Copy long IDs from tool output with a script, never retype them; 5 of 44 retyped TMDb IDs 404ed | evidence: scratch percy-s3 fix.py run | NEW
- 2026-11-23 | When a title's own S3 gallery lacks a character, use the same actor and role from that title's earlier-season guest-star or character gallery on the studio press kit (captions name actor, role, episode), tag it SEASON 1, and say so in the flags; check every gallery link on the media-kit page, not just the episodic one | evidence: Percy-Jackson-S3-E1-2-Picture-Fit.md, 9 S1 stills filled Chiron, Clarisse, Mr. D, Hermes, Hades, Ares, Zeus, Poseidon, Luke | NEW
- 2026-11-23 | The transcript has stamps per speaker block, not per word: give IN and OUT as estimates from the phrase position inside the block, grep every search phrase for a count of 1, and pick phrases of 3 or more words to avoid hits like 'Hades good one' colliding | evidence: timeline-placements.md, 34 of 34 phrases counted once | NEW
- 2026-11-23 | Do not rm even scratch folders from Bash, the permission layer denied it twice on this job; log the leftover path in the report flags the same run | evidence: Fit report flag 6, wwd-director.md 2026-11-23 | REPEAT

## 2026-11-26
- Disney press site has many galleries beyond the kit links (S2 episodic, S2 character-sells, S1 guest-star); read the img alt text for captions. Original size = strip the ?region param. Wikipedia non-free posters are tiny (260 px): use TMDb image CDN original (needs the poster path from a WebFetch of the TMDb page) and iTunes Search API for book covers. Do NOT retry a 403 site with a spoofed browser header, the permission layer refuses it; list it as blocked.
- 2026-11-26 | If claude-in-chrome is not in the tool list, say so at once and stop the browser plan instead of pretending; the Disney S3 episodic page captions give actor names only (no character names), so the Atlas still must come from a TV Insider browser pull | evidence: PJ S3 follow-up, agent-runs.md 2026-11-26 | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
