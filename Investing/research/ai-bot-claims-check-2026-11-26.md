# AI / Grok trading bot claims: evidence check
Date: 2026-11-26. Author: trading-researcher. To: trading-director. Not advice, not a promise of returns.
All sources retrieved 2026-11-26 through web search and page fetch. "Retrieved" means I read it this session; "secondary" means a news report of someone else's data.

## BLUF
1. No audited or broker-verified track record of an AI bot turning a tiny account into thousands in months was found. The "$52 to $4,392 on Solana memecoins" type of claim has no retrievable verification.
2. Where regulators have looked, the "AI bot" was often not real. The SEC alleges the Privvy case bots had no AI and only about 3% of $12.3M raised bought crypto.
3. The best public test is Alpha Arena (nof1): Season 1 had 4 of 6 LLMs lose heavily, 2 won, over about 2 weeks. Grok lost 57.9% in Season 1 (secondary report). Grok 4.20 gained about 12% in Season 1.5 (secondary, conflicting figures). Two weeks is noise, not a track record.
4. Independent research says LLM trading results shrink or vanish after costs, longer periods and bias controls.
5. PDT: FINRA replaced the day trader rule effective 2026-06-04 (firm phase-in allowed to 2027-10-20). The $25k minimum is gone as a FINRA requirement. Your broker's own rules still decide what you can do.
6. Robinhood stop orders on fractional shares: NOT CONFIRMED. Official stop-loss article says whole shares only.

## 1. Regulator warnings (retrieved)
| Source | What it says | URL |
|---|---|---|
| CFTC customer advisory "AI Won't Turn Trading Bots into Money Machines" (page has no date; press release 8854-24 is January 2024, per search listing) | AI cannot predict the future or sudden market changes. Scammers cite returns "sometimes tens of thousands of percent". Cites Mirror Trading International: over $1.7B in bitcoin from at least 23,000 people. Tells readers to weigh fees, spreads and subscription costs and be wary of influencers. | https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/AITradingBots.html |
| SEC OIEA with NASAA and FINRA joint investor alert on AI and investment fraud | Search summary only: guaranteed high returns with little risk are classic fraud signs; check registration on Investor.gov. The page itself returned HTTP 403 to me, so wording NOT VERIFIED first-hand. | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-ai-and-investment-fraud-investor-alert |
| SEC v. Nathan Fuller / Privvy Investments, filed about 2026-05-28 (The Block, secondary) | About $12.3M from about 150 investors, Oct 2022 to mid-2024. Promised 40 to 50 percent in 30 to 45 days. SEC says the code had no AI or stop-loss, only about 3 percent (about $380,000) bought crypto, no profit. These are SEC allegations, not findings. | https://www.theblock.co/news/regulation/2026-05-30-sec-sues-privvy-founder-over-12-3-million-crypto-scheme-as-ai-bots-turn-out-to-be-neither-403118 |
| TSAI Pro / Cryptoaiml SEC complaints (search summary only, dated by that summary as 2026-09-29, $12.5M) | NOT VERIFIED beyond a search summary. I did not open the complaint. | https://www.investmentnews.com/regulation-legal-compliance/fake-signals-frozen-accounts-sec-sues-crypto-ai-platform-over-125m/268436 |
| FTC "Operation AI Comply" (Sept 2024, via law-firm summaries) | Cases on AI-powered business opportunities with guaranteed income claims (Ascend Ecom, Ecommerce Empire Builders, FBA Machine). Not trading bots specifically. One summary mentions a "#1 secret passive income crypto trading bot" case, unnamed, NOT VERIFIED. FTC primary page not opened. | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes |

No FINRA-only AI bot warning retrieved. Did not find an FTC action I could confirm that is specifically about a trading bot.

## 2. Public LLM trading contests: Alpha Arena (nof1)
nof1 primary pages: not retrieved (one URL guess returned 404; leaderboard not read). Everything below is secondary press.
| Item | Figure | Source |
|---|---|---|
| Season 1, crypto perps on Hyperliquid per press, $10,000 each, Oct 18 to Nov 3 2025 | Qwen3 Max $12,231 (+22.3%), DeepSeek $10,489 (+4.9%), Claude Sonnet 4.5 $5,799 (-42.0%), Gemini 2.5 Pro $5,445 (-45.6%), Grok $4,208 (-57.9%), GPT-5 $4,126 (-58.7%). Four of six lost. | ForkLog 2025-11-04: https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/ |
| Same season, other outlet | Search summary says ChatGPT lost 63 percent and trading costs dominated early PnL. Conflicts with ForkLog's 58.7 percent, probably different snapshot. NOT RECONCILED. | https://benzinga.com/crypto/cryptocurrency/25/11/48651974/chatgpt-lost-63-trying-to-trade-crypto-but-one-china-ai-made-a-healthy-profit |
| Season 1.5, US equity tokens, started Nov 20 2025, ended about Dec 3 to 5 2025 | Winner "mystery model" revealed as Grok 4.20, about +12.11 percent average, one report $10,000 to $12,193 in 14 trading days. Mid-contest headlines said about 22 percent, so figures moved. Not evidence of beating the market. | https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/ and https://finance.yahoo.com/news/elon-musks-grok-4-20-123855766.html |
| Season 2 | Planned only. No results found. | search 2026-11-26 |

Read: same model family, Grok, went -57.9 percent then +12 percent in two different two-week windows and formats. That is variance, not skill. Contests used $10,000 stakes, not $60.

## 3. Independent research on LLM trading (retrieved abstracts)
| Paper | Finding | URL |
|---|---|---|
| FINSABER, Li et al. (arXiv 2505.07078) | Two decades, 100+ symbols: earlier LLM advantages "deteriorate significantly" with broader and longer tests. Too cautious in bull markets, too aggressive in bear markets with heavy losses. | https://arxiv.org/abs/2505.07078 |
| "The Alpha Illusion" (arXiv 2605.16895, May 2026) | One-year 2025-01 to 2026-01 five-ticker test: buy-and-hold about $104.8K from $100K; TradingAgents $102.3K net; QuantAgent $77.9K net. 35 of 40 system-cost combinations in prior papers were not modeled. Reported alpha is "not deployment evidence". Small sample, five tickers, authors' own reproduction. | https://www.alphaxiv.org/abs/2605.16895.md |
| Other 2026 arXiv titles from search (Look-Ahead-Bench 2601.13770, 2605.24564, 2603.17692) | Titles and snippets only, not read. Parametric look-ahead bias (model memorized history) and models doing worse live than on static benchmarks are claimed. NOT VERIFIED. | https://arxiv.org/html/2603.17692 |

Live-versus-backtest gap for the same agents: no direct study found.

## 4. Retail trader base rates (secondary)
| Item | Figure | Source |
|---|---|---|
| Brazil day traders, Chague, De-Losso, Giovannetti | About 1.1 percent of 1,551 futures day traders beat minimum wage over the period; no evidence of learning. Futures, not stocks or memecoins. | https://www.bloomberg.com/news/articles/2020-08-15/day-traders-in-brazil-study-would-ve-done-better-with-9-to-5-job and https://econpapers.repec.org/paper/spawpaper/2019wpecon47.htm |
| Barber and Odean, Taiwan | Seen only in blog summaries. NOT VERIFIED. |  |

## 5. Memecoin claims (Solana, pump.fun)
| Item | Figure | Source |
|---|---|---|
| Solidus Labs 2025 report (vendor report, own definitions) | About 93 percent of 388,000 pools showed soft rug pull traits; headlines say 98 to 99 percent. Broad definitions, not peer reviewed. | https://www.soliduslabs.com/reports/solana-rug-pulls-pump-dumps-crypto-compliance |
| Pine Analytics (Substack) | Sniper wallets took over 15,000 SOL in a month; 85 percent sold within five minutes. | https://pineanalytics.substack.com/p/exit-liquidity-machines |
| Dune-dashboard article | Top 50 wallets by profit were 49 bots and 1 person. Secondary, single source. | https://cryptoslate.com/?p=439345 |

Meaning: where bots do profit in memecoins, the retrievable evidence points to speed bots and creators, not a retail user running an AI guide on $52.

## 6. Rules check
**PDT.** FINRA Regulatory Notice 26-10 (retrieved): new intraday margin standards replace day trading margin requirements "in their entirety", including the day-trade-count PDT designation and the $25,000 minimum equity. Effective June 4, 2026; members may phase in until October 20, 2027. No new fixed minimum equity is named; the rule measures an "intraday margin deficit". Regular maintenance margin is unchanged. SEC approval around April 14, 2026 (Federal Register 2026-07485, search listing). https://www.finra.org/rules-guidance/notices/26-10
E*TRADE summary (search snippet only) says $2,000 margin minimum and no day-trade counting. 
**NOT VERIFIED: what Robinhood itself does today.** Investing CLAUDE.md and Zac's 3-day-trades-a-month assumption may be stale for Robinhood. Check Robinhood's own support page, and whether a $60 cash account is affected at all. Cash accounts have separate settlement rules I did not check.
**Robinhood stop orders on fractional shares.** Robinhood's take-profit/stop-loss article: "Only whole-share quantities are supported." Stop loss is a stop order that becomes a market order; closes existing stock/ETF positions only. https://robinhood.com/us/en/support/articles/take-profit-stop-loss/ . Robinhood's fractional-shares article does not list stop orders and says fractional orders are handled "Not Held" with time and price discretion. https://robinhood.com/us/en/support/articles/fractional-shares/ . Conclusion: stops on fractional shares not confirmed by any official page. The only claim of support was a third-party Google Sites page, rejected. Test only by Zac in-app, or by Robinhood support. Relevant to the locked rule "stop at 2 times ATR".

## What could not be verified
nof1 primary leaderboard and posts; SEC Investor.gov alert text (403); TSAI and Cryptoaiml complaints; FTC trading-bot case name; Barber and Odean originals; any audited bot track record; the $52 to $4,392 guide; Robinhood's own post-June-2026 day trading policy.

## Risk notes
- Contest wins over two weeks are not forward evidence. Fees and spreads: Alpha Arena press says costs dominated early PnL (one secondary source); the Alpha Illusion paper shows costs cut paper Sharpe roughly in half.
- A $60 account cannot diversify and fractional stops are unconfirmed.
- Screenshot or paid-course claims are marketing until a broker statement or exchange record is shown.

## Paper tests trading-director could run
1. Log the guide's rules as a fixed rule set and paper trade them through the watch week with Coinbase public candles, fees and spread modeled, versus buy-and-hold BTC.
2. Record every number Alpha Arena style: net of fees, 30-plus trades before any verdict.
3. Zac checks the Robinhood app order screen for a stop on a fractional share (no order placed).

## Verdicts
See ledger rows in `D:\WKP\Investing\research\strategies-tried.md`.
