@../ME.md
@../projects.md

# Investing Challenge ($50 → $60+)

## What This Is
Real money, personal challenge, lowest priority venture. Started with $50 in Robinhood in April 2026. Currently ~$60, fully in cash as of 7/24. PDT rule applies (no $25k+ balance), so limited to swing trades (holding days, not day trades) rather than intraday trading.

## Trade History
- **4/30/26** — bought UAMY, 5 shares, $55.56 avg cost basis / total account value at buy; sold at $59.75 — realized gain, brought account to ~$59.
- **5/13/26** — bought PINS, went all-in with account balance; sold for a $19 profit — brought account to current ~$60.
- Currently 100% cash, no open positions, actively looking for the next swing trade.

## Strategy
Swing trading — hold positions for a few days, not intraday. Zac is still learning candlestick pattern reading and is not yet confident reading charts manually. Wants both reversal setups (oversold stocks likely to bounce) and momentum/breakout setups (stocks breaking upward), not just one style.

## Broker Setup — Decision Locked 7/24
Staying on **Robinhood** for actual trade execution (zero-commission, already set up). Building a separate scanner using **Alpaca**'s free market data API (not for execution) to identify swing trade candidates and alert Zac — he then manually executes on Robinhood.

Reasoning: Robinhood doesn't support programmatic/automated order placement for retail accounts, so a scanner-only integration keeps things simple without switching brokers prematurely.

**Future automation path**: once the account crosses $25k (unlocks full PDT flexibility), move to Alpaca (or similar broker with a trading API) and flip on automated execution, including the "emergency button" concept Zac wants — a manual override that places a trade for him when he can't get to the app in time.

TradeStation was considered and set aside for now — good professional platform with real automation support, but higher account minimums (~$2k+) and more complexity than needed for a $60 account. Revisit once the account has grown.

## Scanner Tool — Spec (to be built)
- Data source: Alpaca free market data API.
- Looking for candidates in two categories simultaneously: (1) oversold/reversal setups, (2) momentum/breakout setups.
- Output: alerts Zac can act on manually via Robinhood.
- Longer-term: once $25k threshold is hit and broker moves to Alpaca, add an execute-directly "emergency button" feature.
- Zac wants Claude to write the code; he'll run it and they'll troubleshoot together iteratively rather than Zac speccing exact indicators up front.

## Philosophy
Long-term goal beyond this challenge: options trading (verticals) once capital allows. General approach favors Rule One-style investing philosophy (buy good companies when they're undervalued, hold long-term) for the eventual larger-capital phase — the current $50-$60 swing-trade challenge is separate from that longer-term approach.

## Open
[FILL IN — Alpaca account setup status]
[FILL IN — first version of scanner code, once built]
[FILL IN — specific technical indicators/thresholds for "oversold" and "breakout" once defined]
[FILL IN — position sizing / risk rules]

