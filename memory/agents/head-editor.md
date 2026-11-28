# Lessons: head-editor

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\head-editor.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Spend no credits: Veo and Firefly credits are at zero, work from what is on disk | evidence: memory\project-ian-trailer-settled.md | NEW
- 2026-11-19 | Nobody can hear audio: say 'not heard' for every sound claim | evidence: agent-runs.md rows 2026-11-17 and 2026-11-18 | NEW
- 2026-11-19 | On the A Knight's Tale prep, pictures plus clips covered 9.6 percent of runtime with 22 gaps over 20 s; check coverage on every WWD prep | evidence: WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md 2026-11-19 | NEW

## Lessons
- 2026-11-19 | WWD is in scope: wwd-director orders a WWD PRACTICE AND PREP job on every review (stringout plus assembly plan from assistant-editor, top 3 notes from head-editor); Zac still makes the cut, so never say WWD is not yours | evidence: Zac asked 2026-11-19 whether the editors help WWD and can practice on it (reports\2026-11-19-System-Reset-Report.md section 1), SOP\SOP-Editing-Department.md, SOP\SOP-WWD-Review-Workflow.md step 5 | CONFIRMED
- 2026-11-20 | Before calling any number a gap or a missing target, grep WWD\STANDARDS.md and the wwd-sound spec first: the style sheet said loudness had no set target while STANDARDS.md already locks -14 LUFS and -1 dBTP; also test any measuring method for blindness (silencedetect at -45 dB cannot see pauses filled with room tone) before praising what it found | evidence: Post-Production\reports\Zac-Style-Sheet-2026-11-19.md notes pass, WWD\STANDARDS.md line 48 | NEW
- 2026-11-20 | Measure Zac's WWD cuts by correlating 2 fps 64x36 grey frames to the video's median frame (the StreamYard two-shot): under 0.6 = cutaway; it caught pictures, cams and cards that the scene-cut detector missed under dissolves, and it showed the real gap is long static two-shot stretches (3 to 11 over 60 s per review), not hold length | evidence: Post-Production\research\editing-study\2026-11-19-zac-work-measurements.md, scratch\editor-study\measure.py | NEW
- 2026-11-22 | Before any loudness or ending claim, run the printed ffmpeg ebur128, blackdetect and repeat commands and compare to STANDARDS.md; Adobe help and Netflix pages are blocked here (403 or empty shell), so never state their numbers or menu steps as sourced, and label YouTube's -14 as third party (Frame.io: "YouTube doesn’t release exact values"); a drill that replicates a known sheet is weaker than a blind one, say so | evidence: SOP\leveling\drills\head-editor-drill-1-result-2026-11-22.md, memory\agents\briefs\head-editor-craft-brief.md, memory\agents\failures\head-editor.md | NEW
- 2026-11-20 | On a rough with placeholders, rule on pattern and treatment only, and when a grade sits on a full-frame adjustment layer check that it will not lift the black pillarbox bars (limit it with Crop or grade per clip); fade the layer in with the dissolve | evidence: Post-Production\projects\ian-trailer\2026-11-20-head-editor-notes.md notes 7 and A | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
