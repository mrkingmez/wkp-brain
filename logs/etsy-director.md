# Etsy Director Log

Format: ## YYYY-MM-DD HH:MM | TYPE | subject | elapsed

## 2026-09-01 | WKD | Christian line digital resize/zip + week's product recommendation | elapsed not precisely tracked at session start

First active WKD work since the "triage complete, hold" status (root
CLAUDE.md venture board, 8/31 Monday Brief) — Zac raised it directly, which
per the venture-status rule takes precedence over the hold for this
specific ask.

**Task 2 — resize/zip (done):** 22 raw Christian-line PNGs at
`E:\04 Warrior King Desins\Puzzles\Imagines\christian\` resized into the
confirmed spec (8x10, 5x7, 11x14, 16x20, A4, A3, all 300 DPI, JPG) and
packaged one zip per design. Discovered the delivery/export convention
already existed on disk (undocumented in LOCAL-PATHS.md, which had a FILL
placeholder) at `D:\04 New Warrior King Designs\_Print Exports\` — one
subfolder per design + a same-named zip at the root, already in live use
for Military and 3 Christian/Landscape designs, but in an OLDER spec (PNG,
4 sizes, no A4/A3). Wrote this batch to a new `\christian\` subfolder
under that root to avoid overwriting the 2 overlapping older exports
(Golden City Revelation, Gothic Cathedral Radiance). LOCAL-PATHS.md
updated with the real path and the spec-version note.

Source is landscape (1536x1024, 3:2 ratio); all 6 target paper sizes are
narrower than that, so every export was rendered in landscape orientation
(matching source composition) with a center-crop on width only — 5.7%
(A4/A3) to 16.7% (8x10/16x20) of width trimmed evenly off both sides.
Never stretched, never letterboxed. Flag for Zac: the source renders are
only ~1.57MP; the 16x20/A3 targets require up to a 4.69x pixel-dimension
upscale to hit 300 DPI at that size, so those two sizes in particular will
be visibly softer than the 8x10/5x7 than the DPI tag implies. This matches
the shop's existing prior-export precedent (same upscale factor applied
to the old Golden City Revelation set) — not a new problem introduced
today, but worth knowing before printing large.

One source file, "Genesis Cosmic Light," was truncated on disk (PNG
missing its final scanline — confirmed via pixel inspection: last row is
a flat [0,0,0] with zero variance vs. real per-pixel noise in the rows
above it). Recovered with PIL's truncated-image tolerance; the defect is
a single 1-pixel-tall row at the very bottom edge in an already near-black
part of the composition, so it should be visually invisible, but the
source file itself is still damaged and worth re-exporting clean from the
original generator if a pristine master matters later.

Result: 22/22 zips built, 6 files each, zip integrity verified (no bad
entries). Source PNGs untouched.

**Task 1 — this week's recommendation (delivered to Zac, not yet acted
on):** Recommended posting from the newly-packaged Christian batch this
week, since it's the only line with digital-ready assets today. Flagged
explicitly as UNGUIDED — the last real WKD traffic pull
(`data\esty-manual-2026-08-20.md`) is 12 days old, past the 10-day
freshness rule, so nothing in the pick is traffic-driven, it's subject/
gift-appeal judgment only. Checked the shared listing cap against Kingdom
Planners: KP has zero listings and the shop itself isn't created yet
(`Kingdom-Planners\CLAUDE.md`), so the full 8/week is available to WKD
this week without contention.

**Found in passing, escalated:** 3 things already live in
`data\etsy-listings-2026-08-20.csv` use "F-35" naming (digital download +
canvas + one more instance), which reads as a direct hit on the root
CLAUDE.md hard rule against current-generation airframe designations. Not
mine to retroactively deindex a live listing — queued as
[WKD-2026-09-01-01] in DECISIONS.md, recommendation is to leave the 2 live
listings grandfathered (near-zero traffic exposure either way) and just
keep F-35/current-gen-airframe designs out of anything new going forward.

Also noted for the record, not blocking: the harness's standing "every
listing ships with an 8-image set, cards 1/6/7/8 generated, 2-5 flagged
for Zac" spec and the "contents enumerated tab by tab" rule both read as
written for Kingdom Planners specifically (tabs = Excel tabs; the 8-card
system isn't documented anywhere in ETSY/CLAUDE.md). Did not force-apply
either literally to WKD without a real WKD photo-spec doc to check against
— flagged as an open question rather than guessed.
