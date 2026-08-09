# Video Transcription

## Transcript output location — absolute rule [2026-08-06]
Every transcript goes in the **same folder as the source video**, as a `.txt`
file. Never a temp folder, scratchpad, or a separate `outputs/transcripts/`
location. Stated by Zac as an absolute: "This is always!" and repeated for the
`.txt` format. Output path is
`<video's containing folder>\<video-name>_transcript.txt`, overriding the default
in the transcriber's own SKILL.md. Applies to every venture, every video.

## The machine has an RTX 5060 — use it [2026-08-06]
Default `pip install torch` installs the CPU-only build, which left an 83-minute
episode grinding for over an hour on CPU while a capable GPU sat idle. Install
torch and torchaudio from the CUDA index instead. Verified working at
torch 2.11.0+cu128, CUDA available, GPU detected. Expect roughly 10-20x on the
Whisper step.

## torch CUDA upgrade breaks torchvision [2026-08-06]
Jumping torch 2.8.0 → 2.11.0 left torchvision on the old CPU-matched version and
incompatible. Upgrade torchvision from the same CUDA index immediately after.
Always verify whisperx, pyannote, and diarization all import cleanly after a
torch version jump before launching a long job.

## Never swap torch mid-run on Windows [2026-08-06]
Windows locks torch DLL files while a process has them loaded. Reinstalling
during an active transcription can fail or leave the install in a broken state.
Wait for the job to finish.

## pyannote gated models must be accepted individually [2026-08-06]
Each model has its own license page and the script only reveals the next one
after clearing the previous. Accepted so far on Zac's HF account:
`pyannote/speaker-diarization-community-1` (current whisperx default, not the
`3.1` version the original setup guide names) and `pyannote/embedding` (used for
voiceprint comparison). A retry re-runs the entire Whisper pass from scratch even
when only the final step failed, so each gate costs a full run.

## Gaming during transcription kills the job [2026-08-06]
An EP106 run was terminated externally with no traceback while Zac was gaming on
the same machine. Whisper, diarization, and embedding models together are
RAM-hungry enough that running alongside a game can trigger an out-of-memory
kill. Launch detached, and treat a silent death with no error as memory pressure
rather than a script bug.

## Voiceprints not yet enrolled [2026-08-06]
`voiceprints/` is empty, so every speaker returns as `Guest/Unknown [n]`.
Enrolling Matt, Zac, and Gabby requires a clean solo audio clip of each. Until
then, speaker mapping has to be done by hand after transcription.

## HF token comes from the environment, not a CLI flag [2026-08-08]
`transcribe.py` no longer takes `--hf-token`. It reads the `HF_TOKEN` Windows
environment variable directly and exits early with a clear message if it's
unset (checked at the top of `main()`, before any model loading). Don't ask
Zac for the token or pass `--hf-token` — it's already set in his environment.
Docs updated to match: `SKILL.md`, `references/setup-guide.md`, and the EP106
resume command in `TASKS.md`.

## EP106 still has no transcript [2026-08-06]
Every blocker was cleared — script bugs fixed permanently in
`D:\WKP\skills\wwd-video-transcriber\scripts\transcribe.py`, all HF licenses
accepted, CUDA live — but the final launch kept getting rejected before
execution after 24+ hours and dozens of tool calls in one session. Fix is a
fresh session, not more retries in the stuck one. Nothing was lost.
