---
name: kp-skills
description: The kp-* skill family for Kingdom Planners and what each one actually covers
metadata:
  type: reference
---

Found at `D:\WKP\.claude\skills\`, not obvious without a directory listing
since they aren't all referenced by name in Kingdom-Planners\CLAUDE.md:

- **kp-prep** — builds the 8-image listing photo set. Cards 1 (title card),
  6 (contents graphic, enumerate every tab, "the one that converts"), 7
  ("works in Excel and Google Sheets," permanent), 8 (veteran credential
  card, permanent) are template/copy-driven. Cards 2-5 must be real
  screenshots of the actual working file, taken by Zac, never staged. Card 6
  needs real tab names from kp-generator's output, never guessed. Has a
  `scripts\watermark.py` for optional preview watermarking, off by default.
- **kp-generator** — builds the spreadsheet itself (tabs, formulas,
  validation). Every planner must work in both Excel and Google Sheets;
  a formula that breaks in one is a broken product, not a minor bug, since
  "works in both" is one of the 8 permanent photo claims (card 7 above).
- **kp-recon** — finds product-gap ideas by reading Etsy review text and
  autocomplete in military/veteran planner categories. Signal has to be a
  real stated need (a review quote or autocomplete pattern), never invented.
- **kp-ledger** — weekly sales/revenue tracking, reporting only, no COGS
  since it's all digital.
- **kp-planner** and **kp-reviews** — not yet read in detail, exist in the
  same skills folder, check before assuming a task needs a new skill built.

**How to apply:** when doing KP photo/listing work, check kp-prep's actual
card-by-card spec before assuming what "the 8 images" means — it's specific
about which cards are template-driven vs. which require real screenshots,
and this distinction is a hard rule (kp-prep's own escalation clause: "the
spreadsheet isn't finished, this skill cannot run yet" / "never guess a tab
name").

Related: [[kp-file-status]]
