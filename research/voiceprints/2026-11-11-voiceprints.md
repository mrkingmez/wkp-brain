# Speaker voiceprints, 2026-11-11

Verdict: WORKS for Zac and Matt (measured on a held-out episode with ground truth). WORKS for Gabby on the one held-out FrostCast I could test, but her print is thin and her check is softer. Voiceprints are in place.

## What was wrong
1. `voiceprints/` was empty, and transcribe.py looked in a skill-folder path that never existed.
2. The matching step embedded only the first 5 segments of each cluster (3 to 5 seconds). On a correct voiceprint that scored 0.19 and 0.22. It could never have matched even with prints enrolled.
3. The 0.70 match floor was too tight. Real runs scored Zac 0.71 and Matt 0.68 (a correct match).
4. `enroll_voices.py` needs a `--hf-token` flag and torchcodec, both dead on this machine.

An older attempt exists at `L:\Winter Wolfs Den review show\_voiceprints\` (matt.npy, zac.npy, Aug 13, notes say Gabby not enrolled). It is not wired to anything. I did not touch or use it.

## Sources (all read-only, all under `L:\Winter Wolfs Den review show\`)
Zac and Matt: StreamYard solo webcam mp4s, seconds 300 to 1800 of each, under `Raw Footage\`. Each cam track is digital silence when that person is not talking, so it is clean one-voice audio.
- Vision Quest\Vision Quest ep 3 and 4 (King-Z and Winter_Wolf webcam)
- Vision Quest\Vision Quest ep 5 and 6 (Untitled_recording webcams)
- Fury
- MKII
- Percey Jackson\Season 2\Ep 1&2
- Serise mass record\Fallout\EP 8

Gabby (no solo track exists anywhere I found):
- Frost-Cast\EP 116 transcript lines Guest/Unknown [1], using only 3 s windows that sit fully inside her turns, after the 2:00 cold open, pitch over 180 Hz. Identity evidence: her lines say "I told King...", "I was scared by my mom", "Let's talk about the adults".
- Raw Footage\Supergirl (2026)\Supergirl review Fans like but Box Office Bomb.mp4, Premiere "Speaker 3" lines, pitch over 185 Hz. Identity evidence: that review's opening hands the floor to "the female demographic / the Oracle" and Speaker 3 answers; median pitch 211 Hz against 154 to 172 Hz for the male speakers. Inferred, not confirmed by Zac.
- Cross-check: EP 116, EP 118 and the Supergirl Speaker 3 voices all clustered together (similarity 0.67 to 0.88) and not with Zac or Matt.

Seconds enrolled: Zac 540, Matt 540, Gabby 147 (49 windows of 3 s, about 16 from EP 116 and 33 from Supergirl). The EP 117 and EP 119 "other voice" windows did not match the Gabby group; I did not use them.

Not used: Supergirl raw Audio 1 to 3 tracks (Audio 1 is Matt's recorder, Audio 2 is Zac's, Audio 3 is a room mix), EP 117, EP 119.

## Held out for testing (never used for enrollment)
- Vision Quest EP 7 raw (`Raw Footage\Vision Quest\EP 7\Vision Quest Review EP 7.mp4`), Zac and Matt. Ground truth comes from that episode's own King-Z and Winter_Wolf webcam tracks (offset 0.4 s corrected). This is real ground truth.
- FrostCast EP 118, Zac, Matt, Gabby. No solo tracks exist for FrostCast, so truth here is the existing EP 118 transcript clusters ([1] Gabby, [2] Zac, [3] Matt) which I checked by content ("introduce my co-host, Oracle" is cluster 2, "Thank you, Oracle, for running the show" is cluster 3). This is a softer check: it measures agreement with those clusters, and two cue lines (3060 s, 3511 s) were ambiguous.

## Results
Cluster to name matching, real `transcribe.py` end to end (new settings), cosine confidence:
| Episode | Cluster | Named | Confidence |
|---|---|---|---|
| VQ EP 7 (2 speakers) | 00 | Matt | 0.79 |
| VQ EP 7 | 01 | Zac | 0.71 |
| EP 118 (3 speakers) | 00 | Matt | 0.68 |
| EP 118 | 01 | Zac | 0.86 |
| EP 118 | 02 | Gabby | 0.77 |
Wrong-person scores in the same runs were 0.22 or lower. Every cluster got the right name.

Line accuracy, VQ EP 7, vs the cam tracks, counting only moments when exactly one person talked (whole transcript line takes one label):
- Matt: 93.5% of 1157 s correct.
- Zac: 82.9% of 521 s correct.
The misses are mostly lines where Whisper's segment covers both people, so one label cannot be right. Frame-level labeling from the diarization alone (before Whisper segments) scored Matt 95.3% and Zac 92.0% of labeled time.

EP 118 (three-person FrostCast), agreement with prior cluster identity, by line (1,426 lines, first minute skipped):
- Gabby: 61 of 66 (92%)
- Zac: 444 of 482 (92%)
- Matt: 813 of 856 (95%)
New transcript labels: Matt 872 lines, Zac 488, Gabby 66.

## Is three-person FrostCast shaky?
Not shaky on the voice matching: all three clusters named correctly with big margins. Weak spots, stated plainly:
- Gabby's print is thin (147 s) and mixed from two sources. 0.77 on EP 118 is solid, but I have one test episode for her and no true ground truth.
- Matt scored 0.68 on EP 118, the lowest. It only passed because the floor is now 0.50.
- Diarization (not the voiceprint) is the main error source: it merges or splits voices, and short interjections land with the wrong person.
- Use `--num-speakers 3` for FrostCast with Gabby. Without it pyannote invents extra clusters (EP 118's old run had 4 including cold open movie quotes).
- A guest voice would stay Guest/Unknown, which is correct behavior.
- The cold open movie quotes can still be labeled as a host, because they are short and their cluster can be absorbed.

## What I changed
Reversible. Original saved at `D:\WKP\scratch\voiceprints\transcribe.py.orig-2026-11-11`.
- `D:\WKP\.claude\skills\wwd-video-transcriber\scripts\transcribe.py`: new `--map-seconds` (default 60, 0 = old behavior), new `--match-threshold` (default 0.50, was 0.70), default voiceprints folder now `D:\WKP\voiceprints`. Nothing else touched. Existing transcripts and recordings were not modified.
- New `scripts\enroll_from_wavs.py` (tested, re-enroll Zac gave cosine 0.98 to the live print).
- New `references\voiceprints-howto.md`.
- `D:\WKP\voiceprints\` zac.npy, matt.npy, gabby.npy, SOURCES.txt (the only things in it).
- `.gitignore`: added `/voiceprints/` and the skill-local voiceprints path. Verified with git check-ignore. The research folder is not ignored. Nothing committed or pushed.
- Test outputs only in `D:\WKP\scratch\voiceprints\` (e2e transcripts, wavs, scripts).

Everything stayed local. The only model used is pyannote/embedding and the diarization model the skill already loads (cached, no new download). No cloud, no money, no accounts.

## Zac needs to do
Nothing required. Optional: when EP 120 finishes, run the chain with `--num-speakers 2` (Zac and Gabby) and glance at the confidence lines. If Gabby's clip ever exists solo (one minute of her talking alone), rebuild her print with `enroll_from_wavs.py` to firm it up. Stale pointer to fix in `memory\topics\transcription.md` ("Voiceprints not yet enrolled") and in CLAUDE.md's transcription section: Jarvis's call.

Files uncommitted for Zac to commit: transcribe.py edit, the two new skill files, .gitignore.
