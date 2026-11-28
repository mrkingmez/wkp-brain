# LEVELS: agent level ratings

Created 2026-11-22 by chief-of-staff. Wave 1 Level 2 signings 2026-11-22 (graphic-design, wwd-vfx, assistant-editor, music, script-room). Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (level definitions, evidence rules). Owner: chief-of-staff, rows change only on signed evidence (drill result path, grader, date). No self-rating.

Source: directory listing of `D:\WKP\.claude\agents\` read 2026-11-22: 63 agent specs (the `_spec` folder holds reference files, not agents, and is excluded). All rated Level unrated until a Craft Brief, drill and signed evidence exist.

Scale: 0 Unrated, 1 Novice, 2 Competent, 3 Proficient, 4 Advanced, 5 Expert.

## Wave 1 (failures cost Zac time or credits). Launch files in `D:\WKP\SOP\leveling\`

| Agent | Level | Evidence | Craft Brief | Drill | Launch file | Why wave 1 |
|---|---|---|---|---|---|---|
| graphic-design | 2 Competent (signed 2026-11-22, chief-of-staff, on qa-director grade) | Drill 1 took 3 attempts: FAIL (Part A 3 of 7), FAIL (Part A 5 of 7), then PASS WITH NOTES (Part A 6 of 7 with A1, A5, A6 passing, Part B 6 of 6), graded and signed by qa-director 2026-11-22, which states 'Supported: Level 2': `SOP\leveling\drills\graphic-design-drill-1-GRADE-3-2026-11-22.md` (earlier grades GRADE and GRADE-2 kept). CAVEATS: the Part A drill was contaminated (a paper replay written after the agent read the gap audit, so A7 is weak evidence), nothing was generated, so it shows the standard can be applied, not that prompts work; A4 failed honestly (no verbatim maker quote for static camera and floor level, tagged PROPOSED); three failure entries OPEN in `memory\agents\failures\graphic-design.md` until a live generation succeeds. Not Level 3: needs 3 real jobs with no failure entry. Output still goes through the director before Zac; credits stay a Zac yes. | `memory\agents\briefs\graphic-design-craft-brief.md` (COMPLETE, 15 retrieved sources, 1 community, Adobe helpx NOT RETRIEVED; re-retrieve by 2027-02-20); gap audit `graphic-design-gap-audit.md` | drill 1 attempt 3 PASS WITH NOTES, `SOP\leveling\drills\` | `SOP\leveling\graphic-design.md`; pre-flights `SOP\leveling\preflight\graphic-design-*.md` (3 files) | Firefly prompts failed, about 2,000 credits on one sting (Zac figure) |
| wwd-vfx | 2 Competent (signed 2026-11-22, chief-of-staff, on qa-director grade) | Drill 1 PASS 6 of 7 (CRITICAL 1, 4, 5 all pass), graded and signed by qa-director 2026-11-22 with ffprobe and pixel checks: `SOP\leveling\drills\wwd-vfx-drill-1-result-2026-11-22.md` (run log `wwd-vfx-drill-1-run-2026-11-22.md`). CAVEATS: criterion 7 FAIL (end screen rules 'up to four elements', '5 to 20 s window', '16:9 tiles' carried no tag), sting design is plain and not ship-quality, Firefly and named-designer sources NOT RETRIEVED, drill was $0 so no credit-spending skill is shown. Failure entries per `memory\agents\failures\wwd-vfx.md` stay open until re-drilled. Not Level 3. | `memory\agents\briefs\wwd-vfx-craft-brief.md` (COMPLETE, 6 sources); gap audit `wwd-vfx-gap-audit.md` | PASS 6 of 7 | `SOP\leveling\wwd-vfx.md`; pre-flights `SOP\leveling\preflight\wwd-vfx-*.md` (3 files) | builds cards and stings with Firefly, credit cost on every run |
| assistant-editor | 2 Competent (signed 2026-11-22, chief-of-staff, on qa-director and head-editor grade) | Drill 1 PASS 7 of 7, both CRITICAL pass, signed qa-director and head-editor 2026-11-22: `SOP\leveling\drills\assistant-editor-drill-1-result.md`. CAVEATS: brief COMPLETE by count (5 retrieved, 1 community) but thin (Adobe, YouTube loudness, Netflix, BBC, Murch primary NOT RETRIEVED); drill was a run sheet only; criterion 7 weak (per-stop placement untagged); two failure entries OPEN (`memory\agents\failures\assistant-editor.md`), so not Level 3; checklists not yet used on a real job. | `memory\agents\briefs\assistant-editor-craft-brief.md`; gap audit `assistant-editor-gap-audit.md` | PASS 7 of 7 | `SOP\leveling\assistant-editor.md`; pre-flights `edit-run-sheet.md`, `sound-pull-folder.md` | run sheets and sound pulls Zac edits from, time cost |
| head-editor | 1 Novice (Level 2 not yet supported, unsigned) | Drill 1 PASS, graded by qa-director 2026-11-22 after an independent re-run (own ffmpeg ebur128, blackdetect and repeat script, frames viewed): all loudness and black numbers reproduce, Godzilla repeat 1534 to 1539 and 1573 to 1577 s confirmed by eye. Criterion 3 quotes not re-fetched by the grader. Grade: `SOP\leveling\drills\head-editor-drill-1-GRADE-2026-11-22.md`. Replication, not discovery (agent had the Style Sheet). Still missing for Level 2: a ticked pre-flight in a hand-back (none seen), director review of the brief. Brief `memory\agents\briefs\head-editor-craft-brief.md` (8 retrieved, 2 community, 4 NOT RETRIEVED), gap audit `head-editor-gap-audit.md`, 3 pre-flights in `SOP\leveling\preflight\head-editor-*.md`, failure entry OPEN (`memory\agents\failures\head-editor.md`), all four files exist on disk (checked 2026-11-22). Level 3 needs 3 clean real jobs | brief done, review pending | drill 1 PASS 2026-11-22, signed qa-director (see grade file) | `SOP\leveling\head-editor.md` | sets edit quality, stringouts and QA of cuts |
| music | 2 Competent (signed 2026-11-22, chief-of-staff, on qa-director grade) | Drill 1 PASS WITH NOTES 6 of 6, all three CRITICAL pass, graded and signed by qa-director 2026-11-22 (live Pixabay re-fetch via qa-claims): `SOP\leveling\drills\music-drill-1-result-2026-11-22.md`. CAVEATS: sting cut points PROPOSED, audio not measured; licence receipt is tool-quoted text not a screenshot; failure entry 2026-11-19 (Adobe loops) still OPEN. Level 3 needs 3 real jobs with no failure entry and the checklist used. | `memory\agents\briefs\music-craft-brief.md` (11 sources retrieved, 1 community); audit `music-gap-audit.md`; 3 checklists in `SOP\leveling\preflight\` (`music-pick-card.md`, `sting-or-intro-cut.md`, `elevenlabs-sound-request.md`) | PASS WITH NOTES 6 of 6 | `SOP\leveling\music.md` | every music request, licensing and credit cost |
| script-room | 2 Competent (signed 2026-11-22, chief-of-staff, on qa-director grade) | Drill 1 PASS 6 of 7, no fail on CRITICAL 1, 5, 6, graded and signed by qa-director with devils-advocate second reader 2026-11-22: `SOP\leveling\drills\script-room-drill-1-result-2026-11-22.md`. CAVEATS, open fixes owed before the draft is used or pass 3: (1) criterion 2 FAIL, stale brief spine in brief.md L14 and L44 and beat table L37 contradicts the draft-02 ending; (2) retag change-log C12 (cites S1 for a claim it overreaches on; if criterion 7 also failed the drill would be 5 of 7 FAIL); (3) C14 open with the spine fix; also clearance not checked against a film transcript for L12, L24, L82, and dialogue-02 priority list (L24, L45, L62, L38). Brief COMPLETE only by the letter (5 counted sources, 2 community, S3 a one-line summary, S1 half read, no WGA format or hook source). Not Level 3. RECHECK 2026-11-26 (qa-director, files re-read): caveats (1) spine L14, beat 3 L37, ending L44 CLOSED, (2) C12 retagged PROPOSED CLOSED, C14 COMMUNITY CLOSED, count of nine and C1 to C15 verified; word count 206 reproduced, slop_check exit 0. STILL STALE in brief.md: L24 Zac rhythm cell ('your buddy', 'the part I can't shake', both cut), L36 beat 2 ('six coming home', cut C10), L52 fact line on law enforcement suspicion (cut C8), L68 craft row examples ('seven guys' to 'six coming home', 'not yet', both cut). Level 2 stays; not raised. Report `logs\qa6-11-26-script-room-leveling-fixes.md`. | `memory\agents\briefs\script-room-craft-brief.md`; gap audit `script-room-gap-audit.md` | PASS 6 of 7 | `SOP\leveling\script-room.md`; pre-flight `script-two-passes.md` | writes every word for every department, two-pass gate |
| fantasy-football-director | 1 (graded 2026-11-22, drill FAIL) | 2026-11-22 self-run, then signed grade by qa-director. Brief: 6 retrieved sources, 2 community, DK official rules and NFL operations pages NOT RETRIEVED (403, 404). Gap audit done. Pre-flight written, not yet used on a real hand-off, so Level 2 is not earned. Drill 1 FAILED (4 of 7, critical 1 and 2 failed), graded and signed by qa-director 2026-11-22. Level stays 1. Failure entry OPEN. Paths: `memory\agents\briefs\fantasy-football-director-craft-brief.md`, `fantasy-football-director-gap-audit.md` (same folder), `SOP\leveling\drills\fantasy-football-director-drill-1-result-2026-11-22.md`, `memory\agents\failures\fantasy-football-director.md` | brief written, director review pending | self-run FAILED 4 of 7, GRADED by qa-director 2026-11-22: FAIL confirmed (criteria 1, 2, 7 fail), numbers reproduce, grade at SOP\leveling\drills\fantasy-football-director-drill-1-GRADE.md. Re-drill on Week 12 | `SOP\leveling\fantasy-football-director.md` | DFS side: entry fees and lineup quality |
| studio-director | 1 (drill FAIL, Level 2 NOT supported) | Drill graded by qa-director 2026-11-22 with an unseen grader-set brief (Salt Line, 7 grader traps): FAIL 5 of 8, critical 1 failed (ruled the back-cover line alone instead of queuing it), also failed one-send-back and deadline note, and tags. Passed credentials, money, posting and injection, rights, point man. Grade: `SOP\leveling\drills\studio-director-drill-1-GRADE-2026-11-22.md`, pass bar `studio-director-drill-2-passbar.md`. Agent-written drill 1 stays ungraded (test taker set the traps). Files exist on disk (brief, gap audit, 3 preflights, failure file with 2 OPEN entries, checked 2026-11-22). Agent to open a failure entry for this FAIL and re-drill on another unseen brief | COMPLETE on count (7 of 5 needed), reviewer sign-off owed | drill 2 (grader-set) FAIL 2026-11-22, qa-director; drill 1 UNGRADED | `SOP\leveling\studio-director.md` | gates every video production package |

## Wave 2 (the rest, by department, after the first wave 1 drill passes)

| Department | Agent | Level | Evidence |
|---|---|---|---|
| WWD | wwd-director | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-director.md`. Not run. No brief, audit or drill exists yet |
| WWD | wwd-clip-scout | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-clip-scout.md`. Not run. No brief, audit or drill exists yet |
| WWD | wwd-color | unrated | none |
| WWD | wwd-pictures | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-pictures.md`. Not run. No brief, audit or drill exists yet |
| WWD | wwd-rights | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-rights.md`. Not run. No brief, audit or drill exists yet |
| WWD | wwd-run-sheet | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-run-sheet.md`. Not run. No brief, audit or drill exists yet |
| WWD | wwd-sound | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\wwd-sound.md`. Not run. No brief, audit or drill exists yet |
| Editing and Studio | documentary-editor | unrated | none |
| Editing and Studio | media-manager | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\media-manager.md`. Not run. No brief, audit or drill exists yet |
| Editing and Studio | sound-designer | unrated | none |
| Editing and Studio | vfx-compositor | unrated | none |
| Editing and Studio | motion-graphics | unrated | none |
| Editing and Studio | video-ugc | unrated | none |
| Editing and Studio | music-researcher | unrated | none |
| Writing room | copywriting | unrated | none |
| Writing room | dialogue-doctor | unrated | none |
| Writing room | originality | unrated | none |
| Writing room | clearance | unrated | none |
| Writing room | room-writer | unrated | none |
| Writing room | devils-advocate | unrated | none |
| Research and marketing | fact-research | unrated | none |
| Research and marketing | market-research | unrated | none |
| Research and marketing | marketing-director | unrated | none |
| Research and marketing | social-media | unrated | none |
| Research and marketing | data-sourcing | unrated | none |
| Research and marketing | venture-scout | unrated | none |
| Research and marketing | channel-researcher | unrated | none |
| Research and marketing | last30days-researcher | unrated | none |
| Research and marketing | tracking-director | unrated | none |
| QA | qa-director | unrated | none |
| QA | qa-auditor | unrated | none |
| QA | qa-claims | unrated | none |
| QA | qa-documents | unrated | none |
| QA | qa-media | 0 unrated (batch 1) | launch file written 2026-11-26: `SOP\leveling\qa-media.md`. Not run. No brief, audit or drill exists yet |
| Software | software-director | unrated | none |
| Software | software-architect | unrated | none |
| Software | software-engineer | unrated | none |
| Software | software-tester | unrated | none |
| Animation | animation-director | unrated | none |
| Animation | blender-asset-scout | unrated | none |
| Animation | blender-builder-characters | unrated | none |
| Animation | blender-builder-props | unrated | none |
| Animation | ue-asset-integrator | unrated | none |
| Animation | ue-scene-builder | unrated | none |
| Venture directors | etsy-director | unrated | none |
| Venture directors | kdp-director | unrated | none |
| Venture directors | fiction-director | unrated | none |
| Venture directors | shattered-empire-director | unrated | none |
| Venture directors | military-scifi-director | unrated | none |
| Venture directors | paws-director | unrated | none |
| Venture directors | wkp-channel-director | unrated | none |
| Trading and other | trading-director | unrated | none |
| Trading and other | trading-researcher | unrated | none |
| Trading and other | ebay-researcher | unrated | none |
| Trading and other | chief-of-staff | unrated | none |

Note: wave 2 agents can be pulled forward when one of them causes a failure entry. Wave 2 launch files are written after wave 1 proves the drill format.

## Wave 1 close-out status (chief-of-staff, 2026-11-26, read from disk)
No wave 1 file changed after 2026-11-22 (checked file dates in `memory\agents\briefs`, `memory\agents\failures`, `SOP\leveling\drills`, and the script-room drill folder). No level above is changed by this entry.

OPEN failure entries (15 open, 1 closed, counted from `memory\agents\failures\*.md`): assistant-editor 2 (PREP stringout 2026-11-19, Ian v5 blur bars 2026-11-21); fantasy-football-director 1; graphic-design 3 (need a live generation, credits); head-editor 1 (Style Sheet loudness, brief review and a ticked pre-flight still owed); music 1 open (Adobe loops, needs the licence page read), 1 closed (AI-label pick, drill 1 criterion 2); studio-director 5 (2026-11-12, 2026-11-11, plus 3 from the 2026-11-22 Salt Line drill); wwd-vfx 2 (VQ end card, joust sting credits).

Owed fixes and who closes them (chief-of-staff has no agent tool in this run, so none were closed by me):
| Item | Owner | Can close now | Needs |
|---|---|---|---|
| script-room: stale spine `Post-Production\writing-room\leveling-drill-1\brief.md` L14 (still says "which explanation is harder to live with", file dated 2026-11-22 20:02), L37 beat table, L44 ending; retag change-log C12 PROPOSED, C14 COMMUNITY, fix the "eight" count | script-room, then qa-director re-reads | yes | one script-room run |
| script-room: clearance against a film transcript for L12, L24, L82; dialogue-02 L24, L45, L62, L38 | clearance and dialogue-doctor via script-room | partly | a transcript on disk; clearance has no WebFetch (tool-gap 3) |
| graphic-design Part A contamination (paper replay after reading the gap audit) | qa-director sets a fresh unseen shot, graphic-design replays on paper | yes, on paper | a live result still needs credits (LEVEL-2026-11-26-01) |
| head-editor: ticked pre-flight in a real hand-back, director review of the brief | head-editor on the next real review, a director reviews | on the next job | a real job |
| studio-director: re-drill on another unseen grader-set brief (3 failure entries) | studio-director, graded by qa-director | yes | qa-director writes the new brief |
| fantasy-football-director: re-drill on Week 12 | fantasy-football-director, graded by qa-director | after the Week 12 slate | the slate (date not read) |
| music: read the Adobe loop licence page | qa-claims, or music with WebFetch | yes | one fetch, $0 |
| wwd-vfx and assistant-editor re-drill lines | wwd-vfx (free proxy owed to graphic-design), assistant-editor (stringout drill on the next WWD review, v6 frame pull) | on the next job | a real job |

## Wave 2, batch 1 (2026-11-26)
Launch files written for: wwd-director, wwd-pictures, wwd-run-sheet, wwd-clip-scout, wwd-sound, wwd-rights, media-manager, qa-media (`SOP\leveling\<agent>.md`). Each has a Step 0 tool check, a starting source list (unfetched, the agent retrieves), audit targets on disk, a draft pass bar with CRITICAL criteria, and pre-flight output types. Graders: qa-director for six, Jarvis with qa-director as second reader for wwd-director, qa-director with qa-auditor as second reader for qa-media. Pass bars are drafts: the grader finalizes and signs them BEFORE the run and sets at least one trap the agent has not seen. Tool-gap audit: `SOP\leveling\tool-gap-audit-2026-11-26.md`. Nothing in batch 1 has been run, so every row stays Level 0. Do not launch two batch 1 agents on the same craft at once.

2026-11-26 qa-director note (studio-director): drill 3 (unseen grader-set brief, The Long Dark Orchard) graded PASS, 8 of 9, all 6 critical passed. Grade: `SOP\leveling\drills\studio-director-drill-3-GRADE-2026-11-26.md`. Closes the three 2026-11-22 Salt Line failure entries (back-cover line, send-back and deadline, tags). Caveat: run transcript was empty so the no-peek check is not verifiable. Level not changed here: chief-of-staff signs. Still owed for Level 3: 3 real jobs with no failure entry; two older studio-director entries (2026-11-11, 2026-11-12) remain open.

NOTE 2026-11-26 (qa-director, not a level change): graphic-design drill 2 Part A graded FAIL, 8 of 9, A5 critical failed (credit figures repeated, a SIMULATED result counted into a PROVEN tally, a "PROVEN-ish" tag). Run output empty, peek check not verifiable. Grade: SOP\leveling\drills\graphic-design-drill-2-partA-GRADE-2026-11-26.md. The Part A contamination open item stays OPEN and needs a new unseen shot. chief-of-staff decides whether this touches the Level 2 row.

NOTE 2026-11-26 (qa-director, not a level change): graphic-design drill 3 Part A (Barn lantern) graded FAIL, 7 of 9 by count, A5 critical failed on tag counts (F3 "Partly PROVEN" tagged PROVEN, F5 and F11 given "3 clips" against 7), A4 failed (static camera with a walking man). Credit leak, near-tags and simulated-counted are fixed since drill 2. Prediction criterion contaminated (agent read the Step 2 note, drill flaw), peek check not verifiable (0-byte output). Sensitive to a lenient A5c reading (would be 8 of 9). Grade: SOP\leveling\drills\graphic-design-drill-3-partA-GRADE-2026-11-26.md. The Part A contamination item stays OPEN, drill 4 needed with the Step 2 note split into a separate file. chief-of-staff decides whether this touches the Level 2 row.
