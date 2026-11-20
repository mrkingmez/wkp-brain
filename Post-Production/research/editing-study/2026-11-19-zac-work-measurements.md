# Zac's work, measured (phase B, editor study, 2026-11-19 overnight)

Read only. Every source file was opened with ffprobe and ffmpeg; nothing was moved, renamed or written next to it. Work files: `D:\WKP\scratch\editor-study\` (measure.py, sheet.py, out\*.json, frames\*.png).

## How it was measured
- **ffprobe**: duration, size, frame rate, streams.
- **Cut detection**: ffmpeg scene score over 0.3 at 160x90. It catches hard cuts only; dissolves and Modern transitions often score under 0.3, so cut counts are a floor, not the true count.
- **Visual change (the useful number)**: every half second a 64x36 grey frame was compared to the video's median frame (the StreamYard two-shot layout dominates every review). Correlation under 0.6 = "off the two-shot" (a picture, clip, solo cam, sticker, spoiler card, opener or end card). Runs under 1 s ignored. Checked by eye on contact sheets of 25 frames for all 8 reviews (`frames\<label>_sheet.png`): every sampled off-two-shot run was a picture, clip, solo cam, card or opener; every sampled two-shot frame was the two-shot.
- **Loudness**: ffmpeg ebur128 (ITU BS.1770) integrated LUFS, loudness range (LRA), true peak; short-term loudness (3 s window) medians for the first 6 s, 6 to 15 s, the body (60 s in to 60 s from the end) and the last 20 s.
- **Dead air**: silencedetect at -45 dB, 1.5 s or longer.
- **Black**: blackdetect on the last 45 s of each review, plus a full pass on Godzilla's last 18 s.
- **Cut ratio**: final duration divided by the raw StreamYard main recording, only where the raw holds one show (mass recordings hold two shows, so no ratio).
- Nobody listened. Every sound claim here is a meter reading, not a listen.

## The 8 WWD reviews (newest first)

| Label | File (under `L:\Winter Wolfs Den review show\Raw Footage\`) | Length | Raw to final |
|---|---|---|---|
| VQ8 | `Vision Quest\Vision Quest ep 8\Vision Quest- Ep8 Is it the best MCU show to-date.mp4` | 27:47 | mass recording, n/a |
| VQ7 | `Vision Quest\EP 7\Vision Quest Review EP 7 FINAL export.mp4` | 23:56 | 42:55 raw, kept 56 percent |
| GODZ | `Godzilla Minus Zero\Godzilla Minus Zero -  Review - All Hail the King! ed.mp4` | 28:54 | 46:16 raw, kept 62 percent |
| VQ56 | `Vision Quest\Vision Quest ep 5 and 6\Vision Quest EP 5 &  6 Review-.mp4` | 28:09 | 46:25 raw, kept 61 percent |
| CLAY | `mass recording clayface and vision ep 3&4\Clayface\Clayface Review-.mp4` | 22:41 | mass recording, n/a |
| CRYS | `mass record crystal LAke Vision Quest\Crystal Lake\Crystal lake review.mp4` | 35:44 | mass recording, n/a |
| SF | `Street Fighter 2026\Street Fighter _2026_ Review - Round 1 - FIGHT! ed.mp4` | 20:47 | 65:42 raw, kept 32 percent |
| CARR | `Carrie (2026 series)\Carrie 2026 Review best show of the year.mp4` | 39:30 | 68:02 raw, kept 58 percent |

All 8: 1920x1080, 30 fps, H.264 plus AAC.

### Picture and visual rhythm

| Label | Time off the two-shot | Off-two-shot runs | Median hold | Runs over 7 s | Median two-shot stretch | Two-shot stretches over 60 s | Longest two-shot stretch |
|---|---|---|---|---|---|---|---|
| VQ8 | 13.2 % | 23 | 5.0 s | 6 | 33 s | 7 | 3:52 |
| VQ7 | 8.0 % | 12 | 6.5 s | 6 | 1:51 | 7 | 5:35 (5:48 to 11:23) |
| GODZ | 12.6 % | 23 | 5.0 s | 7 | 34 s | 7 | 4:05 |
| VQ56 | 9.3 % | 23 | 5.0 s | 4 | 1:04 | 11 | 3:40 |
| CLAY | 10.3 % | 18 | 5.0 s | 5 | 38 s | 3 | 9:55 (11:29 to 21:23) |
| CRYS | 9.0 % | 31 | 5.5 s | 4 | 24 s | 6 | 12:56 (22:18 to 35:14) |
| SF | 15.7 % | 28 | 5.0 s | 9 | 34 s | 7 | 2:44 |
| CARR | 12.2 % | 34 | 8.0 s | 26 | 47 s | 10 | 4:07 |

"Longest two-shot stretch" here counts only the body (from 30 s in to 30 s before the end). The style sheet's table counts the whole video, so a stretch that runs into the end card is longer there (VQ8 4:13, CRYS 13:13).

Read this as: Zac holds a picture about 5 s (inside his own 7 s rule) but uses few of them, and they bunch up. Between bunches the two-shot runs for minutes. In every review there are 3 to 11 stretches of more than a minute where the screen does not change. "Runs over 7 s" mostly are solo cams, clips, openers and end cards (seen on the sheets), not pictures; Carrie (made before the 7 s rule of 2026-10-19) held stills about 8 s.

Opening (frames viewed): every review opens on a Winter Wolf hook (Crystal Lake: both hosts; Carrie transcript not read). It plays over the show opener or movie visuals (VQ, GODZ, CLAY) or on Winter Wolf's own cam with a poster beside him (SF, CARR). Then it cuts to the two-shot at 11.5 s (SF), 15.0 s (VQ8), 18.5 s (VQ7, VQ56, CLAY), 20.0 s (CARR), 21.5 s (GODZ) or 22.5 s (CRYS). The hook text (from Zac's own final transcripts on L:) runs 11 to 23 s. The first line in the two-shot is a "welcome back" restart in every transcript read (VQ8, VQ7, VQ56, CLAY, CRYS, SF, GODZ). Restart spans from the transcript timestamps: VQ8 0:15 to 0:28, VQ7 0:18 to 0:33, VQ56 0:18 onward ("we're back in the chairs"), CLAY 0:18 to 0:36, CRYS 0:23 to 0:42 (19 s), SF 0:11 onward, GODZ 0:21 onward. Only CRYS is quoted as a length in the style sheet.

Things seen on the sheets (viewed, not measured):
- Strong show kit: Vision Quest opener and "VISIONQUEST" title, Wolfie Award Nominee sticker (VQ7), Recommend Watch stamp (VQ8), spoiler alert card in 6 of 8, terminal "Next review" card (VQ56), "Thanks for watching" end card (VQ8, VQ7, VQ56, CLAY, GODZ), red arrow callout (VQ56).
- Street Fighter carries a fighting-game health bar overlay with WOLF and KINGZ P2 for the whole review plus a "2 HITS COMBO!" card: the most committed theme of the 8.
- Pictures are contain-fit with black bars (portrait posters pillarboxed, 2.39 stills letterboxed). Correct per the never-crop rule, but large black areas on posters (Akuma, Dan, Guile in SF; Ultron in VQ8).
- Solo cams: StreamYard individual cams used full frame (Winter Wolf room and King-Z dark room), in VQ8, VQ7, VQ56, GODZ, CLAY, CRYS, SF, CARR.
- Crystal Lake: a StreamYard caption tag "Well.... That was weird." sits under King-Z's name in every two-shot frame sampled from 0:53 to 34:50 (left on for the whole recording).

### Rule checks found by measurement
- **Godzilla: the same picture appears twice**, at 25:36.8 and 26:15.0 (64x36 frames correlate 0.99999). Breaks the no-repeat rule (2026-10-19).
- **Godzilla ends on 10.5 s of black** (28:43.1 to 28:53.6) with 8.8 s of silence after the end card. Other endings: 1.1 to 2.5 s of black (VQ8, VQ7, VQ56, CLAY), none on CRYS, SF, CARR.

### Sound (meters only, not heard)

| Label | Integrated | True peak | LRA | First 6 s | 6 to 15 s | Body median | Last 20 s | Silences 1.5 s+ |
|---|---|---|---|---|---|---|---|---|
| VQ8 | -21.2 LUFS | +0.1 dBTP | 7.8 LU | -15.5 | -16.2 | -22.7 | -26.8 | 2 (3.6 s) |
| VQ7 | -22.8 | -1.7 | 7.2 | -25.4 | -24.5 | -24.1 | -22.7 | 2 (3.3 s) |
| GODZ | -24.7 | -2.4 | 7.8 | -20.2 | -23.8 | -26.3 | -32.8 | 1 (8.8 s, the end) |
| VQ56 | -23.0 | -2.2 | 7.5 | -20.8 | -21.3 | -24.4 | -24.7 | 2 (6.8 s) |
| CLAY | -23.3 | +0.9 | 7.0 | -23.6 | -25.0 | -24.3 | -32.2 | 2 (3.6 s) |
| CRYS | -20.5 | -0.3 | 7.2 | -20.6 | -20.2 | -21.8 | -21.5 | 3 (6.0 s) |
| SF | -20.6 | +1.6 | 7.1 | -20.8 | -21.1 | -21.9 | -24.5 | 0 |
| CARR | -21.5 | +1.0 | 7.8 | -20.2 | -23.2 | -23.1 | -21.1 | 9 (20.5 s) |

Read this as: (1) integrated loudness sits between -20.5 and -24.7 LUFS, 4 dB apart from video to video; (2) 4 of 8 have a true peak above 0 dBTP, which can clip after YouTube re-encodes; (3) the intro level jumps around: VQ8's first 15 s is about 7 LU louder than its talk, VQ7's is about 1 LU quieter; (4) dead air is almost gone (0 to 3 silences in 7 of 8, Carrie 9): Zac trims pauses well.

Second dead-air pass (2026-11-20, after head-editor noted -45 dB is blind to room tone): silencedetect at -35 dB, 1.0 s or longer: SF 4, VQ7 9, CLAY 12, GODZ 18, VQ8 19, CRYS 20, VQ56 21, CARR 32.

## Samples outside WWD (read only)

| Label | File | Length, shape | Hard cuts (scene 0.12) | Integrated | True peak | LRA | Seen on sheet |
|---|---|---|---|---|---|---|---|
| P_MILD | `P:\01 Warrior King Productions\02 Video Project\Coming Soon\Final\Mild.mp4` (2025-10-28) | 1:58, 1080x1920 vertical | 5 | -30.9 LUFS | -14.6 | 3.9 | FrostCast horror picks short: King-Z cam plus poster cards in a branded frame |
| P_DERRY | `...\Coming Soon\Final\King-z Message about Welcome to Derry.mp4` | 2:50, 1920x1080 | 0 | -18.0 | -0.4 | 6.6 | one continuous take to camera (not viewed beyond probe) |
| E_LADIES | `E:\01 Warrior King Productions Archive\Ladies night promo video 2022\Final\Ladies night Promo.mp4` (2022) | 0:40, 1920x1080, 59.94 fps | 29 (about 1.4 s a shot) | -7.9 | +0.6 | 4.5 | event promo: split screens, kinetic text, stage and crowd shots, register card |
| E_FATHERS | `E:\...\Father's Day Video\Final\Father;s Dat 2022.mp4` (2022) | 2:15, 1080x1920 vertical | 24 (about 5.6 s a shot) | -12.1 | +3.0 | 13.7 | "Same Shirt Prank" title card, phone footage, group photo end |

E: was opened read only (ffprobe and frame grabs). P:\Warrior King Productions is empty. P:\WWD Kit holds kit pieces (cards, openers), not finished edits; it was listed, not measured.

## What could not be measured or opened
- Nothing failed to open. A Knight's Tale and Vision Quest EP 8 raw mass recording were not used (no single-show raw).
- Retention: no YouTube retention data was pulled (VidIQ off, no new pull). Any retention claim in the style sheet comes from the pro sources, not from Zac's channel.
- The cut detector misses dissolves; transition counts were not measured.
- Speech pace (words per minute) was not measured.
