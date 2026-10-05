# PAWS Research — Taskagotchi Engagement + Hardware Parts

**Date:** 2026-09-24
**Why this run happened:** Zac's concern that Taskagotchi's daily loop (check mood in the morning, occasionally say "Fetch") is one touchpoint a day — fun for a week, then furniture. Asked for ideas on what else Scout could do, then asked to dig into more hardware "pieces and parts."

**Bottom line:** Six new engagement features drafted (all proposed, none locked). Real hardware research turned up a genuine conflict — the locked screen module only has 4 free pins, and two planned features (SD-card data-sort and voice-line audio) both want more pins than exist combined. That's queued as decision PAWS-007 and needs Zac's call before either feature can actually ship. Two cheap, conflict-free parts are ready to test-buy any time. Nothing has been ordered.

---

## Part 1 — Six New Engagement Features

All of these are proposed, not yet confirmed. Full detail lives in `PAWS\CAPABILITIES.md`.

### 1. Touch-to-act
The screen is a real touchscreen, but right now nothing reads a tap — mood display is read-only. This turns Scout from a status light into a control surface: tap to mark the current top task done, tap a second zone to snooze a flagged decision, tap a third to cycle to the next calendar item. A hold-to-confirm gesture (not a bare tap) protects anything that actually writes data back out.

Blocked on PAWS-001 (task source not yet picked) — "mark done" has to call whatever API that source has, so this can't build before that decision lands.

### 2. Event reactions
A one-off animated reaction to something that just happened, layered briefly on top of the steady-state mood. Checked against what data actually exists:
- A FrostCast/WWD episode going live — **feasible**, existing log file, no new infrastructure.
- A decision getting marked RESOLVED — **feasible**, same reasoning.
- An Etsy sale happening — **not feasible**. Etsy has no sales/traffic API; root CLAUDE.md already confirms the data is hand-typed weekly. Don't build this trigger until that changes.

Worth noting honestly: Scout only sees an event on its next scheduled check-in, not instantly — "reaction" means "most recent event since last check," not a live push.

### 3. The USB-C hub is the real retention anchor
Stated explicitly rather than left implicit: the actual answer to "why won't this go stale after a week" isn't any of the other five features — it's that Scout is also a working USB-C hub, so it stays physically useful on the desk (charging, peripherals) independent of whether anyone's engaging with the character layer that day. Design implication for later firmware/enclosure work: hub passthrough must keep working even if the personality module crashes, is mid-flash, or loses wifi — the two subsystems share an enclosure, not a dependency.

### 4. SD-card data management — promoted toward a real v1 candidate
This ties to a workflow Zac already does by hand constantly: WWD picture pulls, B-roll imports, Etsy photo batches. That's enough of a real recurring use case to move it off the pure-backlog list. Proposed v1 shape: SD card (not USB-A), read-only scan-and-suggest only, Scout never moves or deletes a file without asking every time. One real architecture note: the microcontroller can identify files on the card, but the actual file move into D:\WKP or L:\ has to happen through the companion app or a PC-side helper — the board itself can't write into those drives directly.

This is also the feature in direct conflict with voice audio — see PAWS-007 in Part 2.

### 5. End-of-day recap
Closes the loop the morning mood-check opens — one real completed thing from the day, not a list, matching the "top three, not everything" discipline wkp-daily-brief already uses. Reuses existing infrastructure (TASKS.md rows that flipped to Done today, today-dated log entries) rather than needing anything new.

### 6. Proactive push notifications — made concrete
The companion app push was already planned; this names which specific nudges are actually worth sending, capped at roughly one or two a day, each tied to something already tracked in the repo (never an invented sense of urgency):
- "Etsy's weekly cap resets today"
- "A decision's been open 5+ days"
- "FrostCast records tonight"
- "[Venture] has been flagged BLOCKED for N days"
- "Etsy's Friday data pull is due"

Explicitly ruled out: per-task reminders, a ping for every decision (aged ones only), or any "you haven't checked me today" message — that's the exact guilt-bait pattern the character bible already bans by name.

**Real engineering gap found along the way:** `D:\WKP\dashboard\data\` — the JSON path Scout's mood engine is supposed to read from — doesn't exist on disk yet. The two skills that are supposed to write it (wkp-daily-brief, wkp-monday-brief) currently render straight to a report, not to that path. This blocks event reactions and the end-of-day recap until that write step gets built — an engineering prerequisite, not a decision for Zac.

---

## Part 2 — Hardware Parts Research

Research only. Nothing ordered. Full pricing/suppliers in `PAWS\hardware\PAWS-BOM.xlsx` (every row marked "RESEARCH - NOT ORDERED").

### The finding that changes the plan
The Waveshare ESP32-S3-Touch-LCD-1.69's expansion header exposes exactly **four free GPIO pins** (GPIO2, GPIO3, GPIO17, GPIO18). Everything else is already spoken for — boot pin, battery sense, the native USB flashing lines, the power button, the onboard buzzer. Checked directly against Waveshare's own wiki/docs, not assumed.

Built the simple way, the components on the original wishlist need 10-11 pins combined against 4 available:

| Component | GPIO cost, raw part |
|---|---|
| I2S audio out (voice lines) | 3 pins |
| SD card over SPI | 4 pins |
| RGB status LED | 1 pin |
| Rotary encoder (raw) | 2-3 pins |

**The fix is a sourcing choice, not a scope cut:** buy I2C breakouts instead of raw parts wherever they exist — I2C rides the same two-pin shared bus the touch controller already uses, at effectively zero added pin cost. That's why the haptic driver and rotary encoder below are both recommended as I2C parts.

**One real conflict survives even after that fix:** SD card access and I2S voice audio cannot both run natively on this board at the same time — SD over SPI eats all four remaining pins by itself, leaving nothing for audio, and SD can't run over I2C (the protocol doesn't support it). **Queued as decision PAWS-007** — three real paths, none free of a real tradeoff:
1. Pick one (audio or SD) as the priority, defer the other past this board revision.
2. Add a small I2C GPIO expander chip (MCP23017-class) — itself an I2C part, zero new native pins, frees enough I/O to run both. Not yet researched to the usual three-supplier standard.
3. Check Waveshare's own schematic PDF for solder-pad test points not exposed on the plastic header — not fully verified this session, worth a look before spending on option 2.

### Part-by-part

**1. Audio (voice lines)** — needs an I2S DAC/amp (MAX98357A family) plus a small 8-ohm speaker. Three supplier options plus a bare-IC distributor in the BOM. The preferred 28mm round speaker was out of stock at check — flagged, fallback listed. Competes directly with SD for the last free pin.

**2. Haptic feedback (confirms a touchscreen tap)** — a DRV2605L-class driver, I2C, rides the existing bus free. Cleanest item on the whole list, no conflicts. Ships without a motor; a specific verified motor listing is a flagged follow-up.

**3. RGB status LED** — a WS2812/NeoPixel part, one GPIO regardless of how many LEDs are chained. Cheapest pin cost of anything researched. Single-LED option was out of stock; a 12-LED ring is a live in-stock alternative (look-and-feel call, not an engineering one).

**4. SD card (physical media / data-sort)** — confirmed the ESP32-S3 silicon does support USB OTG host mode per Espressif's docs, but nothing on Waveshare's pages validates host mode as supported on this specific board, and the USB pins are already committed to the flashing port anyway. SPI SD card remains the real path — straight into the PAWS-007 conflict. Do not order until that resolves.

**5. Rotary encoder / button** — an I2C rotary encoder breakout is the clear pick over a raw mechanical encoder, same zero-pin-cost logic as the haptic driver. A plain tactile button is the cheapest fallback if a full encoder is more than needed.

### What to actually do next
**Two parts are ready to buy today with zero conflict and zero open decision:** the haptic driver and the I2C rotary encoder, both under $8. Good first physical test if Zac wants to feel touch-to-act before the bigger board question gets settled.

**Everything else waits on PAWS-007.** That decision — not any single part purchase — determines whether voice lines or SD data-sort ships first on this board revision, or whether a GPIO expander gets added to run both.

**Out of scope this pass:** the USB-C hub module itself (RayCue family or comparable) — separate sourcing thread, runs in parallel per the venture's build sequence.
