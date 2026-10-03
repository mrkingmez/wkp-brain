@../ME.md
@../projects.md

# Kingdom Planners — Digital Planner Shop (Etsy)

## What This Is
Second Etsy shop, completely separate from WarriorKingDesigns. Sells digital spreadsheet planners and trackers — instant download, no physical fulfillment, no POD supplier.

**Why separate, not merged:** different buyer intent entirely. WKD sells physical puzzles and wall art; this sells digital tools. Same lesson learned from the t-shirt-mixing problem that muddied WKD's early reviews. Do not propose merging these shops.

Shop name is a pun on Zac's last name (King) and was chosen deliberately to stay broad — it covers budget, debt, military, wedding, baby, and road-trip planners without boxing the shop into "military only."

## Brand
- **Navy** `#1B3A4B` — primary. Trust/security, matches financial-planning buyer psychology.
- **Warm gold/amber** `#E8A33D` — accent, the stop-scroll contrast color.
- **Cream/off-white** background, not stark white.
- **Fonts (Adobe Fonts, confirmed available):** Hagrid-Extrabold for wordmark/headline, Roboto-Medium for tagline/body.

**Logo status:** v1 built and exported to Adobe Express (navy circle badge, crown icon, KINGDOM / PLANNERS wordmark) — flagged as too generic/clip-art. v2 in progress: a ChatGPT/DALL-E prompt was written targeting 2026 logo trends (custom wordmark as hero, Neo Deco linework crown, one deliberate signature detail, flat 2D vector). When a concept comes back, rebuild it in Adobe Express with real vector shapes and the actual brand fonts. Do not use the raw AI image as the logo file — it won't hold up at different sizes.

## Products Built — All Verified, Zero Formula Errors
| Product | Status | Notes |
|---|---|---|
| **Complete Budget System** | **FILE MISSING — 2026-09-24** | Flagship. 16 tabs: paycheck-style weekly budgeting (5 week blocks/month × 12 months), envelope system with auto-carryover, Debt Tracker fed from monthly actuals, adaptive Payoff Plan. Confirmed 2026-09-24 (etsy-director prep pass): not present anywhere on disk (checked every LOCAL-PATHS.md location plus a full C:/D:/E:/L: drive scan). `C:\Users\kingz\Downloads\Kingdom Planners - Handoff Document.md` confirms it was built in a web chat session and saved to that session's `/mnt/user-data/outputs/`, never downloaded to permanent storage — the exact loss pattern root CLAUDE.md's file retention rule warns about. Needs Zac to re-open that original chat and re-download, or rebuild from scratch, before this product can get a listing pack, photo cards, or be zipped into the Military Family bundle. Its $19 sale price stays as previously set; no listing copy exists for it since inventing tab names/features from a description alone isn't acceptable.
| **Debt Freedom Planner** | Ready | 3 tabs, verified 2026-09-24 against the real file: Start Here, Debt Setup (6 debt slots, Snowball/Avalanche dropdown), Payoff Schedule (36-month live projection, auto-rollover between debts) |
| **PCS Moving Budget Planner** | Ready | 8 tabs, verified 2026-09-24: Start Here, Move Details, Entitlements (DLA/MALT/per diem/TLE), Move Budget, PPM Decision (vs. Government Constructive Cost), Weight Allowance, PCS Timeline (90-day checklist), Rate Reference |
| **Deployment Pay Budget Planner** | Ready | 8 tabs, verified 2026-09-24: Start Here, Deployment Details, Pay Estimator (HFP/IDP, FSA, HDP, CZTE), Savings Deposit Program (10% calculator), Home Budget, Savings Plan, Pre-Deployment Checklist, Rate Reference |
| **VA Disability Claim Tracker** | Ready | 8 tabs, verified 2026-09-24: Start Here, Condition Log, Combined Rating (real whole-person VA math, not naive addition), Payment Estimator, Rate Tables (official 2026 figures), Evidence Tracker, Appointments & Deadlines, Appeal Tracker. **Genuine differentiator vs. competitors** |
| **Terminal Leave / ETS Transition Planner** | Ready | 7 tabs, verified 2026-09-24: Start Here, Separation Details, Leave Decision (terminal leave vs. sell-back, side by side), Transition Timeline (12-month, not 6 as previously noted here), Budget Bridge (pay-gap calculator), Benefits Checklist, Job Search Tracker |
| **Road Trip Planner & Tracker** | Ready | 7 tabs, verified 2026-09-24: Start Here, Trip Setup, Route Planner (leg-by-leg fuel cost), Budget, Daily Log, Packing List, Vehicle Prep. **Correction:** the real file has no separate Lodging Planner or Stops & Attractions tabs, no pie chart, and no built-in mileage-deduction calculator — those were in an earlier plan/description that doesn't match what's actually in the shipped file. Route/fuel/budget tracking covers the same ground, just structured differently. |
| Budget-Envelope-Debt-Tracker | Superseded | Complete Budget System replaced it. Could become a cheaper "lite" tier, or retire it |

All files are Excel-native. **A real Google Sheets compatibility pass (actually opening the files in Sheets) still has not been run.** Formula-level scan done 2026-09-24 against all 6 confirmed files for the functions that typically break in Sheets (XLOOKUP, FILTER, UNIQUE, LET, SORT, SEQUENCE, LAMBDA, TEXTJOIN, IFS, SWITCH): none found, everything is plain IF/MIN/MAX/RANK/EDATE-style logic. Good sign, not a substitute for actually opening each file in Sheets. Do this before listing.

## Pricing
- Etsy fee model: ~9.5% of sale price + $0.45 (6.5% transaction + ~3%+$0.25 processing + $0.20 listing)
- **Anchor + sale price sheet (built 2026-09-24, per the etsy-director agent's standing "never price like a simple planner" rule — this table didn't exist before this pass, just the two flat numbers below):**

| Product | Anchor ("was") | Sale price | Confidence |
|---|---|---|---|
| Complete Budget System | $26 (recommended, file missing) | $19 (already set) | locked |
| Debt Freedom Planner | $16 (new) | $12 (already set) | locked |
| PCS Moving Budget Planner | $22 | $16 | comp-supported |
| Deployment Pay Budget Planner | $23 | $17 | thin comp data, mostly analogy |
| VA Disability Claim Tracker | $25 | $18 | comp thin but real |
| Terminal Leave / ETS Transition Planner | $24 | $18 | no direct comps, complexity analogy |
| Road Trip Planner & Tracker | $19 | $14 | comp-supported |
| Military Family Complete System (bundle, 6 military-relevant planners, Road Trip excluded) | $100 | $75 | bundle-discount % unverified |

Full sourcing/confidence notes and the reasoning behind each number are in `D:\05 Kingdom Planners\Kingdom-Planners-Listing-Prep-Batch-2026-09-24.docx` (Section 1). Bundle can't actually be built/listed until Complete Budget System's file exists.
- Cross-sell mechanism: Etsy doesn't support merged bundle listings across formats, but since every KP product is digital, the bundle itself works as one zipped listing. Each individual listing description also cross-promotes the bundle listing directly (no coupon code needed for this shop specifically; revisit the `BUNDLE10`-style coupon idea only if Etsy's bundle listing underperforms the cross-sell text alone).

## Platform Decision — Researched, Not Guessed
**Etsy only.** eBay was checked (no automated digital delivery, requires manual fulfillment, buried category) and Amazon (no real marketplace lane for standalone spreadsheet templates). Neither fits. Revisit only once the shop has real traction.

## What's Not Done — The Real To-Do List

**Shop mechanics (not started):**
- Create the Etsy shop under the Kingdom Planners name — **BLOCKED 2026-09-07: Etsy is showing a $29 one-time setup fee Zac doesn't have on hand right now.** This gates only the shop-goes-live step. Every free task below (per-listing copy, tags, pricing the 5 unpriced products, bundle price, photos, AI-disclosure research, About/policy copy) can and should be done now so launch is paste-and-go the moment the $29 is available.
- Government ID verification — takes a few days, start early (also blocked behind shop creation)
- Business email (done, 2026-09-07): **kingdomplannerszk@gmail.com** — separate from personal and from WKD. Use this for the Etsy shop registration, Pinterest business account, and all Kingdom Planners correspondence.
- Decide on LLC/EIN — real legal/tax question, worth 20 minutes with a tax preparer once money is coming in, not a casual decision
- Shop banner (navy/gold palette)
- About section copy
- Shop policies — digital instant-download, no-refund-standard language
- **AI-disclosure question — researched 2026-09-24.** Etsy's own policy pages block automated fetching, so this is sourced from search results/third-party citations, not a direct pull of Etsy's page text — needs a live logged-in-browser confirmation of the literal current checkbox/field wording before launch. What's confirmed: the listing editor's "Who made it?" stays "I did," and Etsy's disclosure test is about degree of creative contribution, not medium — no clean carve-out found for "AI-assisted tool" vs. "AI-generated art." Verdict: disclose, same as WKD, different wording since the thing being disclosed is different (AI helped build the tool, not the finished content). Locked sentence, distinct from WKD's: "This planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork." Full sourcing in the Section 6/0 notes of `Kingdom-Planners-Listing-Prep-Batch-2026-09-24.docx`.

**Per-listing work — DONE for 6 of 7, 2026-09-24:**
- Titles, 13 tags, and descriptions written for Debt Freedom Planner, PCS, Deployment, VA Tracker, Terminal Leave, and Road Trip — all checked against Etsy's confirmed-current 140-char title / 13-tag / 20-char-per-tag limits. Complete Budget System blocked, file missing (see Products table above).
- Individual pricing (anchor + sale) set for the 5 previously-unpriced products, plus the bundle. See Pricing section above.
- Military Family bundle price set ($100 anchor / $75 sale), but the bundle listing itself is blocked on Complete Budget System's missing file.
- Full pack, About section, shop policy draft, and AI-disclosure language: `D:\05 Kingdom Planners\Kingdom-Planners-Listing-Prep-Batch-2026-09-24.docx` / `.md`.
- Listing photos / mockup screenshots: still NOT done. See kp-prep skill status below — cards 1 and 6 have real content ready (in the batch doc) but need the actual image built in Adobe Express; cards 2-5 need Zac to screenshot the real working files by hand; cards 7-8 are existing permanent assets, nothing further needed.

**Marketing (not started):**
- Pinterest business account + boards specific to this shop, separate from WKD's

## Product Roadmap — Discussed, Not Built
- Moving Budget Planner (civilian version of PCS)
- Wedding Budget Planner
- New Baby / Nursery Budget Planner
- Rental Property Income Tracker
- Freelance/Small Business Invoice + Expense Tracker
- **PMP-style project tracker** — WBS, timeline, budget/earned-value, risk register. Deliberately dual-purpose: sellable on Etsy (generic enough for broad appeal) AND usable for WKP's own real productions.

## Standing Assessment
The product pipeline is far ahead of the actual shop. Seven finished products, zero listings, no shop created. The highest-leverage work is **listing copy and shop mechanics, not building more spreadsheets.** Push back if the instinct is to build product number eight before anything is live.

## Open
[FILL IN — Etsy shop created y/n, verification status]
[FILL IN — Google Sheets compatibility test results, real open-in-Sheets pass still pending]
[FILL IN — logo v2 final]
[DONE 2026-09-24 — local path for the 6 confirmed .xlsx files is `D:\05 Kingdom Planners\excel\files.zip`; add to LOCAL-PATHS.md. Complete Budget System's file is NOT in that zip and isn't found anywhere on disk — see Products table above.]