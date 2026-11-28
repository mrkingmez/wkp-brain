# OpenInsider latest cluster buys, first pull (2026-11-26, evening ET)

Source: http://openinsider.com/latest-cluster-buys, read in Zac's Windows Chrome (Browser 2), 100 rows, filing dates 2026-10-26 to 2026-11-25. OpenInsider says its data comes from sec.gov, posted 6:00-22:00 ET Mon-Fri. Read-only. Nothing traded. This is a data observation, not a recommendation, and not a verified signal: no backtest has been run.

Access notes: the home page and https:// URLs gave a Chrome error page; the plain `http://openinsider.com/latest-cluster-buys` and `http://openinsider.com/screener?...` URLs load. Purchase-only flag in screener URLs is `xp=1`. SEC EDGAR Form 4 Atom feed also loads (`https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=4&...&output=atom`, HTTP 200, 2026-11-26). OpenInsider terms on automated use NOT RETRIEVED: read it in the browser, do not run a bot against it until the terms are read.

## Rows with 3+ insiders and trade value of $1M or more (filing date, ticker, insiders, price, value, own change)
| Filed | Ticker | Co | Ins | Price | Value | Own chg |
|---|---|---|---|---|---|---|
| 11-25 | COHR | Coherent Corp | 3 | $198.10 | $51.09M | +132% |
| 11-25 | GLXY | Galaxy Digital | 3 | $12.42 | $16.33M | +125% |
| 11-25 | BPRE | Bluerock Private Real Estate Fund (closed-end) | 3 | $12.59 | $41.72M | >999% |
| 11-25 | BORR | Borr Drilling | 2 (D flag) | $3.99 | $81.93M | +66% |
| 11-23 | FUN | Six Flags | 3 | $10.88 | $34.95M | +62% |
| 11-23 | PAM | Pampa Energy | 3 | $23.81 | $69.99M | +8% |
| 11-25 | TMS | Teamshares | 3 | $4.32 | $1.18M | +73% |
| 11-25 | PRE | Prenetics | 3 | $9.92 | $1.26M | +18% |
| 11-25 | VISN | Vistance Networks | 3 | $4.09 | $1.23M | +15% |
| 11-20 | TTMI | TTM Technologies | 3 | $73.60 | $2.58M | +14% |
| 11-20 | EQPT | EquipmentShare | 3 | $14.27 | $1.13M | +5% (D) |
| 11-20 | UPBD | Upbound Group | 10 | $23.50 | $2.29M | +19% (D) |
| 11-20 | HPP | Hudson Pacific | 3 | $8.85 | $1.06M | +68% |
| 11-23 | KYN | Kayne Anderson Energy Infra Fund (closed-end) | 3 | $13.10 | $1.07M | +8% |
| 11-18 | STWD | Starwood Property Trust | 3 | $11.80 | $18.73M | +8% |
| 11-16 | CTEV | Claritev | 2 | $25.29 | $10.41M | +19% (D) |
| 10-30 | RAPP | Rapport Therapeutics | 7 | $21.36 | $22.02M | +42% |

(Other rows with 2 to 5 insiders and smaller values are on the page; re-pull for the full table.)

## Cautions for the trading department
- Several "cluster" rows are large holders, sponsors or closed-end fund affiliates (BPRE, BORR, KYN, GLXY), not ordinary executives. Classify insider type before scoring.
- Ownership change over 100% on a tiny base (BPRE >999%) is not informative.
- Example of why one signal is not enough: NEGG (Newegg) 10% owner V. Galkin bought about $50M between 2025-07-08 and 2025-08-15 at $19.84 to $104.72; the same ticker printed $8.33 on 2026-11-20 and a director has sold on a steady schedule since June 2026. Source: same site, screener s=negg, read 2026-11-26.
- Filing lag: trade dates run 1 to 3 days before filing dates (some weeks). The price on the filing day is not the price the insider paid.
- Free-feed limit: Alpaca paper account gets IEX data only; OTC, foreign and some ADR names (PAM, BORR, TSM) may not trade or quote on the stock watcher.

## Suggested scoring use (for trading-director to decide)
Treat as a scanner input in the paper test: open-market purchases only (P), 3+ insiders, filing within 3 days, insider type classified, forward return logged at 1, 5, 20 trading days against SPY, regime tag recorded. No sizing from this signal until it has its own counted record. Zac's capital goal: grow capital over the next year to fund building his products ("toys for sale", his words). No live money from this work without Zac.
