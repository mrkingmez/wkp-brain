# Drill 1 result: head-editor, attempt 1, 2026-11-22

Agent self-check against the pass bar in `head-editor-drill-1.md`. NOT SIGNED. Grader: qa-director (qa-media) and Jarvis spot-check, status PENDING. The agent never signs. The drill was not blind (contamination note in the drill file).

Work files: `D:\WKP\scratch\hed-level\` (loud1-3.txt, black1-3.txt, sil1-3.txt, rep1-3.txt, rep.py). Files measured are the final exports whose durations match the Style Sheet: 1733.6 s (28:53.6), 1435.5 s (23:55.5), 1666.9 s (27:46.9). Container: H.264 1920x1080 30 fps, AAC audio, all three (ffprobe).

## Commands (printed in full, run 2026-11-22)
- Loudness: `ffmpeg -hide_banner -nostats -i <file> -vn -af ebur128=peak=true -f null -` (Summary block read)
- Black: `ffmpeg -i <file> -vf blackdetect=d=0.5:pix_th=0.10 -an -f null -`
- Silence: `ffmpeg -i <file> -vn -af silencedetect=n=-45dB:d=1.5 -f null -`
- Repeats: `python -I D:\WKP\scratch\hed-level\rep.py <file>` (2 fps, 64x36 grey, cutaway = correlation to the median frame under 0.6, runs of 2 s or more, mid-frame pairs over 0.97 flagged)

## Measurements
| File | Integrated | Loudness range | True peak | vs -14 LUFS house standard | Black over 0.5 s | Silence over 1.5 s at -45 dB |
|---|---|---|---|---|---|---|
| Godzilla Minus Zero | -24.7 LUFS | 7.8 LU | -2.4 dBTP | 10.7 LU short | 12.93 to 13.43 s (0.5 s); 1723.07 to 1733.57 s (10.5 s tail) | 1 stretch, 1724.77 s to the end (8.8 s) |
| Vision Quest EP 7 | -22.8 LUFS | 7.2 LU | -1.7 dBTP | 8.8 LU short | 17.8 to 18.37 s (0.57 s); 1433.87 to 1435.5 s (1.63 s tail) | 2 stretches (154.5 s for 1.6 s; 178.0 s for 1.7 s) |
| Vision Quest EP 8 | -21.2 LUFS | 7.8 LU | +0.1 dBTP | 7.2 LU short | 14.57 to 15.13 s (0.57 s); 1664.47 to 1666.87 s (2.4 s tail) | 2 stretches (174.1 s for 1.8 s; 1665.2 s to the end 1.7 s) |
The "Peak" line in the ebur128 Summary with peak=true is the true peak (read from the printed block; unit shown as dBFS by ffmpeg). The numbers match the Style Sheet table to the decimal for all 3, which confirms the method but also means this is replication, not discovery.

## Defects
1. Godzilla repeated picture: runs at 1534.0 to 1539.5 s and 1572.5 to 1577.5 s, mid-frame correlation 1.000 (about 25:36.7 and 26:15.0 at the mid-frames). Matches the Style Sheet (25:36 and 26:15). Frames not viewed by me; the method's limit: it only catches a repeat with the same framing.
2. Godzilla black tail 10.5 s plus 8.8 s silence, 28:43.07 to the end. Measured.
3. All 3 exports miss -14 LUFS (house standard, `WWD\STANDARDS.md`): 10.7, 8.8 and 7.2 LU short.
4. Vision Quest EP 8 true peak +0.1 dBTP, over the -1 dBTP house limit by 1.1 dB. Godzilla and EP 7 are under it.
5. Godzilla 0.5 s black at 12.93 s: NEW, not in the Style Sheet. Not viewed. May be an intended flash.
6. Vision Quest EP 7 ends on 1.63 s of black and EP 8 on 2.4 s: under 3 s, within the Style Sheet's tolerance, listed for completeness.
Cutaway runs found by the method: Godzilla 23, EP 7 12, EP 8 23 (counts only, unchecked against the Style Sheet's own cutaway totals).

## Loudness standard, quoted
- EBU R128 page (https://tech.ebu.ch/publications/r128, retrieved 2026-11-22): "Recommendation to use an average programme loudness of -23 LUFS and the 'Loudness Range' and 'Maximum True Peak Level' descriptors." and "Target level (-23 LUFS) tolerances restricted to +/- 0.5 LU." (as returned by the fetch tool).
- ITU-R BS.1770 page (https://www.itu.int/rec/R-REC-BS.1770, retrieved 2026-11-22): title "Algorithms to measure audio programme loudness and true-peak audio level", version BS.1770-5, 11/2023.
- YouTube figure: "YouTube doesn’t release exact values, but YouTube tends to shoot for -12 to -14 LUFS." (https://workflow.frame.io/guide/loudness-for-youtube, retrieved 2026-11-22, no date shown) and "they changed this in 2019 and have been using exactly -14 LUFS since then" (https://productionadvice.co.uk/youtube-loudness/, retrieved 2026-11-22).
- What the quotes do NOT prove: EBU -23 is a broadcast recommendation, not a YouTube rule. -14 is a third-party figure, Google published none that I could retrieve. No retrieved source says YouTube raises a quiet upload. The Premiere -14 export steps are PROPOSED (Adobe pages blocked, 403).

## Fix list (ordered by Zac time, smallest first, and Godzilla's pre-post blockers first)
1. Godzilla: set the Out point at 28:43 (last frame of the end card) so the black tail is not exported. PROPOSED (Style Sheet Recipe 5, Premiere clicks not verified on his version). About 1 minute.
2. Godzilla: swap the second use of the repeated picture (about 26:15) for an unused Godzilla picture. PROPOSED (Recipe 4, Alt-drag not verified on 2027). About 5 minutes.
3. Godzilla: view 12.9 to 13.4 s and keep or fix the 0.5 s black. PROPOSED (not viewed by me). About 1 minute.
4. All three: re-export at -14 LUFS and -1 dBTP using a 1-minute test first, then measure with the printed ebur128 command. SOURCED for the measure (S3 BS.1770 defines the measurement, S2 R128 shows a standard exists); the -14 house number is Zac's own rule in STANDARDS.md; the Premiere setting is PROPOSED. About 30 to 60 minutes with exports, hours NOT KNOWN.
5. Vision Quest EP 8: its +0.1 dBTP peak is fixed by the same re-export as item 4. PROPOSED.

## Self-check against the pass bar
1. CRITICAL, finds both defects: pass (both found by method, black exactly, repeat at 1.0 correlation; grader to confirm against the blind list).
2. CRITICAL, loudness measured with command printed for all 3: pass.
3. Standard cited with quote, URL and date, and limits stated: pass (EBU, BS.1770, YouTube third party; Netflix and Adobe NOT RETRIEVED).
4. No unmeasured claims: pass for what is written; no frame was viewed or sound heard by me, and every line says measured or not viewed.
5. Fix list ordered by Zac time: pass, order stated.
6. Every instruction tagged: pass.
Self-check 6 of 6. That is not a grade. Status: PENDING grader sign (qa-media) and Jarvis spot-check. Weaker than a blind pass: the Style Sheet names the same defects and all numbers equal its table.
Not done: no frame pulled and viewed; no audio heard; the 0.5 s black not looked at; VQ7 and VQ8 repeats method found none (with the method's limit).
