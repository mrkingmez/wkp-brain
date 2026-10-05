---
name: wkd-weekly-batch
description: Weekly automated report for WarriorKingDesigns - what
  should post this week, within the shared cap, based on what's
  actually ready on disk, plus draft listing copy for each pick.
  Replaces the stale skills listing-factory-weekly-batch-skill and
  master-plan-daily-executor (see "Why this exists" below).
  Trigger on "wkd weekly batch", "what should WKD post this week",
  "WKD report", or the standing Monday/Wednesday posting cadence.
---

# WKD Weekly Batch Report

## Why this exists (read once, then ignore)
`etsy-director.md` and `ETSY\CLAUDE.md` both referenced
`listing-factory-weekly-batch-skill` and `master-plan-daily-executor`
as the weekly WKD planning tools. Neither exists in
`D:\WKP\.claude\skills\` - confirmed by directory listing, twice now
(ETSY\CLAUDE.md's own note already records a *first* failed attempt
to fix this, swapping in names that also turned out not to exist).

**Correction, 2026-10-03:** those names aren't generic/unrelated demo
content - the real source turned up sitting in
`D:\04 New Warrior King Designs\Listing Factory Skill - SKILL.md` (plus
a companion `30-Day AI Productivity Plan.md` in the same folder). It's
genuinely Zac's own content, built at an earlier stage of this shop and
never moved into the actual skills folder - same failure mode as
Kingdom Planners' Complete Budget System file getting stranded in a web
chat. It's just stale now: it references the retired `E:\Puzzle Art`
path, a Gelato-for-wall-art/Printify-for-puzzles fulfillment split that
predates the shop's Printify-only switch, and a physical-plus-digital
strategy that predates the digital-only lock (8/31). Its genuinely
reusable parts (the title/tag/description formula, the resolution-ceiling
caveat, the marketing-copy generation) are folded into this skill below,
corrected for current reality. Do not go back to the original file or
re-add either phantom skill name anywhere.

## What "on hold" actually means for WKD
Root CLAUDE.md flags WarriorKingDesigns as on hold. That means:
**don't restructure the venture, resume the physical/puzzle line, or
change pricing without Zac raising it.** It does NOT mean refusing to
generate this report, and it does NOT mean refusing to run the free,
reversible prep work (resize/zip into the digital spec) that
`ETSY\CLAUDE.md`'s own locked Active Plan (7/24, amended 8/31)
already authorizes as standing, ongoing work - prioritize military
puzzle and landscape wall art/canvas designs, digital-only, within
the cap. Same boundary Kingdom Planners already runs under: prep is
free and standing, only the live Etsy listing itself needs Zac's own
hand (or, for WKD specifically, nothing further - no $29 gate here).
Locked 2026-10-03, Zac's direct word, after two sessions got stuck
treating routine weekly prep as if it needed fresh permission every
time. See `logs\DECISIONS.md` entries WKD-2026-09-24-01 and
WKD-2026-10-03-01 for the full history this resolves.

## The cap
3 listings/day, 8/week, BOTH SHOPS COMBINED, locked until 15 NOV 26.
Check `kp-planner`'s own note: there is no confirmed shared counter
yet between KP and WKD tooling. Ask Zac directly how many listings
(either shop) already shipped this week before recommending more -
do not assume zero.

## Step 1 - Check what's actually ready
Compare, per line (Military, Landscape, Christian, Fantasy, Sci-Fi,
Christmas, Sports, Thanksgiving):
- Raw source: `D:\04 New Warrior King Designs\<line>\` - this is the
  ONE real art root as of 2026-10-03 (E:\04 Warrior King Desins\ is
  retired, see LOCAL-PATHS.md's WKD section for the full verification
  history; every file that ever existed only on E:\ has been copied
  over, nothing was lost). Skip anything already in a `\Used\`
  subfolder - that's already listed.
- Current digital spec export: `D:\04 New Warrior King Designs\_Print
  Exports\<line>\<design>\` - needs all 6 sizes (8x10, 5x7, 11x14,
  16x20, A4, A3, 300 DPI JPG) plus the zip. Designs only exported to
  the older 4-size PNG spec (flat at the `_Print Exports` root, no
  line subfolder, no A4/A3) don't count as ready.
- Resolution ceiling: most source files run ~1536x1024 (~1.5-2MP).
  Expect a real upscale (confirmed ~4.69x on 16x20/A3 in the
  2026-09-01 Christian and 2026-10-03 Military/Landscape batches) -
  this is normal, not a defect, but don't recommend print sizes above
  the current 6-size spec without Zac confirming a source image was
  deliberately upscaled higher.

## Step 2 - Prioritize per the locked Active Plan
Military (puzzles) and Landscape (wall art/canvas) lead per
ETSY\CLAUDE.md's "what's actually working" section. Christian and
Fantasy/Sci-Fi are secondary - include only if there's cap room left
after Military/Landscape.

## Step 3 - Prep whatever's recommended but not yet export-ready
If a design worth recommending this week is still on the old 4-size
PNG spec or has no digital export at all, run the same resize/zip
pass as the 2026-09-01 Christian-line batch (see logs\etsy-director.md
that date for the exact spec and script approach) to bring it up to
spec. This is prep, not publication - standing authorized work per
the "on hold" clarification above, do not ask Zac before doing it.

## Step 4 - Draft listing copy per design (folded in from the old Listing
Factory skill, corrected for current reality - digital-only, no Gelato,
no physical wall art/puzzle variants)
For each recommended design:
- **TITLE** - under 140 chars, keyword-front-loaded: [Design Name] +
  "Digital Download" + niche keyword + gift/use keyword.
- **TAGS** - exactly 13, each under 20 chars, broad + long-tail mix,
  no redundant words across tags.
- **DESCRIPTION** - 150-250 words. MUST open with "INSTANT DIGITAL
  DOWNLOAD - no physical item will be shipped," list the included
  sizes (8x10/5x7/11x14/16x20/A4/A3), one line on the artwork's mood,
  who it's for. Do not describe a physical/printed/framed product -
  this shop sells digital files only, per the locked 8/31 Active Plan.
- **ALT-TEXT** - one sentence per photo in the listing's image set.
- **AI-DISCLOSURE** - mandatory sentence in the description plus the
  "How It's Made" checkbox noted in the handoff checklist. Confirm
  current Etsy AI-disclosure wording the same way Kingdom Planners'
  2026-09-24 prep pass did - don't assume old wording still matches
  current policy.
- **PRICE** - hold at current levels per ETSY\CLAUDE.md's locked Active
  Plan. Don't invent a new price point from the old skill's $3-8 figure
  without checking what's actually live on comparable current listings
  first - that number predates this correction and isn't verified.

## Step 5 - Write the report
Plain output: which designs, which line, why they're the pick (ties
to the locked Active Plan's "what's working" data), real remaining
cap room this week, the draft listing copy from Step 4 for each one,
and which ones are paste-and-go ready right now versus which needed a
prep pass first (and whether that pass actually ran clean - flag
anything that didn't, same as the Christian batch's truncated-PNG
catch). This is the "automated report of what should be posted"
Zac asked for - a list of filenames alone isn't the deliverable,
ready-to-paste copy is.

## Do not
- Post or list anything live. That's always Zac's action, cap or no
  cap, ready or not.
- Treat "on hold" as a reason to refuse this report or the prep
  work behind it - that confusion is exactly what this skill exists
  to end. If a NEW decision point comes up that this skill doesn't
  cover (pricing change, physical-line revival, a brand-new content
  line), that's when the real hold still applies - queue it instead
  of guessing.
- Reference `listing-factory-weekly-batch-skill` or
  `master-plan-daily-executor` anywhere. They are not real.

## Escalation
If the combined cap is already met, or a design's readiness is
genuinely ambiguous (can't tell if an export is current spec or old
spec), queue a decision rather than guessing. Routine prep and the
report itself are not decision points anymore - see above.
