# eBay Dropship (working name WKP Commerce)

Status: Phase 0, scaffold built, nothing live. Nothing goes live without Zac.
Source spec: `D:\WKP\EBAY-DROPSHIP-BUILD.md`. Director: `ebay-director`. Researcher: `ebay-researcher`.

## Mission
Find products that sell on eBay at a modest-to-solid profit, source them from **US-based wholesale dropship suppliers that ship from US warehouses**, list them at a price that clears every fee with margin to spare, fulfill orders on time, and measure what the system earns with minimal Zac involvement.

## Locked rules (no agent overrides these)
1. **Wholesale suppliers only.** eBay allows dropshipping from a wholesale supplier. eBay prohibits buying the item from another retailer or marketplace (Amazon, Walmart, Target, Home Depot, Costco, AliExpress storefronts, etc.) and shipping it to the buyer. Violations can mean hidden listings, selling limits, or suspension. Every supplier must have a reseller or dropship program with a written agreement. No exceptions, no "just this once."
2. **US warehouses only.** Item ships from inside the US with real tracking from a US carrier (USPS, UPS, FedEx, or a US regional). No overseas origin, no consolidation through overseas hubs.
3. **Blind shipping required.** Supplier ships without their own invoice or retail branding in the box.
4. **Zac pulls the trigger.** Until graduation (below): Zac approves every listing publish, every supplier purchase, every refund, and every price change over 10 percent. Agents prepare and queue; Zac executes or approves.
5. **Money gate.** No agent spends money (supplier orders, subscriptions, promoted listing fees) without an approved line in `decisions-queue.md`.
6. **Listing caps.** Phase 1: max 5 new listings per day, 20 per week. Respect eBay account selling limits, whichever is lower.
7. **Margin floor.** Never list below 20 percent net margin or 5 dollars net profit per unit, whichever is higher. (Zac may change these numbers. Agents may not.)
8. **Kill switch.** If any trigger below fires, the director ends or pauses all active listings via API and alerts Zac. No auto-resume.
9. **Credentials.** eBay keys and tokens live only in environment variables. Never in the repo, logs, chat, queue, or memory. No card numbers anywhere.
10. **No browser bots unattended.** eBay's User Agreement restricts automated access outside its official APIs. The API path is primary. The Claude in Chrome path is supervised only: Zac present, Claude drafts and fills, Zac clicks publish.
11. **Module isolation.** Every script module fails to `SKIP` with a logged reason, never crashes the run.

## Org chart
```
Zac (approves, pulls the trigger)
  ebay-director  (agent: runs the loop, owns the queue, enforces rules)
     ebay-researcher     (agent: deep research, cloud scheduled task 6 AM, 12 PM, 7 PM ET, pushes to Claude app)
     ebay-scout          (skill: finds winning products)
     ebay-supplier-vet   (skill: verifies US wholesale suppliers)
     ebay-lister         (skill: prices and builds listings)
     ebay-fulfillment    (skill: orders, tracking, stock and price sync)
```

## Kill-switch triggers (pause all listings, alert Zac)
- Any eBay policy warning, listing removal, or account notice
- Late shipment rate or tracking upload rate trending toward eBay's seller standards thresholds
- 2 or more "item not received" or "not as described" cases in a rolling 30 days
- A supplier ships from outside the US, ships with retail branding, or changes terms
- Net P and L negative for 14 straight days after the first 10 orders
- API auth failure lasting more than 24 hours (sync is blind)

## Phases and graduation
- **Phase 0, Scaffold and sandbox.** Built, tested in eBay sandbox. No real listings.
- **Phase 1, Gated live.** Real listings, everything through the decision queue. Caps: 5/day, 20/week. Goal: 25 clean orders.
- **Phase 2, Partial autopilot.** Requires 25 orders, zero policy notices, zero defects, net positive. Then listing publishes inside caps and price syncs run without approval. Supplier purchases and refunds stay gated.
- **Phase 3, Full autopilot candidate.** After 90 days in Phase 2 with healthy metrics, Zac decides whether supplier purchases go auto, with a daily spend cap. Requires a supplier with API ordering.

## Honest expectations
Most dropship stores fail on fulfillment, not product research: stockouts, late tracking, and cost changes create defects, and eBay limits the account. Margins on commodity items are thin once fees are in. Measure net per order and defect rate, not revenue.

## Decisions log
Zac's decisions of 2026-10-09:
1. **Name:** pending confirmation (Zac said "eBay is back"; read as a voice-to-text name). Keep WKP Commerce as folder-safe placeholder. Do not use "eBay" in any store name or user ID.
2. **Cash model:** no float. Supplier orders paid per order, as orders come in, on Zac's credit card. Zac enters the card at supplier checkout himself. No card numbers anywhere in the repo, logs, queue, or memory.
3. **Entity and resale certificate:** none yet. Operate as a sole proprietor under Zac's name until done.
   - Suppliers will charge sales tax. Pricing adds a 10 percent supplier_tax_buffer on supplier cost plus shipping.
   - Vetting prefers suppliers that accept individuals or sole proprietors without a resale certificate. Suppliers requiring an EIN or certificate go to status PENDING_ENTITY, not REJECTED.
   - Ledger tracks supplier tax paid as its own column so it can be reclaimed or cut once the certificate exists.
4. **Defaults approved:** 20 percent margin floor, 5 dollars minimum net profit, 5 listings per day, 20 per week, gated until 25 clean orders.
5. **Categories:** open. First director run launches a deep research pass (Phase 0 kickoff), then stops and asks Zac where to go. No product search or listing happens until Zac picks.
