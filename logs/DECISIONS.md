# Decision Queue

Agents append. Zac clears. Nothing else writes.



**Blocked:** what cannot proceed

**Options:** A / B / C

**Recommendation:** which and why

**Status:** OPEN | DECIDED: <answer>

---

## [WWD-2026-08-20-01] 2026-08-20 | WWD | No devils-advocate agent exists to review WWD packages before ship

**Blocked:** WWD director protocol requires handing every draft to a
devils-advocate agent with the format spec path before anything ships. That
agent type does not exist in this environment's available roster (only claude,
claude-code-guide, Explore, general-purpose, Plan, statusline-setup,
wwd-director). Not a one-off, this will recur on every future WWD package,
review, and script unless resolved.

**Options:**
A. Build a proper devils-advocate agent definition (.claude/agents/) so future
   runs get a real, purpose-built adversarial reviewer.
B. Standardize on using general-purpose with an explicit adversarial-review
   prompt as the permanent substitute, and update WWD/CLAUDE.md's hard rule to
   say so plainly instead of naming an agent that doesn't exist.
C. Leave it ad hoc, each director run decides in the moment (current state,
   not sustainable, inconsistent review quality).

**Recommendation:** A. This session's stand-in (general-purpose, briefed
adversarially) caught four real issues (em dashes in internal notes, an
unverifiable host attribution, two chapter-title inconsistencies, one
cherry-picked stat), so the review step has proven value. A dedicated agent
definition would make that review consistent run to run instead of depending
on how well each director happens to brief a generic substitute.

**Status:** DECIDED: Option A. devils-advocate.md created in .claude/agents/ 20 AUG. Needs its two exit tests run before trusting.

**Update 2026-08-26 (jarvis):** devils-advocate.md existed but was never
registering in the agent roster — file was missing its opening `---`
frontmatter fence (started straight at `name:` instead of `---` then
`name:`), so every session silently fell back to the general-purpose
stand-in. Fixed (added the fence). Still needs the two exit tests run
before trusting it as the real reviewer.

---

## [SYS-01] 2026-08-19 | SYSTEM | Agent files arriving HTML-escaped
**Issue:** All 4 agent .md files written with &#x20; instead of
spaces and backslash-escaped markdown (\#, \*, \-). Fixed manually
in VS Code. wwd-director hit this twice.
**Suspected cause:** content copied from rendered view rather than
raw code block.
**Next time:** use the code block copy button, then verify with
`type <file>` before trusting it.
**Status:** OPEN - watch for recurrence

---

## [WWD-2026-08-27-01] 2026-08-27 | WWD | EP109 transcription stalled in diarization, killed - needs a retry-approach decision

**Blocked:** EP109's transcription run (91:36 episode) completed Whisper
transcribe+align fine (22m 39s) but never finished the diarization stage -
ran 4h16m before being killed at 3:33 AM, past the pre-agreed 4-hour
timebox. Root cause found and verified (see logs\wwd-director.md
2026-08-26/27 entry): pyannote's installed pipeline defaults
`embedding_batch_size`/`segmentation_batch_size` to 1, forcing fully
serial GPU calls across the whole file - a real architectural slowness,
not a bug, though the actual kill was triggered by a fresh CPU-delta
check going flat (+0.015s over 20s) right at the deadline, suggesting it
may have also genuinely hung right around then rather than just being
slow the whole way through. No transcript exists for EP109. Source .mp4
is untouched.

**Options:**
A. Just rerun as-is overnight/whenever GPU is free again - accept the
   4+ hour runtime (or longer) as the cost of doing business on this
   8GB card, no script changes.
B. First test the batch-size theory on a short 5-10 min clip cut from
   EP109's audio, to confirm the slowness is audio-length/serial-call
   driven before spending another 4+ hours on the full file.
C. Modify transcribe.py to expose `embedding_batch_size`/
   `segmentation_batch_size` as parameters and try a higher value on a
   short clip first (VRAM permitting on 8GB) - addresses the root cause
   directly instead of just tolerating it, but is a script change to
   scripts\wwd-video-transcriber\ that should get a look before trusting
   it on the full file.

**Recommendation:** C, but B as the immediate first move regardless -
confirm the theory cheaply on a short clip (a few minutes, one GPU-idle
window) before touching the script or committing another 4-hour run to
the full episode. Don't just rerun as-is (A) without at least the cheap
B test, since Wednesday-to-Wednesday means EP109 will otherwise eat
another entire overnight window for the same outcome if the real cause
turns out to be something else.

**Status:** DECIDED: Option C. Zac's call 2026-08-27 - fix
transcribe.py to expose the batch-size params, then retry EP109.

**Update 2026-08-27 (wwd-director):** Done. transcribe.py now exposes
`--embedding-batch-size`/`--segmentation-batch-size` (default 8/8),
plus a related fix found in the same pass - Whisper/align models were
never freed from VRAM before diarization loaded, which was inflating
the diarization-stage VRAM figure. Validated on a 4-min clip before
committing to the full file (diarization completed in 0.2 min, no
OOM). Full EP109 retry: diarization completed in 3.3 minutes, vs.
4h16m last night without finishing. Transcript, chapters, and full
numbers in logs\wwd-director.md 2026-08-27 07:15-07:37 entry. Closed.