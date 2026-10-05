# Kingdom Planners: Listing Prep Batch
**2026-09-24. Prepared while Zac is off for the weekend, back Monday night. DRAFT: nothing here is listed or published.**

This is free prep work only. The shop itself is still blocked on Etsy's $29 setup fee (untouched here, that's Zac's spend call). Everything below is paste-and-go the moment the shop exists.

---

## 0. Read this first: status flags

**Complete Budget System file is missing.** This is the flagship product (16 tabs, the one Kingdom-Planners\CLAUDE.md calls out as "Ready" at $19). I searched every location in LOCAL-PATHS.md plus a full scan of C:, D:, E:, and L: drives. What actually exists on disk in `D:\05 Kingdom Planners\excel\files.zip` is 6 of the 7 products: Debt Freedom Planner, PCS Moving Budget Planner, Deployment Pay Budget Planner, VA Disability Claim Tracker, Terminal Leave/ETS Transition Planner, Road Trip Planner. Complete Budget System is not among them. A handoff document at `C:\Users\kingz\Downloads\Kingdom Planners - Handoff Document.md` explains why: it was built in a web chat session and saved to that session's `/mnt/user-data/outputs/`, which is not permanent storage. This is the exact failure mode root CLAUDE.md's file retention rule warns about. I cannot write listing copy for a file I cannot open, since that would mean inventing tab names and features, which the brief explicitly told me not to do. Full pack below covers the 6 confirmed products. Complete Budget System needs Zac to re-open that original chat and re-download the file, or rebuild it, before it gets a listing pack. Its price stays at the already-set $19 sale in the table below, since that number came from Zac's own prior pricing decision, not from me.

**Google Sheets compatibility:** Kingdom-Planners\CLAUDE.md flags this as not yet tested by actually opening the files in Sheets. I scanned all 6 confirmed files' formulas for the functions that commonly break in Sheets (XLOOKUP, FILTER, UNIQUE, LET, SORT, SEQUENCE, LAMBDA, TEXTJOIN, IFS, SWITCH) and found none. Everything uses plain IF/MIN/MAX/RANK/EDATE-style logic, which is safe in both. That's a good sign, not a verified pass. The listing copy below still says "works in Excel and Google Sheets" because that claim is already locked as a permanent shop asset (card 7 in the kp-prep photo spec). Recommend a 10-minute open-in-Sheets check on all 6 before the shop goes live, just to be sure.

**Etsy AI-disclosure policy (researched today):** Etsy's own policy pages block automated fetching, so this comes from search results and third-party sources citing the policy, not a direct pull of Etsy's page text. Confirmed: the listing editor's "Who made it?" field stays "I did," and Etsy expects a plain disclosure sentence in the description itself when AI played a substantial role in creating the listing's content. Etsy's stated test is about the degree of creative contribution, not the medium. There's no clean carve-out in what I could find for an AI-assisted tool versus AI-generated art. The safer read for Kingdom Planners: disclose, the same way WKD does, just with different wording since the actual thing being disclosed is different (AI helped build the tool; it didn't generate the content a customer sees as the finished art). Exact wording is in Section 6. Before the shop goes live, someone needs to open etsy.com/legal/creativity in an actual logged-in browser and confirm the literal current checkbox/field labels. Automated tools couldn't get past Etsy's bot blocking to read it directly, so the mechanism above is a step below hard-confirmed.

**Title and tag limits (confirmed current, 2026):** Etsy's title limit is still 140 characters. Tags are still exactly 13, up to 20 characters each. What changed this year: Etsy's search algorithm now rewards natural, comma-separated phrasing over titles that max out every character with stuffed keywords, so the titles below are written as readable phrases, not keyword strings. Every title and every tag set below was checked against both limits programmatically; all pass.

---

## 1. Pricing recommendation

Per the standing rule ("anchor price and sale price... never price like a simple planner"), every listing gets a higher anchor (compare-at, "was") price and a lower live sale price. Kingdom-Planners\CLAUDE.md doesn't yet have this anchor/sale structure written down anywhere, just flat numbers for the 2 already-priced products. I built anchors for those too so the whole shop is consistent, and flagged below that CLAUDE.md's price sheet should get updated to actually hold this table going forward.

| Product | Anchor ("was") | Sale price | Confidence |
|---|---|---|---|
| Complete Budget System | $26 (recommended, file missing) | **$19 (already set)** | N/A, locked by Zac already |
| Debt Freedom Planner | **$16 (new)** | **$12 (already set)** | N/A, locked by Zac already |
| PCS Moving Budget Planner | $22 | $16 | Comp-supported: real Etsy Excel-tier listings found clustering up to $20 |
| Deployment Pay Budget Planner | $23 | $17 | Thin comp data (currency-inconsistent search results), mostly built by analogy to PCS's complexity plus the SDP calculator's uniqueness |
| VA Disability Claim Tracker | $25 | $18 | Comp thin but real: category splits between roughly $10 simple notebooks and unpriced "calculator tier" spreadsheets; priced near the top given the whole-person rating calculator is a genuine differentiator nobody else in the comps has |
| Terminal Leave / ETS Transition Planner | $24 | $18 | No direct comps found, priced by complexity analogy: 7 tabs, the most feature-dense of the non-flagship products (calculator, timeline, budget bridge, benefits checklist, job tracker) |
| Road Trip Planner & Tracker | $19 | $14 | Comp-supported: best-covered category in research, multi-tool planners (route, budget, daily log, packing) comp to $10 to $15 |
| **Military Family Complete System (bundle)** | $100 (sum of the 6 military-relevant sale prices: Complete Budget System, Debt Freedom, PCS, Deployment, VA Tracker, Terminal Leave; Road Trip excluded, it's general-audience, not military-specific) | **$75** | Bundle discount convention (15% to 30% off sum-of-parts) is cited across sources but not independently verified against real bundle listings. Treat $75 as a reasonable starting recommendation, not a hard number |

Road Trip Planner is priced and packaged as a standalone, general-audience listing, not part of the military bundle, matching Kingdom-Planners\CLAUDE.md's own bundle definition ("all 6 military-relevant planners").

The bundle listing itself is blocked the same way Complete Budget System is: it can't be built or priced-and-zipped for real until that file exists.

---

## 2. Debt Freedom Planner

**TITLE** (119/140 chars):
Debt Payoff Planner Spreadsheet, Snowball and Avalanche Calculator, 36 Month Debt Free Tracker, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
debt payoff planner, debt snowball, debt avalanche, debt free tracker, payoff calculator, debt spreadsheet, budget planner, excel debt tracker, google sheets budget, debt free planner, finance spreadsheet, pay off debt fast, money management

**PRICE:** Anchor $16, sale $12 (already set by Zac)

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork.

A real month-by-month debt payoff projection, not a rough guess. Enter your debts once and this spreadsheet runs the math for you, every month, automatically.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, the color key, and a plain-language note on how the compounding math works so you know exactly what you're looking at.
- **Debt Setup**: enter each debt's name, balance, interest rate, and minimum payment. Pick Snowball (lowest balance first) or Avalanche (highest interest first) from a dropdown, and set how much extra you can put toward debt each month.
- **Payoff Schedule**: a live 36-month projection that recalculates automatically as you update Setup. As each debt hits zero, its minimum payment rolls into the next debt's extra payment automatically. That's the real snowball effect, not a list re-sorted by hand. Ends with your real payoff date and total interest paid.

Built for anyone carrying more than one debt and tired of guessing when it will actually be gone: credit cards, an auto loan, a personal loan, medical bills. Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

Dealing with a military move, a deployment, or a VA claim at the same time? Check the shop's other planners, or the Military Family Complete System bundle, which includes this planner alongside five others at a lower combined price than buying them separately.

---

## 3. PCS Moving Budget Planner

**TITLE** (117/140 chars):
PCS Moving Budget Planner Spreadsheet, DLA TLE Entitlement Calculator, Military Move Tracker, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
pcs planner, pcs binder, military move, pcs checklist, dla calculator, military spouse, ppm calculator, move budget, pcs spreadsheet, relocation binder, army pcs planner, military family, excel pcs tracker

**PRICE:** Anchor $22, sale $16

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork.

Know what the government actually owes you before you move, track what you really spend, and find out whether doing your own move (PPM) is worth it. Built by a veteran with enough PCS moves behind him to know the government does not volunteer what it owes you.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, plus the three things people leave on the table every PCS: TLE reimbursement, MALT for a second vehicle, and tolls and ferry fees.
- **Move Details**: your grade, dependents, losing and gaining duty stations, and the official DTOD distance, not your odometer, not Google Maps.
- **Entitlements**: what the government owes you, mileage, per diem, DLA, TLE, calculated from the current rates.
- **Move Budget**: what the move actually costs, side by side with your entitlements, so you can see your real gap.
- **PPM Decision**: runs the numbers on doing the move yourself against the Government Constructive Cost, so you know before you commit.
- **Weight Allowance**: your limit by rank and what going over it costs you.
- **PCS Timeline**: a 90-day checklist in order, starting from the day you report to the transportation office.
- **Rate Reference**: the 2026 MALT, TLE, and per diem figures with sources, kept separate so you can update it as rates change without touching your own data.

Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

PCSing while also dealing with debt, a deployment, or a VA claim? Check the Military Family Complete System bundle: six planners together for less than buying them one at a time.

---

## 4. Deployment Pay Budget Planner

**TITLE** (111/140 chars):
Deployment Pay Budget Planner, Military Deployment Spreadsheet, SDP Savings Calculator, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
deployment planner, military deployment, deployment budget, sdp calculator, military spouse, deploy checklist, combat pay tracker, family separation, pay estimator, home budget military, deployment savings, excel deployment, pre deployment plan

**PRICE:** Anchor $23, sale $17

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork.

What you actually earn downrange, what the tax exclusion is worth, and how the household runs while you're gone. Built by a veteran who watched a deployment's extra pay get spent instead of planned for, more than once.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, and the two things that matter most: the Savings Deposit Program's 10% guaranteed return, nothing else in finance pays that, and the Combat Zone Tax Exclusion, often the single largest number on the whole sheet.
- **Deployment Details**: your grade, years of service, pay, and dates. Everything else keys off this tab.
- **Pay Estimator**: the full stack. Hostile Fire/Imminent Danger Pay, Family Separation Allowance, Hardship Duty Pay, and what the tax exclusion is actually worth in dollars.
- **Savings Deposit Program**: models your SDP deposit up to the $10,000 cap at the guaranteed rate, including the extra interest window after you leave the zone.
- **Home Budget**: what the household costs while you're gone, compared against normal, so you can see what actually changes.
- **Savings Plan**: decide where the extra money goes before it starts arriving. Money without a job to do gets spent.
- **Pre-Deployment Checklist**: legal, financial, and household tasks in order, the ones people forget marked clearly.
- **Rate Reference**: the current 2026 special-pay rates with sources, kept separate from your own entries.

Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

Also dealing with debt, a PCS, or a VA claim? Check the Military Family Complete System bundle: six planners together for less than buying them one at a time.

---

## 5. VA Disability Claim Tracker

**TITLE** (106/140 chars):
VA Disability Claim Tracker, Combined Rating Calculator, Veteran Benefits Planner, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
va disability, va claim tracker, combined rating, veteran benefits, va rating calculator, disability tracker, veteran planner, cp exam tracker, va appeal tracker, evidence tracker, military benefits, va spreadsheet, veteran disability

**PRICE:** Anchor $25, sale $18

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified against the official VA rate tables before this file shipped. This is an original tool, not AI-generated artwork.

Track every condition, every deadline, every piece of evidence, and get a real estimate of your combined rating and monthly payment using the official 2026 VA rate tables. Built by a veteran because the claims process hands you no map and the paperwork doesn't forgive a missed deadline.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, and the one thing most people get wrong: VA ratings don't add. A 50% and a 30% isn't 80%. This file runs the real whole-person math.
- **Condition Log**: one row per claimed condition. Date first treated, date filed, claim type, status, rating, effective date, C&P exam date.
- **Combined Rating**: enter each condition's rating and this tab runs the actual VA combination math, not simple addition, and rounds it the way the VA does.
- **Payment Estimator**: pick your combined rating and dependent status, get your monthly payment figure.
- **Rate Tables**: the official 2026 VA compensation rates by dependent status, reference only, kept separate from your own data.
- **Evidence Tracker**: what you have, what's missing, what you requested and when, and where it's filed.
- **Appointments & Deadlines**: C&P exams, filing windows, appeal clocks, with days-out counted for you.
- **Appeal Tracker**: if a claim gets denied, this is where the next step lives. Lane chosen, filed date, deadline, days left.

This is the one genuine calculator in the whole shop that competitors don't have: real whole-person VA math, not a simple addition tool pretending to be one.

Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

An accredited Veterans Service Officer (VFW, DAV, American Legion, or your county VSO) will file your claim for free. You never need to pay anyone a percentage of your back pay.

Also dealing with a PCS, a deployment, or debt? Check the Military Family Complete System bundle: six planners together for less than buying them one at a time.

---

## 6. Terminal Leave / ETS Transition Planner

**TITLE** (105/140 chars):
Military Transition Planner, Terminal Leave Calculator, ETS Separation Checklist, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
military transition, terminal leave, ets checklist, separation planner, leave sell back, military retirement, transition timeline, job search tracker, veteran transition, tap checklist, budget bridge plan, military separation, excel military plan

**PRICE:** Anchor $24, sale $18

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork.

The last twelve months: what your leave is worth, what the money looks like between paychecks, and everything that has to happen before you turn in your ID card. Built by a veteran who watched people get this wrong, expensively and mostly permanently.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, and the three most expensive mistakes: selling leave back without doing the math, missing the VA claim filing window before separation, and underestimating the pay gap between your last military check and your first civilian one.
- **Separation Details**: your grade, years of service, separation type, separation date, and current pay.
- **Leave Decision**: terminal leave versus selling it back, run side by side. Terminal leave keeps your BAH and BAS. Sold leave pays base pay only and is fully taxable.
- **Transition Timeline**: a 12-month checklist working backward from your separation date, with the deadlines that actually bite.
- **Budget Bridge**: the gap between your last military paycheck and your first civilian one. Cash on hand, terminal leave payout, final military pay owed, total resources.
- **Benefits Checklist**: what to claim, convert, or lose. VA disability, VA health care, GI Bill, VA home loan, SGLI to VGLI, each with its own window.
- **Job Search Tracker**: applications, contacts, status, and follow-ups in one place.

Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

Also dealing with a VA claim, a PCS, or debt? Check the Military Family Complete System bundle: six planners together for less than buying them one at a time.

---

## 7. Road Trip Planner & Tracker

**TITLE** (102/140 chars):
Road Trip Planner Spreadsheet, Route and Budget Tracker, Fuel Cost Calculator, Excel and Google Sheets

**TAGS** (13, all 20 chars or under):
road trip planner, road trip budget, travel itinerary, road trip tracker, fuel cost tracker, packing checklist, vacation planner, route planner, trip budget sheet, road trip printable, family road trip, travel spreadsheet, digital trip planner

**PRICE:** Anchor $19, sale $14

**DESCRIPTION:**

AI disclosure: this planner was built with AI assistance, used to help draft formulas and structure. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork.

Plan the route, know the real cost before you leave, and track what you actually spend along the way.

**What's inside, tab by tab:**
- **Start Here**: how to use the workbook, and a real note on fuel estimates. Highway MPG drops with a loaded car, a roof box, a trailer, mountains, headwind, and air conditioning, so use a real-world figure and add a contingency.
- **Trip Setup**: trip name, dates, number of travelers, vehicle, and your real-world highway MPG.
- **Route Planner**: one row per leg, with miles, drive time, and fuel cost that calculates automatically from your Trip Setup numbers.
- **Budget**: estimated versus actual by category. Fuel, lodging, food, attractions, and more, with the difference calculated for you.
- **Daily Log**: where you stayed, what you spent, and what you want to remember, day by day.
- **Packing List**: organized by category with a checkbox for each item.
- **Vehicle Prep**: the pre-trip checklist to run two weeks out, not the night before. Oil, tires, brakes, coolant, and more.

Works in Excel and Google Sheets.

Instant digital download. No physical item ships. You'll get the file immediately after purchase, ready to open and fill in.

Planning a move and a road trip at the same time? Pair this with the PCS Moving Budget Planner, sold separately in this shop.

---

## 8. Military Family Complete System (bundle): BLOCKED, prep only

This listing can't actually be built yet. It's defined as 6 files (Complete Budget System, Debt Freedom Planner, PCS, Deployment, VA Tracker, Terminal Leave) zipped into one download, and Complete Budget System doesn't exist on disk. Copy and pricing below are ready so this is paste-and-go the moment that file is recovered.

**TITLE** (106/140 chars):
Military Family Complete Planner Bundle, Budget Debt PCS Deployment VA Terminal Leave, Excel Google Sheets

**TAGS** (13, all 20 chars or under):
military bundle, veteran planner set, military family kit, budget bundle, pcs deployment va, military planners, veteran bundle, complete system, military finance kit, spouse planner set, planner bundle, excel bundle set, military life kit

**PRICE:** Anchor $100 (sum of the 6 individual sale prices), sale $75. See Section 1 for the confidence note on the discount percentage.

**DESCRIPTION (draft, needs Complete Budget System's real tab list dropped in before publishing):**

AI disclosure: these planners were built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before these files shipped. These are original tools, not AI-generated artwork.

Everything a military family needs to run the money side of service in one bundle, at a lower combined price than buying each planner separately: the Complete Budget System, Debt Freedom Planner, PCS Moving Budget Planner, Deployment Pay Budget Planner, VA Disability Claim Tracker, and Terminal Leave/ETS Transition Planner. Six working spreadsheets, not printables. Every one calculates in real time.

[INSERT: one enumerated line per included planner's tab list here once Complete Budget System's tabs are confirmed]

Works in Excel and Google Sheets. Instant digital download, delivered as one zip file immediately after purchase. No physical item ships.

---

## 9. About section (shop-wide)

Kingdom Planners builds financial planning tools for people navigating real, complicated money situations: military pay and benefits, debt payoff, a deployment, a cross-country move. Every planner here is a working spreadsheet, not a static printable. Formulas calculate. Numbers update automatically.

These tools started with one veteran's own paperwork, 21 years in the Army's worth of it. A move that came with entitlements nobody explained up front. A VA claim that took longer than it should have. A deployment where the extra pay showed up with no plan for where it would go. Every planner in this shop exists because a real gap showed up first.

Built with AI assistance for research, formula logic, and drafting, then tested and finalized by hand. Every calculation is checked against real numbers, and where they exist, official rate tables, before it ships.

Works in Excel and Google Sheets. Instant digital download. Nothing physical ever ships.

---

## 10. Shop policies (draft)

**What you're buying:** every listing in this shop is a digital download only. No physical item ships, ever.

**Format:** Excel (.xlsx), built to also work in Google Sheets.

**Delivery:** instant and automatic through Etsy right after purchase. Download your files from Etsy's Purchases page any time.

**Refunds:** digital files can't be returned once downloaded, so sales are final. If a formula is broken or a file won't open, message the shop through Etsy Messages and it gets fixed or replaced, no argument.

**Use:** for personal, single-household use. Not licensed for resale or redistribution of the file itself.

**Support:** questions about how a tab or formula works go through Etsy Messages. Real answers, not a bot.

**Not official guidance:** every planner says this inside the file too, but it's worth saying here as well. These are planning and organization tools, not legal, tax, or financial advice, and not a product of the VA or DoD. Your orders, your finance office, and the VA in writing are the actual authority on what you're owed.

---

## 11. AI disclosure language (locked for this shop, distinct from WarriorKingDesigns)

WKD's disclosure covers AI-generated art. The image itself is the AI output. Kingdom Planners is different: the product is an original financial tool (structure, formulas, calculators, content), and AI was used as a drafting and research aid to help build it, the same way a person might use a calculator or a template library. Etsy's policy doesn't carve out that distinction explicitly, so the safe move is to disclose plainly rather than assume an exemption.

**Sentence to use in every KP listing description** (already placed at the top of each pack above):
"This planner was built with AI assistance, used to help draft formulas, structure, and reference content. Every calculation was hand-tested and verified before this file shipped. This is an original tool, not AI-generated artwork."

**Handoff checklist reminder for Zac at publish time:**
- [ ] In "How it's made," confirm "Who made it?" is set to "I did."
- [ ] Add the disclosure sentence above at or near the top of the listing description (already done in every pack in this document).
- [ ] Fill in whatever field Etsy currently presents for "did you use AI?" The exact current checkbox/field label couldn't be independently confirmed today because Etsy blocks automated page reads. Check the actual field live in the listing editor and answer honestly. Don't rely on this document for the literal button text.

---

## 12. Photo / mockup plan: what's ready, what's blocked

Per the kp-prep skill (`D:\WKP\.claude\skills\kp-prep\SKILL.md`), every KP listing ships 8 images. Status per card, shop-wide:

- **Card 1, title card.** Copy is ready (each product's real name, pulled from the file itself, is above). The card itself is an Adobe Express template Zac already built. I don't have Adobe Express or an image-generation tool in this session, so I can't produce the actual PNG. Swapping the headline per product in the existing template is a 2-minute job once the shop is being built.
- **Cards 2, 3, 4, 5, real screenshots.** Blocked, and correctly so per the skill's own rule: these have to be actual screenshots of the working file opened in Excel or Sheets, not staged. This is Zac's action once he's back, not something I can fake.
- **Card 6, contents graphic (enumerate every tab).** This is the one the skill flags as the actual conversion driver, and it's the same tab-by-tab list already written into every description above, pulled directly from the real files, not guessed. Ready to hand to Adobe Express or the graphic-design department the moment someone builds the image.
- **Card 7, "works in Excel and Google Sheets."** Already an existing permanent shop asset per the skill, done once, reused everywhere. No new work needed, though see the Section 0 flag on the compatibility pass not having been formally run yet.
- **Card 8, veteran credential card.** Also an existing permanent shop asset. No new work needed.

Bottom line: 4 of 8 cards per listing (2, 3, 4, 5) need Zac's hands-on screenshotting once the shop exists and each file is open. Cards 1 and 6 have all their real content ready now and just need the image itself built (Adobe Express, or hand this section to the graphic-design department if Zac wants that routed there). Cards 7 and 8 need nothing further.

---

## 13. What's ready to paste-and-go vs. what's still missing

**Ready now, paste-and-go the moment the shop exists:**
- Full title, 13 tags, and description for all 6 confirmed products (Debt Freedom, PCS, Deployment, VA Tracker, Terminal Leave, Road Trip).
- Pricing (anchor and sale) for all 6, plus the bundle concept, with confidence levels flagged.
- About section and shop policy copy.
- AI disclosure sentence and publish-time checklist, distinct from WKD's.
- Card 1 and Card 6 content for all 6 products (just needs the image built).

**Still missing or blocked:**
- Complete Budget System file itself is gone. Needs Zac to re-pull it from the original web chat, if that chat or session is still accessible, or rebuild it. Nothing else about this product can move until the file exists: not the listing pack, not the bundle, not its photo cards.
- Military Family Complete System bundle is fully drafted (title, tags, price, partial description) but can't actually be assembled or listed until Complete Budget System exists, since it's one of the 6 files being zipped together.
- Cards 2 through 5 (real screenshots) for all 6 confirmed products need Zac to open each file and capture them by hand. Not something I can produce.
- Cards 1 and 6 images need to actually be built in Adobe Express, or handed to graphic-design. Content is ready, the image files aren't.
- Google Sheets compatibility hasn't had a real open-and-test pass yet, just a formula-safety scan. Recommend 10 minutes checking all 6 files in actual Google Sheets before launch.
- Etsy's literal current AI-disclosure field and checkbox wording couldn't be confirmed by automated tools, since Etsy blocks bot access to its own policy pages. Someone needs to eyeball the real listing editor and etsy.com/legal/creativity in a logged-in browser before publishing.

This is a draft for Zac's review. Give it a real read before anything goes live, especially the pricing confidence levels and the AI disclosure wording.
