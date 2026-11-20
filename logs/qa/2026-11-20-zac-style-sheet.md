# QA report: Zac Style Sheet and Improvement List

Date: 2026-11-20. Checked by qa-director (no bench used, checks run directly). Budget: under 30 min, $0, no credits. Nothing edited, nothing written to L:, P: or E:.

Files checked
- .md: D:\WKP\Post-Production\reports\Zac-Style-Sheet-2026-11-19.md
- .docx: D:\WKP Reports\Editor Style Sheet\2026-11-19 - Zac Style Sheet and Improvement List.docx

## VERDICT: FAIL (one blocker, fix is small; everything else passes or is a note)

## Blocker

**B1. Conflict with a locked WWD rule (checklist 3).**
- Locked rule: `D:\WKP\WWD\CLAUDE.md`, "Pictures are cutaways (LOCKED 2026-10-19, Zac)": "a few solo camera cuts, only when a host makes a good point and has the floor (not every long turn)". Also `D:\WKP\WWD\STANDARDS.md` item 4: "A few solo cams only, when a host makes a good point."
- The sheet breaks it in these places:
  - Part 4 rule 7 "Cams follow the floor": "When one host talks for more than about 15 s, cut to his solo cam". That is cutting on every long turn, the thing Zac ruled out.
  - Page 1 and Part 4 creative call D, and Recipe 2: multicam pitched as a way to "fill many static stretches with cam changes".
  - Part 6: Clayface item 1 ("solo cams on each long turn"), Crystal Lake item 1 ("solo cams through the long turns"), Vision Quest EP 5 and 6 item 1 ("cams through the long turns"), Vision Quest EP 7 item 1 (cam switch at each reply).
  - Part 3 table row "Cam cuts" names "cams are cut by hand, so they are rare" as a gap, which treats the locked rarity as a defect.
- Part 4 opens with "Your locked rules stay as they are and win any conflict" and lists the locked rules, but the solo-cam limit is not in that list. So the sheet claims to respect the rules while contradicting one.
- What a fix looks like (describe only): add the solo-cam rule to the locked list in Part 4. Re-word rule 7, creative call D, Recipe 2's purpose and the Part 6 lines so that pictures and clips carry the 60-second rule and solo cams stay "a few, on a good point". If the studio wants more cams, label it plainly as a PROPOSED CHANGE to a locked rule that needs Zac's yes, in the "What needs your call" list on page 1. Regenerate the .docx from the .md.

## Checklist results

**1. Numbers trace (PASS, with one small miss).** I recomputed from `scratch\editor-study\out\*.json` with my own script (`scratch\editor-study\qa_trace2.py`, `qa_trace3.py`) and read `sil35.txt`.
Traced and matching (14):
1. Longest whole-video stretches: VQ8 23:25 to 27:38 (254 s), VQ7 5:48 to 11:23, GODZ 18:21.5 to 22:26, VQ56 9:50.5 to 13:30, CLAY 11:28.5 to 21:23, CRYS 22:18 to 35:31.5 (13:13), SF 14:19.5 to 17:03.5, CARR 33:31.5 to 37:38.
2. Off-two-shot percentages (13.2, 8.0, 12.6, 9.3, 10.3, 9.0, 15.7, 12.2) all match.
3. Integrated LUFS and true peak for all 8 (-21.2/+0.1, -22.8/-1.7, -24.7/-2.4, -23.0/-2.2, -23.3/+0.9, -20.5/-0.3, -20.6/+1.6, -21.5/+1.0). "4 of 8 above 0 dBTP" is right (VQ8, CLAY, SF, CARR).
4. Godzilla black tail: I re-ran blackdetect on the file, black 28:43.1 for 10.5 s. Silence 8.8 s at 1724.8 s matches the JSON.
5. Godzilla repeat at 25:36.8 and 26:15.0: I grabbed both frames at 32x18 grey and the pixel values are identical. Confirmed.
6. VQ8 61 s solo run at 21:06: JSON run list, 61.5 s. Confirmed.
7. Carrie 24:00 to 28:02 and 33:31 to 37:38, VQ56 24:30 to 27:43 (3:13): match.
8. -35 dB pause counts (SF 4, VQ7 9, CLAY 12, GODZ 18, VQ8 19, CRYS 20, VQ56 21, CARR 32) match `sil35.txt`. "1.2 to 5 minutes between pauses" checks (39.5/32, 20.8/4).
9. Carrie 9 silences, 20.5 s total: match.
10. Intro gaps (VQ8 -15.5 vs -22.7, about 7 LU; VQ7 -25.4 vs -24.1, about 1 LU quieter; Clayface last 20 s -32.2 vs -24.3, about 8 LU) match.
11. Kept ratios (SF 32 percent; VQ7 56, CARR 58, VQ56 61, GODZ 62) match the measurements md.
12. Older work: Ladies Night 40 s over 29 cuts is about 1.4 s; Father's Day 135 s over 24 is 5.6 s; -7.9, -12.1, -30.9 match; "more than 20 LU apart" is right (23 LU).
13. "6.5 to 10.7 LU short of -14": right.
14. Transcript quotes: VQ7 "welcome back everybody" restart at 0:18 and "this show is a hundred percent heating up" confirmed in the EP 7 transcript. Godzilla "Super Saiyan moment" at 18:59 and "creature combat" at 21:44 confirmed. VQ8 "I don't hand out a lot of nines" is in the VQ8 transcripts (time not checked).

Misses and unchecked (notes, not blockers):
- N1. Part 1 note says "a median of exactly 5.0 s on 6 of 8 reviews". The data shows exactly 5.0 on 5 of 8 (VQ8, GODZ, VQ56, CLAY, SF); CRYS is 5.5, VQ7 6.5, CARR 8.0. Page 1 "about 5 s, median of 6 of 8" is defensible as 5.0 to 5.5, but the Part 1 wording is wrong. Fix to 5 of 8.
- N2. Page 1 gap 3 says all 7 transcripts have a "welcome back" restart of "10 to 19 s". That range is not in the measurements md. I confirmed only the Crystal Lake figure is stated in Part 6 and the VQ7 restart exists at 0:18. The per-review restart lengths were not available to trace. Either cite where the 10 to 19 s comes from or say "up to 19 s (Crystal Lake)".
- N3. The Part 1 table counts Carrie's stretches over 60 s as 10 (body only, per the measurements md) while the footnote says the table counts the whole video. Whole-video count from the JSON is 11. Other rows are the same either way. Align the footnote.
- N4. Crystal Lake StreamYard tag, health-bar overlay, spoiler cards and other "seen on frames" claims were not re-viewed by me. They are labeled "viewed, not measured" in the source, which is honest.

**2. Premiere steps vs fact-check (PASS WITH NOTES).** Steps the fact check covered are marked correctly: Lumetri retirement in 2027, 2027 projects not opening in 2026, Export Effects tab and Loudness Normalization, BS.1770 and true peak limit with the beta bug, multicam workflow and the Button Editor, N, V and C shortcuts, end screen 5 to 20 s and 25 s minimum, Generative Extend 2 s and 10 s limits. Sheet marks NOT VERIFIED on the loudness meter path, "New Sequence From Clip", multicam audio option wording, Alt-drag on 2027, M and S shortcuts, Color mode labels, Generative Media credit use.
Stated as fact but not in the fact-check brief and not marked (N5): Recipe 1 steps 1 and 2 (I and O points, "Export tab or File > Export > Media"); Recipe 2 step 3 "Use Clip Names"; Recipe 3 Motion > Scale 115; Recipe 6 Gaussian Blur Blurriness 80, Repeat Edge Pixels, Brightness & Contrast -40; Ripple Delete after Razor. These are long-standing Premiere basics and look ordinary, but under the honesty rule they should carry "not checked against 2026 or 2027" like the others. Also the fact check says the credit table is secondhand; Part 7 says so. Good.
Premiere Pro 2026 and 2027 both installed: confirmed (both folders in C:\Program Files\Adobe).

**3. Locked WWD rules (FAIL, see B1).** Everything else is consistent: 7 s max, no repeats, contain-fit, music intro and outro only, loudness -14 LUFS and -1 dBTP (matches STANDARDS), cards in first 3 minutes, no actor tags (none proposed), pictures only from the title reviewed, Adobe not touched. One watch item (N6): Part 4 rule 10 and Part 6 Clayface suggest opening each topic block with "a picture or clip". Locked clip rule requires a clip to play only under a host line about that exact scene, 6 to 8 s, never back to back. Add that clause so a studio reader does not pull clips for scene changes that the hosts are not describing.

**4. .docx matches .md and location (PASS).** python-docx read: 26 headings in the docx equal the 26 headings in the .md, plus the title. 4 tables with the right shapes (9x8, 14x3, 9x4, 6x4), all four .md tables present. Zero em or en dashes in either file, zero leftover markdown (asterisks, backticks, pipes, hash marks, raw bullets). Letter portrait, 0.7 in margins. File is in `D:\WKP Reports\Editor Style Sheet\` with the date-first name per the SOP. `slop_check.py` on the .md: clean (mechanical pass only). The docx was not rendered to a page image by me, so visual layout and page breaks are NOT CHECKED. Fix B1 will force a rebuild, so check the render then.

**5. Page 1 and Part 7 (PASS WITH NOTES).** Page 1 is plain, has the "what you do well", three gaps, a one-sentence target, and a short "needs your call" list. Small note (N7): "LUFS", "dBTP" and "LU" are never explained in plain words on page 1. One short line ("LUFS is how loud the whole video is, dBTP is the loudest spike") would suit Zac. Part 7 is clearly PLAN ONLY, credits at zero, no run, prompts labelled "when credits return", unverified claims labelled NOT VERIFIED. Passes.

**6. Honesty on what was not heard or verified (PASS).** Page 1 and Part 8 say nobody listened, retention not pulled, YouTube -14 LUFS is third-party, two sources blocked, Adobe Help 403, Carrie transcript not read, transitions and speech pace not measured. Cleanest part of the sheet.

## Gates
Public copy gates do not apply (internal document for Zac). The Part 7 prompts are drafts for Zac's own use. Head-editor notes were stated as applied; I saw the loudness standard, 60 s rule and recipe fixes in the text.

## What I did not run
No audio listening, no frame review beyond the Godzilla repeat and tail, no docx visual render, no live check of Premiere menus. No bench used.

## RECHECK (2026-11-20, qa-director, budget 15 min, $0)

VERDICT: PASS WITH NOTES

B1 resolved. The locked "few solo cams, only on a good point" rule is now in the Part 4 locked list. Rule 7 reads "Cams stay few and earned". The 60-second rule is carried by pictures and clips. Multicam (call D, Recipe 2) is labelled PROPOSED CHANGE and appears in the page-1 "needs your call" list. Part 3 cam row, Part 6 (VQ8, VQ7, Clayface, Crystal Lake, EP 5 and 6) reread: no line contradicts WWD\STANDARDS.md item 4. The old "cut to his solo cam" text is gone from the docx.

Notes handled: N1 (5 of 8), N2 (Crystal Lake 19 s), N3 (footnote explains body vs whole-video), N5 (marked), N6 (clip clause in locked list), N7 (plain-words box). N4 unchanged and honestly labelled.

Docx vs md: 26 headings plus title match the 27 md headings, 4 tables with the same shapes, zero em or en dashes, no leftover markdown, slop_check clean.

Notes, none blocking:
- Part 6 Carrie item 2 (Razor and Ripple Delete) lacks the "not checked on 2026 or 2027" tag.
- Docx visual render and page breaks still not checked by me.
