# IRFL Week 7 lineup (Caerellius Lions, 0012) - 2026-10-21, v2 (rebuilt on the multi-source injury layer)
SUPERSEDES the 3 PM version. Old copy kept at D:\WKP\Fantasy-Football\reports\Week7-Lineup-2026-10-21-v1-superseded.md. Decision support only; Zac sets the lineup by hand.
Run: 2026-10-21 about 4:55 PM ET. Odds re-pulled 4:50 PM (the old pull was 12:15 PM). Roster re-pulled fresh from MFL. 10,000 sims. Byes (from the nflverse schedule, 14 games played): BUF, JAX, LAC, WAS.

## What was wrong with v1
The sim only read out/doubtful/IR from the MFL export. So it (a) missed ESPN's Wednesday designations that MFL did not have yet, (b) kept 141 practice-squad players, 14 released players and several suspended/reserve players in the pool, and (c) left players on their old teams after moves. Roster-relevant examples: Michael Carter was simulated on ARI (4.3) but is on TEN now; Shepard is on a practice squad per nflverse.

## EXPECTED lineup (sim mean 149.0, 10th 111.1, 90th 188.2; MFL projection for the same 17: 148.7)
| Slot | Player | Mean | 10th-90th | Status line (source, time) |
|---|---|---|---|---|
| QB | Goff (DET) | 21.1 | 6.3-38.1 | ACT, no designation (nflverse 12:56Z) |
| RB | B. Robinson (ATL) | 7.7 | 0.5-17.1 | ACT (nflverse 12:56Z) |
| RB | Dowdle (PIT) | 6.6 | 0.9-13.6 | ACT (nflverse 12:56Z) |
| WR | Flowers (BAL) | 15.2 | 4.6-27.3 | ACT (nflverse 12:56Z) |
| WR | J. Jefferson (MIN) | 13.9 | 3.2-25.9 | ACT (nflverse 12:56Z) |
| WR | Ja. Williams (DET) | 10.9 | 1.5-21.3 | ACT (nflverse 12:56Z) |
| WR | Allen (IND) | 9.2 | 1.7-18.1 | ACT (nflverse 12:56Z); replaces Golden |
| TE | LaPorta (DET) | 9.5 | 1.2-19.0 | ACT (nflverse 12:56Z) |
| PK | Bates (DET) | 9.5 | 2.0-19.8 | Active (ESPN 10-12) |
| DL | Hutchinson (DET) | 5.5 | 1.0-10.5 | ACT (nflverse 12:56Z) |
| DL | Wonnum (DET) | 5.4 | 1.0-11.0 | ACT (nflverse 12:56Z) |
| LB | Okereke (CAR) | 8.0 | 3.0-13.5 | ACT (nflverse 12:56Z) |
| LB | Gibbens (ARI) | 5.1 | 2.0-9.0 | ACT (nflverse 12:56Z) |
| LB | Strnad (DEN) | 5.0 | 1.5-9.0 | ACT (nflverse 12:56Z) |
| DB | Scott (CAR) | 5.7 | 2.0-10.0 | ACT (nflverse 12:56Z) |
| DB | Reed (DET) | 5.7 | 2.0-10.0 | ACT (nflverse 12:56Z) |
| DB | Sanker (NOS) | 4.8 | 1.5-8.5 | ACT (nflverse 12:56Z); 2 DL / 3 LB / 3 DB split |

SAFE is the same 17. UPSIDE (mean 147.7, 90th 187.9) swaps in Golden for Allen and Moss for Sanker; it gives up 1.3 points of mean and gains no ceiling (187.9 vs 188.2), so ignore it.

## What changed vs v1 (roster-relevant)
- Golden (GB) is now Questionable, shoulder, limited Wednesday (ESPN 20:20Z). MFL did not show it. Sim 10.6 -> 8.1, so he drops out of the top 4 WR and Allen (IND, 9.2) starts.
- Tavius Robinson (BAL) is now Questionable, pectoral (ESPN 20:38Z). MFL did not show it. Sim 4.9 -> 3.7, so the third DL slot goes away and Sanker takes the third DB slot.
- Spears (TEN) cleared on MFL; ESPN 19:54Z has him a Wednesday non-participant for rest, listed Active. Sim 4.6 -> 6.3. He is a real RB2 contender (Dowdle 6.6 vs Spears 6.3, effectively a tie).
- Ridley (TEN) now Questionable, hip, limited (ESPN 20:05Z). Kancey (TB) Questionable, illness (MFL).
- Michael Carter: sim had him on ARI, he is on TEN. No TEN usage history, so no sim number (bench only).
- Sterling Shepard: nflverse has him on the practice squad (DEV/P07), MFL says NYJ. Not startable.
- Rachaad White: see overrides below.

## Close calls
- RB2 Dowdle 6.6 vs Spears 6.3: 0.3, coin flip. Watch Friday.
- DB3 Sanker 4.8 vs Kinchens 4.7 vs Moss 4.6: noise.
- LB3 Strnad 5.0 and Gibbens 5.1 both start; Barton 3.5 is next.
- WR4 Allen 9.2 vs Flournoy 8.2 vs Golden 8.1 (Q).
- TE LaPorta 9.5 vs Schultz 8.7 vs Goedert 8.2.
- PK Bates 9.5 vs McPherson 8.6 vs Folk 8.2.
- QB Goff 21.1 vs C. Williams 19.6 (was 18.7) vs Brissett 17.0. Gap is 1.5. MFL's own projection still ranks Goff 24.8, Williams 24.2, Brissett 23.9.
- Hockenson (MIN, Q concussion) 7.1 sits behind LaPorta either way.

## Bench
QB Williams, Brissett; RB Spears, Demercado (0.9), Carter (no sim); WR Flournoy, Golden (Q), Ridley (Q); TE Schultz, Goedert, Hockenson (Q); PK McPherson, Folk; DL T. Robinson (Q), Davis (Q); LB Barton, Dodson, Reid; DB Kinchens, Moss, Mukuba, Jenkins, Anderson. Not eligible or no sim: White and Croskey-Merritt (WAS bye; Croskey-Merritt also IR), Molden (LAC bye), Shepard (practice squad), Andersen (FA, Q), taxi and IR slots.

## MFL lineup saved vs optimizer
The lineup export is not reachable by API, so this is the 3 PM lineup and may have changed: Williams, B. Robinson, White, Allen, Flowers, Golden, Ridley, Goedert, Folk, Davis, T. Robinson, Gibbens, Okereke, Strnad, Jenkins, Kinchens, Sanker. Sim mean 114.7 (White scores 0 on the bye). EXPECTED beats it in 86% of simulated weeks, average gain +34.3.
Moves: White -> Dowdle; Ridley and Golden -> Jefferson and Ja. Williams; Williams -> Goff; Goedert -> LaPorta; Folk -> Bates; Davis (Q) and T. Robinson (Q) -> Hutchinson and Wonnum; Jenkins and Kinchens -> Reed and Scott.

## Opponent
Plautianus Chiefs (0010). Their set lineup includes Josh Allen, Rousseau (BUF bye), McLaurin (WAS bye, MFL Out), Walker (JAX bye), McConkey (LAC bye, Q): sim mean 113.8 (sd 22.9). Win probability: EXPECTED 82.6%, SAFE 82.6%, UPSIDE 81.1%, current sheet 50.3%. They can still change their lineup.

## Manual overrides applied (D:\WKP\data\ff-simulator\overrides_2026_wk7.json)
- Brian Branch (DET DB) ACTIVE per Zac 10-21. Not on Zac's roster. Sources still disagree: MFL IR-PUP (20:01Z), nflverse RES/R04 (12:56Z), ESPN Out 10-10. Web (Pride of Detroit, Pro Football Rumors, CBS): practice window opened Wed 10-21, Campbell said he expects activation before Sunday, possible snap count. No activation transaction in the ESPN feed yet. His sim number is built from old usage and may overstate a snap-limited return.
- Cade Mays (DET C) ACTIVE per Zac 10-21. This is the "Maye" Zac meant, not Drake Maye. No Drake Maye override exists (Drake Maye is Active, played 10-18, full practice per nflverse). Mays sources: ESPN 10-10 IR (wrist fracture), nflverse RES/R48 (12:56Z), same Wednesday practice-window news, no activation transaction yet. See the OL section below for what this does and does not change.
- Rachaad White (WAS RB) IR per Zac. CONFLICT with sources: ESPN 10-20 has him Active and playing Monday 10-19 (7 carries, 4 catches, TD); MFL injuries has no entry; his MFL roster slot is ROSTER; nflverse is not reserve. WAS is on bye, so he scores 0 either way.

## Friday and Sunday checks
Golden, T. Robinson, Spears, Ridley (all Wednesday designations); Goff and Jefferson late tags; Lamar Jackson (BAL, Q, limited Wednesday) for Flowers; DET Branch and Mays activation transactions. Re-run build_injuries.py, run_week.py, optimize.py Sunday morning.

## Offensive line layer (phase 2, built and backtested 2026-10-21; NOT applied to the numbers above)
What it is: ol_model.py reads nflverse snap counts to find each team's usual five linemen (top 5 by snap share over the last 6 games), checks them against the injury table (out/IR/reserve = missing, Doubtful 75% missing, Questionable 25% missing), and fits the effect of missing starters on sacks, yards per attempt and yards per carry, with team-season and opposing-defense-season dummies so QB, scheme and opponent are held fixed. Fitted only on games before 2025 week 6 (1,148 team-games, 675 with at least one usual starter absent, 270 with two or more).
Effect sizes per starter missing (all five out = 5x): sack rate +0.3 points (t 1.6, weak), pressure rate +0.6 points (t 1.6), pass EPA per dropback -0.030 (t -2.6), yards per attempt -0.14 (t -1.9), yards per carry -0.09 (t -1.7), yards before contact -0.13 (PFR, t -3.2). Directionally right and modest.
Backtest (18 weeks, 2025 wk6 to 2026 wk5, 546 team-games, 400 sims, same seeds, OL absence taken as a lineman with zero snaps, which is knowable pre-game):
- Team level, all games: passing-yards RMSE 76.3 -> 75.3, rushing-yards RMSE 49.2 -> 48.5 (about 1.4% better); in games with OL miss >= 0.30 the passing-yards bias fell from +18.4 to +5.4. Sacks did NOT improve (MAE 1.39 -> 1.40, bias +0.05 -> +0.14), so the sack piece is not supported. Dropping the sack effect ("yds" variant) keeps most of the yardage gain.
- Player level (QB/RB/WR/TE IRFL points, 5,301 player-games): no improvement. MAE 4.810 -> 4.816, RMSE 7.056 -> 7.071 (slightly worse). Same in games with OL miss >= 0.15.
Verdict: the OL effect is real in team yardage but tiny, and it does not improve player-point forecasts, so it is context only. It is built into the simulator behind a switch (simulate.set_ol, run_week.py --ol) and is OFF by default; none of the lineup, pick or tiebreaker numbers in this report use it.
Week 7 teams with usual OL starters unavailable (share of usual OL5 snaps; sim run with the layer on, for sizing only): NE 0.39 (Vera-Tucker OUT, Ben Brown OUT, Moses Q), BAL 0.22 (Gwyn on reserve, Ioane Q, Simpson Q), MIN 0.17 (Donovan Jackson on reserve), ARI 0.16 (Paris Johnson on reserve), NYG 0.10 (Thomas Q, Eluemunor Q, Mbow Q), IND 0.10 (Goncalves Q, Travis Q), CLE 0.09 (Howard Q, Jenkins Q), TB 0.05 (Goedeke Q), NO 0.05 (Ruiz Q). Everyone else: no usual starter out. Jackson Powers-Johnson, Jurgens (PHI) and a few others are not in the injury table and are treated as available.
How the numbers move with the layer on: largest move is Drake Maye (NE QB) 21.1 -> 20.6; Flowers 15.2 -> 15.0 (BAL), other skill players 0.0 to 0.3. Zac's IRFL lineup is the same 17 either way, EXPECTED mean 149.0 -> 148.8 (full) or 148.7 (no sack effect). Tiebreaker and pick'em margins/totals are unchanged by construction (the game score is anchored to the market line). As context only: NE's line is thin on a short week (supports the CHI pick, already made), BAL has two Q guards plus a Q quarterback, which sits with the market having moved CIN from +2.5 to -1.0 (supports the existing CIN +3.5 pick), and NYG's two starting tackles are both Q (supports HOU -9.5).
Cade Mays (DET C): played center for CAR in 2025 (about 1.0 snap share in most games) but has zero DET snaps in 2026 (he does not appear in any 2026 snap count; ESPN 10-10 had him out with a wrist fracture, nflverse shows IR designated to return). DET's usual five are Ratledge, Scruggs, Sewell, Mahogany, Miller with no one missing, and Bartch (IR 10-16) was a part-time player, so Mays' return cannot register as a restored starter. At most he competes for the center/guard spot. Zero effect on any sim number and only a context flag for Goff, LaPorta and the DET run game.
Team OL strength index (raw z-scores from this and last season: sack rate, pressure rate, rush EPA, yards before contact; NOT adjusted for QB or opponent, so read it as context): top LA +1.20, BUF +1.17, CHI +0.89, DAL +0.73, SF +0.72, IND +0.70; bottom LV -1.92, CLE -1.64, LAC -0.97, MIN -0.90, NYJ -0.81, TEN -0.74. File: D:\WKP\data\ff-simulator\ol_index_2026_wk7.csv. Per-lineman table: ol_week_2026_7.csv.

## Model limits
- Sim margins and totals are anchored to the market line, so injuries never move a game's expected score, only who shares the volume.
- No offensive coordinator column, first-year coaches lean on team history, kickers flat 3.75 per FG, single-game noise is large (backtest only 3-6% better than a recent average).
- A player absent from every source row is treated as available (about 10 players with model value, such as Lavonte David, Kareem Hunt, Darius Slayton and some kickers, have no row).
- Returning players get usage from old games.
- The nflverse week-7 injury file had only 23 rows (Wednesday practice reports, release 12:53Z). The newest row in the table is ESPN 20:38Z today, so nothing is over 24 hours old.
