# Ian "The Wrench Turner" trailer, Draft 3.3: rough assembly v3 and Premiere build guide (assistant-editor, 2026-11-20)

Silent rough assembly, built by ffmpeg from assets on disk. Nothing heard (no audio exists in these files). Beat sheet: "REVISED beat sheet v2" in `2026-11-20-brief-draft3-3.md`. No credits spent, nothing generated, nothing sent. Build script: `D:\WKP\scratch\ian\v3\build_v3.py` (work files in `D:\WKP\scratch\ian\v3\`).

## 1. Output files (all in `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\`, no v1 or v2 file touched)
Measured with ffprobe, frames counted:
| File | Size | fps | Frames | Duration |
|---|---|---|---|---|
| Ian-Trailer-D33-45s-16x9-v3-silent.mp4 | 1920x1080 | 24 | 1080 | 45.000 s |
| Ian-Trailer-D33-45s-9x16-v3-silent.mp4 | 1080x1920 | 24 | 1080 | 45.000 s |
| Ian-Trailer-D33-15s-16x9-v3-silent.mp4 | 1920x1080 | 24 | 360 | 15.000 s |
| Ian-Trailer-D33-15s-9x16-v3-silent.mp4 | 1080x1920 | 24 | 360 | 15.000 s |

Contact sheets (viewed): `D:\WKP\scratch\ian\v3\sheet45_16x9.png`, `sheet45_9x16.png`, `sheet15_16x9.png`, `sheet15_9x16.png`.

## 2. Beat table, 45 s (ROOT = `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\`)
| # | Timeline | Source | In to out | Move | Grade note | Placeholder |
|---|---|---|---|---|---|---|
| 1 | 0:00.0-3.0 | ROOT\Raw Footage\V1.mp4 | 0.0-4.0 (last 1.0 s sits under the dissolve) | none. 9:16: 4:5 window pans 0.55 to 0.65 across the clip | none | CAPTION SLOT 0.3-2.8 (hook line, writing room) |
| 2 | 0:03.0-6.5 | ROOT\Raw Footage\V4.mp4 | 0.8-4.3 | 1.0 s xfade=fade from beat 1 starting at 3.0. 16:9: 4:3 window (crop 1440x1080, x offset 160 to keep the ball) pillarboxed. 9:16: 4:5 window shrunk to 90 percent (972 wide) | MEMORY: warm (red up, blue down), contrast down, blacks lifted, heavy grain, vignette | none |
| 3 and 4 | 0:06.5-12.0 | ROOT\Pictures\R3.png | still, held 5.5 s | slow push 6 percent. 16:9: 608x1080 still centered in a 1440x1080 blurred box, pillarboxed. 9:16: inset 972x1742 over blurred dark bg | MEMORY look as beat 2 | CAPTION SLOT 7.0-9.2 (Wrench Turner caption). Label "R3b morph goes here" 9.5-12.0. Beats 3 and 4 are one held R3 because R3b does not exist |
| 5 | 0:12.0-16.0 | V1 | 3.2-7.2 | none. 9:16 pan 0.62 to 0.68 | none | none |
| 6 | 0:16.0-22.0 | H1 | NEED | dark slate (0x1c1c1c), white text "H1 HOMECOMING - NEED" | none | whole beat is placeholder |
| 7 | 0:22.0-25.0 | B1 | NEED (only with Ian's yes) | slate "B1 BROTHERHOOD - NEED" | none | whole beat. If Ian says no, H1 takes the 3 s |
| 8 | 0:25.0-28.0 | W1 | NEED | slate "W1 SWEETHEART - NEED" | none | whole beat |
| 9 | 0:28.0-30.5 | ROOT\Pictures\Photograph of a scarred wooden w 704265 zpe.png (R5) | still 2.5 s | push 7 percent. 16:9 fg 608x1080 over blurred bg, 9:16 full frame | none | none |
| 10 | 0:30.5-34.5 | ROOT\Pictures\R1.png | still 4.0 s | slow push 10 percent, centered. No door motion | none | none |
| 11 | 0:34.5-38.0 | V1 | 0.0-3.5 | punch-in to 120 percent, static crop on the hands (16:9 crop 1600x900 at x 460, y 4; 9:16 window 720x900 at x 907, y 4) | none | none |
| 12 | 0:38.0-41.0 | black | 3.0 s | none | none | CAPTION SLOT 38.5-40.5 (final line, script-room decides wording) |
| 13 | 0:41.0-45.0 | ROOT\Client info to create this book Trailer\book cover.jpg | 4.0 s | contain-fit, no push, never cropped. 16:9 cover 720x1080 left of center, text right. 9:16 cover 800x1200 with text under | none | "AVAILABLE NOW", "[buy link]" placeholder |

Sum: 3.0 + 3.5 + 5.5 + 4.0 + 6.0 + 3.0 + 3.0 + 2.5 + 4.0 + 3.5 + 3.0 + 4.0 = 45.0 (the 1.0 s dissolve overlaps beats 1 and 2, so beat 1 plus 2 is 6.5 s on the timeline).

## 3. Beat table, 15 s
| Timeline | Source | In to out | Note |
|---|---|---|---|
| 0:00-3.0 | V1 | 0.0-4.0 | CAPTION SLOT 0.3-2.8 (hook) |
| 0:03-5.5 | V4 | 1.5-4.0 | 1.0 s dissolve at 3.0, memory look |
| 0:05.5-9.5 | R3 | still 4.0 s | memory look, CAPTION SLOT 5.7-7.3 (Wrench Turner), label "R3b morph goes here" 7.5-9.5. The brief's crossfade into R3b is not built because R3b does not exist |
| 0:09.5-12.0 | V1 | 3.2-5.7 | CAPTION SLOT 9.8-11.8 (war line, writing room) |
| 0:12-15.0 | cover | 3.0 s | end card, AVAILABLE NOW, [buy link] |

## 4. Placeholders and deviations from the brief (said plainly)
- H1, B1, W1, R3b do not exist, so they are slates. Beat 4 holds R3, no crossfade yet.
- Beats 3 and 4 in the brief were R3 (3.0 s) then R3b crossfade (2.5 s). Because R3b is missing, R3 holds the full 5.5 s.
- 15 s: crossfade window and R3b hold not built, R3 holds 4.0 s.
- In the 16:9 memory beats the 4:3 window crops the sides of V4 (the crop keeps ball and boots, checked on the sheet at 3.0 and 4.5 s). The prior rule "never crop" was about fit; this crop is a stylistic window, head-editor to rule.
- 9:16 stills are scaled to 1080 wide and trimmed 15 px of height (aspect 0.558 vs 0.5625), practically full frame. Not a meaningful crop.
- 9:16 beat 1: the man's head sits near the right edge of the 4:5 window at the start. Zac may reframe in Premiere.
- CAPTION SLOT labels are tiny gray text in the file. No real captions are burned in.
- Music, SFX: none. Not heard anything because there is nothing to hear.
- File size: crf 16 and grain make each 45 s file about 45 to 57 MB. Fine for review, not a delivery spec.

## 5. Premiere build guide for Zac
Version rule: finish in the Premiere version this project starts in (2026 or 2027). A 2027 project does not open in 2026. Every menu path below is from general knowledge of Premiere and is marked NOT VERIFIED for Zac's version unless a fact-research note says otherwise (the only confirmed fact: 2027 retired the Lumetri panel, so the grade steps below name the effects by function and are NOT VERIFIED).

### 5.1 Sequence (16:9 master first)
1. Open Premiere. File > New > Project, name it `Ian Wrench Turner D33`, save inside `ROOT\Premerir\` (NOT VERIFIED, the folder name is spelled that way on disk).
2. File > Import (Ctrl+I). Select V1, V4 from Raw Footage, R1, R3 and R5 from Pictures, book cover.jpg. Click Open.
3. Drag V1 onto the New Item icon at the bottom right of the Project panel. This makes a sequence matching the clip: 1920x1080, 24 fps. Check: Sequence > Sequence Settings shows Frame size 1920 horizontal 1080 vertical, 24 fps (NOT VERIFIED menu wording). Rename it `D33-45s-16x9`.
4. Delete the V1 clip from the timeline (it is only there to set the settings).
5. Drop clips per the beat table: V1 (in 0.0, out 4.0), V4 (in 0.8, out 4.3) and so on. Set in and out in the Source Monitor with I and O, then drag or press the Comma key to insert (NOT VERIFIED shortcut).
6. Stills: drag R3 to the timeline and set its length to 5.5 s by dragging its right edge, or right-click the clip > Speed/Duration and type 00:00:05:12 (5 s 12 frames, 24 fps) (NOT VERIFIED).

### 5.2 9:16 version (derive after the 16:9 is approved)
1. Right-click the finished sequence in the Project panel > Duplicate. Rename `D33-45s-9x16`.
2. Sequence > Sequence Settings: Frame size 1080 horizontal, 1920 vertical (NOT VERIFIED menu wording). Click OK.
3. Select all clips. For each 16:9 clip: Effect Controls > Scale and Position. To copy the rough: set Scale about 125 (this makes the 1080-high frame fill 1350 px wide 4:5 window area) and slide Position horizontally to put the wrench hands in view. Put a blurred, darkened copy of the same clip on V1 underneath (Effects: Gaussian Blur, Brightness lower, NOT VERIFIED names) scaled to fill 1920 high.
4. Stills R1, R3, R5 are vertical: Effect Controls > Scale about 140 so they fill the 1080x1920 frame.

### 5.3 The R3 to R3b crossfade (when R3b exists)
1. Put R3 on V1 and R3b on V2 directly above it, overlapping 1.5 s, starting 9.5 s on the timeline.
2. Click the R3b clip on V2. Open Effect Controls. Under Opacity, set the value to 50 percent.
3. Line the wrench up: with R3b selected, in Effect Controls adjust Position (x, y numbers) and Scale until the wrench shaft in R3b sits exactly over the wrench shaft in R3 (look for the jaw at the bottom center). Type small changes into the numbers, one at a time. Keep the older man's rolled blue sleeve in the same upper right spot.
4. When aligned, set Opacity back to 100 percent.
5. Effects panel, search Cross Dissolve, drag it onto the start of the R3b clip on V2 (the edge where it begins). Double-click the dissolve on the timeline and set Duration to 00:00:01:12 (1.5 s). (NOT VERIFIED exact dialog layout.)
6. R3b then holds 1.0 s. Delete the "R3b morph goes here" label (it is baked into my rough only, not into Premiere).

### 5.4 The memory grade (V4, R3, R3b)
Do this on an Adjustment Layer so it is one place to change. Premiere 2027 retired the Lumetri panel (confirmed by fact-research) so the effect names below are NOT VERIFIED in either version; head-editor to confirm the recipe before QA.
1. Project panel: New Item > Adjustment Layer. Drag it above V4, R3 and R3b on the timeline, covering exactly those clips.
2. Color: warm it. Raise Temperature toward orange a little (about +20) or lower blue slightly. Reduce Contrast a touch and lift the black point so blacks go to dark gray (the lifted blacks give the "slight fade"). My ffmpeg values for reference: red x1.07, blue x0.84, saturation x1.05, contrast x0.93, blacks lifted to 7 percent.
3. Grain: add a film grain effect or overlay a grain clip from `P:\Tools` (NOT VERIFIED which pack) at Overlay or Soft Light blend, 20 to 30 percent.
4. Vignette: a small amount.
5. Narrow frame in 16:9: set each memory clip's Crop (or Scale to 4:3 window) so it is 1440 wide inside 1920, black on both sides. Easiest: Effects > Crop, set Left and Right to 12.5 percent each.
6. Keep the older man out of Brandon's black tee (fence rule): nothing to do on R3 as it is, check on R3b when made.

### 5.5 The punch-in (beat 11)
1. Select V1 on the timeline (the 0.0-3.5 piece).
2. Effect Controls > Motion > Scale: set 120.
3. Position: move until the hands and wrench sit near the middle (about x 1267 of 1920, y 454 before scaling). Type values until it looks right. Drag the Program monitor to check.
4. 16:9 only. In 9:16 the punch is already a 4:5 window at 120 percent.

### 5.6 Beat 2 dissolve
Effects > Video Transitions > Dissolve > Cross Dissolve onto the join between V1 and V4. Set Duration 1 s (00:00:01:00). In ffmpeg I used a plain fade, not the pixel dissolve. In Premiere, Cross Dissolve is the plain blend. (NOT VERIFIED folder path.)

### 5.7 End card
Cover contain-fit: Scale so the whole cover shows, never cropped, no push. Text: AVAILABLE NOW and the real buy link (waiting on Ian; check the link on a phone first, per TASKS). Words come from script-room.

### 5.8 Export for review
File > Export > Media (Ctrl+M), Format H.264, match sequence settings (NOT VERIFIED).

## 6. Not verified
- I did not hear or play any of the files. Frames only, from the contact sheets.
- Premiere steps: not tested in Zac's version.
- Whether head-editor likes the 4:3 crop, the grain level, or the CAPTION SLOT label size.
- No license proof for music (none used here).

## 7. v4 changes (2026-11-20, applies head-editor notes with studio-director rulings; v3 notes above kept)
Files (silent, no captions): `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-D33-45s-16x9-v4-silent.mp4`, `...-45s-9x16-v4-silent.mp4`, `...-15s-16x9-v4-silent.mp4`, `...-15s-9x16-v4-silent.mp4`. Script `D:\WKP\scratch\ian\v4\build_v4.py`. v1, v2, v3 untouched.
Measured with ffprobe: 45 s files 1080 frames (45.000 s), 15 s files 360 frames (15.000 s), 24 fps, 1920x1080 and 1080x1920.
1. 16:9 stills R1, R3, R5 now share one fill recipe: blurred, darkened copy behind the contain-fit still (gaussian sigma 50, brightness -0.28). R3 keeps the 1440 px memory window with pure black bars. Measured luma at 8.0 s: fill 9 of 255, bars 0, so the R3 fill is present but dark because the still itself is dark.
2. Beat 11 (34.5 to 38.0 s): V1 now starts at 0.6 s and the punch animates 115 to 135 percent over 3.5 s (16:9 and 9:16). Head and wrench in frame at 34.6, 36.0 and 37.9 s.
3. V4 memory window: static crop moved from x 160 to x 0, because the ball enters from the left and was clipped by the old window at about 1.6 s. Checked 10 frames from V4 0.8 to 4.4 s: ball and both boots inside. The ball enters from the source's left edge near 1.2 s, so it is not whole before that.
4. R3 push 6 to 8 percent (all four files). R3 hold is now 5.667 s in the 45 s (includes the dissolve overlap).
5. H1 split: slate H1a (3.5 s, wide push) and H1b (2.5 s, tight reframe), hard cut between, 16:9 and 9:16, 45 s only.
6. 9:16 beat 1 pan 0.80 to 0.88 (both 45 s and 15 s). Head fully inside at 0.5 and 2.0 s, near the right edge.
7. V4 into R3: 8 frame dissolve centered on 6.5 s (6.333 to 6.667), V4 out extended by 4 frames (to V4 4.47 s). 15 s files: same, centered on 5.5 s. The cut from R3 back to V1 at 12.0 s stays hard.
Not applied: R5 push direction variation (head-editor C list, not in the rulings), the Premiere grade, loudness and mix notes (not mine). Observation, not changed: in the 9:16 file the V4 pan clips the right boot at about 4.5 s. Not heard, silent files.
