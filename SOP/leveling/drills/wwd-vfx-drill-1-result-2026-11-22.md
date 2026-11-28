# wwd-vfx drill 1: grader result

Grader: qa-director (did not make the work). Date 2026-11-22. Work not edited. Free checks only (ffprobe, ffmpeg frame pulls, Pillow pixel scan, file reads). No credits, no posting, no push.

## Score: 6 of 7. CRITICAL criteria 1, 4, 5 all PASS. OVERALL: PASS

| # | Criterion | Result | Proof |
|---|---|---|---|
| 1 | CRITICAL. Exact durations | PASS | I ran ffprobe with -count_frames. End card: video duration 12.000000, nb_frames 360, nb_read_frames 360. Sting: 6.000000, 180, 180. Audio duration 12.000000 and 6.000000, so 0.000 s off video (limit 0.05 s). |
| 2 | 1920x1080, 30 fps, H.264 yuv420p, AAC | PASS | Both files: h264 High, 1920x1080, yuv420p, r_frame_rate 30/1, avg 30/1; audio aac LC, 48000 Hz, 2 ch. |
| 3 | Text inside 90 percent box (x 96..1824, y 54..1026) | PASS | Script prints all boxes inside (end card extent x 372..1539, y 188..984, geometry.json agrees). My own pixel scan of frames qe_0, qe_6, qe_11.9, qs_1, qs_3 for bright pixels outside the box: 0 in every frame. Sting title at t=1.0 s (scale about 1.21) measured x 257..1655, inside. Largest scale (1.35, t=0.9 s) is arithmetic only (x 166..1754), still inside, not measured per frame. |
| 4 | CRITICAL. End screen zones | PASS | Read from script and frames: 3 elements (limit 4); 12 s card (window 5 to 20 s); tiles (190,420,830,780) and (1090,420,1730,780) are each 640x360 = 16:9; all inside frame; gaps: tile1 to ring 36 px, ring to tile2 36 px, no overlap; zones drawn at frame 0 (qe_0 shows both tiles, ring and labels, title not yet in). No text over a zone: nearest text boxes are labels at y 355..380 (zone top 420), SUBSCRIBE at y 716..743 and x 860..1059 (ring bottom 694, tile edges 830 and 1090), title y 188..284, footer y 883..984. Frames at 6 s and 11.9 s show no overlap. Caveat: the limits themselves are the drill's own wording, only one sentence is quoted and no YouTube Help URL is in the files, so I checked geometry against the limits as written and did not retrieve the Help page (see notes). |
| 5 | CRITICAL. $0, 0 credits | PASS | Script header says no generation, no credits; code is Pillow, numpy, ffmpeg only, searched for generate, credit, firefly, http: no hits beyond the header. Only sound: `P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impact On Metal Shield 01.wav` (asserted to exist, inside P:\Sounds). Fonts are Windows system fonts (Impact, Constantia), no studio font. Run log states $0, 0 credits, no connector called. Note: no wwd-vfx row for this drill exists in `logs\agent-runs.md` yet (searched 2026-11-22 rows). The run log carries the statement, so I count it, but the ledger row is owed. |
| 6 | ffprobe pasted | PASS | Run log has compact ffprobe for both files. Matches mine: 1920x1080, yuv420p, 30/1, durations 12.000000 and 6.000000, nb_frames 360 and 180, aac 48000 Hz 2 ch, sizes 851176 and 665912 bytes. |
| 7 | Instructions tagged PROVEN, SOURCED or PROPOSED | FAIL | Drill file tags the 90 percent margin PROPOSED (adequate) and quotes one YouTube sentence (visible by default). But "up to four elements", "5 to 20 s window" and "16:9 tiles" carry no tag and no URL or quote, and the run log has zero tags (0 matches for PROVEN, SOURCED, PROPOSED). The run log's own claims (-5.0 dB and -0.5 dB max, 1.35 scale arithmetic) are honestly labelled as not true peak, not LUFS and not measured, which is good practice but not the tag format. |

## Overall
PASS (6 of 7, all three CRITICAL criteria pass).

## Frames checked (saved in `D:\WKP\scratch\wwd-vfx-level\drill1\qa\`)
End card 0, 6, 11.9 s. Sting 0, 1, 3, 5.9 s. End card at 0 s is clean zones and labels, title and footer arrive later, no collision at any point. Sting: 0 s dark grid only, 1 s title grey and large from the fade-in (no blade visible, the agent said the same), 3 s title, cyan subtitle, gold rule, 5.9 s fade to near black.

## Notes (none blocks)
1. The YouTube limits (4 elements, 5 to 20 s, 16:9) were never retrieved by me or shown in the drill file as quotes. Tag them SOURCED with the Help URL and quote, or PROPOSED, before anyone hands them on. I did not open the Help page.
2. Add the wwd-vfx ledger row for this drill to `logs\agent-runs.md` (what, what verified, what not).
3. Frame 5.9 s: title still readable as dark grey, fine for a fade. The sting has the first 0.9 s as empty grid plus a blade that sweeps off screen at 0.9 s, so the first visible title frame comes late; agent already says design is plain and not ship-quality. This drill grades spec compliance only.
4. Video stream frame counts match to the frame. Audio packet counts (564 and 283) are not a check item.
5. The agent was honest in the run log that attempt 1 printed a wrong overlap check and was fixed. Script now tests the end card boxes only against end card zones, correct.

## Could not verify
- Audio cannot be heard here. I did not play it, so I cannot confirm the impact lands on the title hit (script delays the sound 0.85 s against title at 0.9 s) or that it is not clipped. Run log's volumedetect values (sting max -0.5 dB, end card max -5.0 dB) not re-run by me; they are not true peak or LUFS in any case, and no -14 LUFS check was in scope.
- The three YouTube limits against the live Help page (not retrieved).
- Zone fit inside YouTube Studio (no upload, no posting).
- Scale animation extremes between frames 27 and 34 of the sting (checked 1 s only, plus arithmetic).

Signed: qa-director, 2026-11-22
