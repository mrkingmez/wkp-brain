# Week 10 Full Simulation Report - 12 Nov 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 20,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| WAS @ NYG | NYG 56.0% | WAS 19.6 - NYG 21.7 | WSH | 48.4% | NYG | 56.2% |
| NE @ DET | DET 59.1% | NE 23.9 - DET 27.0 | NE | 48.4% | DET | 59.3% |
| KC @ ATL | KC 59.3% | KC 25.2 - ATL 22.1 | ATL | 51.6% | KC | 59.3% |
| HOU @ CLE | HOU 64.4% | HOU 22.8 - CLE 17.9 | CLE | 48.4% | HOU | 65.3% |
| MIN @ GB | GB 59.2% | MIN 19.6 - GB 22.6 | MIN | 51.6% | GB | 59.3% |
| MIA @ IND | IND 61.7% | MIA 17.2 - IND 21.2 | IND | 54.7% | IND | 62.3% |
| CAR @ NO | NO 57.9% | CAR 23.2 - NO 25.8 | NO | 53.1% | NO | 57.8% |
| BUF @ NYJ | BUF 72.8% | BUF 29.6 - NYJ 21.6 | NYJ | 48.4% | BUF | 73.5% |
| JAX @ TEN | JAX 78.5% | JAX 28.6 - TEN 18.1 | JAX | 53.1% | JAX | 79.5% |
| LA @ ARI | LA 76.7% | LA 24.7 - ARI 15.3 | LAR | 56.2% | LAR | 77.2% |
| SEA @ LV | SEA 68.9% | SEA 23.7 - LV 17.2 | SEA | 59.3% | SEA | 69.5% |
| SF @ DAL | SF 61.5% | SF 29.7 - DAL 25.7 | DAL | 48.4% | SF | 62.3% |
| PIT @ CIN | CIN 61.0% | PIT 23.0 - CIN 26.6 | PIT | 50.0% | CIN | 60.8% |
| LAC @ BAL | BAL 63.3% | LAC 17.2 - BAL 21.6 | LAC | 53.1% | BAL | 63.8% |

**Eliminator:** biggest favorites this week by win chance: JAX 78.5%, LA 76.7%, BUF 72.8%, SEA 68.9%, HOU 64.4%. Teams already used are not tracked here, check FUTURES-PICKS.md.

## 2. IRFL lineups

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 147.3 | 107.6 | 189.0 |
| 2 SAFE (protects a lead) | 147.0 | 107.4 | 188.8 |
| 3 BALANCED UPSIDE (75th percentile) | 147.3 | 107.6 | 189.0 |
| 4 SWING (90th percentile, for an underdog) | 147.3 | 107.6 | 189.0 |
| 5 CONTINGENCY (every Questionable out) | 138.4 | 103.2 | 175.4 |
| Saved MFL lineup (for comparison) | 130.9 | 92.7 | 171.7 |

Saved starters with no simulation, counted as zero: Strnad, Justin; Mukuba, Andrew; Robinson, Brian.

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.7 | 5.9 to 37.5 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.2 | 2.8 to 23.4 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 1.9 to 19.0 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.4 to 26.0 |  |
| WR | Jefferson, Justin | MIN | 13.0 | 2.8 to 24.9 |  |
| WR | Golden, Matthew | GBP | 12.6 | 2.9 to 23.8 |  |
| WR | Williams, Jameson | DET | 11.5 | 1.6 to 22.8 |  |
| TE | LaPorta, Sam | DET | 9.7 | 1.4 to 19.3 |  |
| PK | Bates, Jake | DET | 10.2 | 2.0 to 19.0 |  |
| DL | Hutchinson, Aidan | DET | 4.7 | 1.0 to 9.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Okereke, Bobby | CAR | 3.0 | 0.0 to 9.5 | Questionable, plays about 75% of sims. |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 4.9 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.7 | 5.9 to 37.5 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.2 | 2.8 to 23.4 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 1.9 to 19.0 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.4 to 26.0 |  |
| WR | Jefferson, Justin | MIN | 13.0 | 2.8 to 24.9 |  |
| WR | Golden, Matthew | GBP | 12.6 | 2.9 to 23.8 |  |
| WR | Williams, Jameson | DET | 11.5 | 1.6 to 22.8 |  |
| TE | LaPorta, Sam | DET | 9.7 | 1.4 to 19.3 |  |
| PK | Bates, Jake | DET | 10.2 | 2.0 to 19.0 |  |
| DL | Hutchinson, Aidan | DET | 4.7 | 1.0 to 9.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 | differs from lineup 1 |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 4.9 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.7 | 5.9 to 37.5 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.2 | 2.8 to 23.4 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 1.9 to 19.0 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.4 to 26.0 |  |
| WR | Jefferson, Justin | MIN | 13.0 | 2.8 to 24.9 |  |
| WR | Golden, Matthew | GBP | 12.6 | 2.9 to 23.8 |  |
| WR | Williams, Jameson | DET | 11.5 | 1.6 to 22.8 |  |
| TE | LaPorta, Sam | DET | 9.7 | 1.4 to 19.3 |  |
| PK | Bates, Jake | DET | 10.2 | 2.0 to 19.0 |  |
| DL | Hutchinson, Aidan | DET | 4.7 | 1.0 to 9.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Okereke, Bobby | CAR | 3.0 | 0.0 to 9.5 | Questionable, plays about 75% of sims. |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 4.9 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 20.7 | 5.9 to 37.5 | Questionable, plays about 75% of sims. |
| RB | White, Rachaad | WAS | 12.2 | 2.8 to 23.4 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 1.9 to 19.0 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.4 to 26.0 |  |
| WR | Jefferson, Justin | MIN | 13.0 | 2.8 to 24.9 |  |
| WR | Golden, Matthew | GBP | 12.6 | 2.9 to 23.8 |  |
| WR | Williams, Jameson | DET | 11.5 | 1.6 to 22.8 |  |
| TE | LaPorta, Sam | DET | 9.7 | 1.4 to 19.3 |  |
| PK | Bates, Jake | DET | 10.2 | 2.0 to 19.0 |  |
| DL | Hutchinson, Aidan | DET | 4.7 | 1.0 to 9.5 |  |
| DL | Wonnum, D.J. | DET | 2.6 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| LB | Okereke, Bobby | CAR | 3.0 | 0.0 to 9.5 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 4.9 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | BAL | 13.7 | 2.0 to 27.5 | differs from lineup 1 |
| RB | White, Rachaad | WAS | 12.2 | 2.8 to 23.4 |  |
| RB | Dowdle, Rico | PIT | 9.7 | 1.9 to 19.0 |  |
| WR | Flowers, Zay | BAL | 14.1 | 3.4 to 26.0 |  |
| WR | Jefferson, Justin | MIN | 13.0 | 2.8 to 24.9 |  |
| WR | Golden, Matthew | GBP | 12.6 | 2.9 to 23.8 |  |
| WR | Williams, Jameson | DET | 11.5 | 1.6 to 22.8 |  |
| TE | LaPorta, Sam | DET | 9.7 | 1.4 to 19.3 |  |
| PK | Bates, Jake | DET | 10.2 | 2.0 to 19.0 |  |
| DL | Hutchinson, Aidan | DET | 4.7 | 1.0 to 9.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Dodson, Tyrel | CAR | 2.6 | 0.5 to 5.0 | differs from lineup 1 |
| LB | Reid, Winston | CLE | 1.1 | 0.0 to 2.5 | differs from lineup 1 |
| DB | Scott, Nick | CAR | 5.9 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 4.9 | 1.5 to 8.5 |  |
| DB | Kinchens, Kamren | LAR | 4.1 | 1.0 to 7.5 |  |

Lineups 1 and 3 are identical; 1 and 4 are identical; 3 and 4 are identical. Where they match, the roster has no real choice between safe and swing this week.

Not simulated this week (bye, no team, new team, or no recent usage, check each one): Moss, Riley (DEN); Robinson, Tavius (BAL); Kancey, Calijah (TBB); Strnad, Justin (DEN); Andersen, Troy (FA); Folk, Nick (FA); Williams, Caleb (CHI); Robinson, Brian (ATL); Jenkins, Rayshawn (BAL); Mukuba, Andrew (PHI); Locke, P.J. (DAL); Goedert, Dallas (PHI); Shepard, Sterling (NYJ).

Changed teams and simulated on the new team with his own old-team rates: Andre Cisco (DB, NYJ to DET); K.J. Britt (LB, NE to DET); Kirk Cousins (QB, LV to MIN); Amani Hooker (DB, TEN to BUF); Davon Godchaux (DL, NO to JAX); Jessie Bates (DB, ATL to JAX); Jordan Davis (DL, PHI to JAX); Jonah Laulu (DL, LV to TEN); Jacoby Brissett (QB, ARI to BAL).

Changed teams, simulated at a REDUCED share (first game on a new team: 0.6 of his old target share, 0.3 of his carries, thin evidence): Josh Downs (WR, IND to KC); Keenan Allen (WR, IND to SF).

Starting quarterbacks named by hand in the overrides file: CLE Deshaun Watson; MIN Kirk Cousins; MIA Kyle McCord; ARI Carson Beck; SEA Drew Lock; LV Fernando Mendoza; BAL Jacoby Brissett.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### BUF @ NYJ

Market: NYJ +8.0, total 51.0. Sim: BUF 29.6, NYJ 21.6. NYJ wins 27.2%, BUF wins 72.8%. Median margin -8.0 for NYJ.

| Team stat | BUF | NYJ |
|---|---|---|
| Plays | 63 | 60 |
| Pass attempts / completions | 30 / 20 | 34 / 22 |
| Passing yards | 248 | 228 |
| Rush attempts / yards | 31 / 138 | 24 / 103 |
| Sacks taken | 2.1 | 2.2 |
| Interceptions thrown | 0.5 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.6 | 1.5 / 0.9 |
| Field goals | 2.2 | 1.6 |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.1 | 248 pass yd, 1.5 TD, 0.5 INT; 6.2 rush, 28 yd |  |
| RB | James Cook | 16.1 | 17.4 car, 78 yd, 0.87 TD; 1.4 rec, 15 yd, 0.07 TD |  |
| RB | Ty Johnson | 6.5 | 1.9 car, 8 yd, 0.09 TD; 2.2 rec, 25 yd, 0.09 TD |  |
| RB | Ray Davis | 3.0 | 2.6 car, 12 yd, 0.07 TD; 0.5 rec, 6 yd, 0.04 TD |  |
| WR | Khalil Shakir | 9.5 | 3.9 rec, 45 yd, 0.20 TD |  |
| WR | DJ Moore | 8.2 | 0.6 car, 3 yd, 0.00 TD; 2.8 rec, 36 yd, 0.26 TD |  |
| WR | Keon Coleman | 7.2 | 2.6 rec, 31 yd, 0.25 TD |  |
| WR | Gabe Davis | 1.4 | 0.7 rec, 7 yd, 0.07 TD | Questionable |
| TE | Dalton Kincaid | 6.5 | 3.4 rec, 41 yd, 0.22 TD | Questionable |
| TE | Dawson Knox | 4.7 | 2.0 rec, 18 yd, 0.15 TD |  |
| K | Tyler Bass | 11.1 | 2.2 FG, 3.0 XP |  |
| DL | Deone Walker | 2.4 | 1.0 solo, 1.5 ast, 0.06 sack, 0.50 PD, 0.00 INT |  |
| DL | Landon Jackson | 2.1 | 0.7 solo, 1.3 ast, 0.20 sack, 0.12 PD, 0.00 INT |  |
| LB | Greg Rousseau | 6.2 | 1.6 solo, 1.0 ast, 0.87 sack, 0.87 PD, 0.00 INT |  |
| LB | Terrel Bernard | 5.7 | 3.0 solo, 3.3 ast, 0.00 sack, 0.41 PD, 0.17 INT |  |
| LB | Dorian Williams | 4.6 | 1.7 solo, 3.3 ast, 0.00 sack, 0.33 PD, 0.25 INT |  |
| DB | Amani Hooker | 7.7 | 3.7 solo, 2.3 ast, 0.00 sack, 0.79 PD, 0.68 INT |  |
| DB | Cole Bishop | 5.1 | 3.2 solo, 2.1 ast, 0.13 sack, 0.23 PD, 0.00 INT |  |
| DB | Davison Igbinosun | 4.1 | 1.7 solo, 1.5 ast, 0.00 sack, 1.20 PD, 0.16 INT |  |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Geno Smith | 17.3 | 228 pass yd, 1.5 TD, 0.7 INT; 1.8 rush, 7 yd |  |
| RB | Braelon Allen | 11.3 | 11.0 car, 51 yd, 0.46 TD; 2.0 rec, 13 yd, 0.06 TD |  |
| RB | Breece Hall | 7.5 | 8.1 car, 31 yd, 0.25 TD; 1.5 rec, 13 yd, 0.04 TD |  |
| RB | Isaiah Davis | 2.4 | 1.8 car, 7 yd, 0.06 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| WR | Garrett Wilson | 7.8 | 4.4 rec, 45 yd, 0.26 TD | Questionable |
| WR | Omar Cooper Jr. | 6.8 | 3.5 rec, 39 yd, 0.27 TD | Questionable |
| WR | Adonai Mitchell | 6.3 | 2.3 rec, 28 yd, 0.21 TD |  |
| WR | Isaiah Williams | 3.6 | 1.4 rec, 13 yd, 0.13 TD |  |
| TE | Mason Taylor | 5.2 | 2.2 rec, 18 yd, 0.20 TD |  |
| TE | Kenyon Sadiq | 4.8 | 2.0 rec, 19 yd, 0.10 TD |  |
| K | Jason Sanders | 10.4 | 2.2 FG, 2.2 XP |  |
| DL | Will McDonald IV | 3.2 | 0.9 solo, 1.2 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| DL | Jowon Briggs | 2.8 | 1.2 solo, 2.1 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | David Bailey | 8.5 | 3.2 solo, 2.3 ast, 0.86 sack, 0.10 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.8 | 4.3 solo, 4.8 ast, 0.03 sack, 0.44 PD, 0.00 INT |  |
| LB | Demario Davis | 6.5 | 3.6 solo, 3.3 ast, 0.16 sack, 0.41 PD, 0.00 INT |  |
| DB | Dane Belton | 7.6 | 4.9 solo, 4.1 ast, 0.09 sack, 0.40 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 7.6 | 4.3 solo, 4.5 ast, 0.00 sack, 0.40 PD, 0.10 INT |  |
| DB | Azareye'h Thomas | 3.6 | 1.9 solo, 2.6 ast, 0.00 sack, 0.45 PD, 0.00 INT |  |

### CAR @ NO

Market: NO -2.5, total 49.0. Sim: CAR 23.2, NO 25.8. NO wins 57.9%, CAR wins 42.1%. Median margin +2.7 for NO.

| Team stat | CAR | NO |
|---|---|---|
| Plays | 62 | 64 |
| Pass attempts / completions | 33 / 21 | 34 / 22 |
| Passing yards | 225 | 230 |
| Rush attempts / yards | 25 / 108 | 28 / 113 |
| Sacks taken | 3.0 | 2.2 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.5 / 1.3 |
| Field goals | 1.7 | 1.9 |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.4 | 225 pass yd, 1.5 TD, 0.7 INT; 2.4 rush, 11 yd |  |
| RB | Chuba Hubbard | 16.5 | 16.4 car, 70 yd, 0.63 TD; 3.1 rec, 20 yd, 0.15 TD |  |
| RB | AJ Dillon | 1.9 | 2.8 car, 12 yd, 0.06 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| RB | Trevor Etienne | 1.3 | 1.6 car, 6 yd, 0.03 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tetairoa McMillan | 12.8 | 5.1 rec, 57 yd, 0.33 TD |  |
| WR | Jalen Coker | 9.5 | 3.8 rec, 40 yd, 0.27 TD |  |
| WR | John Metchie III | 4.5 | 2.0 rec, 19 yd, 0.11 TD |  |
| WR | Brycen Tremayne | 1.9 | 0.8 rec, 9 yd, 0.03 TD |  |
| TE | Darren Waller | 7.6 | 2.9 rec, 31 yd, 0.28 TD |  |
| TE | Tommy Tremble | 5.7 | 2.4 rec, 20 yd, 0.22 TD |  |
| K | Ryan Fitzgerald | 8.0 | 1.5 FG, 2.4 XP |  |
| DL | Derrick Brown | 3.9 | 2.1 solo, 2.0 ast, 0.07 sack, 0.51 PD, 0.00 INT |  |
| DL | Aaron Hall | 2.1 | 0.8 solo, 2.1 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 7.8 | 3.9 solo, 3.1 ast, 0.22 sack, 0.49 PD, 0.18 INT |  |
| LB | Patrick Jones II | 3.4 | 2.3 solo, 0.9 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| LB | Bobby Okereke | 3.0 | 4.2 solo, 2.4 ast, 0.14 sack, 0.68 PD, 0.10 INT | Questionable |
| DB | Nick Scott | 5.9 | 4.3 solo, 1.8 ast, 0.00 sack, 0.26 PD, 0.03 INT |  |
| DB | Zakee Wheatley | 4.6 | 2.8 solo, 1.0 ast, 0.00 sack, 0.61 PD, 0.18 INT |  |
| DB | Tre'von Moehrig | 3.9 | 2.5 solo, 1.9 ast, 0.15 sack, 0.00 PD, 0.00 INT |  |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 20.0 | 230 pass yd, 1.5 TD, 0.7 INT; 4.0 rush, 18 yd |  |
| RB | Kendre Miller | 6.8 | 7.9 car, 28 yd, 0.35 TD; 1.1 rec, 8 yd, 0.04 TD |  |
| RB | Audric Estimé | 6.0 | 6.1 car, 27 yd, 0.31 TD; 0.7 rec, 6 yd, 0.02 TD |  |
| RB | Alvin Kamara | 3.7 | 5.6 car, 22 yd, 0.28 TD; 2.7 rec, 19 yd, 0.14 TD | Questionable |
| WR | Chris Olave | 12.5 | 5.0 rec, 56 yd, 0.32 TD |  |
| WR | Devaughn Vele | 7.3 | 3.0 rec, 30 yd, 0.23 TD |  |
| WR | Jordyn Tyson | 6.2 | 3.0 rec, 26 yd, 0.10 TD |  |
| WR | Bryce Lance | 2.5 | 1.0 rec, 9 yd, 0.10 TD |  |
| TE | Juwan Johnson | 6.5 | 2.6 rec, 26 yd, 0.22 TD |  |
| TE | Noah Fant | 2.2 | 1.1 rec, 10 yd, 0.14 TD | Questionable |
| K | Daniel Carlson | 7.8 | 1.4 FG, 2.6 XP |  |
| DL | Carl Granderson | 6.7 | 2.0 solo, 2.5 ast, 1.01 sack, 0.24 PD, 0.06 INT |  |
| DL | Chase Young | 6.4 | 1.4 solo, 1.3 ast, 1.09 sack, 0.47 PD, 0.00 INT |  |
| LB | Pete Werner | 5.9 | 3.0 solo, 4.1 ast, 0.18 sack, 0.21 PD, 0.00 INT |  |
| LB | Kaden Elliss | 5.9 | 3.7 solo, 2.6 ast, 0.25 sack, 0.10 PD, 0.00 INT |  |
| LB | Danny Stutsman | 3.3 | 2.1 solo, 2.2 ast, 0.00 sack, 0.12 PD, 0.00 INT |  |
| DB | Jonas Sanker | 4.9 | 3.2 solo, 2.0 ast, 0.00 sack, 0.34 PD, 0.04 INT |  |
| DB | Julian Blackmon | 4.5 | 2.4 solo, 2.2 ast, 0.00 sack, 0.23 PD, 0.23 INT |  |
| DB | Kool-Aid McKinstry | 4.3 | 2.5 solo, 1.5 ast, 0.00 sack, 0.94 PD, 0.03 INT |  |

### HOU @ CLE

Market: CLE +5.0, total 40.5. Sim: HOU 22.8, CLE 17.9. CLE wins 35.6%, HOU wins 64.4%. Median margin -5.1 for CLE.

| Team stat | HOU | CLE |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 34 / 21 | 34 / 22 |
| Passing yards | 243 | 250 |
| Rush attempts / yards | 26 / 109 | 25 / 95 |
| Sacks taken | 2.6 | 3.0 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.1 / 0.9 |
| Field goals | 1.7 | 1.3 |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 19.7 | 243 pass yd, 1.5 TD, 0.6 INT; 2.7 rush, 12 yd |  |
| RB | Woody Marks | 8.3 | 13.9 car, 54 yd, 0.46 TD; 1.5 rec, 11 yd, 0.06 TD | Questionable |
| RB | Emari Demercado | 5.3 | 5.9 car, 25 yd, 0.12 TD; 1.0 rec, 9 yd, 0.04 TD |  |
| RB | Dare Ogunbowale | 1.4 | 0.5 car, 2 yd, 0.06 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| WR | Nico Collins | 9.7 | 3.5 rec, 43 yd, 0.26 TD |  |
| WR | Xavier Hutchinson | 6.7 | 2.7 rec, 27 yd, 0.19 TD |  |
| WR | Tank Dell | 6.4 | 2.7 rec, 43 yd, 0.20 TD | Questionable |
| WR | Kayshon Boutte | 6.2 | 2.2 rec, 30 yd, 0.18 TD |  |
| TE | Dalton Schultz | 8.0 | 3.8 rec, 34 yd, 0.13 TD |  |
| TE | Foster Moreau | 3.4 | 1.3 rec, 9 yd, 0.21 TD |  |
| K | Ka'imi Fairbairn | 10.8 | 2.2 FG, 2.3 XP |  |
| DL | Will Anderson Jr. | 6.2 | 2.0 solo, 1.5 ast, 1.01 sack, 0.07 PD, 0.00 INT |  |
| DL | Danielle Hunter | 4.2 | 1.2 solo, 1.3 ast, 0.56 sack, 0.38 PD, 0.00 INT |  |
| LB | Henry To'oTo'o | 4.6 | 2.2 solo, 2.9 ast, 0.08 sack, 0.21 PD, 0.00 INT |  |
| LB | Jake Hansen | 3.8 | 1.9 solo, 2.2 ast, 0.09 sack, 0.22 PD, 0.11 INT |  |
| LB | Azeez Al-Shaair | 2.5 | 3.1 solo, 5.1 ast, 0.00 sack, 0.49 PD, 0.09 INT | Questionable |
| DB | M.J. Stewart | 7.4 | 4.0 solo, 2.7 ast, 0.56 sack, 0.34 PD, 0.00 INT |  |
| DB | Kamari Lassiter | 6.8 | 3.9 solo, 1.8 ast, 0.14 sack, 1.38 PD, 0.07 INT |  |
| DB | Calen Bullock | 5.1 | 2.8 solo, 1.7 ast, 0.00 sack, 0.72 PD, 0.12 INT |  |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Deshaun Watson | 17.9 | 250 pass yd, 1.1 TD, 0.7 INT; 4.7 rush, 19 yd |  |
| RB | Quinshon Judkins | 9.8 | 10.9 car, 37 yd, 0.41 TD; 2.0 rec, 15 yd, 0.04 TD |  |
| RB | Dylan Sampson | 6.7 | 3.4 car, 14 yd, 0.06 TD; 2.5 rec, 23 yd, 0.06 TD |  |
| RB | Jaleel McLaughlin | 2.3 | 1.5 car, 6 yd, 0.08 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | KC Concepcion | 10.1 | 0.9 car, 4 yd, 0.02 TD; 4.0 rec, 46 yd, 0.19 TD |  |
| WR | Jerry Jeudy | 5.2 | 2.3 rec, 24 yd, 0.08 TD |  |
| WR | Denzel Boston | 3.9 | 3.8 rec, 47 yd, 0.24 TD | Questionable |
| WR | Isaiah Bond | 1.9 | 0.7 rec, 10 yd, 0.02 TD |  |
| TE | Harold Fannin Jr. | 8.3 | 4.1 rec, 47 yd, 0.35 TD | Questionable |
| TE | Blake Whiteheart | 1.3 | 0.5 rec, 5 yd, 0.05 TD |  |
| K | Andre Szmyt | 9.1 | 1.9 FG, 1.8 XP |  |
| DL | Adin Huntington | 3.3 | 1.0 solo, 1.3 ast, 0.40 sack, 0.00 PD, 0.00 INT |  |
| DL | Mason Graham | 3.2 | 1.5 solo, 1.6 ast, 0.31 sack, 0.00 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 7.2 | 4.7 solo, 5.7 ast, 0.42 sack, 0.12 PD, 0.00 INT | Questionable |
| LB | Quincy Williams | 5.3 | 4.0 solo, 2.8 ast, 0.12 sack, 0.35 PD, 0.00 INT | Questionable |
| LB | Winston Reid | 1.1 | 0.9 solo, 0.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Grant Delpit | 4.9 | 3.0 solo, 1.6 ast, 0.15 sack, 0.32 PD, 0.07 INT |  |
| DB | Tyson Campbell | 4.9 | 2.3 solo, 2.3 ast, 0.00 sack, 0.43 PD, 0.00 INT |  |
| DB | Myles Harden | 4.7 | 2.2 solo, 1.5 ast, 0.29 sack, 0.72 PD, 0.06 INT |  |

### JAX @ TEN

Market: TEN +10.5, total 46.5. Sim: JAX 28.6, TEN 18.1. TEN wins 21.5%, JAX wins 78.5%. Median margin -10.5 for TEN.

| Team stat | JAX | TEN |
|---|---|---|
| Plays | 62 | 60 |
| Pass attempts / completions | 31 / 20 | 35 / 22 |
| Passing yards | 264 | 216 |
| Rush attempts / yards | 29 / 111 | 22 / 94 |
| Sacks taken | 2.3 | 2.3 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.7 / 1.4 | 1.3 / 0.7 |
| Field goals | 2.1 | 1.4 |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 21.7 | 264 pass yd, 1.7 TD, 0.6 INT; 3.2 rush, 13 yd |  |
| RB | Chris Rodriguez Jr. | 5.3 | 7.4 car, 29 yd, 0.51 TD; 0.6 rec, 6 yd, 0.02 TD | Questionable |
| RB | Bhayshul Tuten | 5.2 | 13.4 car, 51 yd, 0.63 TD; 1.4 rec, 17 yd, 0.20 TD | Questionable |
| RB | Ameer Abdullah | 2.1 | 3.3 car, 13 yd, 0.08 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Parker Washington | 12.2 | 3.7 rec, 60 yd, 0.40 TD |  |
| WR | Brian Thomas Jr. | 5.0 | 1.7 rec, 22 yd, 0.18 TD |  |
| WR | Jakobi Meyers | 3.9 | 3.7 rec, 47 yd, 0.23 TD | Questionable |
| WR | Josh Cameron | 3.2 | 1.1 rec, 14 yd, 0.12 TD |  |
| TE | Brenton Strange | 8.9 | 3.6 rec, 42 yd, 0.19 TD |  |
| TE | Nate Boerkircher | 4.2 | 1.3 rec, 19 yd, 0.17 TD |  |
| K | Cam Little | 9.7 | 1.8 FG, 2.9 XP |  |
| DL | Josh Hines-Allen | 3.8 | 1.9 solo, 1.2 ast, 0.30 sack, 0.15 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.2 solo, 2.1 ast, 0.25 sack, 0.10 PD, 0.00 INT |  |
| LB | Foyesade Oluokun | 7.6 | 4.4 solo, 3.1 ast, 0.28 sack, 0.27 PD, 0.16 INT |  |
| LB | Ventrell Miller | 4.4 | 2.2 solo, 2.5 ast, 0.06 sack, 0.52 PD, 0.04 INT |  |
| LB | Jalen McLeod | 2.4 | 1.3 solo, 0.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Jessie Bates | 7.4 | 4.1 solo, 2.4 ast, 0.00 sack, 0.46 PD, 0.16 INT |  |
| DB | Travis Hunter | 4.8 | 2.7 solo, 1.3 ast, 0.00 sack, 0.72 PD, 0.26 INT |  |
| DB | Jarrian Jones | 4.0 | 2.2 solo, 0.7 ast, 0.00 sack, 0.87 PD, 0.18 INT |  |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 16.0 | 216 pass yd, 1.3 TD, 0.9 INT; 2.5 rush, 10 yd |  |
| RB | Tony Pollard | 12.0 | 14.2 car, 61 yd, 0.49 TD; 1.7 rec, 12 yd, 0.05 TD |  |
| RB | Tyjae Spears | 2.3 | 2.7 car, 11 yd, 0.06 TD; 2.5 rec, 15 yd, 0.05 TD | Questionable |
| RB | Michael Carter | 1.6 | 1.4 car, 6 yd, 0.02 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Wan'Dale Robinson | 10.1 | 4.5 rec, 33 yd, 0.39 TD |  |
| WR | Elic Ayomanor | 5.5 | 2.1 rec, 25 yd, 0.15 TD |  |
| WR | Chimere Dike | 4.9 | 1.9 rec, 19 yd, 0.18 TD |  |
| WR | Carnell Tate | 4.5 | 4.7 rec, 49 yd, 0.26 TD | Questionable |
| TE | Gunnar Helm | 5.0 | 2.4 rec, 21 yd, 0.09 TD |  |
| TE | Daniel Bellinger | 2.7 | 1.3 rec, 11 yd, 0.04 TD |  |
| K | Joey Slye | 7.9 | 1.6 FG, 1.9 XP |  |
| DL | Jacob Martin | 4.4 | 1.4 solo, 0.3 ast, 0.90 sack, 0.25 PD, 0.00 INT |  |
| DL | Jermaine Johnson II | 3.0 | 1.4 solo, 1.0 ast, 0.37 sack, 0.00 PD, 0.00 INT |  |
| LB | Cedric Gray | 4.6 | 3.0 solo, 3.0 ast, 0.04 sack, 0.00 PD, 0.00 INT |  |
| LB | Anthony Hill Jr. | 3.2 | 4.9 solo, 5.4 ast, 0.00 sack, 0.27 PD, 0.00 INT | Questionable |
| LB | Cody Barton | 1.2 | 1.6 solo, 2.2 ast, 0.00 sack, 0.19 PD, 0.00 INT | Questionable |
| DB | Kevin Winston Jr. | 5.8 | 3.5 solo, 3.1 ast, 0.03 sack, 0.07 PD, 0.00 INT |  |
| DB | Cordale Flott | 4.4 | 2.4 solo, 1.3 ast, 0.00 sack, 0.48 PD, 0.30 INT |  |
| DB | Alontae Taylor | 4.4 | 3.1 solo, 0.9 ast, 0.11 sack, 0.00 PD, 0.00 INT |  |

### KC @ ATL

Market: ATL +3.0, total 47.0. Sim: KC 25.2, ATL 22.1. ATL wins 40.7%, KC wins 59.3%. Median margin -3.1 for ATL.

| Team stat | KC | ATL |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 33 / 22 | 33 / 20 |
| Passing yards | 239 | 219 |
| Rush attempts / yards | 26 / 124 | 27 / 115 |
| Sacks taken | 2.5 | 2.1 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.6 / 1.1 | 1.3 / 1.1 |
| Field goals | 1.9 | 1.7 |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 14.8 | 178 pass yd, 1.2 TD, 0.5 INT; 2.2 rush, 10 yd | Questionable |
| RB | Kenneth Walker III | 18.5 | 15.5 car, 76 yd, 0.66 TD; 2.9 rec, 22 yd, 0.35 TD |  |
| RB | Emmett Johnson | 6.1 | 2.4 car, 11 yd, 0.12 TD; 1.5 rec, 21 yd, 0.12 TD |  |
| RB | Kareem Hunt | 2.6 | 2.7 car, 11 yd, 0.09 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| WR | Rashee Rice | 9.0 | 3.7 rec, 37 yd, 0.27 TD |  |
| WR | Xavier Worthy | 5.7 | 3.5 rec, 32 yd, 0.16 TD | Questionable |
| WR | Josh Downs | 4.1 | 1.6 rec, 16 yd, 0.14 TD |  |
| WR | Jalen Royals | 2.5 | 1.1 rec, 10 yd, 0.08 TD |  |
| TE | Travis Kelce | 10.0 | 3.7 rec, 44 yd, 0.23 TD |  |
| TE | Noah Gray | 4.0 | 1.6 rec, 17 yd, 0.12 TD |  |
| K | Harrison Butker | 8.6 | 1.6 FG, 2.6 XP |  |
| DL | George Karlaftis | 5.7 | 1.7 solo, 1.7 ast, 0.55 sack, 1.01 PD, 0.08 INT |  |
| DL | Chris Jones | 4.1 | 1.2 solo, 1.2 ast, 0.60 sack, 0.38 PD, 0.00 INT |  |
| LB | Nick Bolton | 8.3 | 4.8 solo, 5.5 ast, 0.04 sack, 0.24 PD, 0.04 INT |  |
| LB | Drue Tranquill | 6.8 | 4.3 solo, 4.2 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.8 | 1.2 solo, 1.7 ast, 0.00 sack, 0.10 PD, 0.10 INT |  |
| DB | Nohl Williams | 5.1 | 2.5 solo, 1.7 ast, 0.11 sack, 1.03 PD, 0.11 INT |  |
| DB | Chamarri Conner | 5.0 | 3.2 solo, 2.1 ast, 0.16 sack, 0.16 PD, 0.06 INT |  |
| DB | Jaden Hicks | 3.1 | 2.0 solo, 1.6 ast, 0.02 sack, 0.19 PD, 0.00 INT |  |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 16.7 | 219 pass yd, 1.3 TD, 0.9 INT; 3.3 rush, 14 yd |  |
| RB | Bijan Robinson | 21.6 | 19.2 car, 84 yd, 0.92 TD; 3.9 rec, 30 yd, 0.17 TD |  |
| RB | Khalil Herbert | 4.0 | 2.5 car, 10 yd, 0.05 TD; 1.4 rec, 11 yd, 0.04 TD |  |
| WR | Drake London | 12.7 | 5.1 rec, 62 yd, 0.25 TD |  |
| WR | Jahan Dotson | 6.7 | 2.2 rec, 35 yd, 0.18 TD |  |
| WR | Olamide Zaccheaus | 2.2 | 1.1 rec, 8 yd, 0.05 TD |  |
| WR | Chris Blair | 0.7 | 0.3 rec, 3 yd, 0.01 TD |  |
| TE | Kyle Pitts | 9.3 | 3.9 rec, 34 yd, 0.34 TD |  |
| TE | Austin Hooper | 2.6 | 1.2 rec, 10 yd, 0.07 TD |  |
| DL | LaCale London | 3.7 | 1.7 solo, 2.0 ast, 0.32 sack, 0.03 PD, 0.00 INT |  |
| DL | Cameron Thomas | 2.8 | 1.0 solo, 2.1 ast, 0.18 sack, 0.10 PD, 0.00 INT |  |
| LB | Kendal Daniels | 7.6 | 5.0 solo, 2.7 ast, 0.10 sack, 0.24 PD, 0.13 INT |  |
| LB | Harold Perkins Jr. | 4.6 | 2.7 solo, 2.0 ast, 0.20 sack, 0.09 PD, 0.00 INT |  |
| LB | Divine Deablo | 2.8 | 2.1 solo, 2.3 ast, 0.02 sack, 0.24 PD, 0.00 INT | Questionable |
| DB | Xavier Watts | 6.1 | 3.1 solo, 3.4 ast, 0.04 sack, 0.32 PD, 0.15 INT |  |
| DB | C.J. Henderson | 5.6 | 3.4 solo, 1.5 ast, 0.00 sack, 1.00 PD, 0.04 INT |  |
| DB | Mike Hughes | 3.3 | 2.2 solo, 1.0 ast, 0.00 sack, 0.48 PD, 0.03 INT |  |

### LA @ ARI

Market: ARI +9.5, total 39.5. Sim: LA 24.7, ARI 15.3. ARI wins 23.3%, LA wins 76.7%. Median margin -9.5 for ARI.

| Team stat | LA | ARI |
|---|---|---|
| Plays | 64 | 65 |
| Pass attempts / completions | 33 / 22 | 39 / 25 |
| Passing yards | 245 | 241 |
| Rush attempts / yards | 29 / 136 | 24 / 101 |
| Sacks taken | 2.1 | 2.6 |
| Interceptions thrown | 0.6 | 0.8 |
| Passing / rushing TDs | 1.6 / 1.1 | 1.1 / 0.6 |
| Field goals | 1.9 | 1.1 |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 18.5 | 245 pass yd, 1.6 TD, 0.6 INT; 1.4 rush, 5 yd |  |
| RB | Kyren Williams | 20.2 | 15.0 car, 68 yd, 0.57 TD; 4.8 rec, 42 yd, 0.20 TD |  |
| RB | Blake Corum | 12.0 | 10.5 car, 53 yd, 0.48 TD; 1.4 rec, 17 yd, 0.14 TD |  |
| RB | Ronnie Rivers | 0.6 | 0.8 car, 4 yd, 0.02 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Konata Mumpfield | 5.7 | 2.1 rec, 27 yd, 0.16 TD |  |
| WR | Tutu Atwell | 4.7 | 1.8 rec, 25 yd, 0.08 TD |  |
| WR | Xavier Smith | 1.9 | 0.7 rec, 10 yd, 0.03 TD |  |
| TE | Tyler Higbee | 11.1 | 4.4 rec, 52 yd, 0.27 TD |  |
| TE | Colby Parkinson | 7.4 | 4.0 rec, 37 yd, 0.37 TD | Questionable |
| K | Brandon McManus | 8.1 | 1.5 FG, 2.5 XP |  |
| DL | Braden Fiske | 2.7 | 1.4 solo, 1.0 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Aaron Donald | 1.6 | 1.0 solo, 0.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Myles Garrett | 11.7 | 3.2 solo, 0.0 ast, 3.47 sack, 0.00 PD, 0.00 INT | Questionable |
| LB | Nate Landman | 7.0 | 4.1 solo, 3.3 ast, 0.04 sack, 0.32 PD, 0.03 INT |  |
| LB | Omar Speights | 5.3 | 3.1 solo, 2.2 ast, 0.17 sack, 0.24 PD, 0.00 INT |  |
| DB | Quentin Lake | 8.5 | 4.0 solo, 3.2 ast, 0.00 sack, 1.20 PD, 0.39 INT |  |
| DB | Josh Wallace | 4.7 | 3.0 solo, 1.4 ast, 0.00 sack, 0.62 PD, 0.13 INT |  |
| DB | Kamren Kinchens | 4.1 | 2.6 solo, 2.3 ast, 0.04 sack, 0.23 PD, 0.00 INT |  |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Carson Beck | 14.6 | 241 pass yd, 1.1 TD, 0.8 INT |  |
| RB | Tyler Allgeier | 16.4 | 16.4 car, 69 yd, 0.45 TD; 3.7 rec, 26 yd, 0.13 TD |  |
| RB | Bam Knight | 5.1 | 6.8 car, 31 yd, 0.10 TD; 1.6 rec, 14 yd, 0.03 TD | Questionable |
| RB | Evan Hull | 2.6 | 0.0 car, 0 yd, 0.00 TD; 1.2 rec, 12 yd, 0.03 TD |  |
| WR | Reggie Virgil | 4.7 | 2.0 rec, 24 yd, 0.06 TD |  |
| WR | Devin Duvernay | 1.5 | 0.8 rec, 7 yd, 0.02 TD |  |
| WR | Xavier Weaver | 0.8 | 0.5 rec, 5 yd, 0.01 TD | Questionable |
| WR | Simi Fehoko | 0.8 | 0.4 rec, 4 yd, 0.00 TD |  |
| TE | Trey McBride | 24.4 | 12.2 rec, 97 yd, 0.43 TD |  |
| TE | Elijah Higgins | 6.9 | 3.4 rec, 30 yd, 0.09 TD |  |
| K | Chad Ryland | 8.8 | 1.9 FG, 1.6 XP |  |
| DL | Andrew Billings | 2.6 | 1.2 solo, 1.2 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.6 | 1.1 solo, 1.8 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.2 | 2.9 solo, 4.3 ast, 0.03 sack, 0.07 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.1 | 2.6 solo, 4.1 ast, 0.00 sack, 0.23 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.3 | 1.6 solo, 1.0 ast, 0.22 sack, 0.13 PD, 0.00 INT |  |
| DB | Budda Baker | 6.9 | 3.2 solo, 4.1 ast, 0.26 sack, 0.35 PD, 0.07 INT |  |
| DB | Denzel Burke | 4.5 | 2.5 solo, 0.9 ast, 0.00 sack, 0.97 PD, 0.11 INT |  |
| DB | Andrew Wingard | 4.0 | 3.1 solo, 3.4 ast, 0.00 sack, 0.08 PD, 0.08 INT | Questionable |

### LAC @ BAL

Market: BAL -4.5, total 38.5. Sim: LAC 17.2, BAL 21.6. BAL wins 63.3%, LAC wins 36.7%. Median margin +4.6 for BAL.

| Team stat | LAC | BAL |
|---|---|---|
| Plays | 63 | 60 |
| Pass attempts / completions | 34 / 21 | 28 / 18 |
| Passing yards | 246 | 208 |
| Rush attempts / yards | 27 / 104 | 29 / 134 |
| Sacks taken | 2.2 | 2.0 |
| Interceptions thrown | 0.9 | 0.8 |
| Passing / rushing TDs | 1.1 / 0.8 | 1.2 / 1.2 |
| Field goals | 1.3 | 1.6 |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.6 | 246 pass yd, 1.1 TD, 0.9 INT; 3.6 rush, 17 yd | Questionable |
| RB | Omarion Hampton | 9.0 | 10.4 car, 38 yd, 0.38 TD; 1.6 rec, 11 yd, 0.05 TD |  |
| RB | Keaton Mitchell | 7.0 | 4.9 car, 19 yd, 0.07 TD; 2.3 rec, 18 yd, 0.10 TD |  |
| RB | Kimani Vidal | 6.2 | 5.3 car, 21 yd, 0.18 TD; 1.4 rec, 12 yd, 0.08 TD |  |
| WR | Quentin Johnston | 7.1 | 2.2 rec, 36 yd, 0.19 TD |  |
| WR | Tre Harris | 6.5 | 2.9 rec, 32 yd, 0.07 TD |  |
| WR | Ladd McConkey | 4.7 | 2.3 rec, 32 yd, 0.15 TD | Questionable |
| WR | KeAndre Lambert-Smith | 3.7 | 1.4 rec, 18 yd, 0.08 TD |  |
| TE | Oronde Gadsden II | 5.7 | 2.5 rec, 24 yd, 0.12 TD |  |
| TE | Charlie Kolar | 4.8 | 2.2 rec, 22 yd, 0.06 TD |  |
| K | Cameron Dicker | 9.0 | 1.9 FG, 1.7 XP |  |
| DL | Justin Eboigbe | 1.9 | 1.1 solo, 1.7 ast, 0.13 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Teair Tart | 1.7 | 1.1 solo, 1.1 ast, 0.00 sack, 0.07 PD, 0.00 INT |  |
| LB | Tuli Tuipulotu | 4.8 | 1.8 solo, 1.6 ast, 0.39 sack, 0.24 PD, 0.08 INT |  |
| LB | Troy Dye | 3.4 | 1.8 solo, 1.0 ast, 0.11 sack, 0.20 PD, 0.00 INT |  |
| LB | Del'Shawn Phillips | 3.3 | 1.9 solo, 2.6 ast, 0.04 sack, 0.00 PD, 0.00 INT |  |
| DB | Tony Jefferson | 4.4 | 2.6 solo, 2.1 ast, 0.06 sack, 0.19 PD, 0.05 INT |  |
| DB | Tarheeb Still | 3.9 | 2.4 solo, 1.4 ast, 0.00 sack, 0.37 PD, 0.11 INT |  |
| DB | Cam Hart | 3.8 | 2.0 solo, 1.5 ast, 0.00 sack, 0.52 PD, 0.18 INT |  |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 13.7 | 208 pass yd, 1.2 TD, 0.8 INT |  |
| RB | Derrick Henry | 15.4 | 19.4 car, 84 yd, 0.85 TD; 1.0 rec, 8 yd, 0.07 TD |  |
| RB | Justice Hill | 7.9 | 4.1 car, 24 yd, 0.19 TD; 2.4 rec, 16 yd, 0.07 TD |  |
| RB | Rasheen Ali | 1.1 | 0.8 car, 4 yd, 0.02 TD; 0.2 rec, 2 yd, 0.02 TD |  |
| WR | Zay Flowers | 14.1 | 0.8 car, 4 yd, 0.04 TD; 5.0 rec, 63 yd, 0.37 TD |  |
| WR | Rashod Bateman | 4.8 | 1.9 rec, 24 yd, 0.10 TD |  |
| WR | Ja'Kobi Lane | 2.9 | 1.3 rec, 14 yd, 0.04 TD |  |
| WR | Devontez Walker | 2.3 | 0.7 rec, 9 yd, 0.12 TD |  |
| TE | Mark Andrews | 6.3 | 3.0 rec, 24 yd, 0.12 TD |  |
| TE | Josh Cuevas | 3.4 | 1.3 rec, 15 yd, 0.11 TD |  |
| DL | Nnamdi Madubuike | 3.1 | 1.5 solo, 1.5 ast, 0.16 sack, 0.41 PD, 0.00 INT |  |
| DL | Travis Jones | 2.8 | 1.4 solo, 1.5 ast, 0.14 sack, 0.06 PD, 0.00 INT |  |
| LB | Roquan Smith | 7.4 | 3.8 solo, 4.4 ast, 0.17 sack, 0.31 PD, 0.05 INT |  |
| LB | Trenton Simpson | 5.6 | 3.1 solo, 3.3 ast, 0.13 sack, 0.08 PD, 0.08 INT |  |
| LB | Mike Green | 3.0 | 1.1 solo, 1.2 ast, 0.37 sack, 0.00 PD, 0.00 INT |  |
| DB | K'Von Wallace | 5.2 | 4.4 solo, 0.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Malaki Starks | 5.1 | 3.3 solo, 2.2 ast, 0.05 sack, 0.16 PD, 0.00 INT |  |
| DB | Marlon Humphrey | 4.7 | 2.3 solo, 1.4 ast, 0.00 sack, 1.18 PD, 0.10 INT |  |

### MIA @ IND

Market: IND -4.0, total 38.0. Sim: MIA 17.2, IND 21.2. IND wins 61.7%, MIA wins 38.3%. Median margin +4.0 for IND.

| Team stat | MIA | IND |
|---|---|---|
| Plays | 59 | 62 |
| Pass attempts / completions | 30 / 19 | 32 / 20 |
| Passing yards | 230 | 213 |
| Rush attempts / yards | 26 / 118 | 28 / 114 |
| Sacks taken | 1.9 | 2.3 |
| Interceptions thrown | 0.6 | 0.9 |
| Passing / rushing TDs | 1.0 / 0.9 | 1.1 / 1.2 |
| Field goals | 1.3 | 1.6 |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kyle McCord | 13.6 | 230 pass yd, 1.0 TD, 0.6 INT |  |
| RB | Ollie Gordon II | 15.9 | 22.1 car, 97 yd, 0.80 TD; 0.9 rec, 7 yd, 0.02 TD |  |
| RB | Kaytron Allen | 1.8 | 1.2 car, 6 yd, 0.02 TD; 0.4 rec, 7 yd, 0.01 TD |  |
| RB | DJ Herman | 0.9 | 0.0 car, 0 yd, 0.00 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Malik Washington | 10.6 | 1.8 car, 9 yd, 0.07 TD; 4.1 rec, 41 yd, 0.19 TD |  |
| WR | Caleb Douglas | 10.5 | 3.8 rec, 51 yd, 0.27 TD |  |
| WR | Kevin Coleman Jr. | 4.9 | 1.6 rec, 18 yd, 0.22 TD |  |
| WR | Chris Bell | 3.6 | 0.5 car, 3 yd, 0.01 TD; 2.0 rec, 22 yd, 0.06 TD | Questionable |
| TE | Greg Dulcich | 8.5 | 3.7 rec, 42 yd, 0.10 TD |  |
| TE | Will Kacmarek | 0.7 | 0.9 rec, 9 yd, 0.02 TD | Questionable |
| K | Riley Patterson | 7.0 | 1.4 FG, 1.8 XP |  |
| DL | Jordan Phillips | 2.3 | 1.3 solo, 1.9 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DL | Zeek Biggers | 2.0 | 0.7 solo, 1.4 ast, 0.18 sack, 0.11 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 8.2 | 4.3 solo, 5.3 ast, 0.18 sack, 0.10 PD, 0.09 INT |  |
| LB | Jordyn Brooks | 7.2 | 4.2 solo, 5.5 ast, 0.03 sack, 0.20 PD, 0.00 INT |  |
| LB | Joshua Uche | 5.1 | 2.5 solo, 1.8 ast, 0.44 sack, 0.18 PD, 0.00 INT |  |
| DB | Michael Taaffe | 5.4 | 2.9 solo, 2.9 ast, 0.00 sack, 0.21 PD, 0.21 INT |  |
| DB | Chris Johnson | 4.7 | 2.3 solo, 2.5 ast, 0.00 sack, 0.33 PD, 0.18 INT |  |
| DB | Dante Trader Jr. | 3.7 | 2.1 solo, 2.3 ast, 0.00 sack, 0.23 PD, 0.06 INT |  |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 15.1 | 213 pass yd, 1.1 TD, 0.9 INT; 2.6 rush, 10 yd |  |
| RB | Jonathan Taylor | 18.0 | 15.2 car, 58 yd, 0.65 TD; 4.2 rec, 37 yd, 0.10 TD |  |
| RB | Seth McGowan | 4.6 | 4.7 car, 22 yd, 0.18 TD; 0.7 rec, 6 yd, 0.02 TD |  |
| RB | DJ Giddens | 1.3 | 2.2 car, 10 yd, 0.05 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Laquon Treadwell | 5.5 | 2.3 rec, 28 yd, 0.07 TD |  |
| WR | Ashton Dulin | 4.4 | 1.1 rec, 17 yd, 0.25 TD |  |
| WR | Deion Burks | 2.9 | 1.3 rec, 13 yd, 0.03 TD |  |
| TE | Tyler Warren | 14.0 | 6.4 rec, 54 yd, 0.30 TD |  |
| TE | Will Mallory | 3.2 | 1.4 rec, 15 yd, 0.05 TD |  |
| K | Spencer Shrader | 9.7 | 2.0 FG, 2.2 XP |  |
| DL | Adetomiwa Adebawore | 3.5 | 1.3 solo, 1.2 ast, 0.41 sack, 0.39 PD, 0.00 INT |  |
| DL | Jaylahn Tuimoloau | 3.2 | 1.0 solo, 1.4 ast, 0.26 sack, 0.48 PD, 0.00 INT |  |
| LB | CJ Allen | 3.8 | 1.5 solo, 3.1 ast, 0.19 sack, 0.21 PD, 0.00 INT |  |
| LB | Bryce Boettcher | 3.2 | 1.6 solo, 3.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Germaine Pratt | 2.3 | 1.1 solo, 1.5 ast, 0.00 sack, 0.22 PD, 0.06 INT |  |
| DB | Hunter Wohler | 3.6 | 2.2 solo, 2.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Camryn Bynum | 3.6 | 2.0 solo, 1.3 ast, 0.00 sack, 0.51 PD, 0.13 INT |  |
| DB | Sauce Gardner | 3.4 | 2.4 solo, 0.5 ast, 0.00 sack, 0.77 PD, 0.00 INT |  |

### MIN @ GB

Market: GB -3.0, total 42.0. Sim: MIN 19.6, GB 22.6. GB wins 59.2%, MIN wins 40.8%. Median margin +3.1 for GB.

| Team stat | MIN | GB |
|---|---|---|
| Plays | 58 | 61 |
| Pass attempts / completions | 32 / 20 | 31 / 20 |
| Passing yards | 208 | 212 |
| Rush attempts / yards | 24 / 102 | 27 / 96 |
| Sacks taken | 2.2 | 3.4 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.8 | 1.3 / 1.1 |
| Field goals | 1.5 | 1.7 |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 14.9 | 208 pass yd, 1.4 TD, 0.8 INT |  |
| RB | Aaron Jones | 10.7 | 10.9 car, 43 yd, 0.38 TD; 2.2 rec, 15 yd, 0.07 TD |  |
| RB | Jordan Mason | 5.5 | 6.9 car, 30 yd, 0.22 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| RB | DeeJay Dallas | 1.2 | 0.4 car, 2 yd, 0.00 TD; 0.5 rec, 4 yd, 0.02 TD |  |
| WR | Justin Jefferson | 13.0 | 4.9 rec, 52 yd, 0.48 TD |  |
| WR | Jordan Addison | 8.0 | 2.9 rec, 36 yd, 0.19 TD |  |
| WR | Myles Price | 1.7 | 0.8 rec, 7 yd, 0.03 TD |  |
| WR | Tai Felton | 1.5 | 0.7 rec, 7 yd, 0.02 TD |  |
| TE | T.J. Hockenson | 4.3 | 4.4 rec, 39 yd, 0.40 TD | Questionable |
| TE | Gavin Bartholomew | 3.1 | 1.5 rec, 13 yd, 0.05 TD |  |
| K | Will Reichard | 9.8 | 2.1 FG, 2.0 XP |  |
| DL | Jalen Redmond | 3.8 | 1.8 solo, 1.6 ast, 0.19 sack, 0.34 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 2.2 | 1.1 solo, 1.5 ast, 0.11 sack, 0.00 PD, 0.00 INT |  |
| LB | Andrew Van Ginkel | 6.1 | 1.7 solo, 1.7 ast, 0.88 sack, 0.27 PD, 0.10 INT |  |
| LB | Eric Wilson | 6.1 | 3.1 solo, 3.5 ast, 0.38 sack, 0.07 PD, 0.00 INT |  |
| LB | Dallas Turner | 5.5 | 1.7 solo, 1.4 ast, 0.75 sack, 0.17 PD, 0.00 INT |  |
| DB | Byron Murphy | 6.0 | 3.2 solo, 1.2 ast, 0.00 sack, 0.76 PD, 0.47 INT |  |
| DB | Josh Metellus | 5.7 | 3.4 solo, 3.5 ast, 0.04 sack, 0.43 PD, 0.00 INT |  |
| DB | James Pierre | 4.9 | 3.4 solo, 0.7 ast, 0.00 sack, 0.41 PD, 0.25 INT |  |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 16.8 | 212 pass yd, 1.3 TD, 0.7 INT; 1.4 rush, 6 yd |  |
| RB | Pierre Strong | 5.7 | 5.5 car, 19 yd, 0.13 TD; 1.7 rec, 12 yd, 0.05 TD |  |
| RB | Kaleb Johnson | 4.7 | 6.7 car, 27 yd, 0.31 TD; 0.2 rec, 1 yd, 0.00 TD |  |
| RB | Josh Jacobs | 3.5 | 8.9 car, 28 yd, 0.38 TD; 1.9 rec, 12 yd, 0.16 TD | Questionable |
| WR | Christian Watson | 13.0 | 4.7 rec, 62 yd, 0.35 TD |  |
| WR | Matthew Golden | 12.6 | 5.0 rec, 55 yd, 0.35 TD |  |
| WR | Savion Williams | 3.2 | 1.6 car, 7 yd, 0.03 TD; 1.5 rec, 13 yd, 0.11 TD | Questionable |
| WR | Bo Melton | 0.9 | 0.6 rec, 5 yd, 0.03 TD | Questionable |
| TE | Tucker Kraft | 7.6 | 0.6 car, 3 yd, 0.01 TD; 3.4 rec, 27 yd, 0.21 TD |  |
| TE | Jonnu Smith | 1.3 | 0.6 rec, 6 yd, 0.02 TD |  |
| K | Trey Smack | 6.3 | 1.6 FG, 2.3 XP | Questionable |
| DL | Barryn Sorrell | 3.0 | 1.8 solo, 1.1 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| DL | Brenton Cox Jr. | 3.0 | 1.2 solo, 0.9 ast, 0.25 sack, 0.00 PD, 0.00 INT |  |
| LB | Isaiah McDuffie | 5.9 | 2.8 solo, 3.3 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Ty'Ron Hopper | 3.4 | 1.8 solo, 1.7 ast, 0.14 sack, 0.65 PD, 0.25 INT | Questionable |
| LB | Dani Dennis-Sutton | 3.3 | 1.0 solo, 1.5 ast, 0.37 sack, 0.25 PD, 0.00 INT |  |
| DB | Evan Williams | 7.8 | 4.5 solo, 2.7 ast, 0.07 sack, 0.64 PD, 0.31 INT |  |
| DB | Xavier McKinney | 6.1 | 2.5 solo, 2.1 ast, 0.07 sack, 0.77 PD, 0.52 INT |  |
| DB | Brandon Cisse | 4.9 | 2.4 solo, 1.3 ast, 0.13 sack, 1.11 PD, 0.11 INT |  |

### NE @ DET

Market: DET -3.0, total 51.0. Sim: NE 23.9, DET 27.0. DET wins 59.1%, NE wins 40.9%. Median margin +3.0 for DET.

| Team stat | NE | DET |
|---|---|---|
| Plays | 61 | 64 |
| Pass attempts / completions | 32 / 21 | 34 / 23 |
| Passing yards | 259 | 259 |
| Rush attempts / yards | 26 / 121 | 28 / 117 |
| Sacks taken | 2.6 | 2.7 |
| Interceptions thrown | 0.8 | 0.6 |
| Passing / rushing TDs | 1.5 / 1.1 | 1.7 / 1.2 |
| Field goals | 1.8 | 2.0 |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 22.3 | 259 pass yd, 1.5 TD, 0.8 INT; 5.5 rush, 25 yd |  |
| RB | Corey Kiner | 5.0 | 6.5 car, 32 yd, 0.26 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| RB | Rhamondre Stevenson | 3.7 | 11.5 car, 53 yd, 0.43 TD; 3.0 rec, 31 yd, 0.22 TD | Questionable |
| RB | Lan Larison | 1.2 | 0.9 car, 4 yd, 0.02 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | DeMario Douglas | 9.8 | 3.6 rec, 47 yd, 0.27 TD |  |
| WR | Mack Hollins | 7.0 | 2.8 rec, 31 yd, 0.19 TD |  |
| WR | Efton Chism III | 6.3 | 2.5 rec, 26 yd, 0.18 TD |  |
| WR | A.J. Brown | 3.7 | 2.1 rec, 23 yd, 0.10 TD | Questionable |
| TE | Hunter Henry | 6.9 | 3.9 rec, 41 yd, 0.21 TD | Questionable |
| TE | Eli Raridon | 6.2 | 2.3 rec, 29 yd, 0.16 TD |  |
| K | Andy Borregales | 7.5 | 1.4 FG, 2.4 XP |  |
| DL | Christian Barmore | 3.3 | 1.0 solo, 0.7 ast, 0.59 sack, 0.00 PD, 0.00 INT |  |
| DL | Cory Durden | 2.7 | 1.3 solo, 1.5 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Christian Elliss | 6.1 | 3.5 solo, 4.0 ast, 0.13 sack, 0.16 PD, 0.00 INT |  |
| LB | Elijah Ponder | 5.1 | 1.4 solo, 1.0 ast, 0.82 sack, 0.13 PD, 0.00 INT |  |
| LB | Robert Spillane | 3.8 | 1.6 solo, 3.4 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |
| DB | Marcus Jones | 5.3 | 3.0 solo, 2.1 ast, 0.16 sack, 0.50 PD, 0.07 INT |  |
| DB | Craig Woodson | 5.0 | 2.8 solo, 2.2 ast, 0.00 sack, 0.26 PD, 0.08 INT |  |
| DB | Christian Gonzalez | 5.0 | 4.0 solo, 0.7 ast, 0.00 sack, 0.59 PD, 0.00 INT |  |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 20.7 | 259 pass yd, 1.7 TD, 0.6 INT; 2.2 rush, 8 yd | Questionable |
| RB | Jahmyr Gibbs | 22.8 | 21.1 car, 89 yd, 1.02 TD; 3.6 rec, 30 yd, 0.24 TD |  |
| RB | Sione Vaki | 1.3 | 3.3 car, 15 yd, 0.07 TD; 0.6 rec, 5 yd, 0.02 TD | Questionable |
| WR | Amon-Ra St. Brown | 12.5 | 6.9 rec, 71 yd, 0.44 TD | Questionable |
| WR | Jameson Williams | 11.5 | 3.6 rec, 52 yd, 0.44 TD |  |
| WR | Isaac TeSlaa | 4.4 | 1.5 rec, 21 yd, 0.14 TD |  |
| TE | Sam LaPorta | 9.7 | 3.8 rec, 40 yd, 0.30 TD |  |
| TE | Tyler Conklin | 1.6 | 0.7 rec, 7 yd, 0.03 TD |  |
| K | Jake Bates | 10.2 | 2.0 FG, 2.7 XP |  |
| DL | Aidan Hutchinson | 4.7 | 1.9 solo, 1.1 ast, 0.63 sack, 0.14 PD, 0.03 INT |  |
| DL | Alim McNeill | 3.3 | 0.8 solo, 1.1 ast, 0.60 sack, 0.10 PD, 0.00 INT |  |
| LB | Derrick Barnes | 4.2 | 2.3 solo, 1.4 ast, 0.21 sack, 0.19 PD, 0.09 INT |  |
| LB | Malcolm Rodriguez | 2.7 | 1.4 solo, 1.9 ast, 0.05 sack, 0.14 PD, 0.00 INT |  |
| LB | Trevor Nowaske | 1.8 | 1.4 solo, 0.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Chuck Clark | 6.0 | 3.2 solo, 2.3 ast, 0.10 sack, 0.39 PD, 0.26 INT |  |
| DB | Roger McCreary | 5.0 | 3.1 solo, 1.1 ast, 0.08 sack, 1.02 PD, 0.00 INT |  |
| DB | Christian Izien | 3.2 | 2.0 solo, 1.4 ast, 0.13 sack, 0.11 PD, 0.00 INT |  |

### PIT @ CIN

Market: CIN -3.5, total 49.5. Sim: PIT 23.0, CIN 26.6. CIN wins 61.0%, PIT wins 39.0%. Median margin +3.6 for CIN.

| Team stat | PIT | CIN |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 35 / 22 | 35 / 25 |
| Passing yards | 233 | 275 |
| Rush attempts / yards | 25 / 132 | 24 / 98 |
| Sacks taken | 3.1 | 2.9 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.8 / 1.1 |
| Field goals | 1.7 | 2.0 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 17.8 | 233 pass yd, 1.5 TD, 0.7 INT; 1.3 rush, 6 yd |  |
| RB | Jaylen Warren | 18.2 | 14.0 car, 81 yd, 0.49 TD; 3.1 rec, 31 yd, 0.19 TD |  |
| RB | Rico Dowdle | 9.7 | 7.5 car, 34 yd, 0.32 TD; 2.3 rec, 18 yd, 0.07 TD |  |
| WR | Germie Bernard | 11.4 | 5.4 rec, 45 yd, 0.25 TD |  |
| WR | DK Metcalf | 11.1 | 4.6 rec, 50 yd, 0.27 TD |  |
| WR | Scott Miller | 1.8 | 0.9 rec, 8 yd, 0.03 TD |  |
| WR | Brandon Smith | 1.5 | 0.7 rec, 7 yd, 0.02 TD |  |
| TE | Pat Freiermuth | 9.1 | 3.2 rec, 31 yd, 0.33 TD |  |
| TE | Darnell Washington | 7.6 | 2.6 rec, 31 yd, 0.31 TD |  |
| K | Chris Boswell | 9.7 | 2.0 FG, 2.3 XP |  |
| DL | Cameron Heyward | 5.0 | 2.0 solo, 2.1 ast, 0.42 sack, 0.55 PD, 0.00 INT |  |
| DL | Kevin Jobity Jr. | 4.2 | 1.0 solo, 0.0 ast, 1.06 sack, 0.00 PD, 0.00 INT |  |
| LB | Patrick Queen | 7.3 | 3.0 solo, 4.5 ast, 0.37 sack, 0.44 PD, 0.07 INT |  |
| LB | Payton Wilson | 7.2 | 4.1 solo, 3.6 ast, 0.13 sack, 0.32 PD, 0.14 INT |  |
| LB | T.J. Watt | 6.3 | 1.5 solo, 0.9 ast, 0.88 sack, 0.41 PD, 0.14 INT |  |
| DB | Jamel Dean | 6.0 | 2.8 solo, 1.5 ast, 0.00 sack, 1.26 PD, 0.17 INT |  |
| DB | Jalen Ramsey | 5.9 | 3.5 solo, 2.3 ast, 0.28 sack, 0.27 PD, 0.00 INT |  |
| DB | Jaquan Brisker | 5.4 | 3.2 solo, 3.2 ast, 0.00 sack, 0.36 PD, 0.08 INT |  |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 22.9 | 275 pass yd, 1.8 TD, 0.8 INT; 2.7 rush, 11 yd |  |
| RB | Chase Brown | 15.9 | 12.9 car, 52 yd, 0.44 TD; 4.4 rec, 27 yd, 0.18 TD |  |
| RB | Samaje Perine | 6.4 | 6.8 car, 27 yd, 0.29 TD; 0.9 rec, 8 yd, 0.06 TD |  |
| WR | Ja'Marr Chase | 17.4 | 7.0 rec, 76 yd, 0.47 TD |  |
| WR | Tee Higgins | 15.4 | 5.6 rec, 72 yd, 0.44 TD |  |
| WR | Dohnte Meyers | 5.2 | 2.2 rec, 24 yd, 0.08 TD |  |
| WR | Mitchell Tinsley | 2.3 | 1.0 rec, 10 yd, 0.05 TD |  |
| TE | Mike Gesicki | 6.4 | 2.3 rec, 26 yd, 0.26 TD |  |
| TE | Drew Sample | 2.6 | 1.1 rec, 10 yd, 0.08 TD |  |
| K | Evan McPherson | 8.1 | 1.4 FG, 2.7 XP |  |
| DL | Boye Mafe | 5.4 | 1.9 solo, 1.1 ast, 0.74 sack, 0.14 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 5.1 | 1.9 solo, 1.6 ast, 0.66 sack, 0.16 PD, 0.00 INT |  |
| LB | Barrett Carter | 7.5 | 3.1 solo, 4.8 ast, 0.14 sack, 0.58 PD, 0.19 INT |  |
| LB | Demetrius Knight Jr. | 6.5 | 3.6 solo, 3.3 ast, 0.13 sack, 0.20 PD, 0.15 INT |  |
| LB | Joe Giles-Harris | 1.5 | 1.0 solo, 0.9 ast, 0.00 sack, 0.04 PD, 0.00 INT |  |
| DB | Jordan Battle | 7.5 | 4.5 solo, 2.0 ast, 0.00 sack, 0.85 PD, 0.33 INT |  |
| DB | Bryan Cook | 5.6 | 3.8 solo, 2.4 ast, 0.08 sack, 0.00 PD, 0.00 INT |  |
| DB | Daxton Hill | 4.4 | 3.0 solo, 1.1 ast, 0.00 sack, 0.65 PD, 0.00 INT |  |

### SEA @ LV

Market: LV +6.5, total 40.5. Sim: SEA 23.7, LV 17.2. LV wins 31.1%, SEA wins 68.9%. Median margin -6.3 for LV.

| Team stat | SEA | LV |
|---|---|---|
| Plays | 61 | 60 |
| Pass attempts / completions | 30 / 19 | 35 / 22 |
| Passing yards | 216 | 226 |
| Rush attempts / yards | 28 / 123 | 23 / 73 |
| Sacks taken | 2.3 | 2.4 |
| Interceptions thrown | 0.7 | 0.9 |
| Passing / rushing TDs | 1.4 / 1.2 | 1.1 / 0.7 |
| Field goals | 1.8 | 1.3 |

**SEA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drew Lock | 16.0 | 216 pass yd, 1.4 TD, 0.7 INT; 1.1 rush, 5 yd | Questionable |
| RB | Emanuel Wilson | 9.3 | 11.0 car, 45 yd, 0.49 TD; 0.7 rec, 8 yd, 0.07 TD |  |
| RB | Zach Charbonnet | 7.3 | 6.3 car, 30 yd, 0.28 TD; 1.3 rec, 10 yd, 0.05 TD |  |
| RB | Jadarian Price | 6.7 | 5.8 car, 24 yd, 0.13 TD; 1.7 rec, 16 yd, 0.06 TD |  |
| WR | Jaxon Smith-Njigba | 19.9 | 7.5 rec, 90 yd, 0.56 TD |  |
| WR | Cooper Kupp | 5.9 | 2.4 rec, 25 yd, 0.18 TD |  |
| WR | Tory Horton | 4.0 | 1.6 rec, 17 yd, 0.12 TD |  |
| TE | AJ Barner | 7.2 | 0.7 car, 3 yd, 0.13 TD; 2.6 rec, 24 yd, 0.19 TD |  |
| TE | Eric Saubert | 1.3 | 0.5 rec, 5 yd, 0.06 TD |  |
| K | Jason Myers | 9.2 | 1.8 FG, 2.4 XP |  |
| DL | Byron Murphy II | 3.4 | 1.3 solo, 1.8 ast, 0.41 sack, 0.00 PD, 0.00 INT |  |
| DL | Jarran Reed | 1.9 | 0.7 solo, 1.7 ast, 0.11 sack, 0.00 PD, 0.00 INT |  |
| LB | Ernest Jones | 8.2 | 4.3 solo, 4.8 ast, 0.27 sack, 0.52 PD, 0.08 INT |  |
| LB | Drake Thomas | 4.9 | 2.2 solo, 3.2 ast, 0.06 sack, 0.20 PD, 0.14 INT |  |
| LB | DeMarcus Lawrence | 3.7 | 1.2 solo, 1.3 ast, 0.19 sack, 0.31 PD, 0.00 INT |  |
| DB | Devon Witherspoon | 5.4 | 3.8 solo, 2.2 ast, 0.00 sack, 0.43 PD, 0.03 INT |  |
| DB | Julian Love | 5.0 | 3.1 solo, 1.5 ast, 0.00 sack, 0.61 PD, 0.17 INT |  |
| DB | Nick Emmanwori | 4.8 | 2.9 solo, 1.6 ast, 0.24 sack, 0.33 PD, 0.03 INT |  |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Fernando Mendoza | 14.1 | 226 pass yd, 1.1 TD, 0.9 INT |  |
| RB | Ashton Jeanty | 13.3 | 11.9 car, 36 yd, 0.37 TD; 3.8 rec, 29 yd, 0.15 TD |  |
| RB | Mike Washington Jr. | 4.7 | 8.7 car, 28 yd, 0.24 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| RB | Dylan Laube | 1.3 | 0.5 car, 2 yd, 0.11 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 8.2 | 3.2 rec, 38 yd, 0.19 TD |  |
| WR | Jalen Nailor | 3.9 | 1.8 rec, 15 yd, 0.10 TD |  |
| WR | Cody White | 2.6 | 1.0 rec, 10 yd, 0.10 TD |  |
| WR | Jack Bech | 2.3 | 1.1 rec, 10 yd, 0.05 TD |  |
| TE | Brock Bowers | 12.7 | 5.2 rec, 56 yd, 0.32 TD |  |
| TE | Michael Mayer | 7.2 | 3.5 rec, 32 yd, 0.09 TD |  |
| K | Matt Gay | 8.8 | 1.9 FG, 1.8 XP |  |
| DL | Maxx Crosby | 3.9 | 1.4 solo, 1.7 ast, 0.42 sack, 0.06 PD, 0.00 INT |  |
| DL | Tonka Hemingway | 2.4 | 0.8 solo, 1.0 ast, 0.28 sack, 0.24 PD, 0.00 INT |  |
| LB | Nakobe Dean | 9.0 | 4.3 solo, 6.9 ast, 0.09 sack, 0.20 PD, 0.12 INT |  |
| LB | Quay Walker | 6.2 | 2.9 solo, 5.2 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| LB | Tommy Eichenberg | 2.8 | 1.6 solo, 2.0 ast, 0.00 sack, 0.16 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 7.4 | 4.6 solo, 2.7 ast, 0.09 sack, 0.20 PD, 0.12 INT |  |
| DB | Treydan Stukes | 5.2 | 2.7 solo, 2.6 ast, 0.00 sack, 0.49 PD, 0.23 INT |  |
| DB | Eric Stokes | 4.0 | 2.7 solo, 1.2 ast, 0.05 sack, 0.33 PD, 0.00 INT |  |

### SF @ DAL

Market: DAL +4.0, total 55.5. Sim: SF 29.7, DAL 25.7. DAL wins 38.5%, SF wins 61.5%. Median margin -3.9 for DAL.

| Team stat | SF | DAL |
|---|---|---|
| Plays | 61 | 66 |
| Pass attempts / completions | 31 / 21 | 37 / 24 |
| Passing yards | 260 | 264 |
| Rush attempts / yards | 28 / 132 | 26 / 107 |
| Sacks taken | 2.0 | 2.2 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.7 / 1.5 | 1.7 / 1.1 |
| Field goals | 2.2 | 1.9 |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 23.1 | 260 pass yd, 1.7 TD, 0.6 INT; 4.0 rush, 20 yd |  |
| RB | Christian McCaffrey | 18.4 | 12.2 car, 56 yd, 0.81 TD; 3.8 rec, 30 yd, 0.21 TD |  |
| RB | Kaelon Black | 6.1 | 7.4 car, 36 yd, 0.28 TD; 0.4 rec, 3 yd, 0.02 TD |  |
| RB | Kyle Juszczyk | 2.7 | 0.1 car, 1 yd, 0.00 TD; 1.0 rec, 9 yd, 0.14 TD |  |
| WR | Jordan Watkins | 5.9 | 1.8 rec, 30 yd, 0.17 TD |  |
| WR | Deebo Samuel Sr. | 4.4 | 1.2 car, 6 yd, 0.03 TD; 1.8 rec, 21 yd, 0.20 TD | Questionable |
| WR | Keenan Allen | 4.3 | 1.9 rec, 17 yd, 0.11 TD |  |
| WR | Mike Evans | 3.7 | 3.2 rec, 46 yd, 0.26 TD | Questionable |
| TE | George Kittle | 11.4 | 4.3 rec, 51 yd, 0.34 TD |  |
| TE | Luke Farrell | 0.8 | 0.3 rec, 4 yd, 0.01 TD |  |
| K | Eddy Pineiro | 7.8 | 1.3 FG, 3.0 XP |  |
| DL | Keion White | 2.8 | 0.8 solo, 1.0 ast, 0.39 sack, 0.17 PD, 0.00 INT |  |
| DL | Mykel Williams | 2.6 | 1.2 solo, 0.9 ast, 0.30 sack, 0.00 PD, 0.00 INT |  |
| LB | Fred Warner | 9.1 | 4.7 solo, 4.9 ast, 0.05 sack, 0.32 PD, 0.00 INT |  |
| LB | Jaden Dugger | 7.4 | 4.1 solo, 1.4 ast, 0.15 sack, 0.21 PD, 0.22 INT |  |
| LB | Dre Greenlaw | 6.9 | 4.0 solo, 4.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Ji'Ayir Brown | 5.2 | 3.3 solo, 2.5 ast, 0.00 sack, 0.31 PD, 0.06 INT |  |
| DB | Malik Mustapha | 4.9 | 2.8 solo, 1.8 ast, 0.00 sack, 0.56 PD, 0.16 INT |  |
| DB | Marques Sigle | 2.9 | 1.8 solo, 1.6 ast, 0.10 sack, 0.00 PD, 0.00 INT |  |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 21.2 | 264 pass yd, 1.7 TD, 0.7 INT; 3.3 rush, 14 yd |  |
| RB | Javonte Williams | 18.0 | 20.5 car, 83 yd, 0.91 TD; 2.4 rec, 15 yd, 0.11 TD |  |
| RB | Hunter Luepke | 1.8 | 1.1 car, 5 yd, 0.03 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | CeeDee Lamb | 21.5 | 8.3 rec, 92 yd, 0.67 TD |  |
| WR | Ryan Flournoy | 10.7 | 4.1 rec, 46 yd, 0.32 TD |  |
| WR | George Pickens | 9.6 | 4.9 rec, 59 yd, 0.34 TD | Questionable |
| WR | KaVontae Turpin | 1.9 | 0.5 car, 2 yd, 0.05 TD; 0.8 rec, 9 yd, 0.06 TD | Questionable |
| TE | Brevyn Spann-Ford | 4.1 | 2.0 rec, 18 yd, 0.06 TD |  |
| K | Brandon Aubrey | 9.8 | 1.9 FG, 2.6 XP |  |
| DL | Quinnen Williams | 5.3 | 2.3 solo, 1.8 ast, 0.52 sack, 0.12 PD, 0.03 INT |  |
| DL | Otito Ogbonnia | 2.3 | 1.6 solo, 1.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Shemar James | 5.0 | 3.2 solo, 1.9 ast, 0.02 sack, 0.13 PD, 0.13 INT |  |
| LB | Dee Winters | 4.1 | 2.6 solo, 1.5 ast, 0.00 sack, 0.14 PD, 0.13 INT |  |
| LB | DeMarvion Overshown | 3.0 | 1.8 solo, 2.0 ast, 0.00 sack, 0.32 PD, 0.16 INT | Questionable |
| DB | Caleb Downs | 6.3 | 3.3 solo, 2.3 ast, 0.22 sack, 0.40 PD, 0.16 INT |  |
| DB | DaRon Bland | 3.9 | 2.7 solo, 0.9 ast, 0.00 sack, 0.76 PD, 0.00 INT |  |
| DB | Malik Hooker | 3.8 | 2.6 solo, 1.8 ast, 0.00 sack, 0.28 PD, 0.00 INT |  |

### WAS @ NYG

Market: NYG -2.0, total 41.0. Sim: WAS 19.6, NYG 21.7. NYG wins 56.0%, WAS wins 44.0%. Median margin +2.0 for NYG.

| Team stat | WAS | NYG |
|---|---|---|
| Plays | 61 | 62 |
| Pass attempts / completions | 32 / 20 | 30 / 19 |
| Passing yards | 216 | 214 |
| Rush attempts / yards | 27 / 125 | 30 / 123 |
| Sacks taken | 2.4 | 2.1 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.1 / 1.0 | 1.2 / 1.2 |
| Field goals | 1.5 | 1.6 |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 19.2 | 216 pass yd, 1.1 TD, 0.6 INT; 5.2 rush, 30 yd |  |
| RB | Rachaad White | 12.2 | 9.9 car, 44 yd, 0.41 TD; 2.5 rec, 21 yd, 0.15 TD |  |
| RB | Austin Ekeler | 6.6 | 7.6 car, 32 yd, 0.15 TD; 1.3 rec, 12 yd, 0.03 TD |  |
| WR | Stefon Diggs | 10.6 | 4.4 rec, 43 yd, 0.31 TD |  |
| WR | Antonio Williams | 8.3 | 3.8 rec, 38 yd, 0.12 TD |  |
| WR | Van Jefferson | 8.2 | 3.1 rec, 32 yd, 0.32 TD |  |
| WR | Luke McCaffrey | 0.7 | 0.3 rec, 3 yd, 0.01 TD |  |
| TE | Chig Okonkwo | 8.8 | 4.2 rec, 41 yd, 0.09 TD |  |
| TE | John Bates | 1.7 | 0.8 rec, 7 yd, 0.04 TD |  |
| K | Drew Stevens | 9.2 | 1.9 FG, 2.0 XP |  |
| DL | Dorance Armstrong | 3.3 | 1.6 solo, 1.5 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| DL | Shy Tuttle | 3.2 | 1.3 solo, 1.6 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 7.7 | 4.1 solo, 4.9 ast, 0.07 sack, 0.42 PD, 0.09 INT |  |
| LB | Frankie Luvu | 6.4 | 3.2 solo, 4.2 ast, 0.22 sack, 0.21 PD, 0.00 INT |  |
| LB | K'Lavon Chaisson | 4.4 | 1.8 solo, 1.2 ast, 0.39 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Cross | 6.1 | 3.6 solo, 1.6 ast, 0.00 sack, 0.63 PD, 0.21 INT |  |
| DB | Amik Robertson | 5.8 | 3.7 solo, 2.0 ast, 0.00 sack, 0.90 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 5.3 | 3.3 solo, 2.8 ast, 0.00 sack, 0.41 PD, 0.05 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jameis Winston | 17.5 | 214 pass yd, 1.2 TD, 0.6 INT; 3.2 rush, 14 yd |  |
| RB | Devin Singletary | 10.2 | 11.0 car, 42 yd, 0.57 TD; 1.3 rec, 10 yd, 0.07 TD |  |
| RB | Najee Harris | 4.0 | 7.2 car, 29 yd, 0.16 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| RB | Gregory Desrosiers | 2.2 | 3.9 car, 18 yd, 0.08 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Malik Nabers | 13.9 | 5.9 rec, 65 yd, 0.27 TD |  |
| WR | Malachi Fields | 5.8 | 2.2 rec, 28 yd, 0.12 TD |  |
| WR | Darnell Mooney | 4.0 | 0.8 car, 4 yd, 0.02 TD; 1.5 rec, 17 yd, 0.06 TD |  |
| WR | Darius Slayton | 2.8 | 1.1 rec, 12 yd, 0.07 TD |  |
| TE | Isaiah Likely | 11.8 | 4.7 rec, 44 yd, 0.46 TD |  |
| TE | Theo Johnson | 2.6 | 0.9 rec, 12 yd, 0.08 TD |  |
| K | Dominic Zvada | 9.6 | 2.0 FG, 2.2 XP |  |
| DL | DJ Reader | 3.0 | 1.9 solo, 1.2 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Alexander | 2.5 | 0.8 solo, 1.0 ast, 0.36 sack, 0.17 PD, 0.00 INT |  |
| LB | Arvell Reese | 11.0 | 6.2 solo, 2.4 ast, 0.74 sack, 0.42 PD, 0.11 INT |  |
| LB | Micah McFadden | 5.3 | 3.4 solo, 1.4 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| LB | Abdul Carter | 2.9 | 1.0 solo, 1.4 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| DB | Jevon Holland | 5.2 | 2.7 solo, 1.7 ast, 0.00 sack, 0.45 PD, 0.24 INT |  |
| DB | Greg Newsome II | 4.9 | 3.1 solo, 1.1 ast, 0.00 sack, 0.90 PD, 0.11 INT |  |
| DB | Deonte Banks | 4.3 | 1.7 solo, 1.3 ast, 0.00 sack, 1.11 PD, 0.09 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: WAS: Jaden Bradley, WAS: Craig Reynolds, WAS: Dyami Brown, WAS: Leo Chenal, WAS: Jacory Croskey-Merritt, WAS: Nick Bellore, WAS: Javontae Jean-Baptiste, WAS: Treylon Burks, WAS: Ale Kaho, WAS: Austin Keys, WAS: T.J. Maguranyanga, WAS: Laremy Tunsil, WAS: Terry McLaurin, WAS: Lucas Patrick, WAS: Jeremy McNichols, WAS: Daron Payne, WAS: Javon Kinlaw, WAS: Jaylin Lane, WAS: Colson Yankoff, NYG: Eric Gray, NYG: Braxton Berrios, NYG: Tyrone Tracy Jr., NYG: Brian Burns, NYG: Colton Hood, NYG: Gunner Olszewski, NYG: Chauncey Golston, NYG: Korie Black, NYG: Dawuane Smoot, NYG: Dalen Cambre, NYG: Cam Skattebo, NYG: Roy Robertson-Harris, NYG: Tremaine Edmunds, NYG: Jaxson Dart, NYG: Rico Payton, NYG: Raheem Layne, NE: Ben Brown, NE: Alijah Vera-Tucker, NE: Kindle Vildor, NE: Jeremiah Pharms Jr., NE: Tanner Arkin, NE: Harold Landry III, NE: TreVeyon Henderson, NE: Reggie Gilliam, NE: Eric Gregory, NE: Romeo Doubs, NE: Terrell Jennings, NE: Mike Onwenu, NE: Quintayvious Hutchins, NE: Dell Pettus, NE: Elliott Davison, NE: Carlton Davis III, DET: Jack Campbell, DET: Jacob Saylors, DET: Jimmy Rolder, DET: Thomas Harper, DET: Jabari Small, DET: Devin White, DET: Tom Kennedy, DET: Ben Bartch, DET: Anthony Lucas, DET: Jackson Meeks, DET: Avonte Maddox, KC: Nikko Remigio, KC: Marcus Harris, KC: Ethan Downs, KC: Mansoor Delane, KC: Cole Christiansen, KC: Brashard Smith, KC: Justin Watson, KC: Tyquan Thornton, KC: Josh Simmons, KC: L'Jarius Sneed, ATL: Jammie Robinson, ATL: Dylan Drummond, ATL: Brian Robinson, ATL: JD Bertrand, ATL: Jared Ivey, ATL: Brian Asamoah II, ATL: Jalon Walker, ATL: Michael Jerrell, ATL: Samson Ebukam, ATL: Nick Folk, HOU: Jaylin Smith, HOU: Mario Edwards, HOU: British Brooks, HOU: Jaden Crumedy, HOU: Jaylin Noel, HOU: E.J. Speed, HOU: Cade Stover, HOU: Lewis Bond, HOU: Kenneth Murray, Jr., HOU: David Montgomery, HOU: Jayden Higgins, HOU: Dylan Horton, HOU: Bryce Hall, HOU: Jawhar Jordan, HOU: George Odum, CLE: KT Leveston, CLE: Alex Wright, CLE: Nathaniel Watson, CLE: Raheim Sanders, CLE: Teven Jenkins, CLE: Carsen Ryan, MIN: Tavierre Thomas, MIN: Demond Claiborne, MIN: Jeshaun Jones, MIN: Tyler Batty, MIN: C.J. Ham, MIN: Donovan Jackson, MIN: Josh Oliver, GB: Arron Mosby, GB: Jacob Monk, GB: MarShawn Lloyd, GB: Chris Brooks, GB: Skyy Moore, GB: Jonathan Ford, GB: Edgerrin Cooper, GB: Johnathan Baldwin, GB: Javon Hargrave, GB: Drake Dabney, GB: Collin Oliver, GB: Zach Bako-Bewele, GB: Warren Brinson, GB: Jayden Reed, GB: Luke Musgrave, GB: Micah Parsons, MIA: Carlos Washington, MIA: Zane Gonzalez, MIA: Zach Sieler, MIA: Reese Taylor, MIA: Malik Willis, MIA: Ethan Bonner, MIA: Jaylen Wright, MIA: Liam Anderson, MIA: De'Von Achane, IND: Justin Walley, IND: Carl Lawson, IND: Cam Taylor-Britt, IND: Cameron Mitchell, IND: Arden Key, IND: Johnathan Edwards, IND: Alec Pierce, CAR: David Moore, CAR: Corey Thornton, CAR: Marco Wilson, CAR: Ikem Ekwonu, CAR: Mike Jackson, CAR: Akayleb Evans, CAR: LaBryan Ray, CAR: Damien Lewis, CAR: Cam Jackson, CAR: Nic Scourton, CAR: Will Lee III, CAR: Ja'Seem Reed, CAR: Jaelan Phillips, CAR: Jaycee Horn, CAR: Thomas Incoom, CAR: Xavier Legette, CAR: Taylor Moton, CAR: Claudin Cherelus, CAR: Jonathon Brooks, NO: Kevin Austin Jr., NO: Mason Tipton, NO: Moliki Matavao, NO: Treyton Welch, NO: Fadil Diggs, NO: Jayden Price, NO: Travis Etienne, NO: Jonah Williams, NO: Bryan Bresee, NO: Zamir White, NO: Jalen Cropper, NO: Charlie Smyth, NO: Dillon Radunz, BUF: Phidarian Mathis, BUF: Shaq Thompson, BUF: Josh Palmer, BUF: Keonta Jenkins, BUF: Jordan Hancock, BUF: Tre'Davious White, BUF: Kani Walker, BUF: Tyrell Shavers, BUF: Geno Stone, BUF: Frank Gore Jr., BUF: Andre Jones Jr., BUF: Trent Sherfield, NYJ: Sterling Shepard, NYJ: T'Vondre Sweat, NYJ: Kingsley Jonathan, NYJ: David Onyemata, NYJ: Francisco Mauigoa, NYJ: Samuel Womack, NYJ: Arian Smith, NYJ: Max Mitchell, NYJ: Jamaal Pritchett, NYJ: Mykal Walker, NYJ: Marcelino McCrary-Ball, NYJ: Braiden McGregor, NYJ: Jordan Clark, JAX: Cam'Ron Silmon-Craig, JAX: Nick Mullens, JAX: Austin Trammell, JAX: Patrick Mekari, JAX: Austin Johnson, JAX: DaVon Hamilton, JAX: Caleb Ransaw, JAX: Eric Murray, JAX: Anton Harrison, JAX: BJ Green II, TEN: Erick Hallett, TEN: Jaylen Harrell, TEN: James Williams, TEN: Isaiah Oliver, TEN: Tommy Townsend, TEN: Kalel Mullings, TEN: Xavier Restrepo, TEN: Thomas Morstead, TEN: Kendell Brooks, LA: Alex Bachman, LA: Dean Connors, LA: Jaylen Watson, LA: Jordan Whittington, LA: Puka Nacua, LA: Terrance Ferguson, LA: Darious Williams, LA: Pepe Williams, LA: Blake Grupe, LA: Kobie Turner, LA: Jake McQuaide, LA: Tanner Ingle, LA: Justin Dedich, LA: Poona Ford, LA: Davante Adams, ARI: Hunter Long, ARI: Paris Johnson Jr., ARI: Kenny Yeboah, ARI: Wydett Williams Jr., ARI: Kendrick Bourne, ARI: Jeremiyah Love, ARI: Will Johnson, ARI: Art Green, ARI: Gardner Minshew, ARI: Jared Harrison-Hunte, ARI: Michael Wilson, ARI: Jalen Brooks, ARI: Zachary Carter, SEA: Elijah Arroyo, SEA: Trevon Diggs, SEA: Robbie Ouzts, SEA: Julian Neal, SEA: Rashid Shaheed, SEA: Jake Bobo, SEA: Coby Bryant, SEA: AJ Finley, SEA: Velus Jones Jr., SEA: Montorie Foster Jr, SEA: Sam Darnold, LV: Cian Slone, LV: Tim Keenan III, LV: Chigozie Anusiem, LV: Deven Thompkins, LV: Patrick Johnson, LV: Greedy Vance, LV: Carter Runyon, SF: C.J. West, SF: Ricky Pearsall, SF: Alfred Collins, SF: KhaDarel Hodge, SF: Jake Tonges, SF: Nick Martin, SF: Isaac Guerendo, SF: Robert Beal Jr., SF: Sam Okuayinonu, SF: Ogbo Okoronkwo, SF: Gracen Halton, SF: Jalen Graham, DAL: James Mitchell, DAL: Malik Davis, DAL: Jonathan Bullard, DAL: Tyler Goodson, DAL: P.J. Locke, DAL: Jordan Hudson, DAL: Jake Ferguson, DAL: Malachi Lawrence, DAL: Jalen Thompson, DAL: Curtis Robinson, DAL: Luke Schoonmaker, DAL: Reddy Steward, PIT: Roman Wilson, PIT: Esezi Otomewo, PIT: Sebastian Joseph-Day, PIT: Logan Lee, PIT: Marquez Valdes-Scantling, PIT: Sebastian Castro, PIT: Michael Pittman, PIT: Brandin Echols, PIT: Doneiko Slaughter, PIT: Brandon Johnson, PIT: Ben Skowronek, PIT: Derrick Harmon, CIN: Swayze Bozeman, CIN: Isaiah Foskey, CIN: Tanner Hudson, CIN: Erick All, CIN: Bralyn Lux, CIN: Ke'Shawn Williams, CIN: Cashius Howell, CIN: Howard Cross III, CIN: Andrei Iosivas, CIN: Jalen Davis, LAC: Rashawn Slater, LAC: Hayden Rucci, LAC: Trey Lance, LAC: Daniel Brunskill, LAC: David Njoku, LAC: Trevor Penning, LAC: Denzel Perryman, LAC: Patrick Herbert, LAC: Trey Pipkins, LAC: Derwin James, LAC: Alec Ingold, BAL: Durham Smythe, BAL: Carl Jones, BAL: Lamar Jackson, BAL: Chris Moore, BAL: Jovaughn Gwyn, BAL: Tyler Huntley, BAL: Tyler Loop, BAL: Tavius Robinson, BAL: Jake Moody.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.3 | 8.4 to 37.6 |
| QB | Joe Burrow | CIN | 21.3 | 7.4 to 36.3 |
| QB | Brock Purdy | SF | 21.2 | 8.3 to 35.5 |
| QB | Drake Maye | NE | 21.0 | 7.7 to 35.5 |
| QB | Trevor Lawrence | JAX | 19.9 | 7.5 to 33.5 |
| QB | Dak Prescott | DAL | 19.6 | 7.2 to 33.2 |
| RB | Jahmyr Gibbs | DET | 24.1 | 8.2 to 41.8 |
| RB | Bijan Robinson | ATL | 22.7 | 7.7 to 39.6 |
| RB | Kyren Williams | LA | 20.9 | 7.6 to 36.2 |
| RB | Kenneth Walker III | KC | 19.2 | 5.8 to 34.5 |
| RB | Jaylen Warren | PIT | 19.1 | 6.4 to 33.9 |
| RB | Javonte Williams | DAL | 19.0 | 5.4 to 34.4 |
| RB | Christian McCaffrey | SF | 18.7 | 6.0 to 33.4 |
| RB | Jonathan Taylor | IND | 18.4 | 6.1 to 32.7 |
| RB | Ollie Gordon II | MIA | 17.3 | 4.1 to 32.4 |
| RB | Chuba Hubbard | CAR | 17.1 | 5.1 to 31.2 |
| WR | CeeDee Lamb | DAL | 22.7 | 7.9 to 39.5 |
| WR | Jaxon Smith-Njigba | SEA | 21.1 | 6.7 to 37.7 |
| WR | Ja'Marr Chase | CIN | 18.2 | 5.4 to 33.4 |
| WR | Tee Higgins | CIN | 16.1 | 3.9 to 30.8 |
| WR | Zay Flowers | BAL | 14.6 | 3.3 to 28.3 |
| WR | Malik Nabers | NYG | 14.4 | 3.7 to 27.9 |
| WR | Christian Watson | GB | 13.5 | 2.7 to 26.9 |
| WR | Justin Jefferson | MIN | 13.3 | 2.7 to 26.2 |
| WR | Drake London | ATL | 13.2 | 2.9 to 26.3 |
| WR | Tetairoa McMillan | CAR | 13.1 | 3.0 to 25.6 |
| WR | Amon-Ra St. Brown | DET | 13.1 | 0.0 to 30.0 |
| WR | Matthew Golden | GB | 13.0 | 2.8 to 25.5 |
| TE | Trey McBride | ARI | 25.7 | 10.5 to 42.6 |
| TE | Tyler Warren | IND | 14.3 | 3.8 to 27.0 |
| TE | Brock Bowers | LV | 13.1 | 3.0 to 25.9 |
| TE | Isaiah Likely | NYG | 12.0 | 2.2 to 23.8 |
| TE | George Kittle | SF | 11.7 | 2.1 to 23.3 |
| TE | Tyler Higbee | LA | 11.4 | 1.9 to 23.4 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 21.5 | 8.5 to 36.0 |
| QB | Brock Purdy | SF | 20.2 | 8.4 to 33.8 |
| QB | Joe Burrow | CIN | 20.2 | 7.6 to 34.2 |
| QB | Drake Maye | NE | 20.0 | 7.8 to 33.8 |
| QB | Trevor Lawrence | JAX | 18.9 | 7.6 to 31.4 |
| QB | Dak Prescott | DAL | 18.6 | 7.4 to 31.1 |
| RB | Jahmyr Gibbs | DET | 21.0 | 7.0 to 36.9 |
| RB | Bijan Robinson | ATL | 19.6 | 6.5 to 34.7 |
| RB | Kyren Williams | LA | 17.8 | 6.1 to 31.1 |
| RB | Kenneth Walker III | KC | 17.0 | 5.0 to 30.9 |
| RB | Javonte Williams | DAL | 16.8 | 4.7 to 30.9 |
| RB | Jaylen Warren | PIT | 16.6 | 5.7 to 29.5 |
| RB | Christian McCaffrey | SF | 16.5 | 4.7 to 29.9 |
| RB | Jonathan Taylor | IND | 15.9 | 4.7 to 28.7 |
| RB | Ollie Gordon II | MIA | 15.5 | 4.1 to 29.2 |
| RB | James Cook | BUF | 15.4 | 4.0 to 28.5 |
| WR | CeeDee Lamb | DAL | 17.4 | 5.5 to 30.9 |
| WR | Jaxon Smith-Njigba | SEA | 16.2 | 4.8 to 29.3 |
| WR | Ja'Marr Chase | CIN | 13.9 | 3.6 to 25.8 |
| WR | Tee Higgins | CIN | 12.6 | 2.7 to 23.9 |
| WR | Zay Flowers | BAL | 11.6 | 2.2 to 22.4 |
| WR | Malik Nabers | NYG | 11.0 | 2.4 to 21.1 |
| WR | Christian Watson | GB | 10.6 | 1.8 to 21.0 |
| WR | Justin Jefferson | MIN | 10.6 | 1.6 to 21.2 |
| WR | Parker Washington | JAX | 10.3 | 1.2 to 20.9 |
| WR | Tetairoa McMillan | CAR | 10.2 | 1.8 to 20.1 |
| WR | Drake London | ATL | 10.2 | 1.9 to 20.0 |
| WR | Matthew Golden | GB | 10.1 | 1.7 to 20.2 |
| TE | Trey McBride | ARI | 18.3 | 6.8 to 31.2 |
| TE | Tyler Warren | IND | 10.8 | 2.2 to 20.8 |
| TE | Brock Bowers | LV | 10.1 | 1.8 to 20.1 |
| TE | Isaiah Likely | NYG | 9.5 | 1.1 to 19.6 |
| TE | George Kittle | SF | 9.2 | 1.2 to 18.8 |
| TE | Tyler Higbee | LA | 9.0 | 1.1 to 18.2 |
| K | Tyler Bass | BUF | 10.3 | 3.0 to 18.6 |
| K | Ka'imi Fairbairn | HOU | 10.0 | 2.0 to 19.0 |
| K | Jason Sanders | NYJ | 9.6 | 1.0 to 18.6 |
| K | Jake Bates | DET | 9.5 | 2.0 to 17.6 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses come from the merged injury file (MFL, nflverse, ESPN, transactions) at the time of the pull. Re-run when news lands.
- Weather, referee tendencies and in-game injuries are not modeled.