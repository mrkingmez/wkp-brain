---
name: ebay-fulfillment
description: Handles eBay orders for the dropship venture: supplier purchase prep, tracking upload, stock and price sync, buyer messages, returns. Runs first in every director loop.
---

## Orders
1. Pull new paid orders via eBay Fulfillment API.
2. For each: verify supplier stock and current cost. If cost rose and margin breaks floor, flag to Zac (do not auto-cancel; seller-initiated cancels for out of stock create defects).
3. Pre-graduation: write a BUY item to decisions-queue.md with order ID, supplier, SKU, item, cost. No buyer data of any kind in the queue. Zac opens the order in eBay Seller Hub, takes the ship-to from there, and places or approves the supplier order himself.
4. Upload tracking to eBay the moment the supplier provides it, inside handling time.

## Sync (every run)
For every LIVE listing: supplier stock and cost. If stock under 3, set eBay quantity to 0 (keeps listing history). If cost moves and margin breaks floor, queue a PRICE item.

## Buyer messages
Draft replies only. Zac sends until graduation. Never disclose the supplier relationship in a misleading way, never promise what the supplier cannot do.

## Returns
Follow Zac's return policy. Route to supplier's US return address per agreement. Log every return reason.

## Privacy
No buyer data of any kind goes into the repo: no name, address, city, state, ZIP, email, phone, or username, in any file, log, queue item, report, or memory. orders.csv stores order ID, item, and money fields only. Buyer ship-to lives only in eBay Seller Hub.
