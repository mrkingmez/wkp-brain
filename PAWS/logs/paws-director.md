# PAWS Director Log

Append only. Newest at the bottom.

---

## 2026-08-31 — Venture scaffold created
Type: BUILD GUIDE
Created CLAUDE.md, paws-director.md, TASKS.md, DECISIONS.md, folder
structure. Produced Build Guide v1 (Taskagotchi + MAC) and BOM v1.
Six decisions queued, PAWS-001 blocks firmware work.
Elapsed: single session.

## 2026-09-24 — Taskagotchi engagement spec + additive hardware research
Type: mixed — CAPABILITIES addition (closest to CHARACTER/BUILD-GUIDE
scope) plus SOURCING for hardware research. Run solo while Zac is off
for the weekend, reporting back per his ask.

Trigger: Zac's concern that the Taskagotchi loop (morning mood check,
occasional "Fetch") is one touchpoint a day and goes stale after a
week. Asked for engagement ideas built out, plus hardware "pieces and
parts" research.

Part 1 — six engagement ideas from this session's brainstorm written
into CAPABILITIES.md as proposed/NOT YET CONFIRMED additions: touch-to-
act, event reactions, the USB-C hub named explicitly as the retention
anchor, SD-port data management promoted from Horizon toward a v1
candidate (tied to Zac's real WWD/Etsy file-sort workflow), end-of-day
recap, and concrete proactive push-notification triggers. Flagged a
real gap along the way: D:\WKP\dashboard\data\ (the JSON pipe the
character bible assumes Scout reads) does not exist on disk yet —
wkp-daily-brief and wkp-monday-brief render to dashboard/report output
today, not to that JSON path. Blocks event reactions and the recap
until that write step is built. TASKS.md updated to match — new Phase
1B/2 candidates section, SD-port task flagged blocked.

Part 2 — hardware research delegated to a general-purpose subagent
(no WebSearch access from this director's own toolset). Covered audio
(I2S DAC/amp + speaker), haptic feedback (DRV2605L), RGB status LED
(WS2812 class), SD card breakout, and rotary encoder/button, each with
three-plus verified suppliers. Real finding: pulled the actual
Waveshare ESP32-S3-Touch-LCD-1.69 pinout and found only four free GPIO
pins (GPIO2/3/17/18) — a raw SD card breakout needs all four, I2S audio
needs three of the same four, they do not fit together on this board.
Haptic driver and rotary encoder both solved as I2C parts at zero added
pin cost — genuine low-risk wins regardless of the SD/audio conflict.
Queued PAWS-007 (SD vs audio GPIO conflict, three resolution paths) in
decisions\DECISIONS.md rather than guessing which capability ships
first. Built hardware\PAWS-BOM.xlsx (new file, 30 rows, all status
"RESEARCH - NOT ORDERED") and PAWS\PARTS-RESEARCH.md (prose, references
BOM by row/category, restates no prices per the SOURCING rule). Nothing
ordered, no money spent, per the explicit research-only instruction.

Files touched: CAPABILITIES.md, TASKS.md, decisions\DECISIONS.md,
hardware\PAWS-BOM.xlsx (new), PARTS-RESEARCH.md (new), this log.
Elapsed: single session, one delegated subagent call (~211 seconds,
144k tokens) for the hardware research pass.
