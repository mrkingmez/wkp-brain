---
name: ebay-lister
description: Prices approved candidates and builds eBay listings through the eBay Inventory API, or a supervised Chrome draft. Pre-graduation, output goes to the decision queue, not live.
---

## Pricing
Use tools/pricing.py. Never hand-calculate. Formula:
price = ((supplier_cost + supplier_ship) * (1 + supplier_tax_buffer) + per_order_fixed_fee + target_profit) / (1 - fvf_rate - promo_rate)
- supplier_tax_buffer is 0.10 until Zac has a resale certificate, then 0.
- fvf_rate and per_order_fixed_fee come from data/fee-table.md, refreshed monthly from eBay's current fee page for that category. Never hardcode from memory.
- promo_rate is 0 unless Zac approves promoted listings.
- Round to .99 or .97 style endings. Recheck the margin floor after rounding.
- Offer free shipping with cost built into price.

## Listing build
- Title: up to 80 characters, real search terms, no keyword stuffing, no brand names unless authorized.
- Item specifics: fill every required and recommended one.
- Photos: supplier images only where the agreement permits use. Otherwise flag.
- Description: honest, matches the supplier spec exactly. No claims the supplier cannot back.
- Handling time: supplier handling plus 1 day buffer.
- Item location: the supplier's US warehouse state, stated truthfully.
- Business policies: use Zac's eBay payment, return (30-day returns recommended), and shipping policies.
- Quantity: never list more than supplier stock minus 2.

## Path A: API (primary)
tools/ebay_api.py: createOrReplaceInventoryItem, createOffer, then publishOffer only after Zac's approval (or after graduation, inside caps).

## Path B: Claude in Chrome (fallback, supervised)
Zac present. Fill the eBay listing form, stop before "List it," Zac reviews and clicks.

## Output
listings.csv row with status DRAFT, QUEUED, LIVE, PAUSED, ENDED.
