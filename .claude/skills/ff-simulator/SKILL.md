---
name: ff-simulator
description: Monte Carlo simulator for Zac's IRFL lineup and the weekly pick'em card. Builds coaching tendencies from nflverse play-by-play (last 3 seasons, recency weighted), simulates every NFL game thousands of times, scores each player under IRFL rules including IDP, and picks the best lineup. Use for "run the simulation", "best lineup", "who do I start", "simulate the week", coach tendency questions.
---

# ff-simulator

Built 2026-10-15 (Zac's call: simulations using real coaching tendencies, the way his
gambler friend does for DraftKings and FanDuel DFS, plus nflverse Next Gen Stats).
Personal use, decision support only. Never submits anything.

## Run order (all scripts in `scripts\`, Python 3.12 with `-I`)
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

## What the model does
- `coach_model.py`: per coach, weights games by recency (half-life 17 games), shrinks thin
  samples to the league mean, falls back to the team's own history for new head coaches.
  Features: neutral pass rate, overall pass rate, pass over expected, red-zone pass rate,
  4th-and-short go rate, trailing/leading pass rate shifts, pace, shotgun, no-huddle.
- `simulate.py`: draws a margin and total around the market line, turns script into
  pass/run volume with that coach's tendencies, splits volume by player shares, then scores.
  Defenders earn tackles/sacks/INTs/PDs off the opponent's simulated plays.

## Known limits (state these whenever results are shown)
- No offensive coordinator column exists, so a head coach who does not call plays (several
  defensive HCs) is represented by the team's recent offense blended with him.
- First-year coaches lean on the team's earlier history and the league mean.
- Injury news is only as fresh as the MFL export. Re-run Thursday and Sunday morning.
- Single-game player output is noisy: the backtest in `data\ff-simulator\backtest_sim.csv`
  is the honest measure of how much the simulation beats a plain recent average.
- Kickers use an average field goal worth 3.75 points (distance not simulated).
