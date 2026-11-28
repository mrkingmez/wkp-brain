# Failure entries: wwd-vfx

Format per `SOP\SOP-Agent-Leveling.md` part 5. Entries stay OPEN until the Re-drill line is filled with a passed drill.

## 2026-11-22 | Vision Quest finale end card (P:\WWD Kit\Cards\End Card - Vision Quest Finale (MP4).mp4, made 2026-11-15) | cost: NOT KNOWN (found by audit, Zac has not reported it; possible rebuild and re-export if the card is in his EP 8 edit)
- What happened: frames at 6 s and 9 s show the "THANKS FOR WATCHING" line (y about 310 to 390) sitting on the "BEST FOR YOU" zone label and touching the "LATEST UPLOAD" label row. Frames: D:\WKP\scratch\wwd-vfx-level\frames\vq_end_6s.png and vq_9.png.
- What the maker's guidance said: "End screen elements will show at the same time by default." (https://support.google.com/youtube/answer/6388789, retrieved 2026-11-22). Elements land on the zones, so zones and their labels must be clear. No maker page states a label rule, so the no-text-over-a-zone rule is house, PROPOSED.
- What we did instead: placed the title at a fixed y with no overlap test; no frame was checked against the zone boxes.
- Root cause: skipped checklist item (no zone and label overlap test existed).
- Fix: End card pre-flight item 5, overlap test printed by `make_vfx_drill1.py`. Rebuild of the VQ card is offered, not done (no kit piece Zac used is overwritten, a v2 would sit beside it).
- Re-drill: wwd-vfx-drill-1, 2026-11-22, PASS 6 of 7 (graded by qa-director, `SOP\leveling\drills\wwd-vfx-drill-1-result-2026-11-22.md`). Closed for the layout cause only if the director accepts a free-build drill as the re-drill; the VQ card itself is still unfixed, so left OPEN.

## 2026-11-22 | Joust logo sting Firefly runs (data\firefly-prompt-log\, shared with graphic-design) | cost: about 2,000 credits, Zac's figure, NOT retrieved from the account; 5 joust clips on disk
- What happened: repeated rerolls; named unwanted things were drawn (spear), a logo on black was redrawn, left and right placement ignored. Ledger F1 to F6 in `data\firefly-prompt-guide\LESSONS.md`. No settings.txt on any of 18 clips.
- What the maker's guidance said: no retrieved Adobe or Google page (Adobe helpx 403, see the craft brief). Local ledger cites a Google "avoid no and don't" line tagged MAKER S1, which I did not retrieve today.
- What we did instead: ran full-length generations without a cheapest-model test and without tagged instructions.
- Root cause: gap in knowledge plus skipped checklist (no test-first step, no maker source).
- Fix: sting pre-flight items 5 to 9, brief section 3. Re-run of a Firefly drill needs credits, so it is NOT RUN.
- Re-drill: NOT RUN (credits). Stays OPEN. A free proxy would be replaying a logged clip's prompt rewrite against its frames, owed to graphic-design's drill.
