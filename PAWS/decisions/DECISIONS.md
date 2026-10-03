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
**Status:** RESOLVED 9 SEP 2026 — PAWS is the venture name. Scout is the
flagship product and character name.
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
**Status:** SUPERSEDED 9 SEP 2026 — the character is Scout, an original
dog design built for this venture. Not a reuse of the WWD wolf model.
The original question about the wolf model's rigging status no longer
applies.
**Question:** Zac has a 3D wolf model "almost" done. Is it rigged? What
format? Does it need a modeling pass before it can drive expressions?

## PAWS-006 — Investor audience
**Status:** PARTIAL — Zac said "investors and or partners"
**Question:** Which specifically? An angel investor, a manufacturing
partner, and a distribution partner want three different decks. Also:
does this feed the existing WKP grants work?

## PAWS-007 — SD card versus I2S audio, GPIO pin conflict on the locked board
**Status:** OPEN — blocks ordering either the SD card breakout or the
audio components
**Question:** Hardware research run 24 SEP 2026 (see
PAWS\PARTS-RESEARCH.md) confirmed the Waveshare ESP32-S3-Touch-LCD-1.69
exposes only four free GPIO pins (GPIO2, GPIO3, GPIO17, GPIO18) on its
header — everything else is already committed to the display, touch
controller, boot pin, battery sense, native USB, power button, or
buzzer. A raw SD card breakout over SPI needs all four remaining pins
by itself. I2S audio (for the ElevenLabs voice lines already planned in
SCOUT-CHARACTER-BIBLE.md) needs three of those same four pins. They do
not fit together on this board as currently understood. Three real
options, not yet chosen between:
1. Ship one, defer the other past this board revision — pick which.
2. Add a small I2C GPIO expander (MCP23017-class, not yet sourced) to
   free up enough I/O to run both, since I2C rides the existing shared
   bus at zero extra native-pin cost.
3. Check Waveshare's schematic PDF for undocumented solder-pad test
   points not on the plastic header — not yet verified this session.
**Why it matters:** Decides whether the SD-card data-sort capability
(just promoted toward a v1 candidate in CAPABILITIES.md) or the voice-
line audio capability (already planned in the character bible) ships
first on the current board, or whether a small added part removes the
tradeoff entirely. Also decides what gets ordered next.
**Note:** Two components researched the same session have no conflict
and no open decision blocking them — the haptic feedback driver and the
I2C rotary encoder both ride the existing I2C bus at zero added pin
cost. Those can be ordered independent of how PAWS-007 resolves.
