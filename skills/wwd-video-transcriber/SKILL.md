---
name: wwd-video-transcriber
description: >
  Pulls a video file off Zac's local machine, extracts audio, and produces a fully
  diarized transcript with speakers auto-mapped to Matt/Winter Wolf, Zac/KingZ, and
  Gabby/Oracle by voice (not generic Speaker 1/2/3 guessing). Outputs an
  elapsed-timestamped transcript in the exact format the other WWD skills expect, so
  it can feed directly into wwd-frostcast-chapters, wwd-video-upload-package, and
  wwd-shorts-clip-factory without manual retyping. Trigger on "transcribe this",
  "grab the video and transcribe it", "get me a transcript with speakers", or when
  Zac points to a local video file (FrostCast recording or review multicam export)
  and wants a speaker-labeled transcript out of it. Requires Claude Code or Cowork
  with real local filesystem, ffmpeg, and Python access — cannot run in plain
  claude.ai chat since it needs to read a file off Zac's hard drive and run local
  transcription/diarization models.
---

# WWD Video Transcriber

Turns a raw video file sitting on Zac's machine into a clean, speaker-labeled,
elapsed-timestamped transcript — the first domino in the automation chain. Every
other WWD content skill (chapters, upload package, shorts clip factory) currently
requires Zac to hand it a transcript; this skill is what produces that transcript
without him doing it by hand.

## Requires Claude Code or Cowork (local machine access)

This skill needs a real shell: ffmpeg for audio extraction, Python for
transcription/diarization, and read access to the video file's actual path on disk.
It cannot run in plain claude.ai chat. If asked to run there, say so and stop.

## One-time setup (do this once, not per video)

See `references/setup-guide.md` for the full walkthrough. Short version:

1. Install dependencies: `bash scripts/setup_env.sh`
2. Get a free Hugging Face token and accept the pyannote model license (required
   for diarization) — instructions in the setup guide.
3. **Enroll the three core voices.** Collect one clean 20-60 second solo clip of
   each of Matt, Zac, and Gabby talking alone (no crosstalk, no music) — pull these
   from any past episode where one person has an uninterrupted stretch. Run:
   `python scripts/enroll_voices.py --name matt --clip /path/to/matt_sample.wav`
   `python scripts/enroll_voices.py --name zac --clip /path/to/zac_sample.wav`
   `python scripts/enroll_voices.py --name gabby --clip /path/to/gabby_sample.wav`
   This builds voiceprint fingerprints saved to `voiceprints/`. Re-run only if a
   mapping starts drifting or a mic/setup changes significantly.

Confirm setup is done before running a transcription job for the first time — check
that `voiceprints/matt.npy`, `voiceprints/zac.npy`, and `voiceprints/gabby.npy` all
exist. If they don't, stop and do enrollment first rather than transcribing with no
mapping to compare against.

## Step 1 — Get the source file

Ask for (if not already given): the video's file path on disk, and content type
(FrostCast episode or review video — informs default output naming only, doesn't
change the pipeline). Confirm the path resolves before doing any processing.

## Step 2 — Extract audio

`bash scripts/extract_audio.sh <video_path> <output.wav>` — pulls a mono 16kHz WAV,
which is what the transcription/diarization models expect.

## Step 3 — Transcribe + diarize + map speakers

`python scripts/transcribe.py --audio <output.wav> --hf-token <token>`

This does four things in one pass:
- Runs Whisper for word-level transcription
- Runs pyannote diarization to cluster the audio into anonymous speaker blocks
  (SPEAKER_00, SPEAKER_01, etc.)
- Extracts a voice embedding for each diarized cluster and cosine-compares it
  against the enrolled voiceprints in `voiceprints/`
- Relabels each cluster to Matt/Zac/Gabby if the match is confident, or leaves it
  as `Guest/Unknown [n]` if it doesn't clear the confidence threshold — never force
  a guess onto one of the three core names

If a cluster maps to a core host at low confidence, flag it in the output rather
than silently mislabeling — Zac should eyeball anything under the threshold before
trusting it downstream.

## Step 4 — Format the output

Write the final transcript as elapsed-timestamped lines matching WWD convention:

```
[00:00:00] Zac/KingZ: Alright, welcome back to FrostCast...
[00:00:04] Matt/Winter Wolf: Yeah, so this week we've gotta talk about...
[00:01:12] Gabby/Oracle: Actually, real quick, breaking news on that...
```

Save to `<video's containing folder>\<video-name>_transcript.txt` — the same
folder the source video lives in. Never a temp folder, scratchpad, or a separate
outputs directory. This applies to every venture and every video, no exceptions.
This exact format is what
wwd-frostcast-chapters, wwd-video-upload-package, and wwd-shorts-clip-factory
already expect — no reformatting should be needed to hand it straight to those
skills next.

## Step 5 — Hand off

After delivering the transcript, ask whether Zac wants to immediately chain into
chapters, the full upload package, or the shorts pipeline using this transcript —
don't run those automatically, since he may want to review the transcript for
mis-mapped speakers first, especially on a new host/guest combination.

## Do not

- Guess a speaker into Matt/Zac/Gabby below the confidence threshold — label it
  Guest/Unknown instead and flag it
- Run this outside Claude Code/Cowork — it needs real local file + model access
- Skip audio extraction and try to feed video directly into the transcription step
- Overwrite `voiceprints/` files without being asked — those are the one-time
  enrollment and shouldn't need to be redone per video
- Proceed with transcription if voiceprints haven't been enrolled yet
