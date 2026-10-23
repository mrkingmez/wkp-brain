---
name: ff-simulator
description: Monte Carlo simulator for Zac's IRFL lineup and the weekly pick'em card. Builds coaching tendencies from nflverse play-by-play (last 3 seasons, recency weighted), simulates every NFL game thousands of times, scores each player under IRFL rules including IDP, and picks the best lineup. Use for "run the simulation", "best lineup", "who do I start", "simulate the week", coach tendency questions.
---

# ff-simulator

Built 2026-10-15 (Zac's call: simulations using real coaching tendencies, the way his
gambler friend does for DraftKings and FanDuel DFS, plus nflverse Next Gen Stats).
Personal use, decision support only. Never submits anything.

## Run order (all scripts in `scripts\`, Python 3.12 with `-I`)
0. **Injury layer (added 2026-10-21, run before step 2 every week):** `build_injuries.py <season> <week>` merges MFL injuries,
   nflverse injuries + weekly rosters, ESPN league-wide injuries and ESPN transactions (latest source wins, conflicts listed)
   into `data\ff-simulator\injuries_<season>_wk<week>.csv`. Facts Zac gives directly go in `overrides_<season>_wk<week>.json`
   and are applied last. `run_week.py` uses both automatically when the csv exists (else the old MFL-only logic). Out, IR, PUP,
   NFI, reserve, practice squad, cut, suspended = removed; Doubtful plays 25%; Questionable plays 75%.
1. `fetch_pbp.py 2023 2024 2025 2026` and `fetch_stats.py 2024 2025 2026` refresh the data
   (filenames discovered live from nflverse, never hardcoded). Re-run every Tuesday after MNF.
2. Pull fresh lines into a JSON (The Odds API, ODDS_API_KEY) then
   `run_week.py <season> <week> --odds <json>` simulates every game (4000 sims) and writes
   `D:\WKP\data\ff-simulator\sim_<season>_wk<week>.npz` + `_summary.csv`.
   Out / doubtful / IR / suspended players come from the MFL injury export and are removed,
   with their usage handed to teammates. Questionable players play 75% of simulations (a
   questionable QB is replaced by the next QB in those simulations).
3. `optimize.py <season> <week> [--taxi]` picks the lineup under the IRFL slot rules
   (17 starters: QB1, PK1, RB 2-3, WR 2-4, TE 1-2, DL 2-3, LB 2-3, DB 2-3, exactly 8 IDP).
   Reports EXPECTED, SAFE and UPSIDE lineups and compares them to any lineup on the sheet.
4. `roster_compare.py` shows the simulation against the MFL projection for every rostered player.
5. `coach_table.py <season> <week>` writes the current coaching tendency table.
6. `backtest_coach.py` and `backtest_sim.py` test the models against real results.

## Report gate (added 2026-10-21, Zac's rule)
Do not simulate until every team playing that week has an injury report. `wait_and_run.py <season> <week> --until "<local time>"`
polls the nflverse injuries release every 20 minutes (bye teams excluded). When all teams are in it runs build_injuries,
fetch_odds, run_week, optimize in order. If the deadline passes first it runs nothing and lists the missing teams.
nflverse can trail the official NFL report, so a late gate is not proof the team has no report.

## Injury-adjusted margin test (2026-10-21, verdict: no usable edge, NOT wired into picks)
`injury_margin.py` backtests whether QB and RB/WR/TE injuries move a game away from the CLOSING line (2018-2026, 2,220 games,
walk-forward 2022 on). QB out: coefficient 0.05 pts (t 0.6), the market already prices it. Skill players out: 0.09 pts per
fantasy point lost (t 3.3), real but small (a 15-point WR is about 1.4 pts). Out-of-sample error did not improve (11.43 to 11.45,
13.07 to 13.00, 12.61 to 12.57, 12.27 to 12.30). Betting the adjusted side at 1+ pt: 124 of 234 (53.0%, noise at that sample).
Offense only, closing line only (nflverse keeps no opening lines). The Monday card line vs today's market gap is already
measured by `pickem_probs.py`. Use injuries as a flag on a pick, not as a number that overrides the market.

## What the model does
- `coach_model.py`: per coach, weights games by recency (half-life 17 games), shrinks thin
  samples to the league mean, falls back to the team's own history for new head coaches.
  Features: neutral pass rate, overall pass rate, pass over expected, red-zone pass rate,
  4th-and-short go rate, trailing/leading pass rate shifts, pace, shotgun, no-huddle.
- `simulate.py`: draws a margin and total around the market line, turns script into
  pass/run volume with that coach's tendencies, splits volume by player shares, then scores.
  Defenders earn tackles/sacks/INTs/PDs off the opponent's simulated plays.

## Offensive line layer (added 2026-10-21, experimental, OFF by default)
`ol_model.py` (snap_counts + pbp + pfr), `backtest_ol.py`, `simulate.set_ol(scale)`. See the backtest verdict in
`Fantasy-Football\reports\Week7-Lineup-2026-10-21.md` before turning it on.

## Known limits (state these whenever results are shown)
- No offensive coordinator column exists, so a head coach who does not call plays (several
  defensive HCs) is represented by the team's recent offense blended with him.
- First-year coaches lean on the team's earlier history and the league mean.
- Injury news is only as fresh as the MFL export. Re-run Wednesday (when Zac does his card), early Thursday morning before
  practice reports and press conferences, and Sunday morning. Added Wednesday 2026-10-21, Zac's call. Wednesday and early
  Thursday runs are pre-report, so say so in the output: injury status can still change once practice reports land.
- Single-game player output is noisy: the backtest in `data\ff-simulator\backtest_sim.csv`
  is the honest measure of how much the simulation beats a plain recent average.
- Kickers use an average field goal worth 3.75 points (distance not simulated).
