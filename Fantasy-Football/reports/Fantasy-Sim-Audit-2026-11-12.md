# Fantasy Sim Audit, 12 NOV 2026

Hard review of everything built for the IRFL lineup and the pick'em card. Decision support only. Nothing was submitted, nothing was committed to git, no money was spent.

## The short version

1. **The sim could not see trades.** That is why last night's doc called Jordan Davis a bye. He was traded to Jacksonville on 11/10 and plays Sunday. Fixed.
2. **The weekly report script still had Week 6 text and Week 6 file defaults in it.** The Week 9 and Week 10 reports both shipped a paragraph about the Rams being 83.7 percent in the Eliminator. That was October. Fixed.
3. **A Questionable quarterback was shown as if he were sure to play.** Goff read 21.3 last night. With his chance of sitting counted, it is 16.6. Fixed.
4. **The pick'em card is a coin flip on most games, and the math agrees.** Model record weeks 6 to 9: 40 of 80 against the spread. The real edge is the 2 or 3 games a week where the market moved 2 points or more off the card.
5. **Run to run noise is small.** About 0.07 points per player at 4,000 sims. Nothing flipped last night to today because of dice. The changes are real news and real bug fixes.

Eight fixes were applied (all backed up, all tested). Nine bigger changes are proposed, not applied. Details below.

## What I ran

- Read every script in `ff-simulator`, `ff-play-sim` run scripts, `nfl-data`, `fantasy-football-data`, the tracker, the 11/10 fixes folder, the director spec, the venture CLAUDE.md and last night's working files in `scratch\ff10`.
- Rebuilt last night's run from its own inputs, then changed one thing at a time (code, injuries, overrides, odds, seed, sim count) to see what each one moved.
- Checked the sim's assumptions against 2,639 real games (nflverse schedules, 2016 to 2025).
- Tests: tracker 10 of 10 pass. New simulator tests 6 of 6 pass. Before today the simulator had no tests.

**Not audited in depth:** the insides of `play_engine.py` (the snap by snap engine), `coach_model.py`, `dfs_optimize.py`, the Sunday dashboard and `grader.py`. I read how they are called, not every line.

## Findings, ranked by expected impact

### 1. Trades were invisible. FIXED.

**What.** Three separate holes lined up.

- The injury builder gave every record it could not match the same bogus player id. 8,395 players in the nflverse file have no ESPN id, and the code turned all of those blanks into one key. Result: 109 records from 99 different players collapsed into one row on Wednesday (91 records today before the fix). Jordan Davis's trade line was one of them.
- The transaction reader treated "Acquired a draft pick from San Francisco for WR Keenan Allen" as Allen SIGNING with the Colts. It could not tell who came and who left.
- Both simulators only know a player from games he played for that team. A player on a new team got no number at all, and the report filed him under "bye, no team, or no usage".

**Evidence.** Last night's lineup doc: "Jordan Davis (PHI DT), Philadelphia is on bye, replace with Wonnum." ESPN transaction dated 11/10: "Acquired DT Jordan Davis from Philadelphia for a 2027 first-round draft pick." Last night Cousins and Allen were moved by hand editing the injury file, with no log entry.

**Fix applied.** The id bug is closed. The transaction reader now knows arrivals from departures and found all 10 trades in the feed today with no hand edits (Davis, Brissett, Cousins, Allen, Downs, Hooker, Henley, Bates, Cisco, Godchaux). A defender who changes teams is now simulated on the new team with his own tackle and sack rates. A quarterback who changes teams can be named the starter. A runner or receiver who changes teams is NOT guessed: he is listed by name as "changed teams, not simulated".

**Impact.** A healthy starter benched this week. In another week this is a WR1 or a QB. High.

**Still open (proposed).** A share model for runners and receivers on a new team (Keenan Allen at SF, Josh Downs at KC have no number). Effort: half a day plus a backtest.

### 2. The report script carried Week 6 leftovers. FIXED.

**What.** `full_week.py` printed a fixed title ("15 OCT 2026"), a fixed Eliminator paragraph ("LA Rams 83.7 percent, KC 73.5 percent"), "Golden active" and "when the two free agents land I will add them for Week 7" in every report since October. It also did not tell the simulator about current teams, so the report's box scores kept traded players on old teams. Five scripts fell back to the Week 6 or Week 7 odds and roster files when a flag was left off, without a word. `wait_and_run.py` ran the lineup step on the Week 6 roster every time it was used.

**Evidence.** `Week10-Full-Simulation-2026-11-11-wed.md` lines 62, 87, 89, 190. `Week9-Full-Simulation-2026-11-05-thu.md` line 241. Last night's lineup doc quoted "Allen 9.7 on the stale IND sim".

**Fix applied.** Title and Eliminator line are computed from this week's numbers. Old sentences removed. Odds, roster and output path are now required, so a missing flag stops the script. An odds file older than 24 hours prints a warning. Current teams are passed in.

**Impact.** Wrong text went to Zac twice. A wrong roster file could have produced a wrong lineup with no error. High.

### 3. A Questionable quarterback was counted as certain. FIXED.

**What.** The play by play sim carries 90 percent of the quarterback blend. It played a Questionable quarterback in every simulated game. The older sim sits him 25 percent of the time. So the blend ignored most of the risk. Also: the hand-entered facts file (overrides) was read by the old sim only, and neither sim could be told who is starting at quarterback.

**Evidence.** Goff last night: 21.3. Today, same inputs, with the sit chance counted: 16.6. The play sim had Fagnano at quarterback for Baltimore and Brosmer for Minnesota. It had Shedeur Sanders starting for Cleveland at 16.6 because ESPN's status field still says Watson is Out, while ESPN's own note says the Browns named Watson the starter.

**Fix applied.** The quarterback's play chance is applied in the play sim. The overrides file now feeds both sims. A new "qbs" block names the starter by team (used this week for BAL, MIN, LV, ARI, MIA, SEA, CLE).

**Impact.** 4.7 points on the lineup total this week. It could flip a quarterback call any week the backup option is within 5 points. Medium to high.

### 4. Every Questionable player gets the same 75 percent. PROPOSED.

**What.** The sim plays every Questionable at 75 percent. Your own 11/10 study says that is wrong in both directions: Questionable who missed Wednesday practice scored zero 53 to 67 percent of the time, Questionable who was limited scored zero 13 to 38 percent. Rule 4 fixes the first group by hand (times 0.55) and leaves the second alone. It is applied by a person reading notes, so it can be missed. Last night Okereke's Wednesday status was "unconfirmed" and he went out at full value. He did not practice.

**Fix proposed.** The injury file now has a practice column (added today, no behavior change). Use it: Questionable and no practice, play chance 0.40. Questionable and limited or full, 0.85. Rule 4 is locked by Zac, so this is queued as FF-2026-11-12-01, not applied. Effort: 1 hour plus a rerun of the 11/10 backtest.

**Impact.** 2 to 5 points on each affected starter. Most weeks have 1 to 3 of them. Medium to high.

### 5. Pick'em: honest numbers, and one weak spot in the math. PROPOSED.

**What the record says.** Model picks, weeks 6 to 9: 40 of 80 against the spread (50.0 percent). Straight up: 41 of 57. Picks with 2 or more points of line value: 6 of 10. Coin flip games (under 1 point either way): 13 of 33. Samples are small. Nothing here beats the 62 percent long run claim, and nothing here says the labels are wrong.

**Weak spot.** The label percentage uses a smooth curve. Real football scores bunch on 3, 7 and 10. Checked against real games with a closing line in the same band:

| This week's pick | Label says | Real games | Sample |
|---|---|---|---|
| Seattle -3.5 (market -6.5) | 59.0% | 63.3% | 390 |
| LA Rams -7.5 (market -9.5) | 56.0% | 49.2% | 120 |
| Jacksonville -9.5 (market -10.5) | 53.0% | 49.3% | 142 |
| Indianapolis -2.5 (market -4) | 54.5% | 58.1% | 470 |
| New Orleans -1.5 (market -2.5) | 53.0% | 55.8% | 706 |
| LA Chargers +5.5 (market BAL -4.5) | 53.0% | 56.5% | 253 |

Read: Seattle is a better edge than the label says. The Rams lean is softer than it looks (small sample, so do not flip it). Big favorites laying 9 or more have covered a stale line less often than the curve predicts.

**Fix proposed.** Blend the curve with the real-game table by line band. Effort: 2 hours. Queued as FF-2026-11-12-02.

**Also found.** Last night's straight-up side was tilted 15 percent toward the play sim's score. That sim adds nothing beyond the market (its own backtest: coefficient 0.18, error 0.19) and it had the wrong quarterbacks. Today I used the market alone. No straight-up pick changed. Recommend dropping the tilt for good.

**The bad "closing line" (FF-2026-11-10-01).** I compared the local schedule file to the live nflverse copy today. They match. The plus 3.0 on JAX at BAL in Week 9 is nflverse's own error, not ours. Option A in that decision is still right.

**Tiebreaker rule.** "Shade the Monday total under" has thin support: Monday games since 2016 land 1.0 point under the total, give or take 0.9 (187 games). Games with a total of 40 or less land 0.8 over. Use the market total and round down a half. That is what 38 is.

### 6. One stream of dice for the whole week. FIXED.

**What.** All games shared one random stream. A roster change in the first game changed the dice for every later game, so two runs differed everywhere, a little.

**Evidence, measured today.** Same inputs, different seed, 4,000 sims: per-player average moves 0.07 points (95 percent of players under 0.17, quarterbacks about 0.2). Lineup total moves about 0.5. That is far smaller than the model's own error (about 4 points a player).

**Fix applied.** Each game has its own fixed stream. An untouched game now gives the same numbers run to run (tested). The official run uses 20,000 sims and takes 12 seconds.

**Ties.** When two players are within 0.3 points, the sim cannot separate them. Use this order: (1) the one with no injury tag, (2) the one that covers another risk in the lineup (Dodson behind Okereke), (3) the one already saved on MFL, fewer clicks.

**Impact.** Low on its own. It removes "was that the dice?" from every Thursday comparison.

### 7. Ranges are built on a game total that is too tight. PROPOSED (one part FIXED).

**What.** The sim spreads each game's total points with a standard deviation of 9.0. Real games: 13.2 (2,639 games). Margin is fine (13.2 used, 12.7 real). An earlier patch widens offensive players by 1.3 to cover it.

**Fixed part.** Kickers were drawn twice (team field goals, then the kicker's share of a number that was already random). Sim kicker spread was 7.7 points, real is 4.35 (30 kickers, 2026). Now 6.3. The average did not change.

**Proposed.** Set the total spread to 13.2 and refit the 1.3 patch with the existing backtest. This changes ranges, SAFE and SWING lineups and DFS ceilings. It does not change averages or the EXPECTED lineup. Effort: 2 hours.

### 8. Two calibration numbers disagree. PROPOSED.

**What.** The 11/10 report says player projections are unbiased (plus 0.08 a player). The same report says whole lineups score 13.6 points above the sim. I split it: lineups with every starter projected still run 16.4 over (20 lineups, give or take 6.4). Both cannot be true.

**Why it matters.** The headline lineup total is probably about 14 low. Head to head odds are not affected, both teams get the same lift.

**Proposed.** One reconciliation run: sum the same players both ways. My guesses, not verified: the player table drops everyone projected under 3 points and about 12 percent of unmatched players, and managers start Questionable players who end up playing. Effort: 1 hour.

### 9. No head to head, and the optimizer and the report use different numbers. PROPOSED.

**What.** The optimizer picks the lineup on the old sim. The report shows the blend. Last night's doc declined to quote a win chance at all.

**Done today in scratch.** Scored your final 17 against the opponent's saved 17 on the same simulated games: about 53 percent. MFL showed a 26 point edge on stale lineups.

**Proposed.** Add `--opp` and `--blend` to `optimize.py`. Effort: 2 hours.

### 10. Data freshness and fragile inputs. PARTLY FIXED.

- `players.parquet` (the id bridge) was 2 weeks old. Refreshed today. The documented run order only refreshes play by play and stats. Add players and schedules. (Doc updated.)
- The age stamp on the players and schedules files says 10/22 even right after a fresh download. The stamp comes from a stale manifest. The data is current, the label is wrong, so the "state the file age" rule is checking a broken clock. Fix: run `nfl_data.py discover` before `get`. Not applied.
- nflverse's roster file trails real moves by a day or more. It had Nick Folk active the morning after he was waived. FIXED: a release or IR move in the last 60 hours beats it.
- ESPN's status field was wrong for two quarterbacks today (Watson, O'Connell). Its dated notes were right. Handled with the overrides file. There was no overrides file for Week 10 last night.
- MFL's team tag was 2 days behind on Davis. Today I checked every rostered player's team against ESPN's athlete page (one-off). Propose wiring that in.
- Snap counts on disk are from 10/21. They only feed the offensive line layer, which is off.
- The CFBD key is set for the user but a session that was already open cannot see it. Today's run read it from the registry in code. It was not printed or saved.

### 11. Weather is a rule with no tool. PROPOSED.

Your 10/22 rule: flag wind, rain and snow for every outdoor game. No script pulls weather. Last night's doc said "not checked". Today I pulled kickoff forecasts by hand (Open-Meteo, free, no key). Tonight has gusts to 28 mph and a 52 percent chance of rain. Propose a small `weather.py`. Effort: 30 minutes.

### 12. College games. PROPOSED.

`cfb_snapshot.py` reads ESPN only (one book). It does not use the CFBD key. Today's card labels use the Odds API 9-book median, which is the better number. CFBD worked (HTTP 200, 993 calls left) and agreed with ESPN on all six card games. Propose adding the CFBD lines call to the snapshot for a second book and the opening line. Injuries and quarterbacks for college: still not available from any feed we have.

### 13. Tracker gaps.

Weeks 2 to 5 are not in `predictions.csv`. The files to backfill Weeks 2, 3 and 5 exist (model doc and both of Zac's cards in `D:\Documents\Pickups 2026\`). There is no Week 4 folder. I did not backfill today: the time before lock went to the run, and those weeks have no saved market pull, so they add wins and losses but no edge data. Effort: about 1 hour. Queued as FF-2026-11-12-03.

### 14. Documentation drift. NOT CHANGED (not mine to edit).

- The director spec still says MFL blocks player scores and to ask for a screenshot in Recap Mode. The 11/10 work uses the MFL playerScores export, which works.
- Three different places are written down for the simulation report: the director spec, the ff-simulator skill, and where the files really land (`D:\WKP Reports\Fantasy Football\`, flat).
- The director's Card Mode does not mention the LEAN, SLIGHT, NO EDGE labels.

## What I changed (every file backed up first)

Backups: `D:\WKP\scratch\ff-audit-2026-11-12\<name>.orig`. Last night's outputs: `wed-outputs\` in the same folder.

| File | Change |
|---|---|
| `ff-simulator\scripts\build_injuries.py` | Bogus shared id closed. Trades read as arrivals and departures. Fresh release or IR beats the lagging roster file. New `practice` column. Trade list in the run report. |
| `ff-simulator\scripts\run_week.py` | One random stream per game. Players who changed teams. Named quarterbacks. `--odds` required. Stale odds warning. |
| `ff-simulator\scripts\simulate.py` | Named starter goes first at quarterback. Kicker double draw removed. |
| `ff-simulator\scripts\full_week.py` | Week 6 text removed. Current teams and named quarterbacks passed in. Flags required. Optional `--sheet`. |
| `ff-simulator\scripts\optimize.py`, `pickem_probs.py`, `wait_and_run.py` | No more Week 6 defaults. |
| `ff-play-sim\scripts\run_week_play.py` | Named quarterbacks. Overrides applied. Questionable quarterback risk counted. Fixed seed per game. `--roster` required. |
| `ff-simulator\scripts\test_sim_fixes.py` | NEW. 6 tests. |
| `data\ff-simulator\overrides_2026_wk10.json` | NEW. Watson and O'Connell status, 7 named quarterbacks, each with its source. |
| `tracker\predictions.csv` | 2 rows added (`model_thu_rerun`). No row changed or removed. |
| Both SKILL.md files | Run order and new flags. |

**Tests.** `python -I test_sim_fixes.py`: 6 of 6 pass. Tracker `unittest`: 10 of 10 pass. `pytest` is not installed on this machine, so both run on the built-in runner.

## What each change did to this week's numbers

Old sim, your roster, one change at a time:

| Step | What moved |
|---|---|
| New code, last night's inputs | Brissett appears (13.9). Everything else within 0.5. |
| Different seed | Nothing over 0.3. |
| Today's injuries | Jordan Davis appears (3.1). Three Colts players move a point or more after the Allen and Downs trades. |
| Overrides (Watson starts, named quarterbacks) | Sanders 17.4 down to 1.4 (he is the backup). |
| Today's odds | Nothing over 0.1. Lines barely moved. |
| 20,000 sims | Nothing over 0.3. |

## Proposed, in the order I would do them

1. Play chance by practice status (finding 4). Needs Zac's yes, it changes rule 4.
2. Real-game cover table for the labels, and drop the play sim tilt (finding 5).
3. Head to head and one set of numbers in the optimizer (finding 9).
4. Reconcile the two calibration numbers (finding 8).
5. Total spread 13.2 and refit (finding 7).
6. Share model for traded runners and receivers (finding 1).
7. Weather script (finding 11). CFBD lines in the college snapshot (finding 12).
8. ESPN team check for every rostered player inside the injury builder (finding 10).
9. Tracker backfill, Weeks 2, 3, 5 (finding 13).

## Decisions queued

- FF-2026-11-12-01: play chance by practice status, replaces the hand-applied part of rule 4.
- FF-2026-11-12-02: real-game cover table for pick labels, and remove the play sim tilt.
- FF-2026-11-12-03: backfill tracker Weeks 2, 3 and 5.
- FF-2026-11-11-01 (Derrick Moore taxi promotion): no longer needed this week, Davis fills the spot. Left open for Zac to close.

---

# Round two, same day (afternoon): build the proposals, test each one, rerun

Asked for by Jarvis as a relayed instruction from Zac. Every model change below has a before and after number. Two ideas failed their test and were not adopted. Backups: `D:\WKP\scratch\ff-audit-2026-11-12\round2\orig\`. This morning's outputs: `round2\thu-am-outputs\` and `round2\am\`.

## What was built, and the proof for each

| # | Change | Before | After | Verdict |
|---|---|---|---|---|
| 1 | Questionable who did not practice plays 40 percent (was 75). Set in the injury file, automatic. | Error 65.2 | 64.0 (427 player-weeks, 3 seasons) | ADOPTED |
| 1b | Questionable who was limited or full plays 85 percent (my morning proposal) | 65.2 | 68.8 | REJECTED, it made things worse. Stays at 75. |
| 2 | Pick labels from real games with the same closing line, blended with the curve (`cover_table.py`) | Log loss 0.68090 | 0.67997 (19,304 cases, 2016 to 2025, walk forward) | ADOPTED |
| 2b | New HOOK rule for coin-flip games: take the table side at 53 percent or more, else the card underdog | Underdog rule 51.8% | Table side 54.1% (1,062 games) | ADOPTED. It flipped game 8 to Detroit. |
| 2c | Play sim tilt on straight-up picks | In a scratch script | Removed. Market alone now. | ADOPTED |
| 3 | `optimize.py --blend` (pick the lineup on the blend) and `--opp` (win chance against the opponent, same dice) | none | Works. 55.6 percent this week. | ADOPTED |
| 4 | Calibration puzzle (players unbiased, lineups 13.6 over) | unexplained | Solved, see below | NO CODE CHANGE |
| 5 | Game total spread 9.0 to 13.2, widen factor kept at 1.3 | Range coverage 79.5% | 80.0% (target 80). Error unchanged (4.77 to 4.78). | ADOPTED |
| 5b | Total spread 13.2 with a smaller widen factor (1.15 or 1.0) | 79.5% | 75.4% and 70.1% | REJECTED |
| 6 | Traded runner or receiver, first game on the new team: 0.6 of his old target share, 0.3 of his carries | No projection (share error 0.106) | Error 0.040 | ADOPTED, thin evidence (8 players). Always listed by name in the report. |
| 7 | `ff-play-sim\scripts\weather.py` | none | Kickoff forecast for every outdoor game. Flags wind 15, gusts 25, rain 50 percent, snow. | BUILT |
| 8 | CFBD wired into `cfb_snapshot.py`: lines from two books with the opening line, SP+, Elo, FPI | ESPN only | 5 calls a run. Key read from the user environment or registry, never printed or saved (tested). | BUILT |
| 9 | ESPN team check inside `build_injuries.py` for every player on the roster | none | Prints every disagreement. Changes nothing by itself. | BUILT |
| 10 | `dfs_optimize.py` week flag | Defaulted to Week 6 | Required | FIXED |

**Calibration puzzle, solved.** Whole lineups beat the sim by 13.5 points because the 17 starters each beat it by 0.79. All simulated players together are slightly OVER projected (minus 0.35). So the sim is not low. Managers start the players who end up beating their number: wide receivers plus 1.7 each (5.5 points a lineup), players projected 3 to 10 points plus 0.9 each, and 2.5 points a lineup from starters the sim had no number for. Nothing to shrink or lift. Head to head odds are unaffected, both teams get the same lift. A lineup total reads about 13 low against what lineups really score.

**Still wrong after the fix (new finding).** Player ranges are lopsided. Real scores land below the 10th percentile only 3 percent of the time and above the 90th 17 percent of the time. Both ends of the range sit too low. The proper fix is a skewed spread, not a symmetric one. Proposed, not built.

**Tests.** Simulator 6 of 6. Tracker and college snapshot 14 of 14 (4 new CFBD tests).

## Other prediction models: what was tested and what it showed

| Source | Free? | What it gives | Does it beat the market? | Used as |
|---|---|---|---|---|
| CFBD Elo (college) | Free key, 1,000 calls a month | Pregame Elo for every game, history included | No. 2025, 762 games: slope 0.05, error 0.09. Elo side covered 51.4 percent when it disagreed by 3 or more. | Sanity column only |
| CFBD SP+ and FPI (college) | Same key | Team ratings | Cannot be backtested. The API serves only the current number, not what it was before each past game. | Sanity column only |
| CFBD opening and closing lines (college) | Same key | Line history from two books | The card edge is real in college too: when the line moved 2 or more, the closing side covered the opening line 56.4 percent in 2024 and 53.3 in 2025. | Supports college labels |
| In-house NFL Elo (built today from nflverse results) | Free | Rating margin for every game | No. 2016 to 2025, 2,775 games: slope minus 0.01, error 0.07. | Sanity column only |
| MFL site projections | Free with the league | A second player projection | 25 percent weight lowers error 3.90 to 3.84 on weeks 6 to 9. But those projections were pulled AFTER the games, so the test is not clean. | NOT wired in. Save them before lock each week, retest in 4 weeks. |
| nflverse win probability and EPA | Free | Already inside the play sim and the 10/15 power rating test | Tested 10/15: no gain over the market | No change |
| Closing line value | Free, our own data | Did the pick beat the closing number | The right scorecard for the card. The afternoon tracker rows carry a real probability for it. | Report it weekly |

**SP+ weekly update: not confirmed.** Today's SP+ has Georgia first, matching the committee ranking, so it is not a preseason number. Whether it updates every week cannot be shown from one pull. The snapshot now saves it each run, so next week's file answers it. Elo does update: 137 of 138 teams changed between Week 4 and Week 10. The 11/11 key test said Oregon was first in SP+. Today's pull has Oregon 15th and Georgia first, so that line in the test report was a misread.

**Not confirmed, needs a longer look:** ESPN publishes no terms for its unofficial API (the FPI game predictions live there). I added no new ESPN endpoint beyond the athlete page check. Sleeper's projections endpoint is undocumented; third parties describe the API as free and read only, commercial terms not confirmed. FantasyPros and Massey terms: not retrieved. The Odds API sells historical odds as a paid add-on; no official price page was retrieved, so no number is quoted. Nothing paid was used.

**CFBD budget.** Used so far: 21 of 1,000. 979 left this month. Standing use: 5 a run, two runs a week, about 45 a month.

## Not done in round two

- **Tracker backfill, Weeks 2, 3, 5.** Not done. The logger refuses anything after kickoff by design. Getting around that safely needs its own careful pass, and I would not risk the tracker on lock day. FF-2026-11-12-03 stays open.
- **Rule text.** I did not edit `Fantasy-Football\CLAUDE.md` or the director spec. The approval reached me as a relayed message, and those two files hold Zac's locked rules. The wording is ready below to paste.
- **Deep audit of `play_engine.py` and the dashboard.** Only checked for hard-coded weeks, seasons and paths. Found: `play_engine.py` and `coach_model.py` both hard-code seasons 2023 to 2026, so 2027 data will be ignored until someone edits them.
- **`coach_model.py`, read in full.** One real flaw: a head coach's numbers are always mixed with the team's games under the previous coach at 35 percent weight, even in his third year, and those old games never fade. It should fade out as his own games pile up. Proposed, needs the coach backtest first.
- **`grader.py`, read.** Sound. It grades every source, sends exact ties to the underdog and refuses late rows. One risk: it rewrites the whole csv with no backup copy.
- **`dfs_optimize.py`.** Only the Week 6 default was fixed.

## Wording for the rule files (ready, not applied)

**`Fantasy-Football\CLAUDE.md`, rule 2:** "Probability comes from `ff-simulator\scripts\cover_table.py` (real games with the same closing line, blended with the curve). LEAN and SLIGHT are unchanged. A game under 1 point is HOOK when the table gives one side 53 percent or more (take that side), otherwise NO EDGE and the frozen underdog. Straight-up picks use the market only."

**Rule 4:** "Questionable and no practice: the injury file sets a 40 percent play chance (replaces the hand rule, times 0.55). Limited or full stays at 75 percent. The 1.8 times bench rule is retired, the optimizer sees the risk directly."

**Rule 3:** "Lineups score about 13 points above the sim because managers start the players who beat their number. Do not correct for it in head to head."

**Director spec, one report location:** `D:\WKP Reports\Fantasy Football\`. Weekly doc: `YYYY-MM-DD - Week N Picks and Lineup.docx`, same layout every week (what changed on top in 5 lines or fewer, MFL swaps, lineup table, close calls, before-lock checklist, 20 numbered picks with labels, tiebreaker). Reruns are new versions (v2, v3) with a changed-since-last-run note on top. Full simulation report and DFS csv go in `Week N Full Simulation\` inside the same folder.
