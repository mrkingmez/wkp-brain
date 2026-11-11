# NFL DFS facts brief (fantasy football desk, internal)

Date: 2026-11-10. Requested by the fantasy football desk. Labels: OBSERVED = I read it on the page or file myself. SECONDARY = third party, not the platform or author. NOT AVAILABLE = could not retrieve. Date-flag: anything older than 2 years is marked STALE.

## 1. Answer in plain words

- Rosters and caps are confirmed current by a 2026 secondary source. Scoring tables come from older articles (2019 and 2023), so they are STALE. The official DraftKings help page blocked me (403) and the FanDuel help page failed (SSL error). Check both official pages before building a model on exact values.
- The two papers do not say what the question assumes. Hunter, Vielma, Zaman tested hockey and baseball, not football. Haugh and Singal tested FanDuel NFL 2017. I read the full Hunter text, but only the Haugh abstract and Haugh's own slides.
- DraftKings gives a per-contest CSV with % Drafted, for 10 days after the contest ends. No free historical ownership archive found.
- nflverse game data has spread_line and total_line for every game 1999 through 2025, and 150 of 272 games for 2026 so far. The Odds API historical endpoint is paid only.
- No public study with correlation coefficients between game total and DFS or fantasy scoring by position was found.

## 2. Item 1. Platform rules

### DraftKings Classic NFL
- Roster, 9 players: QB, 2 RB, 3 WR, TE, FLEX (RB/WR/TE), DST. Salary cap $50,000. Label: OBSERVED on Rotowire (https://www.rotowire.com/football/article/dfs-football-101-how-to-play-on-draftkings-46369, last updated 2023-03-09, STALE), and SECONDARY confirmed as current by Stokastic (https://www.stokastic.com/articles/nfl-dfs/draftkings-vs-fanduel-nfl-dfs, published 2026-07-15, updated 2026-10-06).
- Scoring table, OBSERVED from Rotowire (2023-03-09, STALE, not the official page):
  - Passing TD 4. Passing yards 1 per 25. 300+ pass yard bonus 3. Interception -1.
  - Rushing TD 6. Rushing yards 1 per 10. 100+ rush yard bonus 3.
  - Receiving TD 6. Receiving yards 1 per 10. 100+ receiving yard bonus 3. Reception 1 (full PPR).
  - Punt, kickoff, FG return TD 6. Fumble lost -1. 2 point conversion 2. Offensive fumble recovery TD 6.
  - DST: sack 1, interception 2, fumble recovery 2, defensive TDs 6, safety 2, blocked kick 2, 2 pt or XP return 2. Points allowed: 0 is 10, 1-6 is 7, 7-13 is 4, 14-20 is 1, 21-27 is 0, 28-34 is -1, 35+ is -4.
- Current confirmation (SECONDARY, 2026-10-06): Stokastic states full PPR and 3 point bonuses at 300 pass yards, 100 rush yards, 100 receiving yards.
- Official page https://www.draftkings.com/help/rules/nfl returned 403 to me. NOT AVAILABLE from the primary source.

### FanDuel NFL
- Roster, 9 players: QB, 2 RB, 3 WR, TE, FLEX, DEF. Cap $60,000. OBSERVED on Rotowire (https://www.rotowire.com/football/article/dfs-football-101-how-to-play-on-fanduel-46545, dated 2019-07-29, STALE). SECONDARY confirmed current by Stokastic 2026-10-06 (same URL as above): classic is one QB, 2 RB, 3 WR, TE, FLEX, one defense, cap $60,000, half PPR, no yardage bonuses. Kickers appear only in single game formats per Stokastic.
- Note a conflict: one search summary of FanDuel's own fantasy page listed a different layout with a K slot. I could not open that page myself, so it is UNVERIFIED. Trust the two sources above for Classic.
- Scoring table, OBSERVED from Rotowire (2019, STALE):
  - Rushing yards 0.1, rushing TD 6. Passing yards 0.04, passing TD 4, interception -1.
  - Receiving yards 0.1, receiving TD 6, reception 0.5. Return TDs 6. Fumble lost -2. 2 pt conversion 2.
  - DEF: sack 1, fumble recovered 2, interception 2, return TD 6, safety 2, blocked kick 2, XP return 2. Points allowed tiers same as DraftKings (10, 7, 4, 1, 0, -1, -4).
  - Kicking (not in Classic per 2026 source): FG 0-39 is 3, 40-49 is 4, 50+ is 5, XP 1.
- Official FanDuel help page: NOT AVAILABLE (SSL handshake failure).

## 3. Item 2. Published research

### Hunter, Vielma, Zaman (2016), "Picking Winners in Daily Fantasy Sports Using Integer Programming"
- Source OBSERVED: arXiv 1604.01455 v3, 23 Jan 2019 revision, full text read. https://arxiv.org/abs/1604.01455 (first posted April 2016). Later pub in INFORMS Journal on Optimization per the manuscript header, not checked.
- Sport: hockey (2015 NHL season data) and baseball. NOT NFL. DraftKings contests. Predictions came from Rotogrinders and Daily Fantasy Nerd.
- Abstract (short quotes): the method "maximize[s] the expected score of an entry subject to a lower bound on its variance and an upper bound on its correlation with previously constructed entries." They "rank in the top-ten multiple times in hockey and baseball contests with thousands of competing entries."
- Stacking, hockey only: they define goalie stacking (avoid, goalie is negatively correlated with opposing skaters), line stacking (same line players, positively correlated), and defensemen stacking. In backtests "the lowest profit margin is achieved by no stacking," and Type 4 stacking (most stacking, at most three teams) had the highest mean profit margin for 100 and 200 lineups. They say this "maximizing variance strategy is effective for winning top-heavy contests."
- Portfolio: more lineups shifted the profit distribution upward. With one lineup the median profit margin was -100 percent, and outliers produced much of the profit at 100 and 200 lineups.
- Their own caveat: "We do not use the actual value of any correlations, just a basic understanding of their sign." Predictions "can even be noisy."
- Football stacking (QB with receivers) is NOT tested in this paper. It cites a Jonathan Bales article on QB pairing as background only.

### Haugh and Singal (2021), "How to Play Fantasy Sports Strategically (and Win)"
- Management Science 67(1):72-92, DOI 10.1287/mnsc.2019.3528. Management Science PDF was paywalled and I did not read it. Abstract SECONDARY via search summary of EconPapers and SSRN (https://econpapers.repec.org/RePEc:inm:ormnsc:v:67:y:2021:i:1:p:72-92 and https://papers.ssrn.com/abstract=3393127, SSRN direct fetch gave 403).
- Abstract content (paraphrase of secondary summary): portfolio framework modeling how opponents pick teams, Dirichlet-multinomial opponent model fitted by Dirichlet regression, expected reward maximization for double-up and top-heavy payouts linked to mean-variance optimization, reduces to binary quadratic programs, algorithm for multiple entries, estimates value of insider trading and collusion, tested on 2017 NFL season contests. The abstract does not mention stacking.
- Haugh's own slides, OBSERVED (Columbia-Bloomberg workshop, 2019-05-17, https://cfe.columbia.edu/sites/default/files/content/slides/How to Play Fantasy Sports Strategically (and Win).pdf):
  - "Conclusion: Want to choose a diversified portfolio of teams where each team's fantasy points score has high mean and variance."
  - Portfolio teams should not compete with each other, so avoid highly correlated entries.
  - Results: FanDuel, 2017-18 NFL season, top-heavy focus, $50 per week for each of two models with N = 50 entries. Slide headline reads "ROI of Over 350% in Just 17 Weeks!" This is the authors' own slide for one season and one account. It is a small sample, I could not verify it independently.
  - Ongoing research slide: "Very high variance in NFL contests due to injuries, roster size, weather, etc." and "Only 16 games per team so also high seasonal variance."
  - Stacking appears only once, as "handle this to some extent via stacking copula," in the further research list.
- So I cannot quote a stacking finding from Haugh and Singal. NOT AVAILABLE beyond the slides.

## 4. Item 3. Ownership and results after contests; free archives

- DraftKings: GameCenter has "Export Lineups to CSV." The CSV has an entrant section (rank, entry ID, entry name, time remaining, points, lineup) and an athlete section (player, roster position, % Drafted, FPTS). Available "10 days after the contest ends." OBSERVED on a DraftKings help mirror (https://z3n-sq-gaming.zendesk.com/hc/en-us/articles/18427755136791-How-do-I-download-a-CSV-to-see-GameCenter-standings-for-a-contest-US), a mirror not the official domain, date unknown. Means ownership is contest specific and the file disappears after 10 days unless saved.
- FanDuel: no official page found. SECONDARY (Rotowire, years old) says reviewing a completed FanDuel contest's ownership is manual, whereas DraftKings allows a CSV. 4for4 says FanDuel shows ownership percentages for players you rostered. Current FanDuel behavior: NOT AVAILABLE.
- Free archives of historical NFL DFS salaries, ownership, results: none confirmed.
  - nfldfs Python package (https://pypi.org/project/nfldfs/) scrapes rotoguru1 salary and points data for DraftKings, FanDuel, Yahoo. I did not test it or confirm rotoguru is still live. SECONDARY.
  - A RapidMiner 2017 competition used a rotoguru DraftKings file for 2014-2017 with only weeks 1-9 per year. Hosting unconfirmed.
  - Rotogrinders ResultsDB is Premium only. Stokastic downloads need membership. BigDataBall NFL DFS data is paid (season pass listed at $25). Footballguys has free weekly percent rostered pages, but these are projections not results.
  - Ownership results by contest: free only for contests you personally entered and saved within 10 days (DraftKings).

## 5. Item 4. Closing lines

- nflverse nfldata games.csv, OBSERVED today by downloading https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv (2026-11-10). Columns include spread_line, total_line, away_moneyline, home_moneyline, over_odds, under_odds. Counts of games with both spread_line and total_line filled: every season 1999 through 2025 is 100 percent (1999 259 of 259, 2020 269, 2021 285, through 2025 285). 2026: 150 of 272 rows filled (rest not yet posted). I did not check whether the nflverse-data "schedules" release matches this file row for row; it describes itself as maintained from this nfldata source (GitHub release page, https://github.com/nflverse/nflverse-data/releases/tag/schedules).
- Not verified: whether these values are true closing lines or a snapshot. The data dictionary page rendered empty to my fetch (https://nflreadr.nflverse.com/articles/dictionary_schedules.html), so the definition and sign convention are NOT AVAILABLE from me. Check before using as "closing."
- moneyline and spread odds columns exist but I did not count fill rates for them.
- The Odds API historical endpoint, OBSERVED on the guide (https://the-odds-api.com/liveapi/guides/v4/#historical-odds): snapshots from 2020-06-06, 10 minute intervals, 5 minute from September 2022. Cost 10 credits x markets x regions per call. Paid plans only per the guide. Pricing page (https://the-odds-api.com/) lists Starter free 500 credits a month, 20K at $30 a month, 100K at $59, 5M at $119, 15M at $249, and shows Historical Odds on every plan including Starter, which conflicts with the guide's "paid usage plans only." UNVERIFIED which is right, test with a free key. NFL specific historical coverage: not stated. Also the 2020 floor means 1999-2019 is not covered.

## 6. Item 5. Does a game's Vegas total predict QB, WR, RB, TE scoring

- No rigorous public study with correlation coefficients by position found. NOT AVAILABLE.
- Qualitative only:
  - FantasyPros (https://www.fantasypros.com/2023/08/how-to-use-vegas-odds-for-fantasy-football-2023, 2023-08-25, STALE by 2 years): charts of game total and team total vs fantasy points by position, data from nflfastR since 2013. Says points rise with game total and the effect is "lowest for running backs." No coefficient, no sample size. Its only coefficients are for player prop lines: pass yards 0.43, QB rush yards 0.64, RB rush yards 0.53. Those are not game totals.
  - FantasyLabs (https://www.fantasylabs.com/?p=3668, 2015-09-24, STALE): says QBs show the strongest link between Vegas Score and fantasy performance of the four groups and RB results are noisy. No coefficients (I opened the page and none are given).
  - Fantasy Footballers Vegas Report pages assert team implied totals correlate most strongly with fantasy points, with no data. Treat as opinion.
- Practical route: join nflverse total_line and spread_line to player game logs (nflverse stats_player), compute implied team total as (total_line minus team spread) divided by 2, regress by position with controls. That would be our own result, not a published one.

## 7. What authors usually get wrong (for the desk)

- Citing Hunter et al. as proof that QB stacking works. It tested hockey and baseball, and used correlation sign, not measured values.
- Citing Haugh and Singal for a stacking result. The accessible material does not state one.
- Treating the 350 percent ROI slide as evidence of an edge. One season, own account, own slide.
- Treating team implied totals as validated by data. Only opinion and uncited charts were found.

## 8. Open questions

- Check official DraftKings and FanDuel rules pages in a logged-in browser for the exact 2026 scoring tables, especially FanDuel's current layout.
- Confirm with the nflreadr dictionary (run `nflreadr::dictionary_schedules` in R) what spread_line and total_line mean, and whether they are closing lines.
- Test whether The Odds API Starter key can reach historical NFL snapshots.
- Haugh and Singal full text via a library or author copy, if stacking findings matter.
