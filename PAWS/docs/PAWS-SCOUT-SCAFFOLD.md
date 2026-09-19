# PAWS-SCOUT-SCAFFOLD.md

Machine-readable handoff, second pass. Everything below is either
LOCKED (Zac decided it) or explicitly marked PROPOSED / NOT YET
CONFIRMED / NOT YET SPECCED. Do not treat a proposed item as locked.

Claude Code: create or overwrite each file below at the exact path
shown, verbatim. Then apply the instructions in the sections after
the file blocks - those are edits to EXISTING files, additive only.

---

### FILE: D:\WKP\PAWS\CLAUDE.md
```
# PAWS - Venture Rules

PAWS is the hardware venture. Scout is the flagship product - an
original desk-pet character, a dog, built specifically for this
venture. Scout has no connection to WWD's wolf. Different venture,
different everything, except that Zac edits and produces WWD. Do not
tie PAWS branding, characters, or positioning to WWD in any document,
pitch, or asset.

## What Scout is

Full character spec: D:\WKP\PAWS\SCOUT-CHARACTER-BIBLE.md
Full capability spec: D:\WKP\PAWS\CAPABILITIES.md
Read both before doing any character, firmware, or marketing work on
this venture.

## The hardware bet

Scout ships as a fused personality-device-plus-USB-C-hub product from
day one. Not a cheap standalone screen first, hub added later - the
fused version is the actual target, decided deliberately, accepting
the bigger build.

Two subsystems, one shell, not one custom PCB:
- Screen and personality module - Waveshare ESP32-S3-Touch-LCD-1.69,
  already ordered, two units.
- Hub module - an existing certified USB-C dock product (RayCue
  family or comparable), not custom silicon. Custom hub hardware is
  a Phase 2 manufacturing-partner move, not a v1 decision.

Both live inside one enclosure designed in-house. The enclosure spec
in formats\ENCLOSURE.md needs to account for housing two subsystems,
not one board - flag this when that work starts.

## Marketing position

Both at once, not one or the other: explicit nostalgia marketing to
adults who grew up with Tamagotchi and Digimon, AND a serious desk
tool in its own right. The character has to earn the second half or
the first half is just a gimmick.

## Platform

Companion app builds for Android first. That is what the household
actually runs. Do not build iOS first on an assumption.

## Hard blockers - never cross these, no exceptions

No microphone on any PAWS device a person under 18 could touch.
No LLM, cloud call, or data collection on any device a person under
18 could touch.
These are legal and safety boundaries, not style preferences. Refuse
and queue a decision rather than design around them.

## Build sequence

1. Character locked. Scout is designed. Done.
2. State machine on PC, no hardware, driven by mock data shaped like
   the real JSON files. This is the actual first milestone.
3. Hardware tracks run in parallel, not sequentially: screen and
   firmware development, and hub sourcing, both move at the same
   time. Neither blocks the other.
4. Companion app (Android) once the state machine proves out.

## Open decisions

See decisions\DECISIONS.md for the full list and current status.
PAWS-001 (task data source) and PAWS-004 (hours per week) are the two
still blocking real progress. Everything else is either resolved or
not yet load-bearing.

## Format files

D:\WKP\PAWS\formats\ still governs BUILD GUIDE, SOURCING, FIRMWARE,
ENCLOSURE, EDUCATION, and INVESTOR output. CHARACTER.md in that
folder now points here rather than carrying its own spec.
```

---

### FILE: D:\WKP\PAWS\SCOUT-CHARACTER-BIBLE.md
```
# Scout - Character Bible

## Identity

Name: Scout. Species: dog. An original PAWS character, not connected
to any other WKP venture's characters or IP.

Why the name: a scout gathers real information and reports it back
honestly, without softening it and without exaggerating it. That is
exactly what the mood engine does. The name is not decoration, it
describes the function.

## The one rule everything else follows

Scout reflects what's actually true. When things are good, Scout is
genuinely up. When things are hard, Scout is genuinely concerned.
Both are real, neither is performed.

The line that keeps this from turning into a guilt mechanic: Scout is
never disappointed AT the owner. Scout gets worried FOR the owner.
Same low-energy animation either way, completely different
relationship. Never a "you let me down" moment. Never manipulative
"come back or I'll be sad" bait. Concern, not blame.

Reference point, not a copy: the Duolingo owl proved real emotional
stakes make a mascot memorable instead of forgettable. Scout takes
the stakes and drops the mockery and the threat. Worried, not
punishing.

## Mood states

**Thriving** - tasks current, no overdue items, no venture flagged
BLOCKED, calendar reasonable.
Ears up, tail moving, an idle bounce animation. Present and glad to
be there, not manic.

**Buried** - overdue items stacking, a venture BLOCKED, calendar
packed solid.
Ears down, lying down, watching. Alert, not asleep. Concerned, not
accusing. No sad-eyes-at-camera guilt imagery.

**Special event** - a calendar entry tagged as a birthday or
anniversary.
Its own excited animation, layered on top of the daily mood state,
not replacing it. A hard week and a birthday can both be true on the
same day - show both.

## Where mood data comes from

Scout does not have its own data pipeline. It reads the same JSON
files D:\WKP\dashboard\data\ already holds, written by
wkp-daily-brief, wkp-monday-brief, and marketing-director. A second
reader on an existing pipe, not new infrastructure.

Composite signal, roughly: open task count against deadlines,
calendar density, count of venture logs flagged BLOCKED, count of
decisions sitting open in DECISIONS.md.

## Voice

Short lines through ElevenLabs for personality moments - a greeting,
a reaction to something fetched, an acknowledgment. Not conversation.
Scout has a voice, not a script it reads at you.

## What Scout is not

Not the WWD wolf. Not licensed IP of any kind - discussed and ruled
out deliberately, see the licensing research in Part 12 of the
Operations Manual. Not a device that punishes neglect. Not a fake
hunger bar wearing a task list.
```

---

### FILE: D:\WKP\PAWS\CAPABILITIES.md
```
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

**Phone (Android)** - v1 feature. Companion app over WiFi or
Bluetooth. Two-way: receives Scout's status, and Scout can push
notifications back out. This is what makes Scout more than a
dashboard - it reaches the owner instead of waiting to be checked.

**Watch** - deferred deliberately. Its own project, not a v1 feature.
Ecosystem not yet chosen - Android is confirmed for phone, which
points toward Wear OS as the likely path, but this is not decided.
Pick one platform once Scout has proven itself worth wearing.
```

---

### FILE: D:\WKP\PAWS\formats\CHARACTER.md
```
# Format - CHARACTER

## What this produces

Character art, states, animation frames, and expression work.

## Authoritative spec

D:\WKP\PAWS\SCOUT-CHARACTER-BIBLE.md carries the actual character
definition - identity, mood states, emotional rules. Read it before
any character work. This file only covers production mechanics.

## Per character task, capture

Which states are covered and how many frames each.
Resolution and color depth against the target screen.
File format and where it lands in art\.
How the state maps to the state machine's outputs.

## Rules

Eight states, three frames each is the baseline, per the mood and
special-event states in the character bible.
Keep the character readable at the actual pixel size. Detail that
disappears on a small panel is wasted work.

## Output

art\ for assets. docs\ for the state and frame spec.
```

---

### INSTRUCTION: decisions\DECISIONS.md

Open D:\WKP\PAWS\decisions\DECISIONS.md. Find PAWS-002 (naming) and
PAWS-005 (character/wolf model). Do not touch any other entry in this
file.

For PAWS-002, append a resolution in whatever format the file already
uses for a resolved item:
RESOLVED 9 SEP 2026 - PAWS is the venture name. Scout is the flagship
product and character name.

For PAWS-005, append a resolution marking it superseded, not answered:
SUPERSEDED 9 SEP 2026 - the character is Scout, an original dog
design built for this venture. Not a reuse of the WWD wolf model.
The original question about the wolf model's rigging status no
longer applies.

Leave PAWS-001, PAWS-003, PAWS-004, and PAWS-006 exactly as they are.

---

### INSTRUCTION: TASKS.md

Open D:\WKP\PAWS\TASKS.md. Match its existing phase structure and
add these items under the appropriate phase - do not restructure the
file, just add rows:
- Character design: DONE. Scout, see SCOUT-CHARACTER-BIBLE.md.
- Fetch v1 (filename/folder/date search, scoped locations): add as a
  build task, not yet started.
- Fetch v2 (content-aware search): add to backlog, explicitly not a
  v1 requirement.
- Android companion app: add as a build phase, sequenced after the
  state machine milestone.
- SD-port data management capability: add to backlog under a Horizon
  or Later section if one exists, or create one. Not yet specced,
  do not schedule it into an active phase.

---

### INSTRUCTION: root CLAUDE.md venture status board

Find the existing PAWS row - it should already be there from the
first PAWS scaffold. Update its status to reflect: character locked
(Scout), hardware direction locked (fused hub-plus-personality device
from day one), still blocked on PAWS-001 and PAWS-004. Do not create
a second PAWS row. If no existing row is found, say so and stop
rather than guessing where to add one.

---

### INSTRUCTION: projects.md, if it exists

Find the existing PAWS section. Update it to reflect the same locked
decisions as the CLAUDE.md update above, matching whatever format the
surrounding entries already use. If projects.md does not exist, skip
this and flag it in your report rather than creating the file.

---

### VERIFICATION CHECKLIST - run after applying everything above

- [ ] `type D:\WKP\PAWS\CLAUDE.md` shows the Scout-and-hub content,
  not the original venture-only version
- [ ] `dir /b D:\WKP\PAWS` includes SCOUT-CHARACTER-BIBLE.md and
  CAPABILITIES.md
- [ ] `findstr /i "wolf" D:\WKP\PAWS\formats\CHARACTER.md` returns
  nothing
- [ ] `findstr /i "PAWS-002" D:\WKP\PAWS\decisions\DECISIONS.md`
  shows a RESOLVED line
- [ ] `findstr /i "PAWS-005" D:\WKP\PAWS\decisions\DECISIONS.md`
  shows a SUPERSEDED line
- [ ] The root CLAUDE.md venture board has exactly one PAWS row, not
  two
