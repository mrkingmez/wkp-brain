# Week 11 Full Simulation Report - 19 Nov 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 20,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| IND @ HOU | HOU 83.1% | IND 16.0 - HOU 28.3 | HOU | 53.1% | HOU | 83.7% |
| MIA @ BUF | BUF 89.5% | MIA 14.6 - BUF 31.1 | MIA | 50.0% | BUF | 90.3% |
| BAL @ CAR | CAR 57.0% | BAL 20.6 - CAR 23.0 | BAL | 50.0% | CAR | 57.8% |
| NO @ CHI | CHI 80.5% | NO 18.6 - CHI 30.1 | NO | 50.0% | CHI | 81.7% |
| TEN @ DAL | DAL 72.7% | TEN 23.6 - DAL 31.4 | TEN | 51.6% | DAL | 73.5% |
| TB @ DET | DET 70.2% | TB 18.6 - DET 25.5 | TB | 48.4% | DET | 70.9% |
| ARI @ KC | KC 89.1% | ARI 12.9 - KC 28.6 | ARI | 51.6% | KC | 89.6% |
| JAX @ NYG | JAX 67.5% | JAX 26.3 - NYG 20.3 | NYG | 51.6% | JAX | 68.1% |
| NYJ @ LAC | LAC 59.0% | NYJ 19.6 - LAC 22.6 | NYJ | 51.6% | LAC | 59.3% |
| LV @ DEN | DEN 77.4% | LV 15.5 - DEN 25.3 | LV | 51.6% | DEN | 78.4% |
| PIT @ PHI | PIT 63.0% | PIT 21.2 - PHI 16.8 | PHI | 50.0% | PIT | 63.8% |
| MIN @ SF | SF 58.7% | MIN 21.8 - SF 24.8 | MIN | 51.6% | SF | 59.3% |
| CIN @ WAS | CIN 68.9% | CIN 30.3 - WAS 23.8 | WSH | 50.0% | CIN | 69.5% |

**Eliminator:** biggest favorites this week by win chance: BUF 89.5%, KC 89.1%, HOU 83.1%, CHI 80.5%, DEN 77.4%. Teams already used are not tracked here, check FUTURES-PICKS.md.

## 2. IRFL lineups

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 143.5 | 109.8 | 179.0 |
| 2 SAFE (protects a lead) | 143.5 | 109.8 | 179.0 |
| 3 BALANCED UPSIDE (75th percentile) | 141.9 | 107.0 | 177.8 |
| 4 SWING (90th percentile, for an underdog) | 140.9 | 106.0 | 176.9 |
| 5 CONTINGENCY (every Questionable out) | 143.5 | 109.8 | 179.0 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 11.2 | 2.1 to 21.9 |  |
| RB | Dowdle, Rico | PIT | 8.7 | 1.5 to 17.6 |  |
| WR | Jefferson, Justin | MIN | 15.4 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.6 | 1.2 to 21.4 |  |
| WR | Flournoy, Ryan | DAL | 10.3 | 1.4 to 20.7 |  |
| TE | Schultz, Dalton | HOU | 9.1 | 1.3 to 18.3 |  |
| PK | Bates, Jake | DET | 9.4 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.1 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| LB | Gibbens, Jack | ARI | 4.5 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 11.2 | 2.1 to 21.9 |  |
| RB | Dowdle, Rico | PIT | 8.7 | 1.5 to 17.6 |  |
| WR | Jefferson, Justin | MIN | 15.4 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.6 | 1.2 to 21.4 |  |
| WR | Flournoy, Ryan | DAL | 10.3 | 1.4 to 20.7 |  |
| TE | Schultz, Dalton | HOU | 9.1 | 1.3 to 18.3 |  |
| PK | Bates, Jake | DET | 9.4 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.1 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| LB | Gibbens, Jack | ARI | 4.5 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 11.2 | 2.1 to 21.9 |  |
| RB | Dowdle, Rico | PIT | 8.7 | 1.5 to 17.6 |  |
| WR | Jefferson, Justin | MIN | 15.4 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.6 | 1.2 to 21.4 |  |
| WR | Flournoy, Ryan | DAL | 10.3 | 1.4 to 20.7 |  |
| TE | Hockenson, T.J. | MIN | 8.1 | 0.0 to 19.5 | Questionable, plays about 75% of sims. differs from lineup 1 |
| PK | Bates, Jake | DET | 9.4 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.1 | 0.0 to 8.5 |  |
| LB | Gibbens, Jack | ARI | 4.5 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| LB | Okereke, Bobby | CAR | 2.5 | 0.0 to 8.0 | Questionable, plays about 75% of sims. differs from lineup 1 |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 11.2 | 2.1 to 21.9 |  |
| RB | Dowdle, Rico | PIT | 8.7 | 1.5 to 17.6 |  |
| WR | Jefferson, Justin | MIN | 15.4 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.6 | 1.2 to 21.4 |  |
| WR | Flournoy, Ryan | DAL | 10.3 | 1.4 to 20.7 |  |
| TE | Hockenson, T.J. | MIN | 8.1 | 0.0 to 19.5 | Questionable, plays about 75% of sims. differs from lineup 1 |
| PK | Bates, Jake | DET | 9.4 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.1 | 0.0 to 8.5 |  |
| LB | Okereke, Bobby | CAR | 2.5 | 0.0 to 8.0 | Questionable, plays about 75% of sims. differs from lineup 1 |
| LB | Gibbens, Jack | ARI | 4.5 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Reed, D.J. | DET | 3.9 | 0.0 to 8.5 | Questionable, plays about 75% of sims. differs from lineup 1 |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 11.2 | 2.1 to 21.9 |  |
| RB | Dowdle, Rico | PIT | 8.7 | 1.5 to 17.6 |  |
| WR | Jefferson, Justin | MIN | 15.4 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.6 | 1.2 to 21.4 |  |
| WR | Flournoy, Ryan | DAL | 10.3 | 1.4 to 20.7 |  |
| TE | Schultz, Dalton | HOU | 9.1 | 1.3 to 18.3 |  |
| PK | Bates, Jake | DET | 9.4 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.1 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.5 |  |
| LB | Gibbens, Jack | ARI | 4.5 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

Lineups 1 and 2 are identical; 1 and 5 are identical; 2 and 5 are identical. Where they match, the roster has no real choice between safe and swing this week.

Not simulated this week (bye, no team, new team, or no recent usage, check each one): Robinson, Tavius (BAL); Reid, Winston (CLE); Folk, Nick (FA); Carter, Michael (TEN); Corum, Blake (LAR); Jenkins, Rayshawn (BAL); Kinchens, Kamren (LAR); Shepard, Sterling (NYJ); Golden, Matthew (GBP); Hollins, Mack (NEP).

Changed teams and simulated on the new team with his own old-team rates: Andre Cisco (DB, NYJ to DET); Jessie Bates (DB, ATL to JAX); Jordan Davis (DL, PHI to JAX); Daiyan Henley (LB, LAC to DEN).

Starting quarterbacks named by hand in the overrides file: BAL Jacoby Brissett; NYG J.J. McCarthy; PHI Joe Milton III; MIN Kirk Cousins.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ KC

Market: KC -16.0, total 41.0. Sim: ARI 12.9, KC 28.6. KC wins 89.1%, ARI wins 10.9%. Median margin +16.2 for KC.

| Team stat | ARI | KC |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 38 / 24 | 32 / 21 |
| Passing yards | 232 | 251 |
| Rush attempts / yards | 22 / 87 | 28 / 128 |
| Sacks taken | 2.6 | 2.2 |
| Interceptions thrown | 0.9 | 0.5 |
| Passing / rushing TDs | 0.9 / 0.5 | 1.8 / 1.3 |
| Field goals | 1.0 | 2.2 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Carson Beck | 14.4 | 232 pass yd, 0.9 TD, 0.9 INT; 2.8 rush, 11 yd |  |
| RB | Tyler Allgeier | 12.6 | 13.1 car, 50 yd, 0.35 TD; 3.1 rec, 21 yd, 0.10 TD |  |
| RB | Bam Knight | 5.6 | 6.0 car, 25 yd, 0.08 TD; 1.4 rec, 12 yd, 0.03 TD |  |
| RB | Evan Hull | 1.7 | 0.0 car, 0 yd, 0.00 TD; 0.8 rec, 8 yd, 0.02 TD |  |
| WR | Harrison Wallace III | 4.1 | 2.0 rec, 19 yd, 0.03 TD |  |
| WR | Reggie Virgil | 3.9 | 1.7 rec, 19 yd, 0.05 TD |  |
| WR | Devin Duvernay | 2.3 | 1.1 rec, 11 yd, 0.02 TD |  |
| WR | Simi Fehoko | 1.4 | 0.6 rec, 7 yd, 0.01 TD |  |
| TE | Trey McBride | 21.5 | 11.2 rec, 84 yd, 0.34 TD |  |
| TE | Elijah Higgins | 5.8 | 2.9 rec, 25 yd, 0.07 TD |  |
| K | Chad Ryland | 8.4 | 1.9 FG, 1.3 XP |  |
| DL | L.J. Collier | 2.7 | 1.1 solo, 0.9 ast, 0.27 sack, 0.34 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.4 | 1.1 solo, 1.6 ast, 0.16 sack, 0.00 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.4 | 3.1 solo, 4.0 ast, 0.00 sack, 0.19 PD, 0.00 INT |  |
| LB | Jack Gibbens | 4.5 | 2.5 solo, 3.6 ast, 0.02 sack, 0.05 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.6 | 1.5 solo, 1.5 ast, 0.32 sack, 0.11 PD, 0.00 INT |  |
| DB | Budda Baker | 6.4 | 3.0 solo, 4.0 ast, 0.23 sack, 0.30 PD, 0.07 INT |  |
| DB | Denzel Burke | 4.0 | 2.3 solo, 0.9 ast, 0.00 sack, 0.80 PD, 0.09 INT |  |
| DB | Dadrion Taylor-Demerson | 2.4 | 2.0 solo, 0.9 ast, 0.00 sack, 0.04 PD, 0.00 INT |  |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 21.3 | 251 pass yd, 1.8 TD, 0.5 INT; 2.2 rush, 10 yd |  |
| RB | Emmett Johnson | 9.7 | 5.5 car, 24 yd, 0.22 TD; 2.0 rec, 27 yd, 0.23 TD |  |
| RB | Kenneth Walker III | 7.0 | 15.2 car, 73 yd, 0.74 TD; 2.5 rec, 19 yd, 0.29 TD | Questionable |
| RB | Kareem Hunt | 2.1 | 2.0 car, 9 yd, 0.09 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | Rashee Rice | 8.5 | 3.4 rec, 39 yd, 0.20 TD |  |
| WR | Josh Downs | 7.6 | 2.8 rec, 33 yd, 0.27 TD |  |
| WR | Xavier Worthy | 6.2 | 2.8 rec, 26 yd, 0.14 TD |  |
| WR | Cyrus Allen | 3.0 | 1.0 rec, 13 yd, 0.11 TD |  |
| TE | Travis Kelce | 8.6 | 3.2 rec, 39 yd, 0.19 TD |  |
| TE | Noah Gray | 3.6 | 1.4 rec, 16 yd, 0.10 TD |  |
| K | Harrison Butker | 8.5 | 1.5 FG, 2.9 XP |  |
| DL | George Karlaftis | 6.6 | 1.7 solo, 1.7 ast, 0.83 sack, 1.20 PD, 0.08 INT |  |
| DL | Chris Jones | 4.1 | 1.0 solo, 1.2 ast, 0.69 sack, 0.38 PD, 0.00 INT |  |
| LB | Drue Tranquill | 7.2 | 4.7 solo, 4.2 ast, 0.00 sack, 0.16 PD, 0.00 INT |  |
| LB | Nick Bolton | 6.4 | 4.8 solo, 5.3 ast, 0.04 sack, 0.18 PD, 0.05 INT | Questionable |
| LB | Jack Cochrane | 2.7 | 1.1 solo, 1.9 ast, 0.00 sack, 0.11 PD, 0.10 INT |  |
| DB | Nohl Williams | 6.1 | 2.5 solo, 2.0 ast, 0.11 sack, 1.39 PD, 0.28 INT |  |
| DB | Chamarri Conner | 5.2 | 2.6 solo, 2.7 ast, 0.16 sack, 0.33 PD, 0.06 INT |  |
| DB | Mansoor Delane | 4.6 | 2.4 solo, 1.5 ast, 0.00 sack, 1.20 PD, 0.10 INT |  |

### BAL @ CAR

Market: CAR -2.5, total 43.5. Sim: BAL 20.6, CAR 23.0. CAR wins 57.0%, BAL wins 43.0%. Median margin +2.3 for CAR.

| Team stat | BAL | CAR |
|---|---|---|
| Plays | 60 | 62 |
| Pass attempts / completions | 30 / 20 | 33 / 20 |
| Passing yards | 207 | 240 |
| Rush attempts / yards | 28 / 127 | 26 / 102 |
| Sacks taken | 2.1 | 2.3 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.1 / 1.1 | 1.5 / 1.0 |
| Field goals | 1.6 | 1.7 |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 15.5 | 207 pass yd, 1.1 TD, 0.7 INT; 3.4 rush, 15 yd |  |
| RB | Derrick Henry | 14.1 | 16.4 car, 70 yd, 0.77 TD; 1.4 rec, 9 yd, 0.07 TD |  |
| RB | Justice Hill | 7.7 | 3.6 car, 21 yd, 0.15 TD; 2.6 rec, 17 yd, 0.07 TD |  |
| RB | Rasheen Ali | 0.9 | 0.7 car, 3 yd, 0.02 TD; 0.2 rec, 2 yd, 0.02 TD |  |
| WR | Zay Flowers | 12.8 | 0.6 car, 3 yd, 0.03 TD; 4.8 rec, 56 yd, 0.34 TD |  |
| WR | Rashod Bateman | 4.8 | 1.9 rec, 23 yd, 0.09 TD |  |
| WR | Ja'Kobi Lane | 4.1 | 1.8 rec, 20 yd, 0.06 TD |  |
| WR | Devontez Walker | 2.0 | 0.7 rec, 8 yd, 0.10 TD |  |
| TE | Mark Andrews | 7.2 | 3.5 rec, 29 yd, 0.12 TD |  |
| TE | Josh Cuevas | 3.6 | 1.4 rec, 16 yd, 0.11 TD |  |
| K | Riley Patterson | 8.6 | 1.7 FG, 2.1 XP |  |
| DL | Travis Jones | 2.8 | 1.6 solo, 1.3 ast, 0.12 sack, 0.05 PD, 0.00 INT |  |
| DL | Broderick Washington | 1.6 | 0.4 solo, 0.6 ast, 0.00 sack, 0.40 PD, 0.15 INT |  |
| LB | Roquan Smith | 7.2 | 4.0 solo, 3.9 ast, 0.15 sack, 0.26 PD, 0.05 INT |  |
| LB | Trenton Simpson | 5.5 | 3.1 solo, 3.5 ast, 0.10 sack, 0.07 PD, 0.07 INT |  |
| LB | Mike Green | 4.1 | 1.5 solo, 1.3 ast, 0.61 sack, 0.00 PD, 0.00 INT |  |
| DB | Kyle Hamilton | 6.5 | 4.7 solo, 1.9 ast, 0.00 sack, 0.46 PD, 0.07 INT |  |
| DB | Marlon Humphrey | 5.0 | 2.3 solo, 1.9 ast, 0.00 sack, 0.94 PD, 0.09 INT |  |
| DB | Malaki Starks | 4.8 | 2.9 solo, 2.3 ast, 0.05 sack, 0.25 PD, 0.00 INT |  |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.5 | 240 pass yd, 1.5 TD, 0.6 INT; 2.1 rush, 9 yd |  |
| RB | Chuba Hubbard | 17.6 | 18.1 car, 70 yd, 0.73 TD; 3.1 rec, 26 yd, 0.14 TD |  |
| RB | Trevor Etienne | 1.8 | 1.8 car, 7 yd, 0.04 TD; 0.5 rec, 4 yd, 0.01 TD |  |
| RB | AJ Dillon | 1.6 | 2.5 car, 9 yd, 0.05 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tetairoa McMillan | 12.0 | 4.6 rec, 56 yd, 0.31 TD |  |
| WR | Jalen Coker | 8.5 | 3.2 rec, 36 yd, 0.27 TD |  |
| WR | John Metchie III | 3.9 | 1.7 rec, 17 yd, 0.09 TD |  |
| WR | Xavier Legette | 2.0 | 0.9 rec, 10 yd, 0.03 TD |  |
| TE | Darren Waller | 2.9 | 2.6 rec, 31 yd, 0.26 TD | Questionable |
| TE | Mitchell Evans | 2.7 | 1.2 rec, 13 yd, 0.04 TD |  |
| K | Ryan Fitzgerald | 8.2 | 1.6 FG, 2.3 XP |  |
| DL | Derrick Brown | 3.9 | 2.0 solo, 1.8 ast, 0.19 sack, 0.38 PD, 0.00 INT |  |
| DL | Aaron Hall | 1.8 | 0.7 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 7.8 | 3.9 solo, 3.1 ast, 0.16 sack, 0.51 PD, 0.30 INT |  |
| LB | Patrick Jones II | 3.3 | 1.9 solo, 0.7 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| LB | Jaelan Phillips | 3.2 | 0.9 solo, 1.0 ast, 0.42 sack, 0.00 PD, 0.00 INT |  |
| DB | Marco Wilson | 5.3 | 3.7 solo, 0.9 ast, 0.00 sack, 1.15 PD, 0.00 INT |  |
| DB | Nick Scott | 4.9 | 3.6 solo, 1.3 ast, 0.00 sack, 0.21 PD, 0.03 INT |  |
| DB | Will Lee III | 4.3 | 2.5 solo, 1.3 ast, 0.00 sack, 0.67 PD, 0.00 INT |  |

### CIN @ WAS

Market: WAS +6.5, total 54.0. Sim: CIN 30.3, WAS 23.8. WAS wins 31.1%, CIN wins 68.9%. Median margin -6.4 for WAS.

| Team stat | CIN | WAS |
|---|---|---|
| Plays | 63 | 61 |
| Pass attempts / completions | 36 / 26 | 32 / 20 |
| Passing yards | 283 | 224 |
| Rush attempts / yards | 25 / 104 | 26 / 124 |
| Sacks taken | 2.5 | 2.9 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 2.1 / 1.2 | 1.4 / 1.2 |
| Field goals | 2.3 | 1.8 |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 25.2 | 283 pass yd, 2.1 TD, 0.7 INT; 2.6 rush, 11 yd |  |
| RB | Chase Brown | 17.5 | 13.0 car, 55 yd, 0.47 TD; 4.8 rec, 29 yd, 0.30 TD |  |
| RB | Samaje Perine | 7.8 | 6.8 car, 28 yd, 0.40 TD; 1.3 rec, 10 yd, 0.08 TD |  |
| RB | Tahj Brooks | 0.7 | 1.2 car, 5 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Ja'Marr Chase | 19.3 | 7.4 rec, 90 yd, 0.51 TD |  |
| WR | Tee Higgins | 14.8 | 5.3 rec, 69 yd, 0.44 TD |  |
| WR | Dohnte Meyers | 5.2 | 2.0 rec, 22 yd, 0.14 TD |  |
| WR | Mitchell Tinsley | 1.9 | 0.8 rec, 9 yd, 0.04 TD |  |
| TE | Mike Gesicki | 6.0 | 2.1 rec, 24 yd, 0.26 TD |  |
| TE | Drew Sample | 3.4 | 1.4 rec, 11 yd, 0.15 TD |  |
| K | Evan McPherson | 8.2 | 1.4 FG, 3.1 XP |  |
| DL | Boye Mafe | 5.1 | 1.7 solo, 1.2 ast, 0.74 sack, 0.11 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 4.2 | 1.7 solo, 1.2 ast, 0.49 sack, 0.12 PD, 0.00 INT |  |
| LB | Barrett Carter | 6.9 | 2.8 solo, 4.7 ast, 0.11 sack, 0.61 PD, 0.16 INT |  |
| LB | Demetrius Knight Jr. | 6.5 | 3.9 solo, 3.1 ast, 0.11 sack, 0.28 PD, 0.10 INT |  |
| LB | Joe Giles-Harris | 1.2 | 0.8 solo, 0.7 ast, 0.00 sack, 0.04 PD, 0.00 INT |  |
| DB | Jordan Battle | 7.3 | 4.3 solo, 1.9 ast, 0.00 sack, 0.85 PD, 0.26 INT |  |
| DB | Bryan Cook | 5.2 | 3.7 solo, 2.1 ast, 0.06 sack, 0.00 PD, 0.00 INT |  |
| DB | Daxton Hill | 4.1 | 2.9 solo, 0.9 ast, 0.00 sack, 0.62 PD, 0.00 INT |  |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 21.5 | 224 pass yd, 1.4 TD, 0.6 INT; 5.7 rush, 31 yd |  |
| RB | Rachaad White | 11.2 | 8.9 car, 41 yd, 0.47 TD; 2.0 rec, 16 yd, 0.13 TD |  |
| RB | Austin Ekeler | 7.2 | 7.1 car, 30 yd, 0.18 TD; 1.6 rec, 13 yd, 0.05 TD |  |
| RB | Robert Henry Jr. | 1.1 | 1.8 car, 8 yd, 0.04 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Stefon Diggs | 10.6 | 4.2 rec, 43 yd, 0.35 TD |  |
| WR | Antonio Williams | 7.2 | 3.0 rec, 33 yd, 0.17 TD |  |
| WR | Van Jefferson | 5.8 | 2.2 rec, 23 yd, 0.23 TD |  |
| WR | Treylon Burks | 5.6 | 2.0 rec, 28 yd, 0.13 TD |  |
| TE | Chig Okonkwo | 7.8 | 3.7 rec, 34 yd, 0.12 TD |  |
| TE | Ben Sinnott | 3.1 | 1.2 rec, 12 yd, 0.10 TD |  |
| K | Drew Stevens | 9.2 | 1.8 FG, 2.4 XP |  |
| DL | Shy Tuttle | 3.1 | 1.3 solo, 1.6 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Dorance Armstrong | 2.7 | 1.3 solo, 1.2 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 8.2 | 4.4 solo, 5.5 ast, 0.07 sack, 0.41 PD, 0.09 INT |  |
| LB | Frankie Luvu | 6.5 | 3.1 solo, 4.2 ast, 0.20 sack, 0.19 PD, 0.00 INT |  |
| LB | K'Lavon Chaisson | 4.2 | 1.6 solo, 1.2 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 6.1 | 3.8 solo, 2.8 ast, 0.00 sack, 0.55 PD, 0.05 INT |  |
| DB | Amik Robertson | 6.0 | 3.8 solo, 1.9 ast, 0.00 sack, 1.05 PD, 0.00 INT |  |
| DB | Nick Cross | 5.8 | 3.1 solo, 2.3 ast, 0.00 sack, 0.59 PD, 0.20 INT |  |

### IND @ HOU

Market: HOU -12.5, total 44.0. Sim: IND 16.0, HOU 28.3. HOU wins 83.1%, IND wins 16.9%. Median margin +12.6 for HOU.

| Team stat | IND | HOU |
|---|---|---|
| Plays | 62 | 63 |
| Pass attempts / completions | 34 / 21 | 33 / 21 |
| Passing yards | 208 | 262 |
| Rush attempts / yards | 25 / 104 | 28 / 110 |
| Sacks taken | 3.0 | 2.2 |
| Interceptions thrown | 0.9 | 0.5 |
| Passing / rushing TDs | 0.9 / 0.9 | 1.8 / 1.3 |
| Field goals | 1.2 | 2.1 |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 13.3 | 208 pass yd, 0.9 TD, 0.9 INT; 2.8 rush, 10 yd |  |
| RB | Jonathan Taylor | 17.1 | 13.4 car, 52 yd, 0.45 TD; 4.9 rec, 41 yd, 0.08 TD |  |
| RB | Seth McGowan | 4.8 | 5.0 car, 24 yd, 0.20 TD; 0.7 rec, 5 yd, 0.01 TD |  |
| RB | DJ Giddens | 0.9 | 1.7 car, 8 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Laquon Treadwell | 7.9 | 3.1 rec, 34 yd, 0.24 TD |  |
| WR | Ashton Dulin | 4.8 | 1.4 rec, 21 yd, 0.21 TD |  |
| WR | Deion Burks | 3.1 | 1.4 rec, 14 yd, 0.03 TD |  |
| WR | Anthony Gould | 1.8 | 1.1 rec, 12 yd, 0.02 TD | Questionable |
| TE | Tyler Warren | 13.9 | 7.0 rec, 52 yd, 0.24 TD |  |
| TE | Andrew Ogletree | 2.1 | 1.1 rec, 9 yd, 0.02 TD |  |
| K | Spencer Shrader | 8.8 | 1.9 FG, 1.6 XP |  |
| DL | Adetomiwa Adebawore | 4.0 | 1.4 solo, 1.4 ast, 0.40 sack, 0.39 PD, 0.00 INT |  |
| DL | Laiatu Latu | 3.4 | 1.3 solo, 0.8 ast, 0.39 sack, 0.18 PD, 0.00 INT |  |
| LB | CJ Allen | 5.3 | 1.9 solo, 3.9 ast, 0.37 sack, 0.38 PD, 0.00 INT |  |
| LB | Bryce Boettcher | 3.6 | 1.6 solo, 4.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Austin Ajiake | 2.3 | 1.1 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Justin Walley | 5.9 | 2.7 solo, 1.5 ast, 0.29 sack, 0.62 PD, 0.00 INT |  |
| DB | A.J. Haulcy | 4.1 | 3.0 solo, 1.8 ast, 0.00 sack, 0.18 PD, 0.00 INT |  |
| DB | Camryn Bynum | 3.6 | 2.0 solo, 1.6 ast, 0.00 sack, 0.46 PD, 0.12 INT |  |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 24.0 | 262 pass yd, 1.8 TD, 0.5 INT; 3.9 rush, 17 yd |  |
| RB | David Montgomery | 8.4 | 9.7 car, 36 yd, 0.54 TD; 0.6 rec, 6 yd, 0.06 TD |  |
| RB | Emari Demercado | 7.5 | 9.4 car, 37 yd, 0.24 TD; 1.2 rec, 10 yd, 0.05 TD |  |
| WR | Nico Collins | 13.7 | 5.0 rec, 62 yd, 0.42 TD |  |
| WR | Tank Dell | 9.3 | 1.0 car, 4 yd, 0.03 TD; 3.0 rec, 45 yd, 0.22 TD |  |
| WR | Xavier Hutchinson | 9.3 | 0.6 car, 3 yd, 0.01 TD; 3.3 rec, 38 yd, 0.30 TD |  |
| WR | Kayshon Boutte | 6.5 | 2.1 rec, 32 yd, 0.20 TD |  |
| TE | Dalton Schultz | 9.1 | 3.9 rec, 39 yd, 0.22 TD |  |
| TE | Foster Moreau | 3.8 | 1.3 rec, 11 yd, 0.23 TD |  |
| K | Ka'imi Fairbairn | 10.7 | 2.1 FG, 2.9 XP |  |
| DL | Will Anderson Jr. | 6.6 | 2.1 solo, 1.6 ast, 1.03 sack, 0.06 PD, 0.00 INT |  |
| DL | Jadeveon Clowney | 3.9 | 1.1 solo, 0.8 ast, 0.67 sack, 0.35 PD, 0.00 INT |  |
| LB | Jake Hansen | 4.6 | 2.3 solo, 3.1 ast, 0.08 sack, 0.19 PD, 0.10 INT |  |
| LB | Henry To'oTo'o | 4.5 | 2.1 solo, 3.3 ast, 0.07 sack, 0.18 PD, 0.00 INT |  |
| LB | Jacob Hummel | 1.1 | 1.0 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | M.J. Stewart | 7.9 | 4.0 solo, 4.9 ast, 0.39 sack, 0.23 PD, 0.00 INT |  |
| DB | Kamari Lassiter | 6.7 | 4.0 solo, 1.6 ast, 0.12 sack, 1.34 PD, 0.06 INT |  |
| DB | Calen Bullock | 5.5 | 2.8 solo, 1.6 ast, 0.00 sack, 0.90 PD, 0.26 INT |  |

### JAX @ NYG

Market: NYG +6.0, total 46.5. Sim: JAX 26.3, NYG 20.3. NYG wins 32.5%, JAX wins 67.5%. Median margin -6.1 for NYG.

| Team stat | JAX | NYG |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 31 / 20 | 32 / 20 |
| Passing yards | 250 | 226 |
| Rush attempts / yards | 28 / 115 | 28 / 112 |
| Sacks taken | 2.3 | 1.9 |
| Interceptions thrown | 0.7 | 0.9 |
| Passing / rushing TDs | 1.5 / 1.3 | 1.1 / 1.1 |
| Field goals | 2.0 | 1.5 |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 19.9 | 250 pass yd, 1.5 TD, 0.7 INT; 3.1 rush, 14 yd |  |
| RB | Bhayshul Tuten | 10.6 | 14.6 car, 58 yd, 0.67 TD; 1.7 rec, 18 yd, 0.16 TD | Questionable |
| RB | Chris Rodriguez Jr. | 4.5 | 6.4 car, 26 yd, 0.42 TD; 0.5 rec, 5 yd, 0.02 TD | Questionable |
| RB | Ameer Abdullah | 1.9 | 2.9 car, 12 yd, 0.07 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Parker Washington | 13.3 | 4.3 rec, 66 yd, 0.39 TD |  |
| WR | Jakobi Meyers | 6.7 | 3.6 rec, 41 yd, 0.19 TD | Questionable |
| WR | Brian Thomas Jr. | 4.9 | 1.9 rec, 21 yd, 0.15 TD |  |
| WR | Josh Cameron | 4.1 | 1.4 rec, 18 yd, 0.15 TD |  |
| TE | Brenton Strange | 8.1 | 3.4 rec, 34 yd, 0.20 TD |  |
| TE | Nate Boerkircher | 3.7 | 1.3 rec, 17 yd, 0.12 TD |  |
| K | Cam Little | 10.1 | 2.0 FG, 2.7 XP |  |
| DL | Josh Hines-Allen | 3.4 | 1.8 solo, 1.4 ast, 0.19 sack, 0.12 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.3 solo, 2.2 ast, 0.23 sack, 0.09 PD, 0.00 INT |  |
| LB | Foyesade Oluokun | 7.9 | 5.1 solo, 2.9 ast, 0.22 sack, 0.22 PD, 0.12 INT |  |
| LB | Ventrell Miller | 4.5 | 2.6 solo, 2.3 ast, 0.05 sack, 0.41 PD, 0.03 INT |  |
| LB | Branson Combs | 2.9 | 1.6 solo, 1.1 ast, 0.05 sack, 0.25 PD, 0.12 INT |  |
| DB | Jessie Bates | 7.2 | 4.1 solo, 2.4 ast, 0.00 sack, 0.40 PD, 0.14 INT |  |
| DB | Travis Hunter | 5.3 | 2.8 solo, 1.4 ast, 0.00 sack, 0.70 PD, 0.37 INT |  |
| DB | Montaric Brown | 3.9 | 2.7 solo, 0.5 ast, 0.00 sack, 0.49 PD, 0.16 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | J.J. McCarthy | 15.5 | 226 pass yd, 1.1 TD, 0.9 INT; 2.8 rush, 12 yd |  |
| RB | Cam Skattebo | 11.2 | 11.9 car, 49 yd, 0.56 TD; 1.5 rec, 14 yd, 0.04 TD |  |
| RB | Devin Singletary | 5.7 | 5.6 car, 20 yd, 0.23 TD; 1.2 rec, 9 yd, 0.06 TD |  |
| RB | Najee Harris | 2.0 | 3.8 car, 15 yd, 0.07 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Malik Nabers | 13.1 | 5.7 rec, 61 yd, 0.23 TD |  |
| WR | Malachi Fields | 6.1 | 2.4 rec, 32 yd, 0.10 TD |  |
| WR | Darnell Mooney | 3.8 | 1.6 rec, 16 yd, 0.06 TD |  |
| WR | Darius Slayton | 2.5 | 1.1 rec, 11 yd, 0.06 TD |  |
| TE | Isaiah Likely | 13.4 | 5.3 rec, 53 yd, 0.47 TD |  |
| TE | Theo Johnson | 2.5 | 1.0 rec, 11 yd, 0.07 TD |  |
| K | Dominic Zvada | 8.7 | 1.8 FG, 2.1 XP |  |
| DL | Shelby Harris | 2.6 | 1.2 solo, 1.3 ast, 0.17 sack, 0.20 PD, 0.00 INT |  |
| DL | DJ Reader | 2.5 | 1.6 solo, 1.0 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Arvell Reese | 10.6 | 5.9 solo, 3.6 ast, 0.59 sack, 0.35 PD, 0.09 INT |  |
| LB | Micah McFadden | 5.8 | 3.7 solo, 2.2 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| LB | Kayvon Thibodeaux | 2.9 | 2.0 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Jevon Holland | 5.2 | 2.5 solo, 1.8 ast, 0.00 sack, 0.50 PD, 0.32 INT |  |
| DB | Ar'Darius Washington | 4.7 | 3.0 solo, 1.0 ast, 0.00 sack, 0.65 PD, 0.18 INT |  |
| DB | Greg Newsome II | 4.7 | 3.1 solo, 1.1 ast, 0.00 sack, 0.71 PD, 0.10 INT |  |

### LV @ DEN

Market: DEN -10.0, total 40.5. Sim: LV 15.5, DEN 25.3. DEN wins 77.4%, LV wins 22.6%. Median margin +10.1 for DEN.

| Team stat | LV | DEN |
|---|---|---|
| Plays | 60 | 61 |
| Pass attempts / completions | 35 / 22 | 32 / 20 |
| Passing yards | 228 | 216 |
| Rush attempts / yards | 22 / 78 | 27 / 114 |
| Sacks taken | 2.8 | 2.5 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.0 / 0.7 | 1.6 / 1.1 |
| Field goals | 1.2 | 1.9 |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Fernando Mendoza | 15.7 | 228 pass yd, 1.0 TD, 0.8 INT; 2.3 rush, 9 yd |  |
| RB | Ashton Jeanty | 12.6 | 10.3 car, 34 yd, 0.23 TD; 3.9 rec, 32 yd, 0.13 TD |  |
| RB | Mike Washington Jr. | 4.4 | 7.7 car, 28 yd, 0.15 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| RB | Dylan Laube | 0.9 | 0.4 car, 2 yd, 0.06 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 7.7 | 3.0 rec, 36 yd, 0.16 TD |  |
| WR | Jalen Nailor | 3.8 | 1.8 rec, 14 yd, 0.09 TD |  |
| WR | Jack Bech | 2.9 | 1.4 rec, 12 yd, 0.06 TD |  |
| WR | Cody White | 2.7 | 1.0 rec, 12 yd, 0.08 TD |  |
| TE | Michael Mayer | 7.0 | 3.4 rec, 31 yd, 0.08 TD |  |
| TE | Brock Bowers | 4.7 | 4.9 rec, 53 yd, 0.28 TD | Questionable |
| K | Matt Gay | 6.4 | 1.9 FG, 1.6 XP | Questionable |
| DL | Maxx Crosby | 4.9 | 2.3 solo, 1.6 ast, 0.51 sack, 0.06 PD, 0.00 INT |  |
| DL | Kwity Paye | 2.4 | 0.8 solo, 1.8 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 8.9 | 4.3 solo, 6.3 ast, 0.08 sack, 0.18 PD, 0.11 INT |  |
| LB | Quay Walker | 6.6 | 3.1 solo, 5.0 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | Tommy Eichenberg | 2.7 | 1.6 solo, 1.9 ast, 0.00 sack, 0.17 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 7.0 | 4.3 solo, 3.0 ast, 0.06 sack, 0.19 PD, 0.11 INT |  |
| DB | Treydan Stukes | 5.0 | 2.8 solo, 2.3 ast, 0.00 sack, 0.42 PD, 0.20 INT |  |
| DB | Eric Stokes | 3.8 | 2.4 solo, 1.3 ast, 0.05 sack, 0.44 PD, 0.00 INT |  |

**DEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bo Nix | 20.5 | 216 pass yd, 1.6 TD, 0.5 INT; 4.9 rush, 21 yd |  |
| RB | Jonah Coleman | 11.6 | 9.5 car, 42 yd, 0.46 TD; 2.2 rec, 22 yd, 0.07 TD |  |
| RB | J.K. Dobbins | 8.3 | 10.9 car, 42 yd, 0.41 TD; 0.9 rec, 6 yd, 0.03 TD |  |
| WR | Courtland Sutton | 9.0 | 3.5 rec, 37 yd, 0.33 TD |  |
| WR | Jaylen Waddle | 6.7 | 3.4 rec, 37 yd, 0.29 TD | Questionable |
| WR | Pat Bryant | 6.1 | 2.1 rec, 24 yd, 0.26 TD |  |
| WR | Marvin Mims Jr. | 4.0 | 0.8 car, 4 yd, 0.02 TD; 1.7 rec, 15 yd, 0.06 TD |  |
| TE | Evan Engram | 4.8 | 2.1 rec, 20 yd, 0.11 TD |  |
| TE | Nate Adkins | 2.5 | 0.6 rec, 5 yd, 0.22 TD |  |
| K | Wil Lutz | 9.4 | 1.8 FG, 2.6 XP |  |
| DL | Malcolm Roach | 3.9 | 1.5 solo, 1.2 ast, 0.51 sack, 0.33 PD, 0.00 INT |  |
| DL | Zach Allen | 3.3 | 0.9 solo, 1.6 ast, 0.37 sack, 0.34 PD, 0.00 INT |  |
| LB | Alex Singleton | 8.7 | 4.9 solo, 5.6 ast, 0.25 sack, 0.24 PD, 0.00 INT |  |
| LB | Nik Bonitto | 4.3 | 1.4 solo, 0.6 ast, 0.58 sack, 0.04 PD, 0.00 INT |  |
| LB | Justin Strnad | 4.0 | 2.0 solo, 2.3 ast, 0.10 sack, 0.38 PD, 0.00 INT |  |
| DB | Ja'Quan McMillian | 6.0 | 2.7 solo, 1.2 ast, 0.37 sack, 0.82 PD, 0.16 INT |  |
| DB | Brandon Jones | 4.1 | 3.2 solo, 2.1 ast, 0.00 sack, 0.50 PD, 0.17 INT | Questionable |
| DB | Pat Surtain II | 4.0 | 3.0 solo, 1.2 ast, 0.00 sack, 0.31 PD, 0.04 INT |  |

### MIA @ BUF

Market: BUF -16.5, total 45.5. Sim: MIA 14.6, BUF 31.1. BUF wins 89.5%, MIA wins 10.5%. Median margin +16.6 for BUF.

| Team stat | MIA | BUF |
|---|---|---|
| Plays | 59 | 63 |
| Pass attempts / completions | 32 / 19 | 29 / 19 |
| Passing yards | 215 | 241 |
| Rush attempts / yards | 25 / 105 | 31 / 145 |
| Sacks taken | 2.1 | 2.0 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 0.8 / 0.8 | 1.6 / 1.8 |
| Field goals | 1.1 | 2.3 |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kyle McCord | 15.1 | 215 pass yd, 0.8 TD, 0.8 INT; 2.2 rush, 10 yd |  |
| RB | Ollie Gordon II | 10.4 | 15.1 car, 64 yd, 0.30 TD; 1.3 rec, 10 yd, 0.02 TD |  |
| RB | Jaylen Wright | 3.6 | 4.9 car, 19 yd, 0.08 TD; 0.6 rec, 6 yd, 0.01 TD |  |
| RB | Kaytron Allen | 1.6 | 0.9 car, 4 yd, 0.01 TD; 0.5 rec, 6 yd, 0.01 TD |  |
| WR | Malik Washington | 8.7 | 1.0 car, 5 yd, 0.02 TD; 3.8 rec, 36 yd, 0.13 TD |  |
| WR | Caleb Douglas | 6.9 | 3.6 rec, 46 yd, 0.18 TD | Questionable |
| WR | Kevin Coleman Jr. | 4.1 | 1.6 rec, 15 yd, 0.15 TD |  |
| WR | Chris Bell | 3.0 | 1.8 rec, 18 yd, 0.04 TD | Questionable |
| TE | Greg Dulcich | 6.5 | 3.1 rec, 31 yd, 0.07 TD |  |
| TE | Will Kacmarek | 1.6 | 0.8 rec, 7 yd, 0.02 TD |  |
| DL | Rodney McGraw | 1.2 | 0.4 solo, 1.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DL | Malik Herring | 1.2 | 0.5 solo, 0.7 ast, 0.13 sack, 0.00 PD, 0.00 INT |  |
| LB | Jordyn Brooks | 7.7 | 4.4 solo, 5.2 ast, 0.03 sack, 0.29 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 6.8 | 3.7 solo, 4.3 ast, 0.13 sack, 0.07 PD, 0.07 INT |  |
| LB | Joshua Uche | 4.5 | 2.2 solo, 2.0 ast, 0.33 sack, 0.14 PD, 0.00 INT |  |
| DB | Chris Johnson | 6.0 | 2.4 solo, 2.2 ast, 0.00 sack, 0.40 PD, 0.28 INT |  |
| DB | Michael Taaffe | 5.9 | 3.0 solo, 2.8 ast, 0.00 sack, 0.31 PD, 0.31 INT |  |
| DB | Jason Marshall Jr. | 2.3 | 1.4 solo, 1.2 ast, 0.00 sack, 0.19 PD, 0.04 INT |  |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.0 | 241 pass yd, 1.6 TD, 0.7 INT; 6.1 rush, 27 yd |  |
| RB | James Cook | 16.6 | 17.7 car, 85 yd, 0.91 TD; 1.2 rec, 12 yd, 0.07 TD |  |
| RB | Ty Johnson | 5.7 | 1.7 car, 7 yd, 0.08 TD; 2.0 rec, 21 yd, 0.09 TD |  |
| RB | Ray Davis | 2.1 | 2.6 car, 12 yd, 0.07 TD; 0.5 rec, 5 yd, 0.04 TD | Questionable |
| WR | DJ Moore | 9.9 | 0.6 car, 3 yd, 0.02 TD; 3.0 rec, 43 yd, 0.36 TD |  |
| WR | Khalil Shakir | 9.1 | 3.6 rec, 42 yd, 0.20 TD |  |
| WR | Keon Coleman | 6.6 | 2.4 rec, 28 yd, 0.23 TD |  |
| WR | Gabe Davis | 1.2 | 0.6 rec, 6 yd, 0.07 TD | Questionable |
| TE | Dawson Knox | 4.5 | 1.9 rec, 16 yd, 0.16 TD |  |
| TE | Dalton Kincaid | 3.3 | 3.1 rec, 41 yd, 0.21 TD | Questionable |
| K | Tyler Bass | 10.8 | 2.0 FG, 3.2 XP |  |
| DL | Deone Walker | 2.5 | 1.0 solo, 1.9 ast, 0.05 sack, 0.41 PD, 0.00 INT |  |
| DL | Landon Jackson | 1.9 | 0.7 solo, 1.2 ast, 0.15 sack, 0.09 PD, 0.00 INT |  |
| LB | Terrel Bernard | 5.3 | 2.8 solo, 3.4 ast, 0.00 sack, 0.32 PD, 0.13 INT |  |
| LB | Greg Rousseau | 5.2 | 1.3 solo, 0.8 ast, 0.71 sack, 0.73 PD, 0.00 INT |  |
| LB | TJ Parker | 4.0 | 1.3 solo, 1.9 ast, 0.53 sack, 0.00 PD, 0.00 INT |  |
| DB | Amani Hooker | 4.6 | 3.8 solo, 2.8 ast, 0.00 sack, 0.94 PD, 0.00 INT | Questionable |
| DB | Davison Igbinosun | 4.6 | 1.7 solo, 1.5 ast, 0.00 sack, 1.27 PD, 0.29 INT |  |
| DB | Cole Bishop | 3.7 | 3.2 solo, 2.1 ast, 0.11 sack, 0.19 PD, 0.00 INT | Questionable |

### MIN @ SF

Market: SF -3.0, total 46.5. Sim: MIN 21.8, SF 24.8. SF wins 58.7%, MIN wins 41.3%. Median margin +2.9 for SF.

| Team stat | MIN | SF |
|---|---|---|
| Plays | 59 | 61 |
| Pass attempts / completions | 33 / 20 | 30 / 21 |
| Passing yards | 217 | 224 |
| Rush attempts / yards | 24 / 98 | 28 / 128 |
| Sacks taken | 1.9 | 3.5 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.6 / 0.8 | 1.4 / 1.2 |
| Field goals | 1.7 | 1.9 |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 17.7 | 217 pass yd, 1.6 TD, 0.7 INT; 2.2 rush, 9 yd |  |
| RB | Aaron Jones | 11.6 | 11.2 car, 44 yd, 0.52 TD; 2.2 rec, 16 yd, 0.07 TD |  |
| RB | Jordan Mason | 6.1 | 8.3 car, 34 yd, 0.24 TD; 0.6 rec, 6 yd, 0.03 TD |  |
| RB | DeeJay Dallas | 1.0 | 0.3 car, 1 yd, 0.00 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Justin Jefferson | 15.4 | 6.3 rec, 64 yd, 0.45 TD |  |
| WR | Myles Price | 3.8 | 1.4 rec, 13 yd, 0.16 TD |  |
| WR | Tai Felton | 3.1 | 1.3 rec, 14 yd, 0.05 TD |  |
| WR | Jauan Jennings | 2.4 | 1.1 rec, 11 yd, 0.04 TD |  |
| TE | T.J. Hockenson | 8.1 | 4.4 rec, 41 yd, 0.39 TD | Questionable |
| TE | Gavin Bartholomew | 5.8 | 2.2 rec, 21 yd, 0.26 TD |  |
| K | Will Reichard | 10.4 | 2.2 FG, 2.3 XP |  |
| DL | Jalen Redmond | 3.9 | 1.7 solo, 1.4 ast, 0.30 sack, 0.42 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 3.1 | 1.3 solo, 1.3 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| LB | Blake Cashman | 6.9 | 4.6 solo, 4.8 ast, 0.43 sack, 0.75 PD, 0.00 INT | Questionable |
| LB | Eric Wilson | 6.4 | 3.3 solo, 3.1 ast, 0.44 sack, 0.06 PD, 0.00 INT |  |
| LB | Dallas Turner | 5.6 | 1.7 solo, 1.2 ast, 0.73 sack, 0.39 PD, 0.00 INT |  |
| DB | Byron Murphy | 5.6 | 3.0 solo, 1.1 ast, 0.00 sack, 0.66 PD, 0.41 INT |  |
| DB | Josh Metellus | 5.4 | 3.4 solo, 3.3 ast, 0.03 sack, 0.32 PD, 0.00 INT |  |
| DB | James Pierre | 4.2 | 2.9 solo, 0.4 ast, 0.00 sack, 0.50 PD, 0.20 INT |  |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 19.0 | 224 pass yd, 1.4 TD, 0.7 INT; 3.7 rush, 18 yd |  |
| RB | Christian McCaffrey | 16.5 | 12.0 car, 53 yd, 0.61 TD; 3.2 rec, 31 yd, 0.23 TD |  |
| RB | Kaelon Black | 6.1 | 7.7 car, 36 yd, 0.28 TD; 0.5 rec, 4 yd, 0.02 TD |  |
| RB | Kyle Juszczyk | 2.1 | 0.1 car, 1 yd, 0.00 TD; 0.8 rec, 7 yd, 0.10 TD |  |
| WR | Keenan Allen | 8.1 | 3.7 rec, 36 yd, 0.14 TD |  |
| WR | Deebo Samuel Sr. | 6.0 | 1.5 car, 9 yd, 0.11 TD; 1.7 rec, 17 yd, 0.19 TD |  |
| WR | Jordan Watkins | 4.6 | 1.6 rec, 23 yd, 0.11 TD |  |
| WR | Mike Evans | 2.7 | 2.6 rec, 31 yd, 0.18 TD | Questionable |
| TE | George Kittle | 9.3 | 3.9 rec, 39 yd, 0.26 TD |  |
| K | Eddy Pineiro | 7.3 | 1.3 FG, 2.5 XP |  |
| DL | Mykel Williams | 2.3 | 0.8 solo, 1.1 ast, 0.33 sack, 0.00 PD, 0.00 INT |  |
| DL | Osa Odighizuwa | 2.1 | 0.7 solo, 1.5 ast, 0.21 sack, 0.08 PD, 0.00 INT |  |
| LB | Fred Warner | 7.8 | 3.8 solo, 5.1 ast, 0.03 sack, 0.24 PD, 0.00 INT |  |
| LB | Jaden Dugger | 5.5 | 3.2 solo, 1.0 ast, 0.10 sack, 0.15 PD, 0.15 INT |  |
| LB | Dre Greenlaw | 2.5 | 3.6 solo, 3.8 ast, 0.09 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | Malik Mustapha | 4.9 | 2.4 solo, 1.6 ast, 0.00 sack, 0.71 PD, 0.27 INT |  |
| DB | Deommodore Lenoir | 3.8 | 2.5 solo, 1.4 ast, 0.00 sack, 0.63 PD, 0.00 INT |  |
| DB | Renardo Green | 3.8 | 2.7 solo, 1.2 ast, 0.00 sack, 0.70 PD, 0.35 INT | Questionable |

### NO @ CHI

Market: CHI -11.5, total 48.5. Sim: NO 18.6, CHI 30.1. CHI wins 80.5%, NO wins 19.5%. Median margin +11.5 for CHI.

| Team stat | NO | CHI |
|---|---|---|
| Plays | 64 | 66 |
| Pass attempts / completions | 36 / 24 | 32 / 21 |
| Passing yards | 255 | 229 |
| Rush attempts / yards | 25 / 98 | 31 / 127 |
| Sacks taken | 3.0 | 2.8 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 1.1 / 0.9 | 1.7 / 1.6 |
| Field goals | 1.4 | 2.2 |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 18.3 | 255 pass yd, 1.1 TD, 0.8 INT; 4.3 rush, 19 yd |  |
| RB | Alvin Kamara | 9.3 | 5.2 car, 19 yd, 0.29 TD; 2.7 rec, 20 yd, 0.17 TD |  |
| RB | Travis Etienne | 5.4 | 5.2 car, 20 yd, 0.10 TD; 1.5 rec, 12 yd, 0.04 TD |  |
| RB | Audric Estime | 5.2 | 6.3 car, 24 yd, 0.23 TD; 0.7 rec, 7 yd, 0.02 TD |  |
| WR | Chris Olave | 11.9 | 4.8 rec, 58 yd, 0.22 TD |  |
| WR | Jordyn Tyson | 9.0 | 6.1 rec, 51 yd, 0.13 TD | Questionable |
| WR | Devaughn Vele | 6.5 | 2.8 rec, 29 yd, 0.15 TD |  |
| WR | Bryce Lance | 2.1 | 0.9 rec, 8 yd, 0.07 TD |  |
| TE | Juwan Johnson | 6.2 | 2.5 rec, 28 yd, 0.16 TD |  |
| TE | Noah Fant | 2.5 | 1.0 rec, 9 yd, 0.10 TD |  |
| DL | Carl Granderson | 6.7 | 2.0 solo, 2.7 ast, 1.00 sack, 0.21 PD, 0.05 INT |  |
| DL | Chase Young | 5.5 | 1.3 solo, 1.4 ast, 0.86 sack, 0.39 PD, 0.00 INT |  |
| LB | Kaden Elliss | 8.0 | 4.4 solo, 4.2 ast, 0.39 sack, 0.29 PD, 0.00 INT |  |
| LB | Danny Stutsman | 4.2 | 2.9 solo, 2.5 ast, 0.00 sack, 0.10 PD, 0.00 INT |  |
| LB | Cameron Jordan | 2.6 | 1.4 solo, 1.0 ast, 0.18 sack, 0.03 PD, 0.00 INT |  |
| DB | Jonas Sanker | 5.3 | 3.4 solo, 2.1 ast, 0.00 sack, 0.57 PD, 0.03 INT |  |
| DB | Julian Blackmon | 4.6 | 2.7 solo, 2.3 ast, 0.00 sack, 0.18 PD, 0.19 INT |  |
| DB | Kool-Aid McKinstry | 4.2 | 2.5 solo, 1.8 ast, 0.00 sack, 0.77 PD, 0.00 INT |  |

**CHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Caleb Williams | 20.0 | 229 pass yd, 1.7 TD, 0.7 INT; 3.4 rush, 14 yd |  |
| RB | D'Andre Swift | 14.1 | 14.1 car, 53 yd, 0.81 TD; 2.2 rec, 15 yd, 0.07 TD |  |
| RB | Kyle Monangai | 6.8 | 7.1 car, 32 yd, 0.32 TD; 0.8 rec, 7 yd, 0.03 TD |  |
| RB | Roschon Johnson | 4.1 | 3.2 car, 13 yd, 0.13 TD; 0.9 rec, 9 yd, 0.03 TD |  |
| WR | Luther Burden III | 14.5 | 0.6 car, 3 yd, 0.02 TD; 5.2 rec, 60 yd, 0.50 TD |  |
| WR | Rome Odunze | 9.7 | 3.5 rec, 46 yd, 0.27 TD |  |
| WR | Kalif Raymond | 6.2 | 2.8 rec, 23 yd, 0.16 TD |  |
| WR | Zavion Thomas | 1.9 | 0.9 rec, 8 yd, 0.03 TD |  |
| TE | Colston Loveland | 11.1 | 4.6 rec, 42 yd, 0.39 TD |  |
| TE | Sam Roush | 1.4 | 0.6 rec, 6 yd, 0.02 TD |  |
| K | Cairo Santos | 9.4 | 1.7 FG, 3.1 XP |  |
| DL | Jeffery Simmons | 6.4 | 3.1 solo, 2.0 ast, 1.11 sack, 1.08 PD, 0.00 INT | Questionable |
| DL | Austin Booker | 5.3 | 2.3 solo, 1.1 ast, 0.62 sack, 0.27 PD, 0.00 INT |  |
| LB | Devin Bush | 6.6 | 3.5 solo, 2.9 ast, 0.27 sack, 0.46 PD, 0.00 INT |  |
| LB | T.J. Edwards | 4.1 | 2.3 solo, 1.3 ast, 0.02 sack, 0.35 PD, 0.13 INT |  |
| LB | D'Marco Jackson | 2.5 | 1.1 solo, 1.3 ast, 0.03 sack, 0.19 PD, 0.15 INT |  |
| DB | Dillon Thieneman | 6.0 | 3.2 solo, 2.8 ast, 0.20 sack, 0.48 PD, 0.09 INT |  |
| DB | Jaylon Johnson | 4.9 | 2.5 solo, 0.8 ast, 0.00 sack, 0.45 PD, 0.20 INT |  |
| DB | Cam Lewis | 4.6 | 2.9 solo, 1.3 ast, 0.00 sack, 0.38 PD, 0.20 INT |  |

### NYJ @ LAC

Market: LAC -3.0, total 42.0. Sim: NYJ 19.6, LAC 22.6. LAC wins 59.0%, NYJ wins 41.0%. Median margin +3.2 for LAC.

| Team stat | NYJ | LAC |
|---|---|---|
| Plays | 60 | 63 |
| Pass attempts / completions | 33 / 21 | 33 / 20 |
| Passing yards | 249 | 235 |
| Rush attempts / yards | 25 / 105 | 28 / 121 |
| Sacks taken | 2.2 | 2.2 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 1.3 / 0.8 | 1.4 / 1.1 |
| Field goals | 1.5 | 1.7 |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Geno Smith | 12.9 | 187 pass yd, 1.0 TD, 0.6 INT; 1.4 rush, 6 yd | Questionable |
| RB | Braelon Allen | 10.0 | 10.1 car, 46 yd, 0.39 TD; 1.7 rec, 12 yd, 0.05 TD |  |
| RB | Breece Hall | 8.2 | 7.9 car, 30 yd, 0.22 TD; 1.8 rec, 19 yd, 0.04 TD |  |
| RB | Isaiah Davis | 2.0 | 1.5 car, 6 yd, 0.05 TD; 0.5 rec, 6 yd, 0.01 TD |  |
| WR | Garrett Wilson | 11.3 | 4.5 rec, 53 yd, 0.25 TD |  |
| WR | Adonai Mitchell | 6.8 | 2.3 rec, 33 yd, 0.19 TD |  |
| WR | Omar Cooper Jr. | 3.3 | 3.1 rec, 38 yd, 0.23 TD | Questionable |
| WR | Isaiah Williams | 1.7 | 1.7 rec, 16 yd, 0.13 TD | Questionable |
| TE | Mason Taylor | 5.5 | 2.4 rec, 20 yd, 0.19 TD |  |
| TE | Kenyon Sadiq | 4.4 | 1.8 rec, 19 yd, 0.09 TD |  |
| K | Jason Sanders | 10.6 | 2.3 FG, 2.0 XP |  |
| DL | Will McDonald IV | 3.4 | 0.9 solo, 1.0 ast, 0.46 sack, 0.00 PD, 0.00 INT |  |
| DL | Darrell Jackson Jr. | 2.8 | 1.3 solo, 2.2 ast, 0.09 sack, 0.17 PD, 0.00 INT |  |
| LB | David Bailey | 7.5 | 2.6 solo, 2.0 ast, 0.76 sack, 0.44 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.5 | 4.2 solo, 4.7 ast, 0.03 sack, 0.38 PD, 0.00 INT |  |
| LB | Demario Davis | 6.2 | 3.5 solo, 3.2 ast, 0.14 sack, 0.36 PD, 0.00 INT |  |
| DB | Dane Belton | 7.1 | 4.2 solo, 4.3 ast, 0.09 sack, 0.52 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 6.3 | 3.6 solo, 3.8 ast, 0.00 sack, 0.35 PD, 0.09 INT |  |
| DB | Azareye'h Thomas | 4.4 | 2.0 solo, 2.7 ast, 0.00 sack, 0.59 PD, 0.16 INT |  |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 19.8 | 235 pass yd, 1.4 TD, 0.7 INT; 4.4 rush, 23 yd |  |
| RB | Omarion Hampton | 11.3 | 12.8 car, 52 yd, 0.56 TD; 1.5 rec, 10 yd, 0.07 TD |  |
| RB | Keaton Mitchell | 6.8 | 4.8 car, 20 yd, 0.10 TD; 2.0 rec, 15 yd, 0.13 TD |  |
| RB | Kimani Vidal | 6.3 | 4.9 car, 21 yd, 0.17 TD; 1.5 rec, 12 yd, 0.11 TD |  |
| WR | Tre Harris | 7.5 | 3.1 rec, 38 yd, 0.11 TD |  |
| WR | Quentin Johnston | 6.6 | 2.0 rec, 31 yd, 0.23 TD |  |
| WR | Ladd McConkey | 4.2 | 2.0 rec, 27 yd, 0.16 TD | Questionable |
| WR | KeAndre Lambert-Smith | 3.4 | 1.3 rec, 16 yd, 0.09 TD |  |
| TE | Oronde Gadsden II | 5.3 | 2.3 rec, 21 yd, 0.16 TD |  |
| TE | Charlie Kolar | 2.0 | 2.2 rec, 22 yd, 0.08 TD | Questionable |
| K | Cameron Dicker | 9.9 | 2.0 FG, 2.3 XP |  |
| DL | Dalvin Tomlinson | 3.3 | 1.2 solo, 1.1 ast, 0.51 sack, 0.00 PD, 0.00 INT |  |
| DL | Teair Tart | 1.8 | 1.0 solo, 1.1 ast, 0.00 sack, 0.19 PD, 0.00 INT |  |
| LB | Del'Shawn Phillips | 4.4 | 2.2 solo, 3.0 ast, 0.04 sack, 0.14 PD, 0.14 INT |  |
| LB | Tuli Tuipulotu | 4.3 | 1.5 solo, 1.5 ast, 0.35 sack, 0.23 PD, 0.08 INT |  |
| LB | Troy Dye | 3.4 | 1.7 solo, 0.9 ast, 0.13 sack, 0.20 PD, 0.00 INT |  |
| DB | Tarheeb Still | 4.4 | 2.5 solo, 1.3 ast, 0.00 sack, 0.51 PD, 0.11 INT |  |
| DB | Tony Jefferson | 4.4 | 2.7 solo, 2.1 ast, 0.07 sack, 0.17 PD, 0.03 INT |  |
| DB | Cam Hart | 4.3 | 2.1 solo, 1.5 ast, 0.00 sack, 0.81 PD, 0.18 INT |  |

### PIT @ PHI

Market: PHI +4.5, total 37.5. Sim: PIT 21.2, PHI 16.8. PHI wins 37.0%, PIT wins 63.0%. Median margin -4.5 for PHI.

| Team stat | PIT | PHI |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 34 / 21 | 32 / 20 |
| Passing yards | 211 | 205 |
| Rush attempts / yards | 27 / 123 | 27 / 103 |
| Sacks taken | 2.6 | 2.7 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.9 | 0.8 / 1.0 |
| Field goals | 1.6 | 1.3 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 16.3 | 211 pass yd, 1.4 TD, 0.6 INT; 1.4 rush, 6 yd |  |
| RB | Jaylen Warren | 16.4 | 13.6 car, 68 yd, 0.43 TD; 3.3 rec, 29 yd, 0.16 TD |  |
| RB | Rico Dowdle | 8.7 | 7.3 car, 31 yd, 0.28 TD; 2.2 rec, 15 yd, 0.06 TD |  |
| RB | Lew Nichols III | 1.2 | 1.6 car, 8 yd, 0.03 TD; 0.2 rec, 1 yd, 0.00 TD |  |
| WR | DK Metcalf | 10.5 | 4.1 rec, 46 yd, 0.29 TD |  |
| WR | Germie Bernard | 9.1 | 4.3 rec, 35 yd, 0.19 TD |  |
| WR | Brandon Smith | 2.7 | 1.3 rec, 12 yd, 0.04 TD |  |
| WR | Ben Skowronek | 1.3 | 0.5 rec, 4 yd, 0.06 TD |  |
| TE | Pat Freiermuth | 8.4 | 3.0 rec, 29 yd, 0.31 TD |  |
| TE | Darnell Washington | 6.2 | 2.4 rec, 26 yd, 0.22 TD |  |
| K | Chris Boswell | 9.3 | 1.9 FG, 2.2 XP |  |
| DL | Cameron Heyward | 4.2 | 1.6 solo, 1.9 ast, 0.33 sack, 0.45 PD, 0.00 INT |  |
| DL | Keeanu Benton | 2.9 | 1.1 solo, 1.5 ast, 0.10 sack, 0.43 PD, 0.00 INT |  |
| LB | Payton Wilson | 7.9 | 4.7 solo, 4.4 ast, 0.10 sack, 0.26 PD, 0.10 INT |  |
| LB | Patrick Queen | 5.9 | 3.3 solo, 5.1 ast, 0.44 sack, 0.36 PD, 0.06 INT | Questionable |
| LB | T.J. Watt | 5.4 | 1.5 solo, 0.7 ast, 0.70 sack, 0.50 PD, 0.11 INT |  |
| DB | Jalen Ramsey | 5.5 | 3.0 solo, 2.3 ast, 0.22 sack, 0.21 PD, 0.00 INT |  |
| DB | Jaquan Brisker | 5.4 | 2.9 solo, 4.0 ast, 0.00 sack, 0.27 PD, 0.06 INT |  |
| DB | Jamel Dean | 5.3 | 2.6 solo, 1.2 ast, 0.00 sack, 1.12 PD, 0.13 INT |  |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Milton III | 16.0 | 205 pass yd, 0.8 TD, 0.7 INT; 7.5 rush, 33 yd |  |
| RB | Saquon Barkley | 7.2 | 8.5 car, 33 yd, 0.43 TD; 0.7 rec, 6 yd, 0.02 TD |  |
| RB | Dameon Pierce | 5.5 | 9.0 car, 31 yd, 0.37 TD; 1.2 rec, 8 yd, 0.03 TD | Questionable |
| WR | Makai Lemon | 7.7 | 3.8 rec, 32 yd, 0.13 TD |  |
| WR | DeVonta Smith | 5.5 | 3.1 rec, 32 yd, 0.16 TD | Questionable |
| WR | Darius Cooper | 4.2 | 1.5 rec, 18 yd, 0.15 TD |  |
| WR | Dontayvion Wicks | 3.6 | 2.0 rec, 23 yd, 0.07 TD | Questionable |
| TE | Dallas Goedert | 7.4 | 3.4 rec, 30 yd, 0.15 TD |  |
| TE | Eli Stowers | 2.0 | 0.9 rec, 10 yd, 0.02 TD |  |
| K | Jake Elliott | 6.3 | 1.2 FG, 1.7 XP |  |
| DL | Jalen Carter | 5.1 | 1.1 solo, 1.6 ast, 0.63 sack, 0.40 PD, 0.00 INT |  |
| DL | Byron Young | 2.1 | 0.8 solo, 1.8 ast, 0.10 sack, 0.00 PD, 0.00 INT |  |
| LB | Jeremiah Trotter Jr. | 6.0 | 3.9 solo, 3.0 ast, 0.06 sack, 0.09 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 4.7 | 3.0 solo, 2.5 ast, 0.06 sack, 0.06 PD, 0.00 INT |  |
| LB | Jalyx Hunt | 3.1 | 1.8 solo, 0.5 ast, 0.16 sack, 0.22 PD, 0.05 INT |  |
| DB | Andrew Mukuba | 5.8 | 3.9 solo, 2.2 ast, 0.00 sack, 0.25 PD, 0.09 INT |  |
| DB | Cooper DeJean | 5.3 | 3.3 solo, 2.1 ast, 0.00 sack, 0.61 PD, 0.12 INT |  |
| DB | Riq Woolen | 4.7 | 3.1 solo, 0.7 ast, 0.00 sack, 1.02 PD, 0.00 INT |  |

### TB @ DET

Market: DET -7.0, total 44.0. Sim: TB 18.6, DET 25.5. DET wins 70.2%, TB wins 29.8%. Median margin +7.0 for DET.

| Team stat | TB | DET |
|---|---|---|
| Plays | 63 | 64 |
| Pass attempts / completions | 33 / 20 | 34 / 22 |
| Passing yards | 209 | 263 |
| Rush attempts / yards | 28 / 134 | 29 / 124 |
| Sacks taken | 2.8 | 2.1 |
| Interceptions thrown | 0.9 | 0.8 |
| Passing / rushing TDs | 1.1 / 0.9 | 1.6 / 1.2 |
| Field goals | 1.4 | 1.9 |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jalon Daniels | 9.7 | 125 pass yd, 0.7 TD, 0.5 INT; 2.5 rush, 12 yd |  |
| RB | Bucky Irving | 15.1 | 14.4 car, 69 yd, 0.50 TD; 2.7 rec, 18 yd, 0.15 TD |  |
| RB | Kenny Gainwell | 8.4 | 6.0 car, 30 yd, 0.10 TD; 2.0 rec, 20 yd, 0.14 TD |  |
| RB | Sean Tucker | 1.6 | 1.8 car, 8 yd, 0.13 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Emeka Egbuka | 9.7 | 4.1 rec, 38 yd, 0.25 TD |  |
| WR | Chris Godwin Jr. | 8.6 | 4.1 rec, 36 yd, 0.15 TD |  |
| WR | Tez Johnson | 5.3 | 1.7 rec, 27 yd, 0.14 TD |  |
| WR | Ted Hurst III | 4.7 | 1.7 rec, 21 yd, 0.15 TD |  |
| TE | Cade Otton | 7.2 | 3.4 rec, 31 yd, 0.13 TD |  |
| K | Chase McLaughlin | 9.9 | 2.1 FG, 1.9 XP |  |
| DL | A'Shawn Robinson | 2.7 | 0.5 solo, 2.0 ast, 0.07 sack, 0.35 PD, 0.21 INT |  |
| DL | Vita Vea | 2.2 | 1.0 solo, 1.2 ast, 0.14 sack, 0.17 PD, 0.00 INT |  |
| LB | Josiah Trotter | 7.8 | 4.3 solo, 4.7 ast, 0.07 sack, 0.34 PD, 0.07 INT |  |
| LB | Alex Anzalone | 6.0 | 2.1 solo, 2.5 ast, 0.08 sack, 0.59 PD, 0.59 INT |  |
| LB | David Walker | 3.8 | 1.9 solo, 1.2 ast, 0.44 sack, 0.00 PD, 0.00 INT |  |
| DB | Jacob Parrish | 6.7 | 3.8 solo, 0.9 ast, 0.00 sack, 1.54 PD, 0.25 INT |  |
| DB | Zyon McCollum | 6.2 | 2.7 solo, 0.8 ast, 0.00 sack, 1.15 PD, 0.59 INT |  |
| DB | Tykee Smith | 5.3 | 2.7 solo, 2.7 ast, 0.00 sack, 0.34 PD, 0.26 INT |  |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 19.3 | 263 pass yd, 1.6 TD, 0.8 INT; 1.9 rush, 7 yd |  |
| RB | Jahmyr Gibbs | 23.1 | 19.4 car, 87 yd, 0.93 TD; 4.1 rec, 38 yd, 0.21 TD |  |
| RB | Sione Vaki | 2.5 | 3.5 car, 15 yd, 0.08 TD; 0.6 rec, 6 yd, 0.02 TD | Questionable |
| WR | Amon-Ra St. Brown | 17.1 | 6.7 rec, 75 yd, 0.48 TD |  |
| WR | Jameson Williams | 10.6 | 3.6 rec, 50 yd, 0.34 TD |  |
| WR | Isaac TeSlaa | 4.8 | 1.6 rec, 21 yd, 0.18 TD |  |
| TE | Sam LaPorta | 8.6 | 3.4 rec, 37 yd, 0.24 TD |  |
| TE | Brock Wright | 1.6 | 0.8 rec, 7 yd, 0.03 TD |  |
| K | Jake Bates | 9.4 | 1.8 FG, 2.6 XP |  |
| DL | DJ Wonnum | 4.2 | 1.4 solo, 1.0 ast, 0.69 sack, 0.07 PD, 0.00 INT |  |
| DL | Derrick Moore | 4.1 | 1.3 solo, 0.5 ast, 0.83 sack, 0.00 PD, 0.00 INT |  |
| LB | Derrick Barnes | 4.6 | 2.8 solo, 1.7 ast, 0.20 sack, 0.17 PD, 0.08 INT |  |
| LB | K.J. Britt | 4.6 | 4.1 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Malcolm Rodriguez | 2.9 | 1.5 solo, 2.4 ast, 0.04 sack, 0.13 PD, 0.00 INT |  |
| DB | Chuck Clark | 6.3 | 3.5 solo, 2.0 ast, 0.08 sack, 0.33 PD, 0.21 INT |  |
| DB | Roger McCreary | 6.1 | 3.4 solo, 1.3 ast, 0.06 sack, 1.23 PD, 0.18 INT |  |
| DB | D.J. Reed | 3.9 | 3.2 solo, 1.4 ast, 0.00 sack, 0.86 PD, 0.17 INT | Questionable |

### TEN @ DAL

Market: DAL -8.0, total 55.0. Sim: TEN 23.6, DAL 31.4. DAL wins 72.7%, TEN wins 27.3%. Median margin +8.0 for DAL.

| Team stat | TEN | DAL |
|---|---|---|
| Plays | 60 | 66 |
| Pass attempts / completions | 35 / 22 | 35 / 22 |
| Passing yards | 245 | 274 |
| Rush attempts / yards | 23 / 110 | 28 / 115 |
| Sacks taken | 2.4 | 2.5 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.6 / 0.9 | 2.0 / 1.4 |
| Field goals | 1.8 | 2.3 |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 20.6 | 245 pass yd, 1.6 TD, 0.6 INT; 2.8 rush, 15 yd |  |
| RB | Tony Pollard | 17.6 | 15.1 car, 72 yd, 0.66 TD; 3.0 rec, 23 yd, 0.23 TD |  |
| RB | Tyjae Spears | 2.6 | 3.2 car, 15 yd, 0.09 TD; 2.5 rec, 16 yd, 0.07 TD | Questionable |
| RB | Nicholas Singleton | 0.6 | 1.1 car, 5 yd, 0.02 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Carnell Tate | 9.7 | 5.0 rec, 58 yd, 0.37 TD | Questionable |
| WR | Elic Ayomanor | 8.4 | 3.0 rec, 40 yd, 0.24 TD |  |
| WR | Chimere Dike | 6.2 | 2.3 rec, 24 yd, 0.24 TD |  |
| WR | Calvin Ridley | 2.9 | 1.2 rec, 14 yd, 0.05 TD |  |
| TE | Gunnar Helm | 6.3 | 2.9 rec, 27 yd, 0.12 TD |  |
| TE | Daniel Bellinger | 4.5 | 1.6 rec, 14 yd, 0.24 TD |  |
| K | Joey Slye | 9.0 | 1.8 FG, 2.4 XP |  |
| DL | Jacob Martin | 4.9 | 1.4 solo, 0.4 ast, 1.01 sack, 0.23 PD, 0.00 INT |  |
| DL | Jermaine Johnson II | 3.3 | 1.8 solo, 0.9 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| LB | Cedric Gray | 6.1 | 3.7 solo, 2.9 ast, 0.05 sack, 0.32 PD, 0.16 INT |  |
| LB | Anthony Hill Jr. | 6.0 | 4.8 solo, 5.3 ast, 0.00 sack, 0.29 PD, 0.00 INT | Questionable |
| LB | Cody Barton | 2.3 | 1.7 solo, 2.3 ast, 0.00 sack, 0.21 PD, 0.00 INT | Questionable |
| DB | Kevin Winston Jr. | 5.9 | 3.8 solo, 2.9 ast, 0.00 sack, 0.07 PD, 0.00 INT |  |
| DB | Joshua Williams | 5.3 | 3.6 solo, 2.4 ast, 0.00 sack, 0.43 PD, 0.00 INT |  |
| DB | Cordale Flott | 5.0 | 2.8 solo, 1.5 ast, 0.00 sack, 0.64 PD, 0.28 INT |  |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 24.0 | 274 pass yd, 2.0 TD, 0.7 INT; 3.8 rush, 16 yd |  |
| RB | Javonte Williams | 18.9 | 22.0 car, 88 yd, 1.11 TD; 1.9 rec, 13 yd, 0.09 TD |  |
| RB | Hunter Luepke | 1.9 | 1.3 car, 6 yd, 0.03 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | CeeDee Lamb | 19.8 | 7.1 rec, 86 yd, 0.68 TD |  |
| WR | George Pickens | 15.6 | 5.2 rec, 69 yd, 0.60 TD |  |
| WR | Ryan Flournoy | 10.3 | 3.7 rec, 45 yd, 0.34 TD |  |
| WR | KaVontae Turpin | 2.8 | 0.7 car, 3 yd, 0.07 TD; 0.8 rec, 9 yd, 0.06 TD |  |
| TE | Brevyn Spann-Ford | 3.8 | 1.6 rec, 18 yd, 0.07 TD |  |
| TE | Luke Schoonmaker | 1.4 | 0.6 rec, 7 yd, 0.03 TD |  |
| K | Brandon Aubrey | 10.2 | 1.9 FG, 3.2 XP |  |
| DL | Quinnen Williams | 6.7 | 2.8 solo, 2.0 ast, 0.66 sack, 0.12 PD, 0.03 INT |  |
| DL | Elijah Garcia | 3.0 | 1.0 solo, 1.9 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| LB | Shemar James | 4.8 | 3.0 solo, 2.0 ast, 0.02 sack, 0.12 PD, 0.13 INT |  |
| LB | Dee Winters | 4.0 | 2.6 solo, 1.6 ast, 0.00 sack, 0.12 PD, 0.12 INT |  |
| LB | DeMarvion Overshown | 3.9 | 1.7 solo, 2.1 ast, 0.00 sack, 0.31 PD, 0.15 INT |  |
| DB | Caleb Downs | 6.5 | 3.2 solo, 3.2 ast, 0.20 sack, 0.37 PD, 0.16 INT |  |
| DB | Malik Hooker | 3.7 | 2.5 solo, 1.5 ast, 0.00 sack, 0.43 PD, 0.00 INT |  |
| DB | Markquese Bell | 3.1 | 2.2 solo, 1.5 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: IND: Alec Pierce, IND: Jaylon Carlies, IND: Will Mallory, IND: Bernhard Raimann, IND: Carl Lawson, IND: Akeem Davis-Gaither, IND: Cam Taylor-Britt, IND: Charvarius Ward, IND: Jerry Tillery, IND: Mo Alie-Cox, IND: Cameron Mitchell, IND: Jalen Travis, HOU: Chad Muma, HOU: Mario Edwards, HOU: Bryce Hall, HOU: Jaylin Noel, HOU: Kenneth Murray, Jr., HOU: Lewis Bond, HOU: Danielle Hunter, HOU: Jawhar Jordan, HOU: Jayden Higgins, HOU: Jaden Crumedy, HOU: Azeez Al-Shaair, HOU: E.J. Speed, HOU: British Brooks, HOU: Sabastian Harsh, HOU: Woody Marks, HOU: Brevin Jordan, HOU: Dare Ogunbowale, HOU: Marvin Harrison Jr., HOU: George Odum, HOU: Dylan Horton, MIA: Julian Hill, MIA: Zach Sieler, MIA: Jamree Kromah, MIA: Zane Gonzalez, MIA: Carlos Washington, MIA: Jalen Reagor, MIA: De'Von Achane, MIA: Ethan Bonner, MIA: Zeek Biggers, MIA: Liam Anderson, MIA: Malik Willis, MIA: Jordan Phillips, MIA: Matthew Butler, BUF: Andre Jones Jr., BUF: Tre'Davious White, BUF: Frank Gore Jr., BUF: Trent Sherfield, BUF: Keonta Jenkins, BUF: Te'Cory Couch, BUF: Kani Walker, BUF: Geno Stone, BUF: Phidarian Mathis, BUF: Josh Palmer, BUF: Shaq Thompson, BAL: Adisa Isaac, BAL: Lamar Jackson, BAL: Chris Moore, BAL: Tyler Loop, BAL: Tyler Huntley, BAL: Carl Jones, BAL: Jovaughn Gwyn, BAL: Tavius Robinson, BAL: Durham Smythe, CAR: Mike Jackson, CAR: Nic Scourton, CAR: Ja'Seem Reed, CAR: Jaycee Horn, CAR: Nick Hampton, CAR: Cam Jackson, CAR: Akayleb Evans, CAR: Jonathon Brooks, CAR: Corey Thornton, CAR: LaBryan Ray, CAR: David Moore, CAR: Claudin Cherelus, CAR: Ikem Ekwonu, CAR: Thomas Incoom, CAR: Taylor Moton, NO: Moliki Matavao, NO: Asim Richards, NO: Jayden Price, NO: Kevin Austin Jr., NO: Mason Tipton, NO: Charlie Smyth, NO: Treyton Welch, NO: Jonah Williams, NO: Fadil Diggs, NO: Zamir White, NO: Dillon Radunz, NO: Christen Miller, NO: Bryan Bresee, NO: Jalen Cropper, CHI: Braxton Jones, CHI: Salvon Ahmed, CHI: Dayo Odeyingbo, CHI: Zavier Scott, CHI: Kaden Davis, CHI: Brittain Brown, CHI: Beau Gardner, CHI: Kentavius Street, CHI: Nikola Kalinic, CHI: Buddy Johnson, CHI: Cole Kmet, TEN: James Williams, TEN: Kalel Mullings, TEN: Dominique Hampton, TEN: Wan'Dale Robinson, TEN: Erick Hallett, TEN: Michael Carter, TEN: Jaylen Harrell, TEN: Tommy Townsend, TEN: Kendell Brooks, DAL: Malik Davis, DAL: Israel Abanikanda, DAL: Jalen Thompson, DAL: Tyler Goodson, DAL: Curtis Robinson, DAL: Malachi Lawrence, DAL: Tyler Booker, DAL: Jordan Hudson, DAL: Jake Ferguson, DAL: DaRon Bland, TB: David Sills, TB: Christian Rozeboom, TB: Josh Hayes, TB: Josh Williams, TB: Jalen McMillan, DET: Ben Bartch, DET: Thomas Harper, DET: Jackson Meeks, DET: Aidan Hutchinson, DET: Jack Campbell, DET: Jabari Small, DET: Jimmy Rolder, DET: Nick Whiteside, DET: Tom Kennedy, DET: Avonte Maddox, DET: Anthony Lucas, DET: Devin White, ARI: Jalen Brooks, ARI: Kenny Yeboah, ARI: Zay Jones, ARI: Michael Wilson, ARI: Jordan Burch, ARI: Art Green, ARI: Paris Johnson Jr., ARI: Jeremiyah Love, ARI: Andrew Wingard, ARI: Gardner Minshew, ARI: Kendrick Bourne, ARI: Will Johnson, ARI: Zachary Carter, KC: Nate Carter, KC: Cole Christiansen, KC: Jared Wiley, KC: Ethan Downs, KC: Justin Watson, KC: Tyquan Thornton, KC: Brashard Smith, KC: Jacob De Jesus, KC: L'Jarius Sneed, JAX: Robert Hainsey, JAX: Caleb Ransaw, JAX: Austin Trammell, JAX: DaVon Hamilton, JAX: Nick Mullens, JAX: Eric Murray, JAX: BJ Green II, JAX: Austin Johnson, JAX: Cam'Ron Silmon-Craig, JAX: Patrick Mekari, JAX: Anton Harrison, NYG: Dawuane Smoot, NYG: Braxton Berrios, NYG: Rico Payton, NYG: Raheem Layne, NYG: Roy Robertson-Harris, NYG: Charlie Jones, NYG: Chandler Martin, NYG: Brian Burns, NYG: Nikko Reed, NYG: Chauncey Golston, NYG: Gunner Olszewski, NYG: Dalen Cambre, NYG: Tyrone Tracy Jr., NYG: Tremaine Edmunds, NYG: Jaxson Dart, NYJ: Jamaal Pritchett, NYJ: Max Mitchell, NYJ: Mykal Walker, NYJ: Jordan Clark, NYJ: Marcelino McCrary-Ball, NYJ: Braiden McGregor, NYJ: Samuel Womack, NYJ: Sterling Shepard, NYJ: David Onyemata, NYJ: T'Vondre Sweat, NYJ: Arian Smith, NYJ: Kingsley Jonathan, LAC: Rashawn Slater, LAC: Trey Pipkins, LAC: Patrick Herbert, LAC: Da'Shawn Hand, LAC: Alec Ingold, LAC: Trey Lance, LAC: Trevor Penning, LAC: Derwin James, LAC: Daniel Brunskill, LAC: Branson Taylor, LV: Chigozie Anusiem, LV: Deven Thompkins, LV: Carter Runyon, LV: Patrick Johnson, LV: Greedy Vance, LV: Cian Slone, DEN: Cody Schrader, DEN: Kolbe Katsis, DEN: Sean Fresch, DEN: Jonah Elliss, DEN: Michael Bandy, DEN: Tyler Badie, DEN: Eyioma Uwazurike, DEN: Taylor Rapp, DEN: RJ Harvey, PIT: Brandon Johnson, PIT: Roman Wilson, PIT: Michael Pittman, PIT: Mason McCormick, PIT: Logan Lee, PIT: Sebastian Joseph-Day, PIT: Esezi Otomewo, PIT: Sebastian Castro, PIT: Marquez Valdes-Scantling, PHI: Keyshawn James-Newby, PHI: Andre' Sam, PHI: Chance Campbell, PHI: Will Shipley, PHI: Elijah Mitchell, PHI: Jalen Hurts, PHI: Tank Bigsby, PHI: Cole Wisniewski, MIN: Kyler Murray, MIN: Josh Oliver, MIN: C.J. Ham, MIN: Bo Richter, MIN: Donovan Jackson, MIN: Jordan Addison, MIN: Tyler Batty, MIN: Demond Claiborne, SF: Robert Beal Jr., SF: Alfred Collins, SF: Kalia Davis, SF: Ogbo Okoronkwo, SF: C.J. West, SF: Isaac Guerendo, SF: Jake Tonges, SF: Jack Jones, SF: Sam Okuayinonu, SF: KhaDarel Hodge, SF: Nick Martin, SF: Gracen Halton, SF: Ricky Pearsall, SF: Jalen Graham, CIN: Ke'Shawn Williams, CIN: Cashius Howell, CIN: Tanner Hudson, CIN: Isaiah Foskey, CIN: Swayze Bozeman, CIN: Bralyn Lux, CIN: Erick All, CIN: Jalen Davis, CIN: Andrei Iosivas, CIN: Howard Cross III, WAS: Craig Reynolds, WAS: Dyami Brown, WAS: Jacory Croskey-Merritt, WAS: Austin Keys, WAS: Javontae Jean-Baptiste, WAS: Jeremy McNichols, WAS: Nick Bellore, WAS: Jaylin Lane, WAS: Terry McLaurin, WAS: Javon Kinlaw, WAS: Leo Chenal, WAS: Daron Payne, WAS: Jaden Bradley.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 23.0 | 8.8 to 38.4 |
| QB | Josh Allen | BUF | 22.2 | 8.0 to 38.0 |
| QB | C.J. Stroud | HOU | 22.0 | 8.1 to 37.4 |
| QB | Dak Prescott | DAL | 21.8 | 8.5 to 36.3 |
| QB | Jayden Daniels | WAS | 20.0 | 7.0 to 34.6 |
| QB | Patrick Mahomes | KC | 19.0 | 6.7 to 32.9 |
| RB | Jahmyr Gibbs | DET | 24.4 | 8.6 to 42.1 |
| RB | Javonte Williams | DAL | 20.1 | 5.6 to 36.3 |
| RB | Tony Pollard | TEN | 18.3 | 5.7 to 33.1 |
| RB | Chuba Hubbard | CAR | 18.2 | 5.5 to 33.1 |
| RB | Chase Brown | CIN | 17.8 | 6.3 to 31.1 |
| RB | James Cook | BUF | 17.7 | 4.6 to 32.2 |
| RB | Jonathan Taylor | IND | 17.5 | 6.0 to 31.2 |
| RB | Jaylen Warren | PIT | 17.0 | 5.4 to 30.6 |
| RB | Christian McCaffrey | SF | 16.8 | 4.9 to 30.7 |
| RB | Bucky Irving | TB | 15.6 | 4.5 to 29.0 |
| WR | CeeDee Lamb | DAL | 20.8 | 6.4 to 37.3 |
| WR | Ja'Marr Chase | CIN | 20.4 | 6.4 to 36.5 |
| WR | Amon-Ra St. Brown | DET | 17.9 | 5.1 to 33.1 |
| WR | George Pickens | DAL | 16.3 | 3.8 to 31.2 |
| WR | Justin Jefferson | MIN | 15.9 | 4.3 to 29.8 |
| WR | Tee Higgins | CIN | 15.4 | 3.5 to 30.1 |
| WR | Luther Burden III | CHI | 14.9 | 3.6 to 28.6 |
| WR | Nico Collins | HOU | 14.2 | 3.0 to 28.0 |
| WR | Parker Washington | JAX | 13.9 | 2.5 to 27.8 |
| WR | Malik Nabers | NYG | 13.6 | 3.4 to 26.5 |
| WR | Zay Flowers | BAL | 13.2 | 2.9 to 25.8 |
| WR | Tetairoa McMillan | CAR | 12.4 | 2.4 to 24.8 |
| TE | Trey McBride | ARI | 22.5 | 8.7 to 38.3 |
| TE | Tyler Warren | IND | 14.2 | 4.3 to 26.2 |
| TE | Isaiah Likely | NYG | 13.7 | 2.9 to 26.8 |
| TE | Colston Loveland | CHI | 11.3 | 2.1 to 22.4 |
| TE | George Kittle | SF | 9.5 | 1.3 to 19.2 |
| TE | Dalton Schultz | HOU | 9.2 | 1.3 to 18.5 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 21.7 | 8.9 to 36.0 |
| QB | Josh Allen | BUF | 21.5 | 8.1 to 36.5 |
| QB | C.J. Stroud | HOU | 21.0 | 8.2 to 35.5 |
| QB | Dak Prescott | DAL | 20.7 | 8.6 to 34.2 |
| QB | Jayden Daniels | WAS | 19.4 | 7.0 to 33.4 |
| QB | Patrick Mahomes | KC | 18.2 | 6.8 to 31.0 |
| RB | Jahmyr Gibbs | DET | 21.1 | 7.4 to 36.7 |
| RB | Javonte Williams | DAL | 18.0 | 5.1 to 32.7 |
| RB | Tony Pollard | TEN | 16.1 | 4.8 to 29.4 |
| RB | Chuba Hubbard | CAR | 16.1 | 4.6 to 29.5 |
| RB | James Cook | BUF | 16.0 | 4.5 to 29.2 |
| RB | Chase Brown | CIN | 15.1 | 4.7 to 27.2 |
| RB | Christian McCaffrey | SF | 14.9 | 3.9 to 27.8 |
| RB | Jaylen Warren | PIT | 14.7 | 4.6 to 26.6 |
| RB | Jonathan Taylor | IND | 14.7 | 4.6 to 26.5 |
| RB | Bucky Irving | TB | 13.7 | 3.8 to 25.7 |
| WR | CeeDee Lamb | DAL | 16.2 | 4.5 to 29.4 |
| WR | Ja'Marr Chase | CIN | 15.6 | 4.5 to 28.4 |
| WR | Amon-Ra St. Brown | DET | 13.7 | 3.4 to 25.5 |
| WR | George Pickens | DAL | 13.0 | 2.5 to 25.1 |
| WR | Justin Jefferson | MIN | 12.2 | 2.7 to 23.4 |
| WR | Tee Higgins | CIN | 12.1 | 2.4 to 23.5 |
| WR | Luther Burden III | CHI | 11.9 | 2.3 to 23.1 |
| WR | Nico Collins | HOU | 11.2 | 2.0 to 22.1 |
| WR | Parker Washington | JAX | 11.2 | 1.7 to 22.0 |
| WR | Zay Flowers | BAL | 10.4 | 1.9 to 20.6 |
| WR | Malik Nabers | NYG | 10.2 | 2.2 to 19.8 |
| WR | Tetairoa McMillan | CAR | 9.7 | 1.5 to 19.4 |
| TE | Trey McBride | ARI | 15.9 | 5.5 to 27.7 |
| TE | Isaiah Likely | NYG | 10.7 | 1.7 to 21.6 |
| TE | Tyler Warren | IND | 10.4 | 2.6 to 19.8 |
| TE | Colston Loveland | CHI | 8.8 | 1.1 to 18.2 |
| TE | George Kittle | SF | 7.4 | 0.6 to 15.7 |
| TE | Dalton Schultz | HOU | 7.2 | 0.7 to 15.1 |
| K | Tyler Bass | BUF | 10.1 | 3.0 to 18.0 |
| K | Ka'imi Fairbairn | HOU | 10.0 | 3.0 to 18.2 |
| K | Jason Sanders | NYJ | 9.8 | 1.0 to 19.0 |
| K | Will Reichard | MIN | 9.7 | 1.0 to 19.0 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses come from the merged injury file (MFL, nflverse, ESPN, transactions) at the time of the pull. Re-run when news lands.
- Weather, referee tendencies and in-game injuries are not modeled.