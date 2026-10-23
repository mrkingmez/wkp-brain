---
name: ff-play-sim
description: Play-by-play NFL game simulator for Zac's fantasy football (built 2026-10-22). Plays a game one snap at a time (down, distance, field position, clock, score) with head-coach call tendencies and defense matchup layers learned from nflverse play-by-play. Use for "play-by-play sim", "run the new sim", "what could this player do in this game", coach vs coach, defense matchup, and backtests of the engine. Read-only, never submits anything. The older game-level simulator is ff-simulator and is untouched.
---

# ff-play-sim

Phase 1 built 2026-10-22 (Zac's call: a different kind of sim that takes defense, injury, weather, field, head coach and
coach head-to-head into account, with Next Gen Stats to find what a player could really do). Decision support only.

## Files (`scripts\`, Python 3.12 with `-I`)
- `play_engine.py`: `load_pbp()`, `Tables(pbp, as_of)` (everything learned from games before `as_of`, e.g. 202607 = before week 7 of 2026),
  `Matchup(T, off_team, def_team, off_coach=None, use_def, use_coach, adj, stretch)`, `sim_game(T, mu_home, mu_away, n, seed, stats)`.
- `backtest_engine.py`: walk-forward team-level backtest (tables rebuilt before each week), writes
  `D:\WKP\data\ff-play-sim\backtest_games.csv`. `--n 300 --weeks 2025:5-18 2026:3-6`.

## What the engine does
- One snap at a time. Pass/run call from a league table by down, distance, field zone, score state and late-half flag, shifted by the
  head coach's own recency-weighted log-odds offset. 4th down go/FG/punt the same way. League drift shift (last two seasons) added.
- Outcomes drawn from real play pools: completion, yards per completion, sack, interception, run yards. Per-spot pools for every
  yard line (a gain of `yl` or more is a touchdown). Offense rating x defense rating (relative to league, shrunk) multiplies each.
- Penalties (snap-wiping), fumbles, pick-sixes, punt/kickoff return TDs, FG make by distance, punt net yards, drive starts from real
  kickoff pools, per-play clock from real pools with a hurry-up flag and coach pace.
- Hooks for later layers: `Matchup(adj={"cmp","sack","int","ypcmp","ypc"})` multipliers (injury, weather, surface go here).
- Not modelled: timeouts, overtime (ties split 50/50), two-point tries, home field (added as +1.5 to the margin in the backtest).

## Backtest verdict (269 games, 2025 wk5-18 + 2026 wk3-6, 300 sims each)
- Spread width: stretch 1.5 on the unit ratings makes the sim's margin sd 6.22 vs the market's 6.25 (without it 4.2, ratings are
  shrunk too hard). `Matchup` default is stretch 1.5.
- Margin MAE 9.73 vs closing line 9.57. Residual-vs-market coefficient +0.18 (se 0.19). **No information beyond the market.**
  The 55-57% bet records at 1-3 pts are inside noise (the no-defense config, which carries no information, also shows 54-55%).
- Layer check: the defense layer creates all the team separation. The coach layer changes team margin very little (it matters for
  play-calling and player volume, not for picks).
- Per-game stats vs real (2024-25): plays 60.3 vs 61.0, yards per play 5.5 vs 5.5, pass rate 57.1% vs 57.1%, 3rd down 39.7% vs 40.0%,
  FG attempts 1.9 vs 2.0, turnovers 1.1 vs 1.1, drive-length mix matches. Touchdown per snap matches in every zone.
- **Known gap:** the sim reaches the red zone ~10% less often than real offenses and under-scores. `YCAL = 1.05` splits the difference
  (yards about +2%, points still about 1.3 per team light, totals bias about -2 per game). Do not use the sim total as a number
  without bias-correcting it.

## Phase 2 (2026-10-22): player layer, QB layer, injuries
- `player_layer.py` `PlayerModel(pbp, as_of, team, avail, active)`: target and carry shares by zone (normal / inside 20 / inside 5),
  catch rate and yards per catch relative to team (shrunk), the QB (most recent weighted dropbacks among available) and the kicker.
  `avail = {gsis_id: play_prob}` removes or scales players (the week's injury file); `active=set` is the backtest-only "known active" mode.
- `play_engine.Matchup(..., qb=gsis_id)` moves completion, yards per catch, sack and interception rates by (this QB's shrunk rate) / (the
  team's recent QB-mix rate). A backup QB is therefore shrunk hard toward the league, not toward the starter.
- `sim_game(..., pm=(home_model, away_model), return_players=True)` returns per-player IRFL points over every sim (offense plus kicker, XP
  and distance-scaled field goals) and volume (targets, receptions, yards, carries). No defenders yet.
- `run_game.py <season> <week> <HOME> <AWAY>` one game with named players. `run_week_play.py <season> <week>` the whole slate plus Zac's
  roster compared with the old sim and a BLEND (writes `data\ff-play-sim\play_sim_*.csv` and `roster_compare_*.csv`).
- Blend weights on the new sim (from the backtest below, stable across both halves of the weeks): QB 0.9, K 0.5, RB 0.15, WR 0.2, TE 0.2;
  the remainder is the old ff-simulator. IDP comes from the old sim only.

## Player backtest (known-active mode, 5,550 player-weeks, 2025 wk6 to 2026 wk5, same rules as ff-simulator's backtest)
| pos | MAE new sim | MAE old sim | MAE plain recent average |
|---|---|---|---|
| QB | 7.70 | 9.20 | 8.32 |
| K | 4.22 | 4.23 | 4.40 |
| RB | 5.12 | 4.52 | 4.78 |
| WR | 4.70 | 4.42 | 4.63 |
| TE | 4.11 | 3.85 | 3.95 |

Best two-way blends: QB 7.70, K 4.21, RB 4.50, WR 4.40, TE 3.83. Verdict: the play sim wins at QB (7% under the plain average, rank corr
0.35 vs 0.28), is level at K, and trails the old sim at RB/WR/TE. Its player predictions are over-spread (slope about 0.7 of actual on
predicted): "active" players do not all get full workloads (limited, hurt mid-game). Without the known-active list every method under-predicts
(injured players hold shares), which is why the injury file matters. Share window (8 to 30 games), per-player efficiency factors and red-zone
shares were each tested and do not change the slope.

## Signal tests (market-relative, scripts in `scripts\`)
- `scheme_signal.py` (participation + FTN charting, train 2023-24, test 2025): personnel/formation/motion/play action/screen/RPO plus box
  count, rushers, blitzers, man/zone and coverage cut pass completion log-loss 0.6445 to 0.6300 (-2.2%), but pass yards 9.243 to 9.223 and
  run yards 6.138 to 6.105 barely move. Scheme mostly changes completion odds, not yardage. Data: participation exists for 2023-2025 only
  (not 2026), FTN charting 2022-2026. Downloaded to `data\nfl\pbp_participation\` and `data\nfl\ftn_charting\`. Not wired into the engine.
- `weather_signal.py`: at play level, wind/temp/roof/surface add nothing (+0.0% to the error). At game level the market under-prices
  wind: 649 outdoor games with wind >= 15 mph (1999-2026) scored 2.1 points below the closing total (t -3.7); under 54-58% in every era,
  55% since 2015 (216 games). Flag for totals, passing and kickers; not wired into the engine.
- `coach_h2h_signal.py`: the same two head coaches' earlier meetings do not predict the next game against the closing spread (3,686 games,
  coefficient -0.03, t -1.1), and a coach's record against the spread does not persist season to season (corr +0.03). No head-to-head edge.

## Phase 3 (2026-10-22): defenders (IDP)
- `player_layer.DefenseModel(pbp, as_of, team, avail, active)`: per defense, recency-weighted shares by event (run tackles, completion tackles,
  sack tackles, assists, sacks incl. half sacks, pass breakups, interceptions, forced fumbles, fumble recoveries) from play-by-play defender
  ids. League event-count distributions per play context (how many solo tackles and assists a run, completion or sack produces; breakup
  rates). `sim_game(..., dm=(home_defense, away_defense))` then credits IRFL points (solo 1, assist 0.5, sack 3, INT 3, PD 1, FF 2, FR 2,
  defensive TD 6) on every simulated play, so a defender's output follows the opponent's run/pass volume, injuries and availability.
- Data on disk that feeds it: pbp defender columns (2023-2026), `stats_player` box scores, `snap_counts`. Participation (who is on the field per
  play, coverage, rushers) exists for 2023-2025 only and is NOT used yet; PFR defense (targets/yards allowed, pressures, missed tackles) exists
  for 2018-2026 on the release but only 2026 is downloaded and it is NOT used yet.
- Backtest (known-active, 8,746 defender-weeks, same rules): MAE DL 1.85 / LB 2.47 / DB 2.27 for the play sim against 1.71 / 2.23 / 2.05 for the
  old sim and 1.71 / 2.23 / 2.05 for the plain recent average. Rank correlation DL 0.313 (avg 0.301), LB 0.490 (0.522), DB 0.413 (0.423).
  Calibration slope of actual on predicted is 0.42 to 0.50 (over-spread), against 0.69 to 0.77 for the plain average.
  Best three-way blend fitted on the first half of the weeks and scored on the second half: DL 1.727 vs 1.707 average, LB 2.233 vs 2.241,
  DB 2.093 vs 2.111. **Verdict: no defender method, old or new, beats a plain recent average by anything real at the player-week level;
  defender points are mostly noise. Use the old sim or the plain average for IDP, the play sim is for what-if (a teammate out, a matchup).**
- Week 7 rosters: both sims agree on Zac's IDP lineup (no change). Blend weights for DL/LB/DB stay 0 on the new sim in `run_week_play.py`.

## Not done yet
- NGS-based player ratings, a scheme-conditioned completion layer, a wind adjustment, participation/PFR-based defender roles.
- Totals are still about 1.3 points per team light (see the known gap above).
