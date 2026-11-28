# Gap audit: head-editor

2026-11-22. Against `head-editor-craft-brief.md`. Only outputs on disk. Agent-proposed ratings are not final; the grader signs.

## Outputs audited
1. `D:\WKP\WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md`, head-editor notes section (lines 113 to 118), 2026-11-19.
2. `D:\WKP\Post-Production\reports\Zac-Style-Sheet-2026-11-19.md` (head-editor notes applied, QA PASS WITH NOTES), 2026-11-20.
3. Godzilla Minus Zero final `... All Hail the King! ed.mp4`: pre-post facts re-measured in drill 1 (`SOP\leveling\drills\head-editor-drill-1-result-2026-11-22.md`).
4. `D:\WKP\Post-Production\projects\ian-trailer\2026-11-20-head-editor-notes.md`: named in my lessons file, not re-read this run, so NOT audited.

## Findings

### A. A Knight's Tale prep notes (item 1)
- Departs: the notes do not state the loudness check or the intro-30-second check at all. Brief S1, S7 want the first 30 s treated as the measured Intro number. Cost: not known, no failure logged; the plan's own note says only stops 7, 28 and 42 were viewed, so 33 of 36 stops are "not viewed" and that is honestly stated.
- Departs: note 1 says "7 s cutaway" per gap but does not check against the 2 to 5 s guidance (S8) beside Zac's 7 s rule. Cost: low.
- Matches: gaps named with start time and length, an honest not-viewed line, creative calls marked as Zac's.
- Missing: no emotion or thought named per gap (Murch order, S4). The note ranks by length only.

### B. Zac Style Sheet (item 2)
- Departs: it says (Part 8 and in my lessons file 2026-11-20) a loudness target was thought missing while `WWD\STANDARDS.md` already locks -14 LUFS and -1 dBTP. Fixed in the sheet text now (Page 1 gap 2 states the standard), but the error ran through a draft. Cost: a QA note and rework, time NOT KNOWN.
- Departs: its Part 3 cites -14 as "your own WWD standard" and says Google publishes none. That matches S5 and S6 (retrieved today: "YouTube doesn't release exact values"). Good.
- Departs: Recipe 1 gives Premiere export clicks marked NOT VERIFIED. Adobe pages are still NOT RETRIEVED (403), so those stay PROPOSED. The sheet already says so.
- Departs: the 60-second rule is called "hard" in Part 4 item 6 but Part 8 says retention was not measured. YouTube's report (S1) only tells Zac where viewers dipped after he reads it. Cost: risk that Zac treats an untested rule as proven. Fix: label PROPOSED in the rule line.

### C. Godzilla Minus Zero final (item 3)
Re-measured 2026-11-22 (drill result): integrated -24.7 LUFS, true peak -2.4 dBFS (matches the sheet), black tail 10.5 s from 1723.07 s, silence 8.8 s at the end, same picture at about 25:36.7 and 26:15.0 (mid-frame correlation 1.000).
- A retrieved standard would have caught: the loudness miss (the -14 house number from STANDARDS.md vs -24.7 is 10.7 LU short; EBU's own -23 target with +/- 0.5 LU would also flag -24.7, which is 1.7 LU under it); the black tail (any blackdetect run); the repeated picture (any repeat check). No outside standard names black or repeat rules; those come from Zac's own rules and a script.
- What it cost: all three were found after the export, so each is a re-export for Zac, hours NOT KNOWN.
- New finding in the drill: a 0.5 s black at 12.9 to 13.4 s (inside the hook or opener, not viewed, could be an intentional flash).

## Ranked: the 3 gaps that cost the most
1. No measured loudness and ending check in the head-editor loop before post. Exports measured -20.5 to -24.7 LUFS (Style Sheet table, 8 of 8) and Godzilla ended on 10.5 s black, all found afterward. Fix: pre-flight `head-editor-final-export-check.md`, run on every export.
2. Stating a standard or target from memory instead of grepping `STANDARDS.md` first (the "no loudness target" error). Fix: lesson already in lessons file 2026-11-20, now a pre-flight item 3 and an OPEN failure entry.
3. Pacing rules presented as firm without a measured retention source, and no thought-per-gap reasoning (Murch order). Fix: tag PROPOSED; require Zac to read Studio retention (S1 report) before the rule is called standard.
