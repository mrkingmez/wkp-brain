# A Knight's Tale review: prep assembly plan and B-roll stringout v1

Built 2026-11-19 by assistant-editor (WWD practice and prep job). A prep aid for Zac. Zac is the editor and owns the cut. Wwd-run-sheet owns the run sheet (v1.1, 49 stops). Nothing in the movie folder was changed except the new `prep\` folder.

**Times are word-position estimates, plus or minus 2 s.** They are times in Zac's edited cut as the transcript shows it (cut length 36:37), copied from run sheet headers and the "to" times. If Zac cuts the 29:54 to 30:24 patch, every stop from 31:11 on moves about 30 s earlier on his timeline, but not in the stringout.

## Files

- Stringout: `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\prep\A-Knights-Tale-PREP-Stringout-v1.mp4`
- Specs (ffprobe): H.264, 1920x1080, 30 fps, yuv420p, 2196.9987 s (36:37), 65,910 frames, 65.55 MB, no audio stream.
- Frame rate choice: 30 fps. ffprobe of both StreamYard cam files returned 30/1 (1920x1080), and the run sheet says the main recording and the sequence are 30 fps. 29.97 would drift from the cams by 2 s over 36 min. The five clips are 23.976 and were conformed to 30 by ffmpeg (frame repeat), as Premiere would.
- Work files (rebuildable): `D:\WKP\scratch\akt-prep\` (parse.py reads the run sheet, render.py builds the file).

## How to use it in Premiere (6 lines)

1. **File > Import** (Ctrl+I), pick `A-Knights-Tale-PREP-Stringout-v1.mp4` from the `prep` folder, click Open.
2. Drag it from the Project panel onto **V2** and drop it with its left edge at `00:00:00:00`. If a "clip does not match sequence settings" box appears, click **Keep existing settings**.
3. Click the clip once on V2, open **Effect Controls** (Window > Effect Controls), click the arrow next to **Opacity**.
4. Click the **Blend Mode** drop-down (shows Normal), pick **Screen** (or **Lighten**). Black drops out, pictures and clips show over your cut. Pictures with see-through edges and dark shots look washed in Screen, so if one looks ghostly, try Lighten or set Blend Mode back to Normal for that part only.
5. Scrub with the small white "STOP nn" tag top left, it matches the stop number in the run sheet. Hide the tag by cropping later, or just cut the stringout away at each stop.
6. Press **C** (Razor), click the V2 stringout at the start and end of each stop you want, press **V**, click the pieces you do not want, press **Delete**. Use the real PNGs and clips from the run sheet for the final, this file is a preview, not for export.

## Assembly table (36 visual stops: 31 pictures, 5 clips)

| Stop | In | Out | Hold | Source file | Type | Motion | Transition (run sheet) |
|---|---|---|---|---|---|---|---|
| 1 | 00:14 | 00:20 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\01 poster.png` | picture | none | Cross Dissolve 24f |
| 5 | 02:19 | 02:25 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\02 william the fake knight.png` | picture | none | Film Dissolve 12f |
| 6 | 02:29 | 02:33 | 4.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\03 director helgeland.png` | picture | none | hard cut |
| 7 | 02:33 | 02:39 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\04 the cast.png` | picture | none | Pop Motion Impacts 10f |
| 8 | 02:41 | 02:44 | 3.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\05 william and chaucer.png` | picture | none | hard cut |
| 9 | 02:45 | 02:51 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\06 jocelyn portrait.png` | picture | none | Glow Impacts 12f |
| 10 | 03:02 | 03:08 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\07 wat in pain.png` | picture | none | hard cut |
| 11 | 03:55 | 04:01 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\08 chaucer announces.png` | picture | none | Light Sweep Impacts 12f |
| 12 | 04:12 | 04:16 | 4.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\09 the gang at the rail.png` | picture | none | Push Impacts 10f |
| 13 | 04:17 | 04:23 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\10 three musketeers.png` | picture | none | hard cut |
| 15 | 05:21 | 05:27 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\11 ten things i hate about you.png` | picture | none | Chaos Impacts 10f |
| 16 | 06:38 | 06:44 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\12 seven kingdoms hedge knight.png` | picture | none | Film Dissolve 12f |
| 17 | 06:58 | 07:04 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\13 peasants and buddies.png` | picture | none | Slide Impacts 10f |
| 18 | 08:16 | 08:22 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\14 the first joust.png` | picture | none | Travel Motion Impacts 12f |
| 20 | 10:15 | 10:21.67 | 6.67 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\clips\AKT-clip-1-debo-heads.mp4` | clip | none (muted clip) | hard cut in |
| 21 | 10:35 | 10:41 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\15 the count.png` | picture | none | hard cut |
| 22 | 10:53 | 10:59 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\16 the splinter lance.png` | picture | none | Slice Impacts 10f |
| 23 | 13:09 | 13:15 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\17 the prince.png` | picture | none | Film Dissolve 12f |
| 24 | 15:03 | 15:11.01 | 8.01 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\clips\AKT-clip-2-stocks.mp4` | clip | none (muted clip) | hard cut in |
| 25 | 15:45 | 15:51 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\18 treated his men.png` | picture | none | Frame Impacts 12f |
| 28 | 20:38 | 20:44.38 | 6.38 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\clips\AKT-clip-3-father.mp4` | clip | none (muted clip) | hard cut in |
| 30 | 23:39 | 23:45 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\19 chaucer naked.png` | picture | none | Spring Motion Impacts 10f |
| 32 | 24:04 | 24:10 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\20 roland wat and kate.png` | picture | none | hard cut |
| 33 | 24:13 | 24:19 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\21 kate at the forge.png` | picture | none | Plateau Wipe Impacts 12f |
| 34 | 25:13 | 25:19 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\22 jocelyn at the banquet.png` | picture | none | Film Dissolve 12f |
| 35 | 26:04 | 26:10 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\23 the ballroom.png` | picture | none | Luma Fade Impacts 12f |
| 36 | 26:11 | 26:18.17 | 7.17 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\clips\AKT-clip-4-dance.mp4` | clip | none (muted clip) | hard cut in |
| 37 | 26:34 | 26:40 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\25 harden steel.png` | picture | none | Block Motion Impacts 10f |
| 39 | 27:24 | 27:30 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\26 rip heath.png` | picture | none | Cross Dissolve 24f |
| 40 | 27:32 | 27:38 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\27 the joker.png` | picture | none | hard cut |
| 41 | 31:11 | 31:15 | 4.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\28 prague set.png` | picture | none | Film Dissolve 12f |
| 42 | 31:16 | 31:22 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\29 stunt armour.png` | picture | none | Mirror Impacts 12f |
| 43 | 31:25 | 31:31.84 | 6.84 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\clips\AKT-clip-5-joust.mp4` | clip | none (muted clip) | hard cut in |
| 44 | 32:14 | 32:20 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\30 the heartthrob.png` | picture | none | Flare Impacts 12f |
| 45 | 33:31 | 33:36 | 5.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\31 the crowd.png` | picture | none | hard cut |
| 47 | 33:46 | 33:52 | 6.00 s | `L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\32 the romantic scene.png` | picture | none | Blur Dissolve Impacts 14f |

Clip "out" is the in time plus the file's own length (ffprobe). Picture "out" is the run sheet's "to" time. "Motion: none" because the run sheet asks for no push-ins or zooms on any picture, and clips play as cut. Stringout transitions: all hard cuts. The run sheet's dissolves and Modern transitions are NOT in the stringout, they are Zac's to add in Premiere.

## Totals

- Pictures: 31 placements, 31 different files, 176 s on screen. Longest hold 6 s (limit 7 s, kept).
- Clips: 5, 35.07 s total (matches the run sheet's 35.08 s), muted.
- Picture plus clip time: 211 s of 2197 s, 9.6 percent of the runtime.
- Not in the stringout by design: 4 solo CAM stops (stops 4, 26, 27, 48), 2 stickers (19, 46), 5 sound-only stops, optional logo sting (stop 2), outro music (49), picture 24 (held back by the run sheet).

## Gap list

- **Missing files:** none. All 31 USE pictures and 5 clip cut files were opened by ffmpeg and rendered. Picture 24 (`24 she takes over.png`) exists on disk and is unplaced on purpose (run sheet, Gaps and flags).
- **Time unclear:** every time is a word-position estimate (plus or minus 2 s). The run sheet flags stop 48 (cam, start "check by ear") and the 6:32 and 29:54 editor cues. The cam in and out times (stops 4, 26, 27, 48) are cut times and the cams are not confirmed synced.
- **Stringout limit:** it follows run sheet v1.1 as read today. If wwd-run-sheet revises a time, rerun `render.py` (about 2 minutes).
- **Run sheet lines past 318 were not read.** The file is 408 lines, I read stops 1 to 49, the transition map and the Gaps and flags section only. Anything after that (Still open list) was not read.

## Visual gaps over 20 s (no picture, clip or cam on screen)

Counted against pictures, clips and the four cams. Stickers are not counted as a change of shot.

- 00:20 to 01:12 (52 s)
- 01:26 to 02:19 (53 s)
- 03:08 to 03:55 (47 s)
- 04:23 to 05:21 (58 s)
- 05:27 to 06:38 (71 s)
- 07:04 to 08:16 (72 s)
- 08:22 to 10:15 (113 s)
- 10:59 to 13:09 (130 s)
- 13:15 to 15:03 (108 s)
- 15:11.01 to 15:45 (34 s)
- 15:51 to 16:22 (31 s)
- 16:33 to 18:57 (144 s)
- 19:12 to 20:38 (86 s)
- 20:44.38 to 23:39 (175 s)
- 24:19 to 25:13 (54 s)
- 25:19 to 26:04 (45 s)
- 26:40 to 27:24 (44 s)
- 27:38 to 31:11 (213 s)
- 31:31.84 to 32:14 (42 s)
- 32:20 to 33:31 (71 s)
- 33:52 to 34:19 (27 s)
- 34:31 to 36:37 (126 s)

## Self-check

- Done: ffprobe of the output (above). Frames pulled and viewed at 3 stop times: stop 7 at 02:36 (cast group photo, tag STOP 07), stop 28 at 20:41 (clip 3, bearded man with net, tag STOP 28), stop 42 at 31:20 (museum armor case, contain-fit with black side bars, tag STOP 42). All three are the right picture at the right time.
- Frame grabs: `D:\WKP\scratch\akt-prep\f_stop07.png`, `f_stop28.png`, `f_stop42.png`, `f_gap.png` (a black gap frame at 16:40).
- Not checked: the other 33 stops (rendered from the same code, not viewed), the file was not played through, no audio exists to check, I cannot hear audio, Premiere Screen blend look not tried (Premiere not run), nothing checked against Zac's real cut because no edited mp4 exists on disk.

## Head-editor notes (viewed frames for stops 7, 28, 42 only; not the other 33 stops, audio or Zac's real cut)

1. CLEAR FIX candidate, pacing: 22 stretches over 20 s with no picture, clip or cam. Worst: 27:38 to 31:11 (213 s), 20:44 to 23:39 (175 s), 16:33 to 18:57 (144 s), 10:59 to 13:09 (130 s), 34:31 to the end (126 s). Pictures plus clips are 9.6 percent of the runtime by the plan's own count. Fill the worst five first with a 7 s cutaway (no repeats) or a cam change, placed where the hosts name a scene or person. Picture 24 is unused and sits near the 20:44 to 23:39 stretch (assistant-editor note: run sheet says it duplicates clip 4, so it is wwd-run-sheet's and Zac's call). No music under talk.
2. CREATIVE CALL for Zac: how many solo cam cuts and where. Only 4 are planned (stops 4, 26, 27, 48). Head-editor's pick: cams for the 27:38 and 20:44 gaps. A sixth clip is also an option. Not applied.
3. Stop 42 (stunt armour): vertical phone photo, black side bars, flash glare, small placard. Contain-fit is correct and kept. Option for Zac: blurred copy behind it, or swap in a cleaner armour still. CREATIVE CALL, not applied. Holds are fine (longest 6 s, all 31 files different).
4. Check: cutting the 29:54 to 30:24 patch moves every stop from 31:11 on about 30 s earlier.
