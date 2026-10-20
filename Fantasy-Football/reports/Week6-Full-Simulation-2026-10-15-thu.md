# Week 6 Full Simulation Report - 15 OCT 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 4,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| SEA @ DEN | SEA 57.4% | SEA 21.7 - DEN 19.0 | DEN | 53.1% | SEA | 57.8% |
| HOU @ JAX | JAX 57.7% | HOU 20.0 - JAX 22.5 | JAX | 50.0% | JAX | 57.8% |
| CHI @ ATL | CHI 51.6% | CHI 26.1 - ATL 25.3 | ATL | 57.8% | CHI | 53.1% |
| BAL @ CLE | BAL 61.0% | BAL 22.4 - CLE 18.6 | BAL | 48.4% | BAL | 62.3% |
| TEN @ IND | IND 69.7% | TEN 18.7 - IND 25.6 | IND | 48.4% | IND | 70.9% |
| NYJ @ NE | NE 71.4% | NYJ 18.2 - NE 25.4 | NE | 48.4% | NE | 70.9% |
| NO @ NYG | NO 51.6% | NO 23.3 - NYG 22.6 | NYG | 51.6% | NYG | 46.9% |
| CAR @ PHI | CAR 59.5% | CAR 21.3 - PHI 17.9 | CAR | 65.3% | CAR | 60.8% |
| PIT @ TB | PIT 57.4% | PIT 21.1 - TB 18.7 | PIT | 50.0% | PIT | 57.8% |
| ARI @ LA | LA 82.2% | ARI 19.7 - LA 32.1 | ARI | 50.0% | LAR | 83.7% |
| LAC @ KC | KC 72.5% | LAC 17.1 - KC 24.8 | KC | 48.4% | KC | 73.5% |
| BUF @ LV | BUF 63.9% | BUF 29.1 - LV 24.5 | LV | 56.2% | BUF | 63.8% |
| DAL @ GB | GB 53.1% | DAL 26.1 - GB 27.0 | GB | 48.4% | GB | 53.1% |
| WAS @ SF | SF 71.4% | WAS 21.8 - SF 29.2 | WSH | 50.0% | SF | 72.2% |

**Flag:** the straight-up pick NYG in NO @ NYG is the market underdog (46.9%). It is a coin flip; the other side is the market favorite. Your call.

**Eliminator (fresh start this week, every team open):** best win chances are LA Rams 83.7%, KC 73.5%, SF 72.2%, IND and NE 70.9%. Surviving all season means saving the biggest favorites for the weeks with weaker options, so the Rams are the safe pick now but not automatically the smart one. I can plan the full 18 weeks once the schedule odds are loaded.

## 2. Five IRFL lineups (Golden active)

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 127.5 | 95.7 | 161.1 |
| 2 SAFE (protects a lead) | 127.3 | 95.7 | 160.4 |
| 3 BALANCED UPSIDE (75th percentile) | 127.5 | 95.7 | 161.1 |
| 4 SWING (90th percentile, for an underdog) | 124.5 | 90.4 | 160.1 |
| 5 CONTINGENCY (every Questionable out) | 127.3 | 95.7 | 160.4 |
| Week 6 sheet lineup (for comparison) | 117.1 | 87.4 | 148.1 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.9 | 4.2 to 33.1 |  |
| RB | Robinson, Brian | ATL | 8.3 | 0.7 to 17.9 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.6 | 0.7 to 16.7 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.5 |  |
| WR | Allen, Keenan | IND | 9.8 | 1.1 to 19.9 |  |
| WR | Golden, Matthew | GBP | 9.3 | 0.7 to 19.4 |  |
| WR | Flournoy, Ryan | DAL | 7.8 | 0.5 to 16.5 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.0 |  |
| DL | Davis, Jordan | PHI | 3.1 | 0.5 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.5 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.1 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.3 | 2.0 to 9.0 |  |
| DB | Kinchens, Kamren | LAR | 5.3 | 2.0 to 9.5 |  |
| DB | Moss, Riley | DEN | 3.6 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.9 | 4.2 to 33.1 |  |
| RB | Robinson, Brian | ATL | 8.3 | 0.7 to 17.9 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.6 | 0.7 to 16.7 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.5 |  |
| WR | Allen, Keenan | IND | 9.8 | 1.1 to 19.9 |  |
| WR | Golden, Matthew | GBP | 9.3 | 0.7 to 19.4 |  |
| WR | Flournoy, Ryan | DAL | 7.8 | 0.5 to 16.5 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.0 |  |
| DL | Davis, Jordan | PHI | 3.1 | 0.5 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.5 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.1 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.3 | 2.0 to 9.0 |  |
| DB | Kinchens, Kamren | LAR | 5.3 | 2.0 to 9.5 |  |
| DB | Jenkins, Rayshawn | PIT | 3.4 | 1.0 to 6.5 | differs from lineup 1 |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.9 | 4.2 to 33.1 |  |
| RB | Robinson, Brian | ATL | 8.3 | 0.7 to 17.9 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.6 | 0.7 to 16.7 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.5 |  |
| WR | Allen, Keenan | IND | 9.8 | 1.1 to 19.9 |  |
| WR | Golden, Matthew | GBP | 9.3 | 0.7 to 19.4 |  |
| WR | Flournoy, Ryan | DAL | 7.8 | 0.5 to 16.5 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.0 |  |
| DL | Davis, Jordan | PHI | 3.1 | 0.5 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.5 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.1 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Kinchens, Kamren | LAR | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 5.3 | 2.0 to 9.0 |  |
| DB | Moss, Riley | DEN | 3.6 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 15.0 | -3.1 to 33.7 | Questionable, plays about 75% of sims. differs from lineup 1 |
| RB | Robinson, Brian | ATL | 8.3 | 0.7 to 17.9 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.6 | 0.7 to 16.7 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.5 |  |
| WR | Allen, Keenan | IND | 9.8 | 1.1 to 19.9 |  |
| WR | Golden, Matthew | GBP | 9.3 | 0.7 to 19.4 |  |
| WR | Flournoy, Ryan | DAL | 7.8 | 0.5 to 16.5 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.0 |  |
| DL | Davis, Jordan | PHI | 3.1 | 0.5 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.5 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.1 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Kinchens, Kamren | LAR | 5.3 | 2.0 to 9.5 |  |
| DB | Scott, Nick | CAR | 5.3 | 2.0 to 9.0 |  |
| DB | Moss, Riley | DEN | 3.6 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.9 | 4.2 to 33.1 |  |
| RB | Robinson, Brian | ATL | 8.3 | 0.7 to 17.9 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.6 | 0.7 to 16.7 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.5 |  |
| WR | Allen, Keenan | IND | 9.8 | 1.1 to 19.9 |  |
| WR | Golden, Matthew | GBP | 9.3 | 0.7 to 19.4 |  |
| WR | Flournoy, Ryan | DAL | 7.8 | 0.5 to 16.5 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.0 |  |
| DL | Davis, Jordan | PHI | 3.1 | 0.5 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.5 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.1 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.3 | 2.0 to 9.0 |  |
| DB | Kinchens, Kamren | LAR | 5.3 | 2.0 to 9.5 |  |
| DB | Jenkins, Rayshawn | PIT | 3.4 | 1.0 to 6.5 | differs from lineup 1 |

Lineups 1 and 3 are identical; 2 and 5 are identical. Your roster has few real choices this week (the only live decisions are QB, the last DB slot and the last WR slot), so the five lineups collapse. Averages shift by about half a point between runs because the dice differ.

Not simulated this week (bye, no team, or no recent usage): Reed, D.J. (DET); Wonnum, D.J. (DET); Hutchinson, Aidan (DET); Andersen, Troy (FA); McPherson, Evan (CIN); Bates, Jake (DET); Goff, Jared (DET); Anderson, Zayne (MIA); LaPorta, Sam (DET); Hockenson, T.J. (MIN); Jefferson, Justin (MIN); Williams, Jameson (DET).

When the two free agents land (a safety and a defensive end), I will add them for Week 7. Defensive line is the thinnest group: Davis and Kancey are the only two playable linemen this week.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ LA

Market: LA -12.5, total 51.5. Sim: ARI 19.7, LA 32.1. LA wins 82.2%, ARI wins 17.8%. Median margin +12.6 for LA.

| Team stat | ARI | LA |
|---|---|---|
| Plays | 64 | 65 |
| Pass attempts / completions | 39 / 25 | 34 / 22 |
| Passing yards | 240 | 272 |
| Rush attempts / yards | 23 / 97 | 29 / 138 |
| Sacks taken | 2.5 | 2.2 |
| Interceptions thrown | 1.0 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.7 | 2.0 / 1.5 |
| Field goals | 1.4 | 2.4 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 17.9 | 240 pass yd, 1.4 TD, 1.0 INT; 2.3 rush, 11 yd |  |
| RB | Jeremiyah Love | 5.8 | 9.5 car, 38 yd, 0.21 TD; 1.4 rec, 8 yd, 0.08 TD | Questionable |
| RB | Tyler Allgeier | 5.4 | 4.5 car, 19 yd, 0.18 TD; 1.5 rec, 9 yd, 0.03 TD |  |
| RB | Michael Carter | 4.6 | 3.9 car, 17 yd, 0.06 TD; 1.3 rec, 11 yd, 0.03 TD |  |
| WR | Michael Wilson | 10.8 | 4.7 rec, 48 yd, 0.24 TD |  |
| WR | Kendrick Bourne | 5.7 | 2.7 rec, 26 yd, 0.06 TD |  |
| WR | Reggie Virgil | 4.1 | 1.8 rec, 20 yd, 0.06 TD |  |
| WR | Marvin Harrison Jr. | 3.0 | 1.1 rec, 13 yd, 0.09 TD |  |
| TE | Trey McBride | 12.7 | 6.2 rec, 48 yd, 0.29 TD |  |
| TE | Teagan Quitoriano | 4.0 | 1.0 rec, 9 yd, 0.36 TD |  |
| K | Chad Ryland | 7.4 | 1.5 FG, 2.0 XP |  |
| DL | Roy Lopez | 4.3 | 2.0 solo, 3.0 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.9 | 1.3 solo, 2.1 ast, 0.13 sack, 0.00 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.9 | 3.2 solo, 4.1 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.1 | 2.5 solo, 4.6 ast, 0.07 sack, 0.18 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.8 | 1.9 solo, 1.1 ast, 0.15 sack, 0.21 PD, 0.00 INT |  |
| DB | Budda Baker | 7.8 | 4.0 solo, 3.6 ast, 0.32 sack, 0.51 PD, 0.18 INT |  |
| DB | Denzel Burke | 4.3 | 2.4 solo, 1.3 ast, 0.00 sack, 0.66 PD, 0.21 INT |  |
| DB | Andrew Wingard | 3.6 | 2.2 solo, 3.1 ast, 0.00 sack, 0.18 PD, 0.18 INT | Questionable |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 22.5 | 272 pass yd, 2.0 TD, 0.7 INT; 1.7 rush, 7 yd |  |
| RB | Kyren Williams | 18.6 | 15.4 car, 74 yd, 0.81 TD; 3.1 rec, 25 yd, 0.17 TD |  |
| RB | Blake Corum | 9.1 | 9.2 car, 45 yd, 0.45 TD; 0.8 rec, 9 yd, 0.04 TD |  |
| WR | Puka Nacua | 18.2 | 0.9 car, 4 yd, 0.09 TD; 6.5 rec, 77 yd, 0.52 TD |  |
| WR | Davante Adams | 11.7 | 3.5 rec, 50 yd, 0.52 TD |  |
| WR | Konata Mumpfield | 3.5 | 1.1 rec, 15 yd, 0.13 TD |  |
| WR | Xavier Smith | 1.8 | 0.7 rec, 10 yd, 0.03 TD |  |
| TE | Tyler Higbee | 7.3 | 2.7 rec, 34 yd, 0.21 TD |  |
| TE | Colby Parkinson | 5.1 | 1.8 rec, 18 yd, 0.25 TD |  |
| K | Harrison Mevis | 8.7 | 1.5 FG, 3.3 XP |  |
| DL | Kobie Turner | 4.2 | 1.5 solo, 2.1 ast, 0.31 sack, 0.40 PD, 0.06 INT |  |
| DL | Poona Ford | 2.3 | 1.2 solo, 1.5 ast, 0.07 sack, 0.18 PD, 0.00 INT |  |
| LB | Byron Young | 5.5 | 2.1 solo, 2.3 ast, 0.68 sack, 0.00 PD, 0.00 INT |  |
| LB | Omar Speights | 5.4 | 3.0 solo, 2.4 ast, 0.29 sack, 0.15 PD, 0.00 INT |  |
| LB | Nate Landman | 5.2 | 3.8 solo, 3.7 ast, 0.06 sack, 0.19 PD, 0.05 INT | Questionable |
| DB | Quentin Lake | 6.2 | 3.5 solo, 2.1 ast, 0.00 sack, 0.97 PD, 0.13 INT |  |
| DB | Kamren Kinchens | 5.3 | 3.4 solo, 2.0 ast, 0.08 sack, 0.30 PD, 0.09 INT |  |
| DB | Kam Curl | 5.2 | 3.6 solo, 2.1 ast, 0.05 sack, 0.35 PD, 0.00 INT |  |

### BAL @ CLE

Market: CLE +4.0, total 41.0. Sim: BAL 22.4, CLE 18.6. CLE wins 39.0%, BAL wins 61.0%. Median margin -3.9 for CLE.

| Team stat | BAL | CLE |
|---|---|---|
| Plays | 61 | 62 |
| Pass attempts / completions | 28 / 19 | 35 / 21 |
| Passing yards | 209 | 233 |
| Rush attempts / yards | 30 / 154 | 25 / 98 |
| Sacks taken | 2.6 | 2.2 |
| Interceptions thrown | 0.5 | 0.8 |
| Passing / rushing TDs | 1.2 / 1.2 | 1.1 / 0.8 |
| Field goals | 1.6 | 1.4 |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Lamar Jackson | 13.6 | 156 pass yd, 0.9 TD, 0.4 INT; 3.9 rush, 22 yd | Questionable |
| RB | Derrick Henry | 17.0 | 19.3 car, 96 yd, 0.84 TD; 1.1 rec, 10 yd, 0.08 TD |  |
| RB | Justice Hill | 3.8 | 2.3 car, 14 yd, 0.06 TD; 1.1 rec, 8 yd, 0.04 TD |  |
| RB | Rasheen Ali | 1.2 | 0.3 car, 1 yd, 0.00 TD; 0.5 rec, 4 yd, 0.03 TD |  |
| WR | Zay Flowers | 14.5 | 5.5 rec, 66 yd, 0.33 TD |  |
| WR | Rashod Bateman | 4.2 | 2.3 rec, 26 yd, 0.11 TD | Questionable |
| WR | Devontez Walker | 2.7 | 0.9 rec, 11 yd, 0.12 TD |  |
| WR | Chris Moore | 2.5 | 0.9 rec, 10 yd, 0.11 TD |  |
| TE | Mark Andrews | 7.3 | 3.6 rec, 27 yd, 0.16 TD |  |
| TE | Matthew Hibner | 2.0 | 1.0 rec, 11 yd, 0.10 TD | Questionable |
| K | Tyler Loop | 8.8 | 1.7 FG, 2.3 XP |  |
| DL | Travis Jones | 3.5 | 1.3 solo, 1.4 ast, 0.29 sack, 0.17 PD, 0.00 INT |  |
| DL | Nnamdi Madubuike | 2.3 | 1.6 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Roquan Smith | 6.7 | 3.4 solo, 4.5 ast, 0.11 sack, 0.15 PD, 0.08 INT |  |
| LB | Trenton Simpson | 6.1 | 3.4 solo, 2.5 ast, 0.22 sack, 0.13 PD, 0.13 INT |  |
| LB | Tavius Robinson | 4.9 | 1.7 solo, 1.5 ast, 0.62 sack, 0.31 PD, 0.00 INT |  |
| DB | Kyle Hamilton | 7.3 | 4.5 solo, 2.4 ast, 0.03 sack, 0.78 PD, 0.16 INT |  |
| DB | Malaki Starks | 5.1 | 3.4 solo, 2.0 ast, 0.09 sack, 0.12 PD, 0.03 INT |  |
| DB | Marlon Humphrey | 4.2 | 3.1 solo, 1.2 ast, 0.04 sack, 0.78 PD, 0.21 INT | Questionable |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Shedeur Sanders | 15.8 | 233 pass yd, 1.1 TD, 0.8 INT; 1.5 rush, 8 yd |  |
| RB | Quinshon Judkins | 8.9 | 13.1 car, 44 yd, 0.37 TD; 2.8 rec, 19 yd, 0.07 TD | Questionable |
| RB | Trayveon Williams | 2.0 | 0.9 car, 4 yd, 0.01 TD; 0.7 rec, 7 yd, 0.02 TD |  |
| RB | Jaleel McLaughlin | 1.8 | 0.5 car, 2 yd, 0.17 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | Denzel Boston | 7.5 | 3.2 rec, 49 yd, 0.30 TD | Questionable |
| WR | Jerry Jeudy | 5.8 | 2.6 rec, 25 yd, 0.11 TD |  |
| WR | KC Concepcion | 5.1 | 0.6 car, 3 yd, 0.01 TD; 3.3 rec, 28 yd, 0.09 TD | Questionable |
| WR | Isaiah Bond | 3.5 | 1.3 rec, 19 yd, 0.04 TD |  |
| TE | Harold Fannin Jr. | 9.5 | 3.7 rec, 33 yd, 0.36 TD |  |
| TE | Sal Cannella | 1.2 | 0.6 rec, 5 yd, 0.01 TD |  |
| K | Andre Szmyt | 8.5 | 1.8 FG, 1.9 XP |  |
| DL | Sam Williams | 3.1 | 1.7 solo, 1.2 ast, 0.18 sack, 0.20 PD, 0.00 INT |  |
| DL | Adin Huntington | 2.5 | 0.6 solo, 1.9 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| LB | Quincy Williams | 6.9 | 3.4 solo, 3.2 ast, 0.00 sack, 0.42 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 5.6 | 3.5 solo, 5.3 ast, 0.19 sack, 0.20 PD, 0.03 INT | Questionable |
| LB | Jerome Baker | 1.5 | 0.4 solo, 1.5 ast, 0.03 sack, 0.00 PD, 0.00 INT |  |
| DB | Ronnie Hickman Jr. | 5.0 | 2.2 solo, 3.0 ast, 0.09 sack, 0.43 PD, 0.12 INT |  |
| DB | Tyson Campbell | 4.2 | 2.9 solo, 1.7 ast, 0.00 sack, 0.44 PD, 0.00 INT |  |
| DB | Denzel Ward | 4.1 | 2.3 solo, 1.4 ast, 0.00 sack, 0.38 PD, 0.12 INT |  |

### BUF @ LV

Market: LV +4.5, total 53.5. Sim: BUF 29.1, LV 24.5. LV wins 36.1%, BUF wins 63.9%. Median margin -4.7 for LV.

| Team stat | BUF | LV |
|---|---|---|
| Plays | 62 | 61 |
| Pass attempts / completions | 30 / 20 | 35 / 23 |
| Passing yards | 237 | 236 |
| Rush attempts / yards | 30 / 150 | 24 / 90 |
| Sacks taken | 2.3 | 2.1 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.6 | 1.7 / 1.0 |
| Field goals | 2.2 | 1.8 |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.6 | 237 pass yd, 1.5 TD, 0.7 INT; 7.1 rush, 37 yd |  |
| RB | James Cook | 15.5 | 16.1 car, 81 yd, 0.78 TD; 1.3 rec, 11 yd, 0.08 TD |  |
| RB | Ty Johnson | 4.8 | 2.1 car, 9 yd, 0.11 TD; 2.0 rec, 23 yd, 0.11 TD | Questionable |
| RB | Ray Davis | 3.2 | 2.7 car, 14 yd, 0.07 TD; 0.5 rec, 6 yd, 0.04 TD |  |
| WR | Khalil Shakir | 7.8 | 3.3 rec, 37 yd, 0.15 TD |  |
| WR | Keon Coleman | 6.2 | 2.1 rec, 27 yd, 0.24 TD |  |
| WR | DJ Moore | 4.7 | 2.3 rec, 28 yd, 0.17 TD | Questionable |
| WR | Skyler Bell | 3.2 | 1.3 rec, 14 yd, 0.07 TD |  |
| TE | Dalton Kincaid | 5.8 | 2.1 rec, 29 yd, 0.14 TD |  |
| TE | Dawson Knox | 4.4 | 1.8 rec, 16 yd, 0.17 TD |  |
| K | Tyler Bass | 9.6 | 1.8 FG, 3.0 XP |  |
| DL | Deone Walker | 2.9 | 1.2 solo, 1.6 ast, 0.09 sack, 0.60 PD, 0.00 INT |  |
| DL | DeWayne Carter | 2.7 | 1.4 solo, 1.0 ast, 0.26 sack, 0.00 PD, 0.00 INT |  |
| LB | Greg Rousseau | 6.2 | 1.9 solo, 1.4 ast, 0.88 sack, 0.39 PD, 0.00 INT |  |
| LB | Terrel Bernard | 4.7 | 3.0 solo, 2.5 ast, 0.00 sack, 0.20 PD, 0.00 INT |  |
| LB | Dorian Williams | 4.1 | 2.1 solo, 3.7 ast, 0.00 sack, 0.14 PD, 0.00 INT |  |
| DB | Cole Bishop | 5.3 | 3.7 solo, 2.6 ast, 0.00 sack, 0.07 PD, 0.07 INT |  |
| DB | C.J. Gardner-Johnson | 5.1 | 3.1 solo, 1.9 ast, 0.00 sack, 0.41 PD, 0.21 INT |  |
| DB | Christian Benford | 5.1 | 2.8 solo, 1.3 ast, 0.06 sack, 0.66 PD, 0.10 INT |  |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 18.5 | 236 pass yd, 1.7 TD, 0.8 INT; 1.6 rush, 6 yd |  |
| RB | Ashton Jeanty | 15.2 | 14.4 car, 50 yd, 0.42 TD; 3.6 rec, 30 yd, 0.23 TD |  |
| RB | Mike Washington Jr. | 4.2 | 3.8 car, 16 yd, 0.28 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| RB | Dylan Laube | 2.0 | 0.6 car, 2 yd, 0.20 TD; 0.3 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 7.9 | 0.5 car, 2 yd, 0.02 TD; 3.2 rec, 35 yd, 0.17 TD |  |
| WR | Cody White | 4.5 | 1.4 rec, 18 yd, 0.22 TD |  |
| WR | Tyler Lockett | 3.2 | 1.4 rec, 13 yd, 0.09 TD |  |
| WR | Jalen Nailor | 2.2 | 1.3 rec, 13 yd, 0.05 TD | Questionable |
| TE | Brock Bowers | 9.0 | 4.8 rec, 49 yd, 0.45 TD | Questionable |
| TE | Michael Mayer | 6.6 | 3.1 rec, 26 yd, 0.15 TD |  |
| K | Matt Gay | 9.8 | 1.9 FG, 2.5 XP |  |
| DL | Maxx Crosby | 4.0 | 1.4 solo, 1.5 ast, 0.39 sack, 0.11 PD, 0.00 INT |  |
| DL | Malcolm Koonce | 3.4 | 1.0 solo, 0.9 ast, 0.50 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 9.3 | 5.9 solo, 3.1 ast, 0.21 sack, 0.18 PD, 0.00 INT |  |
| LB | Quay Walker | 5.5 | 2.7 solo, 3.8 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Elandon Roberts | 2.7 | 1.6 solo, 1.8 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 6.5 | 4.0 solo, 2.3 ast, 0.16 sack, 0.14 PD, 0.00 INT |  |
| DB | Hezekiah Masses | 5.6 | 2.4 solo, 1.4 ast, 0.00 sack, 1.02 PD, 0.49 INT |  |
| DB | Taron Johnson | 5.1 | 3.4 solo, 1.0 ast, 0.00 sack, 0.36 PD, 0.00 INT |  |

### CAR @ PHI

Market: PHI +3.5, total 39.0. Sim: CAR 21.3, PHI 17.9. PHI wins 40.5%, CAR wins 59.5%. Median margin -3.3 for PHI.

| Team stat | CAR | PHI |
|---|---|---|
| Plays | 61 | 61 |
| Pass attempts / completions | 33 / 21 | 31 / 19 |
| Passing yards | 225 | 204 |
| Rush attempts / yards | 26 / 108 | 28 / 121 |
| Sacks taken | 2.3 | 2.1 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.9 | 0.9 / 1.0 |
| Field goals | 1.6 | 1.3 |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.7 | 225 pass yd, 1.4 TD, 0.7 INT; 4.0 rush, 16 yd |  |
| RB | Chuba Hubbard | 13.5 | 14.8 car, 63 yd, 0.57 TD; 1.8 rec, 14 yd, 0.13 TD |  |
| RB | AJ Dillon | 2.5 | 5.8 car, 22 yd, 0.11 TD; 0.3 rec, 2 yd, 0.00 TD | Questionable |
| WR | Tetairoa McMillan | 13.0 | 5.1 rec, 60 yd, 0.33 TD |  |
| WR | Jalen Coker | 9.3 | 4.0 rec, 39 yd, 0.25 TD |  |
| WR | John Metchie III | 4.2 | 1.6 rec, 16 yd, 0.16 TD |  |
| WR | Brycen Tremayne | 2.4 | 1.0 rec, 12 yd, 0.03 TD |  |
| TE | Darren Waller | 5.1 | 2.7 rec, 26 yd, 0.22 TD | Questionable |
| TE | Tommy Tremble | 2.9 | 1.9 rec, 16 yd, 0.09 TD | Questionable |
| K | Ryan Fitzgerald | 8.6 | 1.7 FG, 2.2 XP |  |
| DL | Derrick Brown | 4.1 | 2.0 solo, 2.1 ast, 0.12 sack, 0.48 PD, 0.00 INT |  |
| DL | Lee Hunter | 2.1 | 1.2 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 11.8 | 5.6 solo, 3.0 ast, 0.25 sack, 0.77 PD, 0.50 INT |  |
| LB | Bobby Okereke | 6.5 | 3.5 solo, 2.9 ast, 0.00 sack, 0.48 PD, 0.22 INT |  |
| LB | Princely Umanmielen | 3.2 | 1.5 solo, 0.8 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Scott | 5.3 | 3.7 solo, 2.2 ast, 0.00 sack, 0.05 PD, 0.05 INT |  |
| DB | Will Lee III | 4.9 | 2.7 solo, 1.9 ast, 0.00 sack, 0.86 PD, 0.00 INT |  |
| DB | Zakee Wheatley | 4.6 | 3.6 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tanner McKee | 12.7 | 204 pass yd, 0.9 TD, 0.7 INT |  |
| RB | Dameon Pierce | 11.5 | 15.1 car, 58 yd, 0.33 TD; 2.0 rec, 15 yd, 0.06 TD |  |
| RB | Saquon Barkley | 8.6 | 11.1 car, 53 yd, 0.67 TD; 1.1 rec, 8 yd, 0.02 TD | Questionable |
| WR | DeVonta Smith | 6.9 | 3.9 rec, 43 yd, 0.16 TD | Questionable |
| WR | Dontayvion Wicks | 5.9 | 3.2 rec, 39 yd, 0.12 TD | Questionable |
| WR | Makai Lemon | 5.7 | 2.8 rec, 24 yd, 0.07 TD |  |
| WR | Darius Cooper | 4.5 | 1.4 rec, 19 yd, 0.20 TD |  |
| TE | Dallas Goedert | 6.9 | 2.9 rec, 27 yd, 0.22 TD |  |
| TE | Zach Ertz | 2.6 | 1.2 rec, 12 yd, 0.04 TD |  |
| K | Jake Elliott | 7.2 | 1.4 FG, 1.9 XP |  |
| DL | Jalen Carter | 4.9 | 1.4 solo, 1.0 ast, 0.55 sack, 0.46 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.6 solo, 2.3 ast, 0.06 sack, 0.09 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 6.1 | 4.2 solo, 2.6 ast, 0.08 sack, 0.07 PD, 0.00 INT |  |
| LB | Zack Baun | 6.0 | 3.4 solo, 3.6 ast, 0.03 sack, 0.43 PD, 0.05 INT |  |
| LB | Jeremiah Trotter Jr. | 3.7 | 2.6 solo, 1.8 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| DB | Cooper DeJean | 6.3 | 3.4 solo, 2.4 ast, 0.00 sack, 0.96 PD, 0.22 INT |  |
| DB | Quinyon Mitchell | 4.7 | 3.1 solo, 0.6 ast, 0.00 sack, 0.88 PD, 0.15 INT |  |
| DB | Riq Woolen | 4.6 | 3.3 solo, 1.4 ast, 0.00 sack, 0.64 PD, 0.00 INT |  |

### CHI @ ATL

Market: ATL +1.0, total 51.5. Sim: CHI 26.1, ATL 25.3. ATL wins 48.4%, CHI wins 51.6%. Median margin -0.6 for ATL.

| Team stat | CHI | ATL |
|---|---|---|
| Plays | 66 | 63 |
| Pass attempts / completions | 34 / 21 | 31 / 19 |
| Passing yards | 222 | 234 |
| Rush attempts / yards | 30 / 137 | 30 / 146 |
| Sacks taken | 2.8 | 2.2 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.4 | 1.4 / 1.4 |
| Field goals | 2.0 | 1.9 |

**CHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Caleb Williams | 15.0 | 167 pass yd, 1.1 TD, 0.5 INT; 3.1 rush, 15 yd | Questionable |
| RB | D'Andre Swift | 12.0 | 11.0 car, 51 yd, 0.48 TD; 2.2 rec, 17 yd, 0.06 TD |  |
| RB | Kyle Monangai | 6.7 | 9.5 car, 45 yd, 0.39 TD; 1.1 rec, 9 yd, 0.03 TD | Questionable |
| RB | Roschon Johnson | 3.2 | 1.4 car, 6 yd, 0.03 TD; 1.2 rec, 10 yd, 0.04 TD |  |
| WR | Luther Burden III | 10.7 | 0.9 car, 4 yd, 0.02 TD; 4.2 rec, 45 yd, 0.24 TD |  |
| WR | Kalif Raymond | 9.0 | 3.9 rec, 33 yd, 0.31 TD |  |
| WR | Rome Odunze | 7.4 | 2.9 rec, 36 yd, 0.14 TD |  |
| WR | Jahdae Walker | 3.4 | 0.9 rec, 9 yd, 0.28 TD |  |
| TE | Colston Loveland | 8.4 | 3.6 rec, 33 yd, 0.24 TD |  |
| TE | Cole Kmet | 3.6 | 1.5 rec, 14 yd, 0.13 TD |  |
| K | Cairo Santos | 8.4 | 1.5 FG, 2.7 XP |  |
| DL | Austin Booker | 5.3 | 2.0 solo, 1.3 ast, 0.65 sack, 0.19 PD, 0.00 INT |  |
| DL | Montez Sweat | 2.9 | 1.0 solo, 1.1 ast, 0.41 sack, 0.03 PD, 0.00 INT |  |
| LB | Devin Bush | 5.3 | 2.7 solo, 3.0 ast, 0.21 sack, 0.16 PD, 0.00 INT |  |
| LB | D'Marco Jackson | 2.5 | 1.1 solo, 2.1 ast, 0.05 sack, 0.11 PD, 0.04 INT |  |
| LB | Noah Sewell | 0.9 | 0.4 solo, 0.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Dillon Thieneman | 6.7 | 3.6 solo, 3.5 ast, 0.00 sack, 0.70 PD, 0.19 INT |  |
| DB | Malik Muhammad | 4.3 | 2.3 solo, 1.2 ast, 0.16 sack, 0.50 PD, 0.15 INT |  |
| DB | Jaylon Johnson | 3.8 | 3.0 solo, 0.3 ast, 0.00 sack, 0.29 PD, 0.05 INT |  |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 16.7 | 234 pass yd, 1.4 TD, 0.8 INT; 1.1 rush, 5 yd |  |
| RB | Bijan Robinson | 22.3 | 18.0 car, 94 yd, 0.74 TD; 3.9 rec, 34 yd, 0.23 TD |  |
| RB | Brian Robinson | 8.3 | 8.9 car, 39 yd, 0.55 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| WR | Drake London | 13.2 | 4.9 rec, 71 yd, 0.21 TD |  |
| WR | Jahan Dotson | 6.3 | 2.0 rec, 29 yd, 0.23 TD |  |
| WR | Zachariah Branch | 2.8 | 1.4 rec, 12 yd, 0.04 TD |  |
| WR | Olamide Zaccheaus | 1.8 | 0.9 rec, 8 yd, 0.03 TD |  |
| TE | Kyle Pitts | 9.4 | 3.7 rec, 39 yd, 0.31 TD |  |
| TE | Austin Hooper | 4.3 | 1.4 rec, 14 yd, 0.26 TD |  |
| K | Nick Folk | 9.3 | 1.8 FG, 2.6 XP |  |
| DL | Cameron Thomas | 4.3 | 1.5 solo, 2.0 ast, 0.40 sack, 0.22 PD, 0.00 INT |  |
| DL | Samson Ebukam | 3.0 | 0.6 solo, 0.9 ast, 0.67 sack, 0.00 PD, 0.00 INT |  |
| LB | Kendal Daniels | 5.2 | 3.6 solo, 1.2 ast, 0.25 sack, 0.25 PD, 0.00 INT |  |
| LB | Harold Perkins Jr. | 4.0 | 2.5 solo, 1.9 ast, 0.11 sack, 0.24 PD, 0.00 INT |  |
| LB | Divine Deablo | 4.0 | 3.2 solo, 3.1 ast, 0.03 sack, 0.31 PD, 0.00 INT | Questionable |
| DB | Xavier Watts | 7.7 | 4.3 solo, 2.7 ast, 0.06 sack, 0.64 PD, 0.28 INT |  |
| DB | Jessie Bates | 5.5 | 3.1 solo, 2.0 ast, 0.00 sack, 0.47 PD, 0.10 INT |  |
| DB | C.J. Henderson | 5.1 | 4.4 solo, 0.9 ast, 0.00 sack, 1.08 PD, 0.07 INT | Questionable |

### DAL @ GB

Market: GB -1.0, total 53.0. Sim: DAL 26.1, GB 27.0. GB wins 53.1%, DAL wins 46.9%. Median margin +1.0 for GB.

| Team stat | DAL | GB |
|---|---|---|
| Plays | 65 | 60 |
| Pass attempts / completions | 36 / 23 | 32 / 20 |
| Passing yards | 264 | 258 |
| Rush attempts / yards | 26 / 112 | 26 / 111 |
| Sacks taken | 2.6 | 2.0 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.7 / 1.2 | 1.6 / 1.3 |
| Field goals | 2.0 | 2.0 |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 20.3 | 264 pass yd, 1.7 TD, 0.8 INT; 2.1 rush, 9 yd |  |
| RB | Javonte Williams | 13.1 | 12.3 car, 50 yd, 0.63 TD; 2.2 rec, 14 yd, 0.13 TD |  |
| RB | Tyler Goodson | 2.6 | 3.0 car, 13 yd, 0.08 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| RB | Jaydon Blue | 2.5 | 3.6 car, 15 yd, 0.16 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | CeeDee Lamb | 16.0 | 6.2 rec, 71 yd, 0.46 TD |  |
| WR | George Pickens | 13.2 | 5.0 rec, 63 yd, 0.33 TD |  |
| WR | Ryan Flournoy | 7.8 | 3.1 rec, 35 yd, 0.20 TD |  |
| WR | KaVontae Turpin | 3.4 | 0.6 car, 3 yd, 0.05 TD; 1.0 rec, 13 yd, 0.08 TD |  |
| TE | Jake Ferguson | 6.9 | 2.9 rec, 22 yd, 0.30 TD |  |
| TE | Brevyn Spann-Ford | 1.8 | 0.7 rec, 8 yd, 0.05 TD |  |
| K | Brandon Aubrey | 9.7 | 1.9 FG, 2.7 XP |  |
| DL | Quinnen Williams | 2.9 | 1.3 solo, 1.4 ast, 0.17 sack, 0.05 PD, 0.05 INT |  |
| DL | Otito Ogbonnia | 2.5 | 1.9 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Dee Winters | 5.8 | 4.2 solo, 2.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Jaishawn Barham | 4.3 | 2.6 solo, 2.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Rashan Gary | 3.2 | 2.1 solo, 0.8 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| DB | Caleb Downs | 6.1 | 3.8 solo, 2.1 ast, 0.14 sack, 0.16 PD, 0.00 INT |  |
| DB | DaRon Bland | 4.0 | 2.9 solo, 1.3 ast, 0.00 sack, 0.45 PD, 0.00 INT |  |
| DB | Shavon Revel Jr. | 3.4 | 2.3 solo, 1.1 ast, 0.00 sack, 0.31 PD, 0.00 INT |  |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 20.0 | 258 pass yd, 1.6 TD, 0.5 INT; 1.8 rush, 7 yd |  |
| RB | MarShawn Lloyd | 12.2 | 9.3 car, 36 yd, 0.88 TD; 1.5 rec, 12 yd, 0.13 TD |  |
| RB | Pierre Strong | 7.7 | 4.6 car, 19 yd, 0.11 TD; 2.4 rec, 22 yd, 0.09 TD |  |
| RB | Kaleb Johnson | 4.5 | 6.7 car, 30 yd, 0.17 TD; 0.3 rec, 3 yd, 0.02 TD |  |
| WR | Christian Watson | 13.6 | 3.9 rec, 63 yd, 0.58 TD |  |
| WR | Matthew Golden | 9.3 | 3.0 rec, 46 yd, 0.27 TD |  |
| WR | Bo Melton | 2.2 | 0.8 rec, 9 yd, 0.06 TD |  |
| WR | Skyy Moore | 2.0 | 1.2 rec, 10 yd, 0.06 TD | Questionable |
| TE | Tucker Kraft | 8.1 | 0.6 car, 3 yd, 0.01 TD; 3.2 rec, 34 yd, 0.20 TD |  |
| TE | Jonnu Smith | 2.2 | 0.9 rec, 11 yd, 0.04 TD |  |
| K | Trey Smack | 8.4 | 1.5 FG, 2.8 XP |  |
| DL | Devonte Wyatt | 2.9 | 1.8 solo, 0.9 ast, 0.47 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Brenton Cox Jr. | 2.8 | 1.7 solo, 1.3 ast, 0.11 sack, 0.00 PD, 0.00 INT |  |
| LB | Zaire Franklin | 6.8 | 3.6 solo, 4.6 ast, 0.00 sack, 0.28 PD, 0.00 INT |  |
| LB | Lukas Van Ness | 4.3 | 2.4 solo, 1.7 ast, 0.33 sack, 0.00 PD, 0.00 INT |  |
| LB | Isaiah McDuffie | 3.9 | 2.3 solo, 2.7 ast, 0.03 sack, 0.03 PD, 0.04 INT |  |
| DB | Xavier McKinney | 6.4 | 2.9 solo, 2.1 ast, 0.14 sack, 0.77 PD, 0.44 INT |  |
| DB | Evan Williams | 6.3 | 4.4 solo, 3.5 ast, 0.14 sack, 0.63 PD, 0.22 INT | Questionable |
| DB | Keisean Nixon | 5.8 | 3.4 solo, 1.9 ast, 0.04 sack, 0.81 PD, 0.14 INT |  |

### HOU @ JAX

Market: JAX -2.5, total 42.5. Sim: HOU 20.0, JAX 22.5. JAX wins 57.7%, HOU wins 42.3%. Median margin +2.4 for JAX.

| Team stat | HOU | JAX |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 36 / 23 | 32 / 21 |
| Passing yards | 248 | 239 |
| Rush attempts / yards | 25 / 88 | 27 / 102 |
| Sacks taken | 2.4 | 3.0 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.3 / 0.9 | 1.4 / 1.1 |
| Field goals | 1.5 | 1.7 |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 18.3 | 248 pass yd, 1.3 TD, 0.7 INT; 3.3 rush, 11 yd |  |
| RB | Woody Marks | 8.9 | 11.5 car, 38 yd, 0.35 TD; 1.7 rec, 10 yd, 0.07 TD |  |
| RB | Jawhar Jordan | 3.7 | 5.2 car, 19 yd, 0.09 TD; 0.6 rec, 5 yd, 0.02 TD |  |
| RB | Nick Chubb | 1.7 | 2.1 car, 8 yd, 0.08 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Nico Collins | 13.0 | 4.6 rec, 57 yd, 0.41 TD |  |
| WR | Xavier Hutchinson | 6.8 | 2.8 rec, 33 yd, 0.09 TD |  |
| WR | Jaylin Noel | 5.8 | 0.6 car, 2 yd, 0.01 TD; 2.1 rec, 25 yd, 0.16 TD |  |
| WR | Kayshon Boutte | 5.3 | 2.4 rec, 25 yd, 0.07 TD |  |
| TE | Dalton Schultz | 9.2 | 4.4 rec, 38 yd, 0.17 TD |  |
| TE | Foster Moreau | 3.8 | 1.6 rec, 12 yd, 0.16 TD |  |
| K | Ka'imi Fairbairn | 10.7 | 2.3 FG, 2.0 XP |  |
| DL | Will Anderson Jr. | 7.4 | 2.5 solo, 1.7 ast, 1.10 sack, 0.15 PD, 0.00 INT |  |
| DL | Danielle Hunter | 5.6 | 1.5 solo, 1.5 ast, 0.80 sack, 0.52 PD, 0.00 INT |  |
| LB | Jake Hansen | 4.8 | 2.3 solo, 2.4 ast, 0.14 sack, 0.32 PD, 0.16 INT |  |
| LB | Azeez Al-Shaair | 4.7 | 3.3 solo, 4.5 ast, 0.00 sack, 0.34 PD, 0.13 INT | Questionable |
| LB | Kenneth Murray, Jr. | 1.7 | 0.5 solo, 2.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Reed Blankenship | 7.3 | 4.2 solo, 3.7 ast, 0.00 sack, 0.63 PD, 0.20 INT |  |
| DB | Kamari Lassiter | 5.8 | 3.8 solo, 1.5 ast, 0.00 sack, 0.95 PD, 0.09 INT |  |
| DB | Calen Bullock | 4.6 | 2.9 solo, 1.8 ast, 0.00 sack, 0.56 PD, 0.08 INT |  |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 18.8 | 239 pass yd, 1.4 TD, 0.7 INT; 3.8 rush, 15 yd |  |
| RB | Bhayshul Tuten | 9.5 | 12.5 car, 46 yd, 0.43 TD; 1.2 rec, 10 yd, 0.05 TD |  |
| RB | Chris Rodriguez Jr. | 4.7 | 5.6 car, 21 yd, 0.38 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| RB | Ameer Abdullah | 1.6 | 1.8 car, 7 yd, 0.04 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| WR | Parker Washington | 12.9 | 4.5 rec, 60 yd, 0.39 TD |  |
| WR | Jakobi Meyers | 9.3 | 3.9 rec, 40 yd, 0.22 TD |  |
| WR | Brian Thomas Jr. | 5.8 | 2.3 rec, 26 yd, 0.15 TD |  |
| WR | Josh Cameron | 5.1 | 1.9 rec, 21 yd, 0.18 TD |  |
| TE | Brenton Strange | 9.8 | 4.3 rec, 43 yd, 0.21 TD |  |
| TE | Nate Boerkircher | 1.7 | 1.1 rec, 10 yd, 0.04 TD | Questionable |
| K | Cam Little | 9.0 | 1.8 FG, 2.3 XP |  |
| DL | Josh Hines-Allen | 4.6 | 1.9 solo, 1.7 ast, 0.40 sack, 0.25 PD, 0.00 INT |  |
| DL | Travon Walker | 3.0 | 1.2 solo, 1.4 ast, 0.31 sack, 0.15 PD, 0.00 INT |  |
| LB | Foyesade Oluokun | 7.5 | 4.3 solo, 3.6 ast, 0.00 sack, 0.49 PD, 0.23 INT |  |
| LB | Ventrell Miller | 4.6 | 2.4 solo, 2.0 ast, 0.10 sack, 0.38 PD, 0.05 INT |  |
| LB | Dennis Gardeck | 2.4 | 1.5 solo, 0.9 ast, 0.12 sack, 0.05 PD, 0.00 INT |  |
| DB | Antonio Johnson | 5.8 | 2.8 solo, 1.6 ast, 0.13 sack, 0.59 PD, 0.24 INT |  |
| DB | Travis Hunter | 5.2 | 2.8 solo, 1.4 ast, 0.00 sack, 1.14 PD, 0.20 INT |  |
| DB | Jarrian Jones | 3.9 | 2.8 solo, 0.7 ast, 0.00 sack, 0.99 PD, 0.30 INT | Questionable |

### LAC @ KC

Market: KC -8.0, total 42.0. Sim: LAC 17.1, KC 24.8. KC wins 72.5%, LAC wins 27.4%. Median margin +7.7 for KC.

| Team stat | LAC | KC |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 35 / 21 | 33 / 20 |
| Passing yards | 233 | 227 |
| Rush attempts / yards | 26 / 105 | 27 / 120 |
| Sacks taken | 2.1 | 2.6 |
| Interceptions thrown | 0.9 | 0.8 |
| Passing / rushing TDs | 1.1 / 0.8 | 1.6 / 1.1 |
| Field goals | 1.3 | 1.9 |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.3 | 233 pass yd, 1.1 TD, 0.9 INT; 3.7 rush, 17 yd |  |
| RB | Omarion Hampton | 8.9 | 9.9 car, 36 yd, 0.36 TD; 1.7 rec, 12 yd, 0.05 TD |  |
| RB | Keaton Mitchell | 8.0 | 4.8 car, 19 yd, 0.08 TD; 3.0 rec, 19 yd, 0.13 TD |  |
| RB | Kimani Vidal | 5.5 | 4.6 car, 19 yd, 0.17 TD; 1.1 rec, 10 yd, 0.08 TD |  |
| WR | Ladd McConkey | 5.5 | 2.9 rec, 36 yd, 0.17 TD | Questionable |
| WR | Quentin Johnston | 5.3 | 2.7 rec, 35 yd, 0.13 TD | Questionable |
| WR | Theo Wease Jr. | 2.5 | 1.1 rec, 12 yd, 0.02 TD |  |
| WR | Marquez Valdes-Scantling | 2.0 | 1.2 rec, 12 yd, 0.03 TD | Questionable |
| TE | Oronde Gadsden II | 5.6 | 2.4 rec, 24 yd, 0.13 TD |  |
| TE | Charlie Kolar | 4.0 | 1.9 rec, 19 yd, 0.04 TD |  |
| K | Cameron Dicker | 8.3 | 1.7 FG, 1.7 XP |  |
| DL | Justin Eboigbe | 2.3 | 1.6 solo, 1.3 ast, 0.21 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Teair Tart | 1.9 | 1.4 solo, 0.8 ast, 0.00 sack, 0.11 PD, 0.00 INT |  |
| LB | Tuli Tuipulotu | 6.4 | 2.0 solo, 1.6 ast, 0.54 sack, 0.41 PD, 0.13 INT |  |
| LB | Akheem Mesidor | 5.4 | 2.1 solo, 2.5 ast, 0.53 sack, 0.00 PD, 0.00 INT |  |
| LB | Daiyan Henley | 4.4 | 2.8 solo, 3.3 ast, 0.09 sack, 0.28 PD, 0.05 INT | Questionable |
| DB | Tony Jefferson | 4.6 | 2.8 solo, 1.7 ast, 0.00 sack, 0.38 PD, 0.09 INT |  |
| DB | Cam Hart | 4.2 | 2.2 solo, 1.4 ast, 0.00 sack, 0.81 PD, 0.14 INT |  |
| DB | Genesis Smith | 3.8 | 1.2 solo, 1.2 ast, 0.00 sack, 0.83 PD, 0.38 INT |  |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 18.4 | 227 pass yd, 1.6 TD, 0.8 INT; 1.9 rush, 8 yd |  |
| RB | Kenneth Walker III | 17.4 | 14.0 car, 69 yd, 0.61 TD; 2.9 rec, 24 yd, 0.28 TD |  |
| RB | Kareem Hunt | 5.4 | 5.5 car, 21 yd, 0.25 TD; 0.8 rec, 8 yd, 0.06 TD |  |
| RB | Emmett Johnson | 3.3 | 2.4 car, 9 yd, 0.05 TD; 0.9 rec, 11 yd, 0.03 TD |  |
| WR | Rashee Rice | 8.1 | 4.2 rec, 48 yd, 0.29 TD | Questionable |
| WR | Xavier Worthy | 7.5 | 3.0 rec, 33 yd, 0.18 TD |  |
| WR | Jalen Royals | 2.7 | 1.0 rec, 8 yd, 0.14 TD |  |
| WR | JuJu Smith-Schuster | 2.0 | 1.0 rec, 9 yd, 0.04 TD |  |
| TE | Travis Kelce | 10.5 | 4.0 rec, 44 yd, 0.36 TD |  |
| TE | Noah Gray | 3.3 | 1.5 rec, 15 yd, 0.06 TD |  |
| K | Harrison Butker | 9.5 | 1.9 FG, 2.5 XP |  |
| DL | George Karlaftis | 3.3 | 1.3 solo, 1.9 ast, 0.11 sack, 0.31 PD, 0.13 INT |  |
| DL | Chris Jones | 3.3 | 1.1 solo, 1.2 ast, 0.35 sack, 0.34 PD, 0.00 INT |  |
| LB | Nick Bolton | 8.2 | 4.8 solo, 5.0 ast, 0.06 sack, 0.44 PD, 0.08 INT |  |
| LB | Drue Tranquill | 5.9 | 3.6 solo, 3.7 ast, 0.00 sack, 0.25 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.3 | 1.0 solo, 1.3 ast, 0.00 sack, 0.03 PD, 0.03 INT |  |
| DB | Mansoor Delane | 7.4 | 4.7 solo, 2.0 ast, 0.00 sack, 0.92 PD, 0.25 INT |  |
| DB | Chamarri Conner | 5.4 | 3.4 solo, 1.8 ast, 0.14 sack, 0.35 PD, 0.12 INT |  |
| DB | L'Jarius Sneed | 5.0 | 3.9 solo, 2.4 ast, 0.00 sack, 0.54 PD, 0.00 INT | Questionable |

### NO @ NYG

Market: NYG +1.0, total 46.0. Sim: NO 23.3, NYG 22.6. NYG wins 48.4%, NO wins 51.6%. Median margin -0.6 for NYG.

| Team stat | NO | NYG |
|---|---|---|
| Plays | 64 | 62 |
| Pass attempts / completions | 35 / 23 | 30 / 19 |
| Passing yards | 240 | 193 |
| Rush attempts / yards | 27 / 114 | 30 / 124 |
| Sacks taken | 2.5 | 2.5 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.4 / 1.1 | 1.2 / 1.3 |
| Field goals | 1.7 | 1.7 |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 18.7 | 240 pass yd, 1.4 TD, 0.8 INT; 2.8 rush, 13 yd |  |
| RB | Kendre Miller | 5.3 | 5.7 car, 22 yd, 0.29 TD; 0.7 rec, 5 yd, 0.02 TD |  |
| RB | Audric Estimé | 4.9 | 4.6 car, 21 yd, 0.14 TD; 1.0 rec, 9 yd, 0.03 TD |  |
| RB | Alvin Kamara | 4.6 | 4.4 car, 18 yd, 0.24 TD; 1.7 rec, 10 yd, 0.05 TD | Questionable |
| WR | Chris Olave | 10.1 | 5.4 rec, 64 yd, 0.31 TD | Questionable |
| WR | Devaughn Vele | 7.7 | 3.3 rec, 31 yd, 0.22 TD |  |
| WR | Kevin Austin Jr. | 3.3 | 1.4 rec, 14 yd, 0.09 TD |  |
| WR | Bryce Lance | 2.2 | 1.0 rec, 10 yd, 0.04 TD |  |
| TE | Juwan Johnson | 8.6 | 3.7 rec, 36 yd, 0.23 TD |  |
| TE | Noah Fant | 4.0 | 1.4 rec, 12 yd, 0.23 TD |  |
| K | Charlie Smyth | 8.0 | 1.5 FG, 2.4 XP |  |
| DL | Chase Young | 5.4 | 1.4 solo, 1.1 ast, 0.77 sack, 0.26 PD, 0.00 INT |  |
| DL | Carl Granderson | 4.2 | 1.6 solo, 2.0 ast, 0.43 sack, 0.13 PD, 0.07 INT |  |
| LB | Pete Werner | 4.5 | 2.7 solo, 2.5 ast, 0.09 sack, 0.15 PD, 0.00 INT |  |
| LB | Danny Stutsman | 3.9 | 2.5 solo, 2.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Cameron Jordan | 3.6 | 1.4 solo, 1.4 ast, 0.40 sack, 0.04 PD, 0.00 INT |  |
| DB | Jonas Sanker | 5.0 | 3.3 solo, 2.3 ast, 0.00 sack, 0.14 PD, 0.04 INT |  |
| DB | Julian Blackmon | 4.8 | 3.0 solo, 2.4 ast, 0.00 sack, 0.16 PD, 0.16 INT |  |
| DB | Kool-Aid McKinstry | 4.6 | 3.0 solo, 1.3 ast, 0.00 sack, 0.91 PD, 0.03 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jameis Winston | 15.1 | 193 pass yd, 1.2 TD, 0.5 INT; 1.3 rush, 6 yd |  |
| RB | Cam Skattebo | 10.7 | 11.5 car, 46 yd, 0.64 TD; 1.2 rec, 10 yd, 0.03 TD |  |
| RB | Tyrone Tracy Jr. | 5.5 | 5.1 car, 23 yd, 0.13 TD; 1.1 rec, 10 yd, 0.07 TD |  |
| RB | Devin Singletary | 5.4 | 4.6 car, 19 yd, 0.26 TD; 0.9 rec, 7 yd, 0.06 TD |  |
| WR | Malik Nabers | 10.0 | 4.2 rec, 43 yd, 0.27 TD |  |
| WR | Malachi Fields | 3.6 | 1.4 rec, 16 yd, 0.10 TD |  |
| WR | Darius Slayton | 3.4 | 1.4 rec, 16 yd, 0.08 TD |  |
| WR | Darnell Mooney | 2.2 | 1.2 rec, 13 yd, 0.05 TD | Questionable |
| TE | Isaiah Likely | 10.2 | 4.5 rec, 37 yd, 0.35 TD |  |
| TE | Theo Johnson | 2.3 | 1.2 rec, 14 yd, 0.10 TD | Questionable |
| K | Dominic Zvada | 9.8 | 2.0 FG, 2.3 XP |  |
| DL | Shelby Harris | 2.4 | 1.0 solo, 1.6 ast, 0.00 sack, 0.57 PD, 0.00 INT |  |
| DL | DJ Reader | 2.2 | 1.6 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Arvell Reese | 9.8 | 6.0 solo, 2.9 ast, 0.26 sack, 0.92 PD, 0.23 INT |  |
| LB | Tremaine Edmunds | 9.1 | 5.8 solo, 2.9 ast, 0.48 sack, 0.39 PD, 0.00 INT |  |
| LB | Abdul Carter | 3.0 | 1.2 solo, 1.6 ast, 0.45 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | Jevon Holland | 5.8 | 2.7 solo, 1.7 ast, 0.00 sack, 0.53 PD, 0.38 INT |  |
| DB | Deonte Banks | 4.9 | 1.7 solo, 1.0 ast, 0.00 sack, 1.23 PD, 0.15 INT |  |
| DB | Andru Phillips | 4.6 | 2.8 solo, 1.0 ast, 0.30 sack, 0.40 PD, 0.00 INT |  |

### NYJ @ NE

Market: NE -7.0, total 43.5. Sim: NYJ 18.2, NE 25.4. NE wins 71.4%, NYJ wins 28.6%. Median margin +7.1 for NE.

| Team stat | NYJ | NE |
|---|---|---|
| Plays | 60 | 61 |
| Pass attempts / completions | 34 / 21 | 31 / 21 |
| Passing yards | 207 | 253 |
| Rush attempts / yards | 25 / 101 | 28 / 127 |
| Sacks taken | 2.2 | 2.3 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.2 / 0.8 | 1.6 / 1.2 |
| Field goals | 1.4 | 1.9 |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brady Cook | 15.2 | 207 pass yd, 1.2 TD, 0.6 INT; 1.5 rush, 6 yd |  |
| RB | Braelon Allen | 10.5 | 12.3 car, 50 yd, 0.42 TD; 1.7 rec, 10 yd, 0.06 TD |  |
| RB | Isaiah Davis | 2.4 | 1.7 car, 8 yd, 0.06 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| RB | Khalil Herbert | 1.9 | 2.3 car, 9 yd, 0.03 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| WR | Garrett Wilson | 12.6 | 5.1 rec, 51 yd, 0.39 TD |  |
| WR | Isaiah Williams | 6.2 | 2.7 rec, 25 yd, 0.14 TD |  |
| WR | Tim Patrick | 4.6 | 2.1 rec, 21 yd, 0.07 TD |  |
| WR | Sterling Shepard | 1.2 | 0.6 rec, 5 yd, 0.02 TD |  |
| TE | Kenyon Sadiq | 5.4 | 3.1 rec, 27 yd, 0.19 TD | Questionable |
| TE | Jeremy Ruckert | 3.8 | 1.8 rec, 12 yd, 0.13 TD |  |
| K | Jason Sanders | 8.0 | 1.6 FG, 1.9 XP |  |
| DL | Will McDonald IV | 3.9 | 1.2 solo, 1.2 ast, 0.46 sack, 0.00 PD, 0.00 INT |  |
| DL | Jowon Briggs | 3.4 | 1.1 solo, 2.1 ast, 0.32 sack, 0.00 PD, 0.00 INT |  |
| LB | David Bailey | 7.8 | 3.4 solo, 1.7 ast, 1.01 sack, 0.21 PD, 0.00 INT |  |
| LB | Demario Davis | 6.5 | 3.6 solo, 3.2 ast, 0.39 sack, 0.15 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 6.4 | 3.5 solo, 4.1 ast, 0.05 sack, 0.49 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 10.1 | 5.8 solo, 4.2 ast, 0.00 sack, 0.94 PD, 0.43 INT |  |
| DB | Dane Belton | 5.2 | 3.7 solo, 4.1 ast, 0.23 sack, 0.39 PD, 0.00 INT | Questionable |
| DB | Andre Cisco | 4.2 | 2.8 solo, 0.6 ast, 0.19 sack, 0.16 PD, 0.00 INT |  |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 21.6 | 253 pass yd, 1.6 TD, 0.6 INT; 4.6 rush, 21 yd |  |
| RB | Rhamondre Stevenson | 13.2 | 7.7 car, 37 yd, 0.40 TD; 3.3 rec, 29 yd, 0.17 TD |  |
| RB | TreVeyon Henderson | 6.8 | 8.8 car, 39 yd, 0.40 TD; 1.2 rec, 11 yd, 0.07 TD | Questionable |
| RB | Corey Kiner | 2.6 | 3.1 car, 14 yd, 0.07 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Romeo Doubs | 9.6 | 3.3 rec, 43 yd, 0.32 TD |  |
| WR | DeMario Douglas | 7.3 | 2.7 rec, 32 yd, 0.22 TD |  |
| WR | Efton Chism III | 5.1 | 1.9 rec, 23 yd, 0.15 TD |  |
| WR | Kyle Williams | 5.0 | 1.4 rec, 24 yd, 0.18 TD |  |
| TE | Hunter Henry | 10.1 | 4.1 rec, 46 yd, 0.26 TD |  |
| TE | Eli Raridon | 5.2 | 2.1 rec, 23 yd, 0.14 TD |  |
| K | Andy Borregales | 8.1 | 1.5 FG, 2.6 XP |  |
| DL | Christian Barmore | 2.2 | 0.9 solo, 0.5 ast, 0.26 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Taylor III | 1.8 | 0.6 solo, 0.6 ast, 0.29 sack, 0.00 PD, 0.00 INT |  |
| LB | Elijah Ponder | 5.7 | 1.8 solo, 1.2 ast, 0.76 sack, 0.00 PD, 0.00 INT |  |
| LB | Robert Spillane | 4.5 | 2.7 solo, 2.8 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |
| LB | Gabe Jacas | 3.7 | 1.5 solo, 1.6 ast, 0.25 sack, 0.17 PD, 0.17 INT |  |
| DB | Kindle Vildor | 4.3 | 2.5 solo, 0.5 ast, 0.00 sack, 0.51 PD, 0.00 INT |  |
| DB | Marcus Jones | 3.4 | 2.4 solo, 1.0 ast, 0.08 sack, 0.54 PD, 0.15 INT | Questionable |
| DB | Craig Woodson | 3.3 | 2.4 solo, 1.7 ast, 0.00 sack, 0.29 PD, 0.14 INT | Questionable |

### PIT @ TB

Market: TB +2.5, total 39.5. Sim: PIT 21.1, TB 18.7. TB wins 42.6%, PIT wins 57.4%. Median margin -2.5 for TB.

| Team stat | PIT | TB |
|---|---|---|
| Plays | 64 | 63 |
| Pass attempts / completions | 35 / 22 | 34 / 22 |
| Passing yards | 257 | 232 |
| Rush attempts / yards | 26 / 122 | 27 / 122 |
| Sacks taken | 1.8 | 2.5 |
| Interceptions thrown | 0.7 | 0.9 |
| Passing / rushing TDs | 1.4 / 0.9 | 1.2 / 0.8 |
| Field goals | 1.6 | 1.4 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 18.1 | 257 pass yd, 1.4 TD, 0.7 INT; 1.5 rush, 6 yd |  |
| RB | Jaylen Warren | 20.4 | 15.2 car, 76 yd, 0.62 TD; 3.9 rec, 41 yd, 0.21 TD |  |
| RB | Rico Dowdle | 4.1 | 4.8 car, 19 yd, 0.09 TD; 1.5 rec, 14 yd, 0.05 TD | Questionable |
| RB | Travis Homer | 0.9 | 1.7 car, 7 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | DK Metcalf | 12.5 | 4.9 rec, 57 yd, 0.28 TD |  |
| WR | Germie Bernard | 9.7 | 4.3 rec, 45 yd, 0.13 TD |  |
| WR | Scott Miller | 3.0 | 1.4 rec, 13 yd, 0.05 TD |  |
| TE | Pat Freiermuth | 10.8 | 4.0 rec, 40 yd, 0.44 TD |  |
| TE | Darnell Washington | 6.9 | 2.8 rec, 31 yd, 0.16 TD |  |
| K | Chris Boswell | 8.2 | 1.6 FG, 2.2 XP |  |
| DL | Cameron Heyward | 4.7 | 2.1 solo, 2.3 ast, 0.26 sack, 0.41 PD, 0.00 INT |  |
| DL | Keeanu Benton | 2.1 | 1.5 solo, 1.5 ast, 0.08 sack, 0.19 PD, 0.00 INT | Questionable |
| LB | T.J. Watt | 6.7 | 1.8 solo, 1.0 ast, 0.64 sack, 0.46 PD, 0.20 INT |  |
| LB | Payton Wilson | 6.6 | 3.9 solo, 3.3 ast, 0.17 sack, 0.26 PD, 0.00 INT |  |
| LB | Patrick Queen | 5.2 | 2.5 solo, 4.3 ast, 0.00 sack, 0.20 PD, 0.10 INT |  |
| DB | Jaquan Brisker | 6.3 | 3.4 solo, 3.7 ast, 0.00 sack, 0.67 PD, 0.14 INT |  |
| DB | Robert Spears-Jennings | 4.0 | 2.4 solo, 1.0 ast, 0.00 sack, 0.45 PD, 0.23 INT |  |
| DB | Daylen Everette | 3.8 | 2.6 solo, 0.3 ast, 0.00 sack, 1.06 PD, 0.00 INT |  |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jalon Daniels | 17.1 | 232 pass yd, 1.2 TD, 0.9 INT; 4.6 rush, 22 yd |  |
| RB | Bucky Irving | 14.0 | 14.3 car, 65 yd, 0.39 TD; 2.6 rec, 18 yd, 0.14 TD |  |
| RB | Kenny Gainwell | 7.0 | 3.0 car, 12 yd, 0.05 TD; 2.6 rec, 19 yd, 0.19 TD |  |
| RB | Sean Tucker | 2.7 | 3.6 car, 15 yd, 0.24 TD; 0.2 rec, 2 yd, 0.03 TD | Questionable |
| WR | Emeka Egbuka | 9.8 | 4.2 rec, 41 yd, 0.17 TD |  |
| WR | Chris Godwin Jr. | 9.3 | 4.2 rec, 41 yd, 0.15 TD |  |
| WR | Ted Hurst III | 6.3 | 2.2 rec, 29 yd, 0.21 TD |  |
| WR | Tez Johnson | 4.0 | 1.4 rec, 20 yd, 0.07 TD |  |
| TE | Cade Otton | 9.0 | 4.2 rec, 41 yd, 0.14 TD |  |
| TE | Payne Durham | 0.9 | 0.4 rec, 4 yd, 0.01 TD |  |
| K | Chase McLaughlin | 8.5 | 1.8 FG, 1.9 XP |  |
| DL | A'Shawn Robinson | 3.3 | 0.8 solo, 2.2 ast, 0.19 sack, 0.20 PD, 0.20 INT |  |
| DL | Vita Vea | 2.2 | 0.9 solo, 1.3 ast, 0.09 sack, 0.30 PD, 0.00 INT |  |
| LB | Josiah Trotter | 9.0 | 4.9 solo, 3.7 ast, 0.18 sack, 0.17 PD, 0.17 INT |  |
| LB | Alex Anzalone | 5.3 | 1.8 solo, 3.5 ast, 0.22 sack, 0.27 PD, 0.26 INT |  |
| LB | Lavonte David | 4.2 | 2.7 solo, 1.5 ast, 0.09 sack, 0.08 PD, 0.00 INT |  |
| DB | Jacob Parrish | 6.6 | 3.9 solo, 0.9 ast, 0.00 sack, 1.30 PD, 0.27 INT |  |
| DB | Keionte Scott | 5.5 | 4.9 solo, 0.2 ast, 0.00 sack, 0.48 PD, 0.00 INT |  |
| DB | Tykee Smith | 4.5 | 3.1 solo, 1.4 ast, 0.00 sack, 0.29 PD, 0.03 INT |  |

### SEA @ DEN

Market: DEN +2.5, total 40.5. Sim: SEA 21.7, DEN 19.0. DEN wins 42.6%, SEA wins 57.4%. Median margin -2.4 for DEN.

| Team stat | SEA | DEN |
|---|---|---|
| Plays | 60 | 62 |
| Pass attempts / completions | 30 / 20 | 34 / 21 |
| Passing yards | 209 | 192 |
| Rush attempts / yards | 27 / 114 | 26 / 99 |
| Sacks taken | 2.6 | 2.5 |
| Interceptions thrown | 0.8 | 0.8 |
| Passing / rushing TDs | 1.3 / 1.1 | 1.2 / 0.8 |
| Field goals | 1.6 | 1.4 |

**SEA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Sam Darnold | 15.6 | 209 pass yd, 1.3 TD, 0.8 INT; 2.3 rush, 10 yd |  |
| RB | Emanuel Wilson | 14.0 | 17.5 car, 70 yd, 0.72 TD; 1.2 rec, 10 yd, 0.10 TD |  |
| RB | George Holani | 5.5 | 4.4 car, 19 yd, 0.11 TD; 1.7 rec, 12 yd, 0.04 TD |  |
| WR | Jaxon Smith-Njigba | 19.3 | 7.6 rec, 85 yd, 0.53 TD |  |
| WR | Cooper Kupp | 5.6 | 2.5 rec, 24 yd, 0.13 TD |  |
| WR | Rashid Shaheed | 5.3 | 0.7 car, 4 yd, 0.09 TD; 2.0 rec, 19 yd, 0.08 TD |  |
| WR | Tory Horton | 3.1 | 1.2 rec, 12 yd, 0.12 TD |  |
| TE | AJ Barner | 7.0 | 3.0 rec, 25 yd, 0.15 TD |  |
| TE | Eric Saubert | 1.4 | 0.6 rec, 4 yd, 0.07 TD |  |
| K | Jason Myers | 10.2 | 2.1 FG, 2.2 XP |  |
| DL | Byron Murphy II | 4.2 | 1.7 solo, 1.9 ast, 0.51 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Williams | 3.3 | 1.4 solo, 1.2 ast, 0.43 sack, 0.00 PD, 0.00 INT |  |
| LB | Ernest Jones | 9.2 | 4.6 solo, 4.7 ast, 0.29 sack, 0.50 PD, 0.22 INT |  |
| LB | DeMarcus Lawrence | 3.3 | 1.4 solo, 1.4 ast, 0.12 sack, 0.31 PD, 0.00 INT |  |
| LB | Uchenna Nwosu | 3.2 | 1.4 solo, 1.1 ast, 0.23 sack, 0.33 PD, 0.00 INT |  |
| DB | Nick Emmanwori | 5.9 | 3.9 solo, 1.2 ast, 0.26 sack, 0.49 PD, 0.05 INT |  |
| DB | Devon Witherspoon | 5.6 | 4.0 solo, 2.0 ast, 0.00 sack, 0.42 PD, 0.05 INT |  |
| DB | Julian Love | 5.5 | 2.6 solo, 1.8 ast, 0.00 sack, 1.05 PD, 0.35 INT |  |

**DEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bo Nix | 16.1 | 192 pass yd, 1.2 TD, 0.8 INT; 4.3 rush, 16 yd |  |
| RB | RJ Harvey | 11.0 | 7.5 car, 28 yd, 0.28 TD; 3.6 rec, 24 yd, 0.12 TD |  |
| RB | J.K. Dobbins | 7.2 | 10.9 car, 41 yd, 0.29 TD; 0.8 rec, 5 yd, 0.02 TD |  |
| RB | Tyler Badie | 2.8 | 1.0 car, 4 yd, 0.01 TD; 1.2 rec, 10 yd, 0.03 TD |  |
| WR | Jaylen Waddle | 8.8 | 3.9 rec, 35 yd, 0.20 TD |  |
| WR | Courtland Sutton | 7.4 | 3.1 rec, 28 yd, 0.25 TD |  |
| WR | Troy Franklin | 4.5 | 2.0 rec, 19 yd, 0.09 TD |  |
| WR | Marvin Mims Jr. | 2.9 | 1.5 rec, 10 yd, 0.04 TD |  |
| TE | Evan Engram | 5.0 | 2.3 rec, 22 yd, 0.10 TD |  |
| TE | Nate Adkins | 2.6 | 0.8 rec, 7 yd, 0.19 TD |  |
| K | Wil Lutz | 8.8 | 1.8 FG, 1.9 XP |  |
| DL | Zach Allen | 3.7 | 1.2 solo, 1.3 ast, 0.50 sack, 0.08 PD, 0.00 INT |  |
| DL | Malcolm Roach | 3.2 | 1.5 solo, 1.5 ast, 0.21 sack, 0.29 PD, 0.00 INT |  |
| LB | Alex Singleton | 6.7 | 4.1 solo, 4.7 ast, 0.00 sack, 0.25 PD, 0.00 INT |  |
| LB | Justin Strnad | 4.2 | 2.5 solo, 2.3 ast, 0.09 sack, 0.36 PD, 0.00 INT |  |
| LB | Nik Bonitto | 4.0 | 1.4 solo, 0.8 ast, 0.61 sack, 0.06 PD, 0.00 INT |  |
| DB | Brandon Jones | 6.3 | 3.7 solo, 1.8 ast, 0.00 sack, 0.58 PD, 0.25 INT |  |
| DB | Ja'Quan McMillian | 4.6 | 2.3 solo, 0.8 ast, 0.21 sack, 0.46 PD, 0.13 INT |  |
| DB | Riley Moss | 3.6 | 2.5 solo, 1.3 ast, 0.05 sack, 1.02 PD, 0.15 INT | Questionable |

### TEN @ IND

Market: IND -7.0, total 44.5. Sim: TEN 18.7, IND 25.6. IND wins 69.7%, TEN wins 30.3%. Median margin +7.1 for IND.

| Team stat | TEN | IND |
|---|---|---|
| Plays | 60 | 62 |
| Pass attempts / completions | 35 / 22 | 31 / 19 |
| Passing yards | 231 | 219 |
| Rush attempts / yards | 23 / 92 | 28 / 103 |
| Sacks taken | 2.2 | 2.5 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.3 / 0.7 | 1.4 / 1.4 |
| Field goals | 1.4 | 1.9 |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 18.0 | 231 pass yd, 1.3 TD, 0.6 INT; 2.3 rush, 10 yd |  |
| RB | Tony Pollard | 10.0 | 13.3 car, 54 yd, 0.38 TD; 1.4 rec, 9 yd, 0.04 TD |  |
| RB | Tyjae Spears | 5.3 | 3.9 car, 15 yd, 0.10 TD; 3.0 rec, 18 yd, 0.06 TD | Questionable |
| RB | Nicholas Singleton | 0.9 | 2.0 car, 8 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Wan'Dale Robinson | 10.6 | 4.1 rec, 36 yd, 0.48 TD |  |
| WR | Carnell Tate | 10.0 | 4.4 rec, 49 yd, 0.13 TD |  |
| WR | Elic Ayomanor | 5.1 | 1.7 rec, 23 yd, 0.19 TD |  |
| WR | Chimere Dike | 4.5 | 1.9 rec, 18 yd, 0.14 TD |  |
| TE | Gunnar Helm | 3.8 | 1.8 rec, 15 yd, 0.09 TD |  |
| TE | Daniel Bellinger | 1.8 | 0.9 rec, 8 yd, 0.02 TD |  |
| K | Joey Slye | 7.0 | 1.4 FG, 1.9 XP |  |
| DL | Jeffery Simmons | 6.1 | 2.6 solo, 2.4 ast, 0.54 sack, 0.42 PD, 0.00 INT |  |
| DL | Jacob Martin | 2.6 | 0.7 solo, 0.2 ast, 0.52 sack, 0.24 PD, 0.00 INT |  |
| LB | Anthony Hill Jr. | 6.4 | 3.5 solo, 5.2 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |
| LB | Cedric Gray | 6.0 | 3.9 solo, 3.2 ast, 0.11 sack, 0.06 PD, 0.00 INT |  |
| LB | Cody Barton | 4.0 | 1.8 solo, 2.9 ast, 0.03 sack, 0.40 PD, 0.02 INT |  |
| DB | Alontae Taylor | 4.7 | 3.5 solo, 1.1 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| DB | Amani Hooker | 3.7 | 3.7 solo, 1.4 ast, 0.00 sack, 0.31 PD, 0.11 INT | Questionable |
| DB | Isaiah Oliver | 3.0 | 2.0 solo, 2.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 17.4 | 219 pass yd, 1.4 TD, 0.6 INT; 2.3 rush, 8 yd |  |
| RB | Jonathan Taylor | 16.4 | 18.6 car, 65 yd, 0.88 TD; 2.3 rec, 22 yd, 0.07 TD |  |
| RB | Seth McGowan | 2.8 | 3.4 car, 13 yd, 0.08 TD; 0.5 rec, 5 yd, 0.02 TD |  |
| RB | DJ Giddens | 1.0 | 1.8 car, 7 yd, 0.04 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Keenan Allen | 9.8 | 3.7 rec, 35 yd, 0.44 TD |  |
| WR | Josh Downs | 6.8 | 3.5 rec, 43 yd, 0.19 TD | Questionable |
| WR | Laquon Treadwell | 4.0 | 1.5 rec, 21 yd, 0.06 TD |  |
| WR | Deion Burks | 1.6 | 0.6 rec, 7 yd, 0.03 TD |  |
| TE | Tyler Warren | 12.0 | 5.0 rec, 43 yd, 0.36 TD |  |
| TE | Mo Alie-Cox | 2.7 | 1.1 rec, 11 yd, 0.10 TD |  |
| K | Spencer Shrader | 11.7 | 2.4 FG, 2.6 XP |  |
| DL | DeForest Buckner | 5.1 | 1.6 solo, 2.4 ast, 0.59 sack, 0.31 PD, 0.00 INT |  |
| DL | Laiatu Latu | 3.8 | 1.5 solo, 1.0 ast, 0.39 sack, 0.42 PD, 0.03 INT |  |
| LB | Akeem Davis-Gaither | 6.6 | 4.3 solo, 4.1 ast, 0.00 sack, 0.20 PD, 0.00 INT |  |
| LB | Germaine Pratt | 5.3 | 2.9 solo, 2.3 ast, 0.00 sack, 0.58 PD, 0.11 INT |  |
| LB | Bryce Boettcher | 2.6 | 1.4 solo, 2.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Justin Walley | 6.2 | 3.5 solo, 2.1 ast, 0.22 sack, 0.59 PD, 0.00 INT |  |
| DB | Camryn Bynum | 4.5 | 3.1 solo, 1.3 ast, 0.04 sack, 0.28 PD, 0.10 INT |  |
| DB | A.J. Haulcy | 3.7 | 2.4 solo, 1.7 ast, 0.00 sack, 0.49 PD, 0.00 INT |  |

### WAS @ SF

Market: SF -7.5, total 51.0. Sim: WAS 21.8, SF 29.2. SF wins 71.4%, WAS wins 28.6%. Median margin +7.4 for SF.

| Team stat | WAS | SF |
|---|---|---|
| Plays | 62 | 61 |
| Pass attempts / completions | 33 / 20 | 31 / 21 |
| Passing yards | 220 | 246 |
| Rush attempts / yards | 27 / 122 | 28 / 128 |
| Sacks taken | 1.9 | 2.0 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.2 / 1.1 | 1.8 / 1.4 |
| Field goals | 1.6 | 2.2 |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 18.8 | 220 pass yd, 1.2 TD, 0.6 INT; 3.3 rush, 20 yd |  |
| RB | Jacory Croskey-Merritt | 7.6 | 9.0 car, 38 yd, 0.44 TD; 0.6 rec, 6 yd, 0.01 TD |  |
| RB | Rachaad White | 6.0 | 4.6 car, 20 yd, 0.11 TD; 1.6 rec, 12 yd, 0.11 TD |  |
| RB | Austin Ekeler | 3.6 | 2.9 car, 13 yd, 0.07 TD; 0.9 rec, 10 yd, 0.03 TD |  |
| WR | Terry McLaurin | 9.7 | 3.7 rec, 47 yd, 0.22 TD |  |
| WR | Stefon Diggs | 6.1 | 3.5 rec, 31 yd, 0.29 TD | Questionable |
| WR | Antonio Williams | 6.0 | 2.6 rec, 26 yd, 0.14 TD |  |
| WR | Treylon Burks | 4.2 | 1.4 rec, 17 yd, 0.19 TD |  |
| TE | Chig Okonkwo | 4.7 | 2.1 rec, 21 yd, 0.07 TD |  |
| TE | John Bates | 2.1 | 1.0 rec, 8 yd, 0.06 TD |  |
| K | Drew Stevens | 8.9 | 1.8 FG, 2.3 XP |  |
| DL | Daron Payne | 3.1 | 1.3 solo, 1.2 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Deatrich Wise | 2.9 | 2.9 solo, 0.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 6.5 | 2.6 solo, 3.9 ast, 0.14 sack, 0.58 PD, 0.19 INT |  |
| LB | Bobby Wagner | 5.1 | 2.7 solo, 2.9 ast, 0.19 sack, 0.21 PD, 0.06 INT |  |
| LB | Frankie Luvu | 4.3 | 2.3 solo, 2.5 ast, 0.13 sack, 0.21 PD, 0.00 INT |  |
| DB | Amik Robertson | 7.7 | 5.1 solo, 1.5 ast, 0.00 sack, 1.48 PD, 0.00 INT |  |
| DB | Rasul Douglas | 6.0 | 4.3 solo, 0.8 ast, 0.00 sack, 0.74 PD, 0.20 INT |  |
| DB | Jeremy Reaves | 5.6 | 3.7 solo, 2.4 ast, 0.00 sack, 0.49 PD, 0.07 INT |  |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 22.9 | 246 pass yd, 1.8 TD, 0.6 INT; 4.4 rush, 21 yd |  |
| RB | Christian McCaffrey | 21.8 | 14.1 car, 65 yd, 0.86 TD; 5.0 rec, 40 yd, 0.25 TD |  |
| RB | Kaelon Black | 4.6 | 6.7 car, 29 yd, 0.18 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| RB | Kyle Juszczyk | 2.8 | 0.0 car, 0 yd, 0.00 TD; 1.3 rec, 15 yd, 0.14 TD | Questionable |
| WR | Mike Evans | 16.5 | 6.1 rec, 77 yd, 0.45 TD |  |
| WR | Brandin Cooks | 4.0 | 1.1 rec, 11 yd, 0.30 TD |  |
| WR | Jacob Cowing | 1.8 | 0.7 rec, 8 yd, 0.04 TD |  |
| WR | Jordan Watkins | 1.2 | 0.5 rec, 7 yd, 0.01 TD |  |
| TE | George Kittle | 15.4 | 5.8 rec, 67 yd, 0.48 TD |  |
| TE | Luke Farrell | 1.2 | 0.5 rec, 5 yd, 0.03 TD |  |
| K | Eddy Pineiro | 8.1 | 1.4 FG, 3.0 XP |  |
| DL | Gracen Halton | 4.9 | 1.9 solo, 1.4 ast, 0.29 sack, 0.23 PD, 0.00 INT |  |
| DL | Sebastian Valdez | 3.1 | 1.4 solo, 1.3 ast, 0.37 sack, 0.00 PD, 0.00 INT |  |
| LB | Fred Warner | 9.1 | 4.4 solo, 5.5 ast, 0.08 sack, 0.58 PD, 0.00 INT |  |
| LB | Jaden Dugger | 4.2 | 2.6 solo, 1.5 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| LB | Tatum Bethune | 3.9 | 1.8 solo, 2.6 ast, 0.13 sack, 0.40 PD, 0.00 INT |  |
| DB | Ji'Ayir Brown | 5.7 | 3.4 solo, 2.9 ast, 0.00 sack, 0.45 PD, 0.07 INT |  |
| DB | Renardo Green | 5.6 | 2.8 solo, 1.5 ast, 0.00 sack, 0.85 PD, 0.39 INT |  |
| DB | Malik Mustapha | 4.4 | 2.6 solo, 1.9 ast, 0.00 sack, 0.40 PD, 0.03 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: SEA: Drake Thomas, SEA: Zach Charbonnet, SEA: Chazz Surratt, SEA: Jadarian Price, SEA: Jake Bobo, SEA: Coby Bryant, SEA: Robbie Ouzts, SEA: Julian Neal, DEN: Jonathon Cooper, DEN: Pat Surtain II, DEN: Pat Bryant, DEN: Jonah Coleman, DEN: Talanoa Hufanga, HOU: Damone Clark, HOU: David Montgomery, HOU: Ja'Marcus Ingram, HOU: Christian Kirk, HOU: Jayden Higgins, HOU: Mario Edwards, HOU: Jalen Pitre, HOU: British Brooks, HOU: E.J. Speed, HOU: Henry To'oTo'o, HOU: Jaylin Smith, HOU: Dylan Horton, JAX: BJ Green II, JAX: Caleb Ransaw, CHI: Nikola Kalinic, CHI: T.J. Edwards, CHI: Dayo Odeyingbo, CHI: Ruben Hyppolite II, CHI: Joe Tryon-Shoyinka, CHI: Kyler Gordon, CHI: Brittain Brown, ATL: Yasir Abdullah, ATL: JD Bertrand, ATL: A.J. Terrell, ATL: Jalon Walker, ATL: Ronnie Harrison, ATL: James Pearce Jr., ATL: David Sills, BAL: Ja'Kobi Lane, BAL: T.J. Tampa, BAL: Durham Smythe, BAL: Jacob Hummel, CLE: Dylan Sampson, CLE: Mason Graham, CLE: Alex Wright, CLE: Nathaniel Watson, CLE: Myles Garrett, CLE: Raheim Sanders, CLE: Dillon Gabriel, TEN: Jaylen Harrell, TEN: Kevin Winston Jr., TEN: Darrell Baker Jr., TEN: Kendell Brooks, IND: Arden Key, IND: Cameron Mitchell, IND: Alec Pierce, NYJ: Breece Hall, NYJ: Marcelino McCrary-Ball, NYJ: Tyler Baron, NYJ: Omar Cooper Jr., NYJ: Micheal Clemons, NYJ: Ja'Sir Taylor, NYJ: Adonai Mitchell, NYJ: Arian Smith, NYJ: Joseph Ossai, NYJ: Tre Brown, NYJ: David Onyemata, NYJ: Braiden McGregor, NE: Harold Landry III, NE: Reggie Gilliam, NE: Dell Pettus, NE: Bryce Baringer, NE: Mack Hollins, NE: Quintayvious Hutchins, NE: A.J. Brown, NO: Moliki Matavao, NO: Travis Etienne, NO: Bryan Bresee, NO: Mason Tipton, NYG: Elijah Chatman, NYG: Brian Burns, NYG: Paulson Adebo, NYG: Korie Black, NYG: Jaxson Dart, NYG: Braxton Berrios, NYG: Roy Robertson-Harris, NYG: Jarrick Bernard-Converse, NYG: Gunner Olszewski, NYG: DJ Davidson, NYG: Chauncey Golston, CAR: Mike Jackson, CAR: Xavier Legette, CAR: Jaycee Horn, CAR: Cam Jackson, CAR: LaBryan Ray, CAR: Trevor Etienne, CAR: Tershawn Wharton, CAR: Jonathon Brooks, CAR: Bam Martin-Scott, CAR: Nic Scourton, PHI: Jakorian Bennett, PHI: Jalyx Hunt, PHI: Tank Bigsby, PHI: Grant Calcaterra, PHI: Jalen Hurts, PHI: Will Shipley, PIT: Michael Pittman, PIT: Calvin Austin III, PIT: Derrick Harmon, PIT: Trey Sermon, PIT: Darius Slay, PIT: Adam Thielen, PIT: Ben Skowronek, PIT: Roman Wilson, TB: Markees Watts, TB: Teddy Bridgewater, TB: Jalen McMillan, TB: Antoine Winfield Jr., TB: Baker Mayfield, ARI: Zachary Carter, ARI: Kitan Crawford, ARI: Will Johnson, ARI: Hunter Long, LA: Ahkello Witherspoon, LA: Terrance Ferguson, LA: Darious Williams, LA: Ronnie Rivers, LAC: KeAndre Lambert-Smith, LAC: Tre Harris, LAC: David Njoku, LAC: Denzel Perryman, LAC: Trey Lance, LAC: Da'Shawn Hand, KC: Isiah Pacheco, KC: Joshua Williams, KC: Tyquan Thornton, KC: Cooper McDonald, BUF: Tyrell Shavers, BUF: Jordan Hancock, LV: Jack Bech, LV: Dont'e Thornton Jr., LV: Jamal Adams, LV: Carter Runyon, DAL: Jalen Thompson, DAL: Marist Liufau, DAL: P.J. Locke, DAL: Jonathan Bullard, DAL: Malik Davis, GB: Warren Brinson, GB: Micah Parsons, GB: Savion Williams, GB: Josh Jacobs, GB: Collin Oliver, GB: Luke Musgrave, GB: Nate Hobbs, GB: Jayden Reed, GB: Chris Brooks, GB: Edgerrin Cooper, GB: Jordon Riley, GB: Javon Hargrave, WAS: Jer'Zhan Newton, WAS: Nick Bellore, WAS: Jeremy McNichols, WAS: Marcus Mariota, WAS: Leo Chenal, WAS: Trey Amos, WAS: Jaylin Lane, WAS: Jordan Magee, SF: Alfred Collins, SF: Jake Tonges, SF: Kalia Davis, SF: Nick Martin, SF: Sam Okuayinonu, SF: Isaac Guerendo, SF: Ricky Pearsall, SF: Deebo Samuel Sr., SF: Dre Greenlaw, SF: Demarcus Robinson, SF: C.J. West, SF: Marques Sigle, SF: Garret Wallow.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.9 | 9.3 to 38.1 |
| QB | Brock Purdy | SF | 20.8 | 8.3 to 34.4 |
| QB | Matthew Stafford | LA | 20.3 | 7.8 to 33.8 |
| QB | Drake Maye | NE | 19.9 | 7.8 to 33.3 |
| QB | Dak Prescott | DAL | 18.7 | 7.0 to 31.3 |
| QB | Jordan Love | GB | 18.1 | 7.0 to 30.5 |
| RB | Bijan Robinson | ATL | 23.6 | 9.0 to 39.6 |
| RB | Christian McCaffrey | SF | 22.4 | 8.6 to 38.3 |
| RB | Jaylen Warren | PIT | 21.3 | 7.6 to 36.4 |
| RB | Kyren Williams | LA | 19.3 | 6.4 to 34.1 |
| RB | Derrick Henry | BAL | 18.4 | 5.1 to 32.6 |
| RB | Kenneth Walker III | KC | 17.9 | 5.8 to 31.9 |
| RB | Jonathan Taylor | IND | 16.9 | 4.8 to 31.0 |
| RB | James Cook | BUF | 16.4 | 4.5 to 29.6 |
| RB | Ashton Jeanty | LV | 15.5 | 4.9 to 27.2 |
| RB | Emanuel Wilson | SEA | 14.6 | 3.4 to 27.9 |
| WR | Jaxon Smith-Njigba | SEA | 20.3 | 7.1 to 36.0 |
| WR | Puka Nacua | LA | 19.0 | 5.7 to 34.6 |
| WR | Mike Evans | SF | 17.3 | 4.8 to 32.2 |
| WR | CeeDee Lamb | DAL | 16.6 | 4.8 to 30.9 |
| WR | Zay Flowers | BAL | 15.1 | 3.9 to 28.8 |
| WR | Christian Watson | GB | 14.1 | 2.2 to 28.5 |
| WR | Drake London | ATL | 13.9 | 3.2 to 27.6 |
| WR | George Pickens | DAL | 13.7 | 3.2 to 26.7 |
| WR | Tetairoa McMillan | CAR | 13.4 | 3.0 to 25.9 |
| WR | Nico Collins | HOU | 13.3 | 2.7 to 26.2 |
| WR | Parker Washington | JAX | 13.3 | 2.4 to 26.4 |
| WR | DK Metcalf | PIT | 12.9 | 2.7 to 25.1 |
| TE | George Kittle | SF | 15.9 | 4.0 to 30.6 |
| TE | Trey McBride | ARI | 12.9 | 3.8 to 23.8 |
| TE | Tyler Warren | IND | 12.2 | 2.5 to 23.3 |
| TE | Pat Freiermuth | PIT | 11.0 | 2.0 to 21.8 |
| TE | Travis Kelce | KC | 10.7 | 1.6 to 21.7 |
| TE | Hunter Henry | NE | 10.3 | 1.6 to 20.7 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.2 | 9.4 to 36.7 |
| QB | Brock Purdy | SF | 20.0 | 8.4 to 32.6 |
| QB | Matthew Stafford | LA | 19.2 | 8.0 to 31.8 |
| QB | Drake Maye | NE | 19.0 | 8.0 to 31.4 |
| QB | Dak Prescott | DAL | 17.7 | 7.2 to 29.4 |
| QB | Jordan Love | GB | 17.3 | 7.2 to 28.4 |
| RB | Bijan Robinson | ATL | 20.3 | 7.7 to 34.2 |
| RB | Christian McCaffrey | SF | 19.3 | 6.8 to 34.0 |
| RB | Jaylen Warren | PIT | 18.5 | 6.4 to 32.0 |
| RB | Kyren Williams | LA | 17.1 | 5.4 to 30.6 |
| RB | Derrick Henry | BAL | 16.4 | 5.0 to 29.5 |
| RB | Kenneth Walker III | KC | 15.9 | 4.9 to 28.5 |
| RB | Jonathan Taylor | IND | 15.2 | 4.2 to 28.1 |
| RB | James Cook | BUF | 14.8 | 4.1 to 26.8 |
| RB | Ashton Jeanty | LV | 13.4 | 3.9 to 24.4 |
| RB | Emanuel Wilson | SEA | 13.4 | 3.1 to 25.8 |
| WR | Jaxon Smith-Njigba | SEA | 15.5 | 4.9 to 27.7 |
| WR | Puka Nacua | LA | 15.0 | 4.0 to 27.4 |
| WR | Mike Evans | SF | 13.4 | 3.3 to 24.8 |
| WR | CeeDee Lamb | DAL | 12.9 | 3.3 to 24.2 |
| WR | Zay Flowers | BAL | 11.7 | 2.7 to 22.6 |
| WR | Christian Watson | GB | 11.7 | 1.4 to 23.4 |
| WR | Drake London | ATL | 10.8 | 2.3 to 20.8 |
| WR | George Pickens | DAL | 10.7 | 2.1 to 20.6 |
| WR | Nico Collins | HOU | 10.6 | 1.7 to 21.1 |
| WR | Parker Washington | JAX | 10.6 | 1.5 to 21.0 |
| WR | Tetairoa McMillan | CAR | 10.5 | 2.0 to 20.2 |
| WR | DK Metcalf | PIT | 10.1 | 1.7 to 19.7 |
| TE | George Kittle | SF | 12.4 | 2.6 to 23.7 |
| TE | Trey McBride | ARI | 9.5 | 2.2 to 18.3 |
| TE | Tyler Warren | IND | 9.5 | 1.4 to 19.1 |
| TE | Pat Freiermuth | PIT | 8.8 | 1.1 to 18.3 |
| TE | Travis Kelce | KC | 8.5 | 0.8 to 17.9 |
| TE | Hunter Henry | NE | 8.1 | 0.9 to 16.6 |
| K | Spencer Shrader | IND | 10.8 | 1.0 to 23.0 |
| K | Ka'imi Fairbairn | HOU | 9.9 | 1.0 to 22.4 |
| K | Jason Myers | SEA | 9.4 | 1.0 to 21.4 |
| K | Matt Gay | LV | 9.1 | 1.0 to 19.6 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses came from MFL at the time of the pull. Re-run Thursday morning and Sunday morning for fresh news.
- Weather, referee tendencies and in-game injuries are not modeled.