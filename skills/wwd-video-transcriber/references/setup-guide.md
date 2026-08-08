# WWD Video Transcriber — Setup Guide

One-time setup. Do this before the first real transcription job.

## 1. Install dependencies

```
bash scripts/setup_env.sh
```

This installs `whisperx`, `pyannote.audio`, `torch`, and `torchaudio`. On a
machine without a GPU this still works — it just runs slower (CPU inference).

## 2. Hugging Face token + model license

Diarization uses a gated pyannote model, which requires a free Hugging Face
account and explicitly accepting the model's terms.

1. Create a free account at huggingface.co if you don't have one.
2. Visit `https://huggingface.co/pyannote/speaker-diarization-3.1` and click
   "Agree and access repository."
3. Also accept the license at `https://huggingface.co/pyannote/segmentation-3.0`
   (a dependency of the diarization pipeline).
4. Generate an access token: Settings > Access Tokens > New token (read access
   is enough).
5. Keep that token handy — it gets passed to `transcribe.py --hf-token`.

## 3. Enroll the three core voices

Voice mapping only works once each host has a fingerprint on file. Pull one
clean 20-60 second solo clip per person from any past episode — a stretch
where only they're talking, no crosstalk or music underneath.

```
python scripts/enroll_voices.py --name matt  --clip /path/to/matt_solo.wav
python scripts/enroll_voices.py --name zac   --clip /path/to/zac_solo.wav
python scripts/enroll_voices.py --name gabby --clip /path/to/gabby_solo.wav
```

This writes `voiceprints/matt.npy`, `voiceprints/zac.npy`, `voiceprints/gabby.npy`.
Keep these three files — they're the whole reason speaker mapping works
automatically instead of coming back as generic SPEAKER_00/01/02.

Re-enroll a name only if mapping accuracy starts drifting (new mic, room
change, etc.) — otherwise this is truly one-time.

## Running a job end to end

```
bash scripts/extract_audio.sh /path/to/episode.mp4 /tmp/episode_audio.wav
python scripts/transcribe.py \
  --audio /tmp/episode_audio.wav \
  --hf-token hf_xxxxxxxxxxxx \
  --output /mnt/user-data/outputs/transcripts/episode_transcript.txt
```

## Troubleshooting

- **"Missing voiceprints" warning** — enrollment step 3 wasn't done, or the
  `voiceprints/` folder got wiped. Re-run `enroll_voices.py`.
- **Everyone comes back as Guest/Unknown** — usually a bad enrollment clip
  (too short, crosstalk, or wrong person). Re-enroll with a cleaner clip.
  Could also mean the confidence threshold (0.70 in `transcribe.py`) is too
  strict for a noisy recording — lower it slightly if matches are consistently
  just missing the bar.
- **Diarization step fails with a permissions/401 error** — the Hugging Face
  token doesn't have the gated model licenses accepted yet (step 2), or the
  token itself is wrong.
- **Very slow on CPU** — expected without a GPU; a full ~90 minute FrostCast
  episode can take a while. Consider a smaller Whisper model (`--model medium`
  instead of `large-v3`) if turnaround time matters more than accuracy for a
  given run.
- **A guest or one-off voice never maps** — expected and correct behavior.
  Only Matt/Zac/Gabby are enrolled by design; anyone else always comes back
  as Guest/Unknown [n] and should be manually labeled if needed.
