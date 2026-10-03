# PAWS — Additive Hardware Parts Research

Research only. Nothing here has been ordered. All pricing and supplier
detail lives in `hardware\PAWS-BOM.xlsx`, status column "RESEARCH - NOT
ORDERED" on every row from this pass. This file is the narrative and the
engineering reasoning — it does not restate a single price, per the
venture's standing SOURCING rule.

Research pass run 24 SEP 2026, in response to Zac's ask for "more pieces
and parts" beyond the software engagement ideas (see CAPABILITIES.md for
those). Scope: additive components for the locked Waveshare
ESP32-S3-Touch-LCD-1.69 screen/personality module, inside the fused
screen-plus-hub enclosure. The USB-C hub module itself was out of scope
here — that's a separate sourcing thread.

---

## The finding that changes the plan: this board has almost no free pins

Before any of the individual components below, the actual pinout of the
Waveshare ESP32-S3-Touch-LCD-1.69 needed checking, because every idea
in this document depends on it.

Confirmed from Waveshare's own wiki and docs pages, checked 24 SEP 2026:
the board's expansion header exposes power (5V, 3V3, GND), a shared I2C
bus already carrying the touch controller, the onboard IMU, and the
onboard RTC, a UART pair, and exactly **four free GPIO pins** — GPIO2,
GPIO3, GPIO17, and GPIO18. Everything else on the chip is already spoken
for: GPIO0 is the boot pin, GPIO1 reads battery voltage, GPIO19 and
GPIO20 are the native USB lines wired to the Type-C port used for
flashing, GPIO40/41 run the power button, and GPIO33 or GPIO42 (varies
by board revision) drives the onboard buzzer. The display's own SPI
lines are internal to the module and aren't on the header at all, so
there's no way to piggyback on them.

That four-pin budget does not cover what this brainstorm asked for, if
built the simple way:

| Component | GPIO cost if built with the simplest raw part |
|---|---|
| I2S audio out (voice lines) | 3 pins (BCLK, LRC, DIN) |
| SD card over SPI | 4 pins (CS, SCK, MOSI, MISO) |
| RGB status LED (WS2812) | 1 pin |
| Rotary encoder (raw EC11) | 2 to 3 pins |

That's 10 to 11 pins needed against 4 available. It does not fit, full
stop, if every component is bought as a raw GPIO-hungry part.

**The fix is a sourcing choice, not a scope cut**: buy I2C breakouts
wherever they exist instead of raw parts, because I2C rides the same
two-pin shared bus the touch controller already uses, at effectively
zero additional pin cost. That single substitution is why the haptic
driver and the rotary encoder below are both recommended as I2C parts
rather than the raw components originally on the brainstorm list.

Even after that substitution, one real conflict remains: **SD card
access and I2S audio cannot both run natively at the same time on this
board as currently understood.** SD over SPI needs all four remaining
free pins by itself, which leaves nothing for audio's three pins. There
is no way to run SD over I2C — the protocol doesn't support it. Three
real paths out of this, none of them free of a decision:

1. Don't run both at once. Pick audio (voice lines, already planned per
   the character bible) or SD (data-sort capability, just promoted
   toward a v1 candidate in CAPABILITIES.md) as the priority, and defer
   the other past this board revision.
2. Add a small I2C GPIO expander chip (MCP23017-class) to the board.
   This is itself an I2C part, so it costs zero new native pins, and it
   would free up enough expanded I/O to run SD over the expander while
   keeping I2S native. Not yet researched to the three-supplier
   standard — flagged as a placeholder row in the BOM, only worth
   chasing further once Zac picks this path.
3. Check Waveshare's schematic PDF for the board for any solder-pad
   test points not exposed on the plastic header itself. This was not
   fully verified this session — the schematic file exists at
   files.waveshare.com but its contents weren't confirmed line by line.
   Worth a follow-up look before spending money on option 2.

This is queued as decision PAWS-007 in `decisions\DECISIONS.md` — which
of the three paths, since it changes which parts get ordered next and
whether audio or SD ships first. Not something to guess at.

---

## 1. Audio output — voice lines through a speaker

The character bible already plans short ElevenLabs-rendered voice lines
for personality moments. Getting sound out of the board at all requires
an I2S DAC/amplifier stage plus a small speaker — the ESP32-S3 has no
built-in audio output. I2S itself is simple to add in principle, since
firmware can route I2S to any free GPIO through the chip's pin matrix —
the real constraint is the pin budget above, not I2S complexity.

Candidate part: an I2S Class-D amplifier breakout in the MAX98357A
family, paired with a small 8-ohm speaker in the 20 to 28 millimeter
range common in hobbyist smart-speaker builds. Three supplier options
plus a bare-IC distributor option are in the BOM under "Audio - I2S
DAC/Amp Breakout." The preferred 28 millimeter round speaker was out of
stock at its primary source at the time of check — flagged in the BOM,
recheck before ordering, with a same-spec fallback also listed.

Status: competes directly with SD card access for the last of the four
free pins. See PAWS-007 above before ordering either.

## 2. Haptic feedback — confirming a touch

For confirming a touchscreen tap (for example, the touch-to-act "mark
task done" idea in CAPABILITIES.md), without relying purely on a visual
change the owner might not be looking at. Candidate part: a DRV2605L-
class haptic driver, which is an I2C part and can ride the board's
existing shared I2C bus at zero additional pin cost — its default
address doesn't collide with the touch controller, the IMU, or the
real-time clock already on that bus. This is the cleanest addition in
the whole list from a pin-budget standpoint. Options are in the BOM
under "Haptic - Driver + Motor." The driver ships without a vibration
motor — a small coin-type ERM motor pairs with it, but a specific
verified motor listing wasn't pulled this session, flagged as a
follow-up in the BOM notes.

Status: no conflict with anything else. Reasonable first purchase if
Zac wants to test touch-to-act confirmation feel before committing to
the rest of the board.

## 3. RGB LED / status indicator

An ambient mood signal that doesn't require reading the screen —
relevant specifically because no PAWS device will ever have a
microphone or voice trigger, so there's no other passive "glance and
know" channel besides the screen itself. Candidate part: a WS2812 or
NeoPixel-class addressable RGB LED, which needs only a single GPIO data
line regardless of how many LEDs are chained — the cheapest pin cost of
anything researched this session. Options are in the BOM under "RGB LED
/ Status Indicator," including a single-LED option (out of stock at
check) and a 12-LED ring as a live alternative that gives a fuller halo
effect instead of a single dot.

Status: fits the pin budget easily on its own. The only real question
is single LED versus a ring, which is a look-and-feel call, not an
engineering one.

## 4. Physical media — SD card for the data-sort capability

Ties directly to the SD-port data management capability, just promoted
toward a v1 candidate in CAPABILITIES.md on the strength of Zac's actual
recurring WWD and Etsy file-sorting workflow. Confirmed this session:
the ESP32-S3 silicon itself does support USB OTG host mode in hardware,
per Espressif's own documentation, but nothing on Waveshare's pages for
this specific board validates or documents host mode as a supported,
tested configuration, and the board's USB pins are already committed to
the Type-C flashing port. SD card over SPI remains the realistic near-
term path, as originally assumed in CAPABILITIES.md — but see PAWS-007
above: a raw SPI SD breakout consumes all four free pins by itself, in
direct conflict with I2S audio. Options are in the BOM under "Physical
Media - MicroSD Breakout (SPI)," including a note that this board's
native 3.3-volt logic makes the cheaper 3-volt-only breakout the better
match, rather than paying for level-shifting circuitry this board
doesn't need.

Status: do not order until PAWS-007 resolves. Ordering this component
before that decision risks buying a part that can't coexist with audio
on the current board revision.

## 5. Rotary encoder or button — physical input

For quick actions without needing touchscreen precision. Given the pin
famine, the clear recommendation is an I2C rotary encoder breakout
rather than a raw mechanical encoder — the I2C version rides the
existing shared bus at zero additional pin cost, versus two to three
pins for a raw encoder, which the board can't currently spare without
the GPIO expander from PAWS-007. Both the I2C option and a raw fallback
(only relevant if an expander gets added) are in the BOM under "Input -
Rotary Encoder," along with a plain tactile button as the simplest,
cheapest fallback if a full encoder turns out to be more than this
needs.

Status: no conflict with anything else at the I2C option. Same category
of easy win as the haptic driver.

---

## Overall read — what to actually do next

Two components have zero pin-budget conflict and no open decision
blocking them: the haptic driver and the I2C rotary encoder, both under
eight dollars each per the BOM. Those are the lowest-risk next purchase
if Zac wants to physically test anything before the bigger board
question resolves.

Everything else — audio, SD card, and by extension the RGB LED only in
the sense that it's fine on its own but the overall board layout still
needs settling — is downstream of PAWS-007. That decision is the actual
highest-leverage next step to close, not a specific part purchase: it
determines whether voice lines or the SD data-sort capability ships
first on this board revision, or whether a small GPIO expander gets
added to run both.

## What this does not cover

The USB-C hub module itself (RayCue family or comparable) was out of
scope for this research pass and still needs its own three-supplier
sourcing thread when that work starts, per CLAUDE.md's build-sequence
note that hub sourcing runs in parallel with screen and firmware work.
