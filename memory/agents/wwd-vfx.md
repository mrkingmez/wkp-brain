# Lessons: wwd-vfx

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\wwd-vfx.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Read D:\WKP\WWD\STANDARDS.md and the SOPs before a WWD job; STANDARDS still said 4 s clips after Zac changed the rule, and the job was rebuilt twice | evidence: logs\wwd-director.md 2026-11-19, feedback-clip-length.md | NEW
- 2026-11-19 | Never use the same picture twice in one video and never hold a picture over 7 s | evidence: WWD\CLAUDE.md lock 2026-10-19 | CONFIRMED
- 2026-11-19 | No on-screen actor name tags; write run-sheet notes in plain words | evidence: memory\feedback-no-actor-tags.md | NEW
- 2026-11-19 | Intro stings 6 s or less | evidence: memory\feedback-intro-length.md (Zac 2026-11-19) | NEW
- 2026-11-19 | Patriotic and military graphics always show the American flag | evidence: memory\feedback-always-include-flag.md | CONFIRMED
- 2026-11-19 | Check every show has its end card and Next Up card at intake; A Knight's Tale had neither when the run sheet was built | evidence: logs\wwd-director.md 2026-11-19 | NEW

## Lessons
- 2026-11-19 | When the hosts name no next title, build a generic Next Up beside the best guess and say how unsure the guess is; reuse make_arcade_kit.render and the VQ end card tile coordinates so end-screen slots stay identical | evidence: make_akt_cards.py, run sheet Still open 2 | NEW
- 2026-11-22 | For the joust sting, composite the real WWD logo onto a rectangular shield in Photoshop for the start frame, never use the logo on black; two shots (ride-in, strike) cut with the crack sound; describe the lance by its visible shape, not the word lance | evidence: firefly-prompt-guide\LESSONS.md F2 to F6, 5 joust clips viewed | NEW
- 2026-11-22 | Never name an unwanted object in a video prompt and never stack changes between retries; redesign after three misses | evidence: LESSONS.md F1, F18 | CONFIRMED
- 2026-11-22 | Read firefly-prompt-guide\QUICK-CARD.md section "Seen on Zac's clips" before any Veo prompt | evidence: QUICK-CARD.md 2026-11-22 | NEW
- 2026-11-22 | Leveling job: end cards get a zone and label overlap test and a frame pull before hand-back; the Vision Quest finale card shipped with the title on a zone label; Firefly maker pages return 403 to automated fetch so Firefly cost stays NOT KNOWN until read at the Generate button | evidence: memory\agents\briefs\wwd-vfx-gap-audit.md, failures\wwd-vfx.md, drill result PASS 6 of 7 (criterion 7 tags FAIL) | NEW
- 2026-11-22 | Tag every instruction PROVEN, SOURCED or PROPOSED in the run log, not only in the spec; the drill lost criterion 7 for untagged YouTube limits | evidence: SOP\leveling\drills\wwd-vfx-drill-1-result-2026-11-22.md | NEW
- 2026-11-22 | Joust sting redesign: two 4 s Veo shots (approach, strike) with start stills, real logo composited in Photoshop, cut on the crack, crack SFX added in Premiere, total 6 s or less. Cards in firefly-prompt-guide\REBUILT-PROMPTS-2026-11-22.md, none run | evidence: PROPOSED | NEW
- 2026-11-22 | Before any Veo, Kling or Seedance prompt: run prompt_lint.py, use STANDARD.md templates, write settings.txt from SETTINGS-TEMPLATE.txt, read the credit number at the Generate button, never estimate | evidence: STANDARD.md | NEW
- 2026-11-23 | New end card per show: new script (make_pj_end_card.py) with the zone and text touch test built in and printed before any render; build to scratch first, never rerun into P:\WWD Kit (script asserts no overwrite); constellation decoration must be checked against tile frames (first frame had dots touching tiles, fixed) | evidence: PJ S3 end card frames at 1, 6, 11.8 s viewed, touch test PASS | NEW
- 2026-11-23 | Model AKT end card .mov is ProRes 422 10-bit with no alpha (yuv422p10le); "alpha as the model" means opaque, say so in the hand-back | evidence: ffprobe of AKT and PJ .mov | CONFIRMED
- 2026-11-23 | For an "analyze Zac's intro" job, go to L:\...\Final\ first (published files) before scanning Raw Footage; the PJ intros were in Final all along, and Raw files had no intro | evidence: Final\Percy Jackson Ep 4 recap and review.mp4, coordinator correction | NEW
- 2026-11-23 | Code-built water needs a depth-weighted, thin-line caustic and a tone map; first passes looked like a pool wallpaper or northern lights. Impact flashes over a logo must stay under about 0.7 additive or the logo blows out | evidence: make_pj_intro_new.py frames 15, 58 to 76 | NEW
- 2026-11-23 | Never pipe rm -rf in a Bash call here, the permission system denies the whole command; use a new folder name | evidence: denied call 2026-11-23 | NEW
- 2026-11-24 | Before writing any Firefly or video-model prompt for a kit piece, intro or opener, read REFERENCE\PROMPTING-PLAYBOOK.md (kickoff checklist E, masters and bible B, nine-point start-frame check D3, log format F) then STANDARD.md; keep one change per run and log every try | evidence: REFERENCE\PROMPTING-PLAYBOOK.md, graphic-design order 2026-11-24 | NEW
- 2026-11-26 | Approved Firefly clips carry baked 2.4:1 letterbox bars (picture y140-940): put titles in the bottom bar and water edge and the logo bug on dark sky, never over the trident stem; Constantia digits are old-style, draw "3" in Cambria Bold at baseline anchor; check clip fps (Veo gave 24, kit wants 30) | evidence: make_pj_firefly_title.py, frames 3.9 to 7.9 s | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
