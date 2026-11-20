# A Knight's Tale prep stringout v1: QA report, 2026-11-19

QA by qa-media (readiness pass for Jarvis). Measured, nothing edited. v1 untouched, no v2 needed.

**VERDICT: PASS.** 36 of 36 stops PASS, 0 FAIL. No FIX NEEDED.

## 1. ffprobe (v1)

| Item | Measured | Plan says | Result |
|---|---|---|---|
| Codec / profile | h264 High | H.264 | PASS |
| Resolution | 1920x1080 | 1920x1080 | PASS |
| r_frame_rate / avg | 30/1 and 10123776/337459 (30.000) | 30 fps | PASS |
| pix_fmt | yuv420p | yuv420p | PASS |
| Duration | 2196.998698 s (36:37.0) | 2196.9987 s | PASS |
| Frames (counted) | 65910 | 65,910 | PASS |
| Audio streams | 0 | none | PASS |
| Size / bitrate | 65,554,765 bytes, 238,706 b/s | 65.55 MB | PASS |

## 2. Black and freeze detection (whole file)

- blackdetect (d=0.2, pic_th=0.98): 36 black spans, 1985.8 s of 2197 s (90.4 percent). **All 36 sit in the gaps between stops (by design, the file is a black-background overlay for Screen blend). Zero black frames inside any of the 36 stop windows.** First span 0 to 14 s, last 2031.998 to 2196.965 s (after stop 47, to end of file).
- freezedetect (n=-60dB, d=1 s): 107 freeze spans. **72 sit inside picture stop windows (intended still holds, split into 1 s pieces by the detector), 35 sit inside black gaps (a black frame is a still; expected). 0 are anywhere else. Zero freezes inside the 5 clip stops (all five clips are moving video).**
- Problem spans: none.

## 3. All 36 stops

Method: whole file decoded to 64x36 grayscale (all 65,910 frames, `D:\WKP\scratch\akt-qa\all64.raw`). Source pictures composited on black and contain-fit to 1920x1080 then reduced the same way; source clips use frame at 3.0 s into the clip, compared to the stringout 3.0 s after the stop start. Score = mean abs diff (MAD, 0 to 255, STOP-tag corner masked) and correlation. Each stop was also compared against all 36 sources and had to match its own best. Landing = first and last frame of the contiguous run matching the source (pictures) or non-black (clips). Run-sheet time = the stop's header start in the run sheet; plan time = In column of the plan table. All times MM:SS.\n
| Stop | Type | Plan in | Run sheet in | Landed in | Landed out | Run sheet out | Delta in (s) | Source file | MAD | Corr | Best match is own file | Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | picture | 00:14.00 | 00:14.00 | 00:14.00 | 00:20.00 | 00:20.00 | +0.00 | 01 poster.png | 0.1 | 1.000 | yes | PASS |
| 5 | picture | 02:19.00 | 02:19.00 | 02:19.00 | 02:25.00 | 02:25.00 | +0.00 | 02 william the fake knight.png | 0.2 | 1.000 | yes | PASS |
| 6 | picture | 02:29.00 | 02:29.00 | 02:29.00 | 02:33.00 | 02:33.00 | +0.00 | 03 director helgeland.png | 0.2 | 1.000 | yes | PASS |
| 7 | picture | 02:33.00 | 02:33.00 | 02:33.00 | 02:39.00 | 02:39.00 | +0.00 | 04 the cast.png | 0.2 | 1.000 | yes | PASS |
| 8 | picture | 02:41.00 | 02:41.00 | 02:41.00 | 02:44.00 | 02:44.00 | +0.00 | 05 william and chaucer.png | 0.2 | 1.000 | yes | PASS |
| 9 | picture | 02:45.00 | 02:45.00 | 02:45.00 | 02:51.00 | 02:51.00 | +0.00 | 06 jocelyn portrait.png | 0.1 | 1.000 | yes | PASS |
| 10 | picture | 03:02.00 | 03:02.00 | 03:02.00 | 03:08.00 | 03:08.00 | +0.00 | 07 wat in pain.png | 0.2 | 1.000 | yes | PASS |
| 11 | picture | 03:55.00 | 03:55.00 | 03:55.00 | 04:01.00 | 04:01.00 | +0.00 | 08 chaucer announces.png | 0.1 | 1.000 | yes | PASS |
| 12 | picture | 04:12.00 | 04:12.00 | 04:12.00 | 04:16.00 | 04:16.00 | +0.00 | 09 the gang at the rail.png | 0.2 | 1.000 | yes | PASS |
| 13 | picture | 04:17.00 | 04:17.00 | 04:17.00 | 04:23.00 | 04:23.00 | +0.00 | 10 three musketeers.png | 0.2 | 1.000 | yes | PASS |
| 15 | picture | 05:21.00 | 05:21.00 | 05:21.00 | 05:27.00 | 05:27.00 | +0.00 | 11 ten things i hate about you.png | 0.2 | 1.000 | yes | PASS |
| 16 | picture | 06:38.00 | 06:38.00 | 06:38.00 | 06:44.00 | 06:44.00 | +0.00 | 12 seven kingdoms hedge knight.png | 0.2 | 1.000 | yes | PASS |
| 17 | picture | 06:58.00 | 06:58.00 | 06:58.00 | 07:04.00 | 07:04.00 | +0.00 | 13 peasants and buddies.png | 0.2 | 1.000 | yes | PASS |
| 18 | picture | 08:16.00 | 08:16.00 | 08:16.00 | 08:22.00 | 08:22.00 | +0.00 | 14 the first joust.png | 0.2 | 1.000 | yes | PASS |
| 20 | clip | 10:15.00 | 10:15.00 | 10:15.00 | 10:21.67 | 10:22.00 | +0.00 | AKT-clip-1-debo-heads.mp4 | 1.5 | 1.000 | yes | PASS |
| 21 | picture | 10:35.00 | 10:35.00 | 10:35.00 | 10:41.00 | 10:41.00 | +0.00 | 15 the count.png | 2.6 | 1.000 | yes | PASS |
| 22 | picture | 10:53.00 | 10:53.00 | 10:53.00 | 10:59.00 | 10:59.00 | +0.00 | 16 the splinter lance.png | 3.7 | 0.999 | yes | PASS |
| 23 | picture | 13:09.00 | 13:09.00 | 13:09.00 | 13:15.00 | 13:15.00 | +0.00 | 17 the prince.png | 1.8 | 0.999 | yes | PASS |
| 24 | clip | 15:03.00 | 15:03.00 | 15:03.00 | 15:11.00 | 15:11.00 | +0.00 | AKT-clip-2-stocks.mp4 | 1.3 | 1.000 | yes | PASS |
| 25 | picture | 15:45.00 | 15:45.00 | 15:45.00 | 15:51.00 | 15:51.00 | +0.00 | 18 treated his men.png | 1.9 | 1.000 | yes | PASS |
| 28 | clip | 20:38.00 | 20:38.00 | 20:38.00 | 20:44.37 | 20:44.00 | +0.00 | AKT-clip-3-father.mp4 | 1.2 | 1.000 | yes | PASS |
| 30 | picture | 23:39.00 | 23:39.00 | 23:39.00 | 23:45.00 | 23:45.00 | +0.00 | 19 chaucer naked.png | 3.3 | 0.999 | yes | PASS |
| 32 | picture | 24:04.00 | 24:04.00 | 24:04.00 | 24:10.00 | 24:10.00 | +0.00 | 20 roland wat and kate.png | 2.3 | 1.000 | yes | PASS |
| 33 | picture | 24:13.00 | 24:13.00 | 24:13.00 | 24:19.00 | 24:19.00 | +0.00 | 21 kate at the forge.png | 1.7 | 0.999 | yes | PASS |
| 34 | picture | 25:13.00 | 25:13.00 | 25:13.00 | 25:19.00 | 25:19.00 | +0.00 | 22 jocelyn at the banquet.png | 2.2 | 1.000 | yes | PASS |
| 35 | picture | 26:04.00 | 26:04.00 | 26:04.00 | 26:10.00 | 26:10.00 | +0.00 | 23 the ballroom.png | 2.0 | 0.999 | yes | PASS |
| 36 | clip | 26:11.00 | 26:11.00 | 26:11.00 | 26:18.17 | 26:18.00 | +0.00 | AKT-clip-4-dance.mp4 | 1.2 | 1.000 | yes | PASS |
| 37 | picture | 26:34.00 | 26:34.00 | 26:34.00 | 26:40.00 | 26:40.00 | +0.00 | 25 harden steel.png | 3.2 | 0.999 | yes | PASS |
| 39 | picture | 27:24.00 | 27:24.00 | 27:24.00 | 27:30.00 | 27:30.00 | +0.00 | 26 rip heath.png | 1.2 | 1.000 | yes | PASS |
| 40 | picture | 27:32.00 | 27:32.00 | 27:32.00 | 27:38.00 | 27:38.00 | +0.00 | 27 the joker.png | 3.2 | 1.000 | yes | PASS |
| 41 | picture | 31:11.00 | 31:11.00 | 31:11.00 | 31:15.00 | 31:15.00 | +0.00 | 28 prague set.png | 2.0 | 1.000 | yes | PASS |
| 42 | picture | 31:16.00 | 31:16.00 | 31:16.00 | 31:22.00 | 31:22.00 | +0.00 | 29 stunt armour.png | 1.1 | 1.000 | yes | PASS |
| 43 | clip | 31:25.00 | 31:25.00 | 31:25.00 | 31:31.83 | 31:32.00 | +0.00 | AKT-clip-5-joust.mp4 | 1.3 | 1.000 | yes | PASS |
| 44 | picture | 32:14.00 | 32:14.00 | 32:14.00 | 32:20.00 | 32:20.00 | +0.00 | 30 the heartthrob.png | 3.2 | 1.000 | yes | PASS |
| 45 | picture | 33:31.00 | 33:31.00 | 33:31.00 | 33:36.00 | 33:36.00 | +0.00 | 31 the crowd.png | 2.4 | 0.999 | yes | PASS |
| 47 | picture | 33:46.00 | 33:46.00 | 33:46.00 | 33:52.00 | 33:52.00 | +0.00 | 32 the romantic scene.png | 2.2 | 1.000 | yes | PASS |

Pass rule: delta in within 0.5 s of the run sheet, own source is best of 36, corr over 0.9, MAD under 12. Worst MAD 3.7 (stop 22), worst corr 0.999. Every landing in is exact to the frame (0.00 s). Landed out matches the plan out, and is within 0.5 s of the run sheet header out for all 36 (clips differ by 0.17 to 0.37 s only because the header rounds, plan uses the real file length).

## Cross-checks

- Plan In column equals run sheet header start for all 36 stops (no plan error, no line of the plan is wrong).
- Frames viewed by me: stop 22 (lance, the highest MAD, correct picture), stop 42 (stunt armour, contain-fit with black bars, STOP 42 tag), stop 47 (romantic scene, corner tag STOP 47), and 31:32 (just after clip 5 ends, black as designed). Earlier assembly report also viewed stops 7, 28, 42.
- Stringout carries a small white STOP nn tag top left (documented in the plan). It is not part of the final cut.
- The file has no audio by design, so loudness and silence checks do not apply.
- Not checked: not played through in real time, does not test Zac's real cut (no edited mp4 exists, all times are word-position estimates plus or minus 2 s, per the plan). Picture and clip choice versus the spoken line is the run sheet's job and not re-judged here. Scripts: `D:\WKP\scratch\akt-qa\qa.py`, `cls2.py`, `rep.py`. Raw results `results.json`, `detect.txt`.
