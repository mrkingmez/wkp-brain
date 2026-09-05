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
