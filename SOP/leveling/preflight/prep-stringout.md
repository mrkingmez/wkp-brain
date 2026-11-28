# Pre-flight: WWD prep stringout and assembly plan (silent, on black)

Created 2026-11-22. Paste into the hand-back with proof per item. Tags PROVEN, SOURCED or PROPOSED on every instruction.

1. [ ] Built from the LATEST transcript and run sheet. If the final transcript is newer than the sheet, the sheet owner (wwd-run-sheet) is told and the stringout is rebuilt, not patched. Header gives transcript end time and sheet date. (Gap 1)
2. [ ] Drift table in the plan: for 10 stops, search phrase, sheet time, transcript estimate, difference. Any difference over 5 s is called out (method error about 5 s, measured on A Knight's Tale 2026-11-22).
3. [ ] ffprobe on the render: codec H.264, 1920x1080, fps matches the sheet, no audio stream, duration equals the plan, frame count by `-count_frames` equals plan (S1 concat, S4 progressive).
4. [ ] Every segment built the same way before concat (same size, fps, pixel format) and padded so the frame count is exact (tpad, lesson 2026-11-20). Proof: frame count.
5. [ ] Each stop lands on its frame: QA by qa-media, AND each stop's Said phrase located in the transcript (not only against the sheet).
6. [ ] Black spans only between stops (blackdetect), no freezes inside clips (freezedetect).
7. [ ] Coverage stated: seconds of pictures plus clips over runtime, and every gap over 20 s listed with a PROPOSED fill or "none needed". (Gap 3)
8. [ ] Contain and fit, never crop. Vertical stills in 16:9: the plan says what fills the sides and the fill is checked on a frame pull for symmetry (Ian v5 lesson).
9. [ ] Files: render in `<movie folder>\prep\<Movie>-PREP-Stringout-vN.mp4` (never overwrite), plan .md in `WWD\reports\`. No Zac project file or source media touched.
10. [ ] Plan says plainly it is a prep aid Zac may ignore, and that nothing was heard or viewed beyond the listed frame pulls.
11. [ ] Zero em dashes. Ledger row and lesson written.
