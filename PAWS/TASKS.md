# PAWS — Task List

Status key: [ ] not started  [~] in progress  [x] done  [!] blocked

---

## Phase 0 — Setup (before any parts arrive)

- [x] Character design: DONE. Scout, see SCOUT-CHARACTER-BIBLE.md.
- [ ] Decide task source (Todoist / Microsoft To Do / Google Tasks / Notion / local file) — BLOCKS all firmware work
- [ ] Locate the WKP wolf 3D model, drop into art/
- [ ] Confirm Elegoo Mars generation and build volume
- [ ] Set realistic hours per week so the timeline means something
- [ ] Create GitHub repo, push scaffold
- [ ] Order tools (see docs build guide, Tools section)
- [ ] Order Build 1 parts — TWO boards, not one

## Phase 1 — Taskagotchi (Covacut style)

- [ ] Board boots, wifi connects, static sprite on screen
- [ ] State machine written and tested on PC, no hardware
- [ ] Task API call, parse JSON, map completions to stat changes
- [ ] Port state machine to firmware, swap animations by state
- [ ] Flash persistence, sleep and power management
- [ ] Character art: 8 states, 3 frames each
- [ ] Enclosure designed and printed
- [ ] Photograph finished unit for the pitch deck

## Phase 1B — Companion app (Android)

Sequenced after the state machine milestone in Phase 1.

- [ ] Companion app build (Android first, not iOS)
- [ ] Fetch v1 — filename/folder/date search across scoped locations, surfaced in the companion app or opened on the PC

## Phase 2 — MAC (tracking robot)

- [ ] XIAO board boots, serves hardcoded JSON state
- [ ] Web page polls endpoint, draws a face from the JSON
- [ ] Servos: mood to pose mapping, easing, home on boot
- [ ] Capacitors installed, brownout tested under full servo load
- [ ] Software angle limits set BEFORE first animation loop
- [ ] Camera face tracking
- [ ] Pan and tilt bracket mounted, cable management
- [ ] Photograph and film for content

## Phase 3 — Investor materials

- [ ] Proposal letter
- [ ] Pitch deck
- [ ] Image prompts sent to Zac, images returned
- [ ] Real prototype photos swapped in for renders

## Phase 4 — Education variant (ClassPaw)

- [ ] Teacher workflow defined
- [ ] Confirm zero student-facing data path
- [ ] Teacher interviews for real needs
- [ ] Variant spec written

## Backlog

- [ ] Deskmate (busy light / meeting status)
- [ ] StudyPaw (college, journal feature)
- [ ] Etsy sale notifier
- [ ] Countdown device
- [ ] PAWS voice layer
- [ ] PAWS hologram optics
- [ ] Fetch v2 — content-aware search (photo metadata, then visual content matching). Not a v1 requirement.

## Horizon — Not Yet Specced

- [ ] SD-port data management — Scout scans inserted physical media (SD card, possibly USB-A) and sorts files to where they belong, asking rather than guessing when unsure. Open before building: which port(s), read-only scan-and-suggest vs. read-write move-and-file, and the confirmation rule (never moves or deletes without asking, every time). Do not schedule into an active phase until specced.

---

## Decisions waiting on Zac

See decisions/DECISIONS.md
