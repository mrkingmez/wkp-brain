# Pre-flight: sting or intro cut

Owner: music. Created 2026-11-22. Run before hand-back. One unticked item and the cut does not go to Zac.

1. [ ] Source file path and its license status (receipt path, or "owned, license unproven"). Proof: path.
2. [ ] Cut length in seconds, measured with ffprobe on the output file. WWD intro sting is 6.0 s or less (Zac 2026-11-19). Outro length stated and chosen on purpose. Proof: ffprobe duration line.
3. [ ] The hit or hook lands inside the first 6 s: checked with an ffmpeg RMS-per-window read, not guessed from the page length. Proof: the window numbers. "Not heard" is stated.
4. [ ] Fade out at the end, no hard click at the cut. Proof: the ffmpeg filter in the command (afade) and the end-of-file RMS.
5. [ ] Loudness measured with ebur128 (LUFS and true peak). Library and generated tracks run hot (rock-the-crowd -7.4 LUFS, +1.1 dBTP). A gain change is written down. Proof: output lines.
6. [ ] The cut file is a new file with a new name, the original is untouched, and no file Zac already used is overwritten. Proof: both paths.
7. [ ] The command that made the cut is saved (scratch script or in the card) so a re-cut is one line. Proof: path.
8. [ ] An owned fallback exists for every generated or paid pick, cut to the same length. Proof: path.
9. [ ] The cut is copied to the show's kit folder `P:\WWD Kit\<show>\Sounds\` (WWD) so Zac finds it. Proof: path.
10. [ ] "Not heard by anyone" is said plainly, and Zac auditions before it is used. Proof: line in the hand-back.
