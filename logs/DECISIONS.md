# Decision Queue

Agents append. Zac clears. Nothing else writes.



**Blocked:** what cannot proceed

**Options:** A / B / C

**Recommendation:** which and why

**Status:** OPEN | DECIDED: <answer>

---

## [KP-2026-09-17-01] 2026-09-17 | Kingdom Planners | Shop launch stalled 10 days on $29 setup fee, MAIN EFFORT venture blocked on first revenue

**Blocked:** Kingdom Planners (MAIN EFFORT, seven products finished, zero
listings) has been Blocked since 2026-09-07 on Etsy's one-time $29
shop-setup fee, which Zac doesn't have on hand. Nightly rollup for
2026-09-17 found no update to this task in TASKS.md since it was opened —
10 days stalled on the single gating item between a finished product
pipeline and the venture's first possible revenue.

**Options:**
A. Wait for the $29 to be available from normal cash flow, no other
   action in the meantime.
B. Keep the shop-launch step blocked but confirm the free, no-money-down
   per-listing prep work (titles, 13 tags, descriptions, photos/mockups,
   pricing for the 5 unpriced products) is actively moving — that task
   is listed Not Started, same as the blocked shop-creation task, so the
   parallel work doesn't appear to be happening either.
C. Treat the $29 as a small near-term expense worth prioritizing given
   it unlocks the MAIN EFFORT venture's first revenue, and flag it as
   such rather than leaving it to resolve itself.

**Recommendation:** B — nothing about the $29 gate can be worked around
by an agent (spending money is Zac's call, per the Escalation rule), but
the free prep work sitting equally untouched means MAIN EFFORT is fully
idle right now, not just waiting on funds. Worth Zac confirming whether
prep work is actually in progress or also stalled.

**Status:** OPEN

---

## [WWD-2026-09-17-01] 2026-09-17 | WWD | Higgsfield credits still at 0 — blocks cold open AND all weekly images, no cost analysis done yet

**Blocked:** Cold open (Warden character designs) and all weekly WWD
image generation have been blocked on Higgsfield credits at 0 (free
plan) since at least 2026-08-10, still 0 as of the last confirmed check.
Zac has twice punted the cold-open deadline (now ~2026-09-25, an 8-day
runway from tonight). TASKS.md notes a "cost analysis" for topping up
credits is still pending and has been pending the whole time this has
been blocked — no analysis exists yet for Zac to act on.

**Options:**
A. Run the credits cost analysis now (what Higgsfield tier/spend covers
   the actual weekly image volume this venture needs) so Zac has a
   concrete number to say yes/no to, instead of an open-ended "credits
   are empty."
B. Leave it as-is and wait for Zac to raise it himself.
C. Keep substituting the free workaround already used once (Firefly
   prompts instead of generated art, as done for the 2026-08-10 weekly
   package) as a standing stopgap while credits stay at 0.

**Recommendation:** A — the ~9/25 target is only 8 days out and nothing
in the task notes suggests the cost analysis is scheduled. Turning this
into a specific spend number now gives Zac a fast decision instead of
another silent slip.

**Status:** OPEN

---

## [FF-2026-09-12-01] 2026-09-12 | Fantasy Football | Pick'em card marking scheme unconfirmed — Week 1 card reads as fully blank

**Blocked:** Built the Sunday Dashboard's pick'em panel against
`Fantasy-Football\cards\CODENAME_Week1 Entry.xls` and found every one of
the 20 ATS games, the Eliminator Challenge pick, and the Monday-night
tiebreaker score cell empty — no team name retyped, no "X", no cell
value of any kind in the FAVORED/UNDERDOG/EC columns. Checked cell
background fill too (via `xlrd formatting_info=True`) in case picks are
marked by highlight rather than text — the yellow EC-column fill and
the other template colors are static/decorative across every row
whether or not that row has a pick, so fill color isn't the signal
either. Two different explanations fit what's on disk, and guessing
wrong means the dashboard could silently show "no picks" as if that
were a real, checked state:

**Options:**
A. The card is genuinely not filled in yet for Week 1 — Zac hasn't made
   his picks. Dashboard should show "no picks recorded for this week"
   plainly, per the doc's own rule ("if the file is missing, say so —
   do not fall back and pretend"), same handling extended to "file
   present but empty."
B. Picks get marked some other way this skill hasn't seen yet — a
   different cell, a comment, a second sheet, or a convention only
   visible once a filled-in prior week's card exists to compare against.
   No prior week's card exists on disk to check this against (Week 1 is
   the first week of the season).

**Recommendation:** A, provisionally — nothing in the file contradicts
"not filled in yet," and CLAUDE.md/SKILL.md text ("blank cells adjacent
to each label are the input fields") reads consistent with typed text
that simply isn't there yet. But this is a guess dressed as a
recommendation, not a confirmed mechanism, so Phase 1 ships built to
read the pick columns as specified and displays "no picks recorded"
rather than inventing coverage numbers from an empty sheet. Confirm the
real marking convention once Zac fills in a card (or ask him directly)
so the parser can be checked against a real filled example instead of
guessed at.

**Status:** DECIDED: neither A nor B as guessed — Zac confirmed directly
2026-09-13: picks are marked by **filled cell background color** on
the favored/underdog cell (option B, a convention this skill hadn't
seen), and the real file being checked was the wrong one — the actual
submitted card lives at `D:\Documents\Pickups 2026\Sanders_Week{N}
Entry.xls`, not `Fantasy-Football\cards\` (blank templates only).
Verified against the real Week 1 card: 20/20 picks parsed cleanly (19
games + the Monday-night tiebreaker), zero rows with zero or multiple
filled cells. `pickem_card.py`, the dashboard, and the accuracy
tracker's logger all updated to read fill color from the real path.
Closed.

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

**Status:** RESOLVED: Option B — leave the 2 live F-35 listings as-is (grandfathered), no new current-gen-airframe listings going forward. Zac's call 2026-09-04.

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

**Update 2026-09-04 (Zac):** Affiliation talks haven't actually happened yet
("I have not got the affiliation just yet, need to know where to start
really") — the "in talks" line on tape is ahead of where things actually
stand.

**Zac's call 2026-09-04:** leave the line in the final cut as-is (no cut,
no disclosure line) — it shows the audience real progress is being made.
Delivered `reports\wwd\Shudder-Affiliate-Guide-2026-09-04.docx/.md` —
two real paths (Impact affiliate program, and direct AMC Global Media
partnerships outreach), a ready-to-send email, and a ready-to-send short
message. Zac to actually send these; not something an agent can do
unprompted. Still worth a heads-up to Matt since format/branding calls are
joint, but the "leave the line in" call itself is made.

**Status:** RESOLVED: leave the line in, pursue real affiliation via the
guide above. Revisit if nothing lands in a few weeks (see the guide's
"recommended order of operations," step 4).

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

**Update 2026-09-04:** Zac asked how Good Boy's package got built without
the skills existing. Answer: it was hand-built directly from the format
spec (WWD/CLAUDE.md + `formats\*.md`) by the director session in-chat —
there is no actual installed skill running underneath it. Same as The Last
House and EP103.

**Zac's call 2026-09-04:** "The skill is there now." A real installed
skill (`wwd-review-pipeline`) now exists covering this exact ground —
full upload package, audio extraction, shorts cutting, per-clip captions.
WWD/CLAUDE.md's Related Skills section updated to point at it in place of
the two names that never existed. Effectively Option A, closed.

**Status:** RESOLVED: Option A — wwd-review-pipeline is the real skill
now installed and referenced in WWD/CLAUDE.md.

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

**Update 2026-09-04 (Zac):** Skip the two exit tests — trust it as-is.
devils-advocate is now a standing part of the WWD run chain. Closed.

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

---

## [WWD-2026-09-18-01] 2026-09-18 | WWD | Surfshark sponsor read has an unresolved FTC disclosure question, read is due to air imminently

**Blocked:** The Surfshark sponsor-read task (finalized 2026-09-14,
`L:\Winter Wolfs Den review show\Sponsors\Surfshark\Surfshark-Sponsor-Reads-2026-09-14.md`/`.docx`)
carries a "STILL NEEDS" item that has sat open since it was written and
was never queued here: an attorney check on whether the written
disclosure has to sit physically next to the affiliate link in the video
description/pinned comment, or a spoken disclosure in the read itself is
enough. `clearance`'s second pass flagged this explicitly and
`marketing-director`'s log independently notes "real money attached means
a real attorney/Surfshark brand approval pass still belongs in the loop
before this airs." This is real affiliate revenue (rev-share, not a flat
fee) and an FTC compliance question, not something an agent should
resolve by guessing. Time pressure: EP111 (carrying the read) was
recorded 2026-09-16, and Heat's release lands today, 2026-09-18, in the
same posting week the read is meant to go out — the window to fix
placement before anything airs may already be closing.

**Options:**
A. Get an actual attorney/compliance read on FTC placement rules before
   EP111 airs, hold the sponsor segment out of the upload until that's
   answered.
B. Ship with the spoken in-read disclosure already in the script (per
   TASKS.md, both scripts already have explicit spoken paid-partnership
   disclosure) and add the written link-adjacent disclosure line as a
   belt-and-suspenders precaution, without waiting on formal legal
   sign-off, since the affiliate program's own disclosure requirements
   were part of what got Surfshark's approval already.
C. Leave the description/pinned-comment wording as currently drafted and
   accept the risk as low given the spoken disclosure already exists.

**Recommendation:** B — the read already discloses verbally per
TASKS.md's own notes, so the incremental step (adding a plain written
line next to the link) is cheap insurance while a real legal opinion is
pursued in parallel rather than gating the whole episode on it. This is
still Zac's call given it involves both money and legal exposure.

**Status:** OPEN

---

## [WWD-2026-09-26-01] 2026-09-26 | WWD | Cold open deadline (9/25) passed with no update — same Higgsfield-credit block as WWD-2026-09-17-01, now overdue

**Blocked:** TASKS.md lists the cold open (Warden character designs) target
as "~2026-09-25 (was ~mid-to-late Sept)," punted there by Zac's call on
2026-09-04. That date was yesterday. The only commit in the last 24 hours
(`4616083`, weekly numbers pull) doesn't touch this task, WWD/CLAUDE.md, or
the Higgsfield credit balance, and WWD-2026-09-17-01 (still OPEN) already
flagged that the cost analysis for topping up credits hadn't been done as
of 2026-09-17. Nothing in the repo shows that analysis exists now either,
nine days later. This is the third deadline on the same block (originally
~early Sept, then ~mid-to-late Sept, then ~9/25) with no visible movement
on the underlying gate.

**Options:**
A. Treat this as the same open decision as WWD-2026-09-17-01 and just wait
   for Zac to resolve it — no new entry needed, folds into that one.
B. Escalate now that a third deadline has passed without the cost analysis
   Zac was already asked to review, since repeatedly slipping the same date
   without new information suggests the credit-topup decision itself, not
   the deadline, is the actual blocker.
C. Recommend the venture director re-date the cold open to "unscheduled"
   until the Higgsfield/Firefly decision is made, rather than carrying a
   fourth punt silently.

**Recommendation:** B — this repeats an already-open decision rather than
introducing a new fact, but three missed dates on the same unresolved spend
question is worth surfacing again instead of letting it go stale silently.
No agent can spend company money on Higgsfield credits without Zac's say-so
per the Escalation rule, and the free Firefly fallback stays available if
he'd rather skip the spend than the analysis.

**Status:** OPEN

---

## [WWD-2026-09-26-02] 2026-09-26 | WWD | Heat (1995) review shows "In Progress" and a confirmed 9/18 release in TASKS.md, but does not appear in the latest YouTube pull

**Blocked:** `data/weekly-2026-09-25.md` (VidIQ pull, run 2026-09-25, real
numbers not guessed) checked the newest 30 videos on the Winter Wolf's Den
channel and found no "Heat (1995)" review video, despite TASKS.md stating
the release day was "confirmed Friday 2026-09-18 (locked, no more flex)" by
Zac on 2026-09-14. TASKS.md still lists the task as "In Progress," not
Done, and no commit since then updates its status either way. Three
explanations fit what's on disk and an agent can't tell which without
checking the channel directly: the video published under a different or
retitled name, the 9/18 date slipped without TASKS.md being corrected, or
it's further back in upload history than the newest-30 window checked.
Reporting this as released, or as still pending, without verifying would
violate the Honesty rule.

**Options:**
A. Assume it shipped under a different title and move on — risks silently
   missing a real slip if it didn't ship at all.
B. Assume the 9/18 date slipped and treat it as still blocked/late — risks
   wrongly flagging something that already shipped under a different title.
C. Flag the discrepancy and have Zac or wwd-director confirm directly
   against the channel/upload history, not guessed.

**Recommendation:** C — a five-minute check for whoever has channel access
settles this. TASKS.md should then get corrected to Done (with a link) or
to a real new date, whichever is true, rather than sitting on a locked date
that already passed silently.

**Status:** OPEN