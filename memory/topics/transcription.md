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

## Diarization defaults to batch_size=1 — fully serial, will stall on long files [2026-08-27]
pyannote-audio 4.0.7's `SpeakerDiarization` pipeline (loaded inside whisperx's
`DiarizationPipeline`) defaults both `embedding_batch_size` and
`segmentation_batch_size` to 1, forcing fully serial GPU calls across the whole
file. On EP109 (91:36) this stalled diarization for 4h16m before it was killed
without finishing — genuinely still computing (CPU time climbing at steady
~101-102% of wall clock), not hung, just architecturally slow at batch_size=1.
Root cause confirmed by reading the installed pyannote source directly
(`pyannote/audio/pipelines/speaker_diarization.py`), not guessed.

Fix: whisperx's `DiarizationPipeline` doesn't expose these as constructor args
(it loads the underlying pyannote `Pipeline` via `Pipeline.from_pretrained()`,
which only reads hyperparameters baked into the model's own `config.yaml` —
no passthrough for arbitrary kwargs). Set them as attributes on the loaded
pipeline object *after* construction instead:
`diarize_pipeline.model.embedding_batch_size = N` and
`diarize_pipeline.model.segmentation_batch_size = N`
(`embedding_batch_size` is a plain attribute; `segmentation_batch_size` has a
property setter that forwards to the underlying `Inference.batch_size`). Both
confirmed settable post-load from source. `transcribe.py` now exposes
`--embedding-batch-size`/`--segmentation-batch-size`, both defaulting to 8 —
chosen as the modest/safe end of the 4-8 range for this 8GB RTX 5060, not
pushed higher without more headroom data.

Related fix found in the same pass: Whisper's transcription model and the
align model were never released from VRAM before the diarization pipeline
loaded, so the diarization-stage VRAM figure (7.6GB observed the night of the
stall) likely included leftover Whisper/align weights, not just diarization's
own footprint. `transcribe.py` now does
`del model; del align_model; gc.collect(); torch.cuda.empty_cache();
torch.cuda.reset_peak_memory_stats()` between the align step and the
diarization pipeline load, freeing real headroom before batching even comes
into play.

Result on retry: diarization stage went from >4h16m (never finished) to 3.3
minutes (completed cleanly), peak VRAM 1.04GB. Validate any future pyannote/
whisperx version bump against a short clip first (see `_load_wav_dict` note
above for the pattern) — a version change could silently move
`embedding_batch_size`/`segmentation_batch_size` off the plain-attribute
pattern this fix relies on. `transcribe.py` now guards this with a hasattr
check and prints a warning rather than failing silently if the attributes
disappear in a future pyannote release.

## Facebook Messenger CAN deliver transcript files — via the browser UI, not the API [2026-09-16, corrected same day]
First pass ruled this out: the Composio Facebook API connection
(`FACEBOOK_SEND_MEDIA_MESSAGE`) only accepts a public `media_url`, Drive's
`share_file` tool can only grant access to a specific email (no "anyone with
the link"), and pasting the transcript as chat text isn't viable (Messenger
caps ~2,000 characters/message, EP111's transcript is ~157,000 characters).

That API path is still a dead end, but Zac pushed back — correctly — that
browser automation was the obvious answer and should have been tried first,
not last. Using `claude-in-chrome` to drive Zac's actual logged-in Messenger
session (facebook.com/messages), the file input Messenger's own UI exposes
takes a real local file upload directly, same as a person clicking "attach
file" — no public URL needed at all. Confirmed working 2026-09-16: uploaded
EP111's transcript (154 KB, from the L: drive) via `file_upload` into Matt
Khourie's personal Messenger thread and sent it — delivered, confirmed in the
thread as "Sent."

**How to apply:** for delivering an actual file to a specific person over any
web platform (Messenger, or similar), check whether browser automation can
just use the site's native upload UI before assuming an API-only path (public
URL, specific-recipient share, etc.) is the only option — the UI upload
sidesteps API attachment limitations entirely.

**Locked 2026-09-16 (same session, after the EP111 test landed): Messenger
replaces email as the transcript delivery step.** Zac's call — the whole
reason he was testing this was to fix a real problem with the email step, so
once Messenger delivery was confirmed working he had me retire email outright
rather than run both. Root CLAUDE.md's FrostCast Transcription Workflow step 6
now describes the browser-automation send (navigate to
facebook.com/messages → find the attach-file input → `file_upload` the
transcript path → send → screenshot to confirm "Sent") instead of the old
Gmail send. Requires Zac's Chrome + the claude-in-chrome extension to be
available and logged into Facebook when this step runs — flag to Zac rather
than skipping silently if it isn't.

## Whisper's own transcribe batch_size was still hardcoded — separate OOM [2026-09-09]
The diarization batch-size fix above only covers the diarization stage.
`model.transcribe(audio, batch_size=16)` at the Whisper step was still
hardcoded and OOM'd on EP111 (102 min episode) on the 8GB RTX 5060, mid-run,
with the GPU otherwise clean (447MiB used, no games or other GPU load —
checked via `nvidia-smi` right after the crash). Added `--whisper-batch-size`
CLI flag, default 8 (was 16). Retry succeeded at 8. If a future long/dense
episode OOMs again at this step, drop to 4 before assuming something else is
wrong — large-v3 batches are much heavier per item than diarization
embeddings, so the safe batch size here is lower than the diarization one.
