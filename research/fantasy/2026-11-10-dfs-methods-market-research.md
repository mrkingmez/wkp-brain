# DFS methods: what winning NFL DraftKings and FanDuel players do, and what is publicly known

Date: 2026-11-10. Analyst: market-research. Internal, read-only. Nothing bought, no sign-ups.

Labels: OBSERVED = I opened the page and read it this session. SECONDARY = came from a web search result summary or a relay, I did not open the primary. NOT AVAILABLE = could not retrieve. Several fetches failed (Informs 403, Imperial site DNS error, PyPI page error), so most numbers below are SECONDARY. Nearly everything here is years old, so treat all of it as potentially stale (over 90 days).

## Bottom line

1. The best-sourced academic work (Hunter, Vielma, Zaman 2016; Haugh and Singal 2021) says winning big-field tournaments means building many lineups that are high-variance and not too correlated with each other, and modeling what opponents pick. It does not hand a casual player a formula.
2. No free source found gives historical DraftKings or FanDuel NFL salaries plus actual ownership. A backtest on real DFS slates is not possible from free data I could find. A proxy backtest (nflverse stats plus lines, salaries you scrape yourself) is possible.
3. Profitability is a small-minority game. The one widely cited figure (91 percent of profits to 1.3 percent of players, MLB, first half of 2015) is secondhand and old.
4. Honest expectation for a casual player: negative expected value after rake. Treat DFS as entertainment money.

## 1. Ownership and leverage (GPP)

- Finding: Large-field tournaments pay top-heavy, so players try to differ from the crowd (lower owned, "leverage") while keeping similar upside.
- Evidence:
  - Haugh and Singal, Management Science 2021, model opponents' lineup choices with Dirichlet regression and optimize a portfolio for top-heavy and double-up contests, tested on 2017 NFL contests. SECONDARY (search summary; the Informs PDF returned 403). Authors report 350 percent return over one NFL season. That is the authors' own claim, no replication found. https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.2019.3528 and https://papers.ssrn.com/abstract=3393127
  - Practitioner sites (Stokastic, 4for4, FantasyAlarm) publish weekly ownership projections, mostly gated. SECONDARY.
  - FantasyPros, Joe Pepe, 3 Sep 2024: correlation is critical in tournaments, ownership "does not matter to me in cash games." No ownership percentages or data source given. OBSERVED. https://www.fantasypros.com/2024/09/nfl-dfs-advice-stacking-strategy-fantasy-football
- Published numbers on how much leverage adds to win rate: NOT AVAILABLE. One unvetted page (nfl-2026-projections.pages.dev) claims a backtest win rate of about 22 percent versus 8.3 percent baseline. SECONDARY, methodology unknown, do not use.
- So what: ownership is a tiebreaker among equal-projection choices, only in large GPPs. Do not chase it in cash. Without free ownership data we cannot verify it works for us.
- Confidence: medium on the concept (academic and practitioner agree), low on any magnitude.

## 2. Correlation and stacking

- Finding: Lineups win big tournaments by having several players hit together, so QB plus pass catcher, plus a bring-back from the opposing team, is the standard build.
- Evidence:
  - Hunter, Vielma, Zaman (arXiv 1604.01455, v1 6 Apr 2016, v3 23 Jan 2019). OBSERVED abstract page. Method: build entries one at a time by integer program, maximize expected score subject to a lower bound on variance and an upper bound on correlation with earlier entries. Reported top-ten finishes multiple times in hockey and baseball contests with thousands of entries. The abstract gives no NFL numbers and no stacking figures. https://arxiv.org/abs/1604.01455
  - Correlation coefficients, FanSided piece (2019) citing a FantasyLabs matrix over about five seasons: QB-WR1 .53, QB-WR .51, QB-TE1 .47, QB with opposing QB .58. SECONDARY. Stale. https://fansided.com/2019/08/25/nfl-dfs-gpp-strategy-fanduel-draftkings/4
  - Numberfire (date not confirmed): teams that stacked a WR with the QB won 1.30 percent less than those that did not, the author suggests stackers were forcing it. Same piece says punting a position raised win rate in every contest type. SECONDARY, stale. https://numberfire.com/nfl/news/2976/how-to-win-playing-daily-fantasy-football-part-2-tournament-strategy/amp
  - RB versus own defense negative correlation, and game stacks: described qualitatively by many sites. No quantified source retrieved. NOT AVAILABLE.
- So what: correlation is the best-supported tournament edge, but the numbers we have are old and secondhand. nflverse play-by-play lets us measure QB-WR and bring-back correlations ourselves for free, which beats quoting a 2019 matrix.
- Confidence: medium on direction, low on the coefficients.

## 3. Game environment (totals and spreads)

- Finding: Practitioners start from the betting market: high game total and close spread means more plays and more scoring on both sides.
- Evidence: The Fantasy Footballers weekly "Vegas Report" series asserts team implied totals correlate most strongly with player fantasy output, and notes high-total games are not always the best tournament stacks. SECONDARY (search results only, no methodology, no R-squared, no sample). A FantasyPros piece (Sep 2023) says game totals tend to be very predictive of team offensive performance. SECONDARY.
- Published R-squared of fantasy points on game total: NOT AVAILABLE. Nobody I found published one.
- Free data: the nflverse `schedules` release carries spread_line, total_line and moneylines (per WKP's own nfl-data skill notes in TASKS.md, 2026-09-12). The release list is OBSERVED at https://github.com/nflverse/nflverse-data/releases (tags include schedules, stats_player, stats_team, players, weekly_rosters, espn_data, ftn_charting). The page showed no license text.
- So what: this is testable in-house. Regress DK-style points per player-game on closing total and implied team total across nflverse seasons and publish our own number. Free, and closes the gap.
- Confidence: medium that the effect is real, low on size.

## 4. Cash versus tournaments

- Finding: Cash (50/50, double-up) wants floor and projection. GPP wants ceiling and correlation. Single-entry cash contests are softer than multi-entry ones.
- Evidence (SECONDARY, search summaries of The Fantasy Footballers "Borg" reviews and 4for4):
  - 2025 DraftKings $25 double-up cash lines, weeks 1 to 3: 115.38, 136.26, 150.26 points. Week 1 $10 double-up: 115.38. A week 12 review calls roughly 190 the highest double-up cash line in three years and says the line hit 160 plus five times that season. https://www.thefantasyfootballers.com/dfs/borgs-dfs-cash-lineup-review-for-week-15-fantasy-football-2/
  - Week 3 2024: top $25 double-up team scored 280, which would have placed 9th in the Milly Maker. https://www.thefantasyfootballers.com/dfs/borgs-dfs-cash-lineup-review-for-week-3-fantasy-football-2
  - 4for4: softest cash line is usually the single-entry $5 double-up, because multi-entry contests have sharps entering up to 100 lineups. https://www.4for4.com/node/134337
  - Break-even in 50/50 with 10 percent rake needs about 55 percent win rate. SECONDARY from a tip-sheet site (oddsreference.pages.dev). My own arithmetic agrees: a win pays 2 for 1 minus rake, so about 55.6 percent at 10 percent rake.
- Typical winning GPP first-place score: NOT AVAILABLE as a season-wide number. Only the 280 example above. Optimal entry counts: NOT AVAILABLE beyond the single-entry softness point.
- So what: for Zac, single-entry double-ups are the realistic format. The cash line moves by week (about 115 to 190 in these samples), so a fixed target is wrong.
- Confidence: medium (concrete weekly figures, but one publisher, 2024 and 2025 only).

## 5. Punt QB (about 4,000 dollar quarterback)

- Finding: No study isolates the 4,000 dollar DraftKings QB. Evidence is old and mixed.
- Evidence (SECONDARY, search summaries):
  - Numberfire: punting a position correlated with higher win rate across contest types (stale).
  - FantasyLabs (2014 season piece): very few DFS games are won on a cheap QB alone.
  - Analysis of top 0.1 percent Milly Maker entries: the cheap QB did not need a big game for a lineup to finish near the top.
  - The Fantasy Footballers: the old advice to spend down at QB has faded, spending up and not stacking is in favor.
  - 2015 FanDuel analysis of 503 QB games: you need not be very selective at QB in cash.
- So what: do not build the system around a punt QB. Treat it as an optional lever, test it on our own sim, and note it usually removes the stack.
- Confidence: low. Evidence is old and indirect.

## 6. Free data and tools

| Item | URL | Free? | Coverage | Status |
|---|---|---|---|---|
| nflverse releases (schedules with lines, stats_player, stats_team, players, weekly_rosters, espn_data, ftn_charting) | https://github.com/nflverse/nflverse-data/releases | Free, no key | Multi-season, schedules is one rolling file | OBSERVED tag list |
| nflscrapR play-by-play on Kaggle | Kaggle (exact page not opened) | Free per search result | Older seasons only | SECONDARY |
| RotoGuru DK salary data via PyPI `nfldfs` scraper | https://pypi.org/project/nfldfs/ | Package free | One forum user says DK data covers 2014 week 1 to 2017 week 5, only weeks 1 to 9 of each year | SECONDARY. PyPI fetch failed, so ownership coverage, license and whether the source site still works are unverified |
| Weekly ownership projections | Stokastic, 4for4, FantasyAlarm | Mostly paywalled | Current weeks | SECONDARY. Not signing up |
| Historical DK or FD salary plus actual ownership archive | none found | n/a | n/a | NOT AVAILABLE as free |

- So what: be honest with Zac. A true DFS backtest (real salaries, real ownership, real payouts) needs data we do not have for free. Free route: simulate projections with nflverse and use the public cash-line figures above as the target. DraftKings may let a user download their own contest history. I did not verify that, so ask before relying on it.
- Confidence: high that no turnkey free source surfaced in my searches, medium that none exists (search coverage was limited).

## 7. Realistic profitability

- Finding: Profits are highly concentrated and the average player loses.
- Evidence (SECONDARY):
  - McKinsey 2015, relayed by Imperial Business School, WSJ, PBS and the New York AG: 91 percent of DFS profits for the first half of the 2015 MLB season went to 1.3 percent of players, who paid 40 percent of entry fees. I did not open the McKinsey report. DraftKings disputed the framing. MLB only, stale. https://www.pbs.org/newshour/bb/why-online-daily-fantasy-sports-are-mostly-a-losers-game
  - A 2014 NFL season study: median player paid 87 dollars in entry fees and had a median net loss of 30.70 dollars. Primary not identified. SECONDARY, stale.
  - Rake: a tip-sheet site says 8 to 15 percent, another says DraftKings about 8 percent. Primary fee pages not opened. SECONDARY, approximate. Current share of profitable players: NOT AVAILABLE.
- So what: the right expectation for Zac is a small expected loss per dollar entered with high swings, so entry fees are entertainment money, especially given his stated debt situation. Nothing I found supports a reliable edge for a casual player.
- Confidence: medium on direction (several independent sources agree), low on exact figures.

## What would raise confidence (needs a go, not done)

- Open the Informs Haugh and Singal PDF and the arXiv full text of Hunter et al. in a browser to pull exact variance and stacking findings.
- Open the McKinsey primary report.
- Check DraftKings and FanDuel official rake pages.
- Run the in-house nflverse regression for game total and QB-WR correlation.

## Sources
- https://arxiv.org/abs/1604.01455 (OBSERVED)
- https://pubsonline.informs.org/doi/pdf/10.1287/mnsc.2019.3528 (403, SECONDARY via search)
- https://papers.ssrn.com/abstract=3393127 (SECONDARY)
- https://www.fantasypros.com/2024/09/nfl-dfs-advice-stacking-strategy-fantasy-football (OBSERVED)
- https://rotogrinders.com/lessons/lesson-2-how-game-selection-can-improve-your-roi-1690593 (OBSERVED, paywalled, no usable figures)
- https://github.com/nflverse/nflverse-data/releases (OBSERVED)
- https://fansided.com/2019/08/25/nfl-dfs-gpp-strategy-fanduel-draftkings/4 (SECONDARY)
- https://numberfire.com/nfl/news/2976/how-to-win-playing-daily-fantasy-football-part-2-tournament-strategy/amp (SECONDARY)
- https://www.thefantasyfootballers.com/dfs/borgs-dfs-cash-lineup-review-for-week-15-fantasy-football-2/ and the week 3 2024 review (SECONDARY)
- https://www.4for4.com/node/134337 (SECONDARY)
- https://www.pbs.org/newshour/bb/why-online-daily-fantasy-sports-are-mostly-a-losers-game (SECONDARY)
- https://pypi.org/project/nfldfs/ (fetch failed, SECONDARY)
