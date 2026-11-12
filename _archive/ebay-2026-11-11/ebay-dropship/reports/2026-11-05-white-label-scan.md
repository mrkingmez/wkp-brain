# eBay white label scan (2026-11-05)

Zac's ask: has anyone looked at white label / private label for eBay? Answer: no. Nothing in `ebay-dropship\` before today covers it (checked CLAUDE.md, decisions-queue.md, data\, and all six prior reports). This is the first pass.

Read-only. Nothing listed, bought, priced, or messaged. No supplier contacted. No credentials used.

## Read this first (honest summary)

1. **No candidate passes cleanly on the evidence I could retrieve.** Of the five organizer and auto items I could cost out, four fail the 5 dollar net floor on the assumptions below. One (magnetic tool holder) looks workable but its supplier cost and MOQ are not verified.
2. **White label breaks two locked rules as written.** Rule 1 and 2 say US wholesale supplier, US warehouse. Zac's 10/09 cash model says no float, pay per order. Real white label means buying inventory up front, usually from an overseas factory, then shipping from a US address. That is a Zac decision, not mine. Queued as **EBAY-2026-11-05-01** in `D:\WKP\logs\DECISIONS.md`.
3. **The 10/24 "max cost" column in candidates.csv looks wrong.** See "Math check" below. It matters because some items may have been marked unattractive on bad arithmetic.
4. **The demand numbers are from the 10/24 Terapeak pass (Zac's Seller Hub), not new.** I could not pull sold data this session (see "Could not retrieve").

## Math check (needs ebay-director to confirm)

Fee: 13.6 percent plus 0.40 per order (`data\fee-table.md`, checked 2026-10-10).
Net profit = 0.864 x price - 0.40 - landed cost - outbound postage.
For exactly 20 percent net margin, total cost (landed + postage) must be at or under 0.664 x price - 0.40.
For the 5 dollar floor, total cost must be at or under 0.864 x price - 5.40.

`candidates.csv` (10/24) lists "Max cost for 20% net" of 23.85 for the washer door boot at 57.40. Using the same break-even formula the 10/24 report used, the answer is (0.664 x 57.40 - 0.40) / 1.10 = **34.28** (with the 10 percent tax buffer, no postage). The file's 23.85 equals (0.464 x 57.40 - 0.40) / 1.10, which takes the 20 percent margin out twice. Same pattern on the oven igniter (file 12.04, formula 17.37) and the trimmer head net (file 9.33, formula 13.72). The break-even price table in the 10/24 Doba section is correct. Possible alternative: the file silently reserved an unlabeled postage allowance. I cannot tell which. Before any supplier or part gets rejected on those max-cost numbers, re-run them.

## Assumptions used in every cost-out below

- Prices are Terapeak 90-day averages from the 10/24 pass.
- Outbound postage is an ASSUMPTION (not retrieved). Most of these sell with free shipping (74 to 94 percent of listings per Terapeak), so postage comes out of the sale price.
- Landed cost = factory price + assumed 1.50 to 2.00 per unit for freight and duty. Duty rate for these items NOT retrieved (see below).
- No tax buffer applied, because an importer buying overseas pays no supplier sales tax.

## Candidates (7)

### 1. Magnetic tool holder bar, 24 inch, unbranded (auto/workshop/organization)
- **Demand (10/24 Terapeak, retrieved):** avg sold 22.96, sell-through 15.19 percent, 1,099 sellers, 78 percent free ship. Best sell-through of every organizer-type search.
- **Cost evidence (this pass):** US retail 21.74 (Astro Pneumatic, eppys.com), 25 to 27 (Uline, which mentions a private label program, terms not shown), 30.59 (Master Magnetics). One Global Sources listing at 0.57 per unit, 1 piece MOQ, from China; I do not trust that number. No real MOQ or tier price retrieved.
- **Scenario:** landed 4.00 (assumed), postage 5.50 (assumed, 725 g bar). Net = 0.864 x 22.96 - 0.40 - 4.00 - 5.50 = **9.94, about 43 percent**. Clears the floor if the cost guess holds.
- **Upfront cash:** MOQ not retrieved. If 100 to 200 pieces at 4.00, about 400 to 800 dollars, plus a sample order.
- **Risks:** 1,099 sellers, price pressure. Heavy for its size, so postage swings the result (each extra dollar of postage is a dollar off net). Magnet pull claims (Uline lists 20 lb per inch) must not be copied or overstated.

### 2. Car trunk organizer, foldable, unbranded
- **Demand (10/24):** avg 24.61, sell-through 4.68 percent, 554 sellers, 84 percent free ship. Top sellers priced 9 to 13.
- **Cost evidence:** an Alibaba trunk organizer listing shows 6.90 each at 100 to 499 pieces with customization offered (from a search result summary; I could not open the page, it returned 404). Alibaba's own seller blog says private label car care MOQs typically run 500 to 1,000.
- **Scenario:** landed 6.90 + 2.00 = 8.90, postage 9.00 (bulky, assumed). Net at 24.61 = **2.96, 12 percent**. Fails the 5 dollar floor. At the 13 dollar top-seller price it loses money.
- **Upfront cash:** 100 x 6.90 = 690 before freight and duty.
- **Risks:** bulky returns, poor fit for a budget-tight start.

### 3. Seat gap filler (2-pack), unbranded
- **Demand (10/24):** avg 10.07, sell-through 7.86 percent, 696 sellers, 91 percent free ship.
- **Cost evidence:** Julisheng (Made-in-China) 1.50 to 1.70 per piece at 500 MOQ. Faire brands list 80 to 100 dollar order minimums, but Faire bans eBay resale (see policy section).
- **Scenario:** landed 2.50, postage 4.00 (assumed). Net at 10.07 = 8.70 - 0.40 - 2.50 - 4.00 = **1.80**. Fails.
- **Upfront cash:** 500 x 1.50 to 1.70 = 750 to 850.
- **Verdict:** too cheap a sale to carry postage. Only works as a multi-pack bundle, price unproven.

### 4. Windshield sun shade, folding, unbranded
- **Demand (10/24):** avg 18.95, sell-through 8.56 percent, 2,054 sellers (crowded), 90 percent free ship. Branded sellers (Plasticolor, Motor Trend) show as eBay "best selling" on a search page (no sales counts shown).
- **Cost evidence:** Hebei Cartine (Made-in-China) 5.50 to 6.80 at 50 sets MOQ, the lowest MOQ I found anywhere. Merchize lists print-on-demand sunshades at MOQ 1, origin stated as China, US ship-from NOT confirmed.
- **Scenario:** landed 7.65, postage 6.00 (assumed). Net at 18.95 = 15.97 - 7.65 - 6.00 = **2.32**. Fails.
- **Upfront cash:** 50 x 5.50 to 6.80 = 275 to 340. Seasonal (sun), wrong time of year in November.

### 5. Microfiber towel multi-pack with own label (auto detailing / household)
- **Demand:** NOT retrieved. No Terapeak search was run for it on 10/24. Only German eBay lot listings surfaced.
- **Cost evidence:** MicrofiberWholesale lists a 16x16 300GSM private label towel with "no minimum" on its page and a case of 288. Its OEM page offers logo printing, private labeling and branded packaging, "domestic and overseas factories", lead time "just days" for small in-house runs, ship-from not stated, no price retrieved (page fetch returned 429 on the product page). Contact on the page: 877-791-6677. This is the only lead that may be a US-based supplier.
- **Scenario:** cannot compute. Test: total cost per sellable pack must be at or under 0.664 x price - 0.40.
- **Upfront cash:** unknown, one case of 288 towels is the unit of purchase.
- **Why it is on the list:** light, no fitment, no battery, no hazmat, and a US source exists. It is also the only candidate that could satisfy a "US supplier" reading of the rules.

### 6. Aftermarket appliance parts under own brand (door boot gasket first)
- **Demand (10/24, strongest of the scan):** washer door boot gasket avg 57.40, sell-through 24.69 percent, 336 sellers, 87 percent free ship. Fridge door gasket 57.25 at 29.6 percent. Range element 33.73 at 24.0 percent (252 sellers). Parts sold 3 to 10 times better than organizers.
- **Cost evidence:** none for an own-brand version. No factory, no MOQ, no price. The three US distributors Zac emailed (Reliable, ISS, Safe Appliances) sell OEM and third-party parts, not blank-label product; replies not received as of the files I read.
- **Scenario with corrected math:** at 57.40, 20 percent net needs total cost (landed + postage) at or under 37.71. With 8 to 10 postage (assumed), landed can be about 28 to 30. The 10/24 file's 23.85 is lower than needed.
- **Upfront cash:** unknown.
- **Risks (largest of any candidate):**
  - Fitment returns are the main loss in this category. Buyer sends it back, you eat postage both ways.
  - OEM part numbers: eBay requires "fits" or "compatible with" ahead of a brand name (eBay VeRO page). A 2025 federal ruling on pool parts (Bestway) supports truthful compatibility statements, but it is not an eBay ruling and not legal advice.
  - Heating elements and igniters carry fire or gas risk. Product liability insurance cost NOT retrieved. Start with gaskets, not heat parts.

### 7. Print on demand under Zac's own brand (WKD art on US print providers)
- **What it is:** Zac's own designs on products through Printify, which has a one-click eBay US integration (Printify help center and blog; setup details from third-party guides). Zero inventory.
- **Demand:** NOT retrieved for any POD item on eBay.
- **Cost / MOQ:** MOQ 1, upfront 0. Per-item cost NOT retrieved.
- **Risks:** an eBay community thread reports a "Warehouse Policy" error blocking listings for sellers on the official Printify and Printful integrations. Whether eBay's AI-content disclosure applies to Zac's AI-generated art NOT checked. AI-generated art copyright limits NOT researched.
- **Fit:** the only candidate with no cash and no inventory, but it is outside the household/auto categories EBAY-001 approved and outside "wholesale supplier" as rule 1 is written.

## Upfront cash summary

| # | Item | Price (avg sold) | Est. net per sale | Est. upfront at lowest MOQ found | Floor check |
|---|---|---|---|---|---|
| 1 | Magnetic tool holder 24" | 22.96 | about 9.94 (assumed costs) | 400 to 800 (MOQ not retrieved) | Pass on assumptions |
| 2 | Trunk organizer | 24.61 | about 2.96 | 690 plus freight | Fail |
| 3 | Seat gap filler | 10.07 | about 1.80 | 750 to 850 | Fail |
| 4 | Sun shade | 18.95 | about 2.32 | 275 to 340 | Fail |
| 5 | Microfiber multi-pack | not retrieved | not computable | one 288-unit case, price not retrieved | Unknown |
| 6 | Aftermarket appliance gasket | 57.40 | not computable (no cost) | not retrieved | Unknown, best demand |
| 7 | POD own-brand | not retrieved | not retrieved | 0 | Unknown |

## How white label differs from dropship

| | Dropship (current plan) | White label |
|---|---|---|
| Inventory risk | None, supplier holds stock | You own it. Unsold units are cash lost |
| Upfront cash | None (pay per order) | Hundreds to a few thousand, before the first sale |
| Margin | Squeezed. 10/24 pass: Doba organizers cost too close to sold price | Higher possible, because factory price is below wholesale-resale price |
| Returns | Supplier policy, refund when approved | You eat the return. Item comes back to you, resale only if unopened |
| Handling and defects | Depends on supplier tracking | Own stock means one-day handling and your own tracking, less risk of late shipments |
| Lead time to start | Days | Weeks, overseas factory lead time NOT retrieved |
| Brand risk | Supplier brand on the item | Your own mark. Your own trademark exposure |
| Rules fit | Matches rules 1 to 3 | Conflicts with the 10/09 no-float cash model, and rule 1 as written |

The 10/24 pass found that cheap garden-rack sellers beating Doba resellers ship from California, New Jersey and Kansas from their own stock. White label (or importing) is the form of the business those sellers are already running. That is the case for looking at it, not proof it works for Zac's budget.

## Brand, trademark and IP

- **eBay rules (VeRO page fetched):** brand names allowed only if the product is made by or compatible with that brand; "fits" or "for" before a brand; third-party marks in a store name or username are restricted; sellers must write their own text and take their own photos. The page does NOT describe an own-brand registration process. I found no eBay equivalent of Amazon Brand Registry. Not confirmed either way.
- **Name your own brand carefully:** run a USPTO search before ordering a label. Registering a mark costs 350 dollars per class per several 2026 commercial sources (not verified on uspto.gov). Optional at the start, but without it nobody stops a copycat.
- **Tariffs and import:** Section 301 duties on China still apply per secondary sources. Household-goods rate NOT retrieved. De minimis no longer covers China-origin goods per several blogs, so a customs bond or broker may be required; NOT confirmed. This could add real cost per unit and must be checked before any order.
- **Safety and compliance not researched:** CPSC, Prop 65, UL marks, magnet labeling. Cheap imported magnets and anything electrical carry the most risk. Needs a check before any candidate moves forward.

## eBay policy issues

- **Faire is closed for eBay.** Faire's retailer terms prohibit fulfilling orders on eBay, Amazon, Etsy and other third-party marketplaces, and individual brands add their own bans. Any Faire brand is out unless it grants written permission.
- **Seller standards:** official eBay page says up to 2 percent of transactions can have defects, Below Standard needs defects from more than four buyers, and a higher fee applies from 1 Aug 2026 to sellers Below Standard for four or more consecutive months (search summary of the policy page, not read in full). The 3 percent late-shipment figure on third-party blogs is not an eBay rule.
- **Kill-switch triggers in CLAUDE.md** (2 INR or SNAD in 30 days) are tighter than eBay's. Own-brand returns for "not as described" count against the kill switch.
- **Listing caps and the 20 percent floor** still apply to white label items.

## Stronger categories noticed

- **Parts and consumable-type replacements:** sell-through 14 to 30 percent versus 1 to 5 percent for organizers (Terapeak, 10/24). Strongest signal in the repo. White label fit is gaskets, belts, rollers, not heating parts.
- **Appliance control boards (salvage track, TASKS.md):** 31 to 49 percent sell-through at 65 to 100 dollars. Not white label; used-parts model.
- **Toys and Hobbies:** 26.7 percent sell-through (ZIK, third party, 30-day). Not checked at item level.
- None of these has a retrieved white-label supplier.

## Could NOT retrieve

- **Any new sold-listing data.** eBay's sold search returned HTTP 403 to my fetch, an individual eBay item page also returned 403. Terapeak and Seller Hub need Zac's logged-in session. The eBay Browse API returns active listings only, not sold, so I did not run it. Every demand figure above is from the 10/24 Terapeak pass.
- Supplier price tiers and MOQ for the magnetic bar. The Global Sources 0.57 figure is not trusted.
- MicrofiberWholesale price, ship-from, MOQ for private label (429 error).
- Alibaba trunk organizer page (404). The 6.90 price is from a search result summary only.
- Factory lead times, sample costs, freight cost, duty and customs bond requirements.
- Outbound postage for any item (all assumed).
- Any own-brand supplier for appliance parts.
- eBay's official position on own-brand listings, Brand item specific, or POD in 2026.
- Product liability insurance costs.
- Replies from Reliable, ISS, Safe Appliances (outreach is already sent by Zac; I did not check the inbox).

## What would move this forward (Zac decides, I did none of it)

1. Answer EBAY-2026-11-05-01 (may Zac hold inventory, and may it come from an overseas factory into a US address).
2. Terapeak pulls in Seller Hub: magnetic tool holder (sold counts for US ship-from listings only), microfiber towel packs, door gasket brand-less listings.
3. If yes to 1: sample quotes, which means messaging suppliers. That is a spend-and-contact step I am not allowed to take. Smallest first move: ask MicrofiberWholesale and two magnet bar factories for price and MOQ.
4. ebay-director re-runs the max-cost column in candidates.csv with the corrected formula.

## Sources

- eBay VeRO / IP policy: https://www.ebay.com/help/policies/prohibited-restricted-items/intellectual-property-policy?id=4349
- eBay seller standards (search summary): https://www.ebay.com/help/selling/selling-seller-performance/seller-performance-standards?id=4347
- eBay sellercenter IP: https://www.ebay.com/sellercenter/resources/intellectual-property
- Faire eBay resale restrictions (search summary): https://www.faire.com/support/articles/18524831904667
- MicrofiberWholesale OEM page: https://microfiberwholesale.com/pages/oem-brands
- Microfiber private label product page (not opened, 429): https://www.microfiberwholesale.com/products/16x16-300gsm-microfiber-towels-private-label
- Global Sources magnet bar listing (unverified price): https://m.globalsources.com/Tool-organizer/Wall-Mount-Tool-Magnet-Bar-Rack-1235638657p.htm
- Uline 24 inch magnetic bar: https://www.uline.com/Product/Detail/H-6411/Tool-Storage/Magnetic-Tool-Holder-24
- Alibaba MOQ guide (vehicle accessories): https://seller.alibaba.com/blogs/2026/southeast-asia/vehicle-accessories/moq-lead-time-guide-alibaba-b2b
- Alibaba trunk organizer (search result, page 404): https://www.alibaba.com/product-introduction/best-performance-customized-car-trunk-organizer_1601029181997.html
- Printify eBay US integration: https://help.printify.com/hc/en-us/articles/4483617199761-How-can-I-connect-my-eBay-US-store
- eBay community, POD warehouse policy error: https://community.ebay.com/forum/selling-57920/topic/warehouse-policy-error-blocking-my-listings-legal-pod-seller-using-printifyprintful-161178/?focus_post=214125
- Trademark fee roundup (commercial, not uspto.gov): https://beancount.io/blog/2026/09/27/how-much-does-trademark-cost-2026-uspto-fees-guide
- Repo: `ebay-dropship\reports\2026-10-24-terapeak-doba-first-pass.md`, `data\candidates.csv`, `data\fee-table.md`, `data\suppliers.csv`.
