# eBay fee table

Populate from eBay's current seller fee page for each category before the first pricing run. Record the date checked. Refresh monthly. The pricing script refuses to run if this file is older than 35 days.

Last checked: 2026-10-10
Source: https://www.ebay.com/help/selling/fees-credits-invoices/selling-fees?id=4822 (fetched 2026-10-10 by ebay-researcher; page states no effective date for these rates). Non-store seller rates. Store-subscriber discounts not applied.
Note: eBay page also announces the seller currency conversion charge rises from 3 percent to 3.25 percent on 2026-10-14 for US-registered sellers. Not relevant to USD sales. Insertion fee after 250 free listings per month is reported at 0.35 dollars per listing by a third party (SaleHoo), unverified against eBay.

## Rates
Use category "default" for most categories (Home & Garden, Toys & Hobbies, Pet, eBay Motors Parts & Accessories, Business & Industrial, Health & Beauty, Clothing).
fvf_rate is a decimal (0.1325 means 13.25 percent). One row per category. Rates shown are for the portion up to 7,500 dollars (up to 2,000 for handbags, 5,000 for jewelry). per_order_fixed_fee is 0.30 on orders of 10 dollars or less and 0.40 on orders over 10 dollars; the table uses 0.40 (our price band is above 10 dollars).

| category | fvf_rate | per_order_fixed_fee |
|---|---|---|
| default | 0.136 | 0.40 |
| Books & Magazines, Movies & TV, Music | 0.153 | 0.40 |
| Coins & Paper Money (non-bullion), Trading Cards, Comics | 0.1325 | 0.40 |
| Jewelry & Watches (non-watch-parts) | 0.15 | 0.40 |
| Women's Bags & Handbags | 0.15 | 0.40 |
