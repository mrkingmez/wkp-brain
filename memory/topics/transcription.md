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

## torchcodec is broken in this environment — bypass it, don't fix it [2026-08-09]
pyannote's speaker-embedding step (`Inference.__call__`) decodes audio via
torchcodec, and torchcodec's precompiled DLLs fail to load against this
machine's torch 2.11.0+cu128 build regardless of installed ffmpeg version.
`_load_wav_dict()` in `transcribe.py` now reads the WAV clip directly with
Python's stdlib `wave` module and hands pyannote a
`{'waveform': tensor, 'sample_rate': int}` dict instead of a file path —
`Audio.__call__` skips the torchcodec path entirely when given a dict. Don't
waste a run trying to fix the torchcodec install itself; the warning at
startup ("torchcodec is not installed correctly") is not benign, it will kill
the run at the mapping step. A retry after this kind of crash re-does the full
Whisper + diarization pass from scratch — no checkpointing across runs.

## EP106 transcript done [2026-08-09]
1,406 lines, full 83-minute episode, saved to
`L:\Winter Wolfs Den review show\Frost-Cast\EP 106\...transcript.txt`.
Speakers still came back Guest/Unknown [1]/[2]/[3] — [[voiceprints]] enrollment
is still the blocker for named speakers, unchanged from the 2026-08-06 note.
