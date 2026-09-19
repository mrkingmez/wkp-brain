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
