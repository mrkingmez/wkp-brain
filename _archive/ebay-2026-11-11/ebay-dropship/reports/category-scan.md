# Category scan, Phase 0 kickoff (FULL)

Date: 2026-10-10. Author: ebay-researcher (run directly by the director session; no parallel subagents were spawned).

## Read this first: what this scan can and cannot prove
- No Terapeak, Seller Hub, or eBay Browse API access was available. There is NO item-level 90-day sold vs. active data in this report. Category figures come from one third-party snapshot (ZIK Analytics, 30-day window pulled 2026-09-14). Everything is a lead for ebay-scout to verify, not a verified winner.
- Supplier "accepts a sole proprietor with no resale certificate" could NOT be verified for any named supplier. Public sources conflict and are mostly vendor marketing. Each supplier needs a direct email or signup test (that is ebay-supplier-vet's job, after Zac picks).
- Net-per-sale numbers use ASSUMED supplier cost and shipping (no real wholesale quotes were retrieved). Fees are verified from eBay (see Margin reality).

## What is selling (30-day US snapshot, third-party)
Source: https://www.zikanalytics.com/blog/best-selling-items-on-ebay/ (category data pulled 2026-09-14, article dated 2026-09-23; ZIK's own figures, not eBay's).

| Category | Sell-through (30d) | Units sold (30d) | Avg sold price |
|---|---|---|---|
| eBay Motors | 26.9% | 15,195,180 | 99.09 |
| Home & Garden | 21.8% | 8,077,276 | 54.51 |
| Collectibles & Art | 24.2% | 5,571,347 | 64.33 |
| Health & Beauty | 31.5% | 5,067,850 | 36.77 |
| Business & Industrial | 17.0% | 4,768,935 | 122.18 |
| Toys & Hobbies | 26.7% | 4,722,220 | 75.77 |
| Electronics | 27.9% | 4,225,297 | 134.57 |
| Clothing, Shoes & Accessories | 20.6% | 4,024,417 | 47.95 |
| Sporting Goods | 14.7% | 2,798,764 | 75.52 |
| Jewelry & Watches | 19.0% | 1,217,897 | 126.45 |

Overall average sell-through across 20 categories: 23.3%. Caveat: ZIK's article contradicts its own item numbers in places, and another site (Slayva, https://slayva.com/what-to-sell-on-ebay-2026/) claims 70 to 85 percent sell-through for some categories with no stated method. I discount that claim. Sell-through definitions vary by source (https://www.zikanalytics.com/blog/best-selling-items-on-ebay/ and the search summary of 2026 sell-through guides), so treat the percentages as relative ranking only.

Q4 holiday demand: UNVERIFIED for 2026. No 2026 eBay holiday forecast was found. Latest found is eBay's 2024 guidance (tech stays high Nov to Dec, spikes in Fashion, Electronics, Collectibles): https://export.ebay.com/sea-en/resources/seasonal-guide-for-ebay-sellers/top-selling-items-for-2024-holiday-season/ . Our hard excludes remove most of those (branded, electronics). Seasonal decor is a possible Q4 angle but is late (Oct 10) and unverified.

## What is not selling or is risky
- Sporting Goods is the lowest sell-through (14.7%) and ZIK calls stock bulky and slow. Business & Industrial 17.0%. Same source.
- Cheap light accessories (cables, screen protectors, pet tags): high volume but "easy for anyone else to sell," so price and feedback decide. Same ZIK source. Race to the bottom.
- Branded goods (Apple, Nike, Disney) draw instant VeRO claims; fragile glass/ceramic and oversize furniture kill margin; cosmetics, supplements, skincare have regulatory and return problems; electronics with warranty claims; items needing compatibility checks. Source: https://www.salehoo.com/learn/ebay-dropshipping (vendor guide, not eBay).
- Return and "not as described" rate BY CATEGORY: NOT AVAILABLE. No credible 2026 category-level data found. Defect-rate threshold sources conflict (SaleHoo guide cites under 2 percent; other sources cite 0.5 percent for Top Rated, 5 percent minimum in a dated 2014 post). Verify in Seller Hub. https://www.ecommercebytes.com/?p=6395
- Crackdowns: no official 2026 dropship limit announcement found. One report says a Feb 20, 2026 User Agreement update bans AI "buy for me" agents and LLM scrapers (affects automation, UNVERIFIED against eBay text). A vendor blog says handling-time accuracy is being enforced harder, UNVERIFIED. Sources: https://super-ds.com/blog/ebay-issue-resolution-center-2026 . eBay's own dropshipping policy page failed to load in this session, so the policy text itself is unverified from eBay; third-party guides agree the rule is wholesale/manufacturer only, retailers like Amazon, Walmart, Target prohibited (https://www.salehoo.com/learn/ebay-dropshipping).
- New seller limits: one guide says new accounts often start at 10 items or 500 dollars a month. Single-source, UNVERIFIED. Practical effect: our 5 per day / 20 per week caps may be moot until eBay raises the account limit. Check the account's actual limit before planning volume.

## Supply reality (US wholesale, sole proprietor, no resale certificate)
Honest answer: unproven. No supplier was confirmed to accept an uncertificated sole proprietor for eBay dropshipping.

| Supplier / platform | What public sources say | Status |
|---|---|---|
| Wholesale2B | Shopify app page claims "no resale license, upfront inventory or minimum order quantity," 29.99 per month with trial, lists eBay, mixed Canada/China/US suppliers, no US-warehouse guarantee. https://apps.shopify.com/dropship-auotmated-inventory | Claim is vendor marketing. Supplier origin mix means must filter US-only. UNVERIFIED |
| Doba | Does not require a certificate to use the platform; "suppliers mark which items need a resale certificate," many suppliers will not onboard without one or you pay tax. https://www.doba.com/blog/start-dropshipping/legal-policy-basics/for-us-dropshippers-how-to-register-for-a-resale-certificate-38402 . Pricing from about 24.99 per month with 0.99 trial per ZIK: https://www.zikanalytics.com/blog/ebay-wholesale-suppliers/ | Best fit on paper: item-level certificate flag, so uncertified items exist. Platform price UNVERIFIED |
| TopDawg | Described as 3,000+ verified US suppliers, eBay integration; Business tier 34.99 per month needed to sell (ZIK). Signup requirements (EIN/certificate) NOT found. https://www.zikanalytics.com/blog/ebay-wholesale-suppliers/ | UNVERIFIED, ask TopDawg |
| Spocket | 70 to 80 percent US/EU suppliers, eBay support, Starter 39.99 per month (plan that includes eBay differs by source). License question not found. https://debutify.com/blog/spocket-2026-guide-to-us-and-eu-dropshipping-suppliers | EU suppliers must be excluded (US ship-from rule). UNVERIFIED |
| Costway | Official terms: registered accounts only, marketplace (eBay/Walmart) approval is selective by "company scale and proven operational capability." https://www.costway.com/dropship-terms-conditions | Likely a hard path for an individual. Warehouse list is third-party only |
| WorldWide Brands (directory) | 299 one-time; many listed suppliers require a resale certificate (ZIK). | Directory, not a supplier. Spends money, needs approval |
| Big Rock Sports, Cosmoprof, WASCO | Require commercial storefront, license, or dealership (ZIK). | Reject for now (PENDING_ENTITY at best) |
| CJdropshipping, EPROLO, AliExpress | China-based even with US warehouses. | Excluded by locked rule 2 and 3 |

Flag: general guidance says a resale certificate requires a state sales tax permit first. Until Zac has one, expect to pay sales tax (our 10 percent buffer covers it) and many supplier accounts will be PENDING_ENTITY.

## Margin reality
Verified fees (eBay fee page, fetched 2026-10-10): https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822
- Most categories: 13.6 percent up to 7,500 dollars; books/movies/music 15.3 percent; jewelry 15 percent; per-order fee 0.30 on orders of 10 dollars or less, 0.40 above. Recorded in data/fee-table.md with date checked.
- Fee base may include shipping and sales tax collected from the buyer (one third-party guide, unverified); pricing.py applies the percentage to item price only and builds shipping into price.

Floor prices computed with tools/pricing.py (fvf 13.6 percent, 0.40 fixed, 10 percent supplier tax buffer, 20 percent margin floor, 5 dollars minimum profit). Supplier cost and ship are ASSUMED:

| Assumed cost + ship | Floor price | Net per sale | Net margin |
|---|---|---|---|
| 8 + 4 | 21.99 | 5.40 | 24.6% |
| 12 + 5 | 28.99 | 5.95 | 20.5% |
| 20 + 6 | 43.99 | 9.01 | 20.5% |
| 30 + 8 | 63.99 | 13.09 | 20.4% |
| 45 + 10 | 91.99 | 18.58 | 20.2% |

Takeaway: at the margin floor the net is roughly 5 to 13 dollars on items priced 22 to 64 dollars. Anything under about 20 dollars sold price cannot clear the 5 dollar floor. The 10 percent tax buffer plus 13.6 percent fees means wholesale cost must be about 50 to 55 percent of the sold price. Promoted listing fees would cut further (not modeled).

## Top 5 categories to enter
Ranking blends the ZIK volume and sell-through with our sweet spot and hard excludes. All confidence is LOW to MEDIUM because no item-level eBay data and no supplier terms are verified.

1. **Home & Garden: small household, kitchen, organization (non-brand)**. 8.08M units, 21.8% sell-through, avg sold 54.51 (ZIK). Fits sweet spot (20 to 80 dollars, small box). Sample: drawer/closet organizer set, wholesale cost 12 to 20 dollars assumed. Net per sale about 6 to 9 dollars at floor. Confidence: Medium.
2. **Auto accessories that need no fitment (universal)**. eBay Motors is the biggest category at 26.9% sell-through, 15.2M units (ZIK). Sample: microfiber car-care kit or universal trunk organizer, cost 10 to 20 dollars assumed. Net about 6 to 9 dollars. Risk: fitment and brand-name parts, so stay universal. Confidence: Medium-Low.
3. **Toys & Hobbies, unlicensed (craft, hobby tools, puzzles, bulk building/art supplies)**. 26.7% sell-through, 4.72M units (ZIK). Sample: unbranded craft/art supply set, cost 12 to 18 dollars assumed. Net about 6 to 8 dollars. Risk: licensed characters trigger VeRO, so only generic. Confidence: Medium-Low.
4. **Pet supplies (non-consumable: beds, grooming tools, toys)**. Named in our scout sweet spot, but no pet sell-through figure was retrieved, so the demand case is UNVERIFIED. Sample: unbranded grooming brush or pet bed, cost 12 to 25 dollars assumed. Net about 6 to 10 dollars. Confidence: Low.
5. **Hand tools and garden/workshop supplies (Business & Industrial, Home & Garden)**. Business & Industrial is 17.0% sell-through but 4.77M units at avg 122 (ZIK), so low sell-through with high ticket. Sample: unbranded hand-tool or drill-bit set, cost 20 to 30 dollars assumed. Net about 9 to 13 dollars. Risk: slow sell-through, weight. Confidence: Low.

Watch list (not top 5): seasonal Christmas decor (timing late and unverified).

## Top 5 categories to avoid
1. **Electronics and anything with a battery or charger.** Hard exclude for first 90 days; warranty claims; brand-heavy listings (the top sellers in the ZIK list are Apple items), so brand-gated.
2. **Health & Beauty (cosmetics, supplements, skincare).** 31.5% sell-through tempts, but hard exclude (certification/regulation, returns). Source: https://www.salehoo.com/learn/ebay-dropshipping
3. **Branded apparel, shoes, licensed goods.** VeRO risk; the adidas, Pokemon, Apple items topping the ZIK list are brand-gated. Instant claim risk.
4. **Sporting Goods, bulky.** Lowest sell-through at 14.7% and bulky freight (ZIK). Fails oversize exclude.
5. **Cheap light accessories (cables, screen protectors, pet tags) and Jewelry & Watches.** Race to the bottom (ZIK); jewelry is 19.0% sell-through with a 15 percent fee and heavy brand/authenticity exposure. Cannot clear the 5 dollar floor at low prices.

## Recommended next step
Zac picks 1 to 3 categories. Then scout verifies item-level 90-day sold data (Terapeak/Seller Hub needed, Zac's account) and supplier vet tests actual signup terms. Biggest unknown to resolve first: whether any US wholesale dropship supplier will actually onboard Zac without a certificate. The single cheapest test is Doba's free/0.99 trial, to see how many items in a chosen category carry no certificate flag. That is a SPEND item and was not done.
