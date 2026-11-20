# DraftKings Week 11: Own-Numbers Runbook (v2)

Early games only, 7 lineups at $1. Written 2026-11-19. Decision support only: Zac enters, Zac pays, Zac uploads. No agent logs in to DraftKings. This replaces the Saturday and Sunday steps in the 2026-11-19 Explainer and Runbook (that file is kept). The friend's-file mode still works if he ever sends a file again.

This document holds method and checks only. Player salaries, ownership numbers and lineups stay in `D:\Draft Kings\` (outside the repo).

## What changed since v1 (5 lines)

1. The builder now runs on OUR numbers: our simulator's projections and our own ownership ESTIMATE. No friend file is needed this week.
2. Two rule fixes so the build matches the friend's notes exactly: at least 5 chalk-pool players in EVERY lineup (v1 allowed 4 and 3), and the bring-back line is the slate's middle game total (v1 also had a 44-point floor of ours).
3. Bug fixed: when no stored lineup fit the caps, v1 dropped the exposure caps (a test put one player in 7 of 7 lineups). Now it solves new lineups with the caps built in, and the checker tests the caps on its own.
4. The simulator's default starting QB now follows the most recent starter. Without the overrides file it now picks Cousins, McCarthy and Milton (it used to pick Wentz, Winston and McKee).
5. New one-line command, `dk_own_build.py`: refresh, re-sim, projections, ownership, lineups, checks.

## Part 1. Data refresh done this morning (Thursday 2026-11-19, Eastern time)

| Source | Pulled | Freshness |
|---|---|---|
| nflverse play-by-play and player stats 2026 | 8:01 AM | nflverse files updated 10:03 and 10:04 UTC today. Stats now run through **Week 10** (they stopped at Week 9 in the v1 build). |
| nflverse players and schedules | 8:01 AM | refreshed |
| Odds API, NFL and college lines | 8:01 AM | 29 NFL games. Early-game lines unchanged from the 7:10 AM pull. |
| MFL roster, saved starters, injuries | 8:02 AM | pulled with `mfl_roster_pull.py` |
| Merged injury file (MFL, nflverse rosters, ESPN injuries, ESPN transactions) | 8:03 AM | newest nflverse roster 07:09 UTC, ESPN injury feed 13:02 UTC (8:02 AM ET). Thursday practice reports were **not out yet**. |
| Simulator rerun, 20,000 sims per game | 8:05 AM | `run_week.py` and `full_week.py`, Week 11 |

**Starting QBs on the 14 early-slate teams, each from a dated source** (kept in `D:\Draft Kings\Week 11\qbs_confirmed_week11.json`):

| Team | Starter | Source and date |
|---|---|---|
| MIA | Kyle McCord | RotoBaller 11/16, SI starting-QB page 11/11 (Willis on IR). No team statement for Week 11 found. |
| BUF | Josh Allen | SI starting-QB page 11/11, no injury tag 11/19 |
| NO | Tyler Shough | SI 11/11, no tag 11/19 |
| CHI | Caleb Williams | SI 11/11, no tag 11/19 |
| TEN | Cam Ward | SI 11/11, no tag 11/19 |
| DAL | Dak Prescott | SI 11/11, no tag 11/19 |
| TB | **UNCONFIRMED** | Bay News 9 11/16: Baker Mayfield foot sprain, in and out of a walking boot; Jalon Daniels would make his 4th start. MFL feed 11/19: Mayfield Questionable, did not practice Wednesday. Our sim plays Mayfield in 40 percent of games, Daniels in the rest. |
| DET | Jared Goff | SI 11/11, Fox Sports Week 11 page, no tag 11/19 |
| ARI | Carson Beck | azfamily 11/12 and ClutchPoints (Minshew on IR) |
| KC | Patrick Mahomes | SI 11/11, no tag 11/19. One search snippet mentioned ACL surgery, most likely an older page. Recheck Sunday. |
| PIT | Aaron Rodgers | SI 11/11, no tag 11/19 |
| PHI | Joe Milton III | Sirianni announced 11/18 (profootballrumors, Yahoo). Hurts out for the season. |
| BAL | Jacoby Brissett | NBC Sports 11/13: Lamar Jackson out 6 to 10 weeks |
| CAR | Bryce Young | SI 11/11, no tag 11/19 |

The TB QB fails the gate's "confirmed starter" test until the Sunday inactives. The SI page is dated 11/11, so for the nine teams that lean on it, "confirmed" means no change reported since then and no injury tag today.

**QB-picking fix in the simulator.** Before: with no overrides entry, the team's QB was the one with the most pass attempts over the last 14 team games. After: the QB who threw 10 or more passes in the team's most recent game goes first. Tested on all 26 Week 11 teams with the overrides switched off: the new rule matches every named starter (MIN Cousins, NYG McCarthy, PHI Milton, BAL Brissett), where the old rule missed three. The six simulator tests still pass. The overrides file still wins when it names a starter. The rule cannot see a mid-week benching or a new injury on its own, which is why the dated QB list stays a required step.

## Part 2. What own-numbers mode is, in plain words

- **Projections:** our simulator plays every game 20,000 times with the live betting line, each coach's habits, injuries and recent usage. Each player's range comes straight from those games: `dk_25`, `dk_50`, `dk_75`, `dk_85`, `dk_95`, `dk_99` percentiles, plus mean and spread. That is the same percentile set the friend's file has, so the builder uses it the same way.
- **Defenses:** our simulator had no team-defense scoring, so `own_proj.py` now scores each defense on DK rules from the same simulated games (sacks, interceptions, fumbles, points allowed). Defensive and return touchdowns and safeties use typical league rates. That part is our assumption.
- **Vegas numbers:** team implied total and game total come from our own Odds API pull.
- **Status:** Q, D and Out tags from our merged injury file. Out and Doubtful are removed. Q stays in and is flagged.
- **Ownership:** our own ESTIMATE, see Part 3. Every ownership number in the outputs is labeled ESTIMATE.

## Part 3. Our ownership estimate (option A)

**How it works.** Every DK lineup has 1 QB, 1 DST and 7 RB, WR and TE. So the field's ownership has a fixed budget per position: 100 percent at QB and at DST, and about 230 RB, 339 WR and 131 TE percent (the FLEX split, taken from the Week 10 reference file as a slate-level constant). Inside each position the budget is shared out by a popularity score built from: value (our points per $1,000), our projection, our ceiling (dk_95), the team's implied total, the game total, salary and a Q tag. For a defense, the opponent's implied total counts (lower is more popular). Recent usage and news come in through our projection. Slate size comes in through the budget: 7 games share the same 100 percent, so the top plays get more. Each factor is ranked inside its position, which beat raw z-scores in the backtest (z-scores let one star soak up the budget). Fit by least squares with a small penalty. Script `dk_own.py`, coefficients in `dk_own_params_full.json`. A no-salary version (`dk_own_params_nosal.json`) gives rough numbers before DK salaries are out.

**Backtest on Week 10** (7 early games, 218 of our players matched to DK IDs). The reference is the friend's `My Own` column, which is **his projected ownership, not real ownership**. Real DK ownership needs a login, so it was not retrieved. His column was used only to fit and score the model. It is not an input at Week 11.

| Test | Rank correlation (Spearman) | Mean miss, all players | Mean miss, players he had at 5%+ (54) |
|---|---|---|---|
| Fit on all 7 games (optimistic) | 0.824 | 1.56 points of ownership | 3.94 |
| **Leave one game out (honest)** | **0.814** | **1.95** | **5.26** |
| No-salary version, leave one game out | 0.790 | 2.48 | 6.55 |
| First try (z-scores), leave one game out, rejected | 0.830 | 2.68 | 7.25 |

By position (leave one game out): QB 0.852, RB 0.834, WR 0.845, TE 0.832, DST 0.666. 11 of his top 15 are in our top 15. Top-6 chalk pool overlap: RB 6 of 6, WR 3 of 6, TE 4 of 6. The low-owned QB list (under 15 percent) matches his except for two QBs, one each way.

**Second check, a free public source:** Fantasy Alarm's Week 10 ownership article (published 2026-11-13, retrieved 2026-11-19 about 8:20 AM ET, free page). It covers the 10-game MAIN slate, not the early slate, so only the ranks compare. On the 17 early-slate players it lists, the friend's numbers rank-matched Fantasy Alarm at 0.895. Ours matched at 0.547. Ours is clearly the weakest of the three.

**Where it is rough (read before trusting it):**
1. **Defenses** are the weakest part (rank 0.67, average miss about 5.5 points). Two popular Week 10 defenses came out near zero in ours.
2. **Cheap backups who just took over a starting job.** The field chases them, but our projection can lag on a role change, so we undercount them.
3. **Players our projection likes more or less than the public does.** The field follows public projections, ours follows our sim. Where those differ, our ownership follows ours and is wrong. This is the main reason we trail Fantasy Alarm.
4. **One week of fitting data, 218 players.** The FLEX split and the coefficients come from Week 10 only. Treat every number as a range of plus or minus 5 points for anyone over 10 percent.
5. **Week 11 so far uses the no-salary version only.** DK salaries arrive Saturday. The full model runs then.

**Week 11 public ownership check:** no free Week 11 ownership numbers were found Thursday morning. RotoGrinders' ownership table needs a paid plan (not used). The Fantasy Alarm article for Week 10 came out Friday, so check `fantasyalarm.com` NFL DFS ownership articles Saturday. Use it as a sanity check on our top 15 only, and only for early-slate players.

**What the estimate drives in the build:** the chalk pool (top 6 by ownership at RB, WR and TE), the low-owned QB gate (under 15 percent), the leverage caps (ownership sums), and the duplicate estimate. A miss on a borderline player can move him in or out of the chalk pool, so the build report lists every pool player.

## Part 4. The friend's rules, as built (DK only, never IRFL)

Checked against his notes (`DFS-Friend-Process-1-of-3-2026-11-13.md`, parts 1 and 3):

| His rule | In the builder |
|---|---|
| Chalk pool: top 6 RB, WR, TE by projected ownership, plus any top 6 by projection | Same. Every lineup needs at least 5 from the pool (fixed in v2) |
| No QB under $5,000 | Hard limit |
| A low-owned QB must pass the gate: confirmed starter, implied total 21+, top-12 ceiling, defense outside the top 8 | Every lineup. Low-owned means under 15 percent (our line). Confirmed starter means named in the dated QB list. Defense rank = DK points allowed to QBs, from nflverse through Week 10. |
| Pair the QB with his receivers | Core and leverage: QB plus 2 receivers. Balanced: QB plus 1. |
| Bring-back in a high-scoring game, never 3 or more | Required when the game total is at or above the slate middle (median). At most 2 (fixed in v2). |
| Caps, not locks | Nobody is forced in. Leverage comes from ownership caps (sums of 200, 160 and 135 percent by tier) and at least 2 players under 10 percent in leverage lineups. |
| Portfolio caps (Jarvis's brief) | A player in at most 4 of 7, a QB in at most 2, any two lineups share at most 5 players, 7 different lineups, $50,000 cap, early games only |

Our own additions, not his: no more than 4 offensive players from one team, no defense facing our own players, the tie-in weights in the simulation, the duplicate estimate.

## Part 5. Week 10 dry run in own-numbers mode

Folder `D:\Draft Kings\Week 10\dryrun-own\`. Inputs: our Week 10 simulator draws made before the games (2026-11-12), defenses re-simulated from the same pre-game inputs, and the ownership estimate from the **leave-one-game-out** fit (so no game's ownership was fitted on itself). DK IDs and salaries from the Week 10 DK salary file. Mock 7-entry template with fake entry IDs.

- **Build:** 7 lineups, 4 QBs (each used at most twice), 36 players, the most-used player in 4 of 7, any two lineups share at most 5. Validation PASS on both files, including the new independent portfolio checks (exposure 4, QB 2, overlap 5, QB salary, bring-backs). One leverage slot had no stored lineup that fit the caps; the builder solved 24 new ones with the caps built in and picked one. Our model's own number: at least one of the 7 beat the top-1 percent line in 20.1 percent of 20,000 simulated Sundays (a model number, not a win rate).
- **Real Week 10 points** (DK scoring computed from nflverse stats pulled today. Defense points-allowed uses the plain final score, a small approximation):

| Lineup set | Best | Average | Notes |
|---|---|---|---|
| Own-numbers mode (new) | 136.7 | 118.9 | 2 lineups had a RB with no Week 10 stat line (likely did not play). Our Thursday injury file had him healthy. |
| Friend-file mode, v2 rules (same builder) | 151.7 | 104.9 | |
| Friend-file mode, v1 rules (first build) | 163.5 | 128.8 | |
| The friend's own 3 lineups | 141.6 | 119.7 | |
| The 3 lineups in `entries ... (1).csv` (who built them is not recorded) | 203.4 | 141.0 | |

- **How the own-numbers lineups differ from the friend-file lineups:** none of the 7 is the same lineup. They share 25 players. Ours used 36 players, his-file mode 41. Ours leaned on cheaper receivers and defenses our sim liked. His-file mode carried more of the popular RBs and the field's favorite defenses. The own-numbers average beat friend-file v2 by 14 points, but trailed v1 by 10 points and the friend's own three by 1. **One week is noise.** No cash line or contest results were retrieved, so none of these can be called a win or a loss.
- **Lesson:** a Q player who sits on Sunday costs a whole lineup. The Sunday 11:30 AM rebuild with `--out` is not optional.

## Part 6. Runbook (all times ET)

**Who runs what.** Zac drops two files. Jarvis runs the build and reads the report. Zac uploads and enters. Nothing on DraftKings is done by an agent.

**Saturday 11/21**
1. **Zac, on DraftKings (spends $7):** open the early-only contest, enter 7 times at $1 with any legal lineup (DK quick fill is fine, it gets replaced). Check: 7 entries, $7.
2. **Zac:** download the entries template (Lineups, Edit Entries, Download) and the salary file (contest page, Export to CSV). Save both into `D:\Draft Kings\Week 11\`. Tell Jarvis "DK files are in".
3. **Jarvis: refresh first, then build.** One command (it refreshes nflverse, odds, MFL and injuries, prints the starting-QB check, re-sims at 20,000, builds projections, ownership and lineups, and runs the checks):
   `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I D:\WKP\Fantasy-Football\dfs\dk_own_build.py --week 11 --dk-salaries "D:\Draft Kings\Week 11\<DKSalaries file>.csv" --template "D:\Draft Kings\Week 11\<entries file>.csv" --outdir "D:\Draft Kings\Week 11\sat"`
4. **Jarvis, before trusting the build:** (a) read the QB check lines. If any team's default QB is wrong, add that team to the `qbs` block in `D:\WKP\data\ff-simulator\overrides_2026_wk11.json` and to `qbs_confirmed_week11.json`, then rerun with `--no-refresh`. (b) Search Friday's final injury reports (Out, Doubtful, Questionable) for every player in the 7 lineups and note each one with its date. (c) Look at the own-numbers log lines: DK players with no projection, and sim players not found in the DK file. (d) Check Fantasy Alarm (or another free ownership page) for early-slate players. If one of our top-15 ownership numbers is off by more than 15 points, say so in the report to Zac. Do not hand-edit the estimate.
5. **Both checks in `build_report.txt` must say RESULT: PASS.** Then Jarvis sends Zac the 7 lineups with a one-line status on every player.
6. **Zac uploads** the file ending in `- FILLED.csv` (Lineups, Edit Entries, Upload) and confirms all 7 entries show the new lineups.

**Sunday 11/22**
1. **10:00 to 11:00 AM:** morning news for game-time decisions, mostly the TB QB and every Q player in our lineups.
2. **11:30 AM, inactives drop.** RotoWire lineups page or team accounts. List every inactive in our 7 lineups.
3. **11:35 AM to 12:15 PM, final rebuild (Jarvis).** Zac downloads a fresh entries template (same entry IDs). Jarvis updates the TB line in `qbs_confirmed_week11.json` (and the overrides file if Daniels starts), then runs the same command with `--outdir "D:\Draft Kings\Week 11\sun"` plus `--out "Name One;Name Two"` for the inactives. Add `--drop-q` if any Q player is still unclear. The refresh runs again by default, which is the rule. For one or two swaps only, editing those players by hand on DK is fine.
4. **By 12:30 PM:** both checks PASS, Zac uploads, confirms 7 lineups.
5. **12:45 PM: stop.** No more rebuilding (the friend's rule). Lock is 1:00 PM.

**Monday:** Zac sends the final results (score per lineup, finish, cash line, winnings). Jarvis runs `dk_actual.py` for real points and logs the projected-versus-real ownership if a free source has it.

## Part 7. Open questions for Zac

1. **TB QB:** if Mayfield is still unclear Sunday morning, leave TB QBs out of the 7 (the gate already blocks them as low-owned), or allow Mayfield if he is active at 11:30?
2. **Contest:** all 7 in one $1 early-only contest (Week 10 was the $15K First Down, 20 entry max), or split them the way the friend advises?
3. **Real ownership:** DK shows the real percent drafted on the contest page after lock. A screenshot Monday would let us fit the model on REAL ownership instead of the friend's projection. Worth doing every week?
4. **Week 10 entries:** the file `entries ... (1).csv` holds 3 lineups that scored 115, 203 and 104 by our count. Were those the ones you entered, and how did they finish?

## Files

- Scripts (repo, method only): `D:\WKP\Fantasy-Football\dfs\` `dk_own_build.py` (one command), `own_proj.py` (our projections, DST, IDs), `dk_own.py` (ownership estimate), `dk_gpp.py` (builder, `--own` or `--friend`), `dk_validate.py` (checks), `dk_actual.py` (real points after games), `qb_check.py` (default QB versus named starters), `mfl_roster_pull.py`, coefficient files `dk_own_params_full.json` and `dk_own_params_nosal.json`.
- Simulator change: `D:\WKP\.claude\skills\ff-simulator\scripts\simulate.py` (`qb_order`, `last_att`).
- Player data (outside repo): `D:\Draft Kings\Week 10\dryrun-own\` (dry run, backtest, comparison), `D:\Draft Kings\Week 10\dryrun-friend-v2\` (friend-file mode under v2 rules), `D:\Draft Kings\Week 11\` (QB list, preliminary no-salary projections and ownership, smoke test on FAKE salaries in `smoketest_FAKE\`, never upload from it).

## Notes and limits

- The ownership numbers are estimates fitted on another person's projection for one week. They are not measured ownership.
- The Week 10 dry-run scores are one slate. They do not show that either mode is better.
- Defense scoring in our projections and in `dk_actual.py` uses simplified rules (stated in each script).
- This run: Opus 5.5, ff-simulator 20,000 sims per game (seed 2026), builder 20,000 correlated slates (seed 11), 120 solves per tier.

