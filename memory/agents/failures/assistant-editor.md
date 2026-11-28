# Failure ledger: assistant-editor

Rules: `D:\WKP\SOP\SOP-Agent-Leveling.md` part 5. An entry stays OPEN until its Re-drill line is filled with a passed drill.

## 2026-11-19 | A Knight's Tale PREP stringout v1 | cost: NOT KNOWN (Zac time not recorded, no credits, rebuild not yet done)
- What happened: stringout and plan were timed to the first-cut transcript (ends 2197.9 s). Zac's final transcript ends 2189.9 s and his export is 2196.67 s. Measured 2026-11-22 (`D:\WKP\scratch\leveling-drill1\akt_delta.py`): median -7.0 s, range -9.0 to +5.7 s across 40 matched stops. Files: `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\prep\A-Knights-Tale-PREP-Stringout-v1.mp4`, plan `WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md`. Whether Zac used it: NOT KNOWN. Not a Zac-reported failure, found by this audit.
- What the maker's guidance said: no source found for transcript drift, searched: ffmpeg docs, EBU, ITU, YouTube help (none cover editing workflow). Source for the check method: none, PROPOSED.
- What we did instead: QA compared the render to the run sheet only (36 of 36 PASS), never to the spoken line or to a later cut.
- Root cause: skipped check, no step compared the transcript version to the final cut, and QA tested consistency not correctness.
- Fix: preflight `SOP\leveling\preflight\prep-stringout.md` items 1, 2 and 5; `edit-run-sheet.md` item 1.
- Re-drill: OPEN. Drill 1 covered run sheet building (passed mechanically, see result file). A stringout drill on the next WWD review is still owed.

## 2026-11-21 | Ian trailer v5 lopsided blur bars | cost: one more build (v6 queued) and a head-editor round, time NOT KNOWN
- What happened: v5 (`P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-D34-45s-16x9-v5-*`) put vertical stills on a blurred fill; TASKS.md and the gap list (line 56) record the bars as lopsided. Not re-viewed by me this job.
- What the maker's guidance said: ffmpeg docs (retrieved 2026-11-22, https://ffmpeg.org/ffmpeg-filters.html): "Enable decreasing or increasing output video width or height if necessary to keep the original aspect ratio." That gives contain and fit, nothing about fill symmetry.
- What we did instead: contain-fit with a blurred background, subject off centre on some stills, no frame pull of every still before delivery.
- Root cause: skipped checklist item (no frame check of each non-16:9 still for symmetry).
- Fix: `rough-cut-with-gap-list.md` item 4 and `prep-stringout.md` item 8.
- Re-drill: OPEN until v6 is built and a frame pull of every vertical still is checked.
