# Decision Queue

Agents append. Zac clears. Nothing else writes.



**Blocked:** what cannot proceed

**Options:** A / B / C

**Recommendation:** which and why

**Status:** OPEN | DECIDED: <answer>

---

## [WKD-2026-09-01-01] 2026-09-01 | WKD | 3 live listings appear to violate the current-generation-airframe rule

**Blocked:** Root CLAUDE.md's hard rule states "Never use military insignia,
service marks, or current-generation airframe designations (F-35, F-22).
WWII-era subjects are safe." While pulling context for this week's WKD
digital-product recommendation, `data\etsy-listings-2026-08-20.csv` shows
at least 3 currently-live listings built around the F-35 specifically:
"F-35 Fighter Jet Digital Download | Printable Military Wall Art |
Aviation Poster" ($5.99), "F-35 Sunrise Takeoff Canvas | Fighter Jet Wall
Art | Veteran Gift" ($54.99), and the raw art asset "F-35 Stealth Aerial
Maneuver" also sits in the Military source folder unused as a listing yet.
This is not a new-listing decision (the rule clearly covers those going
forward) — it's a question of whether the 2 already-live F-35 listings
need to be pulled/deindexed retroactively. Deindexing an existing listing
is a real business call (loses whatever SEO/history it has, however thin)
that isn't mine to make unilaterally.

**Options:**
A. Deactivate both live F-35 listings (digital download + canvas) now,
   treat the rule as retroactive.
B. Leave the 2 live F-35 listings as-is (grandfathered, posted before the
   rule was set), just make sure no *new* F-35/current-gen-airframe
   listings go up going forward — rule applies prospectively only.
C. Leave as-is for now, revisit at the 15 NOV 26 rule review.

**Recommendation:** B. The rule reads as a going-forward safety guardrail
tied to the current listing-cap/anti-suspension window, not framed as a
retroactive catalog-scrub requirement, and these 2 listings have had
effectively zero traffic (per the 8/20 weekly pull) so the exposure is
low either way. Flagging rather than acting because pulling a live
listing is irreversible-ish (loses its listing age/any accumulated
signal) and Zac hasn't weighed in on retroactive scope.

**Status:** OPEN

---

## [WWD-2026-08-31-02] 2026-08-31 | WWD | Good Boy review: unconfirmed Shudder affiliation talk, joint Matt/Zac call

**Blocked:** devils-advocate's review of the Good Boy (2025) upload package
(WWD-2026-08-31-01, same folder) surfaced a real branding/business exposure
issue that is not mine to decide per WWD/CLAUDE.md's hard rule ("Format,
schedule, or branding changes are JOINT decisions with Matt.").

Transcript line 159 (Good Boy.txt, timecode 00:13:47:14): "And shudder is
the one who behind it... I'm working on getting us affiliated with that. We
are in talks." This is an unsigned business negotiation, said on tape,
during a positive review of a Shudder film. Left as-is in the final video
and in searchable metadata, it: (1) tells Shudder the pipeline is public
before terms exist, (2) reads as undisclosed sponsorship on an unpaid
review with nothing in the package saying so, (3) is a branding-adjacent
call the director protocol reserves for Matt and Zac jointly.

**Action already taken as a protective default, not a final decision:** I
removed the chapter title "Visual Style and Shudder Affiliation" from the
public-facing description/chapters (renamed, retimed per the review's other
finding that the timecode was wrong anyway) so the affiliation talk isn't
turned into a permanent, searchable YouTube chapter label while this is
open. This does NOT touch the actual video/audio, which I don't edit and
don't control - the raw talk is still on tape regardless of what the
description says.

**Options (as posed by devils-advocate):**
A. Cut the segment in the edit (Premiere). Removes the exposure entirely,
   costs the runtime and the personality of an unscripted aside.
B. Keep it in the final cut, add a plain disclosure line to the video
   description stating the review is unpaid and the Den has no current
   affiliation with Shudder. Keeps the moment, adds a compliance line.
C. Hold the upload until the Shudder deal (if any) actually settles one way
   or the other, publish once there's something real to disclose or nothing
   to worry about.

**Recommendation:** none offered by the reviewing agent beyond "Zac picks."
No recommendation from this director either, this is a business call about
a real external relationship neither agent has visibility into.

**Status:** OPEN

---

## [WWD-2026-08-31-01] 2026-08-31 | WWD | wwd-video-upload-package and wwd-shorts-clip-factory are not installed as skills

**Blocked:** WWD/CLAUDE.md's Related Skills section and the wwd-director
routing instructions both name wwd-video-upload-package and
wwd-shorts-clip-factory as the tools that run every FrostCast/Review "full
work up." Neither exists as an installed skill on this machine (confirmed
by directory check of D:\WKP\.claude\skills\ during this session - no
folder for either). This is not a one-off: The Last House package, EP103,
and now Good Boy (2025) have all hit this same gap, each time worked around
by hand-building the package from formats\<TYPE>.md plus the skill
description in CLAUDE.md, and none of the three prior occurrences got
formally queued.

**Options:**
A. Build real skill definitions for both (SKILL.md + any supporting
   scripts) so future runs get consistent, tool-driven output instead of a
   hand-built package that varies slightly by whichever session builds it.
B. Formally retire the two skill names from CLAUDE.md/director routing and
   document "hand-build from the format spec" as the actual permanent
   process, since that's what's happened 3 times running.
C. Leave it ad hoc, decide per-run (current state, same problem as the
   devils-advocate gap before it got fixed).

**Recommendation:** A for wwd-video-upload-package at minimum, since its
output structure (title, description, chapters, tags, thumbnail concept,
shorts candidates, FB/IG posts, end screens, posting schedule) is now
stable across 3 real runs and could be templated. B may be the more honest
call for wwd-shorts-clip-factory specifically, since actually cutting video
requires real source access and ffmpeg work that a director session can
already do by hand when the source file is reachable (done successfully
this session for Good Boy).

**Status:** OPEN

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