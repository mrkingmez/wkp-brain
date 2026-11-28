# Pre-flight: End card (wwd-vfx)

Run before hand-back, paste into the hand-back with each item ticked and one line of proof. One unticked item means it does not go to Zac. Built 2026-11-22 from `wwd-vfx-craft-brief.md` and the gap audit. Tags: SOURCED S1 to S5 are in the brief.

1. Duration is 12.000 s, 360 frames at 30 fps (ffprobe nb_frames pasted). Inside the 5 to 20 s end screen window (S1, SOURCED).
2. 1920x1080, 30/1, h264, yuv420p, aac present (ffprobe pasted). 30 fps matches the show (S3, SOURCED).
3. At most 4 zones (two video tiles plus subscribe is the house layout), tiles 16:9, inside frame, not overlapping (S1, SOURCED). Coordinates written in the script header.
4. Zones are drawn from frame 0 and stay to the last frame (S1 "show at the same time", SOURCED). No video fade to black over them (S4, SOURCED).
5. No text touches any zone or zone label. The script prints the text boxes and the zone touch test, and the result is pasted. Frames pulled at 0, mid, last and looked at (defect seen on the Vision Quest finale card).
6. All text inside x 96..1824, y 54..1026 (PROPOSED convention for web, test is the box print).
7. Card 3 and the NEXT line name the real newest FrostCast per `REFERENCE\PROJECT-BOARD.md`, no review score, no em dash, handles only.
8. Sound is owned, path from `P:\Sounds\` named in the script header, no generation. Audio length equals video length within 0.05 s. Not heard by the agent, say so.
9. MP4 saved beside the .mov, no existing kit file overwritten (new version name). .mov, if made, says whether it has alpha (probe pix_fmt pasted, S5).
10. The upload package's End Screen section states the zones, the 5 to 20 s window and that the 25 s minimum is met by the full video (S1).
11. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED.
12. Ledger row says $0, 0 credits.
