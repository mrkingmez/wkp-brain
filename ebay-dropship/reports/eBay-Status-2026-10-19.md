# eBay and WKP Commerce: Status, Steps and Notes (2026-10-19)

Saved before a computer restart so nothing from today's eBay talk is lost. "WKP Commerce" is the working name of the eBay dropship company. Everything below is from today's session and the venture files.

## Read this first
1. **The eBay keys on the home desktop say SANDBOX.** `EBAY_ENV` is set to SANDBOX. The sign-in you did at developer.ebay.com was the Production page. Sandbox and Production use different Client IDs and secrets. Before the token script can work for real, the Production Client ID and secret have to be in the environment variables and `EBAY_ENV` has to say PRODUCTION. You type those yourself, never paste them in chat.
2. **The refresh token is not set yet.** `EBAY_REFRESH_TOKEN` is "not set" as of tonight. Client ID and secret are set.
3. **Do the token step on the home desktop, not the work laptop.** The authorization code expires in about 5 minutes.
4. **No spend has been approved.** The Doba trial and anything else that costs money waits for your yes.
5. **The product list is a guess until real data arrives.** All costs are assumed.
6. **Nothing is listed or bought.** Phase 0, nothing live.

## Where things stand
**Done**
- Scaffold built 2026-10-10 (agents, skills, data, tools, tests). Pricing tests pass.
- Ranked shortlist of five product types (assumed costs): `D:\WKP Reports\eBay Margin Picks\2026-10-19 - eBay Margin Picks.docx`.
- Privacy policy text written: `D:\WKP\ebay-dropship\reports\privacy-policy-text.md` and `D:\WKP Reports\eBay Privacy Policy\2026-10-19 - eBay Privacy Policy.docx`. You pasted it into a Google Doc and set it to "Anyone with the link, Viewer."
- eBay Developer redirect form filled in at developer.ebay.com, User Tokens, Production: display title "WKP Commerce," privacy policy URL, accepted URL and declined URL all pointing at that Google Doc.
- Token swap script written: `D:\WKP\ebay-dropship\tools\get_refresh_token.py`. It reads the keys from the environment, asks for your RuName and the address eBay sends you to, and saves the refresh token as a user environment variable without printing it.
- Calendar reminder set for today 6:30 PM (popups at 6:20 and 6:30). TASKS.md row added.

**Not done**
- The refresh token.
- Confirm the form was saved and the RuName is listed (you were at the work laptop when you filled it in).
- Confirm which scopes were ticked: sell.inventory, sell.fulfillment, sell.account (see below).
- Doba trial yes or no.
- Terapeak or Seller Hub sold numbers (or tell me you have no seller account yet).
- Real product list.

## Get the refresh token (home desktop)
1. Fix the keys first (see "Read this first" item 1). In Windows environment variables set `EBAY_ENV` to `PRODUCTION`, and `EBAY_CLIENT_ID` and `EBAY_CLIENT_SECRET` to the Production values from developer.ebay.com, Application Keys, Production column. Open a new terminal afterward.
2. developer.ebay.com, then Application Keys, then User Tokens (Production). Confirm the WKP Commerce RuName is listed. If it is not, redo the form and click Save.
3. Make sure the scopes **sell.inventory**, **sell.fulfillment** and **sell.account** are ticked. The refresh token only works for the scopes picked here.
4. Click the OAuth sign-in link for the RuName (not the older "Auth'n'auth" link). Log in as the seller account and click **Agree and Continue**.
5. You land on your Google Doc. Copy the whole address from the address bar. It has a long `code=...` in it.
6. Right away, open PowerShell and run:
   `& "C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe" -I "D:\WKP\ebay-dropship\tools\get_refresh_token.py"`
7. It prints the environment first. If it says SANDBOX, stop. Fix the keys.
8. Paste your RuName at the first prompt. Paste the address at the second (hidden, press Enter).
9. Success says "Saved EBAY_REFRESH_TOKEN." It lasts about 18 months, then repeat this.
10. Close PowerShell, open a new one, tell Claude. Claude checks the variable is set and tests it against the seller account.

Never paste the code, the address, the secret or the token into chat. Delete any notes with the code from the work laptop.

## What the eBay keys do and do not do
- **Client ID and secret only (app-level):** search live eBay listings (Browse API), see asking prices, how many sellers, shipping costs. No access to your account.
- **With the refresh token (user-level):** your listings, orders, inventory and fulfillment. Needed to create or manage listings.
- **Not available through the API either way:** sold counts. Browse shows active listings only. Terapeak numbers have to come from you (Seller Hub, Research tab).

## Money and approvals needed from you
- **Doba trial:** about $0.99 per earlier research, not re-checked today. Check the price on their sign-up page. You make the account and enter the card yourself. Claude cannot do that. Once logged in, Claude can filter to US-warehouse items and pull real wholesale prices with you watching.
- **No spend** without an approved line in `D:\WKP\ebay-dropship\decisions-queue.md`. Say "yes" in chat and Claude logs it.
- **Terapeak or Seller Hub:** Seller Hub, Research tab, free with a seller account. Your seller account setup is still marked "Not Started" on the setup list. If there is no seller account, Terapeak will not open. Fallback: Doba prices plus eBay's public "Sold items" search.

## Product shortlist (all costs assumed, nothing verified)
Rules used: eBay fee 13.6 percent plus 0.40 per order over 10 dollars, 10 percent supplier tax buffer, 20 percent margin floor, 5 dollar minimum profit. Wholesale cost plus shipping must be about 50 to 55 percent of the selling price or less.
1. Hand tool and drill-bit sets, unbranded: sold 60 to 90, net about 13 to 19.
2. Drawer, closet and kitchen organizer sets: sold 30 to 55, net about 6 to 10. Best demand.
3. Universal car-care and trunk organizers: sold 30 to 50, net about 6 to 9.
4. Unbranded craft and art supply sets: sold 30 to 45, net about 6 to 8.
5. Pet beds, grooming tools, toys (non-consumable): sold 30 to 50, net about 6 to 10.
Volume and sell-through numbers came from a third-party 30-day snapshot (ZIK Analytics). Treat as relative ranking only.

## Locked venture rules (no agent overrides these)
1. Wholesale suppliers only. Never buy from another retailer or marketplace and ship it to the buyer.
2. US warehouses only, shipped with real tracking from a US carrier.
3. Blind shipping, no supplier invoice or retail branding in the box.
4. Zac approves every listing publish, every supplier purchase, every refund, and every price change over 10 percent until graduation.
5. No spend without an approved line in `decisions-queue.md`.
6. Phase 1 caps: 5 new listings per day, 20 per week, or eBay's own limit if lower.
7. Never list below 20 percent net margin or 5 dollars net profit per unit, whichever is higher.
8. Kill switch: policy warning, listing removal, late shipping trend, 2 or more item-not-received cases in 30 days, a supplier shipping from outside the US, or a failed API login for over 24 hours pauses all listings and alerts Zac.
9. Credentials live only in Windows environment variables. Never in files, chat, logs or memory. No card numbers anywhere.
10. No unattended browser bots on eBay. API first. Browser path only with Zac present and Zac clicking publish.
11. Do not use the word "eBay" in any store name or user ID.

## Company decisions already made (2026-10-09)
- Name: placeholder WKP Commerce, not confirmed (EBAY-002).
- Cash model: no float. Supplier orders paid per order on Zac's own card, entered by Zac at checkout.
- Entity: none yet. Sole proprietor under Zac's name. Suppliers charge sales tax, so pricing carries the 10 percent buffer. Suppliers that need an EIN or resale certificate are marked PENDING_ENTITY, not rejected.
- Defaults: 20 percent margin floor, 5 dollar minimum profit, 5 per day and 20 per week, gated until 25 clean orders.
- Category: still open (EBAY-001). No product search or listing until Zac picks.

## How the company is organized
Zac approves. `ebay-director` runs the loop. Under it: `ebay-researcher` (cloud scheduled task, 6 AM, 12 PM and 7 PM ET), `ebay-scout` (finds winners), `ebay-supplier-vet` (verifies US wholesale suppliers), `ebay-lister` (prices and builds listings), `ebay-fulfillment` (orders, tracking, stock and price sync).
Phases: 0 scaffold and sandbox (now), 1 gated live (goal: 25 clean orders), 2 partial autopilot (after 25 orders with zero policy notices), 3 full autopilot candidate (after 90 days, supplier with API ordering).

## Still-open items checklist
- [ ] Production keys in the environment, `EBAY_ENV` set to PRODUCTION
- [ ] RuName saved and scopes confirmed
- [ ] Refresh token saved
- [ ] Yes or no on the Doba trial
- [ ] Seller account exists? Terapeak numbers
- [ ] Pick the category (EBAY-001) and confirm the name (EBAY-002)
- [ ] Zac's setup checklist: seller account, business policies, dedicated card, notifications, GitHub connected (`EBAY-DROPSHIP-BUILD.md` section 7)
- [ ] Populate `data\fee-table.md` from eBay's current fee page (pricing.py will not run until it is filled and dated)
- [ ] Verify eBay API endpoint paths and scopes in `ebay_api.py` against the developer docs

## After the restart
- Environment variables stay. Nothing else needs to be running.
- This Claude session ends. Anything I scheduled inside the session is gone, but the Google Calendar reminder stays.
- Start a new session in `D:\WKP`, say "pick up the eBay token step," and I will read this file, `TASKS.md` and the ebay-dropship folder.

## Where everything is
- This file: `D:\WKP\ebay-dropship\reports\eBay-Status-2026-10-19.md` (Word copy in `D:\WKP Reports\eBay Status\`)
- Venture rules and decisions: `D:\WKP\ebay-dropship\CLAUDE.md`, `decisions-queue.md`
- Token script: `D:\WKP\ebay-dropship\tools\get_refresh_token.py`
- Margin picks: `D:\WKP\ebay-dropship\reports\best-margin-picks-2026-10-19.md`
- Category scan: `D:\WKP\ebay-dropship\reports\category-scan.md`
- Env variables guide: `D:\WKP\ebay-dropship\reports\eBay-Env-Variables-Guide.md`
- Privacy policy text: `D:\WKP\ebay-dropship\reports\privacy-policy-text.md`
- Full spec: `D:\WKP\EBAY-DROPSHIP-BUILD.md`
