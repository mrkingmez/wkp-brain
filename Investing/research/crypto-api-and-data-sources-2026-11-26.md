# Crypto API and free data sources, 2026-11-26

Owner: trading-researcher, for trading-director. Retrieval date for every fact below: 2026-11-26 unless stated. No keys, accounts or orders were touched. Not financial advice.

## BLUF
1. Robinhood has an official Crypto Trading API for US Robinhood Crypto customers. It uses Ed25519 signing, 100 requests per minute (300 burst) per account, and has NO sandbox or paper mode in the docs. The paper side must be our own simulated ledger on live quotes.
2. Even market data from Robinhood needs signed, authenticated requests (and therefore a key Zac makes). For keyless data use Coinbase Exchange, Kraken or Binance.US public endpoints.
3. At a $60 account, Robinhood's standard fee tier is 0.95 percent per executed order on the exchange-routed tier (0.50 percent reduced). A round trip costs about 1.9 percent before spread. That is a heavy hurdle for any short-hold strategy. Fee amount for market-maker routing is NOT in the schedule (it says "No commissions", spread is the cost, spread size NOT RETRIEVED).
4. Alpaca free plan: IEX only, 200 calls per minute, 30 websocket symbols. Fine for a scanner of a few dozen names.

## Part 1: Robinhood Crypto Trading API

| Item | Finding | Source (URL) |
|---|---|---|
| Who may use it | "Available to customers in the United States only." Only active Robinhood Crypto accounts can create keys. | docs intro, https://docs.robinhood.com/crypto/trading/ (page is JavaScript-rendered; I read the OpenAPI text embedded in its page script chunk). Also https://robinhood.com/us/en/support/articles/crypto-api and https://robinhood.com/us/en/newsroom/robinhood-crypto-trading-api/ |
| Key creation | Zac creates credentials himself in crypto account settings on web classic (desktop browser), choosing which actions the key may do. He generates an Ed25519 key pair, uploads the PUBLIC key, receives an API key. Private key never goes to Robinhood. Credentials can be modified, disabled or deleted any time. Agents never see or ask for the keys. | docs intro "Creating an API key"; support article; newsroom |
| Auth scheme | Three headers on every authenticated request: x-api-key, x-signature, x-timestamp. Signature is Ed25519 over the string api_key + timestamp + path + method + body, base64 encoded. Timestamp in seconds, valid 30 seconds. | docs Authentication section and sample code |
| Rate limits | 100 requests per minute per account, 300 per minute in bursts. Token bucket, per endpoint, "actual values fluctuate" with service load. | docs "Rate Limiting" section |
| Versions | v1: orders without fee tiers. v2: orders with fee tiers (counts toward 30-day volume). Read-only actions on both. No v1 deprecation date. | support article |
| Endpoints | Accounts, trading_pairs, holdings, orders (place, get, cancel), best_bid_ask, estimated_price. | docs OpenAPI paths |
| Supported trading pairs | NOT RETRIEVED. The list comes from the authenticated trading_pairs endpoint. Docs only show BTC-USD and ETH-USD as examples. | docs |
| Market data and auth | Quotes (best_bid_ask, estimated_price) are listed with the same security block as every other endpoint: key, signature and timestamp. So quotes need authentication. No public quote endpoint found in the docs. | docs OpenAPI paths |
| Fees | Fee schedule dated 20261102 (PDF): "No commissions" on buying and selling. Exchange routing tiers by trailing 30-day volume: $0 to $10K = 0.95 percent standard, 0.50 percent reduced. Next tier $10K to $50K = 0.75 and 0.35. Limit orders always use exchange routing. Market maker routing (default for market orders): rebates go to Robinhood, no fee line, so cost is in the spread. | https://cdn.robinhood.com/assets/robinhood/legal/rhc-fee-schedule.pdf ; https://robinhood.com/us/en/support/articles/crypto-fee-tiers/ |
| API fee wrinkle | Support page says v2 orders are charged the standard rate until the reduced/standard rollout completes. Market and stop orders always pay standard. | https://robinhood.com/us/en/support/articles/crypto-fee-tiers/ |
| Spread | NOT RETRIEVED. Robinhood publishes no spread figure. Support page says only pricing "may vary across routing settings." Measure it ourselves by logging best_bid_ask on paper. | fee tiers article |
| Automated trading allowed? | Yes for the account holder's own use: newsroom says users can "run automated or algorithmic strategies." Use is subject to the Crypto Customer Agreement (revised Nov 3, 2026). Section 20 covers third-party API Licensees and says Robinhood may terminate the account or disable API/MCP access "for any reason, including excessive market data usage," and that API connectivity "is not guaranteed." Section 20 is written about third-party licensees; whether Zac running his own script is "API Licensee" use is not spelled out, so the newsroom and docs are the basis, and an attorney reading is NOT RETRIEVED. | newsroom URL above; https://cdn.robinhood.com/assets/robinhood/legal/Robinhood%20Crypto%20Customer%20Agreement.pdf |
| Paper or sandbox | NONE found. The docs, support article and newsroom mention no sandbox, test or paper environment. Treat as none. The paper side is our own simulated ledger fed by live quotes (needs one authenticated read-only key, or use a keyless exchange feed as a proxy and note that it is not Robinhood's price). | all three Robinhood pages |
| State availability | The API is "United States" only. Per-state list NOT RETRIEVED. Agreement says restricted-coin rules apply by state residency (current plus past 45 days), and Robinhood Crypto, LLC is licensed in New York. Zac's state is Georgia, but a Georgia confirmation is NOT RETRIEVED. Zac already trades Robinhood Crypto-eligible account status himself, so he can see in-app whether crypto is enabled. | agreement PDF section on restricted cryptocurrencies |
| Protection | Not FDIC insured or SIPC protected. | support article |

Implication for the plan: a read-only key (quotes and holdings only, no trade permission) is the safest first step if Zac wants Robinhood prices in paper tests. Key permissions are chosen at creation, per the support article. Zac's call.

## Part 2: Free data sources

### Stocks
| Source | Limits | Source URL |
|---|---|---|
| Alpaca Basic (free) | Real-time feed IEX only. Historical calls 200 per minute. Websocket 30 symbols. History since 2016. Latest 15 minutes of historical data withheld. Paid Algo Trader Plus is $99 per month (option only). | https://docs.alpaca.markets/docs/about-market-data-api |
| Alpaca screener endpoints | NOT RETRIEVED (docs URL 404). | n/a |
| Finviz free | Quotes delayed 1 minute (NASDAQ, NYSE, AMEX). Terms on automated scraping NOT READ, so do not automate. Elite is $39.50 per month or $299.50 per year regular (option only). | https://finviz.com/elite.ashx |

### Crypto
| Source | Auth | Limits and notes | Source URL |
|---|---|---|---|
| Coinbase Exchange public candles | None | GET /products/{id}/candles, granularity 60, 300, 900, 3600, 21600, 86400 seconds, 300 candles max per call, not for frequent polling. Public limit 10 requests per second per IP, burst 15. Whether public data needs no auth is stated for the candles endpoint (security overridden to none). | https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles ; https://docs.cdp.coinbase.com/exchange/rest-api/rate-limits |
| Kraken public OHLC | None | GET https://api.kraken.com/0/public/OHLC, intervals 1 to 21600 minutes, most recent 720 candles only. Public endpoint rate limit NOT RETRIEVED; documented REST counters are per API key (Starter max 15, decay 0.33 per second). | https://docs.kraken.com/api/docs/rest-api/get-ohlc-data ; https://docs.kraken.com/api/docs/guides/spot-rest-ratelimits |
| Binance.US public market data | None for klines | klines weight 1, max 1,000 bars per call, 6,000 weight per minute per IP, 429 then IP ban if ignored. Docs advise websockets over polling. Only the first 100K of 327K characters read. US state limits for Binance.US NOT RETRIEVED. | https://docs.binance.us/ |
| CoinGecko Demo (free) | Key needed (free) | 100 calls per minute, 10,000 per month, daily and hourly history 1 year, attribution required. Paid Basic $35 monthly, Analyst $129, Lite $499, Pro $999 (options only; Black Friday discount noted on page, temporary). Terms page itself not read. | https://www.coingecko.com/en/api/pricing |

### Paid scanners (options only, nothing signed up or bought)
| Product | Price | Source |
|---|---|---|
| TradingView Essential | $12.95 per month billed annually (special price on page; monthly rate not stated, page implies about $14.95) | https://www.tradingview.com/pricing/ |
| TradingView Plus | $29.95 per month billed annually | same |
| TradingView Premium | $59.95 per month billed annually | same |
| TradingView Ultimate | $199.95 per month billed annually | same |
| Trade Ideas Standard | $127 per month, or $1,068 per year | https://www.trade-ideas.com/pricing/ |
| Trade Ideas Premium | $254 per month, or $2,136 per year | same |
| Finviz Elite | see above | see above |

Any of these costs more per month than a meaningful share of a $60 account. None is justified at this size.

## Fit at $60 (arithmetic from retrieved numbers)
- $60 account at 0.95 percent standard fee: about $0.57 per fill, about $1.14 round trip, 1.9 percent of the position. A position needs to move more than that plus spread to win. Limit orders may get the 0.50 percent reduced fee only if they rest and fill as maker; then round trip is about 1.0 percent.
- No PDT rule applies to crypto (PDT is a stock margin rule, per `Investing\CLAUDE.md` context). A rule citation for crypto is NOT RETRIEVED here.
- 100 requests per minute is ample for polling a handful of pairs.

## Could not verify
Robinhood supported pair list, spread data, per-state API availability including Georgia, attorney reading of Agreement section 20 for self-built scripts, Alpaca screener endpoints, Alpaca and CoinGecko terms of service text, Kraken public rate limits, Binance.US state availability, Finviz automation terms, TradingView monthly price.

## Method note
docs.robinhood.com renders in JavaScript, so a normal page read returned only the word "Robinhood". I downloaded the page's own public script chunk with plain curl (no spoofing) and read the OpenAPI text embedded in it. PDFs fetched from Robinhood's own CDN.

## What trading-director could test on paper
1. Own simulated ledger with the Robinhood fee schedule baked in (0.95 percent standard, 0.50 percent reduced) and a spread assumption measured later, running on Coinbase or Kraken public candles. Label results "proxy prices, not Robinhood quotes."
2. If Zac chooses, one read-only Robinhood key to log best_bid_ask for a week and measure the real spread. Zac makes it; no one else handles it.
3. Hand the endpoint limits to data-sourcing via trading-director for the plumbing. Read each provider's terms before automating.
