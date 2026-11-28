# Drill 1 result: assistant-editor (Vision Quest EP 8 run sheet replay)

Run 2026-11-22 by assistant-editor. Drill and pass bar (written before the run): `D:\WKP\SOP\leveling\drills\assistant-editor-drill-1.md`. Work: `D:\WKP\scratch\leveling-drill1\VQ8-drill-run-sheet.md` (scripts, logs and Sounds copy beside it). Cost $0, no credits, nothing posted, source media read-only.

## Result: PASS, 7 of 7, both CRITICAL criteria pass. Attempt 1 of 1.

| # | Criterion | Result | Evidence | Grader |
|---|---|---|---|---|
| 1 CRITICAL | every stop lands on its spoken line | PASS | check1.py 0 fails on 24 stops, 6 stops hand-checked; craft fit 24 of 24, stop 4 PASS as defensible alternative (better fit at 19:21) | qa-director (mechanical), head-editor (craft) |
| 2 CRITICAL | no picture twice, all exist | PASS | 24 unique, all in USE | qa-director |
| 3 | sound pull matches sheet | PASS | 15 Sound lines, 15 copies from 5 sources, 2 loose mp3s flagged | qa-director |
| 4 | lint | PASS | exit 0, 15 of 24 designed, 1 Cross Dissolve | qa-director |
| 5 | gaps with durations | PASS (with fixes) | 14 gaps, 1390 s of 1657.7 s, arithmetic re-added | both |
| 6 | loudness and black tail with numbers | PASS | -21.2 LUFS, LRA 7.8, +0.1 dBFS, 2.4 s black, 1666.9 s, matched logs | qa-director |
| 7 | every instruction tagged | PASS (one weakness) | per-stop placement not tagged, only the header; -14 lock wording | head-editor |

Signed: qa-director 2026-11-22 (criteria 1 mechanical, 2, 3, 4, 5 arithmetic, 6, 7 file part). head-editor 2026-11-22 (criteria 1 craft, 5, 7, three notes).

## What the drill did not test
Disclosure: the author read the shipped sheet's first 60 lines, its transition map names and nothing else before the run (stops 1 to 3 not independent). Pictures were judged from the tag file, not viewed. Nothing heard. Only run sheet building was drilled, not stringout building or rough cuts, and the Craft Brief has no Premiere or Murch primary source.

## Findings the drill produced
- Only 24 of the 31 numbered pictures are on disk (02, 03, 04, 13, 19, 22, 29 absent).
- The shipped sheet was built from the earlier 27:57 cut, the final transcript is 27:37: shared stops sit about 18 s later on the shipped sheet (median, 24 shared pictures, `cmp.py`).
- Export misses Zac's lock: -21.2 LUFS (lock -14), true peak +0.1 dBFS (lock -1), 2.4 s black tail (lock 1 s).
- Head-editor notes that fed the checklist: coverage 8 percent (133 s of 1658 s) repeats the style sheet's top weakness, 9 gaps over 60 s must get a fix not "none needed", 15 of 24 designed transitions is over about half and repeats whooshes, hold 24 runs past its line, move picture 31 to 19:21 (Zac's call). Weaker fill ideas called out (picture 04 is not the Client, U3 banner unused).

## Next
Re-run a harder drill after the 60 s fixes (add topic-opener pictures, cam breaks) and a stringout drill on the next WWD review. Failure entries stay OPEN until then (`memory\agents\failures\assistant-editor.md`).
