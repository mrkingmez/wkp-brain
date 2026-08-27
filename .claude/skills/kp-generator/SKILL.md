---
name: kp-generator
description: Builds the spreadsheet itself - tab structure, formula
  blocks, validation rules. This is the Kingdom Planners equivalent
  of image generation, but the product is a spreadsheet, not art.
  Trigger on 'kp generator', 'build the spreadsheet', 'scaffold the
  planner'.
---

# Kingdom Planners Generator

## What this builds
Not an image. A working spreadsheet: tab layout, named ranges,
formula blocks, data validation, conditional formatting.

## Compatibility is not optional
Every planner ships in both Google Sheets and Excel. Before calling
anything done, check XLOOKUP support, dynamic arrays, conditional
formatting, data validation, and protected ranges in both. A formula
that works in Excel and breaks in Sheets is a broken product, not a
minor bug - it's one of the eight permanent photo claims made on
every listing.

## Rules
Base new tab structure on what kp-recon found, not on what's easy
to build.
Reuse patterns from the VA tracker once its structure is confirmed -
don't reinvent validation logic per planner.

## Escalation
Formula behaves differently between Sheets and Excel - flag it and
do not ship until resolved. This is a "works in both" product.