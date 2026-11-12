---
name: ebay-supplier-vet
description: Verifies a dropship supplier meets the venture's locked rules before any product from it can be listed. Writes to ebay-dropship/data/suppliers.csv.
---

## Pass criteria (all required)
- Is a wholesaler, distributor, or manufacturer with a published reseller or dropship program. Not a retail storefront.
- Will sign or provide a dropship agreement (eBay can ask sellers for one).
- Ships from US warehouses only, with tracking, via US carriers.
- Blind shipping available.
- Inventory feed or API, or at minimum a daily-updated stock page, so fulfillment can sync stock.
- Stated handling time 2 business days or less.
- Clear return process to a US address.
- Accepts reseller registration (may require resale certificate and business info: flag to Zac).

## Fail on sight
Ships from overseas or "global warehouses" with no US guarantee, no agreement, retail-only checkout, no tracking, prices identical to its own retail site with no reseller tier.

## Output
suppliers.csv: supplier, url, type, us_warehouse(Y/N), blind_ship(Y/N), agreement(Y/N/PENDING), feed_type, handling_days, fees, notes, status(APPROVED/REJECTED/PENDING_ZAC).
Any subscription fee goes to decisions-queue.md as a SPEND item. Monthly WKP tool ceiling is 50 to 100 dollars total, across all ventures.
