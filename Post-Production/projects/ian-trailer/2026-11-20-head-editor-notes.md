# Ian "The Wrench Turner" trailer, Draft 3.3 v3 silent rough: head-editor notes (2026-11-20)

I advise, Zac cuts. Nobody can hear audio: the four v3 files have no audio stream (ffprobe on the 45 s 16:9 file lists one stream, video). Every sound line below is "not heard", a plan only.

## What I viewed and did not view
- Viewed: all four contact sheets (`D:\WKP\scratch\ian\v3\sheet45_16x9.png`, `sheet45_9x16.png`, plus the 15 s sheets listed by assistant-editor, which I did not open); full-size frames I pulled with ffmpeg from the 45 s files at 16:9 1.0, 4.5, 8.0, 32.0, 36.0 s and 9:16 0.2, 1.5, 8.0, 36.0 s (`D:\WKP\scratch\ian\v3\he\m16.png`, `m9.png`). Read the brief, assembly plan, SFX cue sheet, music file (first 50 lines) and the Style Sheet.
- Not viewed: playback of any file, the 15 s files, motion between frames (so I cannot judge the feel of the push-ins or the 1.0 s dissolve), V1 around the arm drop (3.0 to 3.4 s), the devils-advocate file (assistant-editor and the brief already carry its changes). Slates (H1, B1, W1, R3b) are placeholders, so I judge their timing only, not their content.
- Premiere menus: nothing here is tested on Zac's Premiere 2026 or 2027. Anything not confirmed says NOT VERIFIED.

## What works
- Present versus memory reads clearly in the frames: cool, bright, grey garage against warm sand light with the ball. The 4.5 s frame (ball, boots, shadow) is the best single frame in the cut.
- Beat 11 lands on a different place in the car than beat 1 would suggest in 16:9: the tight hands and wrench read as "working again" even in a still frame.
- End card is contain-fit, uncropped, no push. Correct.
- Structure holds to the brief: no door rise, no present-day child, no whose-car caption.

## Top notes (8)

**1. One treatment for vertical stills in 16:9: dark blurred fill, everywhere. CLEAR FIX, assistant-editor.**
What: R1 and R5 sit on a blurred fill, but R3 sits on what reads as pure black (the frame at 8.0 s is a 608 px strip on near black). Why: two looks for the same type of picture reads as a mistake, and the Style Sheet pick (creative call B) is a blurred, darkened copy behind the still, still contain-fit. R3 is so dark that its blur is nearly black anyway, so the fix costs nothing there. The fix: same recipe on R1, R3, R3b, R5: blurred copy scaled to fill, Gaussian Blur about 80 with Repeat Edge Pixels, Brightness about -40, the real still on top at contain-fit. Memory beats (R3, R3b) keep the 1440 px window: fill stays inside the window and the 240 px bars each side stay pure black, so V4, R3 and R3b share one frame shape. Note for Zac: call B for WWD portrait posters is still his to rule; this note only unifies the trailer. Also true and unavoidable: a 608 px strip is 32 percent of a 1920 frame, so R1, the payoff of the garage beat, is small. Do not enlarge it (that is a crop). Let its 10 percent push carry it.

**2. Beat 11 against beat 1. CREATIVE CALL. My pick: keep it as a bookend, but make it a stronger change.**
What: beat 11 is V1 0.0 to 3.5 again, same action as beat 1, punched in to 120 percent. In the 16:9 frames (1.0 s and 36.0 s) it is the same shot with the hands larger. Why: the brief says never repeat the same picture; here it is a callback on purpose, and the ratchet clicks returning (S6 on frame one) carry the meaning. But V1 is nearly spent (0 to 4 and 3.2 to 7.2 are used), so a different clip is not available. The fix, three changes in one move: (a) animate the punch-in from 115 to 135 percent over the 3.5 s so it pushes toward the hands instead of sitting still; (b) start the clip at about V1 0.6 s so the first frame is mid-turn, not the same frame as beat 1; (c) keep the crop on hands and wrench, head only at the bottom edge. 135 percent on 1080p is a 1422 x 800 source area, soft but fine under grain; do not go past 140. Alternative if Zac wants more difference: 75 percent speed on the last turn (sound then needs its own take, ratchet is sync-sensitive). Not my pick.
Who: assistant-editor applies; Zac approves by eye.

**3. V4 memory window crops the sides (x offset 160). CREATIVE CALL. My pick: allow it for V4 only, with limits.**
What: the 4:3 window cuts 480 px of the 16:9 picture. Why I allow it: "contain-fit, never crop" is the rule for pictures and posters (never lose part of a graphic someone made). V4 is moving footage reframed as a stylistic memory window, the same type of move as the punch-in in note 2, and the brief asked for a narrower frame so the memory never reads as present-day Brandon with a child. In the 4.5 s frame the ball, shadow and both boots are inside. Limits: (a) keep the crop static, no pan; (b) ball and both boots must be inside on every frame from V4 0.8 to 4.3 s (check the ball's entry at about V4 1.0 s and the bump at about 3.0 s, I did not view those frames); (c) if the ball is clipped anywhere, move x offset, do not shrink the window. Fallback if Zac dislikes it: full V4 frame scaled to 75 percent, centered, black all around (a true windowbox, nothing cropped). I do not pick it, it looks like a TV in a dark room.

**4. Still holds: R3 at 5.5 s is a stand-in, hold the real plan. CLEAR FIX plus one CREATIVE CALL.**
What: R3 holds 5.5 s with a 6 percent push because R3b is missing. The real plan is R3 3.0 s, 1.5 s crossfade, R3b 1.0 s. 5.5 s of one still is inside the Style Sheet range (7 s max) but at the long end for a 45 s trailer. Fix (clear): when R3b arrives, rebuild to 3.0 plus 2.5. Until then, raise the R3 push to 8 percent so it is not static. R1 at 4.0 s with a 10 percent push is fine. R5 at 2.5 s is fine. The real long hold is coming: H1 is 6.0 s of one still (0:16 to 0:22), the longest still in the film. CREATIVE CALL, my pick: split H1 into two framings, a wide push for 3.5 s, then a cut to a tighter reframe of the hug (hands on his back, mom's face) for 2.5 s. A reframe of your own still is a move, not a violation of contain-fit. If a Veo upgrade ever exists the split is moot, but there are no credits.

**5. 9:16 beat 1 framing. CLEAR FIX, assistant-editor.**
What: at 0.2 and 1.5 s the head sits on the right edge of the 4:5 window, partly cut (frame m9.png). Why: the face is the hook, and the pan 0.55 to 0.65 starts too far left. Fix: start the pan at about 0.80 and end near 0.88 (window about x 845 to 930, so the right edge sits near x 1710 to 1794 of the 1920 source). The head is near x 1450 to 1560 and the wrench near x 1200 to 1440 by my read of the 640 px frames, so both stay in. These numbers are read off thumbnails: confirm by eye. The beat 11 window (x 907, 720 wide) keeps the head in at 36.0 s.

**6. Hard cut from V4 into R3 at 6.5 s jumps from bright warm to near black. CLEAR FIX, assistant-editor.**
What: V4 is a bright beige frame, R3 is a dark strip, back to back in the same memory. Fix: an 8 frame (0.33 s) Cross Dissolve centered on 6.5, V4 out extended to about 4.5 so the dissolve has handle (V4 is 8 s, handles exist). The reverb tail M3 from the cue sheet already carries across, so sound and picture agree. Keep the 12.0 s cut from R3b back to V1 HARD: that cut is the world changing, and the sound lane (air in on A2, wrench clink tail) does the bridging. Not heard.

**7. The memory grade on an adjustment layer will also lift the pillarbox bars. CLEAR FIX, assistant-editor.**
What: the ffmpeg rough lifted blacks inside the window only. A lifted-black effect on a full-frame adjustment layer turns the black bars dark grey, which makes the window look like a grey frame. Fix: see the recipe in section A below (Crop on the adjustment layer, or put the grade on each clip). Also fade the adjustment layer in with the 1.0 s dissolve at 3.0 s so the grade does not pop on at the start of V4.

**8. Loudness plan for the real mix. CLEAR FIX (process), wwd-sound or sound-designer does the mix.**
What: the files are silent, so no loudness exists to measure today. Why it needs care: the trailer has a silent open (0 to 3 s), a dropout stretch (30.5 to 38 s with no music) and a final chord, so integrated loudness sits low unless the music cue is mastered right. The working music is measured at -18.2 LUFS integrated, peak -0.3 dBFS, so it needs about +4 dB to reach -14 before the SFX count; the chord tail file is -12.2. Zac's standard is -14 LUFS integrated, -1 dBTP (Style Sheet Recipe 1, WWD\STANDARDS.md). -14 is a third-party YouTube reference, not Google documentation, and I did not verify TikTok or Facebook levels; Ian posts on all three. Steps in section D. The 15 s files are measured separately, because a short file can measure a different integrated value.

## A. Memory grade recipe for Premiere (V4, R3, R3b)
Version rule: finish in the Premiere version the project starts in (2026 or 2027). A 2027 project will not open in 2026. The Style Sheet reports (fact-research, from Adobe staff replies, Adobe Help pages were blocked) that 2027 retired the Lumetri Color panel. I could not verify any menu below on either version. If a name differs, find the same word nearby and tell the studio so this file is fixed.

Target look (from assistant-editor's ffmpeg values): warm (red up about 7 percent, blue down about 16 percent), saturation about 105 percent, contrast down about 7 percent, blacks lifted to about 7 percent, heavy grain, small vignette.

Build once on the 16:9 sequence, then duplicate for 9:16 (the adjustment layer comes with it).
1. Click the **Project** panel. Click the **New Item** icon (page with a folded corner, bottom right of the panel). Pick **Adjustment Layer**. Click OK (accept the sequence size). NOT VERIFIED menu wording.
2. Drag the adjustment layer onto the **track above** V4, R3 and R3b. Lengthen or shorten its ends by dragging so it starts at 3.0 s (the start of the V4 dissolve) and ends at 12.0 s (the last frame of R3b). Check the playhead at 11.23 s still shows the layer on, and at 12.0 s it is off.
3. Fade it in so there is no pop: click the layer, open **Effect Controls**, open **Opacity**, put the playhead at 3.0 s, click the **stopwatch** next to Opacity, type 0. Move the playhead to 4.0 s, type 100. This matches the 1.0 s dissolve. NOT VERIFIED that an adjustment layer takes opacity keyframes the same in 2027 (it did in earlier versions).
4. Confine the grade to the memory window: **Effects** panel, search **Crop**, drag it onto the adjustment layer. In **Effect Controls**, set **Left** 12.5 and **Right** 12.5 percent. The grade then only touches the middle 1440 px and the bars stay pure black. NOT VERIFIED that Crop on an adjustment layer limits the grade area; if the bars still go grey after the steps, do step 4b instead.
   4b. Fallback: skip the lifted black on the layer. Put the **Brightness & Contrast** (or the black lift) directly on V4, R3 and R3b one at a time, copy and paste attributes (right-click the first clip, Copy, select the others, right-click, Paste Attributes). The warm tint and grain still go on the layer.
5. Warm and fade, **Path A, Premiere 2026 with the Lumetri Color effect** (NOT VERIFIED on 2026, long-standing layout): select the layer, click the **Color** workspace (top bar), open **Lumetri Color**. **Basic Correction**: **Temperature** about +25, **Contrast** about -8, **Blacks** about +12 (raising Blacks lifts them), **Saturation** about 105. **Creative** tab: **Faded Film** about 20, Intensity unchanged. **Vignette** section at the bottom of the Creative tab: **Amount** about -1.0, **Midpoint** about 50, **Feather** about 60. Change one slider at a time, look at the **Waveform** (Window, Lumetri Scopes) so the lowest values sit around 5 to 8 percent, not at zero, and the highest do not clip.
   **Path B, either version, classic effects** (NOT VERIFIED on both): in **Effects** search **Color Balance** (or **Three-Way Color Corrector**), push the midtone and highlight balance toward orange (red up, blue down); **Brightness & Contrast** for Contrast about -8; no black lift slider in Brightness and Contrast, so lift blacks with the **Levels** effect (Output Black about 18 out of 255). Vignette: skip, or draw an Ellipse Mask feathered 150 on a Brightness & Contrast copy set to -25 with the mask inverted.
   **Path C, Premiere 2027 Color mode**: Lumetri is gone and I have not seen the real screen. Exact names NOT VERIFIED, so do the same moves by function (warm the temperature, drop contrast, lift the shadow floor, faded film, small vignette), and send a screenshot of the Color tab so head-editor can write real clicks. Do not stack Lumetri and Color mode on the same clip (Style Sheet staff warning).
6. Grain: do not rely on an effect name. Put a film grain overlay clip on the track above the adjustment layer from the owned kit (media-manager to give the path under `P:\Tools`, I did not search it), set its **Blend Mode** (Effect Controls, Opacity, Blend Mode) to **Overlay** or **Soft Light**, **Opacity** 20 to 30 percent, same length as the layer, same Crop Left and Right 12.5 percent. Heavy means visible in the 4.5 s frame at full size; if the ball and boots turn to mush, drop to 15.
7. Check the older man: no black tee. Check R3b when it exists.
8. Compare to the saved baseline: Program monitor, **Comparison View** (button under the monitor, NOT VERIFIED name on 2027), reference frame = the V4 4.5 s frame of the ffmpeg rough. One change at a time.
9. Skin check: nothing here has a face in memory (hands and boots only), so the Vectorscope skin line check applies to present beats only: do not push the warm look onto V1 or the 9:16 face frames.

## B. R3 to R3b alignment and Cross Dissolve (when R3b exists)
Stand-in plan from the brief: 1.5 s crossfade, R3b holds 1.0 s. A true crossfade, not motion interpolation (ffmpeg minterpolate snapped on unlike images in the morph test, xfade=fade was clean, xfade=dissolve was a grainy pixel dissolve). In Premiere, **Cross Dissolve** is the plain blend (NOT VERIFIED on 2027).
1. Make R3b the same pixel size as R3 (768 or 848 wide) when it is generated. If the sizes differ, set **Scale** in Effect Controls until their widths match, before aligning.
2. Put R3 on V1 and R3b on V2 directly above it. Slide R3b so it starts 1.5 s before R3 would end (R3 3.0 s from 6.5 s, so R3b starts at 9.5 s on the timeline, R3 runs to 11.0 s, R3b holds to 12.0 s).
3. Click R3b. **Effect Controls**, **Opacity**, set **50 percent**. Both pictures now show through each other (onion skin).
4. Zoom the Program monitor to 200 percent (the zoom menu under the monitor, shows **Fit**) and look at the wrench. Click **Motion**. Change **Position** first (two numbers, x then y) in steps of 1 or 2, one number at a time, until the wrench shaft and the bottom jaw of R3b sit exactly on R3's. Then **Scale** in steps of 0.5 if the wrench length is off. Do not use Rotation unless the wrench angle differs (the brief says vertical in both). Match the **wrench**, the **caged lamp** (upper right) and the **rolled blue sleeve**; the two lower hands are SUPPOSED to differ.
5. Extra check (NOT VERIFIED name on 2027): set R3b's **Blend Mode** (under Opacity) to **Difference** at 100 percent. Where the pictures match, the frame goes black. The wrench shaft should be darkest. Set Blend Mode back to **Normal** after.
6. Set **Opacity** back to **100**. Do not use the 50 percent for the final.
7. **Effects** panel, search **Cross Dissolve**, drag it to the start of R3b on V2. Double-click the transition, set **Duration** to 00:00:01:12 (1.5 s at 24 fps, 36 frames), **Alignment** Start at Cut. NOT VERIFIED dialog layout. Option with more control: skip the transition, keyframe Opacity 0 at the R3b start to 100 after 36 frames with **Ease Out**, so the arriving young hand settles. My pick: the transition first, keyframes only if the dissolve looks mechanical.
8. Move the playhead to the midpoint of the dissolve and freeze on it. You should see ONE wrench and ONE lamp. A double wrench means step 4 is off by a few pixels.
9. The slow push must not slide the two pictures apart: right-click R3 and R3b together and pick **Nest**, then keyframe **Scale** 100 to 108 on the nest, not on the pictures (the push then moves them as one). Do the push after the alignment is final.
10. The R3 to R3b dissolve sits inside the memory adjustment layer, so both get the same grade. Sound X1 (single wrench clink at the midpoint, 10.25 s in the cue sheet) is a plan only, not heard.

## C. Cut-hiding notes
- 3.0 s, V1 to V4, 1.0 s dissolve: the ratchet tail S4 must be gone before 2.95 so no present sound leaks into the dream. Cut on action: V1 ends mid-turn. Fine.
- 6.5 s, V4 to R3: add the 8 frame dissolve (note 6) and let the reverb tail overlap into R3 so the ear arrives before the eye (a short J-cut, M3 in the cue sheet).
- 12.0 s, R3b to V1: HARD cut. The change of world is the point. Bring the present air bed (A2) in about 6 frames before the picture cut (J-cut); not heard. If V1 3.2 starts after the arm has already dropped, back the in-point to about 3.0 to catch the motion (cut on action); I did not view those frames.
- 28.0 s, slate to R5 and 30.5 s R5 to R1: two stills in a row, both vertical on blur (6.5 s of stills). The duffel set-down U1 lands on the cut (sound hides the cut). Vary the push direction between R5 (push in) and R1 (push in, slow): make R5 push slightly sideways, or R1 start wide, so the two moves do not feel the same.
- 34.5 s, R1 to V1 punch-in: cut on sound (S6 ratchet click on frame one). R1 ends on the car front, V1 shows the underside: the angle changes completely, which a click on frame one covers. Start the V1 shot punched in at 115 percent and push to 135 (note 2) so the first frame feels like arrival.
- 38.0 s: cut to black on the final chord, ratchet stops dead. Black is 3.0 s with a caption, inside the Style Sheet's under 3 s tolerance for tails (it is not a tail, it carries the line).
- 41.0 s: end card on a click placed 0.05 s before the chord (sound plan).
- Memory entry and exit are the only two grade changes in the film: keep them motivated. Do not use the memory look on anything else.

## D. Loudness export check (Style Sheet Recipe 1 plus an ffmpeg measure)
Premiere (steps 1 to 8 of Recipe 1 are NOT VERIFIED on 2026 or 2027, copied from the Style Sheet):
1. Finish the mix first. The file only has a loudness once sound exists.
2. Go to **Export** (File, Export, Media). Format **H.264**. Range **Sequence In/Out** (or whole sequence for a final).
3. **Effects** section of the export settings, tick **Loudness Normalization**, standard ITU BS.1770 (Media Encoder shows BS.1770-3), **Target Loudness -14 LUFS**, **True Peak Limit -1 dBTP**.
4. Export a test. Do not trust the dialog: measure it.

Measure (ffmpeg is on PATH, `C:\Users\kingz\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe`):
```
ffmpeg -nostats -i "<export>.mp4" -af ebur128=peak=true -f null - 2>&1 | findstr /i "I: LRA Peak"
```
Read the Summary block at the end: **I** (integrated, target -14.0, accept -15 to -13), **LRA**, **True peak** (must be at or under -1.0 dBFS). Run it on each of the four files, the 15 s files separately. Then check for a silent file: the same `ffprobe` that listed only a video stream today must list an audio stream after the mix.
If integrated reads short, do not push the Premiere target: send the music cue to the mix (wwd-sound or sound-designer owns levels) and re-export. A two-pass `loudnorm` in ffmpeg (`loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json`, then rerun with the measured values) is the free fallback; I have not tested it on this material. Two caveats: the quiet dropout at 30.5 to 38 s gets gated out of the integrated number (ebur128 ignores very quiet blocks), so a file that reads -14 may still feel soft to a viewer at that stretch (not heard), and the Style Sheet notes Adobe's own normalization bug report in a beta (Recipe 1 step 7 test export covers it).
Music proof: the working track is owned but its license is UNPROVEN, and the Pixabay pick carries a Content ID risk (music file). Do not publish on either until proof is on disk. That is the music agent's call, not mine.

## Hand-offs
- assistant-editor: notes 1, 4 (rebuild when R3b exists), 5, 6, 7, and the grade and R3b recipes.
- Zac (creative calls): note 2 (pick: stronger bookend), 3 (pick: allow V4 crop with limits), 4 H1 split (pick: yes).
- sound-designer / wwd-sound: note 8 mix levels, J-cuts in section C.
- media-manager: grain overlay path under `P:\Tools`.
- Style Sheet call B (blurred fill for WWD portrait posters) is Zac's to rule separately.
