# wwd-vfx drill 1: run log (agent's own record, not the grade)

Run 2026-11-22 by wwd-vfx. Script: `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_vfx_drill1.py` (one run, 3 minutes wall time total across two attempts; attempt 1 printed a wrong overlap check because it mixed the sting's text boxes into the end card zone test, fixed in the script, same renders). Outputs: `D:\WKP\scratch\wwd-vfx-level\drill1\drill1-end-card-12s.mp4`, `drill1-sting-6s.mp4`, `geometry.json`. Cost: $0, 0 credits, no generation tool, no connector called. Sound: `P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impact On Metal Shield 01.wav` (owned Adobe SFX library, index P:\ csv).

## ffprobe (pasted, compact)
drill1-end-card-12s.mp4
  video: h264 High, 1920x1080, yuv420p, r_frame_rate 30/1, duration 12.000000, nb_frames 360
  audio: aac LC, 48000 Hz, 2 ch, duration 12.000000
  format duration 12.000000, size 851176
drill1-sting-6s.mp4
  video: h264 High, 1920x1080, yuv420p, r_frame_rate 30/1, duration 6.000000, nb_frames 180
  audio: aac LC, 48000 Hz, 2 ch, duration 6.000000
  format duration 6.000000, size 665912

## Script geometry check (printed by the script)
End card text boxes all inside x 96..1824, y 54..1026 (extent x 372..1539, y 188..984). Sting boxes inside (title at final scale x 372..1548, y 410..590; at its largest animated scale 1.35 it spans x 166..1754 by arithmetic, not measured per frame). Zones: tiles (190,420,830,780) and (1090,420,1730,780), both 640x360 = 16:9, ring centre (960,600) r 90. No text box touches a zone; the three zone labels sit outside the zones (LATEST UPLOAD y 355..380, BEST FOR YOU y 355..380, SUBSCRIBE y 716..743 against ring bottom 694).

## Frames I looked at (Read)
End card frame 0 (zones and labels on screen from frame 0, title not yet in), 11.9 s (all text in, no overlap). Sting at 1.0 s (title mid-scale, grey from fade-in, no blade visible: the blade finishes at 0.9 s), 3.0 s (title, subtitle, gold rule clean). Frames saved in the same folder (e0.png, e119.png, s_1.png, s_3.png, others).

## Not verified
Audio never heard (cannot). Volumedetect: sting max -0.5 dB, end card max -5.0 dB (not true peak, not LUFS). Design quality is plain, no wolf or frost motif beyond a faint grid: the drill tests spec compliance, not creative merit; I would not ship this sting as the show look.
