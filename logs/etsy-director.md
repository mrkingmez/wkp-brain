# Etsy Director Log

Format: ## YYYY-MM-DD HH:MM | TYPE | subject | elapsed

## 2026-10-03 | WKD | First real wkd-weekly-batch run (Military + Landscape prep) | ~1 session

First real execution of the new `wkd-weekly-batch` skill, after
`etsy-director.md`'s "on hold" language and the two phantom skill
references were fixed earlier today (see DECISIONS.md WKD-2026-09-24-01 /
WKD-2026-10-03-01).

**Confirmed real folder names (LOCAL-PATHS.md was wrong/incomplete).**
`E:\04 Warrior King Desins\Puzzles\Imagines\` only has christian,
Christmas, Fantasy, Military — no Landscapes folder there at all. Found a
second, previously undocumented raw-art tree at
`D:\04 New Warrior King Designs\` with its own Christmas, Fantasy,
**Landscapes**, Military, Sci-FI, Sports, Thanksgiving, and a second
christian folder — Military and christian exist in both trees, with the
D:\ copies running later (through Dec 2025) than the E:\ copies (through
Sep 2025). Landscapes only exists on D:\. Updated LOCAL-PATHS.md with the
full real structure, including each category's \Used\ subfolder
convention (= already listed, skip).

**Prepped 3 Military + 3 Landscape designs to current digital spec**
(8x10/5x7/11x14/16x20/A4/A3, JPG, 300 DPI, zipped), none of which existed
in current spec before today — every Military design on disk only had the
old 4-size-PNG export, and only 3 of 20 available Landscape designs had
any export at all (also old spec). Built a reusable version of the
2026-09-01 Christian-batch script at
`.claude\skills\wkd-weekly-batch\scripts\wkd_resize_zip.py` instead of a
one-off scratch script. Output, zip-integrity verified (6 files each, no
bad entries):
- `_Print Exports\Military\` — Arlington Autumn Salute, Apache Attack in
  Desert, Submarine Night Surfacing
- `_Print Exports\Landscapes\` — Majestic Scottish Highlands, Autumn
  Forest Splendor, Tropical Waterfall Paradise
Same 4.69x max upscale factor on the 16x20/A3 sizes as the Christian
batch (same ~1536x1024 source resolution) — expected, not a new problem.

**Excluded both F-35 raw designs** (F-35 Sunrise Takeoff, F-35 Stealth
Aerial Maneuver) from candidate selection per the standing current-gen-
airframe rule — did not prep or recommend either.

**Cap counter still unconfirmed.** No evidence in TASKS.md, DECISIONS.md,
or this log of any listing actually going live since before 2026-09-01.
Treated as 0 used this week but flagged rather than assumed — queued
WKD-2026-10-03-02. Sized the recommendation to the Mon/Wed 3+3=6 cadence
(within the 8/week combined cap either way) rather than the full 8, to
leave headroom against that uncertainty.

**Traffic data is stale.** `data\etsy-manual-2026-08-20.md` is the newest
file in `data\`, 44 days old — recommendation is subject/gift-appeal
judgment only, not traffic-driven. Flagged per the closed-loop rule.

No listing was posted or published. Prep and report only.


## 2026-09-24 | KP | full free-prep pass, 6 of 7 products, Zac away for the weekend | ~1 session

Ran while Zac is off (back Monday night): the free per-listing prep work
TASKS.md already scoped as doable with no money down. Guardrails held: shop
creation stays Blocked (untouched, $29 fee is Zac's spend call), nothing
listed or published, everything delivered as a draft package for his review.

**Read the real product files first, per the brief.** Found 6 of the 7
finished products at `D:\05 Kingdom Planners\excel\files.zip` (Debt Freedom,
PCS, Deployment, VA Tracker, Terminal Leave, Road Trip) and opened every tab
of every file with openpyxl before writing a word of copy. **Complete Budget
System, the flagship 16-tab product, is not on disk anywhere** — checked
every LOCAL-PATHS.md location plus a full scan of C:, D:, E:, and L:. A
handoff doc in Downloads confirmed why: it was built in a web chat session
and left in that session's `/mnt/user-data/outputs/`, never downloaded, the
exact loss pattern root CLAUDE.md's file retention rule exists to prevent.
Did not invent tab names or features for it. It's flagged as blocked in
CLAUDE.md, TASKS.md, and the batch doc, with a clear next action (Zac
re-pulls the file from the original chat or rebuilds it).

**Also caught while reading the real files:** Kingdom-Planners\CLAUDE.md's
existing product descriptions for Road Trip Planner and Terminal Leave
didn't match what's actually in the shipped files (Road Trip has no
Lodging/Attractions tabs, no pie chart, no built-in mileage deduction;
Terminal Leave's timeline is 12 months, not 6). Corrected CLAUDE.md's
Products table to the verified real tab lists rather than leaving the stale
description standing next to new copy that would have contradicted it.

**Delivered:** full listing packs (title, 13 tags, description with every
tab enumerated) for the 6 confirmed products, plus a drafted-but-blocked
pack for the Military Family bundle; anchor+sale pricing for all 7
products and the bundle (2 already locked by Zac, 5 new, confidence level
noted per number since real Etsy comp data came back thin for 2 of them);
About section and shop-policy draft; the AI-disclosure sentence and
publish-time checklist, written distinct from WKD's since the thing being
disclosed is different (AI-assisted tool build vs. AI-generated art) —
researched against real search results since Etsy's own policy pages
block automated fetch, flagged for a live browser double-check before
launch. Full package: `D:\05 Kingdom Planners\Kingdom-Planners-Listing-Prep-
Batch-2026-09-24.docx` / `.md`. Ran the no-ai-slop pass before calling it
done (found and fixed one stray em dash in a section header).

**Delegated, not guessed:** spawned two general-purpose subagents for real
web research rather than answering from training knowledge — one confirmed
Etsy's current AI-disclosure mechanism and the 140-char/13-tag/20-char
limits, one pulled real Etsy comp pricing for the military-planner niche.
Both came back with sourced, honestly-caveated results (some categories had
thin or currency-inconsistent data, said so rather than papering over it).

**Not done, no image-generation tool available this session:** the 8-card
kp-prep photo set. Cards 1 and 6 have real, ready copy (pulled from the
actual files) but need the image built in Adobe Express or routed to
graphic-design. Cards 2-5 are correctly left for Zac, the skill's own rule
requires real screenshots of the working files, not staged content. Cards 7
and 8 are existing permanent assets, nothing needed.

No DECISIONS.md entries queued this session — pricing was grounded in real
(if uneven-confidence) comp research plus complexity analogy to the two
prices Zac already locked, which is what "pricing recommendation" was
asked for, not a call requiring his judgment beyond reviewing the numbers.

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
(`data\etsy-manual-2026-08-20.md`) is 12 days old, past the 10-day
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
