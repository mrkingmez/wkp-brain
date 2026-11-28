# Week 11 Full Simulation Report - 21 Nov 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 20,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| IND @ HOU | HOU 83.1% | IND 16.2 - HOU 28.6 | HOU | 53.1% | HOU | 83.7% |
| MIA @ BUF | BUF 89.5% | MIA 14.2 - BUF 30.6 | MIA | 50.0% | BUF | 90.3% |
| BAL @ CAR | CAR 57.0% | BAL 20.6 - CAR 23.0 | BAL | 50.0% | CAR | 57.8% |
| NO @ CHI | CHI 80.5% | NO 18.6 - CHI 30.1 | NO | 50.0% | CHI | 81.7% |
| TEN @ DAL | DAL 71.3% | TEN 23.8 - DAL 31.2 | TEN | 51.6% | DAL | 73.5% |
| TB @ DET | DET 63.5% | TB 20.8 - DET 25.2 | TB | 48.4% | DET | 70.9% |
| ARI @ KC | KC 89.8% | ARI 12.4 - KC 28.6 | ARI | 51.6% | KC | 89.6% |
| JAX @ NYG | JAX 67.5% | JAX 26.0 - NYG 20.0 | NYG | 51.6% | JAX | 68.1% |
| NYJ @ LAC | LAC 59.0% | NYJ 19.6 - LAC 22.6 | NYJ | 51.6% | LAC | 59.3% |
| LV @ DEN | DEN 78.6% | LV 15.2 - DEN 25.6 | LV | 51.6% | DEN | 78.4% |
| PIT @ PHI | PIT 60.1% | PIT 20.7 - PHI 17.3 | PHI | 50.0% | PIT | 63.8% |
| MIN @ SF | SF 60.2% | MIN 21.6 - SF 25.0 | MIN | 51.6% | SF | 59.3% |
| CIN @ WAS | CIN 67.6% | CIN 30.1 - WAS 24.1 | WSH | 50.0% | CIN | 69.5% |

**Eliminator:** biggest favorites this week by win chance: KC 89.8%, BUF 89.5%, HOU 83.1%, CHI 80.5%, DEN 78.6%. Teams already used are not tracked here, check FUTURES-PICKS.md.

## 2. IRFL lineups

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 143.1 | 108.7 | 179.1 |
| 2 SAFE (protects a lead) | 142.1 | 108.7 | 177.2 |
| 3 BALANCED UPSIDE (75th percentile) | 143.1 | 108.7 | 179.1 |
| 4 SWING (90th percentile, for an underdog) | 142.0 | 107.4 | 178.0 |
| 5 CONTINGENCY (every Questionable out) | 142.2 | 108.8 | 177.3 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | Dowdle, Rico | PIT | 8.9 | 1.7 to 17.9 |  |
| RB | White, Rachaad | WAS | 8.4 | 0.0 to 20.2 | Questionable, plays about 75% of sims. |
| WR | Jefferson, Justin | MIN | 15.5 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.8 | 1.4 to 21.6 |  |
| WR | Flournoy, Ryan | DAL | 10.7 | 1.6 to 21.2 |  |
| TE | Hockenson, T.J. | MIN | 10.7 | 1.8 to 21.1 |  |
| PK | Bates, Jake | DET | 9.3 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.0 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.0 |  |
| LB | Gibbens, Jack | ARI | 4.4 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | Dowdle, Rico | PIT | 8.9 | 1.7 to 17.9 |  |
| RB | Demercado, Emari | HOU | 7.6 | 1.1 to 15.5 | differs from lineup 1 |
| WR | Jefferson, Justin | MIN | 15.5 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.8 | 1.4 to 21.6 |  |
| WR | Flournoy, Ryan | DAL | 10.7 | 1.6 to 21.2 |  |
| TE | Hockenson, T.J. | MIN | 10.7 | 1.8 to 21.1 |  |
| PK | Bates, Jake | DET | 9.3 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.0 | 0.0 to 8.5 |  |
| LB | Gibbens, Jack | ARI | 4.4 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| LB | Barton, Cody | TEN | 3.0 | 1.0 to 5.5 | differs from lineup 1 |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 8.4 | 0.0 to 20.2 | Questionable, plays about 75% of sims. |
| RB | Dowdle, Rico | PIT | 8.9 | 1.7 to 17.9 |  |
| WR | Jefferson, Justin | MIN | 15.5 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.8 | 1.4 to 21.6 |  |
| WR | Flournoy, Ryan | DAL | 10.7 | 1.6 to 21.2 |  |
| TE | Hockenson, T.J. | MIN | 10.7 | 1.8 to 21.1 |  |
| PK | Bates, Jake | DET | 9.3 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.0 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.0 |  |
| LB | Gibbens, Jack | ARI | 4.4 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | White, Rachaad | WAS | 8.4 | 0.0 to 20.2 | Questionable, plays about 75% of sims. |
| RB | Dowdle, Rico | PIT | 8.9 | 1.7 to 17.9 |  |
| WR | Jefferson, Justin | MIN | 15.5 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.8 | 1.4 to 21.6 |  |
| WR | Flournoy, Ryan | DAL | 10.7 | 1.6 to 21.2 |  |
| TE | Hockenson, T.J. | MIN | 10.7 | 1.8 to 21.1 |  |
| PK | Bates, Jake | DET | 9.3 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.0 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.0 |  |
| LB | Gibbens, Jack | ARI | 4.4 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Reed, D.J. | DET | 3.9 | 0.0 to 8.5 | Questionable, plays about 75% of sims. differs from lineup 1 |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 20.0 | 5.0 to 36.9 |  |
| RB | Dowdle, Rico | PIT | 8.9 | 1.7 to 17.9 |  |
| RB | Demercado, Emari | HOU | 7.6 | 1.1 to 15.5 | differs from lineup 1 |
| WR | Jefferson, Justin | MIN | 15.5 | 4.5 to 27.7 |  |
| WR | Flowers, Zay | BAL | 12.8 | 3.0 to 24.3 |  |
| WR | Williams, Jameson | DET | 10.8 | 1.4 to 21.6 |  |
| WR | Flournoy, Ryan | DAL | 10.7 | 1.6 to 21.2 |  |
| TE | Hockenson, T.J. | MIN | 10.7 | 1.8 to 21.1 |  |
| PK | Bates, Jake | DET | 9.3 | 2.0 to 18.0 |  |
| DL | Wonnum, D.J. | DET | 4.2 | 0.5 to 8.5 |  |
| DL | Moore, Derrick | DET | 4.0 | 0.0 to 8.5 |  |
| DL | Davis, Jordan | JAC | 3.1 | 0.5 to 6.0 |  |
| LB | Gibbens, Jack | ARI | 4.4 | 1.5 to 8.0 |  |
| LB | Strnad, Justin | DEN | 4.0 | 1.0 to 7.5 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 4.9 | 1.5 to 8.5 |  |

Lineups 1 and 3 are identical. Where they match, the roster has no real choice between safe and swing this week.

Not simulated this week (bye, no team, new team, or no recent usage, check each one): Robinson, Tavius (BAL); Okereke, Bobby (CAR); Reid, Winston (CLE); Folk, Nick (FA); Carter, Michael (TEN); Corum, Blake (LAR); Jenkins, Rayshawn (BAL); Kinchens, Kamren (LAR); Locke, P.J. (DAL); Shepard, Sterling (NYJ); Golden, Matthew (GBP); Hollins, Mack (NEP).

Changed teams and simulated on the new team with his own old-team rates: Andre Cisco (DB, NYJ to DET); Jessie Bates (DB, ATL to JAX); Jordan Davis (DL, PHI to JAX).

Starting quarterbacks named by hand in the overrides file: BAL Jacoby Brissett; NYG J.J. McCarthy; PHI Joe Milton III; MIN Kirk Cousins.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ KC

Market: KC -16.5, total 40.5. Sim: ARI 12.4, KC 28.6. KC wins 89.8%, ARI wins 10.2%. Median margin +16.7 for KC.

| Team stat | ARI | KC |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 39 / 24 | 32 / 21 |
| Passing yards | 233 | 250 |
| Rush attempts / yards | 22 / 87 | 28 / 129 |
| Sacks taken | 2.6 | 2.2 |
| Interceptions thrown | 0.9 | 0.5 |
| Passing / rushing TDs | 0.9 / 0.4 | 1.8 / 1.3 |
| Field goals | 0.9 | 2.2 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Carson Beck | 14.2 | 233 pass yd, 0.9 TD, 0.9 INT; 2.7 rush, 11 yd | Questionable |
| RB | Tyler Allgeier | 12.6 | 13.0 car, 50 yd, 0.33 TD; 3.1 rec, 21 yd, 0.10 TD |  |
| RB | Bam Knight | 5.6 | 6.0 car, 25 yd, 0.07 TD; 1.4 rec, 12 yd, 0.03 TD |  |
| RB | Evan Hull | 1.8 | 0.0 car, 0 yd, 0.00 TD; 0.8 rec, 8 yd, 0.02 TD |  |
| WR | Harrison Wallace III | 4.1 | 2.0 rec, 19 yd, 0.03 TD |  |
| WR | Reggie Virgil | 3.9 | 1.7 rec, 19 yd, 0.04 TD |  |
| WR | Devin Duvernay | 2.4 | 1.2 rec, 11 yd, 0.02 TD |  |
| WR | Simi Fehoko | 1.4 | 0.6 rec, 7 yd, 0.01 TD |  |
| TE | Trey McBride | 21.8 | 11.4 rec, 85 yd, 0.35 TD |  |
| TE | Elijah Higgins | 5.9 | 3.0 rec, 26 yd, 0.06 TD |  |
| K | Chad Ryland | 8.5 | 1.9 FG, 1.3 XP |  |
| DL | L.J. Collier | 2.7 | 1.1 solo, 0.9 ast, 0.27 sack, 0.33 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.4 | 1.1 solo, 1.6 ast, 0.15 sack, 0.00 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.5 | 3.1 solo, 4.0 ast, 0.00 sack, 0.18 PD, 0.00 INT |  |
| LB | Jack Gibbens | 4.4 | 2.5 solo, 3.6 ast, 0.03 sack, 0.06 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.6 | 1.5 solo, 1.5 ast, 0.32 sack, 0.11 PD, 0.00 INT |  |
| DB | Budda Baker | 6.3 | 2.9 solo, 4.0 ast, 0.23 sack, 0.29 PD, 0.06 INT |  |
| DB | Denzel Burke | 4.0 | 2.3 solo, 0.9 ast, 0.00 sack, 0.80 PD, 0.09 INT |  |
| DB | Max Melton | 3.2 | 1.9 solo, 1.5 ast, 0.00 sack, 0.56 PD, 0.00 INT |  |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 23.3 | 250 pass yd, 1.8 TD, 0.5 INT; 4.9 rush, 23 yd |  |
| RB | Emmett Johnson | 15.2 | 12.1 car, 56 yd, 0.51 TD; 2.2 rec, 29 yd, 0.28 TD |  |
| RB | Kareem Hunt | 4.0 | 4.5 car, 20 yd, 0.21 TD; 0.3 rec, 4 yd, 0.02 TD |  |
| RB | Jaydn Ott | 1.4 | 2.3 car, 11 yd, 0.06 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Rashee Rice | 9.4 | 3.9 rec, 42 yd, 0.23 TD |  |
| WR | Josh Downs | 8.7 | 3.2 rec, 36 yd, 0.33 TD |  |
| WR | Xavier Worthy | 6.9 | 3.1 rec, 28 yd, 0.17 TD |  |
| WR | Cyrus Allen | 3.3 | 1.1 rec, 14 yd, 0.14 TD |  |
| TE | Travis Kelce | 10.2 | 3.5 rec, 43 yd, 0.21 TD |  |
| TE | Noah Gray | 4.0 | 1.6 rec, 17 yd, 0.12 TD |  |
| K | Harrison Butker | 8.5 | 1.5 FG, 2.9 XP |  |
| DL | George Karlaftis | 6.6 | 1.7 solo, 1.7 ast, 0.82 sack, 1.19 PD, 0.08 INT |  |
| DL | Chris Jones | 4.1 | 1.0 solo, 1.2 ast, 0.69 sack, 0.38 PD, 0.00 INT |  |
| LB | Nick Bolton | 8.5 | 4.8 solo, 5.3 ast, 0.04 sack, 0.18 PD, 0.05 INT |  |
| LB | Drue Tranquill | 7.1 | 4.7 solo, 4.2 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.7 | 1.1 solo, 1.9 ast, 0.00 sack, 0.10 PD, 0.10 INT |  |
| DB | Nohl Williams | 6.0 | 2.5 solo, 2.0 ast, 0.11 sack, 1.37 PD, 0.27 INT |  |
| DB | Chamarri Conner | 5.2 | 2.6 solo, 2.6 ast, 0.16 sack, 0.33 PD, 0.06 INT |  |
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
| DL | Broderick Washington | 1.6 | 0.4 solo, 0.6 ast, 0.00 sack, 0.39 PD, 0.15 INT |  |
| LB | Roquan Smith | 7.1 | 4.0 solo, 3.9 ast, 0.14 sack, 0.26 PD, 0.04 INT |  |
| LB | Trenton Simpson | 5.6 | 3.1 solo, 3.5 ast, 0.10 sack, 0.06 PD, 0.07 INT |  |
| LB | Mike Green | 4.1 | 1.5 solo, 1.3 ast, 0.61 sack, 0.00 PD, 0.00 INT |  |
| DB | Kyle Hamilton | 6.5 | 4.7 solo, 1.9 ast, 0.00 sack, 0.44 PD, 0.08 INT |  |
| DB | Malaki Starks | 4.8 | 2.9 solo, 2.3 ast, 0.04 sack, 0.25 PD, 0.00 INT |  |
| DB | K'Von Wallace | 3.7 | 3.0 solo, 0.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |

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
| TE | Darren Waller | 5.4 | 2.6 rec, 31 yd, 0.26 TD | Questionable |
| TE | Tommy Tremble | 4.6 | 2.5 rec, 23 yd, 0.22 TD | Questionable |
| K | Ryan Fitzgerald | 8.2 | 1.6 FG, 2.3 XP |  |
| DL | Derrick Brown | 3.9 | 2.0 solo, 1.9 ast, 0.18 sack, 0.39 PD, 0.00 INT |  |
| DL | Aaron Hall | 1.8 | 0.7 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 7.8 | 3.9 solo, 3.1 ast, 0.17 sack, 0.51 PD, 0.30 INT |  |
| LB | Patrick Jones II | 3.3 | 1.9 solo, 0.7 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| LB | Jaelan Phillips | 3.2 | 0.9 solo, 1.0 ast, 0.44 sack, 0.00 PD, 0.00 INT |  |
| DB | Marco Wilson | 5.3 | 3.8 solo, 0.9 ast, 0.00 sack, 1.15 PD, 0.00 INT |  |
| DB | Nick Scott | 4.9 | 3.6 solo, 1.3 ast, 0.00 sack, 0.21 PD, 0.03 INT |  |
| DB | Will Lee III | 4.3 | 2.5 solo, 1.3 ast, 0.00 sack, 0.68 PD, 0.00 INT |  |

### CIN @ WAS

Market: WAS +6.0, total 54.0. Sim: CIN 30.1, WAS 24.1. WAS wins 32.4%, CIN wins 67.6%. Median margin -5.9 for WAS.

| Team stat | CIN | WAS |
|---|---|---|
| Plays | 63 | 61 |
| Pass attempts / completions | 36 / 26 | 32 / 20 |
| Passing yards | 283 | 224 |
| Rush attempts / yards | 25 / 104 | 26 / 124 |
| Sacks taken | 2.5 | 2.9 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 2.0 / 1.2 | 1.4 / 1.2 |
| Field goals | 2.3 | 1.8 |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 25.0 | 283 pass yd, 2.0 TD, 0.7 INT; 2.6 rush, 11 yd |  |
| RB | Chase Brown | 17.4 | 13.0 car, 55 yd, 0.46 TD; 4.8 rec, 29 yd, 0.29 TD |  |
| RB | Samaje Perine | 7.8 | 6.8 car, 28 yd, 0.40 TD; 1.3 rec, 10 yd, 0.07 TD |  |
| RB | Tahj Brooks | 0.7 | 1.2 car, 5 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Ja'Marr Chase | 19.4 | 7.4 rec, 90 yd, 0.52 TD |  |
| WR | Tee Higgins | 14.8 | 5.4 rec, 68 yd, 0.44 TD |  |
| WR | Dohnte Meyers | 5.2 | 2.0 rec, 22 yd, 0.13 TD |  |
| WR | Mitchell Tinsley | 1.9 | 0.8 rec, 9 yd, 0.04 TD |  |
| TE | Mike Gesicki | 5.9 | 2.1 rec, 24 yd, 0.25 TD |  |
| TE | Drew Sample | 3.3 | 1.4 rec, 11 yd, 0.14 TD |  |
| K | Evan McPherson | 8.2 | 1.4 FG, 3.0 XP |  |
| DL | Boye Mafe | 5.1 | 1.6 solo, 1.2 ast, 0.74 sack, 0.10 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 4.2 | 1.7 solo, 1.2 ast, 0.50 sack, 0.11 PD, 0.00 INT |  |
| LB | Barrett Carter | 6.9 | 2.8 solo, 4.7 ast, 0.11 sack, 0.61 PD, 0.16 INT |  |
| LB | Demetrius Knight Jr. | 6.5 | 3.9 solo, 3.1 ast, 0.11 sack, 0.28 PD, 0.10 INT |  |
| LB | Joe Giles-Harris | 1.2 | 0.8 solo, 0.8 ast, 0.00 sack, 0.04 PD, 0.00 INT |  |
| DB | Jordan Battle | 7.2 | 4.3 solo, 1.9 ast, 0.00 sack, 0.84 PD, 0.27 INT |  |
| DB | Bryan Cook | 5.2 | 3.7 solo, 2.1 ast, 0.06 sack, 0.00 PD, 0.00 INT |  |
| DB | DJ Turner II | 3.3 | 1.6 solo, 0.9 ast, 0.00 sack, 0.56 PD, 0.00 INT |  |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 21.7 | 224 pass yd, 1.4 TD, 0.6 INT; 5.8 rush, 31 yd |  |
| RB | Rachaad White | 8.4 | 9.0 car, 41 yd, 0.48 TD; 2.0 rec, 16 yd, 0.13 TD | Questionable |
| RB | Austin Ekeler | 7.2 | 7.1 car, 30 yd, 0.18 TD; 1.6 rec, 13 yd, 0.05 TD |  |
| RB | Robert Henry Jr. | 1.1 | 1.8 car, 8 yd, 0.04 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Stefon Diggs | 10.6 | 4.2 rec, 43 yd, 0.35 TD |  |
| WR | Antonio Williams | 7.2 | 3.0 rec, 32 yd, 0.17 TD |  |
| WR | Van Jefferson | 5.9 | 2.2 rec, 23 yd, 0.24 TD |  |
| WR | Treylon Burks | 2.2 | 2.0 rec, 28 yd, 0.13 TD | Questionable |
| TE | Chig Okonkwo | 7.8 | 3.7 rec, 34 yd, 0.12 TD |  |
| TE | Ben Sinnott | 3.1 | 1.2 rec, 12 yd, 0.11 TD |  |
| K | Drew Stevens | 9.2 | 1.8 FG, 2.5 XP |  |
| DL | Shy Tuttle | 3.1 | 1.3 solo, 1.6 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Dorance Armstrong | 2.7 | 1.3 solo, 1.2 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 8.1 | 4.3 solo, 5.5 ast, 0.07 sack, 0.41 PD, 0.09 INT |  |
| LB | Frankie Luvu | 6.5 | 3.1 solo, 4.2 ast, 0.20 sack, 0.20 PD, 0.00 INT |  |
| LB | K'Lavon Chaisson | 4.2 | 1.6 solo, 1.2 ast, 0.39 sack, 0.00 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 6.1 | 3.8 solo, 2.8 ast, 0.00 sack, 0.55 PD, 0.05 INT |  |
| DB | Amik Robertson | 6.0 | 3.8 solo, 1.9 ast, 0.00 sack, 1.06 PD, 0.00 INT |  |
| DB | Nick Cross | 5.8 | 3.1 solo, 2.3 ast, 0.00 sack, 0.59 PD, 0.20 INT |  |

### IND @ HOU

Market: HOU -12.5, total 44.5. Sim: IND 16.2, HOU 28.6. HOU wins 83.1%, IND wins 16.9%. Median margin +12.6 for HOU.

| Team stat | IND | HOU |
|---|---|---|
| Plays | 62 | 63 |
| Pass attempts / completions | 34 / 21 | 33 / 21 |
| Passing yards | 208 | 262 |
| Rush attempts / yards | 25 / 104 | 28 / 110 |
| Sacks taken | 3.0 | 2.2 |
| Interceptions thrown | 0.9 | 0.5 |
| Passing / rushing TDs | 0.9 / 0.9 | 1.8 / 1.3 |
| Field goals | 1.2 | 2.2 |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Philip Rivers | 12.0 | 208 pass yd, 0.9 TD, 0.9 INT |  |
| RB | Jonathan Taylor | 18.1 | 15.2 car, 58 yd, 0.52 TD; 4.8 rec, 40 yd, 0.09 TD |  |
| RB | Seth McGowan | 4.0 | 5.7 car, 27 yd, 0.23 TD; 0.7 rec, 5 yd, 0.01 TD | Questionable |
| RB | DJ Giddens | 1.1 | 2.0 car, 9 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Laquon Treadwell | 8.0 | 3.1 rec, 34 yd, 0.24 TD |  |
| WR | Ashton Dulin | 4.9 | 1.4 rec, 22 yd, 0.21 TD |  |
| WR | Deion Burks | 3.1 | 1.4 rec, 14 yd, 0.03 TD |  |
| WR | Anthony Gould | 1.8 | 1.1 rec, 12 yd, 0.02 TD | Questionable |
| TE | Tyler Warren | 14.0 | 7.0 rec, 52 yd, 0.25 TD |  |
| TE | Andrew Ogletree | 2.2 | 1.1 rec, 10 yd, 0.02 TD |  |
| K | Spencer Shrader | 8.9 | 1.9 FG, 1.7 XP |  |
| DL | Adetomiwa Adebawore | 4.1 | 1.4 solo, 1.5 ast, 0.41 sack, 0.38 PD, 0.00 INT |  |
| DL | Laiatu Latu | 3.4 | 1.3 solo, 0.8 ast, 0.38 sack, 0.19 PD, 0.00 INT |  |
| LB | CJ Allen | 5.4 | 1.9 solo, 3.9 ast, 0.37 sack, 0.39 PD, 0.00 INT |  |
| LB | Bryce Boettcher | 3.6 | 1.6 solo, 4.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Austin Ajiake | 2.3 | 1.1 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Justin Walley | 5.9 | 2.7 solo, 1.5 ast, 0.29 sack, 0.62 PD, 0.00 INT |  |
| DB | A.J. Haulcy | 4.0 | 2.9 solo, 1.8 ast, 0.00 sack, 0.17 PD, 0.00 INT |  |
| DB | Camryn Bynum | 3.6 | 2.0 solo, 1.6 ast, 0.00 sack, 0.46 PD, 0.12 INT |  |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 24.2 | 262 pass yd, 1.8 TD, 0.5 INT; 3.9 rush, 17 yd |  |
| RB | David Montgomery | 8.4 | 9.7 car, 36 yd, 0.56 TD; 0.6 rec, 6 yd, 0.06 TD |  |
| RB | Emari Demercado | 7.6 | 9.4 car, 37 yd, 0.24 TD; 1.2 rec, 11 yd, 0.05 TD |  |
| WR | Nico Collins | 13.8 | 5.0 rec, 62 yd, 0.43 TD |  |
| WR | Xavier Hutchinson | 9.4 | 0.6 car, 3 yd, 0.02 TD; 3.4 rec, 39 yd, 0.30 TD |  |
| WR | Tank Dell | 9.3 | 1.0 car, 4 yd, 0.03 TD; 3.0 rec, 45 yd, 0.22 TD |  |
| WR | Kayshon Boutte | 4.9 | 2.1 rec, 32 yd, 0.20 TD | Questionable |
| TE | Dalton Schultz | 9.1 | 3.8 rec, 39 yd, 0.22 TD |  |
| TE | Foster Moreau | 3.8 | 1.3 rec, 11 yd, 0.24 TD |  |
| K | Ka'imi Fairbairn | 10.8 | 2.1 FG, 2.9 XP |  |
| DL | Will Anderson Jr. | 6.5 | 2.0 solo, 1.6 ast, 1.03 sack, 0.06 PD, 0.00 INT |  |
| DL | Jadeveon Clowney | 3.9 | 1.1 solo, 0.8 ast, 0.67 sack, 0.36 PD, 0.00 INT |  |
| LB | Henry To'oTo'o | 4.6 | 2.1 solo, 3.3 ast, 0.07 sack, 0.18 PD, 0.00 INT |  |
| LB | Jake Hansen | 4.6 | 2.3 solo, 3.1 ast, 0.09 sack, 0.19 PD, 0.09 INT |  |
| LB | Jacob Hummel | 1.1 | 1.0 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | M.J. Stewart | 7.9 | 4.1 solo, 4.9 ast, 0.39 sack, 0.24 PD, 0.00 INT |  |
| DB | Kamari Lassiter | 6.7 | 4.0 solo, 1.7 ast, 0.12 sack, 1.34 PD, 0.06 INT |  |
| DB | Calen Bullock | 5.5 | 2.8 solo, 1.6 ast, 0.00 sack, 0.91 PD, 0.25 INT |  |

### JAX @ NYG

Market: NYG +6.0, total 46.0. Sim: JAX 26.0, NYG 20.0. NYG wins 32.5%, JAX wins 67.5%. Median margin -6.1 for NYG.

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
| QB | Trevor Lawrence | 19.7 | 250 pass yd, 1.5 TD, 0.7 INT; 3.1 rush, 14 yd |  |
| RB | Bhayshul Tuten | 13.9 | 14.6 car, 58 yd, 0.66 TD; 1.7 rec, 17 yd, 0.16 TD |  |
| RB | Chris Rodriguez Jr. | 6.0 | 6.4 car, 26 yd, 0.41 TD; 0.5 rec, 5 yd, 0.02 TD |  |
| RB | Ameer Abdullah | 1.9 | 2.9 car, 12 yd, 0.07 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Parker Washington | 13.3 | 4.4 rec, 66 yd, 0.39 TD |  |
| WR | Jakobi Meyers | 9.0 | 3.7 rec, 41 yd, 0.19 TD |  |
| WR | Brian Thomas Jr. | 4.9 | 1.9 rec, 21 yd, 0.15 TD |  |
| WR | Josh Cameron | 4.1 | 1.4 rec, 18 yd, 0.15 TD |  |
| TE | Brenton Strange | 8.1 | 3.4 rec, 35 yd, 0.20 TD |  |
| TE | Nate Boerkircher | 3.7 | 1.3 rec, 17 yd, 0.13 TD |  |
| K | Cam Little | 10.0 | 2.0 FG, 2.6 XP |  |
| DL | Josh Hines-Allen | 3.4 | 1.8 solo, 1.4 ast, 0.19 sack, 0.12 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.2 solo, 2.2 ast, 0.23 sack, 0.10 PD, 0.00 INT |  |
| LB | Foyesade Oluokun | 7.9 | 5.1 solo, 2.9 ast, 0.22 sack, 0.22 PD, 0.12 INT |  |
| LB | Ventrell Miller | 4.5 | 2.6 solo, 2.3 ast, 0.05 sack, 0.41 PD, 0.03 INT |  |
| LB | Branson Combs | 2.9 | 1.6 solo, 1.1 ast, 0.06 sack, 0.25 PD, 0.12 INT |  |
| DB | Jessie Bates | 7.2 | 4.1 solo, 2.4 ast, 0.00 sack, 0.41 PD, 0.14 INT |  |
| DB | Travis Hunter | 5.3 | 2.8 solo, 1.4 ast, 0.00 sack, 0.70 PD, 0.36 INT |  |
| DB | Antonio Johnson | 5.1 | 2.7 solo, 1.8 ast, 0.19 sack, 0.27 PD, 0.12 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | J.J. McCarthy | 15.4 | 226 pass yd, 1.1 TD, 0.9 INT; 2.8 rush, 12 yd |  |
| RB | Cam Skattebo | 11.1 | 11.9 car, 49 yd, 0.56 TD; 1.4 rec, 13 yd, 0.03 TD |  |
| RB | Devin Singletary | 5.6 | 5.6 car, 20 yd, 0.23 TD; 1.1 rec, 9 yd, 0.06 TD |  |
| RB | Najee Harris | 2.1 | 3.8 car, 15 yd, 0.08 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Malik Nabers | 13.2 | 5.7 rec, 61 yd, 0.23 TD |  |
| WR | Malachi Fields | 6.1 | 2.3 rec, 31 yd, 0.10 TD |  |
| WR | Darnell Mooney | 3.8 | 1.6 rec, 17 yd, 0.06 TD |  |
| WR | Darius Slayton | 2.5 | 1.1 rec, 11 yd, 0.06 TD |  |
| TE | Isaiah Likely | 13.4 | 5.3 rec, 53 yd, 0.46 TD |  |
| TE | Theo Johnson | 2.5 | 1.0 rec, 11 yd, 0.07 TD |  |
| K | Dominic Zvada | 8.7 | 1.8 FG, 2.0 XP |  |
| DL | Shelby Harris | 2.6 | 1.2 solo, 1.3 ast, 0.17 sack, 0.20 PD, 0.00 INT |  |
| DL | DJ Reader | 2.5 | 1.6 solo, 1.0 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Arvell Reese | 10.6 | 5.9 solo, 3.6 ast, 0.59 sack, 0.34 PD, 0.09 INT |  |
| LB | Micah McFadden | 5.8 | 3.7 solo, 2.2 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| LB | Kayvon Thibodeaux | 2.9 | 2.0 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Jevon Holland | 5.2 | 2.5 solo, 1.8 ast, 0.00 sack, 0.50 PD, 0.33 INT |  |
| DB | Ar'Darius Washington | 4.7 | 3.0 solo, 1.0 ast, 0.00 sack, 0.65 PD, 0.18 INT |  |
| DB | Greg Newsome II | 4.6 | 3.1 solo, 1.1 ast, 0.00 sack, 0.71 PD, 0.10 INT |  |

### LV @ DEN

Market: DEN -10.5, total 40.5. Sim: LV 15.2, DEN 25.6. DEN wins 78.6%, LV wins 21.4%. Median margin +10.6 for DEN.

| Team stat | LV | DEN |
|---|---|---|
| Plays | 60 | 61 |
| Pass attempts / completions | 35 / 22 | 32 / 20 |
| Passing yards | 229 | 216 |
| Rush attempts / yards | 22 / 78 | 27 / 115 |
| Sacks taken | 2.9 | 2.5 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.0 / 0.6 | 1.6 / 1.1 |
| Field goals | 1.2 | 1.9 |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Fernando Mendoza | 15.7 | 229 pass yd, 1.0 TD, 0.8 INT; 2.3 rush, 9 yd |  |
| RB | Ashton Jeanty | 12.5 | 10.2 car, 34 yd, 0.23 TD; 4.0 rec, 32 yd, 0.13 TD |  |
| RB | Mike Washington Jr. | 4.3 | 7.7 car, 28 yd, 0.15 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| RB | Dylan Laube | 0.9 | 0.4 car, 2 yd, 0.05 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 7.7 | 3.0 rec, 37 yd, 0.16 TD |  |
| WR | Jalen Nailor | 3.7 | 1.8 rec, 14 yd, 0.08 TD |  |
| WR | Jack Bech | 2.9 | 1.4 rec, 12 yd, 0.06 TD |  |
| WR | Cody White | 2.6 | 1.0 rec, 11 yd, 0.08 TD |  |
| TE | Brock Bowers | 8.9 | 4.9 rec, 53 yd, 0.28 TD | Questionable |
| TE | Michael Mayer | 7.1 | 3.5 rec, 32 yd, 0.08 TD |  |
| K | Matt Gay | 6.4 | 1.9 FG, 1.5 XP | Questionable |
| DL | Maxx Crosby | 4.9 | 2.3 solo, 1.7 ast, 0.51 sack, 0.06 PD, 0.00 INT |  |
| DL | Kwity Paye | 2.4 | 0.8 solo, 1.8 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 8.8 | 4.3 solo, 6.3 ast, 0.08 sack, 0.17 PD, 0.10 INT |  |
| LB | Quay Walker | 6.6 | 3.1 solo, 5.0 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| LB | Tommy Eichenberg | 2.7 | 1.6 solo, 2.0 ast, 0.00 sack, 0.16 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 7.1 | 4.4 solo, 2.9 ast, 0.06 sack, 0.19 PD, 0.11 INT |  |
| DB | Treydan Stukes | 4.9 | 2.8 solo, 2.3 ast, 0.00 sack, 0.42 PD, 0.20 INT |  |
| DB | Eric Stokes | 3.8 | 2.4 solo, 1.3 ast, 0.05 sack, 0.44 PD, 0.00 INT |  |

**DEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bo Nix | 20.6 | 216 pass yd, 1.6 TD, 0.5 INT; 4.9 rush, 21 yd |  |
| RB | Jonah Coleman | 11.6 | 9.5 car, 42 yd, 0.46 TD; 2.2 rec, 22 yd, 0.07 TD |  |
| RB | J.K. Dobbins | 8.3 | 10.9 car, 42 yd, 0.41 TD; 0.9 rec, 6 yd, 0.03 TD |  |
| WR | Courtland Sutton | 9.0 | 3.5 rec, 37 yd, 0.33 TD |  |
| WR | Jaylen Waddle | 8.9 | 3.4 rec, 36 yd, 0.29 TD |  |
| WR | Pat Bryant | 6.2 | 2.1 rec, 25 yd, 0.26 TD |  |
| WR | Marvin Mims Jr. | 4.0 | 0.8 car, 4 yd, 0.02 TD; 1.7 rec, 15 yd, 0.06 TD |  |
| TE | Evan Engram | 4.9 | 2.1 rec, 20 yd, 0.12 TD |  |
| TE | Nate Adkins | 2.5 | 0.6 rec, 5 yd, 0.22 TD |  |
| K | Wil Lutz | 9.4 | 1.8 FG, 2.6 XP |  |
| DL | Malcolm Roach | 3.9 | 1.5 solo, 1.2 ast, 0.51 sack, 0.33 PD, 0.00 INT |  |
| DL | Zach Allen | 3.3 | 0.9 solo, 1.6 ast, 0.37 sack, 0.34 PD, 0.00 INT |  |
| LB | Alex Singleton | 8.7 | 4.9 solo, 5.6 ast, 0.26 sack, 0.24 PD, 0.00 INT |  |
| LB | Nik Bonitto | 4.4 | 1.4 solo, 0.6 ast, 0.58 sack, 0.04 PD, 0.00 INT |  |
| LB | Justin Strnad | 4.0 | 2.0 solo, 2.3 ast, 0.10 sack, 0.38 PD, 0.00 INT |  |
| DB | Ja'Quan McMillian | 6.0 | 2.7 solo, 1.2 ast, 0.37 sack, 0.83 PD, 0.16 INT |  |
| DB | Talanoa Hufanga | 4.2 | 1.7 solo, 1.0 ast, 0.10 sack, 0.35 PD, 0.20 INT |  |
| DB | Brandon Jones | 4.1 | 3.2 solo, 2.1 ast, 0.00 sack, 0.51 PD, 0.17 INT | Questionable |

### MIA @ BUF

Market: BUF -16.5, total 44.5. Sim: MIA 14.2, BUF 30.6. BUF wins 89.5%, MIA wins 10.5%. Median margin +16.6 for BUF.

| Team stat | MIA | BUF |
|---|---|---|
| Plays | 59 | 63 |
| Pass attempts / completions | 32 / 19 | 29 / 19 |
| Passing yards | 215 | 241 |
| Rush attempts / yards | 25 / 105 | 31 / 145 |
| Sacks taken | 2.1 | 2.0 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 0.8 / 0.7 | 1.6 / 1.8 |
| Field goals | 1.1 | 2.3 |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kyle McCord | 14.8 | 215 pass yd, 0.8 TD, 0.7 INT; 2.2 rush, 10 yd |  |
| RB | Ollie Gordon II | 10.4 | 15.1 car, 63 yd, 0.29 TD; 1.3 rec, 10 yd, 0.02 TD |  |
| RB | Jaylen Wright | 3.5 | 4.9 car, 19 yd, 0.08 TD; 0.6 rec, 6 yd, 0.01 TD |  |
| RB | Kaytron Allen | 1.6 | 0.9 car, 4 yd, 0.01 TD; 0.5 rec, 6 yd, 0.01 TD |  |
| WR | Caleb Douglas | 9.4 | 3.7 rec, 47 yd, 0.17 TD |  |
| WR | Malik Washington | 8.6 | 1.0 car, 5 yd, 0.02 TD; 3.8 rec, 35 yd, 0.12 TD |  |
| WR | Chris Bell | 4.0 | 1.8 rec, 18 yd, 0.04 TD |  |
| WR | Kevin Coleman Jr. | 4.0 | 1.6 rec, 15 yd, 0.14 TD |  |
| TE | Greg Dulcich | 6.5 | 3.1 rec, 31 yd, 0.07 TD |  |
| TE | Will Kacmarek | 1.6 | 0.8 rec, 7 yd, 0.02 TD |  |
| DL | Rodney McGraw | 1.2 | 0.4 solo, 1.6 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DL | Malik Herring | 1.2 | 0.4 solo, 0.7 ast, 0.12 sack, 0.00 PD, 0.00 INT |  |
| LB | Jordyn Brooks | 7.7 | 4.4 solo, 5.2 ast, 0.03 sack, 0.28 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 6.8 | 3.7 solo, 4.3 ast, 0.13 sack, 0.07 PD, 0.07 INT |  |
| LB | Joshua Uche | 4.5 | 2.2 solo, 2.0 ast, 0.33 sack, 0.13 PD, 0.00 INT |  |
| DB | Chris Johnson | 6.1 | 2.4 solo, 2.2 ast, 0.00 sack, 0.40 PD, 0.29 INT |  |
| DB | Michael Taaffe | 5.8 | 3.0 solo, 2.8 ast, 0.00 sack, 0.30 PD, 0.30 INT |  |
| DB | Julius Brents | 3.1 | 1.9 solo, 1.6 ast, 0.00 sack, 0.09 PD, 0.00 INT |  |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 23.7 | 241 pass yd, 1.6 TD, 0.7 INT; 6.1 rush, 27 yd |  |
| RB | James Cook | 16.6 | 17.7 car, 85 yd, 0.91 TD; 1.2 rec, 12 yd, 0.06 TD |  |
| RB | Ty Johnson | 5.7 | 1.7 car, 7 yd, 0.08 TD; 2.0 rec, 21 yd, 0.09 TD |  |
| RB | Ray Davis | 2.7 | 2.6 car, 12 yd, 0.07 TD; 0.4 rec, 5 yd, 0.04 TD |  |
| WR | DJ Moore | 9.8 | 0.6 car, 3 yd, 0.02 TD; 3.0 rec, 43 yd, 0.36 TD |  |
| WR | Khalil Shakir | 9.1 | 3.6 rec, 42 yd, 0.20 TD |  |
| WR | Keon Coleman | 6.6 | 2.4 rec, 28 yd, 0.23 TD |  |
| WR | Gabe Davis | 1.2 | 0.6 rec, 6 yd, 0.07 TD | Questionable |
| TE | Dawson Knox | 4.4 | 1.9 rec, 16 yd, 0.15 TD |  |
| TE | Dalton Kincaid | 2.1 | 3.1 rec, 40 yd, 0.21 TD | Questionable |
| K | Tyler Bass | 10.7 | 2.0 FG, 3.1 XP |  |
| DL | Deone Walker | 2.4 | 1.0 solo, 1.8 ast, 0.05 sack, 0.41 PD, 0.00 INT |  |
| DL | Landon Jackson | 1.9 | 0.8 solo, 1.2 ast, 0.15 sack, 0.09 PD, 0.00 INT |  |
| LB | Terrel Bernard | 5.3 | 2.8 solo, 3.4 ast, 0.00 sack, 0.32 PD, 0.13 INT |  |
| LB | Greg Rousseau | 5.2 | 1.3 solo, 0.8 ast, 0.70 sack, 0.73 PD, 0.00 INT |  |
| LB | TJ Parker | 4.0 | 1.3 solo, 1.9 ast, 0.53 sack, 0.00 PD, 0.00 INT |  |
| DB | Amani Hooker | 6.2 | 3.8 solo, 2.8 ast, 0.00 sack, 0.94 PD, 0.00 INT |  |
| DB | Cole Bishop | 4.9 | 3.2 solo, 2.1 ast, 0.11 sack, 0.19 PD, 0.00 INT |  |
| DB | Davison Igbinosun | 4.6 | 1.7 solo, 1.6 ast, 0.00 sack, 1.29 PD, 0.29 INT |  |

### MIN @ SF

Market: SF -3.5, total 46.5. Sim: MIN 21.6, SF 25.0. SF wins 60.2%, MIN wins 39.8%. Median margin +3.4 for SF.

| Team stat | MIN | SF |
|---|---|---|
| Plays | 59 | 61 |
| Pass attempts / completions | 33 / 20 | 30 / 21 |
| Passing yards | 217 | 223 |
| Rush attempts / yards | 24 / 98 | 28 / 129 |
| Sacks taken | 1.9 | 3.5 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.5 / 0.8 | 1.5 / 1.3 |
| Field goals | 1.6 | 1.9 |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 17.6 | 217 pass yd, 1.5 TD, 0.7 INT; 2.2 rush, 9 yd |  |
| RB | Aaron Jones | 11.6 | 11.2 car, 44 yd, 0.51 TD; 2.2 rec, 16 yd, 0.07 TD |  |
| RB | Jordan Mason | 6.1 | 8.3 car, 34 yd, 0.24 TD; 0.6 rec, 6 yd, 0.03 TD |  |
| RB | DeeJay Dallas | 1.1 | 0.3 car, 1 yd, 0.00 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Justin Jefferson | 15.5 | 6.3 rec, 65 yd, 0.45 TD |  |
| WR | Myles Price | 3.7 | 1.4 rec, 13 yd, 0.15 TD |  |
| WR | Tai Felton | 3.0 | 1.3 rec, 14 yd, 0.05 TD |  |
| WR | Jauan Jennings | 2.4 | 1.1 rec, 11 yd, 0.04 TD |  |
| TE | T.J. Hockenson | 10.7 | 4.4 rec, 41 yd, 0.38 TD |  |
| TE | Gavin Bartholomew | 5.8 | 2.2 rec, 21 yd, 0.27 TD |  |
| K | Will Reichard | 10.4 | 2.2 FG, 2.2 XP |  |
| DL | Jalen Redmond | 3.9 | 1.7 solo, 1.4 ast, 0.30 sack, 0.42 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 3.1 | 1.3 solo, 1.3 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| LB | Blake Cashman | 9.2 | 4.6 solo, 4.8 ast, 0.43 sack, 0.75 PD, 0.00 INT |  |
| LB | Andrew Van Ginkel | 6.6 | 1.8 solo, 1.5 ast, 0.86 sack, 0.24 PD, 0.09 INT |  |
| LB | Eric Wilson | 6.4 | 3.3 solo, 3.1 ast, 0.43 sack, 0.06 PD, 0.00 INT |  |
| DB | Byron Murphy | 5.6 | 3.0 solo, 1.2 ast, 0.00 sack, 0.66 PD, 0.40 INT |  |
| DB | Josh Metellus | 5.4 | 3.4 solo, 3.3 ast, 0.03 sack, 0.31 PD, 0.00 INT |  |
| DB | James Pierre | 4.2 | 2.9 solo, 0.4 ast, 0.00 sack, 0.50 PD, 0.20 INT |  |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 19.1 | 223 pass yd, 1.5 TD, 0.7 INT; 3.8 rush, 19 yd |  |
| RB | Christian McCaffrey | 16.6 | 12.0 car, 53 yd, 0.63 TD; 3.2 rec, 31 yd, 0.23 TD |  |
| RB | Kaelon Black | 6.2 | 7.7 car, 36 yd, 0.28 TD; 0.5 rec, 4 yd, 0.02 TD |  |
| RB | Kyle Juszczyk | 2.1 | 0.1 car, 1 yd, 0.00 TD; 0.8 rec, 7 yd, 0.10 TD |  |
| WR | Keenan Allen | 8.1 | 3.7 rec, 36 yd, 0.14 TD |  |
| WR | Deebo Samuel Sr. | 6.0 | 1.5 car, 9 yd, 0.11 TD; 1.7 rec, 17 yd, 0.19 TD |  |
| WR | Mike Evans | 5.0 | 2.6 rec, 31 yd, 0.18 TD | Questionable |
| WR | Jordan Watkins | 4.6 | 1.6 rec, 23 yd, 0.11 TD |  |
| TE | George Kittle | 9.3 | 3.9 rec, 39 yd, 0.26 TD |  |
| TE | Luke Farrell | 0.6 | 0.3 rec, 3 yd, 0.01 TD |  |
| K | Eddy Pineiro | 7.3 | 1.3 FG, 2.6 XP |  |
| DL | Mykel Williams | 2.3 | 0.8 solo, 1.1 ast, 0.33 sack, 0.00 PD, 0.00 INT |  |
| DL | Osa Odighizuwa | 2.1 | 0.7 solo, 1.5 ast, 0.21 sack, 0.08 PD, 0.00 INT |  |
| LB | Fred Warner | 7.8 | 3.8 solo, 5.1 ast, 0.03 sack, 0.24 PD, 0.00 INT |  |
| LB | Jaden Dugger | 5.6 | 3.2 solo, 1.0 ast, 0.11 sack, 0.15 PD, 0.15 INT |  |
| LB | Dre Greenlaw | 4.7 | 3.6 solo, 3.8 ast, 0.09 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | Renardo Green | 5.0 | 2.7 solo, 1.2 ast, 0.00 sack, 0.71 PD, 0.35 INT |  |
| DB | Malik Mustapha | 4.9 | 2.4 solo, 1.6 ast, 0.00 sack, 0.72 PD, 0.26 INT |  |
| DB | Ji'Ayir Brown | 4.4 | 2.9 solo, 2.1 ast, 0.00 sack, 0.33 PD, 0.00 INT |  |

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
| WR | Jordyn Tyson | 11.9 | 6.1 rec, 51 yd, 0.13 TD |  |
| WR | Chris Olave | 11.9 | 4.8 rec, 58 yd, 0.22 TD |  |
| WR | Devaughn Vele | 6.5 | 2.8 rec, 29 yd, 0.15 TD |  |
| WR | Bryce Lance | 2.1 | 0.9 rec, 8 yd, 0.07 TD |  |
| TE | Juwan Johnson | 6.2 | 2.5 rec, 28 yd, 0.16 TD |  |
| TE | Noah Fant | 2.5 | 1.0 rec, 9 yd, 0.10 TD |  |
| K | Charlie Smyth | 7.7 | 1.5 FG, 1.9 XP |  |
| DL | Carl Granderson | 6.6 | 2.0 solo, 2.7 ast, 0.98 sack, 0.21 PD, 0.04 INT |  |
| DL | Chase Young | 5.5 | 1.3 solo, 1.4 ast, 0.87 sack, 0.38 PD, 0.00 INT |  |
| LB | Kaden Elliss | 8.0 | 4.5 solo, 4.3 ast, 0.39 sack, 0.29 PD, 0.00 INT |  |
| LB | Danny Stutsman | 4.2 | 2.9 solo, 2.5 ast, 0.00 sack, 0.10 PD, 0.00 INT |  |
| LB | Cameron Jordan | 2.6 | 1.4 solo, 1.0 ast, 0.18 sack, 0.03 PD, 0.00 INT |  |
| DB | Jonas Sanker | 5.3 | 3.4 solo, 2.1 ast, 0.00 sack, 0.56 PD, 0.03 INT |  |
| DB | Julian Blackmon | 4.6 | 2.7 solo, 2.3 ast, 0.00 sack, 0.19 PD, 0.18 INT |  |
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
| WR | Jahdae Walker | 1.5 | 0.4 rec, 4 yd, 0.11 TD |  |
| TE | Colston Loveland | 11.1 | 4.6 rec, 42 yd, 0.39 TD |  |
| TE | Sam Roush | 1.4 | 0.6 rec, 6 yd, 0.02 TD |  |
| K | Cairo Santos | 9.4 | 1.7 FG, 3.1 XP |  |
| DL | Jeffery Simmons | 8.4 | 3.1 solo, 2.0 ast, 1.09 sack, 1.08 PD, 0.00 INT |  |
| DL | Austin Booker | 5.4 | 2.3 solo, 1.1 ast, 0.63 sack, 0.27 PD, 0.00 INT |  |
| LB | Devin Bush | 6.6 | 3.5 solo, 2.8 ast, 0.26 sack, 0.46 PD, 0.00 INT |  |
| LB | T.J. Edwards | 4.1 | 2.3 solo, 1.3 ast, 0.02 sack, 0.36 PD, 0.13 INT |  |
| LB | D'Marco Jackson | 2.5 | 1.1 solo, 1.3 ast, 0.03 sack, 0.19 PD, 0.16 INT |  |
| DB | Dillon Thieneman | 5.9 | 3.2 solo, 2.9 ast, 0.20 sack, 0.48 PD, 0.08 INT |  |
| DB | Jaylon Johnson | 4.9 | 2.4 solo, 0.8 ast, 0.00 sack, 0.45 PD, 0.20 INT |  |
| DB | Cam Lewis | 4.6 | 3.0 solo, 1.3 ast, 0.00 sack, 0.38 PD, 0.20 INT |  |

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
| QB | Geno Smith | 16.9 | 249 pass yd, 1.3 TD, 0.8 INT; 1.5 rush, 6 yd |  |
| RB | Braelon Allen | 11.0 | 10.2 car, 47 yd, 0.39 TD; 2.1 rec, 16 yd, 0.06 TD |  |
| RB | Breece Hall | 9.3 | 8.0 car, 31 yd, 0.22 TD; 2.2 rec, 25 yd, 0.05 TD |  |
| RB | Isaiah Davis | 2.3 | 1.6 car, 6 yd, 0.05 TD; 0.6 rec, 7 yd, 0.02 TD |  |
| WR | Garrett Wilson | 14.5 | 5.6 rec, 69 yd, 0.34 TD |  |
| WR | Adonai Mitchell | 8.7 | 2.9 rec, 42 yd, 0.27 TD |  |
| WR | Tim Patrick | 2.1 | 0.9 rec, 10 yd, 0.03 TD |  |
| TE | Mason Taylor | 7.2 | 3.0 rec, 26 yd, 0.27 TD |  |
| TE | Kenyon Sadiq | 5.4 | 2.2 rec, 23 yd, 0.11 TD |  |
| K | Jason Sanders | 10.6 | 2.3 FG, 2.0 XP |  |
| DL | Will McDonald IV | 3.4 | 0.9 solo, 1.0 ast, 0.46 sack, 0.00 PD, 0.00 INT |  |
| DL | Darrell Jackson Jr. | 2.8 | 1.3 solo, 2.2 ast, 0.08 sack, 0.17 PD, 0.00 INT |  |
| LB | David Bailey | 7.5 | 2.6 solo, 2.0 ast, 0.76 sack, 0.42 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.5 | 4.2 solo, 4.7 ast, 0.03 sack, 0.38 PD, 0.00 INT |  |
| LB | Demario Davis | 6.2 | 3.5 solo, 3.2 ast, 0.14 sack, 0.37 PD, 0.00 INT |  |
| DB | Dane Belton | 7.1 | 4.2 solo, 4.3 ast, 0.09 sack, 0.52 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 6.4 | 3.6 solo, 3.8 ast, 0.00 sack, 0.34 PD, 0.09 INT |  |
| DB | Azareye'h Thomas | 4.4 | 2.0 solo, 2.8 ast, 0.00 sack, 0.58 PD, 0.16 INT |  |

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
| TE | Charlie Kolar | 3.7 | 2.2 rec, 22 yd, 0.08 TD | Questionable |
| K | Cameron Dicker | 9.9 | 2.0 FG, 2.3 XP |  |
| DL | Dalvin Tomlinson | 3.3 | 1.2 solo, 1.1 ast, 0.50 sack, 0.00 PD, 0.00 INT |  |
| DL | Justin Eboigbe | 2.4 | 1.0 solo, 1.6 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Del'Shawn Phillips | 4.4 | 2.2 solo, 3.0 ast, 0.05 sack, 0.14 PD, 0.15 INT |  |
| LB | Tuli Tuipulotu | 4.3 | 1.5 solo, 1.5 ast, 0.35 sack, 0.22 PD, 0.08 INT |  |
| LB | Troy Dye | 3.3 | 1.7 solo, 0.9 ast, 0.13 sack, 0.19 PD, 0.00 INT |  |
| DB | Tony Jefferson | 4.4 | 2.7 solo, 2.1 ast, 0.06 sack, 0.18 PD, 0.03 INT |  |
| DB | Cam Hart | 4.2 | 2.1 solo, 1.5 ast, 0.00 sack, 0.81 PD, 0.19 INT |  |
| DB | Elijah Molden | 4.0 | 2.4 solo, 1.8 ast, 0.00 sack, 0.22 PD, 0.05 INT |  |

### PIT @ PHI

Market: PHI +3.5, total 37.5. Sim: PIT 20.7, PHI 17.3. PHI wins 39.9%, PIT wins 60.1%. Median margin -3.5 for PHI.

| Team stat | PIT | PHI |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 34 / 21 | 32 / 19 |
| Passing yards | 212 | 204 |
| Rush attempts / yards | 27 / 122 | 27 / 104 |
| Sacks taken | 2.6 | 2.6 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.9 | 0.9 / 1.0 |
| Field goals | 1.5 | 1.3 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 16.2 | 212 pass yd, 1.4 TD, 0.6 INT; 1.4 rush, 6 yd |  |
| RB | Jaylen Warren | 16.7 | 13.5 car, 67 yd, 0.41 TD; 3.6 rec, 31 yd, 0.16 TD |  |
| RB | Rico Dowdle | 8.9 | 7.2 car, 30 yd, 0.28 TD; 2.3 rec, 16 yd, 0.06 TD |  |
| RB | Lew Nichols III | 1.2 | 1.6 car, 8 yd, 0.03 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | DK Metcalf | 11.0 | 4.4 rec, 49 yd, 0.30 TD |  |
| WR | Germie Bernard | 9.6 | 4.6 rec, 38 yd, 0.20 TD |  |
| WR | Ben Skowronek | 1.3 | 0.5 rec, 4 yd, 0.06 TD |  |
| TE | Pat Freiermuth | 8.8 | 3.2 rec, 31 yd, 0.30 TD |  |
| TE | Darnell Washington | 6.6 | 2.5 rec, 27 yd, 0.22 TD |  |
| K | Chris Boswell | 9.3 | 1.9 FG, 2.1 XP |  |
| DL | Cameron Heyward | 4.2 | 1.6 solo, 1.9 ast, 0.33 sack, 0.44 PD, 0.00 INT |  |
| DL | Keeanu Benton | 2.9 | 1.1 solo, 1.5 ast, 0.10 sack, 0.44 PD, 0.00 INT |  |
| LB | Payton Wilson | 7.9 | 4.7 solo, 4.3 ast, 0.10 sack, 0.26 PD, 0.11 INT |  |
| LB | Patrick Queen | 5.9 | 3.3 solo, 5.1 ast, 0.44 sack, 0.36 PD, 0.06 INT | Questionable |
| LB | T.J. Watt | 5.4 | 1.5 solo, 0.7 ast, 0.70 sack, 0.50 PD, 0.10 INT |  |
| DB | Jalen Ramsey | 5.5 | 3.1 solo, 2.3 ast, 0.22 sack, 0.21 PD, 0.00 INT |  |
| DB | Jaquan Brisker | 5.4 | 3.0 solo, 4.0 ast, 0.00 sack, 0.26 PD, 0.06 INT |  |
| DB | Jamel Dean | 5.3 | 2.6 solo, 1.2 ast, 0.00 sack, 1.10 PD, 0.12 INT |  |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Milton III | 16.1 | 204 pass yd, 0.9 TD, 0.7 INT; 7.5 rush, 33 yd |  |
| RB | Saquon Barkley | 7.5 | 8.6 car, 33 yd, 0.44 TD; 0.8 rec, 7 yd, 0.02 TD |  |
| RB | Dameon Pierce | 5.8 | 9.1 car, 31 yd, 0.38 TD; 1.4 rec, 9 yd, 0.03 TD | Questionable |
| RB | Jaydon Blue | 0.6 | 0.0 car, 0 yd, 0.00 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | Makai Lemon | 8.6 | 4.2 rec, 36 yd, 0.15 TD |  |
| WR | DeVonta Smith | 8.0 | 3.4 rec, 36 yd, 0.17 TD |  |
| WR | Darius Cooper | 4.7 | 1.7 rec, 20 yd, 0.16 TD |  |
| WR | Marquise Brown | 2.2 | 1.0 rec, 11 yd, 0.02 TD |  |
| TE | Dallas Goedert | 8.3 | 3.8 rec, 34 yd, 0.17 TD |  |
| TE | Eli Stowers | 2.2 | 1.0 rec, 12 yd, 0.02 TD |  |
| K | Jake Elliott | 6.4 | 1.2 FG, 1.8 XP |  |
| DL | Jalen Carter | 5.1 | 1.1 solo, 1.6 ast, 0.62 sack, 0.41 PD, 0.00 INT |  |
| DL | Byron Young | 2.1 | 0.8 solo, 1.8 ast, 0.09 sack, 0.00 PD, 0.00 INT |  |
| LB | Jeremiah Trotter Jr. | 6.0 | 3.9 solo, 3.0 ast, 0.06 sack, 0.09 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 4.8 | 3.0 solo, 2.5 ast, 0.06 sack, 0.06 PD, 0.00 INT |  |
| LB | Nolan Smith | 3.4 | 1.1 solo, 1.0 ast, 0.59 sack, 0.07 PD, 0.00 INT |  |
| DB | Andrew Mukuba | 5.8 | 3.9 solo, 2.2 ast, 0.00 sack, 0.25 PD, 0.09 INT |  |
| DB | Cooper DeJean | 5.3 | 3.3 solo, 2.1 ast, 0.00 sack, 0.61 PD, 0.11 INT |  |
| DB | Riq Woolen | 4.8 | 3.1 solo, 0.7 ast, 0.00 sack, 1.04 PD, 0.00 INT |  |

### TB @ DET

Market: DET -4.5, total 46.0. Sim: TB 20.8, DET 25.2. DET wins 63.5%, TB wins 36.5%. Median margin +4.5 for DET.

| Team stat | TB | DET |
|---|---|---|
| Plays | 63 | 65 |
| Pass attempts / completions | 32 / 20 | 34 / 23 |
| Passing yards | 206 | 266 |
| Rush attempts / yards | 28 / 137 | 28 / 122 |
| Sacks taken | 2.8 | 2.1 |
| Interceptions thrown | 0.8 | 0.9 |
| Passing / rushing TDs | 1.3 / 1.0 | 1.6 / 1.1 |
| Field goals | 1.6 | 1.9 |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Baker Mayfield | 11.7 | 154 pass yd, 0.9 TD, 0.6 INT; 1.8 rush, 9 yd | Questionable |
| RB | Bucky Irving | 15.6 | 14.7 car, 70 yd, 0.57 TD; 2.6 rec, 17 yd, 0.17 TD |  |
| RB | Kenny Gainwell | 8.7 | 6.1 car, 31 yd, 0.11 TD; 2.0 rec, 20 yd, 0.16 TD |  |
| RB | Sean Tucker | 1.7 | 1.8 car, 9 yd, 0.15 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Emeka Egbuka | 9.8 | 4.0 rec, 37 yd, 0.28 TD |  |
| WR | Chris Godwin Jr. | 8.5 | 4.0 rec, 35 yd, 0.16 TD |  |
| WR | Tez Johnson | 5.4 | 1.7 rec, 27 yd, 0.16 TD |  |
| WR | Ted Hurst III | 4.7 | 1.7 rec, 20 yd, 0.16 TD |  |
| TE | Cade Otton | 7.2 | 3.4 rec, 30 yd, 0.14 TD |  |
| K | Chase McLaughlin | 10.1 | 2.1 FG, 2.1 XP |  |
| DL | A'Shawn Robinson | 2.7 | 0.5 solo, 2.0 ast, 0.07 sack, 0.36 PD, 0.20 INT |  |
| DL | Vita Vea | 2.2 | 1.0 solo, 1.2 ast, 0.14 sack, 0.17 PD, 0.00 INT |  |
| LB | Josiah Trotter | 7.8 | 4.3 solo, 4.7 ast, 0.07 sack, 0.34 PD, 0.06 INT |  |
| LB | Alex Anzalone | 6.0 | 2.1 solo, 2.5 ast, 0.08 sack, 0.60 PD, 0.60 INT |  |
| LB | David Walker | 3.9 | 1.9 solo, 1.3 ast, 0.45 sack, 0.00 PD, 0.00 INT |  |
| DB | Jacob Parrish | 6.7 | 3.8 solo, 0.9 ast, 0.00 sack, 1.55 PD, 0.26 INT |  |
| DB | Zyon McCollum | 6.3 | 2.7 solo, 0.8 ast, 0.00 sack, 1.16 PD, 0.60 INT |  |
| DB | Tykee Smith | 5.3 | 2.7 solo, 2.7 ast, 0.00 sack, 0.35 PD, 0.26 INT |  |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 19.4 | 266 pass yd, 1.6 TD, 0.9 INT; 1.9 rush, 7 yd |  |
| RB | Jahmyr Gibbs | 23.0 | 19.2 car, 86 yd, 0.91 TD; 4.1 rec, 38 yd, 0.21 TD |  |
| RB | Sione Vaki | 2.5 | 3.4 car, 15 yd, 0.08 TD; 0.6 rec, 6 yd, 0.02 TD | Questionable |
| WR | Amon-Ra St. Brown | 17.3 | 6.8 rec, 76 yd, 0.49 TD |  |
| WR | Jameson Williams | 10.8 | 3.7 rec, 51 yd, 0.34 TD |  |
| WR | Isaac TeSlaa | 4.8 | 1.6 rec, 21 yd, 0.18 TD |  |
| TE | Sam LaPorta | 8.7 | 3.5 rec, 38 yd, 0.23 TD |  |
| TE | Brock Wright | 1.6 | 0.8 rec, 7 yd, 0.03 TD |  |
| K | Jake Bates | 9.3 | 1.8 FG, 2.6 XP |  |
| DL | DJ Wonnum | 4.2 | 1.4 solo, 1.0 ast, 0.68 sack, 0.07 PD, 0.00 INT |  |
| DL | Derrick Moore | 4.0 | 1.3 solo, 0.5 ast, 0.81 sack, 0.00 PD, 0.00 INT |  |
| LB | K.J. Britt | 4.6 | 4.1 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Derrick Barnes | 4.5 | 2.7 solo, 1.7 ast, 0.19 sack, 0.16 PD, 0.07 INT |  |
| LB | Malcolm Rodriguez | 2.9 | 1.4 solo, 2.4 ast, 0.04 sack, 0.12 PD, 0.00 INT |  |
| DB | Chuck Clark | 6.3 | 3.5 solo, 2.0 ast, 0.08 sack, 0.33 PD, 0.21 INT |  |
| DB | Roger McCreary | 6.1 | 3.4 solo, 1.3 ast, 0.07 sack, 1.20 PD, 0.17 INT |  |
| DB | D.J. Reed | 3.9 | 3.2 solo, 1.4 ast, 0.00 sack, 0.84 PD, 0.16 INT | Questionable |

### TEN @ DAL

Market: DAL -7.5, total 55.0. Sim: TEN 23.8, DAL 31.2. DAL wins 71.3%, TEN wins 28.7%. Median margin +7.5 for DAL.

| Team stat | TEN | DAL |
|---|---|---|
| Plays | 60 | 66 |
| Pass attempts / completions | 35 / 22 | 35 / 22 |
| Passing yards | 244 | 275 |
| Rush attempts / yards | 23 / 111 | 28 / 115 |
| Sacks taken | 2.4 | 2.5 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.7 / 0.9 | 2.0 / 1.4 |
| Field goals | 1.8 | 2.3 |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 20.6 | 244 pass yd, 1.7 TD, 0.6 INT; 2.8 rush, 15 yd |  |
| RB | Tony Pollard | 17.7 | 15.1 car, 73 yd, 0.67 TD; 3.0 rec, 23 yd, 0.23 TD |  |
| RB | Tyjae Spears | 5.0 | 3.2 car, 15 yd, 0.09 TD; 2.5 rec, 16 yd, 0.07 TD | Questionable |
| RB | Nicholas Singleton | 0.6 | 1.1 car, 5 yd, 0.02 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Carnell Tate | 9.5 | 5.0 rec, 57 yd, 0.36 TD | Questionable |
| WR | Elic Ayomanor | 8.3 | 3.0 rec, 40 yd, 0.24 TD |  |
| WR | Chimere Dike | 6.3 | 2.3 rec, 24 yd, 0.25 TD |  |
| WR | Calvin Ridley | 2.9 | 1.2 rec, 14 yd, 0.05 TD |  |
| TE | Gunnar Helm | 6.3 | 2.9 rec, 27 yd, 0.13 TD |  |
| TE | Daniel Bellinger | 4.5 | 1.6 rec, 14 yd, 0.24 TD |  |
| K | Joey Slye | 9.0 | 1.7 FG, 2.4 XP |  |
| DL | Jacob Martin | 4.9 | 1.4 solo, 0.4 ast, 1.02 sack, 0.23 PD, 0.00 INT |  |
| DL | Jermaine Johnson II | 3.2 | 1.8 solo, 0.9 ast, 0.34 sack, 0.00 PD, 0.00 INT |  |
| LB | Cedric Gray | 6.1 | 3.7 solo, 2.9 ast, 0.05 sack, 0.31 PD, 0.16 INT |  |
| LB | Anthony Hill Jr. | 6.0 | 4.8 solo, 5.3 ast, 0.00 sack, 0.29 PD, 0.00 INT | Questionable |
| LB | Cody Barton | 3.0 | 1.7 solo, 2.3 ast, 0.00 sack, 0.21 PD, 0.00 INT |  |
| DB | Kevin Winston Jr. | 5.9 | 3.8 solo, 3.0 ast, 0.00 sack, 0.07 PD, 0.00 INT |  |
| DB | Joshua Williams | 5.3 | 3.6 solo, 2.4 ast, 0.00 sack, 0.42 PD, 0.00 INT |  |
| DB | Cordale Flott | 5.1 | 2.8 solo, 1.5 ast, 0.00 sack, 0.64 PD, 0.28 INT |  |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 24.0 | 275 pass yd, 2.0 TD, 0.7 INT; 3.8 rush, 16 yd |  |
| RB | Javonte Williams | 18.9 | 21.9 car, 87 yd, 1.09 TD; 1.9 rec, 14 yd, 0.10 TD |  |
| RB | Hunter Luepke | 2.0 | 1.3 car, 6 yd, 0.03 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | CeeDee Lamb | 20.5 | 7.5 rec, 89 yd, 0.69 TD |  |
| WR | George Pickens | 16.1 | 5.4 rec, 71 yd, 0.60 TD |  |
| WR | Ryan Flournoy | 10.7 | 3.9 rec, 47 yd, 0.35 TD |  |
| WR | KaVontae Turpin | 2.9 | 0.7 car, 3 yd, 0.07 TD; 0.8 rec, 10 yd, 0.06 TD |  |
| TE | Brevyn Spann-Ford | 4.0 | 1.7 rec, 19 yd, 0.07 TD |  |
| K | Brandon Aubrey | 10.2 | 1.9 FG, 3.2 XP |  |
| DL | Quinnen Williams | 6.6 | 2.8 solo, 2.0 ast, 0.65 sack, 0.12 PD, 0.03 INT |  |
| DL | Elijah Garcia | 3.0 | 1.0 solo, 1.9 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| LB | Shemar James | 4.9 | 3.0 solo, 2.0 ast, 0.02 sack, 0.12 PD, 0.12 INT |  |
| LB | Dee Winters | 4.0 | 2.6 solo, 1.6 ast, 0.00 sack, 0.12 PD, 0.12 INT |  |
| LB | DeMarvion Overshown | 3.8 | 1.7 solo, 2.1 ast, 0.00 sack, 0.30 PD, 0.15 INT |  |
| DB | Caleb Downs | 6.5 | 3.2 solo, 3.2 ast, 0.21 sack, 0.37 PD, 0.15 INT |  |
| DB | Malik Hooker | 3.7 | 2.5 solo, 1.5 ast, 0.00 sack, 0.42 PD, 0.00 INT |  |
| DB | Markquese Bell | 3.1 | 2.2 solo, 1.5 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: IND: Carl Lawson, IND: Alec Pierce, IND: Cameron Mitchell, IND: Charvarius Ward, IND: Daniel Jones, IND: Jalen Travis, IND: Cam Taylor-Britt, IND: Will Mallory, IND: Akeem Davis-Gaither, IND: Jaylon Carlies, IND: Jerry Tillery, IND: Mo Alie-Cox, IND: Bernhard Raimann, IND: Sauce Gardner, IND: Riley Leonard, HOU: Dare Ogunbowale, HOU: Brevin Jordan, HOU: George Odum, HOU: Jaylin Noel, HOU: Azeez Al-Shaair, HOU: Lewis Bond, HOU: E.J. Speed, HOU: Woody Marks, HOU: Kenneth Murray, Jr., HOU: Jayden Higgins, HOU: Jawhar Jordan, HOU: Jake Andrews, HOU: Sabastian Harsh, HOU: Danielle Hunter, HOU: Jaden Crumedy, HOU: Dylan Horton, HOU: Marvin Harrison Jr., HOU: Bryce Hall, HOU: Mario Edwards, HOU: British Brooks, MIA: Jamree Kromah, MIA: Bradley Pinion, MIA: Jalen Reagor, MIA: Jordan Phillips, MIA: Julian Hill, MIA: De'Von Achane, MIA: Carlos Washington, MIA: Zeek Biggers, MIA: Zane Gonzalez, MIA: Jared Wayne, MIA: Malik Willis, MIA: Ethan Bonner, MIA: Matthew Butler, MIA: Zach Sieler, MIA: Liam Anderson, BUF: Phidarian Mathis, BUF: Josh Palmer, BUF: Dorian Williams, BUF: Keonta Jenkins, BUF: Trent Sherfield, BUF: Christian Benford, BUF: Te'Cory Couch, BUF: Shaq Thompson, BUF: Geno Stone, BUF: Kani Walker, BUF: Tre'Davious White, BUF: Frank Gore Jr., BUF: Andre Jones Jr., BAL: Jovaughn Gwyn, BAL: Chris Moore, BAL: Tavius Robinson, BAL: Tyler Loop, BAL: Durham Smythe, BAL: Lamar Jackson, BAL: Tyler Huntley, BAL: Carl Jones, BAL: Marlon Humphrey, BAL: Nnamdi Madubuike, BAL: Jaylinn Hawkins, CAR: Thomas Incoom, CAR: Jaycee Horn, CAR: Ikem Ekwonu, CAR: Isaiah Simmons, CAR: Taylor Moton, CAR: David Moore, CAR: Nick Hampton, CAR: Claudin Cherelus, CAR: Corey Thornton, CAR: Jonathon Brooks, CAR: Nic Scourton, CAR: Ja'Seem Reed, CAR: LaBryan Ray, CAR: Cam Jackson, CAR: Akayleb Evans, CAR: Mike Jackson, CAR: Bobby Okereke, NO: Fadil Diggs, NO: Moliki Matavao, NO: Justin Reid, NO: Zamir White, NO: Kevin Austin Jr., NO: Jayden Price, NO: Dillon Radunz, NO: Jalen Cropper, NO: Mason Tipton, NO: Treyton Welch, NO: Martin Emerson, NO: Christen Miller, NO: Bryan Bresee, NO: Asim Richards, NO: Taliese Fuaga, NO: Jonah Williams, CHI: Nikola Kalinic, CHI: Kentavius Street, CHI: Zavier Scott, CHI: Cole Kmet, CHI: Kaden Davis, CHI: Braxton Jones, CHI: Dayo Odeyingbo, CHI: Brittain Brown, CHI: Buddy Johnson, CHI: Beau Gardner, CHI: Salvon Ahmed, CHI: Kyler Gordon, TEN: Kendell Brooks, TEN: Erick Hallett, TEN: Kalel Mullings, TEN: Michael Carter, TEN: Wan'Dale Robinson, TEN: Dominique Hampton, TEN: Jaylen Harrell, TEN: James Williams, TEN: Tommy Townsend, DAL: Jalen Thompson, DAL: Israel Abanikanda, DAL: Malik Davis, DAL: Jordan Hudson, DAL: Malachi Lawrence, DAL: Jake Ferguson, DAL: Curtis Robinson, DAL: P.J. Locke, DAL: Tyler Goodson, DAL: Tyler Booker, DAL: DaRon Bland, DAL: Jonathan Mingo, TB: Antoine Winfield Jr., TB: Jalen McMillan, TB: David Sills, TB: Christian Rozeboom, TB: Josh Hayes, TB: Josh Williams, DET: Jackson Meeks, DET: Devin White, DET: Avonte Maddox, DET: Tom Kennedy, DET: Anthony Lucas, DET: Jack Campbell, DET: Aidan Hutchinson, DET: Jimmy Rolder, DET: Thomas Harper, DET: Nick Whiteside, DET: Jabari Small, DET: Ben Bartch, ARI: Paris Johnson Jr., ARI: Jeremiyah Love, ARI: Jalen Brooks, ARI: Art Green, ARI: Zachary Carter, ARI: Jordan Burch, ARI: Jon Gaines II, ARI: Kendrick Bourne, ARI: Gardner Minshew, ARI: Kenny Yeboah, ARI: Zay Jones, ARI: Will Johnson, ARI: Michael Wilson, ARI: Andrew Wingard, KC: Jacob De Jesus, KC: Ethan Downs, KC: Kenneth Walker III, KC: Jaylon Moore, KC: Jared Wiley, KC: Tyquan Thornton, KC: L'Jarius Sneed, KC: Justin Watson, KC: Trey Smith, KC: Brashard Smith, KC: Nate Carter, KC: Cole Christiansen, JAX: Austin Trammell, JAX: Cam'Ron Silmon-Craig, JAX: DaVon Hamilton, JAX: Nick Mullens, JAX: Anton Harrison, JAX: Patrick Mekari, JAX: Eric Murray, JAX: Robert Hainsey, JAX: Austin Johnson, JAX: Caleb Ransaw, JAX: BJ Green II, NYG: Gunner Olszewski, NYG: Chandler Martin, NYG: Tyrone Tracy Jr., NYG: Chauncey Golston, NYG: Braxton Berrios, NYG: Rico Payton, NYG: Jaxson Dart, NYG: Dalen Cambre, NYG: Charlie Jones, NYG: Brian Burns, NYG: Dawuane Smoot, NYG: Roy Robertson-Harris, NYG: Raheem Layne, NYG: Nikko Reed, NYG: Tremaine Edmunds, NYJ: Max Mitchell, NYJ: Kingsley Jonathan, NYJ: Jamaal Pritchett, NYJ: Marcelino McCrary-Ball, NYJ: T'Vondre Sweat, NYJ: Omar Cooper Jr., NYJ: Mykal Walker, NYJ: David Onyemata, NYJ: Sterling Shepard, NYJ: Arian Smith, NYJ: Jordan Clark, NYJ: Isaiah Williams, NYJ: Samuel Womack, NYJ: Braiden McGregor, LAC: Alec Ingold, LAC: Patrick Herbert, LAC: Kendall Williamson, LAC: Branson Taylor, LAC: Daiyan Henley, LAC: Trevor Penning, LAC: Derwin James, LAC: Rodney Shelley, LAC: Da'Shawn Hand, LAC: Daniel Brunskill, LAC: Trey Pipkins, LAC: Rashawn Slater, LAC: Trey Lance, LV: Chigozie Anusiem, LV: Patrick Johnson, LV: Cian Slone, LV: Greedy Vance, LV: Tonka Hemingway, LV: Carter Runyon, LV: Deven Thompkins, DEN: Taylor Rapp, DEN: Michael Bandy, DEN: Tyler Badie, DEN: Jonah Elliss, DEN: RJ Harvey, DEN: Eyioma Uwazurike, DEN: Sean Fresch, DEN: Kolbe Katsis, DEN: Cody Schrader, PIT: Michael Pittman, PIT: Mason McCormick, PIT: Brandon Johnson, PIT: Sebastian Castro, PIT: Logan Lee, PIT: Brandon Smith, PIT: Roman Wilson, PIT: Sebastian Joseph-Day, PIT: Marquez Valdes-Scantling, PIT: Esezi Otomewo, PHI: Tank Bigsby, PHI: Andre' Sam, PHI: Cole Wisniewski, PHI: Keyshawn James-Newby, PHI: Chance Campbell, PHI: Elijah Mitchell, PHI: Zack Baun, PHI: Will Shipley, PHI: Jalen Hurts, PHI: Dontayvion Wicks, MIN: Josh Oliver, MIN: Tyler Batty, MIN: C.J. Ham, MIN: Jordan Addison, MIN: Bo Richter, MIN: Demond Claiborne, MIN: Donovan Jackson, MIN: Kyler Murray, SF: Jalen Graham, SF: Ogbo Okoronkwo, SF: Alfred Collins, SF: Ricky Pearsall, SF: Kalia Davis, SF: Gracen Halton, SF: KhaDarel Hodge, SF: Isaac Guerendo, SF: Jake Tonges, SF: Robert Beal Jr., SF: C.J. West, SF: Nick Martin, SF: Sam Okuayinonu, SF: Jack Jones, CIN: Oren Burks, CIN: Andrei Iosivas, CIN: Isaiah Foskey, CIN: Jalen Davis, CIN: Howard Cross III, CIN: Erick All, CIN: Bralyn Lux, CIN: Ke'Shawn Williams, CIN: Cashius Howell, CIN: Swayze Bozeman, CIN: Dalton Risner, CIN: Tanner Hudson, WAS: Jaden Bradley, WAS: Javontae Jean-Baptiste, WAS: Jaylin Lane, WAS: Leo Chenal, WAS: Craig Reynolds, WAS: Javon Kinlaw, WAS: Daron Payne, WAS: Austin Keys, WAS: Terry McLaurin, WAS: Jacory Croskey-Merritt, WAS: Jeremy McNichols, WAS: Dyami Brown, WAS: Nick Bellore.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 22.9 | 8.6 to 37.7 |
| QB | C.J. Stroud | HOU | 22.1 | 8.1 to 37.4 |
| QB | Josh Allen | BUF | 22.0 | 7.8 to 37.7 |
| QB | Dak Prescott | DAL | 21.9 | 8.5 to 36.4 |
| QB | Patrick Mahomes | KC | 21.1 | 7.9 to 35.7 |
| QB | Jayden Daniels | WAS | 20.1 | 7.1 to 34.9 |
| RB | Jahmyr Gibbs | DET | 24.2 | 8.5 to 41.9 |
| RB | Javonte Williams | DAL | 20.0 | 5.7 to 36.0 |
| RB | Jonathan Taylor | IND | 18.5 | 6.5 to 32.6 |
| RB | Tony Pollard | TEN | 18.3 | 5.6 to 33.2 |
| RB | Chuba Hubbard | CAR | 18.2 | 5.5 to 33.1 |
| RB | Chase Brown | CIN | 17.7 | 6.4 to 30.9 |
| RB | James Cook | BUF | 17.7 | 4.8 to 32.2 |
| RB | Jaylen Warren | PIT | 17.2 | 5.7 to 30.8 |
| RB | Christian McCaffrey | SF | 16.9 | 4.8 to 30.8 |
| RB | Bucky Irving | TB | 16.1 | 4.7 to 29.6 |
| WR | CeeDee Lamb | DAL | 21.6 | 6.8 to 38.2 |
| WR | Ja'Marr Chase | CIN | 20.5 | 6.6 to 36.7 |
| WR | Amon-Ra St. Brown | DET | 18.1 | 5.1 to 33.4 |
| WR | George Pickens | DAL | 16.8 | 4.0 to 32.0 |
| WR | Justin Jefferson | MIN | 16.0 | 4.4 to 30.1 |
| WR | Tee Higgins | CIN | 15.4 | 3.7 to 29.6 |
| WR | Garrett Wilson | NYJ | 15.1 | 3.6 to 29.1 |
| WR | Luther Burden III | CHI | 14.9 | 3.6 to 28.6 |
| WR | Nico Collins | HOU | 14.2 | 3.2 to 27.8 |
| WR | Parker Washington | JAX | 13.9 | 2.5 to 27.8 |
| WR | Malik Nabers | NYG | 13.6 | 3.3 to 26.6 |
| WR | Zay Flowers | BAL | 13.2 | 2.9 to 25.8 |
| TE | Trey McBride | ARI | 22.9 | 9.0 to 39.0 |
| TE | Tyler Warren | IND | 14.2 | 4.2 to 26.3 |
| TE | Isaiah Likely | NYG | 13.7 | 3.0 to 26.7 |
| TE | Colston Loveland | CHI | 11.3 | 2.1 to 22.4 |
| TE | T.J. Hockenson | MIN | 10.9 | 1.8 to 21.8 |
| TE | Travis Kelce | KC | 10.4 | 1.1 to 21.7 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 21.6 | 8.8 to 35.6 |
| QB | Josh Allen | BUF | 21.3 | 7.9 to 36.2 |
| QB | C.J. Stroud | HOU | 21.1 | 8.3 to 35.5 |
| QB | Dak Prescott | DAL | 20.7 | 8.7 to 34.2 |
| QB | Patrick Mahomes | KC | 20.3 | 8.0 to 34.0 |
| QB | Jayden Daniels | WAS | 19.5 | 7.1 to 33.7 |
| RB | Jahmyr Gibbs | DET | 20.9 | 7.3 to 36.6 |
| RB | Javonte Williams | DAL | 17.9 | 5.2 to 32.3 |
| RB | Tony Pollard | TEN | 16.2 | 4.7 to 29.6 |
| RB | Chuba Hubbard | CAR | 16.1 | 4.6 to 29.5 |
| RB | James Cook | BUF | 16.0 | 4.6 to 29.1 |
| RB | Jonathan Taylor | IND | 15.7 | 5.0 to 28.1 |
| RB | Chase Brown | CIN | 15.0 | 4.7 to 27.0 |
| RB | Christian McCaffrey | SF | 15.0 | 3.9 to 27.9 |
| RB | Jaylen Warren | PIT | 14.9 | 4.7 to 26.7 |
| RB | Bucky Irving | TB | 14.3 | 4.0 to 26.5 |
| WR | CeeDee Lamb | DAL | 16.7 | 4.8 to 30.1 |
| WR | Ja'Marr Chase | CIN | 15.7 | 4.6 to 28.3 |
| WR | Amon-Ra St. Brown | DET | 13.9 | 3.4 to 25.8 |
| WR | George Pickens | DAL | 13.4 | 2.7 to 25.6 |
| WR | Justin Jefferson | MIN | 12.3 | 2.8 to 23.3 |
| WR | Tee Higgins | CIN | 12.1 | 2.5 to 23.1 |
| WR | Luther Burden III | CHI | 11.9 | 2.3 to 23.1 |
| WR | Garrett Wilson | NYJ | 11.6 | 2.4 to 22.3 |
| WR | Nico Collins | HOU | 11.3 | 2.1 to 21.9 |
| WR | Parker Washington | JAX | 11.1 | 1.7 to 22.0 |
| WR | Zay Flowers | BAL | 10.4 | 1.9 to 20.6 |
| WR | Malik Nabers | NYG | 10.3 | 2.1 to 19.9 |
| TE | Trey McBride | ARI | 16.2 | 5.7 to 28.2 |
| TE | Isaiah Likely | NYG | 10.7 | 1.7 to 21.3 |
| TE | Tyler Warren | IND | 10.5 | 2.5 to 19.9 |
| TE | Colston Loveland | CHI | 8.8 | 1.1 to 18.2 |
| TE | T.J. Hockenson | MIN | 8.5 | 0.9 to 17.8 |
| TE | Travis Kelce | KC | 8.5 | 0.6 to 18.1 |
| K | Ka'imi Fairbairn | HOU | 10.0 | 3.0 to 18.6 |
| K | Tyler Bass | BUF | 10.0 | 3.0 to 18.0 |
| K | Jason Sanders | NYJ | 9.8 | 1.0 to 19.0 |
| K | Will Reichard | MIN | 9.6 | 1.0 to 19.0 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses come from the merged injury file (MFL, nflverse, ESPN, transactions) at the time of the pull. Re-run when news lands.
- Weather, referee tendencies and in-game injuries are not modeled.