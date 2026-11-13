# Week 10 Full Simulation - Wednesday Run, 2026-11-11 (9:20 PM ET)

Decision support only. Nothing was submitted on MFL or the pick'em platform. Card and IRFL lineup lock at Thursday 11/12 kickoff, Washington at New York Giants, 8:15 PM ET. This is the first run of Week 10, so there is no earlier run to diff against; the Thursday rerun will list every change against this report.

Companion docs: `Pickups 2026 - Week 10` (model card and lineup summary) and `Week 10 Lineup` (status line on every player).

## 0. WHAT THIS RUN CHANGED OR FOUND

- **Pick'em:** 20 picks logged to `tracker\predictions.csv` before kickoff at 2026-11-12T02:19Z, source `model`, line_source `frozen_card_wed_run`. 2 LEAN, 6 SLIGHT, 12 NO EDGE. Expected right out of 20: 10.3.
- **Biggest edges:** Seattle -3.5 at Las Vegas (market -6.5, 3.0 move, rookie Mendoza starts after the Cousins trade) and LA Rams -7.5 at Arizona (market -9.5, 2.0 move, Minshew out for the season, Beck starts).
- **Lineup:** the saved MFL lineup has four zero-point starters (Robinson on IR, Strnad, Davis and Mukuba on byes). Recommended 17 projects 151.6 versus 132.7 saved.
- **Data errors and stale inputs found:** nflverse roster file lags the 11/10 trades (Allen IND to SF, Cousins LV to MIN); the sim's QBs for BAL, MIN, LV, ARI, MIA are pre-news; `full_week.py` crashed on the 'every Questionable out' lineup (no healthy QB or second DL) and I added a one-line guard that skips an unfillable lineup; `optimize.py` defaults to the Week 6 roster and sheet, so both flags were passed explicitly. No Week 10 DFS salary file exists.
- **Odds data check:** the nflverse spread_line never differed from the Odds API market by 5 or more points on any NFL game this week (largest: BAL, 4.5 vs 4.0). No 20-point swing, nothing that looks like a data error.

## 1. Card summary

| # | Game | Card | Market | Gap | Pick (ATS) | Tier | SU |
|---|---|---|---|---|---|---|---|
| 1 | Washington Commanders at NEW YORK GIANTS | NY Giants -1.5 | Giants -2 | 0.5 | **Washington +1.5** | NO EDGE | Giants (56%) |
| 2 | Florida State Seminoles at PITTSBURGH PANTHERS | Pittsburgh -3.5 | Pittsburgh -3.5 | 0.0 | **Florida State +3.5** | NO EDGE | n/a |
| 3 | Auburn Tigers at MISSISSIPPI STATE BULLDOGS | Auburn -3.5 | Auburn -2.5 | 1.0 | **Mississippi State +3.5** | SLIGHT | n/a |
| 4 | Wisconsin Badgers at MARYLAND TERRAPINS | Wisconsin -8.5 | Wisconsin -9 | 0.5 | **Maryland +8.5** | NO EDGE | n/a |
| 5 | Arizona State Sun Devils at UCF KNIGHTS | U. Central Florida -3.5 | UCF -3.5 | 0.0 | **Arizona State +3.5** | NO EDGE | n/a |
| 6 | Fresno State Bulldogs at TEXAS STATE BOBCATS | Texas State -8.5 | Texas State -9.5 | 1.0 | **Texas State -8.5** | SLIGHT | n/a |
| 7 | Texas Longhorns at LSU TIGERS | Lsu -3.5 | LSU -4 | 0.5 | **Texas +3.5** | NO EDGE | n/a |
| 8 | New England Patriots at DETROIT LIONS | Detroit -2.5 | Lions -3 | 0.5 | **New England +2.5** | NO EDGE | Lions (58%) |
| 9 | Miami Dolphins at INDIANAPOLIS COLTS | Indianapolis -2.5 | Colts -3.5 | 1.0 | **Indianapolis -2.5** | SLIGHT | Colts (57%) |
| 10 | Kansas City Chiefs at ATLANTA FALCONS | Kansas City -3.5 | Chiefs -3 | 0.5 | **Atlanta +3.5** | NO EDGE | Chiefs (60%) |
| 11 | Houston Texans at CLEVELAND BROWNS | Houston -4.5 | Texans -5 | 0.5 | **Cleveland +4.5** | NO EDGE | Texans (64%) |
| 12 | Minnesota Vikings at GREEN BAY PACKERS | Green Bay -3.5 | Packers -3 | 0.5 | **Minnesota +3.5** | NO EDGE | Packers (60%) |
| 13 | Jacksonville Jaguars at TENNESSEE TITANS | Jacksonville -9.5 | Jaguars -10.5 | 1.0 | **Jacksonville -9.5** | SLIGHT | Jaguars (79%) |
| 14 | Carolina Panthers at NEW ORLEANS SAINTS | New Orleans -1.5 | Saints -2.5 | 1.0 | **New Orleans -1.5** | SLIGHT | Saints (58%) |
| 15 | Buffalo Bills at NEW YORK JETS | Buffalo -7.5 | Bills -8 | 0.5 | **NY Jets +7.5** | NO EDGE | Bills (73%) |
| 16 | Seattle Seahawks at LAS VEGAS RAIDERS | Seattle -3.5 | Seahawks -6.5 | 3.0 | **Seattle -3.5** | LEAN | Seahawks (69%) |
| 17 | Los Angeles Rams at ARIZONA CARDINALS | LA Rams -7.5 | Rams -9.5 | 2.0 | **LA Rams -7.5** | LEAN | Rams (74%) |
| 18 | San Francisco 49ers at DALLAS COWBOYS | San Francisco -3.5 | 49ers -4 | 0.5 | **Dallas +3.5** | NO EDGE | 49ers (63%) |
| 19 | Pittsburgh Steelers at CINCINNATI BENGALS | Cincinnati -3.5 | Bengals -3.5 | 0.0 | **Pittsburgh +3.5** | NO EDGE | Bengals (60%) |
| 20 | Los Angeles Chargers at BALTIMORE RAVENS | Baltimore -5.5 | Ravens -4 | 1.5 | **LA Chargers +5.5** | SLIGHT | Ravens (62%) |

Monday-night tiebreaker: **Baltimore 21, Chargers 17, total 38** (market 38.5).

Per-game status lines are in the Pickups doc, section 5.

## 2. IRFL lineups from the simulation (old sim, Week 10 roster, MFL roster 02:09Z)

| Lineup | Average | One sigma | 10th to 90th |
|---|---|---|---|
| EXPECTED, SAFE and UPSIDE (same 17 as the Lineup doc) | 151.2 | 31.1 | 113.2 to 192.5 |
| With Moore (taxi) at DL2 instead of Wonnum | 151.5 | 31.1 | 113.5 to 192.3 |

The optimizer with `--taxi` swaps Wonnum for Moore and nothing else. Contingency lineup (every Questionable out) cannot be filled: no healthy QB (Goff is Questionable) and one healthy DL.

## 3. Known limits

- Sim quarterbacks are stale for BAL, MIN, LV, ARI, MIA. Offense-only effect on the players of those games.
- Injury news is as fresh as 11/12 02:09Z (MFL) and the ESPN feed to 00:29Z. Thursday practice reports are not in.
- College games have no injury, odds-history or sim data beyond the 9-book line.
- The simulation is anchored on the market. It does not find edges against it.

## 4. RAW SIMULATION OUTPUT (ff-simulator full_week.py, 4,000 runs per game)

# Week 10 Full Simulation Report - 15 OCT 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 4,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| WAS @ NYG | NYG 55.9% | WAS 19.7 - NYG 21.5 | WSH | 48.4% | NYG | 56.2% |
| NE @ DET | DET 59.1% | NE 24.0 - DET 27.1 | NE | 48.4% | DET | 59.3% |
| KC @ ATL | KC 57.9% | KC 25.0 - ATL 22.3 | ATL | 51.6% | KC | 59.3% |
| HOU @ CLE | HOU 64.6% | HOU 23.3 - CLE 18.2 | CLE | 48.4% | HOU | 65.3% |
| MIN @ GB | GB 59.7% | MIN 19.3 - GB 22.6 | MIN | 51.6% | GB | 59.3% |
| MIA @ IND | IND 62.1% | MIA 17.0 - IND 21.0 | IND | 53.1% | IND | 60.8% |
| CAR @ NO | NO 58.2% | CAR 22.9 - NO 25.5 | NO | 53.1% | NO | 57.8% |
| BUF @ NYJ | BUF 73.8% | BUF 29.6 - NYJ 21.4 | NYJ | 48.4% | BUF | 73.5% |
| JAX @ TEN | JAX 78.7% | JAX 28.3 - TEN 18.0 | JAX | 53.1% | JAX | 79.5% |
| LA @ ARI | LA 76.9% | LA 24.4 - ARI 14.8 | LAR | 56.2% | LAR | 77.2% |
| SEA @ LV | SEA 68.7% | SEA 23.5 - LV 17.1 | SEA | 59.3% | SEA | 69.5% |
| SF @ DAL | SF 62.2% | SF 29.9 - DAL 25.7 | DAL | 48.4% | SF | 62.3% |
| PIT @ CIN | CIN 61.1% | PIT 23.0 - CIN 26.6 | PIT | 50.0% | CIN | 60.8% |
| LAC @ BAL | BAL 62.3% | LAC 17.3 - BAL 21.3 | LAC | 54.7% | BAL | 62.3% |

**Eliminator (fresh start this week, every team open):** best win chances are LA Rams 83.7%, KC 73.5%, SF 72.2%, IND and NE 70.9%. Surviving all season means saving the biggest favorites for the weeks with weaker options, so the Rams are the safe pick now but not automatically the smart one. I can plan the full 18 weeks once the schedule odds are loaded.

## 2. Five IRFL lineups (Golden active)

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 150.7 | 111.5 | 190.6 |
| 2 SAFE (protects a lead) | 150.7 | 111.5 | 190.6 |
| 3 BALANCED UPSIDE (75th percentile) | 150.6 | 111.4 | 191.1 |
| 4 SWING (90th percentile, for an underdog) | 150.6 | 111.4 | 191.1 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.8 | 6.6 to 36.8 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.1 | 3.1 to 22.9 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 2.1 to 18.7 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.6 to 25.7 |  |
| WR | Golden, Matthew | GBP | 13.7 | 3.4 to 25.3 |  |
| WR | Jefferson, Justin | MIN | 13.2 | 3.1 to 24.5 |  |
| WR | Williams, Jameson | DET | 11.4 | 1.5 to 22.4 |  |
| TE | LaPorta, Sam | DET | 9.9 | 1.5 to 19.7 |  |
| PK | Bates, Jake | DET | 10.3 | 1.0 to 21.8 |  |
| DL | Hutchinson, Aidan | DET | 4.6 | 1.0 to 9.0 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.6 | 0.0 to 11.5 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 |  |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.1 |  |
| DB | Sanker, Jonas | NOS | 4.8 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.8 | 6.6 to 36.8 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.1 | 3.1 to 22.9 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 2.1 to 18.7 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.6 to 25.7 |  |
| WR | Golden, Matthew | GBP | 13.7 | 3.4 to 25.3 |  |
| WR | Jefferson, Justin | MIN | 13.2 | 3.1 to 24.5 |  |
| WR | Williams, Jameson | DET | 11.4 | 1.5 to 22.4 |  |
| TE | LaPorta, Sam | DET | 9.9 | 1.5 to 19.7 |  |
| PK | Bates, Jake | DET | 10.3 | 1.0 to 21.8 |  |
| DL | Hutchinson, Aidan | DET | 4.6 | 1.0 to 9.0 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Okereke, Bobby | CAR | 5.6 | 0.0 to 11.5 | Questionable, plays about 75% of sims. |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 |  |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.1 |  |
| DB | Sanker, Jonas | NOS | 4.8 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.8 | 6.6 to 36.8 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.1 | 3.1 to 22.9 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 2.1 to 18.7 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.6 to 25.7 |  |
| WR | Golden, Matthew | GBP | 13.7 | 3.4 to 25.3 |  |
| WR | Jefferson, Justin | MIN | 13.2 | 3.1 to 24.5 |  |
| WR | Williams, Jameson | DET | 11.4 | 1.5 to 22.4 |  |
| TE | LaPorta, Sam | DET | 9.9 | 1.5 to 19.7 |  |
| PK | Bates, Jake | DET | 10.3 | 1.0 to 21.8 |  |
| DL | Hutchinson, Aidan | DET | 4.6 | 1.0 to 9.0 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.6 | 0.0 to 11.5 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 |  |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.1 |  |
| DB | Reed, D.J. | DET | 4.1 | 0.0 to 9.0 | Questionable, plays about 75% of sims. differs from lineup 1 |
| DB | Sanker, Jonas | NOS | 4.8 | 1.5 to 8.5 |  |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.8 | 6.6 to 36.8 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.1 | 3.1 to 22.9 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 2.1 to 18.7 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.6 to 25.7 |  |
| WR | Golden, Matthew | GBP | 13.7 | 3.4 to 25.3 |  |
| WR | Jefferson, Justin | MIN | 13.2 | 3.1 to 24.5 |  |
| WR | Williams, Jameson | DET | 11.4 | 1.5 to 22.4 |  |
| TE | LaPorta, Sam | DET | 9.9 | 1.5 to 19.7 |  |
| PK | Bates, Jake | DET | 10.3 | 1.0 to 21.8 |  |
| DL | Hutchinson, Aidan | DET | 4.6 | 1.0 to 9.0 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.6 | 0.0 to 11.5 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 |  |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.1 |  |
| DB | Reed, D.J. | DET | 4.1 | 0.0 to 9.0 | Questionable, plays about 75% of sims. differs from lineup 1 |
| DB | Sanker, Jonas | NOS | 4.8 | 1.5 to 8.5 |  |

Lineups 1 and 2 are identical; 3 and 4 are identical. Your roster has few real choices this week (the only live decisions are QB, the last DB slot and the last WR slot), so the five lineups collapse. Averages shift by about half a point between runs because the dice differ.

Not simulated this week (bye, no team, or no recent usage): Wright, Nahshon (NYJ); Moss, Riley (DEN); Robinson, Tavius (BAL); Davis, Jordan (PHI); Kancey, Calijah (TBB); Strnad, Justin (DEN); Andersen, Troy (FA); Folk, Nick (ATL); Williams, Caleb (CHI); Robinson, Brian (ATL); Jenkins, Rayshawn (BAL); Mukuba, Andrew (PHI); Locke, P.J. (DAL); Goedert, Dallas (PHI); Shepard, Sterling (NYJ).

When the two free agents land (a safety and a defensive end), I will add them for Week 7. Defensive line is the thinnest group: Davis and Kancey are the only two playable linemen this week.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### BUF @ NYJ

Market: NYJ +8.0, total 51.0. Sim: BUF 29.6, NYJ 21.4. NYJ wins 26.2%, BUF wins 73.8%. Median margin -8.2 for NYJ.

| Team stat | BUF | NYJ |
|---|---|---|
| Plays | 64 | 61 |
| Pass attempts / completions | 30 / 20 | 34 / 22 |
| Passing yards | 248 | 230 |
| Rush attempts / yards | 31 / 137 | 24 / 103 |
| Sacks taken | 2.1 | 2.2 |
| Interceptions thrown | 0.5 | 0.7 |
| Passing / rushing TDs | 1.6 / 1.6 | 1.4 / 0.9 |
| Field goals | 2.2 | 1.6 |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.2 | 248 pass yd, 1.6 TD, 0.5 INT; 6.1 rush, 28 yd |  |
| RB | James Cook | 15.9 | 17.1 car, 76 yd, 0.86 TD; 1.5 rec, 15 yd, 0.07 TD |  |
| RB | Ty Johnson | 6.6 | 1.9 car, 8 yd, 0.09 TD; 2.3 rec, 25 yd, 0.10 TD |  |
| RB | Ray Davis | 3.0 | 2.6 car, 12 yd, 0.07 TD; 0.5 rec, 6 yd, 0.05 TD |  |
| WR | Khalil Shakir | 9.7 | 3.9 rec, 46 yd, 0.21 TD |  |
| WR | DJ Moore | 8.1 | 0.5 car, 2 yd, 0.00 TD; 2.8 rec, 35 yd, 0.26 TD |  |
| WR | Keon Coleman | 7.3 | 2.7 rec, 32 yd, 0.25 TD |  |
| WR | Gabe Davis | 1.4 | 0.7 rec, 7 yd, 0.08 TD | Questionable |
| TE | Dalton Kincaid | 6.7 | 3.4 rec, 41 yd, 0.22 TD | Questionable |
| TE | Dawson Knox | 4.7 | 2.0 rec, 18 yd, 0.15 TD |  |
| K | Tyler Bass | 11.2 | 2.2 FG, 3.0 XP |  |
| DL | Deone Walker | 2.4 | 1.0 solo, 1.5 ast, 0.06 sack, 0.51 PD, 0.00 INT |  |
| DL | Landon Jackson | 2.1 | 0.7 solo, 1.3 ast, 0.20 sack, 0.13 PD, 0.00 INT |  |
| LB | Greg Rousseau | 6.3 | 1.6 solo, 1.0 ast, 0.88 sack, 0.90 PD, 0.00 INT |  |
| LB | Terrel Bernard | 5.7 | 3.0 solo, 3.3 ast, 0.00 sack, 0.40 PD, 0.16 INT |  |
| LB | Dorian Williams | 4.6 | 1.7 solo, 3.3 ast, 0.00 sack, 0.31 PD, 0.26 INT |  |
| DB | Cole Bishop | 5.2 | 3.2 solo, 2.2 ast, 0.13 sack, 0.22 PD, 0.00 INT |  |
| DB | Davison Igbinosun | 4.1 | 1.7 solo, 1.5 ast, 0.00 sack, 1.19 PD, 0.15 INT |  |
| DB | C.J. Gardner-Johnson | 3.4 | 2.1 solo, 1.2 ast, 0.00 sack, 0.25 PD, 0.13 INT |  |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Geno Smith | 17.1 | 230 pass yd, 1.4 TD, 0.7 INT; 1.8 rush, 7 yd |  |
| RB | Braelon Allen | 11.4 | 11.1 car, 51 yd, 0.45 TD; 2.0 rec, 13 yd, 0.06 TD |  |
| RB | Breece Hall | 7.4 | 8.1 car, 31 yd, 0.26 TD; 1.4 rec, 12 yd, 0.04 TD |  |
| RB | Isaiah Davis | 2.4 | 1.8 car, 8 yd, 0.06 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| WR | Garrett Wilson | 7.6 | 4.4 rec, 45 yd, 0.24 TD | Questionable |
| WR | Omar Cooper Jr. | 6.8 | 3.6 rec, 40 yd, 0.26 TD | Questionable |
| WR | Adonai Mitchell | 6.4 | 2.3 rec, 29 yd, 0.21 TD |  |
| WR | Isaiah Williams | 3.6 | 1.4 rec, 14 yd, 0.13 TD |  |
| TE | Mason Taylor | 5.1 | 2.2 rec, 18 yd, 0.19 TD |  |
| TE | Kenyon Sadiq | 4.9 | 2.0 rec, 20 yd, 0.10 TD |  |
| K | Jason Sanders | 10.4 | 2.2 FG, 2.2 XP |  |
| DL | Will McDonald IV | 3.3 | 0.9 solo, 1.2 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| DL | Jowon Briggs | 2.8 | 1.1 solo, 2.1 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | David Bailey | 8.6 | 3.2 solo, 2.3 ast, 0.88 sack, 0.09 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.8 | 4.2 solo, 4.8 ast, 0.04 sack, 0.45 PD, 0.00 INT |  |
| LB | Demario Davis | 6.5 | 3.6 solo, 3.3 ast, 0.15 sack, 0.41 PD, 0.00 INT |  |
| DB | Dane Belton | 7.7 | 5.0 solo, 4.1 ast, 0.09 sack, 0.41 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 7.6 | 4.3 solo, 4.6 ast, 0.00 sack, 0.41 PD, 0.10 INT |  |
| DB | Azareye'h Thomas | 3.7 | 1.9 solo, 2.7 ast, 0.00 sack, 0.47 PD, 0.00 INT |  |

### CAR @ NO

Market: NO -2.5, total 48.5. Sim: CAR 22.9, NO 25.5. NO wins 58.2%, CAR wins 41.8%. Median margin +2.8 for NO.

| Team stat | CAR | NO |
|---|---|---|
| Plays | 62 | 64 |
| Pass attempts / completions | 34 / 21 | 34 / 23 |
| Passing yards | 225 | 230 |
| Rush attempts / yards | 25 / 109 | 28 / 114 |
| Sacks taken | 3.0 | 2.2 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.5 / 1.3 |
| Field goals | 1.7 | 1.9 |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.5 | 225 pass yd, 1.5 TD, 0.7 INT; 2.5 rush, 11 yd |  |
| RB | Chuba Hubbard | 16.6 | 16.5 car, 71 yd, 0.63 TD; 3.1 rec, 20 yd, 0.15 TD |  |
| RB | AJ Dillon | 1.8 | 2.8 car, 11 yd, 0.05 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| RB | Trevor Etienne | 1.3 | 1.6 car, 7 yd, 0.03 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tetairoa McMillan | 12.8 | 5.1 rec, 57 yd, 0.34 TD |  |
| WR | Jalen Coker | 9.6 | 3.9 rec, 40 yd, 0.29 TD |  |
| WR | John Metchie III | 4.4 | 1.9 rec, 19 yd, 0.11 TD |  |
| WR | Brycen Tremayne | 1.9 | 0.8 rec, 9 yd, 0.03 TD |  |
| TE | Darren Waller | 7.7 | 2.9 rec, 32 yd, 0.26 TD |  |
| TE | Tommy Tremble | 5.7 | 2.4 rec, 20 yd, 0.23 TD |  |
| K | Ryan Fitzgerald | 8.1 | 1.5 FG, 2.4 XP |  |
| DL | Derrick Brown | 3.8 | 2.0 solo, 2.0 ast, 0.07 sack, 0.53 PD, 0.00 INT |  |
| DL | Aaron Hall | 2.1 | 0.8 solo, 2.1 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 7.9 | 4.0 solo, 3.2 ast, 0.23 sack, 0.48 PD, 0.19 INT |  |
| LB | Bobby Okereke | 5.6 | 4.2 solo, 2.4 ast, 0.15 sack, 0.69 PD, 0.11 INT | Questionable |
| LB | Patrick Jones II | 3.4 | 2.3 solo, 0.9 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Scott | 5.9 | 4.2 solo, 1.8 ast, 0.00 sack, 0.27 PD, 0.03 INT |  |
| DB | Zakee Wheatley | 4.5 | 2.7 solo, 1.0 ast, 0.00 sack, 0.59 PD, 0.18 INT |  |
| DB | Tre'von Moehrig | 3.9 | 2.5 solo, 1.9 ast, 0.15 sack, 0.00 PD, 0.00 INT |  |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 19.7 | 230 pass yd, 1.5 TD, 0.7 INT; 3.9 rush, 18 yd |  |
| RB | Alvin Kamara | 7.0 | 5.7 car, 23 yd, 0.28 TD; 2.7 rec, 19 yd, 0.15 TD | Questionable |
| RB | Kendre Miller | 6.7 | 7.9 car, 28 yd, 0.34 TD; 1.0 rec, 7 yd, 0.04 TD |  |
| RB | Audric Estimé | 5.9 | 6.1 car, 27 yd, 0.30 TD; 0.7 rec, 6 yd, 0.02 TD |  |
| WR | Chris Olave | 12.3 | 5.0 rec, 56 yd, 0.31 TD |  |
| WR | Devaughn Vele | 7.2 | 3.0 rec, 30 yd, 0.21 TD |  |
| WR | Jordyn Tyson | 6.3 | 3.0 rec, 27 yd, 0.10 TD |  |
| WR | Bryce Lance | 2.5 | 1.0 rec, 9 yd, 0.11 TD |  |
| TE | Juwan Johnson | 6.4 | 2.6 rec, 26 yd, 0.21 TD |  |
| TE | Noah Fant | 2.2 | 1.1 rec, 10 yd, 0.14 TD | Questionable |
| K | Daniel Carlson | 7.8 | 1.4 FG, 2.6 XP |  |
| DL | Carl Granderson | 6.8 | 2.0 solo, 2.5 ast, 1.03 sack, 0.25 PD, 0.05 INT |  |
| DL | Chase Young | 6.4 | 1.4 solo, 1.3 ast, 1.09 sack, 0.48 PD, 0.00 INT |  |
| LB | Pete Werner | 5.9 | 3.1 solo, 4.1 ast, 0.18 sack, 0.21 PD, 0.00 INT |  |
| LB | Kaden Elliss | 5.8 | 3.7 solo, 2.6 ast, 0.24 sack, 0.10 PD, 0.00 INT |  |
| LB | Danny Stutsman | 3.3 | 2.1 solo, 2.2 ast, 0.00 sack, 0.12 PD, 0.00 INT |  |
| DB | Jonas Sanker | 4.8 | 3.2 solo, 2.0 ast, 0.00 sack, 0.33 PD, 0.04 INT |  |
| DB | Julian Blackmon | 4.5 | 2.5 solo, 2.2 ast, 0.00 sack, 0.23 PD, 0.23 INT |  |
| DB | Kool-Aid McKinstry | 4.3 | 2.6 solo, 1.5 ast, 0.00 sack, 0.94 PD, 0.02 INT |  |

### HOU @ CLE

Market: CLE +5.0, total 41.5. Sim: HOU 23.3, CLE 18.2. CLE wins 35.4%, HOU wins 64.6%. Median margin -5.1 for CLE.

| Team stat | HOU | CLE |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 34 / 21 | 35 / 22 |
| Passing yards | 246 | 252 |
| Rush attempts / yards | 27 / 109 | 25 / 97 |
| Sacks taken | 2.6 | 2.9 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.1 / 0.9 |
| Field goals | 1.7 | 1.4 |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 19.2 | 246 pass yd, 1.5 TD, 0.6 INT; 2.1 rush, 9 yd |  |
| RB | Woody Marks | 6.9 | 10.7 car, 43 yd, 0.37 TD; 1.5 rec, 11 yd, 0.06 TD | Questionable |
| RB | Emari Demercado | 4.5 | 4.5 car, 20 yd, 0.09 TD; 1.0 rec, 9 yd, 0.04 TD |  |
| RB | David Montgomery | 4.0 | 6.1 car, 24 yd, 0.25 TD; 0.6 rec, 6 yd, 0.05 TD | Questionable |
| WR | Nico Collins | 9.5 | 3.5 rec, 43 yd, 0.25 TD |  |
| WR | Xavier Hutchinson | 6.7 | 2.7 rec, 27 yd, 0.18 TD |  |
| WR | Tank Dell | 6.3 | 2.6 rec, 42 yd, 0.21 TD | Questionable |
| WR | Kayshon Boutte | 6.1 | 2.1 rec, 29 yd, 0.18 TD |  |
| TE | Dalton Schultz | 8.0 | 3.8 rec, 35 yd, 0.14 TD |  |
| TE | Foster Moreau | 3.2 | 1.2 rec, 9 yd, 0.19 TD |  |
| K | Ka'imi Fairbairn | 10.8 | 2.2 FG, 2.3 XP |  |
| DL | Will Anderson Jr. | 6.3 | 2.1 solo, 1.6 ast, 1.01 sack, 0.08 PD, 0.00 INT |  |
| DL | Danielle Hunter | 4.3 | 1.2 solo, 1.4 ast, 0.57 sack, 0.37 PD, 0.00 INT |  |
| LB | Azeez Al-Shaair | 4.8 | 3.2 solo, 5.1 ast, 0.00 sack, 0.47 PD, 0.09 INT | Questionable |
| LB | Henry To'oTo'o | 4.6 | 2.2 solo, 3.0 ast, 0.09 sack, 0.22 PD, 0.00 INT |  |
| LB | Jake Hansen | 3.9 | 1.9 solo, 2.2 ast, 0.10 sack, 0.23 PD, 0.12 INT |  |
| DB | M.J. Stewart | 7.5 | 4.1 solo, 2.7 ast, 0.57 sack, 0.33 PD, 0.00 INT |  |
| DB | Kamari Lassiter | 6.6 | 3.8 solo, 1.8 ast, 0.13 sack, 1.35 PD, 0.07 INT |  |
| DB | Calen Bullock | 5.1 | 2.8 solo, 1.7 ast, 0.00 sack, 0.76 PD, 0.12 INT |  |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Shedeur Sanders | 17.2 | 252 pass yd, 1.1 TD, 0.7 INT; 3.0 rush, 13 yd |  |
| RB | Quinshon Judkins | 11.4 | 13.6 car, 47 yd, 0.52 TD; 2.0 rec, 15 yd, 0.04 TD |  |
| RB | Dylan Sampson | 7.2 | 4.2 car, 17 yd, 0.07 TD; 2.5 rec, 23 yd, 0.06 TD |  |
| RB | Jaleel McLaughlin | 2.7 | 1.8 car, 8 yd, 0.11 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | KC Concepcion | 10.3 | 1.1 car, 5 yd, 0.01 TD; 4.0 rec, 46 yd, 0.20 TD |  |
| WR | Denzel Boston | 7.5 | 3.9 rec, 47 yd, 0.25 TD | Questionable |
| WR | Jerry Jeudy | 5.2 | 2.3 rec, 24 yd, 0.08 TD |  |
| WR | Isaiah Bond | 1.9 | 0.7 rec, 10 yd, 0.02 TD |  |
| TE | Harold Fannin Jr. | 8.5 | 4.2 rec, 47 yd, 0.35 TD | Questionable |
| TE | Blake Whiteheart | 1.3 | 0.5 rec, 5 yd, 0.06 TD |  |
| K | Andre Szmyt | 9.1 | 1.9 FG, 1.9 XP |  |
| DL | Adin Huntington | 3.4 | 1.0 solo, 1.3 ast, 0.42 sack, 0.00 PD, 0.00 INT |  |
| DL | Mason Graham | 3.3 | 1.5 solo, 1.6 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 7.4 | 4.7 solo, 5.8 ast, 0.44 sack, 0.11 PD, 0.00 INT | Questionable |
| LB | Quincy Williams | 5.3 | 4.0 solo, 2.8 ast, 0.13 sack, 0.36 PD, 0.00 INT | Questionable |
| LB | Winston Reid | 1.0 | 0.9 solo, 0.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Tyson Campbell | 4.9 | 2.3 solo, 2.3 ast, 0.00 sack, 0.44 PD, 0.00 INT |  |
| DB | Grant Delpit | 4.9 | 3.0 solo, 1.6 ast, 0.14 sack, 0.32 PD, 0.08 INT |  |
| DB | Myles Harden | 4.8 | 2.1 solo, 1.6 ast, 0.30 sack, 0.74 PD, 0.06 INT |  |

### JAX @ TEN

Market: TEN +10.5, total 46.5. Sim: JAX 28.3, TEN 18.0. TEN wins 21.3%, JAX wins 78.7%. Median margin -10.3 for TEN.

| Team stat | JAX | TEN |
|---|---|---|
| Plays | 62 | 60 |
| Pass attempts / completions | 31 / 20 | 36 / 22 |
| Passing yards | 266 | 216 |
| Rush attempts / yards | 29 / 112 | 23 / 94 |
| Sacks taken | 2.3 | 2.2 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.7 / 1.4 | 1.2 / 0.7 |
| Field goals | 2.1 | 1.4 |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 21.7 | 266 pass yd, 1.7 TD, 0.6 INT; 3.3 rush, 13 yd |  |
| RB | Bhayshul Tuten | 9.9 | 13.4 car, 51 yd, 0.64 TD; 1.4 rec, 17 yd, 0.20 TD | Questionable |
| RB | Chris Rodriguez Jr. | 5.4 | 7.4 car, 29 yd, 0.50 TD; 0.6 rec, 6 yd, 0.02 TD | Questionable |
| RB | Ameer Abdullah | 2.0 | 3.2 car, 13 yd, 0.08 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Parker Washington | 12.1 | 3.7 rec, 60 yd, 0.39 TD |  |
| WR | Jakobi Meyers | 7.4 | 3.7 rec, 47 yd, 0.23 TD | Questionable |
| WR | Brian Thomas Jr. | 4.9 | 1.7 rec, 22 yd, 0.17 TD |  |
| WR | Josh Cameron | 3.2 | 1.1 rec, 14 yd, 0.12 TD |  |
| TE | Brenton Strange | 9.0 | 3.6 rec, 42 yd, 0.19 TD |  |
| TE | Nate Boerkircher | 4.2 | 1.3 rec, 19 yd, 0.17 TD |  |
| K | Cam Little | 9.6 | 1.8 FG, 2.9 XP |  |
| DL | Josh Hines-Allen | 3.8 | 1.9 solo, 1.2 ast, 0.30 sack, 0.15 PD, 0.00 INT |  |
| DL | Travon Walker | 2.2 | 1.2 solo, 1.3 ast, 0.32 sack, 0.12 PD, 0.00 INT | Questionable |
| LB | Foyesade Oluokun | 7.8 | 4.4 solo, 3.1 ast, 0.30 sack, 0.28 PD, 0.15 INT |  |
| LB | Ventrell Miller | 4.4 | 2.2 solo, 2.5 ast, 0.07 sack, 0.51 PD, 0.04 INT |  |
| LB | Jalen McLeod | 2.4 | 1.3 solo, 0.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Travis Hunter | 4.8 | 2.7 solo, 1.3 ast, 0.00 sack, 0.72 PD, 0.27 INT |  |
| DB | Jarrian Jones | 4.1 | 2.3 solo, 0.7 ast, 0.00 sack, 0.88 PD, 0.18 INT |  |
| DB | Montaric Brown | 3.9 | 2.4 solo, 0.5 ast, 0.00 sack, 0.62 PD, 0.22 INT |  |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 15.8 | 216 pass yd, 1.2 TD, 0.9 INT; 2.5 rush, 11 yd |  |
| RB | Tony Pollard | 12.0 | 14.3 car, 61 yd, 0.49 TD; 1.7 rec, 12 yd, 0.04 TD |  |
| RB | Tyjae Spears | 4.2 | 2.7 car, 10 yd, 0.06 TD; 2.5 rec, 15 yd, 0.05 TD | Questionable |
| RB | Michael Carter | 1.6 | 1.4 car, 6 yd, 0.02 TD; 0.5 rec, 4 yd, 0.01 TD |  |
| WR | Wan'Dale Robinson | 10.0 | 4.5 rec, 33 yd, 0.38 TD |  |
| WR | Carnell Tate | 8.3 | 4.6 rec, 49 yd, 0.25 TD | Questionable |
| WR | Elic Ayomanor | 5.5 | 2.1 rec, 25 yd, 0.16 TD |  |
| WR | Chimere Dike | 4.9 | 2.0 rec, 19 yd, 0.17 TD |  |
| TE | Gunnar Helm | 5.1 | 2.4 rec, 22 yd, 0.08 TD |  |
| TE | Daniel Bellinger | 2.7 | 1.3 rec, 11 yd, 0.04 TD |  |
| K | Joey Slye | 8.0 | 1.6 FG, 1.8 XP |  |
| DL | Jacob Martin | 4.4 | 1.4 solo, 0.3 ast, 0.88 sack, 0.26 PD, 0.00 INT |  |
| DL | Jermaine Johnson II | 2.9 | 1.3 solo, 1.0 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| LB | Anthony Hill Jr. | 6.1 | 4.9 solo, 5.4 ast, 0.00 sack, 0.27 PD, 0.00 INT | Questionable |
| LB | Cedric Gray | 4.7 | 3.0 solo, 3.0 ast, 0.05 sack, 0.00 PD, 0.00 INT |  |
| LB | Cody Barton | 2.2 | 1.6 solo, 2.2 ast, 0.00 sack, 0.18 PD, 0.00 INT | Questionable |
| DB | Amani Hooker | 7.5 | 3.8 solo, 2.3 ast, 0.00 sack, 0.74 PD, 0.61 INT |  |
| DB | Kevin Winston Jr. | 5.9 | 3.6 solo, 3.1 ast, 0.03 sack, 0.06 PD, 0.00 INT |  |
| DB | Alontae Taylor | 4.5 | 3.1 solo, 1.0 ast, 0.12 sack, 0.00 PD, 0.00 INT |  |

### KC @ ATL

Market: ATL +3.0, total 47.0. Sim: KC 25.0, ATL 22.3. ATL wins 42.1%, KC wins 57.9%. Median margin -2.7 for ATL.

| Team stat | KC | ATL |
|---|---|---|
| Plays | 62 | 63 |
| Pass attempts / completions | 33 / 22 | 33 / 21 |
| Passing yards | 239 | 220 |
| Rush attempts / yards | 26 / 124 | 27 / 115 |
| Sacks taken | 2.5 | 2.1 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.6 / 1.1 | 1.3 / 1.1 |
| Field goals | 1.9 | 1.7 |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 14.9 | 180 pass yd, 1.2 TD, 0.5 INT; 2.2 rush, 10 yd | Questionable |
| RB | Kenneth Walker III | 19.0 | 15.4 car, 75 yd, 0.65 TD; 3.2 rec, 23 yd, 0.39 TD |  |
| RB | Emmett Johnson | 6.4 | 2.4 car, 11 yd, 0.12 TD; 1.6 rec, 22 yd, 0.13 TD |  |
| RB | Kareem Hunt | 2.6 | 2.7 car, 11 yd, 0.09 TD; 0.5 rec, 5 yd, 0.02 TD |  |
| WR | Rashee Rice | 9.7 | 4.1 rec, 40 yd, 0.28 TD |  |
| WR | Xavier Worthy | 6.3 | 3.8 rec, 35 yd, 0.17 TD | Questionable |
| WR | Jalen Royals | 2.7 | 1.1 rec, 10 yd, 0.09 TD |  |
| WR | Cyrus Allen | 2.1 | 0.9 rec, 10 yd, 0.04 TD |  |
| TE | Travis Kelce | 10.7 | 4.0 rec, 48 yd, 0.25 TD |  |
| TE | Noah Gray | 4.4 | 1.8 rec, 19 yd, 0.13 TD |  |
| K | Harrison Butker | 8.5 | 1.6 FG, 2.5 XP |  |
| DL | George Karlaftis | 5.8 | 1.7 solo, 1.8 ast, 0.56 sack, 1.03 PD, 0.09 INT |  |
| DL | Chris Jones | 4.1 | 1.2 solo, 1.2 ast, 0.59 sack, 0.39 PD, 0.00 INT |  |
| LB | Nick Bolton | 8.4 | 4.9 solo, 5.4 ast, 0.04 sack, 0.24 PD, 0.04 INT |  |
| LB | Drue Tranquill | 7.0 | 4.4 solo, 4.2 ast, 0.00 sack, 0.16 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.8 | 1.3 solo, 1.7 ast, 0.00 sack, 0.09 PD, 0.11 INT |  |
| DB | Chamarri Conner | 5.1 | 3.2 solo, 2.1 ast, 0.16 sack, 0.17 PD, 0.05 INT |  |
| DB | Nohl Williams | 5.0 | 2.5 solo, 1.7 ast, 0.10 sack, 1.03 PD, 0.10 INT |  |
| DB | Jaden Hicks | 3.1 | 2.0 solo, 1.6 ast, 0.02 sack, 0.19 PD, 0.00 INT |  |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 16.7 | 220 pass yd, 1.3 TD, 0.9 INT; 3.4 rush, 14 yd |  |
| RB | Bijan Robinson | 21.9 | 19.4 car, 85 yd, 0.95 TD; 4.0 rec, 30 yd, 0.17 TD |  |
| RB | Khalil Herbert | 4.0 | 2.5 car, 10 yd, 0.05 TD; 1.4 rec, 11 yd, 0.04 TD |  |
| WR | Drake London | 12.8 | 5.2 rec, 62 yd, 0.23 TD |  |
| WR | Jahan Dotson | 6.8 | 2.2 rec, 35 yd, 0.18 TD |  |
| WR | Olamide Zaccheaus | 2.3 | 1.1 rec, 9 yd, 0.05 TD |  |
| WR | Chris Blair | 0.8 | 0.3 rec, 3 yd, 0.01 TD |  |
| TE | Kyle Pitts | 9.3 | 3.9 rec, 33 yd, 0.35 TD |  |
| TE | Austin Hooper | 2.7 | 1.2 rec, 10 yd, 0.08 TD |  |
| DL | LaCale London | 3.6 | 1.7 solo, 2.0 ast, 0.33 sack, 0.03 PD, 0.00 INT |  |
| DL | Cameron Thomas | 2.9 | 1.0 solo, 2.1 ast, 0.18 sack, 0.10 PD, 0.00 INT |  |
| LB | Kendal Daniels | 7.6 | 5.0 solo, 2.6 ast, 0.10 sack, 0.24 PD, 0.14 INT |  |
| LB | Harold Perkins Jr. | 4.6 | 2.7 solo, 2.0 ast, 0.20 sack, 0.09 PD, 0.00 INT |  |
| LB | Divine Deablo | 2.7 | 2.1 solo, 2.3 ast, 0.02 sack, 0.23 PD, 0.00 INT | Questionable |
| DB | Jessie Bates | 7.5 | 4.3 solo, 2.5 ast, 0.00 sack, 0.43 PD, 0.15 INT |  |
| DB | Xavier Watts | 6.0 | 3.1 solo, 3.4 ast, 0.04 sack, 0.33 PD, 0.14 INT |  |
| DB | C.J. Henderson | 5.7 | 3.5 solo, 1.4 ast, 0.00 sack, 1.01 PD, 0.04 INT |  |

### LA @ ARI

Market: ARI +9.5, total 39.0. Sim: LA 24.4, ARI 14.8. ARI wins 23.1%, LA wins 76.9%. Median margin -9.7 for ARI.

| Team stat | LA | ARI |
|---|---|---|
| Plays | 64 | 65 |
| Pass attempts / completions | 33 / 22 | 39 / 25 |
| Passing yards | 246 | 243 |
| Rush attempts / yards | 29 / 138 | 24 / 102 |
| Sacks taken | 2.1 | 2.6 |
| Interceptions thrown | 0.6 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.1 | 1.1 / 0.5 |
| Field goals | 1.9 | 1.1 |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 18.3 | 246 pass yd, 1.5 TD, 0.6 INT; 1.4 rush, 6 yd |  |
| RB | Kyren Williams | 20.6 | 15.0 car, 68 yd, 0.59 TD; 5.0 rec, 43 yd, 0.20 TD |  |
| RB | Blake Corum | 12.3 | 10.7 car, 54 yd, 0.47 TD; 1.5 rec, 18 yd, 0.15 TD |  |
| RB | Ronnie Rivers | 0.7 | 0.8 car, 4 yd, 0.02 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Konata Mumpfield | 5.9 | 2.2 rec, 28 yd, 0.15 TD |  |
| WR | Tutu Atwell | 4.8 | 1.8 rec, 25 yd, 0.08 TD |  |
| TE | Tyler Higbee | 11.7 | 4.6 rec, 55 yd, 0.27 TD |  |
| TE | Colby Parkinson | 7.6 | 4.2 rec, 39 yd, 0.36 TD | Questionable |
| K | Brandon McManus | 8.0 | 1.5 FG, 2.5 XP |  |
| DL | Braden Fiske | 2.8 | 1.4 solo, 1.0 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| DL | Aaron Donald | 1.6 | 1.0 solo, 0.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Myles Garrett | 11.8 | 3.2 solo, 0.0 ast, 3.49 sack, 0.00 PD, 0.00 INT | Questionable |
| LB | Nate Landman | 7.1 | 4.1 solo, 3.3 ast, 0.05 sack, 0.31 PD, 0.04 INT |  |
| LB | Omar Speights | 5.3 | 3.1 solo, 2.1 ast, 0.17 sack, 0.22 PD, 0.00 INT |  |
| DB | Quentin Lake | 8.5 | 4.0 solo, 3.2 ast, 0.00 sack, 1.19 PD, 0.40 INT |  |
| DB | Josh Wallace | 4.7 | 3.0 solo, 1.4 ast, 0.00 sack, 0.64 PD, 0.13 INT |  |
| DB | Kamren Kinchens | 4.1 | 2.6 solo, 2.3 ast, 0.04 sack, 0.24 PD, 0.00 INT |  |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 16.8 | 243 pass yd, 1.1 TD, 0.8 INT; 4.2 rush, 17 yd |  |
| RB | Tyler Allgeier | 14.8 | 13.6 car, 58 yd, 0.36 TD; 3.7 rec, 27 yd, 0.12 TD |  |
| RB | Bam Knight | 4.6 | 5.6 car, 26 yd, 0.07 TD; 1.6 rec, 14 yd, 0.03 TD | Questionable |
| RB | Evan Hull | 2.6 | 0.0 car, 0 yd, 0.00 TD; 1.2 rec, 12 yd, 0.03 TD |  |
| WR | Reggie Virgil | 4.7 | 2.0 rec, 24 yd, 0.06 TD |  |
| WR | Devin Duvernay | 1.5 | 0.8 rec, 7 yd, 0.01 TD |  |
| WR | Xavier Weaver | 0.8 | 0.5 rec, 5 yd, 0.01 TD | Questionable |
| WR | Simi Fehoko | 0.8 | 0.4 rec, 4 yd, 0.00 TD |  |
| TE | Trey McBride | 24.4 | 12.2 rec, 98 yd, 0.42 TD |  |
| TE | Elijah Higgins | 6.8 | 3.4 rec, 30 yd, 0.09 TD |  |
| K | Chad Ryland | 8.8 | 1.9 FG, 1.5 XP |  |
| DL | Andrew Billings | 2.6 | 1.2 solo, 1.2 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.6 | 1.1 solo, 1.9 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.2 | 2.9 solo, 4.3 ast, 0.03 sack, 0.07 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.1 | 2.6 solo, 4.1 ast, 0.00 sack, 0.23 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.3 | 1.6 solo, 1.0 ast, 0.21 sack, 0.14 PD, 0.00 INT |  |
| DB | Budda Baker | 6.9 | 3.2 solo, 4.1 ast, 0.26 sack, 0.34 PD, 0.08 INT |  |
| DB | Denzel Burke | 4.5 | 2.6 solo, 0.9 ast, 0.00 sack, 0.96 PD, 0.11 INT |  |
| DB | Andrew Wingard | 4.0 | 3.1 solo, 3.4 ast, 0.00 sack, 0.08 PD, 0.08 INT | Questionable |

### LAC @ BAL

Market: BAL -4.0, total 38.5. Sim: LAC 17.3, BAL 21.3. BAL wins 62.3%, LAC wins 37.7%. Median margin +3.7 for BAL.

| Team stat | LAC | BAL |
|---|---|---|
| Plays | 63 | 60 |
| Pass attempts / completions | 34 / 21 | 29 / 18 |
| Passing yards | 246 | 208 |
| Rush attempts / yards | 27 / 105 | 29 / 133 |
| Sacks taken | 2.2 | 2.0 |
| Interceptions thrown | 0.9 | 0.7 |
| Passing / rushing TDs | 1.1 / 0.8 | 1.1 / 1.2 |
| Field goals | 1.3 | 1.6 |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.6 | 246 pass yd, 1.1 TD, 0.9 INT; 3.6 rush, 16 yd | Questionable |
| RB | Omarion Hampton | 9.1 | 10.6 car, 38 yd, 0.39 TD; 1.6 rec, 11 yd, 0.05 TD |  |
| RB | Keaton Mitchell | 6.8 | 4.9 car, 19 yd, 0.07 TD; 2.3 rec, 17 yd, 0.09 TD |  |
| RB | Kimani Vidal | 6.2 | 5.4 car, 22 yd, 0.18 TD; 1.4 rec, 12 yd, 0.08 TD |  |
| WR | Quentin Johnston | 7.0 | 2.2 rec, 37 yd, 0.16 TD |  |
| WR | Tre Harris | 6.4 | 2.8 rec, 31 yd, 0.08 TD |  |
| WR | Ladd McConkey | 4.7 | 2.3 rec, 32 yd, 0.14 TD | Questionable |
| WR | KeAndre Lambert-Smith | 3.6 | 1.4 rec, 17 yd, 0.08 TD |  |
| TE | Oronde Gadsden II | 5.6 | 2.5 rec, 24 yd, 0.11 TD |  |
| TE | Charlie Kolar | 4.8 | 2.2 rec, 22 yd, 0.06 TD |  |
| K | Cameron Dicker | 9.0 | 1.9 FG, 1.8 XP |  |
| DL | Justin Eboigbe | 1.9 | 1.1 solo, 1.7 ast, 0.13 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Teair Tart | 1.7 | 1.1 solo, 1.1 ast, 0.00 sack, 0.06 PD, 0.00 INT |  |
| LB | Daiyan Henley | 5.6 | 2.6 solo, 3.3 ast, 0.04 sack, 0.28 PD, 0.16 INT |  |
| LB | Tuli Tuipulotu | 4.9 | 1.8 solo, 1.6 ast, 0.41 sack, 0.24 PD, 0.07 INT |  |
| LB | Del'Shawn Phillips | 3.4 | 2.0 solo, 2.7 ast, 0.04 sack, 0.00 PD, 0.00 INT |  |
| DB | Tony Jefferson | 4.4 | 2.7 solo, 2.2 ast, 0.06 sack, 0.20 PD, 0.05 INT |  |
| DB | Tarheeb Still | 3.9 | 2.3 solo, 1.4 ast, 0.00 sack, 0.36 PD, 0.11 INT |  |
| DB | Cam Hart | 3.8 | 2.0 solo, 1.5 ast, 0.00 sack, 0.53 PD, 0.18 INT |  |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Fagnano | 15.5 | 208 pass yd, 1.1 TD, 0.7 INT; 3.4 rush, 15 yd |  |
| RB | Derrick Henry | 15.3 | 19.5 car, 83 yd, 0.84 TD; 1.0 rec, 8 yd, 0.07 TD |  |
| RB | Justice Hill | 8.0 | 4.1 car, 24 yd, 0.20 TD; 2.4 rec, 16 yd, 0.07 TD |  |
| RB | Rasheen Ali | 1.1 | 0.8 car, 4 yd, 0.01 TD; 0.3 rec, 3 yd, 0.03 TD |  |
| WR | Zay Flowers | 14.1 | 0.8 car, 4 yd, 0.03 TD; 5.1 rec, 63 yd, 0.36 TD |  |
| WR | Rashod Bateman | 4.8 | 1.9 rec, 24 yd, 0.09 TD |  |
| WR | Ja'Kobi Lane | 3.0 | 1.4 rec, 14 yd, 0.04 TD |  |
| WR | Devontez Walker | 2.3 | 0.7 rec, 9 yd, 0.11 TD |  |
| TE | Mark Andrews | 6.2 | 3.0 rec, 25 yd, 0.11 TD |  |
| TE | Josh Cuevas | 3.5 | 1.3 rec, 15 yd, 0.12 TD |  |
| DL | Nnamdi Madubuike | 3.1 | 1.5 solo, 1.5 ast, 0.17 sack, 0.40 PD, 0.00 INT |  |
| DL | Travis Jones | 2.7 | 1.3 solo, 1.5 ast, 0.13 sack, 0.06 PD, 0.00 INT |  |
| LB | Roquan Smith | 7.3 | 3.7 solo, 4.4 ast, 0.17 sack, 0.31 PD, 0.05 INT |  |
| LB | Trenton Simpson | 5.6 | 3.1 solo, 3.3 ast, 0.12 sack, 0.07 PD, 0.08 INT |  |
| LB | Mike Green | 2.9 | 1.1 solo, 1.3 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| DB | Malaki Starks | 5.1 | 3.2 solo, 2.2 ast, 0.05 sack, 0.15 PD, 0.00 INT |  |
| DB | K'Von Wallace | 5.1 | 4.4 solo, 0.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Marlon Humphrey | 4.8 | 2.3 solo, 1.5 ast, 0.00 sack, 1.20 PD, 0.11 INT |  |

### MIA @ IND

Market: IND -3.5, total 38.0. Sim: MIA 17.0, IND 21.0. IND wins 62.1%, MIA wins 37.9%. Median margin +4.3 for IND.

| Team stat | MIA | IND |
|---|---|---|
| Plays | 59 | 63 |
| Pass attempts / completions | 30 / 19 | 32 / 20 |
| Passing yards | 231 | 213 |
| Rush attempts / yards | 26 / 120 | 28 / 115 |
| Sacks taken | 1.9 | 2.4 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.0 / 0.9 | 1.1 / 1.1 |
| Field goals | 1.3 | 1.5 |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Zach Wilson | 0.0 | 0 pass yd, 0.0 TD, 0.0 INT |  |
| RB | Ollie Gordon II | 15.7 | 21.9 car, 97 yd, 0.78 TD; 0.9 rec, 7 yd, 0.02 TD |  |
| RB | Kaytron Allen | 1.8 | 1.1 car, 6 yd, 0.02 TD; 0.4 rec, 7 yd, 0.01 TD |  |
| RB | DJ Herman | 0.9 | 0.0 car, 0 yd, 0.00 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Malik Washington | 10.8 | 1.8 car, 9 yd, 0.07 TD; 4.2 rec, 42 yd, 0.20 TD |  |
| WR | Caleb Douglas | 10.6 | 3.9 rec, 52 yd, 0.27 TD |  |
| WR | Kevin Coleman Jr. | 5.0 | 1.6 rec, 18 yd, 0.23 TD |  |
| WR | Chris Bell | 3.6 | 2.0 rec, 22 yd, 0.05 TD | Questionable |
| TE | Greg Dulcich | 8.5 | 3.7 rec, 42 yd, 0.10 TD |  |
| TE | Will Kacmarek | 1.4 | 0.8 rec, 8 yd, 0.03 TD | Questionable |
| K | Riley Patterson | 6.9 | 1.4 FG, 1.7 XP |  |
| DL | Jordan Phillips | 2.3 | 1.3 solo, 1.9 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DL | Zeek Biggers | 2.1 | 0.7 solo, 1.4 ast, 0.19 sack, 0.11 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 8.1 | 4.3 solo, 5.2 ast, 0.17 sack, 0.10 PD, 0.09 INT |  |
| LB | Jordyn Brooks | 7.2 | 4.1 solo, 5.6 ast, 0.03 sack, 0.20 PD, 0.00 INT |  |
| LB | Joshua Uche | 5.2 | 2.5 solo, 1.8 ast, 0.45 sack, 0.19 PD, 0.00 INT |  |
| DB | Michael Taaffe | 5.5 | 2.9 solo, 3.0 ast, 0.00 sack, 0.22 PD, 0.21 INT |  |
| DB | Chris Johnson | 4.7 | 2.3 solo, 2.5 ast, 0.00 sack, 0.32 PD, 0.19 INT |  |
| DB | Dante Trader Jr. | 3.7 | 2.2 solo, 2.3 ast, 0.00 sack, 0.22 PD, 0.05 INT |  |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 15.2 | 213 pass yd, 1.1 TD, 0.9 INT; 2.7 rush, 11 yd |  |
| RB | Jonathan Taylor | 14.6 | 15.2 car, 59 yd, 0.62 TD; 2.6 rec, 23 yd, 0.06 TD |  |
| RB | Seth McGowan | 4.0 | 4.6 car, 22 yd, 0.18 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| RB | DJ Giddens | 1.3 | 2.2 car, 10 yd, 0.06 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Keenan Allen | 9.7 | 4.5 rec, 42 yd, 0.18 TD |  |
| WR | Josh Downs | 8.2 | 3.4 rec, 35 yd, 0.21 TD |  |
| WR | Laquon Treadwell | 3.5 | 1.4 rec, 18 yd, 0.04 TD |  |
| WR | Ashton Dulin | 2.8 | 0.6 rec, 10 yd, 0.17 TD |  |
| TE | Tyler Warren | 9.2 | 4.1 rec, 34 yd, 0.21 TD |  |
| TE | Mo Alie-Cox | 2.1 | 0.9 rec, 8 yd, 0.17 TD | Questionable |
| K | Spencer Shrader | 9.8 | 2.0 FG, 2.2 XP |  |
| DL | Adetomiwa Adebawore | 3.5 | 1.3 solo, 1.2 ast, 0.40 sack, 0.38 PD, 0.00 INT |  |
| DL | Jaylahn Tuimoloau | 3.2 | 1.0 solo, 1.4 ast, 0.26 sack, 0.50 PD, 0.00 INT |  |
| LB | CJ Allen | 3.8 | 1.5 solo, 3.1 ast, 0.19 sack, 0.21 PD, 0.00 INT |  |
| LB | Akeem Davis-Gaither | 3.8 | 3.2 solo, 3.4 ast, 0.00 sack, 0.08 PD, 0.00 INT | Questionable |
| LB | Bryce Boettcher | 3.2 | 1.6 solo, 3.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Camryn Bynum | 3.7 | 2.1 solo, 1.3 ast, 0.00 sack, 0.52 PD, 0.12 INT |  |
| DB | Hunter Wohler | 3.7 | 2.3 solo, 2.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Sauce Gardner | 3.5 | 2.4 solo, 0.6 ast, 0.00 sack, 0.79 PD, 0.00 INT |  |

### MIN @ GB

Market: GB -3.0, total 42.0. Sim: MIN 19.3, GB 22.6. GB wins 59.7%, MIN wins 40.3%. Median margin +3.1 for GB.

| Team stat | MIN | GB |
|---|---|---|
| Plays | 59 | 61 |
| Pass attempts / completions | 32 / 20 | 31 / 20 |
| Passing yards | 210 | 212 |
| Rush attempts / yards | 24 / 102 | 27 / 96 |
| Sacks taken | 2.2 | 3.4 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 1.3 / 0.7 | 1.3 / 1.1 |
| Field goals | 1.4 | 1.7 |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Max Brosmer | 11.2 | 157 pass yd, 1.0 TD, 0.6 INT |  |
| RB | Aaron Jones | 10.7 | 11.0 car, 43 yd, 0.38 TD; 2.2 rec, 16 yd, 0.07 TD |  |
| RB | Jordan Mason | 5.4 | 6.8 car, 30 yd, 0.21 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| RB | DeeJay Dallas | 1.2 | 0.4 car, 2 yd, 0.01 TD; 0.5 rec, 4 yd, 0.01 TD |  |
| WR | Justin Jefferson | 13.2 | 5.0 rec, 54 yd, 0.47 TD |  |
| WR | Jordan Addison | 7.9 | 2.9 rec, 36 yd, 0.17 TD |  |
| WR | Jauan Jennings | 1.8 | 1.1 rec, 11 yd, 0.04 TD | Questionable |
| WR | Myles Price | 1.7 | 0.8 rec, 7 yd, 0.03 TD |  |
| TE | T.J. Hockenson | 7.9 | 4.4 rec, 39 yd, 0.41 TD | Questionable |
| TE | Gavin Bartholomew | 3.2 | 1.5 rec, 14 yd, 0.04 TD |  |
| K | Will Reichard | 9.5 | 2.0 FG, 1.9 XP |  |
| DL | Jalen Redmond | 3.8 | 1.8 solo, 1.6 ast, 0.18 sack, 0.35 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 2.2 | 1.1 solo, 1.5 ast, 0.10 sack, 0.00 PD, 0.00 INT |  |
| LB | Blake Cashman | 7.5 | 5.0 solo, 5.2 ast, 0.47 sack, 0.82 PD, 0.00 INT | Questionable |
| LB | Eric Wilson | 6.1 | 3.1 solo, 3.6 ast, 0.37 sack, 0.07 PD, 0.00 INT |  |
| LB | Andrew Van Ginkel | 5.9 | 1.7 solo, 1.7 ast, 0.82 sack, 0.27 PD, 0.10 INT |  |
| DB | Byron Murphy | 6.1 | 3.2 solo, 1.2 ast, 0.00 sack, 0.78 PD, 0.48 INT |  |
| DB | Josh Metellus | 5.7 | 3.4 solo, 3.5 ast, 0.04 sack, 0.44 PD, 0.00 INT |  |
| DB | James Pierre | 4.8 | 3.3 solo, 0.7 ast, 0.00 sack, 0.43 PD, 0.24 INT |  |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 17.9 | 212 pass yd, 1.3 TD, 0.7 INT; 2.2 rush, 8 yd |  |
| RB | Pierre Strong | 7.0 | 8.4 car, 27 yd, 0.18 TD; 1.8 rec, 12 yd, 0.05 TD |  |
| RB | Kaleb Johnson | 6.6 | 10.3 car, 38 yd, 0.44 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Christian Watson | 14.2 | 5.2 rec, 66 yd, 0.40 TD |  |
| WR | Matthew Golden | 13.7 | 5.4 rec, 58 yd, 0.41 TD |  |
| WR | Savion Williams | 3.7 | 2.3 car, 9 yd, 0.05 TD; 1.7 rec, 13 yd, 0.12 TD | Questionable |
| WR | Bo Melton | 1.0 | 0.6 rec, 5 yd, 0.04 TD | Questionable |
| TE | Tucker Kraft | 8.5 | 0.9 car, 4 yd, 0.02 TD; 3.7 rec, 29 yd, 0.24 TD |  |
| TE | Jonnu Smith | 1.4 | 0.7 rec, 6 yd, 0.02 TD |  |
| K | Trey Smack | 6.2 | 1.6 FG, 2.3 XP | Questionable |
| DL | Barryn Sorrell | 3.0 | 1.8 solo, 1.1 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| DL | Brenton Cox Jr. | 3.0 | 1.2 solo, 0.9 ast, 0.25 sack, 0.00 PD, 0.00 INT |  |
| LB | Isaiah McDuffie | 5.9 | 2.8 solo, 3.3 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Ty'Ron Hopper | 3.5 | 1.8 solo, 1.7 ast, 0.15 sack, 0.65 PD, 0.24 INT | Questionable |
| LB | Dani Dennis-Sutton | 3.3 | 1.0 solo, 1.5 ast, 0.35 sack, 0.25 PD, 0.00 INT |  |
| DB | Evan Williams | 7.7 | 4.4 solo, 2.7 ast, 0.08 sack, 0.63 PD, 0.31 INT |  |
| DB | Xavier McKinney | 6.2 | 2.6 solo, 2.1 ast, 0.07 sack, 0.78 PD, 0.52 INT |  |
| DB | Brandon Cisse | 4.9 | 2.4 solo, 1.3 ast, 0.13 sack, 1.10 PD, 0.11 INT |  |

### NE @ DET

Market: DET -3.0, total 51.0. Sim: NE 24.0, DET 27.1. DET wins 59.1%, NE wins 40.9%. Median margin +3.1 for DET.

| Team stat | NE | DET |
|---|---|---|
| Plays | 61 | 65 |
| Pass attempts / completions | 32 / 21 | 34 / 23 |
| Passing yards | 261 | 260 |
| Rush attempts / yards | 26 / 122 | 28 / 117 |
| Sacks taken | 2.6 | 2.7 |
| Interceptions thrown | 0.8 | 0.6 |
| Passing / rushing TDs | 1.5 / 1.1 | 1.7 / 1.2 |
| Field goals | 1.8 | 2.0 |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 22.1 | 261 pass yd, 1.5 TD, 0.8 INT; 5.4 rush, 24 yd |  |
| RB | Corey Kiner | 5.0 | 6.5 car, 32 yd, 0.25 TD; 0.2 rec, 1 yd, 0.00 TD |  |
| RB | Rhamondre Stevenson | 3.7 | 11.3 car, 51 yd, 0.42 TD; 3.0 rec, 31 yd, 0.21 TD | Questionable |
| RB | Lan Larison | 1.1 | 0.8 car, 4 yd, 0.01 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | DeMario Douglas | 9.8 | 3.6 rec, 46 yd, 0.27 TD |  |
| WR | Mack Hollins | 7.2 | 2.8 rec, 32 yd, 0.20 TD |  |
| WR | Efton Chism III | 6.3 | 2.6 rec, 26 yd, 0.18 TD |  |
| WR | A.J. Brown | 3.8 | 2.1 rec, 23 yd, 0.10 TD | Questionable |
| TE | Hunter Henry | 6.9 | 3.9 rec, 41 yd, 0.20 TD | Questionable |
| TE | Eli Raridon | 6.2 | 2.3 rec, 29 yd, 0.16 TD |  |
| K | Andy Borregales | 7.4 | 1.3 FG, 2.4 XP |  |
| DL | Christian Barmore | 3.4 | 1.0 solo, 0.7 ast, 0.61 sack, 0.00 PD, 0.00 INT |  |
| DL | Cory Durden | 2.7 | 1.4 solo, 1.5 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Christian Elliss | 6.2 | 3.5 solo, 4.0 ast, 0.13 sack, 0.16 PD, 0.00 INT |  |
| LB | Elijah Ponder | 5.1 | 1.4 solo, 1.0 ast, 0.82 sack, 0.13 PD, 0.00 INT |  |
| LB | Robert Spillane | 3.8 | 1.7 solo, 3.4 ast, 0.00 sack, 0.28 PD, 0.00 INT |  |
| DB | Marcus Jones | 5.3 | 3.0 solo, 2.1 ast, 0.16 sack, 0.52 PD, 0.07 INT |  |
| DB | Craig Woodson | 5.0 | 2.8 solo, 2.2 ast, 0.00 sack, 0.28 PD, 0.09 INT |  |
| DB | Christian Gonzalez | 5.0 | 4.0 solo, 0.7 ast, 0.00 sack, 0.58 PD, 0.00 INT |  |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 20.8 | 260 pass yd, 1.7 TD, 0.6 INT; 2.2 rush, 8 yd | Questionable |
| RB | Jahmyr Gibbs | 22.8 | 21.2 car, 90 yd, 1.00 TD; 3.6 rec, 30 yd, 0.24 TD |  |
| RB | Sione Vaki | 2.3 | 3.3 car, 15 yd, 0.07 TD; 0.6 rec, 5 yd, 0.02 TD | Questionable |
| WR | Amon-Ra St. Brown | 12.8 | 7.0 rec, 71 yd, 0.47 TD | Questionable |
| WR | Jameson Williams | 11.4 | 3.6 rec, 52 yd, 0.42 TD |  |
| WR | Isaac TeSlaa | 4.5 | 1.5 rec, 21 yd, 0.14 TD |  |
| WR | DeAndre Carter | 0.6 | 0.3 rec, 3 yd, 0.00 TD |  |
| TE | Sam LaPorta | 9.9 | 3.9 rec, 41 yd, 0.30 TD |  |
| TE | Tyler Conklin | 1.6 | 0.8 rec, 7 yd, 0.03 TD |  |
| K | Jake Bates | 10.3 | 2.0 FG, 2.7 XP |  |
| DL | Aidan Hutchinson | 4.6 | 1.9 solo, 1.1 ast, 0.61 sack, 0.14 PD, 0.03 INT |  |
| DL | Alim McNeill | 3.3 | 0.9 solo, 1.1 ast, 0.59 sack, 0.10 PD, 0.00 INT |  |
| LB | Derrick Barnes | 4.3 | 2.4 solo, 1.5 ast, 0.23 sack, 0.19 PD, 0.09 INT |  |
| LB | Malcolm Rodriguez | 2.7 | 1.5 solo, 1.9 ast, 0.05 sack, 0.16 PD, 0.00 INT |  |
| LB | Trevor Nowaske | 1.8 | 1.4 solo, 0.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Chuck Clark | 6.2 | 3.3 solo, 2.4 ast, 0.10 sack, 0.40 PD, 0.26 INT |  |
| DB | Roger McCreary | 5.1 | 3.1 solo, 1.1 ast, 0.08 sack, 1.04 PD, 0.00 INT |  |
| DB | D.J. Reed | 4.1 | 3.3 solo, 1.4 ast, 0.00 sack, 0.89 PD, 0.17 INT | Questionable |

### PIT @ CIN

Market: CIN -3.5, total 49.5. Sim: PIT 23.0, CIN 26.6. CIN wins 61.1%, PIT wins 38.9%. Median margin +3.4 for CIN.

| Team stat | PIT | CIN |
|---|---|---|
| Plays | 64 | 63 |
| Pass attempts / completions | 35 / 22 | 36 / 25 |
| Passing yards | 234 | 277 |
| Rush attempts / yards | 25 / 133 | 25 / 98 |
| Sacks taken | 3.2 | 2.9 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.8 / 1.1 |
| Field goals | 1.7 | 2.0 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 17.8 | 234 pass yd, 1.5 TD, 0.7 INT; 1.3 rush, 6 yd |  |
| RB | Jaylen Warren | 18.3 | 14.1 car, 81 yd, 0.50 TD; 3.1 rec, 31 yd, 0.18 TD |  |
| RB | Rico Dowdle | 9.7 | 7.5 car, 34 yd, 0.32 TD; 2.3 rec, 18 yd, 0.07 TD |  |
| WR | Germie Bernard | 11.4 | 5.4 rec, 45 yd, 0.25 TD |  |
| WR | DK Metcalf | 11.2 | 4.6 rec, 50 yd, 0.26 TD |  |
| WR | Scott Miller | 1.8 | 0.9 rec, 8 yd, 0.03 TD |  |
| WR | Brandon Smith | 1.6 | 0.7 rec, 7 yd, 0.02 TD |  |
| TE | Pat Freiermuth | 9.1 | 3.2 rec, 31 yd, 0.33 TD |  |
| TE | Darnell Washington | 7.6 | 2.6 rec, 31 yd, 0.32 TD |  |
| K | Chris Boswell | 9.7 | 2.0 FG, 2.3 XP |  |
| DL | Cameron Heyward | 5.1 | 2.0 solo, 2.1 ast, 0.42 sack, 0.58 PD, 0.00 INT |  |
| DL | Kevin Jobity Jr. | 4.2 | 1.0 solo, 0.0 ast, 1.06 sack, 0.00 PD, 0.00 INT |  |
| LB | Patrick Queen | 7.3 | 3.0 solo, 4.4 ast, 0.37 sack, 0.45 PD, 0.08 INT |  |
| LB | Payton Wilson | 7.2 | 4.1 solo, 3.7 ast, 0.13 sack, 0.33 PD, 0.14 INT |  |
| LB | T.J. Watt | 6.3 | 1.5 solo, 0.9 ast, 0.88 sack, 0.43 PD, 0.14 INT |  |
| DB | Jamel Dean | 6.0 | 2.8 solo, 1.5 ast, 0.00 sack, 1.26 PD, 0.16 INT |  |
| DB | Jalen Ramsey | 5.8 | 3.5 solo, 2.3 ast, 0.26 sack, 0.26 PD, 0.00 INT |  |
| DB | Jaquan Brisker | 5.4 | 3.2 solo, 3.2 ast, 0.00 sack, 0.36 PD, 0.09 INT |  |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 23.1 | 277 pass yd, 1.8 TD, 0.8 INT; 2.7 rush, 11 yd |  |
| RB | Chase Brown | 16.0 | 13.0 car, 52 yd, 0.44 TD; 4.5 rec, 27 yd, 0.18 TD |  |
| RB | Samaje Perine | 6.5 | 6.8 car, 27 yd, 0.30 TD; 1.0 rec, 8 yd, 0.06 TD |  |
| WR | Ja'Marr Chase | 17.6 | 7.0 rec, 77 yd, 0.48 TD |  |
| WR | Tee Higgins | 15.4 | 5.6 rec, 72 yd, 0.45 TD |  |
| WR | Dohnte Meyers | 5.1 | 2.2 rec, 24 yd, 0.08 TD |  |
| WR | Mitchell Tinsley | 2.3 | 1.0 rec, 11 yd, 0.04 TD |  |
| TE | Mike Gesicki | 6.5 | 2.3 rec, 26 yd, 0.27 TD |  |
| TE | Drew Sample | 2.6 | 1.1 rec, 10 yd, 0.07 TD |  |
| K | Evan McPherson | 8.2 | 1.5 FG, 2.7 XP |  |
| DL | Boye Mafe | 5.4 | 1.9 solo, 1.1 ast, 0.73 sack, 0.14 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 5.1 | 1.9 solo, 1.6 ast, 0.65 sack, 0.15 PD, 0.00 INT |  |
| LB | Barrett Carter | 7.6 | 3.1 solo, 4.9 ast, 0.14 sack, 0.58 PD, 0.21 INT |  |
| LB | Demetrius Knight Jr. | 6.6 | 3.6 solo, 3.4 ast, 0.13 sack, 0.20 PD, 0.16 INT |  |
| LB | Joe Giles-Harris | 1.5 | 1.0 solo, 0.9 ast, 0.00 sack, 0.05 PD, 0.00 INT |  |
| DB | Jordan Battle | 7.6 | 4.6 solo, 2.1 ast, 0.00 sack, 0.86 PD, 0.33 INT |  |
| DB | Bryan Cook | 5.7 | 3.9 solo, 2.4 ast, 0.09 sack, 0.00 PD, 0.00 INT |  |
| DB | Daxton Hill | 4.4 | 3.0 solo, 1.1 ast, 0.00 sack, 0.67 PD, 0.00 INT |  |

### SEA @ LV

Market: LV +6.5, total 40.5. Sim: SEA 23.5, LV 17.1. LV wins 31.3%, SEA wins 68.7%. Median margin -6.3 for LV.

| Team stat | SEA | LV |
|---|---|---|
| Plays | 61 | 60 |
| Pass attempts / completions | 30 / 19 | 35 / 22 |
| Passing yards | 217 | 228 |
| Rush attempts / yards | 28 / 124 | 23 / 74 |
| Sacks taken | 2.3 | 2.4 |
| Interceptions thrown | 0.7 | 0.9 |
| Passing / rushing TDs | 1.4 / 1.2 | 1.1 / 0.7 |
| Field goals | 1.8 | 1.3 |

**SEA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drew Lock | 16.2 | 217 pass yd, 1.4 TD, 0.7 INT; 1.1 rush, 5 yd | Questionable |
| RB | Emanuel Wilson | 9.3 | 11.1 car, 46 yd, 0.49 TD; 0.7 rec, 8 yd, 0.07 TD |  |
| RB | Zach Charbonnet | 7.2 | 6.3 car, 31 yd, 0.28 TD; 1.3 rec, 10 yd, 0.04 TD |  |
| RB | Jadarian Price | 6.7 | 5.8 car, 24 yd, 0.13 TD; 1.7 rec, 16 yd, 0.06 TD |  |
| WR | Jaxon Smith-Njigba | 20.3 | 7.6 rec, 92 yd, 0.58 TD |  |
| WR | Cooper Kupp | 5.9 | 2.4 rec, 24 yd, 0.18 TD |  |
| WR | Tory Horton | 4.0 | 1.6 rec, 17 yd, 0.12 TD |  |
| TE | AJ Barner | 7.2 | 0.7 car, 3 yd, 0.13 TD; 2.7 rec, 24 yd, 0.19 TD |  |
| TE | Eric Saubert | 1.3 | 0.5 rec, 5 yd, 0.06 TD |  |
| K | Jason Myers | 9.1 | 1.8 FG, 2.4 XP |  |
| DL | Byron Murphy II | 3.4 | 1.3 solo, 1.8 ast, 0.40 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Williams | 2.1 | 1.5 solo, 1.0 ast, 0.21 sack, 0.13 PD, 0.00 INT | Questionable |
| LB | Ernest Jones | 8.3 | 4.3 solo, 4.8 ast, 0.27 sack, 0.52 PD, 0.08 INT |  |
| LB | Drake Thomas | 4.9 | 2.2 solo, 3.3 ast, 0.07 sack, 0.21 PD, 0.15 INT |  |
| LB | DeMarcus Lawrence | 3.7 | 1.2 solo, 1.3 ast, 0.19 sack, 0.32 PD, 0.00 INT |  |
| DB | Devon Witherspoon | 5.5 | 3.8 solo, 2.3 ast, 0.00 sack, 0.42 PD, 0.03 INT |  |
| DB | Julian Love | 5.0 | 3.1 solo, 1.5 ast, 0.00 sack, 0.64 PD, 0.16 INT |  |
| DB | Nick Emmanwori | 4.9 | 2.9 solo, 1.6 ast, 0.25 sack, 0.33 PD, 0.03 INT |  |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 15.8 | 228 pass yd, 1.1 TD, 0.9 INT; 2.1 rush, 6 yd |  |
| RB | Ashton Jeanty | 12.5 | 10.9 car, 34 yd, 0.26 TD; 3.9 rec, 29 yd, 0.15 TD |  |
| RB | Mike Washington Jr. | 4.1 | 8.0 car, 26 yd, 0.17 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| RB | Dylan Laube | 1.0 | 0.5 car, 2 yd, 0.06 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 8.2 | 3.2 rec, 38 yd, 0.19 TD |  |
| WR | Jalen Nailor | 3.9 | 1.9 rec, 15 yd, 0.09 TD |  |
| WR | Cody White | 2.6 | 1.0 rec, 10 yd, 0.10 TD |  |
| WR | Jack Bech | 2.3 | 1.1 rec, 10 yd, 0.04 TD |  |
| TE | Brock Bowers | 12.8 | 5.3 rec, 56 yd, 0.32 TD |  |
| TE | Michael Mayer | 7.1 | 3.5 rec, 32 yd, 0.08 TD |  |
| K | Matt Gay | 8.7 | 1.9 FG, 1.7 XP |  |
| DL | Maxx Crosby | 4.0 | 1.4 solo, 1.7 ast, 0.44 sack, 0.06 PD, 0.00 INT |  |
| DL | Tim Keenan III | 2.5 | 0.7 solo, 1.7 ast, 0.31 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 9.1 | 4.4 solo, 6.9 ast, 0.09 sack, 0.19 PD, 0.12 INT |  |
| LB | Quay Walker | 6.2 | 2.9 solo, 5.2 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| LB | Tommy Eichenberg | 2.8 | 1.7 solo, 2.0 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 7.4 | 4.6 solo, 2.8 ast, 0.09 sack, 0.19 PD, 0.11 INT |  |
| DB | Treydan Stukes | 5.2 | 2.7 solo, 2.5 ast, 0.00 sack, 0.50 PD, 0.24 INT |  |
| DB | Eric Stokes | 4.0 | 2.7 solo, 1.2 ast, 0.06 sack, 0.32 PD, 0.00 INT |  |

### SF @ DAL

Market: DAL +4.0, total 55.5. Sim: SF 29.9, DAL 25.7. DAL wins 37.8%, SF wins 62.2%. Median margin -4.0 for DAL.

| Team stat | SF | DAL |
|---|---|---|
| Plays | 61 | 66 |
| Pass attempts / completions | 31 / 21 | 37 / 24 |
| Passing yards | 261 | 265 |
| Rush attempts / yards | 28 / 133 | 26 / 107 |
| Sacks taken | 2.0 | 2.2 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.8 / 1.5 | 1.6 / 1.1 |
| Field goals | 2.3 | 1.9 |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 23.2 | 261 pass yd, 1.8 TD, 0.6 INT; 4.1 rush, 21 yd |  |
| RB | Christian McCaffrey | 19.0 | 12.2 car, 56 yd, 0.80 TD; 4.1 rec, 32 yd, 0.23 TD |  |
| RB | Kaelon Black | 6.2 | 7.4 car, 36 yd, 0.28 TD; 0.5 rec, 4 yd, 0.02 TD |  |
| RB | Kyle Juszczyk | 2.9 | 0.1 car, 1 yd, 0.00 TD; 1.0 rec, 10 yd, 0.15 TD |  |
| WR | Mike Evans | 7.6 | 3.5 rec, 50 yd, 0.28 TD | Questionable |
| WR | Jordan Watkins | 6.3 | 2.0 rec, 32 yd, 0.18 TD |  |
| WR | Deebo Samuel Sr. | 4.8 | 1.2 car, 6 yd, 0.03 TD; 2.0 rec, 23 yd, 0.21 TD | Questionable |
| WR | Demarcus Robinson | 3.7 | 1.5 rec, 16 yd, 0.10 TD |  |
| TE | George Kittle | 12.4 | 4.8 rec, 55 yd, 0.36 TD |  |
| TE | Luke Farrell | 0.8 | 0.4 rec, 4 yd, 0.01 TD |  |
| K | Eddy Pineiro | 7.7 | 1.3 FG, 3.0 XP |  |
| DL | Keion White | 2.7 | 0.8 solo, 0.9 ast, 0.37 sack, 0.19 PD, 0.00 INT |  |
| DL | Mykel Williams | 2.6 | 1.2 solo, 0.9 ast, 0.30 sack, 0.00 PD, 0.00 INT |  |
| LB | Fred Warner | 9.1 | 4.8 solo, 4.9 ast, 0.04 sack, 0.34 PD, 0.00 INT |  |
| LB | Jaden Dugger | 7.5 | 4.1 solo, 1.4 ast, 0.15 sack, 0.21 PD, 0.21 INT |  |
| LB | Dre Greenlaw | 6.8 | 3.9 solo, 4.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Ji'Ayir Brown | 5.2 | 3.4 solo, 2.6 ast, 0.00 sack, 0.31 PD, 0.06 INT |  |
| DB | Malik Mustapha | 4.8 | 2.7 solo, 1.8 ast, 0.00 sack, 0.54 PD, 0.16 INT |  |
| DB | Renardo Green | 4.0 | 2.5 solo, 1.3 ast, 0.00 sack, 0.77 PD, 0.46 INT | Questionable |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 21.2 | 265 pass yd, 1.6 TD, 0.7 INT; 3.3 rush, 14 yd |  |
| RB | Javonte Williams | 17.9 | 20.6 car, 83 yd, 0.91 TD; 2.4 rec, 15 yd, 0.10 TD |  |
| RB | Hunter Luepke | 1.8 | 1.1 car, 5 yd, 0.02 TD; 0.6 rec, 5 yd, 0.01 TD |  |
| WR | CeeDee Lamb | 21.7 | 8.3 rec, 93 yd, 0.68 TD |  |
| WR | Ryan Flournoy | 10.7 | 4.1 rec, 47 yd, 0.32 TD |  |
| WR | George Pickens | 9.1 | 4.8 rec, 59 yd, 0.32 TD | Questionable |
| WR | KaVontae Turpin | 1.9 | 0.5 car, 2 yd, 0.05 TD; 0.8 rec, 9 yd, 0.06 TD | Questionable |
| TE | Brevyn Spann-Ford | 4.1 | 1.9 rec, 18 yd, 0.07 TD |  |
| K | Brandon Aubrey | 9.9 | 1.9 FG, 2.6 XP |  |
| DL | Quinnen Williams | 5.3 | 2.3 solo, 1.8 ast, 0.50 sack, 0.12 PD, 0.03 INT |  |
| DL | Otito Ogbonnia | 2.3 | 1.5 solo, 1.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Shemar James | 5.0 | 3.2 solo, 1.9 ast, 0.02 sack, 0.12 PD, 0.13 INT |  |
| LB | Dee Winters | 4.0 | 2.5 solo, 1.5 ast, 0.00 sack, 0.13 PD, 0.14 INT |  |
| LB | Jaishawn Barham | 3.0 | 2.1 solo, 1.4 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Caleb Downs | 6.3 | 3.3 solo, 2.3 ast, 0.23 sack, 0.40 PD, 0.16 INT |  |
| DB | DaRon Bland | 3.9 | 2.7 solo, 0.8 ast, 0.00 sack, 0.77 PD, 0.00 INT |  |
| DB | Malik Hooker | 3.8 | 2.6 solo, 1.8 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |

### WAS @ NYG

Market: NYG -2.0, total 41.0. Sim: WAS 19.7, NYG 21.5. NYG wins 55.9%, WAS wins 44.1%. Median margin +2.1 for NYG.

| Team stat | WAS | NYG |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 32 / 20 | 30 / 19 |
| Passing yards | 216 | 216 |
| Rush attempts / yards | 27 / 127 | 30 / 125 |
| Sacks taken | 2.4 | 2.1 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.1 / 1.0 | 1.1 / 1.2 |
| Field goals | 1.5 | 1.6 |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 19.3 | 216 pass yd, 1.1 TD, 0.6 INT; 5.3 rush, 30 yd |  |
| RB | Rachaad White | 12.1 | 9.8 car, 44 yd, 0.39 TD; 2.5 rec, 22 yd, 0.14 TD |  |
| RB | Austin Ekeler | 6.6 | 7.7 car, 32 yd, 0.15 TD; 1.3 rec, 12 yd, 0.03 TD |  |
| WR | Stefon Diggs | 10.5 | 4.4 rec, 43 yd, 0.31 TD |  |
| WR | Antonio Williams | 8.3 | 3.8 rec, 38 yd, 0.12 TD |  |
| WR | Van Jefferson | 8.2 | 3.1 rec, 32 yd, 0.32 TD |  |
| WR | Luke McCaffrey | 0.7 | 0.3 rec, 3 yd, 0.01 TD |  |
| TE | Chig Okonkwo | 8.8 | 4.2 rec, 41 yd, 0.10 TD |  |
| TE | John Bates | 1.8 | 0.8 rec, 7 yd, 0.05 TD |  |
| K | Drew Stevens | 9.2 | 1.9 FG, 2.0 XP |  |
| DL | Dorance Armstrong | 3.2 | 1.6 solo, 1.5 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| DL | Shy Tuttle | 3.1 | 1.3 solo, 1.5 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 7.6 | 4.1 solo, 4.8 ast, 0.07 sack, 0.40 PD, 0.09 INT |  |
| LB | Frankie Luvu | 6.4 | 3.2 solo, 4.1 ast, 0.23 sack, 0.21 PD, 0.00 INT |  |
| LB | K'Lavon Chaisson | 4.4 | 1.7 solo, 1.2 ast, 0.39 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Cross | 6.1 | 3.6 solo, 1.6 ast, 0.00 sack, 0.64 PD, 0.21 INT |  |
| DB | Amik Robertson | 5.9 | 3.8 solo, 2.1 ast, 0.00 sack, 0.89 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 5.3 | 3.3 solo, 2.9 ast, 0.00 sack, 0.40 PD, 0.05 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jameis Winston | 17.2 | 216 pass yd, 1.1 TD, 0.6 INT; 3.2 rush, 14 yd |  |
| RB | Devin Singletary | 10.2 | 11.1 car, 43 yd, 0.56 TD; 1.3 rec, 10 yd, 0.07 TD |  |
| RB | Najee Harris | 4.0 | 7.2 car, 30 yd, 0.16 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| RB | Gregory Desrosiers | 2.2 | 3.8 car, 18 yd, 0.08 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Malik Nabers | 14.0 | 5.9 rec, 65 yd, 0.28 TD |  |
| WR | Malachi Fields | 5.8 | 2.2 rec, 28 yd, 0.12 TD |  |
| WR | Darnell Mooney | 4.0 | 0.8 car, 4 yd, 0.03 TD; 1.4 rec, 17 yd, 0.06 TD |  |
| WR | Darius Slayton | 2.7 | 1.1 rec, 13 yd, 0.06 TD |  |
| TE | Isaiah Likely | 11.6 | 4.7 rec, 44 yd, 0.42 TD |  |
| TE | Theo Johnson | 2.5 | 0.9 rec, 11 yd, 0.07 TD |  |
| K | Dominic Zvada | 9.6 | 2.0 FG, 2.2 XP |  |
| DL | DJ Reader | 3.0 | 1.9 solo, 1.2 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Alexander | 2.6 | 0.8 solo, 1.0 ast, 0.37 sack, 0.16 PD, 0.00 INT |  |
| LB | Arvell Reese | 11.0 | 6.2 solo, 2.4 ast, 0.73 sack, 0.43 PD, 0.11 INT |  |
| LB | Micah McFadden | 5.3 | 3.4 solo, 1.5 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| LB | Abdul Carter | 3.0 | 1.0 solo, 1.4 ast, 0.29 sack, 0.00 PD, 0.00 INT |  |
| DB | Jevon Holland | 5.3 | 2.7 solo, 1.7 ast, 0.00 sack, 0.45 PD, 0.26 INT |  |
| DB | Greg Newsome II | 4.9 | 3.1 solo, 1.1 ast, 0.00 sack, 0.91 PD, 0.12 INT |  |
| DB | Deonte Banks | 4.3 | 1.7 solo, 1.3 ast, 0.00 sack, 1.11 PD, 0.09 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: WAS: Colson Yankoff, WAS: Austin Keys, WAS: Lucas Patrick, WAS: Josh Johnson, WAS: Drake Jackson, WAS: Javontae Jean-Baptiste, WAS: Tyler Biadasz, WAS: Nick Bellore, WAS: Jaden Bradley, WAS: Jeremy McNichols, WAS: Leo Chenal, WAS: Daron Payne, WAS: Laremy Tunsil, WAS: T.J. Maguranyanga, WAS: Treylon Burks, WAS: Jacory Croskey-Merritt, WAS: Jaylin Lane, WAS: Jalyn Holmes, WAS: Dyami Brown, WAS: Ale Kaho, WAS: Terry McLaurin, WAS: Javon Kinlaw, WAS: Craig Reynolds, NYG: Dawuane Smoot, NYG: Tremaine Edmunds, NYG: Raheem Layne, NYG: Brian Burns, NYG: DJ Davidson, NYG: Colton Hood, NYG: Dalen Cambre, NYG: Tyrone Tracy Jr., NYG: Chauncey Golston, NYG: Cam Skattebo, NYG: Jaxson Dart, NYG: Isaiah Hodgins, NYG: Rico Payton, NYG: Jihad Ward, NYG: Braxton Berrios, NYG: Korie Black, NYG: Gunner Olszewski, NYG: Roy Robertson-Harris, NYG: Elijah Chatman, NYG: Eric Gray, NE: Charles Woods, NE: Harold Landry III, NE: Reggie Gilliam, NE: Chad Muma, NE: Mike Onwenu, NE: Jack Westover, NE: Marte Mapu, NE: Carlton Davis III, NE: Tanner Arkin, NE: Quintayvious Hutchins, NE: Dell Pettus, NE: Romeo Doubs, NE: Elliott Davison, NE: Alijah Vera-Tucker, NE: TreVeyon Henderson, NE: Kindle Vildor, NE: Jeremiah Pharms Jr., NE: Eric Gregory, NE: Terrell Jennings, DET: Tom Kennedy, DET: Terrion Arnold, DET: Jimmy Rolder, DET: Jackson Meeks, DET: Anthony Lucas, DET: Jack Campbell, DET: Avonte Maddox, DET: Devin White, DET: Jacob Saylors, DET: Ben Bartch, DET: Jabari Small, DET: Thomas Harper, KC: Nikko Remigio, KC: Mansoor Delane, KC: Esa Pole, KC: Justin Watson, KC: Marcus Harris, KC: Ethan Downs, KC: L'Jarius Sneed, KC: Zacch Pickens, KC: Shane Buechele, KC: Isiah Pacheco, KC: Brashard Smith, KC: Cole Christiansen, KC: Josh Simmons, KC: Tyquan Thornton, ATL: Brian Asamoah II, ATL: Jared Ivey, ATL: Natrone Brooks, ATL: Ronnie Harrison, ATL: Samson Ebukam, ATL: JD Bertrand, ATL: Dylan Drummond, ATL: Jammie Robinson, ATL: Brian Robinson, ATL: Michael Jerrell, ATL: Nick Folk, ATL: Bralen Trice, ATL: Jack Nelson, ATL: Jalon Walker, HOU: Myles Bryant, HOU: Cade Stover, HOU: George Odum, HOU: Jayden Higgins, HOU: Jawhar Jordan, HOU: British Brooks, HOU: Bryce Hall, HOU: Christian Kirk, HOU: Damone Clark, HOU: Jaden Crumedy, HOU: Dylan Horton, HOU: E.J. Speed, HOU: Aiden Fisher, HOU: Jaylin Smith, HOU: Jamal Hill, HOU: Jaylin Noel, HOU: Kenneth Murray, Jr., HOU: Mario Edwards, HOU: Lewis Bond, CLE: Nathaniel Watson, CLE: Cedric Tillman, CLE: Brenden Bates, CLE: Deshaun Watson, CLE: Jerome Ford, CLE: Raheim Sanders, CLE: KT Leveston, CLE: Carsen Ryan, CLE: Alex Wright, CLE: Gage Larvadain, CLE: Teven Jenkins, MIN: Ty Chandler, MIN: Jeshaun Jones, MIN: Donovan Jackson, MIN: Ben Sims, MIN: C.J. Ham, MIN: Demond Claiborne, MIN: Taki Taimani, MIN: Josh Oliver, MIN: Tyler Batty, GB: Jonathan Ford, GB: Johnathan Baldwin, GB: Drake Dabney, GB: Josh Jacobs, GB: Edgerrin Cooper, GB: Jayden Reed, GB: Luke Musgrave, GB: Nate Hobbs, GB: Chris Brooks, GB: Arron Mosby, GB: Shemar Bartholomew, GB: MarShawn Lloyd, GB: Jacob Monk, GB: Micah Parsons, GB: Warren Brinson, GB: Collin Oliver, GB: Javon Hargrave, GB: Zach Bako-Bewele, GB: John FitzPatrick, GB: Skyy Moore, MIA: Rob Beal Jr., MIA: De'Von Achane, MIA: Zane Gonzalez, MIA: Zach Sieler, MIA: Quinton Bell, MIA: Liam Anderson, MIA: Carlos Washington, MIA: Jaylen Wright, MIA: Malik Willis, MIA: Julian Hill, MIA: Ethan Bonner, MIA: Ryan Miller, MIA: Keith Cooper Jr., MIA: Caleb Johnson, IND: Eric Johnson, IND: Johnathan Edwards, IND: Nick Westbrook-Ikhine, IND: Carl Lawson, IND: Jaylon Jones, IND: Cameron Mitchell, IND: Arden Key, IND: Cam Taylor-Britt, IND: Danny Pinter, IND: Alec Pierce, IND: Justin Walley, CAR: Jonathon Brooks, CAR: Corey Thornton, CAR: Jimmy Horn Jr., CAR: Mike Jackson, CAR: Cam Jackson, CAR: Jaelan Phillips, CAR: Xavier Legette, CAR: LaBryan Ray, CAR: Ikem Ekwonu, CAR: Ja'Seem Reed, CAR: Will Lee III, CAR: Krys Barnes, CAR: Marco Wilson, CAR: Damien Lewis, CAR: Jaycee Horn, CAR: Thomas Incoom, CAR: David Moore, CAR: Taylor Moton, CAR: Akayleb Evans, CAR: Nic Scourton, NO: Dillon Radunz, NO: Bryan Bresee, NO: Moliki Matavao, NO: Kevin Austin Jr., NO: Zamir White, NO: Mason Tipton, NO: Jayden Price, NO: Jalen Cropper, NO: Jack Stoll, NO: Fadil Diggs, NO: Charlie Smyth, NO: Travis Etienne, NO: Jonah Williams, NO: Devin Neal, BUF: Keonta Jenkins, BUF: Tyrell Shavers, BUF: Josh Palmer, BUF: Tre'Davious White, BUF: Jordan Hancock, BUF: Phidarian Mathis, BUF: Shaq Thompson, BUF: Andre Jones Jr., BUF: Frank Gore Jr., BUF: Mecole Hardman, BUF: Kani Walker, NYJ: Max Mitchell, NYJ: Marcelino McCrary-Ball, NYJ: Kingsley Jonathan, NYJ: Jamaal Pritchett, NYJ: Samuel Womack, NYJ: Eric Watts, NYJ: Francisco Mauigoa, NYJ: Ja'Sir Taylor, NYJ: Arian Smith, NYJ: Brady Cook, NYJ: Stone Smartt, NYJ: Braiden McGregor, NYJ: T'Vondre Sweat, NYJ: David Onyemata, NYJ: Sterling Shepard, NYJ: Joseph Ossai, NYJ: Mykal Walker, NYJ: Nahshon Wright, NYJ: Jordan Clark, NYJ: Micheal Clemons, JAX: Patrick Mekari, JAX: BJ Green II, JAX: Anton Harrison, JAX: Austin Johnson, JAX: Cam'Ron Silmon-Craig, JAX: Emmanuel Ogbah, JAX: Nick Mullens, JAX: DaVon Hamilton, JAX: Caleb Ransaw, JAX: Austin Trammell, JAX: Eric Murray, TEN: Jaylen Harrell, TEN: Darrell Baker Jr., TEN: Erick Hallett, TEN: James Williams, TEN: Kaiir Elam, TEN: Jalyn Armour-Davis, TEN: Tommy Townsend, TEN: James Proche, TEN: Mohamoud Diabate, TEN: Thomas Morstead, TEN: Isaiah Oliver, TEN: Xavier Restrepo, TEN: Kalel Mullings, TEN: Kendell Brooks, LA: Jordan Whittington, LA: Davante Adams, LA: Darious Williams, LA: Alex Bachman, LA: Kobie Turner, LA: Derion Kendrick, LA: Puka Nacua, LA: Blake Grupe, LA: Justin Dedich, LA: Poona Ford, LA: Dean Connors, LA: Terrance Ferguson, LA: Ahkello Witherspoon, LA: Pepe Williams, LA: Tanner Ingle, LA: Jaylen Watson, LA: Jake McQuaide, LA: Xavier Smith, ARI: Owen Pappoe, ARI: PJ Mustipher, ARI: BJ Ojulari, ARI: Will Johnson, ARI: Kendrick Bourne, ARI: Kenny Yeboah, ARI: Jeremiyah Love, ARI: Jaden Davis, ARI: Zachary Carter, ARI: Jared Harrison-Hunte, ARI: Hunter Long, ARI: Art Green, ARI: Jalen Brooks, ARI: Wydett Williams Jr., ARI: Michael Wilson, ARI: Paris Johnson Jr., ARI: Gardner Minshew, SEA: Julian Neal, SEA: Montorie Foster Jr, SEA: Jake Bobo, SEA: Rashid Shaheed, SEA: Coby Bryant, SEA: Trevon Diggs, SEA: Jimmy Ciarlo, SEA: Sam Darnold, SEA: Robbie Ouzts, SEA: Velus Jones Jr., SEA: Elijah Arroyo, SEA: AJ Finley, LV: Patrick Johnson, LV: Carter Runyon, LV: Shedrick Jackson, LV: Greedy Vance, LV: Cian Slone, LV: Deven Thompkins, LV: Darnay Holmes, LV: Chigozie Anusiem, LV: Jon Rhattigan, LV: Jamal Adams, LV: Aidan O'Connell, LV: Elandon Roberts, SF: Ogbo Okoronkwo, SF: Ricky Pearsall, SF: C.J. West, SF: Alfred Collins, SF: KhaDarel Hodge, SF: Eric Kendricks, SF: Isaac Guerendo, SF: Sam Okuayinonu, SF: Jalen Graham, SF: Kalia Davis, SF: Jake Tonges, SF: Gracen Halton, SF: Nick Martin, DAL: Caelen Carson, DAL: Jalen Thompson, DAL: Curtis Robinson, DAL: Malachi Lawrence, DAL: Jonathan Bullard, DAL: Phil Mafah, DAL: Reddy Steward, DAL: Jake Ferguson, DAL: Hakeem Adeniji, DAL: Tyler Goodson, DAL: Trikweze Bridges, DAL: Malik Davis, DAL: Luke Schoonmaker, DAL: James Mitchell, DAL: Jordan Hudson, DAL: P.J. Locke, PIT: Roman Wilson, PIT: Derrick Harmon, PIT: Michael Pittman, PIT: Sebastian Joseph-Day, PIT: Doneiko Slaughter, PIT: Calvin Austin III, PIT: Logan Lee, PIT: Rayshawn Jenkins, PIT: Ben Skowronek, PIT: Brandin Echols, PIT: Brandon Johnson, PIT: Adam Thielen, PIT: Sebastian Castro, PIT: Esezi Otomewo, CIN: Cashius Howell, CIN: McKinnley Jackson, CIN: Erick All, CIN: Swayze Bozeman, CIN: Bralyn Lux, CIN: Howard Cross III, CIN: Isaiah Foskey, CIN: Tanner Hudson, CIN: Ke'Shawn Williams, CIN: Andrei Iosivas, CIN: Jalen Davis, LAC: Trey Lance, LAC: Rashawn Slater, LAC: Patrick Herbert, LAC: Austin Deculus, LAC: Trey Pipkins, LAC: Derwin James, LAC: Denzel Perryman, LAC: Marquez Valdes-Scantling, LAC: Da'Shawn Hand, LAC: David Njoku, LAC: Hassan Haskins, LAC: Trevor Penning, LAC: Daniel Brunskill, LAC: Alec Ingold, LAC: Bobby Hart, BAL: Tyler Loop, BAL: Chris Moore, BAL: Tyler Huntley, BAL: Jacob Hummel, BAL: Lamar Jackson, BAL: Durham Smythe, BAL: David Ojabo, BAL: Carl Jones, BAL: Jake Moody, BAL: Tavius Robinson, BAL: Jovaughn Gwyn.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.3 | 8.7 to 36.5 |
| QB | Joe Burrow | CIN | 21.5 | 8.4 to 35.7 |
| QB | Brock Purdy | SF | 21.3 | 8.7 to 35.2 |
| QB | Drake Maye | NE | 20.8 | 8.2 to 34.4 |
| QB | Trevor Lawrence | JAX | 20.0 | 7.9 to 33.2 |
| QB | Dak Prescott | DAL | 19.6 | 7.3 to 32.6 |
| RB | Jahmyr Gibbs | DET | 24.1 | 8.7 to 41.3 |
| RB | Bijan Robinson | ATL | 23.0 | 8.0 to 39.4 |
| RB | Kyren Williams | LA | 21.3 | 8.2 to 36.2 |
| RB | Kenneth Walker III | KC | 19.8 | 6.6 to 34.8 |
| RB | Christian McCaffrey | SF | 19.3 | 6.7 to 33.7 |
| RB | Jaylen Warren | PIT | 19.2 | 7.0 to 33.1 |
| RB | Javonte Williams | DAL | 18.9 | 6.0 to 33.9 |
| RB | Chuba Hubbard | CAR | 17.3 | 5.7 to 30.7 |
| RB | Ollie Gordon II | MIA | 17.2 | 4.6 to 31.3 |
| RB | James Cook | BUF | 16.7 | 4.7 to 30.9 |
| WR | CeeDee Lamb | DAL | 22.9 | 8.2 to 39.6 |
| WR | Jaxon Smith-Njigba | SEA | 21.5 | 7.0 to 37.6 |
| WR | Ja'Marr Chase | CIN | 18.4 | 5.3 to 33.3 |
| WR | Tee Higgins | CIN | 16.1 | 4.4 to 30.1 |
| WR | Christian Watson | GB | 14.7 | 3.6 to 28.9 |
| WR | Zay Flowers | BAL | 14.6 | 3.5 to 27.9 |
| WR | Malik Nabers | NYG | 14.6 | 3.8 to 28.0 |
| WR | Matthew Golden | GB | 14.1 | 3.3 to 27.1 |
| WR | Justin Jefferson | MIN | 13.5 | 3.1 to 25.9 |
| WR | Drake London | ATL | 13.3 | 3.0 to 26.3 |
| WR | Amon-Ra St. Brown | DET | 13.2 | 0.0 to 30.5 |
| WR | Tetairoa McMillan | CAR | 13.2 | 3.1 to 25.5 |
| TE | Trey McBride | ARI | 25.7 | 11.0 to 42.3 |
| TE | Brock Bowers | LV | 13.2 | 3.0 to 25.8 |
| TE | George Kittle | SF | 12.7 | 2.8 to 25.0 |
| TE | Tyler Higbee | LA | 12.1 | 2.4 to 24.3 |
| TE | Isaiah Likely | NYG | 11.8 | 2.5 to 22.5 |
| TE | Travis Kelce | KC | 10.9 | 1.8 to 22.5 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 21.6 | 8.7 to 35.2 |
| QB | Brock Purdy | SF | 20.3 | 8.9 to 33.3 |
| QB | Joe Burrow | CIN | 20.3 | 8.5 to 33.3 |
| QB | Drake Maye | NE | 19.9 | 8.4 to 32.8 |
| QB | Trevor Lawrence | JAX | 18.9 | 8.1 to 31.1 |
| QB | Dak Prescott | DAL | 18.6 | 7.5 to 30.5 |
| RB | Jahmyr Gibbs | DET | 21.0 | 7.4 to 36.4 |
| RB | Bijan Robinson | ATL | 19.9 | 6.9 to 34.8 |
| RB | Kyren Williams | LA | 18.1 | 6.7 to 31.0 |
| RB | Kenneth Walker III | KC | 17.4 | 5.6 to 31.3 |
| RB | Christian McCaffrey | SF | 16.9 | 5.1 to 30.4 |
| RB | Javonte Williams | DAL | 16.7 | 5.3 to 30.2 |
| RB | Jaylen Warren | PIT | 16.7 | 6.2 to 28.7 |
| RB | Ollie Gordon II | MIA | 15.3 | 4.6 to 28.0 |
| RB | James Cook | BUF | 15.2 | 4.3 to 28.3 |
| RB | Chuba Hubbard | CAR | 15.1 | 4.8 to 27.3 |
| WR | CeeDee Lamb | DAL | 17.5 | 5.8 to 30.8 |
| WR | Jaxon Smith-Njigba | SEA | 16.5 | 5.1 to 29.4 |
| WR | Ja'Marr Chase | CIN | 14.1 | 3.6 to 25.9 |
| WR | Tee Higgins | CIN | 12.6 | 3.0 to 23.5 |
| WR | Christian Watson | GB | 11.6 | 2.4 to 22.5 |
| WR | Zay Flowers | BAL | 11.5 | 2.4 to 21.8 |
| WR | Malik Nabers | NYG | 11.1 | 2.5 to 21.1 |
| WR | Matthew Golden | GB | 10.9 | 1.9 to 21.3 |
| WR | Justin Jefferson | MIN | 10.7 | 1.8 to 21.0 |
| WR | Parker Washington | JAX | 10.3 | 1.2 to 20.7 |
| WR | Tetairoa McMillan | CAR | 10.2 | 1.9 to 20.0 |
| WR | Drake London | ATL | 10.2 | 2.0 to 19.9 |
| TE | Trey McBride | ARI | 18.2 | 7.2 to 31.0 |
| TE | Brock Bowers | LV | 10.1 | 1.9 to 19.8 |
| TE | George Kittle | SF | 10.0 | 1.6 to 19.9 |
| TE | Tyler Higbee | LA | 9.4 | 1.5 to 18.8 |
| TE | Isaiah Likely | NYG | 9.2 | 1.3 to 18.5 |
| TE | Travis Kelce | KC | 8.7 | 1.1 to 18.0 |
| K | Tyler Bass | BUF | 10.4 | 2.0 to 21.0 |
| K | Ka'imi Fairbairn | HOU | 10.0 | 1.0 to 21.4 |
| K | Jason Sanders | NYJ | 9.6 | 1.0 to 21.4 |
| K | Jake Bates | DET | 9.6 | 1.0 to 20.0 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses came from MFL at the time of the pull. Re-run Thursday morning and Sunday morning for fresh news.
- Weather, referee tendencies and in-game injuries are not modeled.