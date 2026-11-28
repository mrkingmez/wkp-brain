# Pre-flight: Final export check (head-editor), run when Zac's export lands

Built 2026-11-22 from the craft brief and the A Knight's Tale export that sat locked by Premiere (ffprobe permission denied, size static). Paste into the hand-back ticked with proof.

1. [ ] The file is not still being written: size read twice 60 s apart is equal, and ffprobe opens it; otherwise the report says "not probed, render locked" and stops.
2. [ ] ffprobe lists video codec, resolution, frame rate, audio codec, sample rate, channels and duration, and these match the project spec in the package.
3. [ ] Loudness measured with the printed ebur128 command: integrated LUFS and true peak, compared to -14 LUFS and -1 dBTP (house standard, `WWD\STANDARDS.md`).
4. [ ] Short-term loudness of the first 15 s (intro) and the last 20 s is measured and compared to the talk; the intro gap is stated in LU.
5. [ ] Black detect run: start black, end black and any mid black over 0.5 s listed; a tail over 3 s flagged.
6. [ ] Pictures at every run-sheet stop time were pulled as frames and each one is named as seen or "not pulled".
7. [ ] Repeated-picture check by method, with the method's limit stated.
8. [ ] Chapter times in the package are checked against the final cut's real duration and marked match or off by N seconds.
9. [ ] Every claim about sound says "meter reading" or "heard by Zac", never "sounds good".
10. [ ] If the file is a changed re-export, the old and new numbers are shown side by side, one change at a time.
11. [ ] Every instruction to Zac is tagged PROVEN, SOURCED or PROPOSED; Premiere export clicks are PROPOSED unless backed by a retrieved page or screenshot.
12. [ ] No em dashes.
