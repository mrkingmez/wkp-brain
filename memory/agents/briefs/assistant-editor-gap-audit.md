# Gap audit: assistant-editor

Written 2026-11-22 by assistant-editor. Against `memory\agents\briefs\assistant-editor-craft-brief.md` (S1 ffmpeg docs, S2 EBU R 128, S3 ITU-R BS.1770, S4 YouTube upload settings, S5 Murch via Wikipedia). Only outputs that exist on disk are audited, paths named. Measured numbers come from scripts run 2026-11-22 (listed). Nothing here was heard.

## Outputs audited

### A. A Knight's Tale PREP stringout v1 and plan (job 2026-11-19)
Files: `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\prep\A-Knights-Tale-PREP-Stringout-v1.mp4` (65,554,765 bytes), plan `D:\WKP\WWD\reports\A-Knights-Tale-Prep-Assembly-Plan.md`, QA `D:\WKP\WWD\reports\A-Knights-Tale-Stringout-QA-2026-11-19.md`, run sheet `...\A-Knights-Tale-Edit-Run-Sheet.md`. Zac's final export now exists: `...\A knights Tale A one for the ages.mp4`, 2196.67 s by ffprobe. Final transcript `A knights Tale final.txt` ends 2189.93 s, the first-cut transcript the sheet was built from ends 2197.93 s.

Measured by `D:\WKP\scratch\leveling-drill1\akt_delta.py` (reads the sheet's search phrases, finds each in both transcripts, interpolates by word position):
- Method check: sheet time minus first-cut estimate, median -0.3 s, max absolute 4.6 s (stop 2 is the optional sting). So the method is good to about plus or minus 5 s.
- Against the FINAL transcript: 40 of 49 phrases found (9 not found, Zac edited those lines). Median shift -7.0 s, range -9.0 to +5.7 s. Stops 18 to 49 sit 6.4 to 9.0 s earlier in the final than in the stringout. Stops 3 to 7 sit 3.9 to 5.7 s later (Zac's 11-21 intro package, which the sheet notes but the stringout v1 never got). Stops 14 and 16 move -2.8 and -5.6.
- Cost: dropped on V2 above the final cut, about 30 of 40 matched pictures would land 6 to 9 s off their line. Search phrases (already on the sheet) are the only thing that still lands them. Not verified by frame pulls on Zac's export, only by transcript position, and not known whether Zac used the stringout at all.
- QA report check: it proves 36 of 36 stops land on their RUN SHEET frame. It does not test the sheet against the spoken line, a loudness number, or a later cut. Pass was true and not enough.
- Coverage (head-editor notes in the plan, line 115): 22 stretches over 20 s with no picture, clip or cam, worst 213 s (27:38 to 31:11). Pictures and clips are 9.6 percent of runtime. The plan listed them and proposed no fill.
- Craft Brief departures: S1 concat and frame count method followed (65,910 frames matched, PROVEN). No loudness line (S2, S3) because the stringout is silent by design, but the plan carried a -14 LUFS target with no source (brief section 3).

### B. Ian trailer v1 to v5 and the 45 s gap list (jobs 2026-11-17 to 2026-11-21)
Files: `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\` (v1 16:9 38 s, v2, D33 v3 and v4 four files each, D34 v5 two files), `D:\WKP\Post-Production\reports\Ian-Trailer-45s-Build-and-Gap-List-2026-11-21.md`. I did NOT re-probe or view these this job (budget), so the findings below are from the gap list text, my lessons file and TASKS.md.
- v3 came out 1079 frames, not 1080, until tpad was added (lessons 2026-11-20). Rework, caught by my own ffprobe count, no cost to Zac.
- v4 static memory crop clipped the entering ball at x 160, fixed at x 0 (lessons 2026-11-20). Caught by my own frame pull.
- v5: TASKS.md records "fix lopsided blur bars" and the gap list line 56 says R1, R3, R5 vertical stills fill about a third of a 16:9 frame on blurred fill. Contain-fit is correct (S1: scale with force_original_aspect_ratio "keep the original aspect ratio"), but a symmetric blurred fill with an off-centre subject reads lopsided. v6 queued. Cost: one more build and a head-editor round. Not viewed again by me.
- 12.0 s missing of 45 s (H1 6, B1 3, W1 3), 4 NEED stills: the gap list did the arithmetic with a floor and a cheapest path (lesson 2026-11-21). Credit cost "NOT RETRIEVED", honest.
- No loudness measurement exists for any Ian file because all are silent except v2 sound files, which were never measured against S2/S3 (not checked this job).
- The "22 gaps over 20 s" head-editor note lives in the AKT plan (line 115), not in an Ian file.

### C. Drill 1 build (this job) for contrast
`D:\WKP\scratch\leveling-drill1\VQ8-drill-run-sheet.md`. Used the FINAL transcript, mechanical checks pass, but 7 of 31 numbered pictures were not on disk, the old shipped sheet is about 18 s later than the final cut on most stops (it was built from the earlier 27:57 cut), and the export misses the lock: -21.2 LUFS (lock -14), true peak +0.1 dBFS (lock -1), black tail 2.4 s (lock 1 s). Details in the drill result.

## Ranked: the 3 gaps that cost the most
1. **Timing drift against the final cut.** Stringouts and run sheets are timed to a pre-final transcript, then Zac recuts. AKT: median 7.0 s, up to 9.0 s off, about 30 of 40 matched stops. VQ8 shipped sheet: median about 18 s off the final. Fix: take the LATEST transcript, compare its length to the newest export or sequence, print a drift table (search phrase vs time) in the hand-back, and rebuild the stringout when the final transcript lands. Preflight items 1 and 2.
2. **Checks that prove consistency, not correctness, and no loudness, tail or coverage numbers.** QA of A passed 36 of 36 against our own sheet. Real exports miss the lock (VQ8 -21.2 LUFS, +0.1 dBTP, 2.4 s black). Every run sheet that names -14 LUFS should say it is Zac's lock and give the measured number when an export exists (S2, S3). Fix: preflight loudness and black tail items, with the command, on every output type.
3. **Coverage and fill.** Pictures plus clips covered 9.6 percent of AKT, and 8 percent (132 s of 1657.7 s) of the VQ8 drill cut with 24 pictures. Gap lists exist but with no fill proposal or count of what is missing on disk (7 pictures absent). Fix: every gap over 25 s gets a PROPOSED fill or "talk-led, none needed", and a file-exists check runs before placement.
Also logged (not top 3): Ian v5 lopsided blur bars (blurred fill symmetry for vertical stills in 16:9).

## Scripts and logs (all in `D:\WKP\scratch\leveling-drill1\`)
akt_delta.py, check1.py, cmp.py, build.py, pull.py, ebur.log, black.log.
