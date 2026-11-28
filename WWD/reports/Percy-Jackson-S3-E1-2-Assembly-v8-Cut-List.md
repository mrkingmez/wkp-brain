# Percy Jackson S3 Eps 1 and 2: Assembly v8 (2026-11-27)
File: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\export\Percy-Jackson-S3-E1-2-Assembly-v8.mp4`, phone copy `...-v8-240p-phone.mp4` (426x240, 15 fps, 24.7 MB). v1 to v7 untouched.
Ordered by wwd-director after a whisper spot check of v7 found the echo of KingZ's wrong line still audible at v7 23:06 to 23:10.

## The one change (cut C5, Prometheus a god)
- v7 cut C5 removed raw 2322.691 to 2324.392 s (1.701 s): KingZ "Prometheus was a god". Winter Wolf's echo started at raw 2324.40 and was left in.
- v8 cut C5 removes raw 2322.691 to 2325.400 s (2.709 s). The extension is exactly 1.000 s (30 frames, raw 2324.400 to 2325.400).
- Matched by words (faster-whisper on the raw mix): "Prometheus" 2322.80 to 2323.24, "was a god" to 2323.92, echo "Was a god, that's what, yeah" 2324.40 to 2325.30, "And" starts 2325.52. Cut point chosen on the quietest stretch between the echo and "And" (raw mix about -34 dB at 2325.36, against -26 to -16 dB speech). Matches fact-research Facts-Refresh 2026-11-27 item 3 (E 23:34:25 to 23:37:15, E = raw minus 908 s, so raw 2322.8 to 2325.5).
- Join in the file at 1386.30 s (frame 41589). Words across the join (faster-whisper on v8, 1382.3 to 1390.3): "...I was, I was mistaken, Atlas with Prometheus. | And he was punished for giving Earth fire to the human..." The echo is gone. No dangling clause: "And he was punished for giving fire" reads as a clean sentence about Prometheus. KingZ's "I was mistaken, Atlas with Prometheus" stays, as in v7.

## Timeline after the change
Everything after the join moved 1.000 s earlier, content otherwise identical to v7 (pictures, clips, cam runs, banners, rimshot, music tail all keep their relative place).
| Item | v7 | v8 |
|---|---|---|
| Total length | 1883.467 s (31:23.47), 56,504 frames | 1882.467 s (31:22.47), 56,474 frames |
| Conversation ends, Next Up card (generic, 6 s) starts | 1865.467 s | 1864.467 s (frame 55,934) |
| End card (12 s) starts | 1871.467 s | 1870.467 s |
| End card ends | 1883.467 s | 1882.467 s |

## How it was built
- Picture: `D:\WKP\scratch\pj-edit\plan_v8.json` (made from plan_v7.json by `v8\mkplan.py`: K[9] start moved to frame 69762 with 1199 frames, every later F shifted -30, camrun straddling the join shortened). `build_video_v8.py` reuses the v7b rendered pieces by frame mapping (before the join as is, after the join shifted 30 frames, 180 pieces, only the pieces touching the join re-rendered). Cards re-rendered from the same kit files.
- Audio: `mix_final_v4.wav` (the exact v7 audio, checked against the v7 mp4 by correlation 0.99999 at lag 0) with the 30 frames (48,000 samples) removed at the join and a 6 ms fade-in on the new start, `v8\audio8.py`. Same limiter, same gain, one AAC encode (256 kb/s, 48 kHz). Everything after the join (sfx, banners, rimshot, outro music anchored to the end) moves together, so nothing slips against the picture.
- Not re-measured per section: intro, speech and outro levels (unchanged material).

## Measured on v8 (ffprobe, ebur128, blackdetect, freezedetect, silencedetect)
- 1920x1080, 30 fps, H.264 plus AAC, 56,474 frames, 1882.467 s.
- Integrated -14.0 LUFS, true peak -1.3 dBTP, LRA 5.9 LU (v6 and v7 same: -14.0 and -1.3).
- Black: none (blackdetect 0.5 s). Silence: only the last 1.09 s (end pad). Freezedetect (2 s, -60 dB) lists the picture holds and 2 s hold segments, as in earlier versions: not compared line by line with v7.
- Frames viewed at 1864.0 (two-shot), 1865.0 and 1870.0 (Next Up card), 1871.0 (end card). Not viewed: the rest of the cut, not heard by anyone.
Not verified: no listening, no qa-director pass on v8.
