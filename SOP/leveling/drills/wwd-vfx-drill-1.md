# Drill 1: wwd-vfx (free build, end card and sting)

Written 2026-11-22 BEFORE the build. Agent: wwd-vfx. Grader: qa-director (qa-media for the ffprobe and frame check), never the agent. Cost: $0, 0 credits, no generation, nothing posted.

## Task
Build from owned assets and code only (Pillow, numpy, ffmpeg, one owned sound from P:\Sounds):
1. A 12 s YouTube end card, MP4.
2. A 6 s logo-style sting (title reveal plus impact sound), MP4, in the show look (cyan, white, gold; Winter Wolf's Den text only, no studio logo or font).
Script goes to `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_vfx_drill1.py`. Outputs to `D:\WKP\scratch\wwd-vfx-level\drill1\` (not the kit, so no kit piece is touched).

## Written spec (the standard the grader checks against)
- End card: 12.000 s (360 frames), sting: 6.000 s (180 frames). Each file has an audio stream within 0.05 s of the video length.
- 1920x1080, 30 fps (the show frame rate: A Knight's Tale final export probed r_frame_rate 30/1), H.264 yuv420p, AAC.
- Safe margin: all text inside a 90 percent box, x 96 to 1824, y 54 to 1026 (PROPOSED convention, web delivery does not require it).
- End card zones: two 16:9 video elements and one subscribe ring (3 elements, YouTube allows up to four on 16:9). Card length inside the 5 to 20 s window. Zones are visible from frame 0 because "End screen elements will show at the same time by default." No text of any kind overlaps a zone or its label (defect seen on the Vision Quest finale end card).

## Pass bar (7 criteria, pass 6 of 7, CRITICAL = 1, 4, 5)
1. CRITICAL. Exact durations per spec (ffprobe duration and nb_frames).
2. 1920x1080, 30 fps, H.264 yuv420p, AAC present.
3. Text inside the 90 percent margin (script bbox check printed, frame pixel check on 3 frames).
4. CRITICAL. End-screen zones match the quoted YouTube Help limits: at most 4 elements, window 5 to 20 s, tiles 16:9, inside the frame, non-overlapping, visible from frame 0, no text over any zone or zone label.
5. CRITICAL. $0 and 0 credits: no video model, no generation tool called, sound from P:\Sounds only, ledger line says so.
6. ffprobe output for both files pasted in the result.
7. Every instruction handed on is tagged PROVEN, SOURCED or PROPOSED.

## Grader's checklist
Run ffprobe on both files, pull frames at 0, 6 s, 11.9 s (end card) and 0, 1, 3, 5.9 s (sting), look at them, run the overlap check, read the script header for assets. Sign with name and date in `wwd-vfx-drill-1-result-2026-11-22.md`.
