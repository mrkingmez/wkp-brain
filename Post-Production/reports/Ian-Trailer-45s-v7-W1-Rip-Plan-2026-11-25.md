# Ian trailer 45 s v7: W1 rip at beat 8 (assistant-editor, 2026-11-25)

Zac 2026-11-25: "Let's make it part of the big video." The W1 torn-photo rip (happy W1a rips down the middle to reveal the caught W1b) is now the beat 8 shot. Silent file, nothing generated, no credits.

## Files
- v7 45 s 16:9: `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-D34-45s-16x9-v7-with-gap-cards-silent.mp4` (v5 and v6 kept, nothing overwritten). The name says gap cards because H1a, H1b, B1 and R3b are still slates or the R3 hold.
- Rip used: `Ian-Trailer-W1-Rip-3s-16x9-v2-center-silent.mp4` (same folder, motion-graphics, 72 frames, 24 fps, 1920x1080). The v1 rip is not used.
- Builder: `D:\WKP\scratch\ian\v7\build_v7.py` (takes `--rip <file name>`, `--ripdir`).
- Rebuild when a new rip lands (v3, v2-left and so on), one line, refuses to overwrite so give a new tag: `python D:\WKP\scratch\ian\v7\build_v7.py --which 45a --rip <new file name> --tag v7b --work D:/WKP/scratch/ian/v7/work_v7b`
- If the rip file is missing the build puts a labelled 3 s slate "W1 RIP PLACEHOLDER" in the slot.
- Rip is 16:9 only. The 9:16 45 s still carries its W1 gap card (rip for 9:16 is a later render, see rip README). The 15 s cut-downs (v6) have no beat 8, so there is no 15 s change.

## Timeline v7 (24 fps, 1080 frames)
| Beat | Time | Source | Status |
|---|---|---|---|
| 1 to 3 | 0.0 to 12.0 | V1, V4 memory, R3 hold | same as v6 |
| 4 | 12.0 to 16.0 | V1 second beat | same as v6 |
| 6a, 6b | 16.0 to 22.0 | H1 | gap cards (H1 not on disk) |
| 7 | 22.0 to 25.0 | B1 | gap card (B1 not on disk) |
| **8** | **25.0 to 28.0** | **W1 rip v2-center, frames 600 to 671** | **IN, real clip** |
| 9 to 13 | 28.0 to 45.0 | R5, R1, V1 punch, black, end card | same as v6 |
Total 45.000 s, 1080 frames. v6 already had W1 at 25.0 to 28.0, so nothing else moved.

## Premiere sequence notes (beat 8)
Sequence 1920x1080, 24 fps. Zac's Premiere steps are not verified for his version, so these are placement notes, not click paths.
1. Put the rip clip on the video track with its first frame at 25:00 (frame 600) and its last frame at 27:23 (frame 671). It is 72 frames, do not trim it and do not stretch it.
2. No transition on either side. The B1 shot before it ends on a hard cut into the rip's first frame (the happy photo holding still), and the rip's last frame (W1b, the caught shot) hard cuts into R5 at 28:00. The torn paper is the transition.
3. The 4 frame cushion: leave 4 frames (0.17 s) of clear room on each side of the rip, no title, no caption, no music hit, no other effect inside 24:20 to 25:00 and 28:00 to 28:04, so the tear and the cut land clean. I read "4 frame cushion" that way, Zac correct me if he meant handles on the clip itself.
4. Caption slots from v5 do not touch beat 8 (they sit at 0.3 to 2.8 s, 7.0 to 9.2 s, 38.5 to 40.5 s).
5. Fallback if the rip file fails: W1a then W1b with Barn Doors Wipe (Effects > Video Transitions > Wipe > Barn Doors), 0.6 s centered on the cut. NOT verified for his version.
6. W1 gets the frame check (readable truck badges at the party) like every other still. The rip frames are from W1a and W1b, check both halves.

## Audio cue sheet, F1 fire crackle plus rip (notes only, not heard, no audio made)
Edits to the F1 row of `Post-Production\projects\ian-trailer\2026-11-20-sfx-cue-sheet.md`:
| Cue | Time in 45 s | What | Level and fades |
|---|---|---|---|
| F1 | 24.80 to 28.00 | Distant fire crackle bed (Fire Fireplace Pops Crackle 01, 30.0 to 33.2, high-pass 150 Hz, low-pass 3 kHz), plays under the whole rip as before | -30, in 0.5 (pre-laps 0.2 s), out 0.4 at 28.0. Crickets B1 out under F1 by 25.3 (-38) |
| R-TEAR | 26.20 (rip clip 1.2 s, the hold ends and the tear starts) | One real paper tear, about 0.3 s, fast start | about -18, no reverb, no music hit |
| R-THUMP | 26.30 to 26.50 | Small thump for the shake as the halves open | about -22 |
| none | 26.5 to 28.0 | Fire only, no voices, no party murmur, no children | U1 duffle lands on the cut at 28.00 as before |
Timing check: the 1.2 s hold figure comes from the rip README default (hold 1.2). The v2-center clip's own hold was not read by me, so confirm the tear frame in the clip (motion-graphics README sound cue says paper tear at 1.2 s). Paper-tear and thump files are not chosen: sound-designer picks from the Adobe SFX library (free ruling) or ElevenLabs only with Zac's yes.

## Checks done
- ffprobe v7: h264, 1920x1080, 24 fps, 1080 frames counted, 45.000 s.
- Frames viewed at 24.5 (B1 gap card), 25.5 (W1a happy photo, whole), 26.5 (tear open, halves apart), 27.5 (W1b caught shot, Brandon furious), 28.5 (R5 workbench). Sheet `D:\WKP\scratch\ian\v7\chk\rowA.png` and `rowB.png`.

## Not verified
Not played as video, only 5 frames viewed. Nothing heard. Rip hold timing not read from the clip. Premiere behaviour and the cushion reading not verified. Readable-badge frame check on W1a and W1b not done by me. No qa-director pass. 9:16 has no rip. H1, B1, R3b still missing (gap cards and R3 hold in place).
