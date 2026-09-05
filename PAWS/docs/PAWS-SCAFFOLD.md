# PAWS-SCAFFOLD.md
Machine-readable handoff. Claude Code reads this and builds every file
below at the exact path shown. Do not summarize or paraphrase the
content inside each block - write it verbatim.

---

### FILE: D:\WKP\PAWS\CLAUDE.md
```
# PAWS — Venture Rules

Hardware venture under Warrior King Productions. Desk devices driven by
a task list, built around an original WKP character.

## What PAWS is

A family of small desk devices that show one thing you would otherwise
open an app to check. The pet is one skin over that idea. Everything in
this venture shares one state machine and one character.

**PAWS** is the venture name and the eventual flagship device (voice
assistant with a rendered character face).

## Product line

| Codename | What it is | Status |
|---|---|---|
| TASKAGOTCHI | Flat panel pet fed by a task list | Build 1 |
| MAC | Camera-tracking robot, browser face, two servos | Build 2 |
| PAWS | Voice assistant, rendered character, hologram optics | Destination |
| DESKMATE | Busy light / meeting status variant | Backlog |
| CLASSPAW | Teacher classroom tool | Backlog |
| STUDYPAW | College variant with journal | Backlog |

## Hard rules

- **No microphone on any device intended for a child.** No LLM, no cloud,
  no data collection on any device a person under 18 touches. This is not
  a preference, it is the thing that keeps the venture legal.
- **Never hardcode credentials or API tokens in firmware.** ESP32 NVS
  storage plus a captive-portal setup page. This applies even to the
  prototype on Zac's desk.
- **Nothing from this venture touches the Columbia County network.** Home
  lab only, permanently.
- **Money is written out in full** in every document ("99 dollars", not
  the symbol-plus-M form). Zac uses text to speech.
- **Spell out symbols** that break a screen reader: microfarads, "240 by
  280", degrees. No micro sign, no multiplication sign, no arrows.
- **Every part gets multiple supplier options** with price and lead time.
  Never a single-source recommendation.
- Character is the WKP wolf. Never a generic blob, never a licensed
  character, never Cortana.

## Build discipline

- Test the state machine on a PC before it ever touches hardware.
- One board is a prototype, two boards is a project. Always order a spare.
- Software angle limits on every servo before the first animation loop.
- Capacitors across every servo. Not optional.
- Data-capable USB cables only.

## Printing

- **Elegoo Mars (resin)**: the character figure, decorative bezels, fine
  detail parts. Not enclosures.
- **Enclosures**: PETG on FDM, printed out of house or on a second
  printer. Resin enclosures crack at snap fits and yellow under UV.

## File conventions

- Logs append to `logs/paws-director.md`
- Open questions append to `decisions/DECISIONS.md`
- Bill of materials lives in `hardware/PAWS-BOM.xlsx`, not in prose
- Build guides live in `docs/`

## Open items

- Task source not yet chosen (see DECISIONS.md)
- Character 3D model located but not yet placed in `art/`
- Hours per week not yet set, timeline is provisional
```

---

### FILE: D:\WKP\.claude\agents\paws-director.md
```
---
name: paws-director
description: Runs the PAWS hardware venture end to end - build guides,
  bill of materials, parts sourcing, firmware planning, enclosure and
  print jobs, teacher and education variants, investor materials. Use
  for anything touching Taskagotchi, MAC, PAWS, Deskmate, ClassPaw, or
  StudyPaw. NOT for WWD, FrostCast, Etsy, novels, WKP Channel, RUBY TWO,
  or investing.
tools: Read, Write, Edit, Glob, Grep, Bash, Agent
model: sonnet
memory: project
color: orange
---

You are the PAWS hardware director. You classify, follow the format
spec for that type, log, and report.

This venture has no worker skills yet. You do the work yourself, guided
by the format file. That is deliberate - PAWS is early and does not have
enough repeat volume to justify separate skills. When a type starts
repeating often enough to be worth extracting, say so and queue it.

## Every run

1. Read D:\WKP\PAWS\CLAUDE.md for venture rules and hard limits.
2. Classify into exactly ONE type: BUILD GUIDE, SOURCING, FIRMWARE,
   ENCLOSURE, CHARACTER, EDUCATION, or INVESTOR.
   Cannot tell? Queue a decision. Never guess the type.
3. Read the format file for that type and follow it exactly.
   BUILD GUIDE -> D:\WKP\PAWS\formats\BUILD-GUIDE.md
   SOURCING    -> D:\WKP\PAWS\formats\SOURCING.md
   FIRMWARE    -> D:\WKP\PAWS\formats\FIRMWARE.md
   ENCLOSURE   -> D:\WKP\PAWS\formats\ENCLOSURE.md
   CHARACTER   -> D:\WKP\PAWS\formats\CHARACTER.md
   EDUCATION   -> D:\WKP\PAWS\formats\EDUCATION.md
   INVESTOR    -> D:\WKP\PAWS\formats\INVESTOR.md
   If the file does not exist, queue a decision naming it.
   Do not build the deliverable from memory instead.
4. Run the pipeline. Write EVERY intermediate artifact to a real file.
   Never pass findings as text between steps.
5. Prices and lead times go in hardware\PAWS-BOM.xlsx, never in prose.
   Prose references the BOM, it does not restate it.
6. Append to D:\WKP\PAWS\logs\paws-director.md, including elapsed time.
7. Report BLUF first, then detail.

## Hard rules

- Never recommend a single supplier. Every part gets at least three
  options with price and lead time.
- Never spec a microphone, an LLM, or any data collection into a device
  a person under 18 will touch. Refuse and queue a decision instead.
- Never put a credential in firmware. NVS plus captive portal, always.
- Never spec resin for an enclosure. Resin is character and detail parts
  only.
- Money written out in full. Symbols that break text to speech get
  spelled as words.
- Verify every price and link before writing it. A stale price is worse
  than no price.
- Scope and budget changes are Zac's call. Queue them. Never decide them.

## Escalation

You cannot ask Zac anything. Append to decisions\DECISIONS.md and return
DECISION QUEUED plus the ID.
```

---

### FILE: D:\WKP\PAWS\TASKS.md
```
# PAWS — Task List

Status key: [ ] not started  [~] in progress  [x] done  [!] blocked

---

## Phase 0 — Setup (before any parts arrive)

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

---

## Decisions waiting on Zac

See decisions/DECISIONS.md
```

---

### FILE: D:\WKP\PAWS\decisions\DECISIONS.md
```
# PAWS — Decision Queue

Append only. Zac resolves, marks RESOLVED with the answer and date.

---

## PAWS-001 — Task source
**Status:** OPEN — blocks all firmware work
**Question:** Where do the tasks that drive the pet actually live?
**Options:** Todoist (easiest API, free tier, token auth) / Microsoft To Do
(best fit for the teacher and office variants) / Google Tasks / Notion /
plain local file synced from the PC.
**Why it matters:** This decides the entire integration layer. Every hour
of firmware work after Phase 1 Step 2 depends on it.
**Note:** If any of these are work tasks on county systems, that is a
non-starter. Personal task source only.

## PAWS-002 — Venture vs product naming
**Status:** OPEN
**Question:** Is PAWS the venture name, the flagship product name, or both?
Current scaffold assumes both. Is PAWS a WKP sub-brand or standalone?

## PAWS-003 — Elegoo Mars generation
**Status:** OPEN
**Question:** Which Mars? Build volume differs enough between generations to
change how the wolf figure gets sliced and whether it needs splitting.

## PAWS-004 — Hours per week
**Status:** OPEN
**Question:** Realistic weekly hours. The timeline in the build guide is
provisional until this is set.

## PAWS-005 — Character source
**Status:** OPEN
**Question:** Zac has a 3D wolf model "almost" done. Is it rigged? What
format? Does it need a modeling pass before it can drive expressions?

## PAWS-006 — Investor audience
**Status:** PARTIAL — Zac said "investors and or partners"
**Question:** Which specifically? An angel investor, a manufacturing
partner, and a distribution partner want three different decks. Also:
does this feed the existing WKP grants work?
```

---

### FILE: D:\WKP\PAWS\logs\paws-director.md
```
# PAWS Director Log

Append only. Newest at the bottom.

---

## 2026-08-31 — Venture scaffold created
Type: BUILD GUIDE
Created CLAUDE.md, paws-director.md, TASKS.md, DECISIONS.md, folder
structure. Produced Build Guide v1 (Taskagotchi + MAC) and BOM v1.
Six decisions queued, PAWS-001 blocks firmware work.
Elapsed: single session.
```

---

### FILE: D:\WKP\PAWS\formats\BUILD-GUIDE.md
```
# Format - BUILD GUIDE

## What this produces
A printable, step-by-step guide Zac can work through without asking a
single follow-up question. If he has to ask how to do a step, the guide
failed.

## Structure
1. What you are building, one paragraph, and what it does when finished.
2. Parts required - reference hardware\PAWS-BOM.xlsx by row. Do NOT
   restate prices in prose.
3. Tools required, with a note on which are one-time purchases.
4. Safety and hard limits before any assembly step.
5. Numbered steps. Every step is an action, not a note to self.
6. Verification after each phase - what proves the step worked.
7. Troubleshooting - the three most likely failure points and the fix.

## Rules
Every command copy-pasteable. Every click named.
Software angle limits on servos BEFORE the first animation loop, always.
Capacitors across every servo, stated as a step, not a footnote.
State machine tested on PC before it touches hardware.
Money written out in full. No symbols that break text to speech.
Never a single-source part. Three options minimum, from the BOM.

## Output
docs\PAWS-<device>-Build-Guide-v<N>.md
```

---

### FILE: D:\WKP\PAWS\formats\SOURCING.md
```
# Format - SOURCING

## What this produces
Parts research that ends in BOM rows, not prose.

## Rules
EVERY part gets at least three supplier options with price and lead time.
Never a single-source recommendation. This is a hard venture rule.
Verify every price and every link before writing it. A stale price is
worse than no price - flag anything you could not confirm.
Note the date the price was checked, in the BOM row.
Money written out in full.

## Per part, capture
Part name and spec. Why this spec and not a cheaper one.
Three suppliers: name, price, lead time, link, date checked.
Known substitutes if it goes out of stock.
Whether it is a consumable, a one-time tool, or per-unit.

## Output
Rows appended to hardware\PAWS-BOM.xlsx.
Prose report references the BOM. It does not restate it.
```

---

### FILE: D:\WKP\PAWS\formats\FIRMWARE.md
```
# Format - FIRMWARE

## What this produces
Firmware plans and code for ESP32 and XIAO class boards.

## HARD BLOCKERS - refuse and queue a decision
Never spec a microphone into a device a person under 18 will touch.
Never spec an LLM, cloud call, or any data collection into a device a
person under 18 will touch.
Never put a credential or API token in firmware. NVS storage plus a
captive-portal setup page, always, including on Zac's own prototype.

## Sequence, in order
1. State machine written and tested on a PC. No hardware.
2. Board boots, wifi connects, static output.
3. API call, parse, map to state.
4. Port the tested state machine.
5. Animation and hardware output.
6. Persistence, sleep, power management.

Do not reorder this. Debugging a state machine over a serial cable is
misery, and skipping step 1 is how it happens.

## Rules
Task source is blocked by PAWS-001 until Zac resolves it. Do not assume
a provider and do not build the integration layer against a guess.
Data-capable USB cables only - state this wherever flashing is involved.
Note flash and RAM headroom against the target board.

## Output
firmware\ for code. docs\ for the plan.
```

---

### FILE: D:\WKP\PAWS\formats\ENCLOSURE.md
```
# Format - ENCLOSURE

## What this produces
Enclosure design specs and print jobs.

## HARD RULE
Never spec resin for an enclosure. Resin cracks at snap fits and yellows
under UV. Elegoo Mars is for the character figure, decorative bezels,
and fine detail parts only.
Enclosures are PETG on FDM, printed out of house or on a second printer.

## Per enclosure, capture
Internal dimensions with clearance for every component, stated.
Screen cutout dimensions - spell out as "240 by 280", no symbols.
Port access - USB, power, reset.
Ventilation if anything runs warm.
Assembly method - screws, snap fit, or friction.
Wall thickness and why.
Print orientation and whether supports are needed.
Estimated print time and material.

## Rules
Elegoo Mars generation is unresolved - PAWS-003. Do not assume a build
volume. If a part might need splitting, say so and queue it.
Spell out symbols that break text to speech. Millimeters, degrees,
microfarads written as words.

## Output
docs\ for the spec. Model files referenced by path, not embedded.
```

---

### FILE: D:\WKP\PAWS\formats\CHARACTER.md
```
# Format - CHARACTER

## What this produces
Character art, states, animation frames, and expression work for the
WKP wolf.

## HARD RULE
The character is the WKP wolf. Never a generic blob, never a licensed
character, never Cortana, never a mascot borrowed from anywhere.

## Per character task, capture
Which states are covered and how many frames each.
Resolution and color depth against the target screen.
File format and where it lands in art\.
How the state maps to the state machine's outputs.

## Open blockers
PAWS-005 - the wolf model is located but rigging status, format, and
whether it needs a modeling pass are unknown. Do not plan expression
work in detail until that resolves.

## Rules
Eight states, three frames each is the Taskagotchi baseline.
Keep the character readable at the actual pixel size. Detail that
disappears on a 240 by 280 panel is wasted work.

## Output
art\ for assets. docs\ for the state and frame spec.
```

---

### FILE: D:\WKP\PAWS\formats\EDUCATION.md
```
# Format - EDUCATION

## What this produces
ClassPaw and StudyPaw variant specs for classroom and student use.

## HARD BLOCKERS - these are what keep the venture legal
No microphone on any device a person under 18 touches.
No LLM, no cloud call, no data collection on any device a person under
18 touches.
Zero student-facing data path. If a design creates one, refuse and queue
a decision. Do not design around it and do not ask forgiveness later.

## Per variant, capture
Who operates it - teacher only, or student facing.
What data it touches and where that data goes. If the answer is anywhere
off the device, stop.
The workflow it actually replaces. If it does not replace something a
teacher does today, it is a toy.
COPPA and FERPA exposure, named plainly.

## Rules
Teacher interviews before spec, not after. PAWS TASKS Phase 4 has this
in the right order - keep it there.
Nothing in this variant touches the Columbia County network. Home lab
only, permanently.

## Output
docs\PAWS-<variant>-Spec-v<N>.md
```

---

### FILE: D:\WKP\PAWS\formats\INVESTOR.md
```
# Format - INVESTOR

## What this produces
Proposal letters, pitch decks, and partner materials.

## Blocked until PAWS-006 resolves
An angel investor, a manufacturing partner, and a distribution partner
want three different documents. Do not write a generic deck that serves
none of them. If the audience is not named, queue the decision.

## Per document, capture
The audience, named specifically.
The ask, stated as a number and a use of funds.
Traction - real photographs of real prototypes, never renders, once
prototypes exist.
The wedge, stated plainly: every existing desk device is a timer. PAWS
is fed by a real synced task list. That is software and it ports across
all three hardware paths unchanged.
Market comparables with sources and dates.

## Rules
Money written out in full. "Ninety nine dollars", never the symbol form.
Never overstate build status. A device that boots is not a device that
ships.
No projections presented as facts. Label estimates as estimates.
Positioning note: lead with the product, not the AI pipeline behind it.

## Output
docs\ for text. Image prompts go to Zac, images come back from him.
```

---

### EMPTY FOLDERS - create with a .gitkeep placeholder

- D:\WKP\PAWS\art\.gitkeep (empty file)
- D:\WKP\PAWS\docs\.gitkeep (empty file)
- D:\WKP\PAWS\firmware\.gitkeep (empty file)
- D:\WKP\PAWS\hardware\.gitkeep (empty file)

---

### VERIFICATION CHECKLIST - run after creating everything

- [ ] `dir /b D:\WKP\PAWS\formats` shows exactly 7 files
- [ ] `dir /b D:\WKP\.claude\agents` includes paws-director.md
- [ ] paws-director.md is NOT present anywhere under D:\WKP\PAWS\
- [ ] `findstr /s /i "watershed" D:\WKP\PAWS\*.md` returns nothing
- [ ] Every empty folder (art, docs, firmware, hardware) has a .gitkeep
