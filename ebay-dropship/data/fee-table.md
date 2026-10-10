# eBay fee table

Populate from eBay's current seller fee page for each category before the first pricing run. Record the date checked. Refresh monthly. The pricing script refuses to run if this file is older than 35 days.

Last checked: NEVER

## Rates
fvf_rate is a decimal (0.1325 means 13.25 percent). One row per category.

| category | fvf_rate | per_order_fixed_fee |
|---|---|---|
