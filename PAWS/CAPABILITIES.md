# Scout - Capabilities

## Fetch

**V1 - ships with the first build.**
Location search by filename, folder, and file date across a fixed set
of scoped locations. Not a full-drive search - scoped deliberately so
Scout never digs somewhere it wasn't meant to, and so results come
back fast.

Proposed default scope, NOT YET CONFIRMED:
D:\WKP, Documents, Downloads, Desktop, L:
Confirm or correct this list before building the index.

Trigger: "Scout, fetch the VA tracker" or equivalent, spoken or typed
in the companion app. Scout searches the scoped locations and either
surfaces the result on the companion app or opens it directly on the
PC.

**V2 - later upgrade, not required for v1.**
Content-aware search. Photo metadata (capture date, location if
present) for "find the picture from the PCS move" style requests
where the filename means nothing. Eventually genuine visual content
matching - understanding what's IN an image, not just what it's named
or when it was taken. Real engineering, sequenced after v1 proves the
concept works at all.

## Data management - new direction, not yet fully specced

Introduced 9 SEP 2026: physical media ports - SD card mentioned
specifically - so Scout can scan inserted storage, identify what's on
it, and sort files to where they belong. If it doesn't know where
something goes, it asks rather than guessing.

This is a real direction, not a locked spec. Before building it,
resolve:
- Which port - SD, USB-A, both.
- Read-only scan-and-suggest, or read-write move-and-file.
- Confirmation rule - the safe default is Scout NEVER moves or
  deletes a file without asking first, every time, no "trust me"
  mode. State this explicitly before writing a line of code for it.

## Connectivity

**PC** - solved already. Reads D:\WKP\dashboard\data\ directly. No
new work.

Note, checked 24 SEP 2026: D:\WKP\dashboard\data\ does not exist on
disk yet. wkp-daily-brief and wkp-monday-brief (the two skills the
character bible names as the source) currently render straight to a
dashboard/report, not to JSON files at that path. "Solved already" is
the target architecture, not the current state. This blocks the event
reaction and end-of-day recap capabilities below until the JSON write
step actually exists. Flagging here rather than in a decision queue -
this is an engineering prerequisite, not a scope call for Zac.

**Phone (Android)** - v1 feature. Companion app over WiFi or
Bluetooth. Two-way: receives Scout's status, and Scout can push
notifications back out. This is what makes Scout more than a
dashboard - it reaches the owner instead of waiting to be checked.

**Watch** - deferred deliberately. Its own project, not a v1 feature.
Ecosystem not yet chosen - Android is confirmed for phone, which
points toward Wear OS as the likely path, but this is not decided.
Pick one platform once Scout has proven itself worth wearing.

## Touch-to-act - proposed, NOT YET CONFIRMED

Added 24 SEP 2026, from the engagement brainstorm on why the daily
loop is currently one touchpoint. The screen on the Waveshare
ESP32-S3-Touch-LCD-1.69 is a capacitive touchscreen. Right now nothing
reads a tap - mood display is read-only. This turns Scout from a
status light into a control surface.

What it does: tap Scout to mark the current top task done, tap a
second zone to snooze a flagged decision, tap a third to cycle to the
next calendar item - three or four hit zones on the round display,
not a menu system. The action fires immediately, matching Scout's
"reflects what's true" character - no confirmation dialog fatigue,
but a hold-to-confirm gesture (not a bare tap) on anything that writes
data back out, so a mis-tap can't silently mark a task done.

What's genuinely new versus what's reused: touch hardware itself is
native to the board, no new part. What's new is a write-back path -
today Scout only reads JSON, it never writes anything back to a task
source. That write path depends entirely on PAWS-001 (task source)
being resolved first, since "mark done" has to call whatever API that
source has. Also new: touch-zone hit-testing in firmware, and the
hold-to-confirm gesture logic.

Sequencing: this is a Phase 1B/2 item, after the state machine and
Fetch v1, not part of the Taskagotchi MVP - it depends on PAWS-001 the
same way the rest of the integration layer does, so it cannot start
before that decision lands regardless of priority.

## Event reactions - proposed, NOT YET CONFIRMED

Added 24 SEP 2026. Distinct from the two steady-state moods (Thriving,
Buried) and the special-event layer (birthday/anniversary) already in
the character bible - this is a one-off animated reaction to a
specific thing that just happened, layered briefly on top of whatever
the steady-state mood already is, the same way the special-event layer
works.

Candidate triggers, checked against what data actually exists today:
- A FrostCast/WWD episode goes live - FEASIBLE. Detectable by reading
  new "Released"/"live" entries in logs\wwd-director.md since Scout's
  last check. Existing log format, no new infrastructure.
- A decision in DECISIONS.md gets marked RESOLVED - FEASIBLE.
  Detectable the same way, reading decisions\DECISIONS.md for new
  RESOLVED entries. Existing file format, no new infrastructure.
- An Etsy sale happens - NOT FEASIBLE without new infrastructure.
  Etsy has no traffic or sales API export (root CLAUDE.md: "Etsy
  provides NO traffic CSV export... typed by hand each Friday").
  There is no live signal to react to. Do not build this trigger
  until that changes - it would either be fake (react to nothing) or
  require a genuinely new data source, which is its own proposal.

What's genuinely new: an event-diff watcher - Scout has to remember
what it last saw in each log/decision file and compare on each check-
in, not just read current state the way the mood engine does today.
This is not real-time push - Scout only sees an event on its next
scheduled data check, so "reaction" means "most recent event since
last check," not live notification. State that expectation plainly
rather than overselling it as instant.

## The USB-C hub is the retention anchor, not a feature to add

Added 24 SEP 2026, worth stating explicitly rather than leaving
implicit. Zac's actual concern was that a pure pet loop goes stale
after a week and the device becomes furniture. The fused
hub-plus-personality bet already made in CLAUDE.md is the real answer
to that, not something the six capabilities on this page need to
solve on their own: because Scout is also a working USB-C hub, the
object stays physically plugged into the desk and in daily use -
charging a laptop, passing through peripherals - independent of
whether the owner is currently engaged with the character layer at
all. A pet that gets ignored still has a job. A hub that gets ignored
doesn't.

Design implication worth carrying into FIRMWARE and ENCLOSURE work
when that starts: the hub passthrough must stay fully functional even
if the ESP32-S3 side crashes, is mid-flash, loses wifi, or is asleep.
The two subsystems share an enclosure, not a dependency - hub function
should never be gated on personality-module health. Flag this as a
firmware and enclosure design constraint, not just a marketing point.

## Data management - promoted toward a v1 candidate, still open items below

Introduced 9 SEP 2026 as a new direction, not yet specced. Updated 24
SEP 2026: Zac tied this directly to a real recurring workflow he
already does by hand - WWD picture pulls (per LOCAL-PATHS.md, `L:\
Winter Wolfs Den review show\Raw Footage\`), B-roll imports, and Etsy
photo batches (`E:\04 Warrior King Desins`, `D:\04 New Warrior King
Designs\_Print Exports`). That's enough of a concrete, repeat use case
to move this off the pure-backlog Horizon list toward a real v1
candidate - still not locked, still has open items below, but no
longer "not yet specced enough to schedule."

Proposed v1 shape:
- Port: SD card, not USB-A. Matches the original 9 SEP framing and
  sidesteps the USB-A/OTG host-mode question on the ESP32-S3 (see
  PARTS-RESEARCH.md for what's actually confirmed about that).
- Read-only scan-and-suggest only for v1. Scout scans an inserted SD
  card, reads file type and date metadata, and matches against known
  folder conventions (the WWD Raw Footage structure, the WKD export
  structure in LOCAL-PATHS.md) to suggest a destination.
- Confirmation rule carries over unchanged and stays locked: Scout
  never moves or deletes a file without asking first, every time, no
  "trust me" mode.
- Architecture note worth flagging now, before this gets scheduled:
  the ESP32-S3 reading an SD card can identify files, but the actual
  move into `D:\WKP` or `L:\` folders has to happen on the PC or
  through the companion app, which have real filesystem/network
  access - the microcontroller itself is not positioned to write into
  those drives. Any v1 build has to route the confirmed move through
  the companion app or a PC-side helper, not attempt it on-device.

Still open before this can schedule into an actual phase: which
folder-convention rules Scout applies for suggestions (start with WWD
and WKD since those are the concrete cases Zac named, expand later),
and where in the phase sequence this lands - realistically after the
companion app and Fetch v1, since it depends on the same PC-write path
Fetch already needs solved.

Added 24 SEP 2026, from PARTS-RESEARCH.md: a real hardware conflict,
not just an open spec question. A raw SD card breakout over SPI needs
four GPIO pins, and the Waveshare ESP32-S3-Touch-LCD-1.69 only exposes
four free pins total on its header - which are the same pins the
planned I2S voice-line audio needs three of. SD and audio cannot both
run natively on the current board at the same time. See PAWS-007 in
decisions\DECISIONS.md - this has to resolve before SD-port work can
actually schedule into a phase, on top of the folder-convention and
sequencing items above.

## End-of-day recap - proposed, NOT YET CONFIRMED

Added 24 SEP 2026. Closes the loop the morning mood-check opens - Zac
checks Scout's mood in the morning, this gives him one thing back at
the end of the day instead of the loop being entirely one-directional.

What it does: at a set evening time, Scout surfaces one real
completed thing from that day - not a list, one item, matching the
"Top three, not everything" discipline wkp-daily-brief already uses.

Data source: this reuses infrastructure that already exists rather
than requiring anything new - TASKS.md rows that flipped to Done
today, and today-dated entries in any venture's logs\*.md. This is
functionally the same read wkp-daily-brief already does for its
"Yesterday" section, just re-timed to run the same evening instead of
the next morning. No new data pipeline required, unlike event
reactions above - this can be built once the JSON-to-dashboard-data
write path exists (see the Connectivity note above) or, as an interim
version, by reading TASKS.md and logs\*.md directly the way the brief
skills already do.

Selection logic still needs a rule: when multiple things completed in
a day, pick the most concrete/highest-effort one, not the first one
alphabetically or the most recent. Worth borrowing whatever heuristic
wkp-daily-brief's "Top three" already uses for prioritization rather
than inventing a second one.

## Proactive push notifications - made concrete

Companion app push was already planned (see Connectivity above,
"Scout can push notifications back out"). Added 24 SEP 2026: which
specific nudges are worth sending, since an unfiltered list turns into
noise and starts to look like the manipulative "come back or I'll be
sad" bait the character bible explicitly rules out.

Nudges worth sending, each tied to a real tracked constraint, not an
invented one:
- "Etsy's weekly cap resets today" - ties to the locked Etsy listing
  cap rule in root CLAUDE.md (max 3/day, 8/week combined shops).
- "A decision's been open 5+ days" - ties to decisions\DECISIONS.md
  aging. Delivered in Scout's concern-for-you voice, not a nag.
- "FrostCast records tonight" - ties to the standing Wednesday 9pm
  commitment in root CLAUDE.md.
- "[Venture] has been flagged BLOCKED for N days" - ties directly to
  what already drives the Buried mood state, but gives it a specific,
  named reason instead of just a low-energy animation.
- "Etsy's Friday data pull is due" - ties to the manual, easy-to-miss
  hand-typed data rule (data\etsy-manual-YYYY-MM-DD.md).

Explicitly not a nudge: per-task reminders (that's a duplicate to-do
list, not Scout's job), a ping for every single decision queued
(aged ones only), or any "you haven't checked me today" message -
that is the exact bait pattern the character bible rules out by name.

Rule to carry into the build: cap proactive pushes at roughly one or
two a day, and require every nudge to trace to a constraint that is
already tracked somewhere in the repo (a locked rule, an aging
decision, a standing commitment, a BLOCKED flag) - never an invented
sense of urgency.
