# WKT Trading: Locked Rules (set 2026-10-19)

## Phase plan
1. Watch week: record data, paper-trade, self-grade. No real orders. Going a month without a trade is fine.
2. Bitcoin sentinel for the BTC interest/hold account: buy zone, caution, and danger texts.
3. Live crypto on the Robinhood Crypto Trading API (Ed25519 key, existing account).
4. Stocks on Alpaca once it's open and funded: Rule One quality filter and vertical spreads.

## Risk
- Score under 70 = no trade. Risk 0.5 percent at 70-79, 1 percent at 80-89, 2 percent at 90+.
- Max position 25 percent of the account. Stop at 2 times ATR on 1-hour bars. Target 2.5R.
- Time stop: 3 days for crypto, 5 days for stocks.
- Daily kill switch at -5 percent: no new trades, text Zac. Open positions keep their own stops.
- Monday is a watch day: only trade if the score is 90 or higher.
- Max 4 open positions.

## Operation
- Weekdays 9:30 AM to 5:00 PM ET: 1-minute checks. After 5 PM and weekends: crypto every 15 minutes.
- Twilio YES/NO approval with auto-execute if no reply (for the live phase).
- Hosting: Zac's home machines, not Render.
- Crypto universe is not limited; it scans the whole list and filters by volume.
- Data: Coinbase public candles for crypto, yfinance for stocks.
