# Voiceprints how-to (built 2026-11-11)

Voiceprints live in `D:\WKP\voiceprints\` (matt.npy, zac.npy, gabby.npy). Gitignored. Biometric data of
Matt and Gabby: local only, never commit, never upload. transcribe.py loads them by default, no flag needed.

## Use
Run transcribe.py as before. Always pass `--num-speakers` when you know it (2 for a Zac and Matt review,
3 for FrostCast with Gabby). Output labels are `Matt/Winter Wolf`, `Zac/KingZ`, `Gabby/Oracle`. The run prints
one line per cluster with its confidence. A cluster below the floor stays `Guest/Unknown [n]`.

## What changed in transcribe.py (2026-11-11, original saved at scratch\voiceprints\transcribe.py.orig-2026-11-11)
1. `--map-seconds` (default 60): embeds the cluster's longest turns, about 60 s. The old code embedded the first 5
   segments (3 to 5 s) and scored 0.19 against a correct voiceprint. `--map-seconds 0` restores the old behavior.
2. `--match-threshold` (default 0.50, was 0.70): correct matches measured 0.68 to 0.89, wrong people 0.22 or less.
3. Default voiceprints folder is now `D:\WKP\voiceprints` (was a folder inside the skill that never existed).

## Refresh or rebuild a voiceprint
Use clean one-person audio: the StreamYard solo webcam mp4s in `L:\...\Raw Footage\<show>\` are best.
    python scripts\enroll_from_wavs.py --name zac --src "<solo1.mp4>" "<solo2.mp4>"
(old enroll_voices.py needs --hf-token and torchcodec, do not use it.) Test with `--voiceprints-dir` pointing at a
scratch folder first. Sources used for the live set: see `D:\WKP\voiceprints\SOURCES.txt`.

## Known limits
- Gabby's print is thin (about 150 s, from FrostCast EP 116 and the Supergirl review, no solo track exists).
  When a solo Gabby recording appears, rebuild with it.
- Cluster naming is only as good as the diarization: when pyannote merges two voices or splits one, lines go
  to the wrong person even though the voiceprint match is right. Guests (a 4th voice) stay Guest/Unknown.
- Zac's voice sounds different across mic eras (Zac to Zac similarity 0.67 to 0.94 between old and new files). If Zac
  starts coming back Unknown after a mic change, refresh it with a recent solo webcam file.
