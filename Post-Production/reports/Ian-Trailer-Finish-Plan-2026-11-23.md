# Ian "Wrench Turner" trailer: FINISH PLAN and FINISH LIST (2026-11-23)

Point man: assistant-editor. Free favor for Ian, Zac delivers the files, Ian posts. Nothing generated, spent, posted, sent or pushed by the team. DO NOT FORWARD TO IAN: this file names the plot fence. Credit cost for every Firefly click is NOT RETRIEVED, Zac reads it at the Generate button.

Tags: PROVEN = measured or viewed in a file today. SOURCED = from a named file or page. PROPOSED = my plan or default, nobody has tested or heard it. Nobody has heard any sound.

## BLUF

- Four files are the goal: 45 s and 15 s, each 16:9 and 9:16. The cover story animatic is a separate piece and is not in this list.
- Everything that does not need Zac or credits is done: v6 builder, four v6 placeholder files, captions burner, music probe, loudness checker, R3b alignment check, sitting sheet, delivery blocks. The only blockers are the Firefly sitting, a licensed music file, Ian's buy link and Zac's ears.
- The day the four winners land, one command builds all four files with the real stills. No re-planning.
- Zac's ordered steps are at the bottom (Part E). Seven steps, three of them ten minutes or less.

## Part A. FINISH LIST (every step to a delivered trailer)

Who: TEAM or ZAC. Status: DONE (team, today), READY (team, waits on a trigger), WAITING (Zac).

| # | Step | Who | Blocked on | Tag | Status |
|---|---|---|---|---|---|
| 1 | Prompts in the chain doc match the four log folders and pass the linter | TEAM | nothing | PROVEN | DONE. Script compares main and negative text for R3b, H1, B1, W1: all 8 MATCH. prompt_lint: 0 FAIL, 3 WARN (R3b 138, H1 139, B1 139 words vs the 125 word target, which is PROPOSED, not trimmed). No prompt text was changed |
| 2 | Firefly sitting: R3b, H1, B1, W1 in order, settings.txt with the credit number | ZAC | Firefly credits (refilled 2026-11-20, amount unknown) | SOURCED sheet, PROPOSED strengths | WAITING. Sheet: Part B |
| 3 | Pick winners, save to Pictures folder with the exact file names, say "winners are in" | ZAC | step 2 | SOURCED | WAITING |
| 4 | R3 to R3b alignment check (50 percent blend of the two stills, one wrench and one lamp or nudge) | TEAM | step 3 | PROPOSED | READY. `tools\r3b_check.py` ran on a stand-in |
| 5 | v6 assembly rules (below, Part C) build all four files with the winners | TEAM | step 3 | PROVEN on stand-ins | READY. Placeholder v6 already built (see Part D) |
| 6 | The 12 s gap fix: H1 6.0 s, B1 3.0 s, W1 3.0 s fill the 12.0 s hole, 45.0 s total | TEAM | step 3 | PROVEN (1080 frames at 24 fps with stand-ins) | READY. Fallbacks: B1 dropped means H1 holds 9.0 s (`--drop-b1`), W1 dropped means R5 and R1 each hold 1.5 s longer (`--drop-w1`), both tested to 1080 frames |
| 7 | head-editor notes on v6 (pacing, bars, 9:16 small stills), apply clear fixes, creative calls to Zac | TEAM then ZAC | step 5 | PROPOSED | READY |
| 8 | Music: download the Pixabay track and save the license proof | ZAC | nothing, can be done today | SOURCED | WAITING. Steps in Part C |
| 9 | Music edit points from the real file (loudness and level per second) | TEAM | step 8 | PROVEN tool | READY. `tools\music_probe.py` reproduced the music agent's -18.2 LUFS and -0.3 dBFS on the owned track |
| 10 | Sound pass: cue sheet SFX plus music into one mix, by ffmpeg (team master) or Premiere (Zac) | TEAM (sound-designer) | steps 5 and 9, final cut times | PROPOSED | READY after v6 with winners. Cue sheet: `projects\ian-trailer\2026-11-20-sfx-cue-sheet.md`. Every cue is "not heard" until Zac listens |
| 11 | Burned-in captions (He came home from the war. / Back then, he was the Wrench Turner. / The car was the easy part. / 15 s: The wrench still fit his hand.) | TEAM | step 5 for the real build | PROVEN on placeholder files, frames viewed | READY. `tools\captions_v6.py`. The Wrench Turner line has a switch (`--no-wt`) if Ian says no |
| 12 | Buy link on the end card and in the description | ZAC gets it from Ian, TEAM types it | Ian's link, checked on a phone | SOURCED (open item since Draft 3.3) | WAITING. End card shows [buy link] until then |
| 13 | One short text to Ian: caption OK, cover use in video and ads (and a bigger cover file if he has one), the buy link, keep the AI label on | ZAC | nothing | SOURCED (the four lines are items 3, 4, 5 and 9 of Draft 3.3 Section 9, word for word) | WAITING. Items 1, 2, 6, 7 and 8 are NOT asked: Zac ruled 2026-11-21 that the team decides the small shots and nothing goes back to Ian per item |
| 14 | 9:16 and 15 s versions | TEAM | step 5 | PROVEN | READY. Same script, same command. The 15 s files only change at R3b. In 9:16 the three 16:9 stills (H1, B1, W1) are contain-fit, so they sit small on a blurred fill. head-editor call: contain-fit (the never-crop rule) or a middle window |
| 15 | Loudness to -14 LUFS integrated, true peak at or under -1.0 dBTP, on all four files | TEAM | steps 10 and 11 | -14 is Zac's lock, PROPOSED for TikTok and Facebook (not verified for them). EBU R 128 itself says -23 | READY. `tools\loud_check.py` (tested). Two-pass loudnorm is the fallback, untested on this material |
| 16 | qa-media frame check (no readable badge, plate or logo on any generated still or truck, no child, no second woman) and loudness | TEAM (qa-director route) | step 15 | PROPOSED | READY after the export |
| 17 | Final listen and look, approve or send back notes | ZAC | step 16 | n.a. | WAITING |
| 18 | Name the four files, copy to the Final folder, hand to Ian with the which-file-goes-where list and the paste blocks (Part C) | ZAC delivers, TEAM prepares the folder | step 17 | SOURCED | READY |

## Part B. Firefly sitting sheet

Separate one-sheet file (phone and print): `D:\WKP\Post-Production\reports\Ian-Trailer-Firefly-Sitting-Sheet-2026-11-23.md`, docx `D:\WKP Reports\Ian Book Trailer\2026-11-23 - Ian Firefly Sitting Sheet.docx`. Prompts are copied by script from the chain doc, not retyped.

## Part C. Rules and recipes for the team steps

### C1. v6 assembly rules once winners land (rule set, SOURCED from Draft 3.3, the 45 s gap list and the chain doc unless tagged)

1. File names must be exactly: `R3b-handoff.png`, `H1-homecoming-v1.png`, `B1-brotherhood-v1.png`, `W1-sweetheart-v1.png` in `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Pictures\`. A missing name means that beat stays a gap card.
2. Timeline (24 fps, 45 s): V1 0.0 to 3.0, V4 memory 3.0 to 6.5, R3 into R3b 6.5 to 12.0 (R3 alone until 9.5, crossfade 9.5 to 11.0, R3b hold to 12.0), V1 12.0 to 16.0, H1 16.0 to 22.0 (3.5 s wide push then 2.5 s tighter reframe, one still), B1 22.0 to 25.0, W1 25.0 to 28.0, R5 28.0 to 30.5, R1 30.5 to 34.5, V1 punch-in 34.5 to 38.0, black with the last line 38.0 to 41.0, cover end card 41.0 to 45.0.
3. The R3 to R3b hand-off is a plain crossfade of two stills with one continuous push across both (PROPOSED, 6 percent over the whole slot so the scale does not jump at the dissolve). Never a video-model morph (STANDARD R6, hand-offs failed 6 of 6). Length 1.5 s per Draft 3.3, 2.0 s per the 2026-11-22 chain doc is one number (`--xf 48`), a look call for Zac. If the 50 percent blend shows two wrenches, nudge Position and Scale of R3b in Premiere (Draft 3.3 Appendix G 5.3).
4. The 15 s file: V1 0.0 to 3.0, V4 3.0 to 5.5, R3 into R3b 5.5 to 9.5 (crossfade 7.5 to 9.0, my choice, the clink sits at 8.25 not 8.5), V1 3.2 to 5.7 at 9.5 to 12.0, end card 12.0 to 15.0.
5. Memory look on V4, R3, R3b only: warm, lifted blacks, heavy grain, vignette, 1440 px window with black side bars. The older man never wears a black tee.
6. Stills never cropped: contain-fit on a blurred fill. v6 fix (PROVEN, frames viewed): the fill is now built from the still averaged with its own mirror image, so the left and right bars match. v5 bars were lopsided because the fill followed whatever was on each side of the still.
7. Winners are checked against the fence by eye before the build: no child or small figure, one woman only in W1, flag correct in H1, no readable text on trucks or clothing.
8. Optional, off by default: `--r2` puts the R2 still over the second V1 beat (12 to 16 s). The v6 queue named it but the head-editor v5 notes file was not found on disk, so the source is not confirmed. V1 live footage is the better "thinking" beat, so I recommend leaving it off.
9. v1 to v5 stay. The script refuses to overwrite a file.

### C2. Commands (team, run when winners land)

```
python D:\WKP\scratch\ian\v6\tools\r3b_check.py R3.png R3b-handoff.png out.png
python D:\WKP\scratch\ian\v6\build_v6.py --which all --tag v6c
python D:\WKP\scratch\ian\v6\build_v6.py --which all --tag v6clean --nolabels --out <scratch>   (clean files for caption burn)
python D:\WKP\scratch\ian\v6\tools\captions_v6.py <clean.mp4> <out.mp4> 45 16x9
python D:\WKP\scratch\ian\v6\tools\loud_check.py <four finished files>
```

### C3. Music: Zac's steps, nothing else (SOURCED from the music agent 2026-11-20, page read online that day)

1. Open https://pixabay.com/music/solo-piano-ambient-509927/ ("Ambient" by leberch, 2:04, Pixabay Content License, no credit needed, Content ID registered).
2. Full-page screenshot showing the title, "Free for use under the Pixabay Content License", "Content ID Registered" and the date. Save as `2026-11-23 pixabay-leberch-ambient-trackpage.png`.
3. Open https://pixabay.com/service/license-summary/ and print it to PDF as `2026-11-23 pixabay-license-summary.pdf`.
4. Click Download on the track page. Pixabay may ask for a free account or a check, the team did not test that.
5. Save the mp3 and both proof files in a new folder `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Music\Pixabay\`.
6. Say "music is in". The team measures it (`music_probe.py`), writes the edit points and rebuilds the mix on the same cue times.

Risk, said plainly: a Content ID claim may land on Ian's upload. Keep the screenshots and dispute with the Pixabay license. Not stated on Pixabay's pages: whether the license covers Ian posting a video Zac made. Owned `searching-for-hope` and `beautiful-way-to-end` are timing demo only (no license proof on disk). Alex Morgan is dropped (tracks labeled AI generated). No ElevenLabs music.

### C4. Delivery (Zac hands over, Ian posts)

File names (PROPOSED): `The-Wrench-Turner-Trailer-45s-9x16.mp4`, `-45s-16x9.mp4`, `-15s-9x16.mp4`, `-15s-16x9.mp4`, saved in `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Final\` (empty today).

Which file goes where (Ian can change it, upload specs not rechecked): TikTok 45 s 9:16 first, the 15 s 9:16 a few days later. YouTube 45 s 16:9 as a normal video, 15 s 9:16 as a Short. Facebook 45 s 9:16 as a Reel, and on a different day a 16:9 as a page post.

Paste blocks (approved copy, Draft 3.3 Section 10, unchanged). Fill the brackets. If the buy link does not work on a phone that day, delete "Available now." from both blocks and from the end card.

45 second files

    He came home from the war.

    The Wrench Turner by Ian Griffin. Available now.
    [BUY LINK]

    Music: [MUSIC CREDIT]
    The scenes in this trailer were made with AI tools.

    #TheWrenchTurner #BookTrailer

15 second files

    He came home from the war. The old wrench still fit his hand.

    The Wrench Turner by Ian Griffin. Available now.
    [BUY LINK]

    Music: [MUSIC CREDIT]
    The scenes in this trailer were made with AI tools.

    #TheWrenchTurner #BookTrailer

Notes: TikTok may swap `[BUY LINK]` for `Link in bio.` The Pixabay pick needs no credit, delete the music line if that track ships. The 15 s middle sentence is marketing's edit and was not read by originality and clearance by name. The AI label toggle on Ian's accounts is his call, recommend on for all three (TikTok and Facebook rules not verified).

## Part D. Done now by the team (2026-11-23)

All of it free, read-only on source media, nothing generated, nothing sent.

- Spot-check: chain doc against `D:\WKP\data\firefly-prompt-log\ian-R3b, ian-H1, ian-B1, ian-W1\prompt.txt`: main and negative text identical in all four (script `scratch\ian\v6\verify_prompts.py`). Each log folder's `settings.txt` still has the PANEL and RESULT blocks blank for Zac, and `notes.txt` is blank, as intended. No prompt text touched, so no new lint run beyond the check above.
- v6 builder `D:\WKP\scratch\ian\v6\build_v6.py` and four placeholder files in Rough Cut (probed, frames counted): `Ian-Trailer-D34-45s-16x9-v6-with-gap-cards-silent.mp4` (1920x1080, 1080 frames, 45.000 s), `...-45s-9x16-v6-...` (1080x1920, 1080 frames), `...-15s-16x9-v6-...` (1920x1080, 360 frames, 15.000 s), `...-15s-9x16-v6-...` (1080x1920, 360 frames). They still hold gap cards for R3b, H1, B1, W1. Not played, silent. v1 to v5 untouched.
- Winners path proven with stand-ins (frames of an old still and three clip frames in a scratch folder named as the winners): all four combinations of 45 s and 15 s built to 1080 and 360 frames, plus the `--drop-b1` and `--drop-w1` fallbacks. Contact sheets viewed: bars are now mirror-symmetric, the R3 to R3b crossfade runs, 9:16 stills sit contain-fit. The stand-in R3b ghosts the wrench because it is a shifted copy of R3 (expected, and it shows why the alignment check exists). Stand-in output stayed in scratch.
- Captions: burned onto clean 9:16 and 16:9 placeholder files in scratch, frames viewed at C1, C2, C3 and C4. They sit clear of the hands. C2 on 16:9 sits over the lamp and sleeve at the top of R3, so check one real frame once R3b exists.
- Music cue demo (scratch, NOT for posting): the owned track with the music agent's edit points on the 45 s file, probed with the new loudness checker: integrated -20.2 LUFS, LRA 14.9 LU, true peak -2.4 dBFS, black 38 to 41 s as designed. It misses -14 by 6 LUFS before any sound effects, so the mix needs about +6 dB of gain and a limiter, not just a normalize pass. Not heard. The owned track has no license proof, so this file never goes to Ian.
- Tools in `D:\WKP\scratch\ian\v6\tools\`: `r3b_check.py`, `music_probe.py`, `loud_check.py`, `mix_rough.py`, `captions_v6.py`, `make_sheet.py`. loud_check was tested on the cover story sound file (read -15.1 LUFS, true peak -1.5, so that older piece also misses the -14 target by 1.1).
- Not done on purpose: the SFX mix (cue times move with the winners, so sound-designer builds it once v6 is final), real buy link and music credit (waiting on Ian and Zac), any Firefly click.

## Part E. What Zac must do, in this order

1. Music proof, 10 minutes, anytime (Part C3). Independent of everything else. Say "music is in".
2. Firefly sitting with the sheet: R3b, H1, B1, W1 in order. Copy the credit number from the Generate button into settings.txt before each click. Save winners with the exact names. Three misses on a card: stop and say which, do not try a fourth.
3. Say "winners are in" (and name any still you dropped). Team builds v6 and the clean captioned set the same day.
4. Watch the v6 45 s 16:9 once (path comes with the build). Say OK or give one change. The only open look calls: crossfade 1.5 s or 2.0 s, the small 9:16 stills, C2 caption position.
5. Send Ian the four-item text (Draft 3.3 Section 9 items 3, 4, 5 and 9, word for word). Paste the buy link back to Jarvis. If Ian says no to the Wrench Turner line, the team runs `--no-wt`.
6. Listen once to the team master (picture, captions, sound, music, -14 LUFS, qa-media passed) and say OK or give notes. Open Premiere only if you want to polish: Draft 3.3 Appendix G is the build guide.
7. Copy the four files from the Final folder to Ian with the which-file-goes-where list and the paste blocks. Ian posts.

## Open items and honest limits

- Nobody has played any file or heard any sound. Credit cost, panel options (Reference types, Negative box, Seed, Veo End frame and Audio switch), the Firefly prompt length limit and every strength value are NOT VERIFIED or UNTESTED.
- Pixabay license reach for a third-party poster and Content ID handling are not stated on its pages.
- Ian's answers (caption, cover use and file, buy link) are open. The Ford marks on the cover remain an attorney question, not raised with Ian.
- The head-editor v5 notes file was not found on disk (TASKS names the v6 queue only).
- No qa-director pass has run on these new files or the sheet. Word was not available to render the docx, so the sheet's page count is not checked.
- Premiere menu names are NOT VERIFIED on Zac's 2026 or 2027 install.
