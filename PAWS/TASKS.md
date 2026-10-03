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

## Phase 1B / Phase 2 candidates — added 24 SEP 2026, engagement brainstorm

Four of the six ideas from this session's engagement brainstorm land
here (the other two are the USB-C-hub-as-retention-anchor framing
note, which isn't a build task, and SD-port data management, tracked
in its own section below). All four depend on PAWS-001 (task source)
and/or the D:\WKP\dashboard\data\ JSON write path, which does not
exist on disk yet (flagged in CAPABILITIES.md Connectivity section) —
do not start firmware work on any of these before those are resolved.
See CAPABILITIES.md for full specs.

- [ ] Touch-to-act — mark task done / snooze decision / cycle calendar
  by tapping the screen, with hold-to-confirm on anything that writes
  data back out. Blocked on PAWS-001 (needs a write-back API).
- [ ] Event reactions — one-off animation for a FrostCast episode going
  live or a decision closing (both feasible off existing logs). Etsy
  sale reaction explicitly NOT feasible — no Etsy API/export exists.
- [ ] End-of-day recap — one real completed thing, pulled from TASKS.md
  and today's log entries, delivered in the evening. No new data
  pipeline required beyond what wkp-daily-brief already reads.
- [ ] Proactive push notifications (companion app) — concrete nudge
  list specced in CAPABILITIES.md: Etsy cap reset, aged decision,
  FrostCast recording night, BLOCKED-venture flag, Etsy Friday data
  pull. Capped at one to two pushes a day, each tied to a real tracked
  constraint.

## SD-port data management — promoted toward v1 candidate, still has open items

- [ ] SD-port data management — Scout scans an inserted SD card,
  reads file type/date metadata, and suggests a destination against
  known folder conventions (WWD Raw Footage, WKD exports) — read-only
  scan-and-suggest for v1, never read-write. Confirmation rule locked:
  Scout never moves or deletes a file without asking first, every
  time. Architecture note: the actual file move has to route through
  the companion app or a PC-side helper — the ESP32-S3 is not
  positioned to write into D:\WKP or L:\ directly. Still open: which
  folder-convention rules to encode first (start with WWD and WKD),
  and exact phase placement (after companion app + Fetch v1, since it
  needs the same PC-write path). Full spec in CAPABILITIES.md.
  BLOCKED on PAWS-007 as of 24 SEP 2026 — SD card over SPI and the
  planned I2S voice-line audio both need pins the Waveshare
  ESP32-S3-Touch-LCD-1.69 doesn't have enough of to run both natively.
  See PARTS-RESEARCH.md and decisions\DECISIONS.md.

## Additive hardware research — added 24 SEP 2026

- [ ] Resolve PAWS-007 (SD card vs I2S audio GPIO conflict) before
  ordering the SD breakout or the audio amp/speaker — see
  decisions\DECISIONS.md and PARTS-RESEARCH.md.
- [ ] Haptic feedback driver (DRV2605L, I2C, zero added GPIO cost) —
  no blocker, candidate for an early low-risk purchase. See
  PARTS-RESEARCH.md and hardware\PAWS-BOM.xlsx.
- [ ] I2C rotary encoder (STEMMA QT class, zero added GPIO cost) — no
  blocker, candidate for an early low-risk purchase alongside the
  haptic driver. See PARTS-RESEARCH.md and hardware\PAWS-BOM.xlsx.
- [ ] RGB status LED (WS2812 class, one GPIO) — no blocker, fits the
  pin budget on its own. See PARTS-RESEARCH.md and hardware\PAWS-BOM.xlsx.

---

## Decisions waiting on Zac

See decisions/DECISIONS.md
