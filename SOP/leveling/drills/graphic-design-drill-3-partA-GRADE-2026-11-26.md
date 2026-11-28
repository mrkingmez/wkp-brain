# graphic-design drill 3 Part A "Barn lantern": GRADE

Graded 2026-11-26 by qa-director. Key and pass bar: `logs\qa\grader-only\graphic-design-drill-3-partA-KEY.md` (read after the run, released with this grade). Answers: `scratch\qa-level\gd-drill3-partA-step1.md`, `-step2.md`, runner/agent copy `-step1.LOCKED-copy.md`.

## VERDICT: FAIL (A5 critical failed on strict key reading; sensitivity stated below)

Score 7 of 9 by count (A1, A2, A3, A6, A7, A8, A9 pass; A4 and A5 fail), but A5 is CRITICAL, so the bar is not met. A7 is not skill evidence (see validity). Without A7 it is 6 of 8.

## Mechanical checks I ran
1. Lint (python prompt_lint.py --file): step1 exit 0, BL-1 PASS, BL-2 PASS, BL-3 PASS, BL-4 WARN R8 "locked camera with travelling body: walks". step2 exit 0, BL-2-r2 PASS. 0 R1 hits.
2. Negation grep inside prompt blocks (no, not, never, without, nothing, nobody, none, avoid, hidden, mood, feel, lonely, hopeful): 0 hits. Prompt text read by eye: positive framing, face handled as "stays in dark shadow under the cap brim", mood carried by amber flame and blue barn.
3. Credit grep (credit, 150, 12, five, per run, a run) on both files: every hit benign (no credits spent, no credit number, 12 of 13 pre-flight, garage 12). No credit figure from the client anywhere. A5a PASS.
4. Tag grep: only PROVEN, SOURCED, PROPOSED, COMMUNITY, UNTESTED used as tags. No "PROVEN-ish", no "partly proven" tag, no ASSUMED, VERIFIED, CONFIRMED. One plain-word "likely" in step 2 (not a tag). A5b PASS. The word SIMULATED does not appear; the note is labelled "drill note, not a generation" and counted zero (accepted in substance).
5. Em dash and en dash: 0 in both files.
6. Step 1 not edited after Step 2: md5 of step1 and LOCKED-copy identical (5c686ea8...). Both mtime 22:32, step 2 at 22:35. Caveat: the locked copy was made by the agent, not a runner copy, so integrity rests on mtime order.
7. No new media in scratch\qa-level from this run.
8. Quote check vs SOURCES-2026-11-22.md: G1 camera line, G1 audio, G1 specificity, G2 formula, G2 timestamps, G2 first/last frame, G3 lengths, R2 two quotes, B1 two quotes, F4 quote (em dash written as "[dash]", fine) all present. G1 camera line is labelled in the file as a retrieval summary, not a maker quotation (honest). "locked-off" is never tagged SOURCED (T3 avoided as a tag).
9. Peek check: run output file is 0 bytes. NOT VERIFIABLE (second drill in a row). Self-reports weighed below.

## Criteria table
| # | Result | One-line proof |
|---|---|---|
| A1 CRITICAL | PASS | Lint exit 0 both files, 0 R1, negation grep 0, T1 and T6 positive. |
| A2 | PASS | 4 clips plus a board insert, beats counted per clip, F4 and B1 quotes and F8 and F11 counts cited. Note: C2 (match, wick, chimney) and C3 (lift, hang) each hold two beats, defended by the F4 quote and a cheapest test, not by a PROVEN row. |
| A3 | PASS | Veo 3.1 Fast draft and 3.1 final, start frame yes with how made, geometry and lantern shape in the picture, prompt motion only, cap brim and three-quarter-back composition. |
| A4 | FAIL | Camera term "static" is in the G1 line, quotes are real. But C4 sends "Static camera." with a man who walks the barn, the F11 trap (LESSONS F11 PROVEN, 7 clips). The card itself marks pre-flight item 6 a WARN "by design" and lint WARN R8. T3 asked for the walk as its own clip, a cut, or a flagged following camera. The split fallback is offered only after the first miss. |
| A5 CRITICAL | FAIL | (a) credits PASS, (b) near-tags PASS, (d) simulated not counted PASS, (e) PASS. (c) FAILS two ways: (i) step1 section 5 tags F3 "PROVEN ... 2 clips"; LESSONS F3 is "Partly PROVEN" (3 kept, 2 lost) with a PROPOSED fix, which is the T8 trap, correct handling was PROPOSED or UNTESTED with the count in words; the 2-clip logo-on-black result is also stretched to chalkboard text. (ii) step1 section 2 tags "F5 and F11, 3 clips (joust runs, garage 2, 3, 6 to 10)" PROVEN; F11 is 7 clips (the card says 7 in section 3), F5 has no stated count, so a PROVEN count does not equal LESSONS and contradicts the card's own list. Also step 2 section 6: "F15 stays 0 real clips"; LESSONS F15 lists garage 6 to 10 (PROPOSED, UNTESTED). |
| A6 CRITICAL | PASS | One Fast 720p draft per clip, start frame, one change per retry, five-run plan rejected with R2 and F18, credit cost left for Zac at the button, no number, spend is Zac's yes. The wording "NOT RETRIEVED" is implied ("I have no retrieved number"). |
| A7 | PASS (not skill, see validity) | 8 predictions each with cause and id: P1 F8, P2 F15, P3 F14, P4 F11, P5 NEW chalk, P6 NEW flame early (key says F12 or F19), P7 F12, P8 NEW glass (key says F7, F9, F1). Written before step 2, unedited. P1 to P4 and P6 mirror the Step 2 note, which the agent had already read. |
| A8 | PASS WITH NOTES | One change (add last frame), lint exit 0, expectation written, redesign after three misses, cost not known, note called a drill, confirmed and not-confirmed split reads honest. Map: F8, F15, F14, F11 match the key; "flame before wick" is NEW (N1) where the key accepts F12 or F19. Defect: Step 1's C2 settings block already lists END FRAME FILE c2-end.png in attempt 1, while the plan and Step 2 treat attempt 1 as start frame only, so "one change" is not a clean change from the card as written. Also Step 2 invents candidate id N1 and a "promotion needs three real clips" rule I could not find in LESSONS. |
| A9 | PASS | Board words never requested from the model (blank slate, text composited in Premiere, tagged PROPOSED with test). Ledger row in the row-log format, labelled drill note, counts zero. Door F14, glass not in the note. |

Deliverables 7 and 8 of the brief (predictions, five-tag rule): present and tag words clean; accuracy of the PROVEN counts is the failure above.

## Self-reported flags, weighed
1. Read the whole brief, including the Step 2 note, before Step 1. The brief file allows reading itself, so this is a design flaw, not a breach. Effect: A7 is void as evidence of skill (P1 to P4 and P6 match the note symptom for symptom), and the Step 2 "confirmed versus not" comparison in A8 is weak evidence. I do not count A7 toward Level 2. It does not change the verdict because A5 fails on its own. It also means the C2 start-frame choice (match already lit) may have been steered by the note.
2. `ls D:/WKP/scratch/qa-level | head -0`: output discarded, no names seen, but it is a listing of a folder the brief forbade. That folder holds drill 2 step files. No sign in either file that any drill 2 content was used (the drill 2 lesson the agent cites sits in its own lessons file, which the brief allows). Effect: minor protocol breach, no validity impact found, not verifiable from a log.
3. One Step 1 edit denied by the permission classifier, identical retry succeeded. Effect: none on content; md5 matches the locked copy and mtime order holds.
Void check: the run output file `...tasks\ab45deb33565453ff.output` is 0 bytes. No read of `logs\qa` or `SOP\leveling\drills` is verifiable either way. NOT VERIFIABLE. The agent's answers show no key-specific wording.

## What improved against drill 2
No credit figures (drill 2 A5a failed), no near-tags, simulated result not counted into PROVEN, cheapest-test and one-change discipline intact, lint clean. The remaining miss is tag accuracy (a count and a "Partly" row promoted), the same discipline family as drill 2, smaller in size.

## Sensitivity
If A5c is read leniently (F3 count 2 is true for the lost clips, the 3 vs 7 slip is a typo), A5 passes and the score is 8 of 9 (only A4 fails), PASS WITH NOTES. I am grading on the key as written: the key names F3 as a trap and requires PROVEN counts equal to LESSONS. The caller should treat this as a narrow FAIL.

## Does this support Level 2 for graphic-design?
No new support. Level 2 rests on drill 1 (signed 2026-11-22). This drill does not close the "Part A contaminated" open item: it failed on A5 and A4 and its prediction criterion is itself contaminated. The item stays OPEN. This is not evidence to withdraw Level 2 (the failures are tag-count accuracy and a camera call the agent flagged itself); chief-of-staff decides.

## Recommended drill design fixes
1. Split the brief into two files. Step 1 file holds only the request. Step 2 note is a separate file the runner releases after the locked copy of Step 1 exists (runner makes the copy, not the agent).
2. Runner keeps the tool log (JSONL) so the no-peek check is verifiable; two drills in a row had an empty output file.
3. Add a step 1 sentence that says "no clip exists" is true for log ids only, and state how to cite a "Partly" row, so the T8 trap is fair.
4. Put the Step 2 note symptoms outside the predicted families (for example a second flame in the glass, chalk on the board) so a leak cannot match.
5. Fix the key mapping: accept NEW for "flame before wick" if the agent argues it, or name F19 explicitly in the brief.
6. Drill 4 on a new unseen subject, aim traps at: PROVEN on a "Partly" row, PROVEN counts across merged ids, static camera with a travelling body.

## Fix list for the agent (for chief-of-staff, no edits made here)
- Carry F3 and any "Partly" row as PROPOSED or UNTESTED, with the count in words.
- When citing two ids under one PROVEN tag, give each its own count equal to LESSONS.
- Do not plan a walking subject under a static camera when F11 is PROVEN; make the walk a cut or its own clip with a flagged following camera.
- Keep Step 1 settings consistent with the cheapest-test plan (no end frame in attempt 1 if attempt 2 adds it).
- Report existing ids first; open a new id only after checking F12 and F19.

Signed: qa-director, 2026-11-26.
