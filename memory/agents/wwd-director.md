# Lessons: wwd-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\wwd-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Read D:\WKP\WWD\STANDARDS.md and the SOPs before a WWD job; STANDARDS still said 4 s clips after Zac changed the rule, and the job was rebuilt twice | evidence: logs\wwd-director.md 2026-11-19, feedback-clip-length.md | NEW
- 2026-11-19 | Never use the same picture twice in one video and never hold a picture over 7 s | evidence: WWD\CLAUDE.md lock 2026-10-19 | CONFIRMED
- 2026-11-19 | No on-screen actor name tags; write run-sheet notes in plain words | evidence: memory\feedback-no-actor-tags.md | NEW
- 2026-11-19 | Zero-question rule: the whole chain runs without Zac; only money and public posting go to him | evidence: root CLAUDE.md lock 2026-11-11, memory\feedback-own-the-operation.md | CONFIRMED
- 2026-11-19 | Shorts cadence: YouTube 1 a day incl Thursday 6 to 7 PM; FB and IG Thursday 1 at 6 PM, 4 to 5 a day Friday to Tuesday, Wednesday 2; 31-slot logic retired | evidence: memory\feedback-shorts-cadence.md | CONFIRMED
- 2026-11-19 | EP 120 Opus clips are approved; never re-ask or list a spot-check | evidence: memory\feedback-opus-clips-settled.md | CONFIRMED
- 2026-11-19 | Re-read wwd-frostcast-chapters SKILL.md before writing chapters, never from memory | evidence: memory\topics\wwd-skill-formats.md EP112 miss | NEW
- 2026-11-19 | Start a review at intake (pictures, music, kit, clip stock) so the post-transcript step takes under an hour | evidence: SOP-WWD-Review-Workflow, A Knight's Tale 2026-11-19 | NEW
- 2026-11-19 | Order the editing department's PREP stringout after the run sheet passes lint | evidence: SOP-Editing-Department 2026-11-19 | NEW

## Lessons

- 2026-11-20 (Zac correction): Zac's Wednesday 2026-11-18 command to send upload packages and Shorts to Google Drive (N:) was never written down, so nothing copied. Rule now in SOP-Output-Locations-and-Formats.md and LOCAL-PATHS.md. ON REQUEST ONLY (Zac 2026-11-20, not automatic): when Zac asks, mirror to N:\My Drive\01 Warrior King Productions\WWD\Upload Packages\<Movie>\ and verify the files open. When Zac gives a standing command, write it to the right file the same turn.
- 2026-11-21 | When the export is still rendering, build the package from the final transcript and stage the mp4 steps; a size-stable check is not enough, ffprobe can still say Permission denied because Premiere holds the file, so never copy or retry it | evidence: AKT package 2026-11-21, logs\wwd-director.md | NEW
- 2026-11-21 | Subagent copy files often carry hook lines not on the safe list ("skipped for 25 years"); list them in flags instead of silently trusting them, and check card and end-screen picks against the inventory date | evidence: A-Knights-Tale-Upload-Package.md flags 6 and 7 | NEW
- 2026-11-21 | Whisper word times are 0.2 to 0.4 s early and caption builds drop the first word at the in-point; always run check_clip on the finished head and add prepend_text (and drop_tail 1) before shipping, and set the in-point so the clip does not open on So/Yeah | evidence: AKT shorts 1 to 5, captions missed ONE/THEY/SHE/THIS/FOR | NEW
- 2026-11-21 | Do not caption a number the host stumbled on (AKT clip 2 said "95 and 1990 and 2005"): start the clip after the stumble instead | evidence: AKT clip 2 in-point 87.12 | NEW
- 2026-11-23 | A transcript can have 4 speaker labels when the handoff says 1; decide speakers from in-text evidence ("The King and I", "King") and say so; the .mp4 in the folder was the 48:25 raw, never time from it | evidence: Percy S3 chain 2026-11-23 | NEW
- 2026-11-23 | Do not write memory to the movie folder's .claude\agent-memory path named in the spec; it created an empty stray folder there. Use D:\WKP\memory\agents | evidence: Percey Jackson\Season 3\EP 1 and 2\.claude | NEW
- 2026-11-24 | When a tool (web page) cannot run, reproduce its stages with search agents but make them record the real publish date and URL per item; the first pass still had wrong details (Stewart death date, Hunger Games record, Rings renewal not new), so always send the numbers through fact-research before the PDF | evidence: Tuesday Intel 2026-11-24 stage3-factcheck.json | NEW
- 2026-11-25 | When EP has only two hosts, --num-speakers 3 still ran clean: the spurious third cluster only yields a few Guest/Unknown lines (map them to the nearest host); check that Gabby is absent by in-text mentions of the Oracle in third person | evidence: EP 122 transcript lines 729, 1083 | NEW
- 2026-11-25 | Heredocs with an apostrophe inside a long chained Bash command broke the shell; write long docs with the Write tool, then convert with md_to_docx.py | evidence: EP 122 audio cut first attempt failed | NEW
- 2026-11-26 | Opus project list is GET /api/clip-projects?q=mine (not /api/projects); score field is `score`, not viralityScore; check copy for clips whose text the brief file lacked (HP, small-screen Marvel copy was written blind and had a wrong "fight") | evidence: EP122 shorts plan | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
- 2026-11-27 | Before building a package check whether the folder's mp4 is the raw recording (ffprobe it): when Zac could not edit, the finished video is an Assembly in export\ (latest vN), so map transcript times to its plan file and audio-check each chapter with faster-whisper; a spot check also caught a leftover echo of a cut wrong claim, so whisper every cut join before trusting a cut list | evidence: Percy S3 package 2026-11-27, Assembly v8 | NEW
- 2026-11-27 | Build the package docx from a copy of the md with code-fence lines removed and "- " bullets inside paste blocks protected, then grep the docx XML for backticks; qa-director found 24 lone-backtick paragraphs in the first build | evidence: logs\qa\2026-11-27-percy-jackson-upload-package.md B1 | NEW
