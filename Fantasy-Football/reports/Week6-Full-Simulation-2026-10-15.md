# Week 6 Full Simulation Report - 15 OCT 2026

Decision support only. Nothing was submitted anywhere. Every number comes from 4,000 simulated versions of each game, built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.

## 1. Winners and pick'em

The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.

| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |
|---|---|---|---|---|---|---|
| SEA @ DEN | SEA 57.4% | SEA 21.7 - DEN 19.0 | DEN | 53.1% | SEA | 57.8% |
| HOU @ JAX | JAX 57.7% | HOU 20.0 - JAX 22.5 | JAX | 50.0% | JAX | 57.8% |
| CHI @ ATL | CHI 51.6% | CHI 25.8 - ATL 25.1 | ATL | 57.8% | CHI | 53.1% |
| BAL @ CLE | BAL 64.6% | BAL 23.6 - CLE 18.8 | BAL | 51.6% | BAL | 65.3% |
| TEN @ IND | IND 68.3% | TEN 19.1 - IND 25.5 | IND | 48.4% | IND | 70.9% |
| NYJ @ NE | NE 70.7% | NYJ 18.4 - NE 25.4 | NE | 48.4% | NE | 70.9% |
| NO @ NYG | NO 52.7% | NO 23.5 - NYG 22.6 | NYG | 51.6% | NYG | 46.9% |
| CAR @ PHI | CAR 52.2% | CAR 20.1 - PHI 19.2 | CAR | 57.8% | CAR | 53.1% |
| PIT @ TB | PIT 57.8% | PIT 20.9 - TB 18.7 | PIT | 50.0% | PIT | 57.8% |
| ARI @ LA | LA 82.8% | ARI 19.3 - LA 31.8 | ARI | 50.0% | LAR | 83.7% |
| LAC @ KC | KC 73.5% | LAC 17.2 - KC 25.3 | KC | 48.4% | KC | 73.5% |
| BUF @ LV | BUF 62.3% | BUF 28.9 - LV 24.6 | LV | 56.2% | BUF | 63.8% |
| DAL @ GB | GB 55.1% | DAL 25.7 - GB 27.4 | GB | 50.0% | GB | 54.7% |
| WAS @ SF | SF 73.1% | WAS 21.4 - SF 29.2 | WSH | 50.0% | SF | 72.2% |

**Flag:** the straight-up pick NYG in NO @ NYG is the market underdog (46.9%). It is a coin flip; the other side is the market favorite. Your call.

**Eliminator (fresh start this week, every team open):** best win chances are LA Rams 83.7%, KC 73.5%, SF 72.2%, IND and NE 70.9%. Surviving all season means saving the biggest favorites for the weeks with weaker options, so the Rams are the safe pick now but not automatically the smart one. I can plan the full 18 weeks once the schedule odds are loaded.

## 2. Five IRFL lineups (Golden active)

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 127.5 | 96.3 | 160.1 |
| 2 SAFE (protects a lead) | 127.4 | 96.8 | 159.7 |
| 3 BALANCED UPSIDE (75th percentile) | 127.5 | 96.3 | 160.1 |
| 4 SWING (90th percentile, for an underdog) | 124.9 | 92.5 | 158.6 |
| 5 CONTINGENCY (every Questionable out) | 127.4 | 96.8 | 159.7 |
| Week 6 sheet lineup (for comparison) | 116.9 | 87.0 | 147.8 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.6 | 4.0 to 33.5 |  |
| RB | Robinson, Brian | ATL | 8.4 | 0.7 to 18.1 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.4 | 0.8 to 16.2 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.1 |  |
| WR | Allen, Keenan | IND | 10.0 | 1.3 to 20.3 |  |
| WR | Golden, Matthew | GBP | 9.4 | 0.9 to 19.2 |  |
| WR | Flournoy, Ryan | DAL | 7.9 | 0.4 to 16.4 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.8 |  |
| DL | Davis, Jordan | PHI | 3.1 | 1.0 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.4 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.4 | 2.0 to 9.5 |  |
| DB | Kinchens, Kamren | LAR | 5.2 | 2.0 to 9.0 |  |
| DB | Moss, Riley | DEN | 3.5 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.6 | 4.0 to 33.5 |  |
| RB | Robinson, Brian | ATL | 8.4 | 0.7 to 18.1 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.4 | 0.8 to 16.2 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.1 |  |
| WR | Allen, Keenan | IND | 10.0 | 1.3 to 20.3 |  |
| WR | Golden, Matthew | GBP | 9.4 | 0.9 to 19.2 |  |
| WR | Flournoy, Ryan | DAL | 7.9 | 0.4 to 16.4 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.8 |  |
| DL | Davis, Jordan | PHI | 3.1 | 1.0 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.4 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.4 | 2.0 to 9.5 |  |
| DB | Kinchens, Kamren | LAR | 5.2 | 2.0 to 9.0 |  |
| DB | Jenkins, Rayshawn | PIT | 3.4 | 1.0 to 6.0 | differs from lineup 1 |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.6 | 4.0 to 33.5 |  |
| RB | Robinson, Brian | ATL | 8.4 | 0.7 to 18.1 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.4 | 0.8 to 16.2 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.1 |  |
| WR | Allen, Keenan | IND | 10.0 | 1.3 to 20.3 |  |
| WR | Golden, Matthew | GBP | 9.4 | 0.9 to 19.2 |  |
| WR | Flournoy, Ryan | DAL | 7.9 | 0.4 to 16.4 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.8 |  |
| DL | Davis, Jordan | PHI | 3.1 | 1.0 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.4 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Kinchens, Kamren | LAR | 5.2 | 2.0 to 9.0 |  |
| DB | Scott, Nick | CAR | 5.4 | 2.0 to 9.5 |  |
| DB | Moss, Riley | DEN | 3.5 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Williams, Caleb | CHI | 15.0 | -3.1 to 33.9 | Questionable, plays about 75% of sims. differs from lineup 1 |
| RB | Robinson, Brian | ATL | 8.4 | 0.7 to 18.1 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.4 | 0.8 to 16.2 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.1 |  |
| WR | Allen, Keenan | IND | 10.0 | 1.3 to 20.3 |  |
| WR | Golden, Matthew | GBP | 9.4 | 0.9 to 19.2 |  |
| WR | Flournoy, Ryan | DAL | 7.9 | 0.4 to 16.4 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.8 |  |
| DL | Davis, Jordan | PHI | 3.1 | 1.0 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.4 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.4 | 2.0 to 9.5 |  |
| DB | Kinchens, Kamren | LAR | 5.2 | 2.0 to 9.0 |  |
| DB | Moss, Riley | DEN | 3.5 | 0.0 to 8.0 | Questionable, plays about 75% of sims. |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Brissett, Jacoby | ARI | 17.6 | 4.0 to 33.5 |  |
| RB | Robinson, Brian | ATL | 8.4 | 0.7 to 18.1 |  |
| RB | Croskey-Merritt, Jacory | WAS | 7.4 | 0.8 to 16.2 |  |
| WR | Flowers, Zay | BAL | 14.5 | 4.1 to 26.1 |  |
| WR | Allen, Keenan | IND | 10.0 | 1.3 to 20.3 |  |
| WR | Golden, Matthew | GBP | 9.4 | 0.9 to 19.2 |  |
| WR | Flournoy, Ryan | DAL | 7.9 | 0.4 to 16.4 |  |
| TE | Schultz, Dalton | HOU | 9.2 | 1.7 to 17.6 |  |
| PK | Folk, Nick | ATL | 9.3 | 1.0 to 20.8 |  |
| DL | Davis, Jordan | PHI | 3.1 | 1.0 to 6.0 |  |
| DL | Kancey, Calijah | TBB | 0.7 | 0.0 to 2.0 |  |
| LB | Okereke, Bobby | CAR | 6.4 | 2.5 to 11.0 |  |
| LB | Gibbens, Jack | ARI | 5.2 | 2.0 to 9.0 |  |
| LB | Strnad, Justin | DEN | 4.2 | 1.0 to 8.0 |  |
| DB | Scott, Nick | CAR | 5.4 | 2.0 to 9.5 |  |
| DB | Kinchens, Kamren | LAR | 5.2 | 2.0 to 9.0 |  |
| DB | Jenkins, Rayshawn | PIT | 3.4 | 1.0 to 6.0 | differs from lineup 1 |

Lineups 1 and 3 are identical; 2 and 5 are identical. Your roster has few real choices this week (the only live decisions are QB, the last DB slot and the last WR slot), so the five lineups collapse. Averages shift by about half a point between runs because the dice differ.

Not simulated this week (bye, no team, or no recent usage): Reed, D.J. (DET); Wonnum, D.J. (DET); Hutchinson, Aidan (DET); Andersen, Troy (FA); McPherson, Evan (CIN); Bates, Jake (DET); Goff, Jared (DET); Anderson, Zayne (MIA); LaPorta, Sam (DET); Hockenson, T.J. (MIN); Jefferson, Justin (MIN); Williams, Jameson (DET).

When the two free agents land (a safety and a defensive end), I will add them for Week 7. Defensive line is the thinnest group: Davis and Kancey are the only two playable linemen this week.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ LA

Market: LA -12.5, total 51.5. Sim: ARI 19.3, LA 31.8. LA wins 82.8%, ARI wins 17.2%. Median margin +12.5 for LA.

| Team stat | ARI | LA |
|---|---|---|
| Plays | 64 | 65 |
| Pass attempts / completions | 38 / 25 | 34 / 22 |
| Passing yards | 240 | 273 |
| Rush attempts / yards | 23 / 97 | 29 / 136 |
| Sacks taken | 2.5 | 2.2 |
| Interceptions thrown | 0.9 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.6 | 2.0 / 1.5 |
| Field goals | 1.5 | 2.4 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 17.6 | 240 pass yd, 1.4 TD, 0.9 INT; 2.3 rush, 10 yd |  |
| RB | Jeremiyah Love | 5.8 | 9.5 car, 38 yd, 0.21 TD; 1.4 rec, 8 yd, 0.07 TD | Questionable |
| RB | Tyler Allgeier | 5.4 | 4.5 car, 19 yd, 0.16 TD; 1.5 rec, 9 yd, 0.03 TD |  |
| RB | Michael Carter | 4.6 | 3.9 car, 17 yd, 0.06 TD; 1.3 rec, 11 yd, 0.03 TD |  |
| WR | Michael Wilson | 10.8 | 4.6 rec, 48 yd, 0.25 TD |  |
| WR | Kendrick Bourne | 5.6 | 2.7 rec, 27 yd, 0.06 TD |  |
| WR | Reggie Virgil | 4.0 | 1.8 rec, 19 yd, 0.06 TD |  |
| WR | Marvin Harrison Jr. | 3.0 | 1.1 rec, 13 yd, 0.09 TD |  |
| TE | Trey McBride | 12.6 | 6.2 rec, 48 yd, 0.28 TD |  |
| TE | Teagan Quitoriano | 3.8 | 0.9 rec, 9 yd, 0.35 TD |  |
| K | Chad Ryland | 7.6 | 1.5 FG, 1.9 XP |  |
| DL | Roy Lopez | 4.4 | 2.0 solo, 3.0 ast, 0.29 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.9 | 1.3 solo, 2.1 ast, 0.12 sack, 0.00 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.8 | 3.2 solo, 4.1 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.2 | 2.5 solo, 4.6 ast, 0.07 sack, 0.18 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.8 | 1.8 solo, 1.0 ast, 0.16 sack, 0.23 PD, 0.00 INT |  |
| DB | Budda Baker | 7.8 | 4.0 solo, 3.7 ast, 0.32 sack, 0.50 PD, 0.18 INT |  |
| DB | Denzel Burke | 4.3 | 2.3 solo, 1.3 ast, 0.00 sack, 0.65 PD, 0.23 INT |  |
| DB | Andrew Wingard | 3.6 | 2.2 solo, 3.0 ast, 0.00 sack, 0.17 PD, 0.18 INT | Questionable |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 22.5 | 273 pass yd, 2.0 TD, 0.7 INT; 1.7 rush, 7 yd |  |
| RB | Kyren Williams | 18.7 | 15.3 car, 73 yd, 0.84 TD; 3.1 rec, 25 yd, 0.16 TD |  |
| RB | Blake Corum | 9.0 | 9.1 car, 44 yd, 0.46 TD; 0.9 rec, 9 yd, 0.03 TD |  |
| WR | Puka Nacua | 18.4 | 0.9 car, 4 yd, 0.09 TD; 6.5 rec, 78 yd, 0.53 TD |  |
| WR | Davante Adams | 11.7 | 3.5 rec, 50 yd, 0.52 TD |  |
| WR | Konata Mumpfield | 3.4 | 1.1 rec, 15 yd, 0.12 TD |  |
| WR | Xavier Smith | 1.8 | 0.7 rec, 10 yd, 0.03 TD |  |
| TE | Tyler Higbee | 7.4 | 2.7 rec, 34 yd, 0.22 TD |  |
| TE | Colby Parkinson | 5.1 | 1.8 rec, 18 yd, 0.25 TD |  |
| K | Harrison Mevis | 8.6 | 1.4 FG, 3.3 XP |  |
| DL | Kobie Turner | 4.2 | 1.5 solo, 2.0 ast, 0.31 sack, 0.40 PD, 0.08 INT |  |
| DL | Poona Ford | 2.3 | 1.1 solo, 1.4 ast, 0.07 sack, 0.17 PD, 0.00 INT |  |
| LB | Byron Young | 5.5 | 2.1 solo, 2.3 ast, 0.68 sack, 0.00 PD, 0.00 INT |  |
| LB | Omar Speights | 5.3 | 2.9 solo, 2.5 ast, 0.26 sack, 0.16 PD, 0.00 INT |  |
| LB | Nate Landman | 5.2 | 3.8 solo, 3.8 ast, 0.06 sack, 0.20 PD, 0.05 INT | Questionable |
| DB | Quentin Lake | 6.2 | 3.6 solo, 2.1 ast, 0.00 sack, 0.94 PD, 0.12 INT |  |
| DB | Kamren Kinchens | 5.2 | 3.4 solo, 2.0 ast, 0.09 sack, 0.30 PD, 0.08 INT |  |
| DB | Kam Curl | 5.2 | 3.5 solo, 2.1 ast, 0.05 sack, 0.34 PD, 0.00 INT |  |

### BAL @ CLE

Market: CLE +5.0, total 42.5. Sim: BAL 23.6, CLE 18.8. CLE wins 35.4%, BAL wins 64.6%. Median margin -4.9 for CLE.

| Team stat | BAL | CLE |
|---|---|---|
| Plays | 61 | 62 |
| Pass attempts / completions | 28 / 19 | 35 / 21 |
| Passing yards | 207 | 234 |
| Rush attempts / yards | 30 / 154 | 25 / 97 |
| Sacks taken | 2.6 | 2.2 |
| Interceptions thrown | 0.5 | 0.8 |
| Passing / rushing TDs | 1.2 / 1.3 | 1.2 / 0.8 |
| Field goals | 1.7 | 1.4 |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Lamar Jackson | 13.8 | 154 pass yd, 0.9 TD, 0.4 INT; 3.9 rush, 22 yd | Questionable |
| RB | Derrick Henry | 17.3 | 19.4 car, 96 yd, 0.90 TD; 1.1 rec, 9 yd, 0.09 TD |  |
| RB | Justice Hill | 3.9 | 2.3 car, 14 yd, 0.06 TD; 1.1 rec, 9 yd, 0.04 TD |  |
| RB | Rasheen Ali | 1.2 | 0.3 car, 1 yd, 0.00 TD; 0.5 rec, 4 yd, 0.03 TD |  |
| WR | Zay Flowers | 14.5 | 5.5 rec, 66 yd, 0.34 TD |  |
| WR | Rashod Bateman | 4.0 | 2.2 rec, 25 yd, 0.11 TD | Questionable |
| WR | Devontez Walker | 2.7 | 0.9 rec, 11 yd, 0.12 TD |  |
| WR | Chris Moore | 2.5 | 0.9 rec, 10 yd, 0.12 TD |  |
| TE | Mark Andrews | 7.4 | 3.6 rec, 27 yd, 0.17 TD |  |
| TE | Matthew Hibner | 2.0 | 1.0 rec, 10 yd, 0.10 TD | Questionable |
| K | Tyler Loop | 8.9 | 1.7 FG, 2.4 XP |  |
| DL | Travis Jones | 3.5 | 1.3 solo, 1.4 ast, 0.29 sack, 0.17 PD, 0.00 INT |  |
| DL | Nnamdi Madubuike | 2.2 | 1.6 solo, 1.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Roquan Smith | 6.7 | 3.4 solo, 4.5 ast, 0.11 sack, 0.15 PD, 0.08 INT |  |
| LB | Trenton Simpson | 6.0 | 3.4 solo, 2.5 ast, 0.22 sack, 0.13 PD, 0.13 INT |  |
| LB | Tavius Robinson | 4.8 | 1.7 solo, 1.4 ast, 0.60 sack, 0.32 PD, 0.00 INT |  |
| DB | Kyle Hamilton | 7.4 | 4.5 solo, 2.4 ast, 0.03 sack, 0.81 PD, 0.15 INT |  |
| DB | Malaki Starks | 5.1 | 3.4 solo, 2.0 ast, 0.09 sack, 0.13 PD, 0.03 INT |  |
| DB | Marlon Humphrey | 4.2 | 3.1 solo, 1.2 ast, 0.04 sack, 0.78 PD, 0.21 INT | Questionable |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Shedeur Sanders | 16.0 | 234 pass yd, 1.2 TD, 0.8 INT; 1.5 rush, 8 yd |  |
| RB | Quinshon Judkins | 8.7 | 13.0 car, 44 yd, 0.36 TD; 2.8 rec, 19 yd, 0.07 TD | Questionable |
| RB | Trayveon Williams | 2.1 | 0.9 car, 4 yd, 0.02 TD; 0.8 rec, 7 yd, 0.02 TD |  |
| RB | Jaleel McLaughlin | 1.9 | 0.5 car, 2 yd, 0.18 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | Denzel Boston | 7.7 | 3.3 rec, 49 yd, 0.31 TD | Questionable |
| WR | Jerry Jeudy | 5.9 | 2.6 rec, 26 yd, 0.12 TD |  |
| WR | KC Concepcion | 5.1 | 0.6 car, 3 yd, 0.01 TD; 3.3 rec, 27 yd, 0.09 TD | Questionable |
| WR | Isaiah Bond | 3.7 | 1.3 rec, 20 yd, 0.03 TD |  |
| TE | Harold Fannin Jr. | 9.3 | 3.6 rec, 33 yd, 0.35 TD |  |
| TE | Blake Whiteheart | 1.3 | 0.4 rec, 4 yd, 0.08 TD |  |
| K | Andre Szmyt | 8.6 | 1.8 FG, 1.9 XP |  |
| DL | Sam Williams | 3.1 | 1.7 solo, 1.2 ast, 0.20 sack, 0.20 PD, 0.00 INT |  |
| DL | Adin Huntington | 2.5 | 0.6 solo, 2.0 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| LB | Quincy Williams | 6.9 | 3.4 solo, 3.2 ast, 0.00 sack, 0.41 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 5.6 | 3.5 solo, 5.4 ast, 0.21 sack, 0.19 PD, 0.03 INT | Questionable |
| LB | Jerome Baker | 1.4 | 0.4 solo, 1.5 ast, 0.02 sack, 0.00 PD, 0.00 INT |  |
| DB | Ronnie Hickman Jr. | 5.1 | 2.2 solo, 3.0 ast, 0.09 sack, 0.43 PD, 0.11 INT |  |
| DB | Tyson Campbell | 4.2 | 2.9 solo, 1.7 ast, 0.00 sack, 0.44 PD, 0.00 INT |  |
| DB | Denzel Ward | 4.2 | 2.3 solo, 1.4 ast, 0.00 sack, 0.37 PD, 0.13 INT |  |

### BUF @ LV

Market: LV +4.5, total 53.5. Sim: BUF 28.9, LV 24.6. LV wins 37.7%, BUF wins 62.3%. Median margin -4.2 for LV.

| Team stat | BUF | LV |
|---|---|---|
| Plays | 62 | 61 |
| Pass attempts / completions | 30 / 20 | 35 / 23 |
| Passing yards | 238 | 234 |
| Rush attempts / yards | 30 / 150 | 24 / 90 |
| Sacks taken | 2.4 | 2.0 |
| Interceptions thrown | 0.6 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.6 | 1.6 / 1.0 |
| Field goals | 2.2 | 1.8 |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.6 | 238 pass yd, 1.5 TD, 0.6 INT; 7.2 rush, 38 yd |  |
| RB | James Cook | 15.4 | 16.2 car, 81 yd, 0.76 TD; 1.3 rec, 11 yd, 0.08 TD |  |
| RB | Ty Johnson | 5.0 | 2.1 car, 9 yd, 0.12 TD; 2.0 rec, 23 yd, 0.12 TD | Questionable |
| RB | Ray Davis | 3.1 | 2.7 car, 13 yd, 0.07 TD; 0.5 rec, 6 yd, 0.04 TD |  |
| WR | Khalil Shakir | 7.7 | 3.3 rec, 37 yd, 0.13 TD |  |
| WR | Keon Coleman | 6.2 | 2.1 rec, 28 yd, 0.23 TD |  |
| WR | DJ Moore | 4.7 | 2.3 rec, 28 yd, 0.18 TD | Questionable |
| WR | Skyler Bell | 3.2 | 1.4 rec, 15 yd, 0.07 TD |  |
| TE | Dalton Kincaid | 6.0 | 2.2 rec, 30 yd, 0.14 TD |  |
| TE | Dawson Knox | 4.3 | 1.8 rec, 16 yd, 0.15 TD |  |
| K | Tyler Bass | 9.6 | 1.8 FG, 2.9 XP |  |
| DL | Deone Walker | 2.9 | 1.2 solo, 1.6 ast, 0.10 sack, 0.60 PD, 0.00 INT |  |
| DL | DeWayne Carter | 2.7 | 1.5 solo, 1.0 ast, 0.26 sack, 0.00 PD, 0.00 INT |  |
| LB | Greg Rousseau | 6.2 | 1.9 solo, 1.5 ast, 0.89 sack, 0.36 PD, 0.00 INT |  |
| LB | Terrel Bernard | 4.8 | 3.1 solo, 2.6 ast, 0.00 sack, 0.19 PD, 0.00 INT |  |
| LB | Dorian Williams | 4.2 | 2.1 solo, 3.8 ast, 0.00 sack, 0.13 PD, 0.00 INT |  |
| DB | Cole Bishop | 5.3 | 3.7 solo, 2.6 ast, 0.00 sack, 0.06 PD, 0.06 INT |  |
| DB | Christian Benford | 5.2 | 2.9 solo, 1.4 ast, 0.07 sack, 0.69 PD, 0.11 INT |  |
| DB | C.J. Gardner-Johnson | 5.2 | 3.2 solo, 1.9 ast, 0.00 sack, 0.39 PD, 0.22 INT |  |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 18.2 | 234 pass yd, 1.6 TD, 0.8 INT; 1.6 rush, 6 yd |  |
| RB | Ashton Jeanty | 15.3 | 14.4 car, 50 yd, 0.44 TD; 3.6 rec, 30 yd, 0.23 TD |  |
| RB | Mike Washington Jr. | 4.2 | 3.8 car, 16 yd, 0.29 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| RB | Dylan Laube | 2.0 | 0.6 car, 2 yd, 0.20 TD; 0.3 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 8.0 | 0.6 car, 2 yd, 0.01 TD; 3.2 rec, 35 yd, 0.18 TD |  |
| WR | Cody White | 4.3 | 1.4 rec, 17 yd, 0.21 TD |  |
| WR | Tyler Lockett | 3.3 | 1.4 rec, 13 yd, 0.10 TD |  |
| WR | Jalen Nailor | 2.1 | 1.3 rec, 12 yd, 0.06 TD | Questionable |
| TE | Brock Bowers | 9.2 | 4.7 rec, 49 yd, 0.43 TD | Questionable |
| TE | Michael Mayer | 6.5 | 3.1 rec, 26 yd, 0.15 TD |  |
| K | Matt Gay | 9.7 | 1.9 FG, 2.5 XP |  |
| DL | Maxx Crosby | 4.0 | 1.4 solo, 1.5 ast, 0.39 sack, 0.10 PD, 0.00 INT |  |
| DL | Malcolm Koonce | 3.5 | 1.1 solo, 0.9 ast, 0.52 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 9.4 | 5.9 solo, 3.1 ast, 0.22 sack, 0.18 PD, 0.00 INT |  |
| LB | Quay Walker | 5.6 | 2.7 solo, 3.9 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Elandon Roberts | 2.7 | 1.7 solo, 1.8 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 6.5 | 4.0 solo, 2.3 ast, 0.16 sack, 0.14 PD, 0.00 INT |  |
| DB | Hezekiah Masses | 5.7 | 2.4 solo, 1.5 ast, 0.00 sack, 1.04 PD, 0.50 INT |  |
| DB | Taron Johnson | 5.1 | 3.4 solo, 1.0 ast, 0.00 sack, 0.39 PD, 0.00 INT |  |

### CAR @ PHI

Market: PHI +1.0, total 39.5. Sim: CAR 20.1, PHI 19.2. PHI wins 47.8%, CAR wins 52.2%. Median margin -0.7 for PHI.

| Team stat | CAR | PHI |
|---|---|---|
| Plays | 61 | 61 |
| Pass attempts / completions | 33 / 21 | 31 / 18 |
| Passing yards | 226 | 202 |
| Rush attempts / yards | 26 / 106 | 29 / 123 |
| Sacks taken | 2.4 | 2.1 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.3 / 0.9 | 1.0 / 1.1 |
| Field goals | 1.5 | 1.4 |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.0 | 226 pass yd, 1.3 TD, 0.6 INT; 4.0 rush, 16 yd |  |
| RB | Chuba Hubbard | 13.2 | 14.5 car, 62 yd, 0.55 TD; 1.8 rec, 14 yd, 0.12 TD |  |
| RB | AJ Dillon | 2.5 | 5.7 car, 21 yd, 0.11 TD; 0.4 rec, 3 yd, 0.00 TD | Questionable |
| WR | Tetairoa McMillan | 13.2 | 5.2 rec, 62 yd, 0.32 TD |  |
| WR | Jalen Coker | 9.1 | 4.0 rec, 39 yd, 0.22 TD |  |
| WR | John Metchie III | 4.1 | 1.6 rec, 16 yd, 0.14 TD |  |
| WR | Brycen Tremayne | 2.4 | 1.0 rec, 12 yd, 0.03 TD |  |
| TE | Darren Waller | 4.8 | 2.7 rec, 26 yd, 0.18 TD | Questionable |
| TE | Tommy Tremble | 3.1 | 2.0 rec, 16 yd, 0.09 TD | Questionable |
| K | Ryan Fitzgerald | 8.5 | 1.7 FG, 2.0 XP |  |
| DL | Derrick Brown | 4.1 | 2.1 solo, 2.1 ast, 0.11 sack, 0.47 PD, 0.00 INT |  |
| DL | Lee Hunter | 2.1 | 1.3 solo, 1.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 11.8 | 5.5 solo, 2.9 ast, 0.26 sack, 0.76 PD, 0.50 INT |  |
| LB | Bobby Okereke | 6.4 | 3.4 solo, 3.0 ast, 0.00 sack, 0.48 PD, 0.20 INT |  |
| LB | Princely Umanmielen | 3.2 | 1.5 solo, 0.8 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Scott | 5.4 | 3.7 solo, 2.2 ast, 0.00 sack, 0.05 PD, 0.06 INT |  |
| DB | Will Lee III | 4.8 | 2.6 solo, 1.9 ast, 0.00 sack, 0.86 PD, 0.00 INT |  |
| DB | Zakee Wheatley | 4.7 | 3.6 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jalen Hurts | 16.2 | 202 pass yd, 1.0 TD, 0.7 INT; 3.9 rush, 19 yd |  |
| RB | Dameon Pierce | 10.5 | 13.2 car, 51 yd, 0.29 TD; 1.9 rec, 15 yd, 0.07 TD |  |
| RB | Saquon Barkley | 6.8 | 9.7 car, 46 yd, 0.43 TD; 1.1 rec, 8 yd, 0.03 TD | Questionable |
| WR | DeVonta Smith | 6.6 | 3.7 rec, 42 yd, 0.17 TD | Questionable |
| WR | Dontayvion Wicks | 5.9 | 3.2 rec, 39 yd, 0.14 TD | Questionable |
| WR | Makai Lemon | 5.6 | 2.8 rec, 23 yd, 0.07 TD |  |
| WR | Darius Cooper | 4.5 | 1.4 rec, 18 yd, 0.21 TD |  |
| TE | Dallas Goedert | 7.0 | 2.9 rec, 27 yd, 0.22 TD |  |
| TE | Zach Ertz | 2.6 | 1.2 rec, 12 yd, 0.04 TD |  |
| K | Jake Elliott | 7.1 | 1.4 FG, 1.9 XP |  |
| DL | Jalen Carter | 4.9 | 1.4 solo, 1.0 ast, 0.56 sack, 0.47 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.6 solo, 2.4 ast, 0.07 sack, 0.10 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 6.1 | 4.1 solo, 2.5 ast, 0.08 sack, 0.08 PD, 0.00 INT |  |
| LB | Zack Baun | 5.9 | 3.4 solo, 3.6 ast, 0.02 sack, 0.41 PD, 0.06 INT |  |
| LB | Jeremiah Trotter Jr. | 3.6 | 2.6 solo, 1.8 ast, 0.00 sack, 0.16 PD, 0.00 INT |  |
| DB | Cooper DeJean | 6.3 | 3.4 solo, 2.4 ast, 0.00 sack, 0.96 PD, 0.22 INT |  |
| DB | Riq Woolen | 4.7 | 3.3 solo, 1.4 ast, 0.00 sack, 0.66 PD, 0.00 INT |  |
| DB | Quinyon Mitchell | 4.6 | 3.1 solo, 0.5 ast, 0.00 sack, 0.87 PD, 0.14 INT |  |

### CHI @ ATL

Market: ATL +1.0, total 51.0. Sim: CHI 25.8, ATL 25.1. ATL wins 48.4%, CHI wins 51.6%. Median margin -0.6 for ATL.

| Team stat | CHI | ATL |
|---|---|---|
| Plays | 66 | 63 |
| Pass attempts / completions | 33 / 21 | 31 / 19 |
| Passing yards | 222 | 234 |
| Rush attempts / yards | 30 / 138 | 30 / 146 |
| Sacks taken | 2.8 | 2.2 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.5 / 1.3 | 1.4 / 1.4 |
| Field goals | 1.9 | 1.9 |

**CHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Caleb Williams | 15.0 | 167 pass yd, 1.1 TD, 0.5 INT; 3.1 rush, 16 yd | Questionable |
| RB | D'Andre Swift | 12.0 | 11.1 car, 51 yd, 0.47 TD; 2.2 rec, 16 yd, 0.06 TD |  |
| RB | Kyle Monangai | 6.5 | 9.5 car, 44 yd, 0.37 TD; 1.0 rec, 9 yd, 0.03 TD | Questionable |
| RB | Roschon Johnson | 3.2 | 1.4 car, 6 yd, 0.03 TD; 1.2 rec, 10 yd, 0.04 TD |  |
| WR | Luther Burden III | 10.6 | 0.9 car, 4 yd, 0.02 TD; 4.2 rec, 45 yd, 0.24 TD |  |
| WR | Kalif Raymond | 9.0 | 3.9 rec, 33 yd, 0.31 TD |  |
| WR | Rome Odunze | 7.3 | 2.9 rec, 36 yd, 0.14 TD |  |
| WR | Jahdae Walker | 3.5 | 0.9 rec, 9 yd, 0.28 TD |  |
| TE | Colston Loveland | 8.5 | 3.7 rec, 34 yd, 0.25 TD |  |
| TE | Cole Kmet | 3.6 | 1.4 rec, 13 yd, 0.13 TD |  |
| K | Cairo Santos | 8.4 | 1.5 FG, 2.7 XP |  |
| DL | Austin Booker | 5.3 | 2.0 solo, 1.3 ast, 0.65 sack, 0.19 PD, 0.00 INT |  |
| DL | Montez Sweat | 2.9 | 1.0 solo, 1.0 ast, 0.41 sack, 0.03 PD, 0.00 INT |  |
| LB | Devin Bush | 5.3 | 2.7 solo, 3.0 ast, 0.21 sack, 0.16 PD, 0.00 INT |  |
| LB | D'Marco Jackson | 2.5 | 1.1 solo, 2.1 ast, 0.05 sack, 0.11 PD, 0.04 INT |  |
| LB | Noah Sewell | 0.9 | 0.4 solo, 0.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Dillon Thieneman | 6.6 | 3.6 solo, 3.5 ast, 0.00 sack, 0.69 PD, 0.19 INT |  |
| DB | Malik Muhammad | 4.3 | 2.3 solo, 1.2 ast, 0.17 sack, 0.49 PD, 0.15 INT |  |
| DB | Jaylon Johnson | 3.8 | 3.0 solo, 0.3 ast, 0.00 sack, 0.30 PD, 0.05 INT |  |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 16.6 | 234 pass yd, 1.4 TD, 0.8 INT; 1.1 rush, 5 yd |  |
| RB | Bijan Robinson | 22.2 | 18.0 car, 94 yd, 0.75 TD; 3.9 rec, 34 yd, 0.22 TD |  |
| RB | Brian Robinson | 8.4 | 8.9 car, 39 yd, 0.55 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| WR | Drake London | 13.3 | 4.9 rec, 71 yd, 0.21 TD |  |
| WR | Jahan Dotson | 6.3 | 2.1 rec, 29 yd, 0.22 TD |  |
| WR | Zachariah Branch | 2.7 | 1.4 rec, 12 yd, 0.03 TD |  |
| WR | Olamide Zaccheaus | 1.8 | 0.9 rec, 7 yd, 0.03 TD |  |
| TE | Kyle Pitts | 9.5 | 3.7 rec, 39 yd, 0.32 TD |  |
| TE | Austin Hooper | 4.2 | 1.4 rec, 13 yd, 0.24 TD |  |
| K | Nick Folk | 9.3 | 1.8 FG, 2.6 XP |  |
| DL | Cameron Thomas | 4.3 | 1.5 solo, 2.0 ast, 0.39 sack, 0.22 PD, 0.00 INT |  |
| DL | Samson Ebukam | 3.0 | 0.6 solo, 0.9 ast, 0.66 sack, 0.00 PD, 0.00 INT |  |
| LB | Kendal Daniels | 5.3 | 3.6 solo, 1.2 ast, 0.26 sack, 0.25 PD, 0.00 INT |  |
| LB | Harold Perkins Jr. | 4.1 | 2.5 solo, 1.9 ast, 0.11 sack, 0.25 PD, 0.00 INT |  |
| LB | Divine Deablo | 4.0 | 3.2 solo, 3.0 ast, 0.03 sack, 0.32 PD, 0.00 INT | Questionable |
| DB | Xavier Watts | 7.7 | 4.3 solo, 2.8 ast, 0.05 sack, 0.63 PD, 0.29 INT |  |
| DB | Jessie Bates | 5.6 | 3.1 solo, 2.0 ast, 0.00 sack, 0.47 PD, 0.09 INT |  |
| DB | C.J. Henderson | 5.2 | 4.4 solo, 0.9 ast, 0.00 sack, 1.08 PD, 0.08 INT | Questionable |

### DAL @ GB

Market: GB -1.5, total 53.0. Sim: DAL 25.7, GB 27.4. GB wins 55.1%, DAL wins 44.9%. Median margin +1.8 for GB.

| Team stat | DAL | GB |
|---|---|---|
| Plays | 65 | 60 |
| Pass attempts / completions | 36 / 24 | 31 / 20 |
| Passing yards | 264 | 257 |
| Rush attempts / yards | 26 / 111 | 27 / 111 |
| Sacks taken | 2.6 | 2.0 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.7 / 1.1 | 1.6 / 1.4 |
| Field goals | 2.0 | 2.1 |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 20.1 | 264 pass yd, 1.7 TD, 0.8 INT; 2.1 rush, 9 yd |  |
| RB | Javonte Williams | 12.9 | 12.2 car, 49 yd, 0.63 TD; 2.2 rec, 14 yd, 0.13 TD |  |
| RB | Tyler Goodson | 2.5 | 3.0 car, 13 yd, 0.07 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| RB | Jaydon Blue | 2.4 | 3.5 car, 15 yd, 0.15 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | CeeDee Lamb | 16.0 | 6.2 rec, 71 yd, 0.45 TD |  |
| WR | George Pickens | 13.3 | 5.1 rec, 63 yd, 0.33 TD |  |
| WR | Ryan Flournoy | 7.9 | 3.2 rec, 35 yd, 0.21 TD |  |
| WR | KaVontae Turpin | 3.3 | 0.6 car, 3 yd, 0.05 TD; 1.1 rec, 13 yd, 0.07 TD |  |
| TE | Jake Ferguson | 6.8 | 2.9 rec, 22 yd, 0.29 TD |  |
| TE | Brevyn Spann-Ford | 1.7 | 0.7 rec, 7 yd, 0.05 TD |  |
| K | Brandon Aubrey | 9.7 | 1.9 FG, 2.6 XP |  |
| DL | Quinnen Williams | 2.9 | 1.3 solo, 1.4 ast, 0.18 sack, 0.06 PD, 0.05 INT |  |
| DL | Otito Ogbonnia | 2.6 | 2.0 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Dee Winters | 5.8 | 4.2 solo, 2.6 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Jaishawn Barham | 4.2 | 2.6 solo, 2.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Rashan Gary | 3.1 | 2.1 solo, 0.8 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| DB | Caleb Downs | 6.0 | 3.7 solo, 2.0 ast, 0.15 sack, 0.16 PD, 0.00 INT |  |
| DB | DaRon Bland | 4.1 | 3.0 solo, 1.3 ast, 0.00 sack, 0.45 PD, 0.00 INT |  |
| DB | Shavon Revel Jr. | 3.4 | 2.3 solo, 1.1 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 20.0 | 257 pass yd, 1.6 TD, 0.5 INT; 1.8 rush, 7 yd |  |
| RB | MarShawn Lloyd | 12.6 | 9.3 car, 36 yd, 0.95 TD; 1.5 rec, 12 yd, 0.12 TD |  |
| RB | Pierre Strong | 7.9 | 4.6 car, 19 yd, 0.12 TD; 2.5 rec, 22 yd, 0.11 TD |  |
| RB | Kaleb Johnson | 4.5 | 6.8 car, 30 yd, 0.16 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| WR | Christian Watson | 13.7 | 3.9 rec, 63 yd, 0.59 TD |  |
| WR | Matthew Golden | 9.4 | 3.1 rec, 46 yd, 0.27 TD |  |
| WR | Bo Melton | 2.1 | 0.8 rec, 9 yd, 0.06 TD |  |
| WR | Skyy Moore | 1.8 | 1.2 rec, 10 yd, 0.06 TD | Questionable |
| TE | Tucker Kraft | 8.0 | 0.6 car, 3 yd, 0.01 TD; 3.1 rec, 33 yd, 0.21 TD |  |
| TE | Mark Redman | 2.2 | 0.9 rec, 11 yd, 0.03 TD |  |
| K | Trey Smack | 8.6 | 1.5 FG, 2.8 XP |  |
| DL | Devonte Wyatt | 3.1 | 1.8 solo, 0.9 ast, 0.48 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Brenton Cox Jr. | 2.8 | 1.6 solo, 1.3 ast, 0.11 sack, 0.00 PD, 0.00 INT |  |
| LB | Zaire Franklin | 6.7 | 3.6 solo, 4.6 ast, 0.00 sack, 0.26 PD, 0.00 INT |  |
| LB | Lukas Van Ness | 4.3 | 2.5 solo, 1.7 ast, 0.33 sack, 0.00 PD, 0.00 INT |  |
| LB | Isaiah McDuffie | 4.0 | 2.3 solo, 2.7 ast, 0.04 sack, 0.04 PD, 0.04 INT |  |
| DB | Xavier McKinney | 6.6 | 2.9 solo, 2.2 ast, 0.14 sack, 0.78 PD, 0.45 INT |  |
| DB | Evan Williams | 6.1 | 4.4 solo, 3.5 ast, 0.15 sack, 0.61 PD, 0.22 INT | Questionable |
| DB | Keisean Nixon | 5.8 | 3.5 solo, 1.8 ast, 0.05 sack, 0.80 PD, 0.15 INT |  |

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

Market: KC -8.0, total 42.5. Sim: LAC 17.2, KC 25.3. KC wins 73.5%, LAC wins 26.5%. Median margin +8.3 for KC.

| Team stat | LAC | KC |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 35 / 21 | 33 / 20 |
| Passing yards | 234 | 226 |
| Rush attempts / yards | 26 / 106 | 27 / 120 |
| Sacks taken | 2.1 | 2.7 |
| Interceptions thrown | 0.9 | 0.9 |
| Passing / rushing TDs | 1.1 / 0.8 | 1.6 / 1.1 |
| Field goals | 1.3 | 1.9 |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.5 | 234 pass yd, 1.1 TD, 0.9 INT; 3.6 rush, 18 yd |  |
| RB | Omarion Hampton | 9.0 | 9.9 car, 36 yd, 0.37 TD; 1.7 rec, 12 yd, 0.05 TD |  |
| RB | Keaton Mitchell | 8.0 | 4.8 car, 19 yd, 0.08 TD; 2.9 rec, 19 yd, 0.14 TD |  |
| RB | Kimani Vidal | 5.6 | 4.6 car, 20 yd, 0.18 TD; 1.1 rec, 10 yd, 0.08 TD |  |
| WR | Ladd McConkey | 5.4 | 2.9 rec, 36 yd, 0.16 TD | Questionable |
| WR | Quentin Johnston | 5.4 | 2.7 rec, 35 yd, 0.14 TD | Questionable |
| WR | Theo Wease Jr. | 2.5 | 1.1 rec, 12 yd, 0.02 TD |  |
| WR | Marquez Valdes-Scantling | 1.9 | 1.2 rec, 12 yd, 0.03 TD | Questionable |
| TE | Oronde Gadsden II | 5.7 | 2.5 rec, 25 yd, 0.12 TD |  |
| TE | Charlie Kolar | 4.0 | 1.9 rec, 18 yd, 0.04 TD |  |
| K | Cameron Dicker | 8.4 | 1.8 FG, 1.8 XP |  |
| DL | Justin Eboigbe | 2.3 | 1.6 solo, 1.3 ast, 0.20 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Teair Tart | 2.0 | 1.5 solo, 0.8 ast, 0.00 sack, 0.11 PD, 0.00 INT |  |
| LB | Tuli Tuipulotu | 6.4 | 2.1 solo, 1.6 ast, 0.55 sack, 0.40 PD, 0.14 INT |  |
| LB | Akheem Mesidor | 5.4 | 2.0 solo, 2.5 ast, 0.53 sack, 0.00 PD, 0.00 INT |  |
| LB | Daiyan Henley | 4.3 | 2.7 solo, 3.4 ast, 0.10 sack, 0.29 PD, 0.06 INT | Questionable |
| DB | Tony Jefferson | 4.5 | 2.8 solo, 1.7 ast, 0.00 sack, 0.37 PD, 0.08 INT |  |
| DB | Cam Hart | 4.2 | 2.2 solo, 1.4 ast, 0.00 sack, 0.80 PD, 0.13 INT |  |
| DB | Derwin James | 3.8 | 2.8 solo, 2.4 ast, 0.03 sack, 0.35 PD, 0.15 INT | Questionable |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 18.5 | 226 pass yd, 1.6 TD, 0.9 INT; 1.9 rush, 8 yd |  |
| RB | Kenneth Walker III | 17.3 | 14.1 car, 69 yd, 0.60 TD; 2.9 rec, 24 yd, 0.28 TD |  |
| RB | Kareem Hunt | 5.5 | 5.4 car, 20 yd, 0.27 TD; 0.8 rec, 8 yd, 0.06 TD |  |
| RB | Emmett Johnson | 3.4 | 2.4 car, 9 yd, 0.05 TD; 0.9 rec, 11 yd, 0.03 TD |  |
| WR | Rashee Rice | 8.2 | 4.2 rec, 48 yd, 0.31 TD | Questionable |
| WR | Xavier Worthy | 7.6 | 3.0 rec, 33 yd, 0.20 TD |  |
| WR | Jalen Royals | 2.6 | 1.0 rec, 8 yd, 0.13 TD |  |
| WR | JuJu Smith-Schuster | 2.0 | 0.9 rec, 9 yd, 0.03 TD |  |
| TE | Travis Kelce | 10.6 | 4.0 rec, 44 yd, 0.37 TD |  |
| TE | Noah Gray | 3.3 | 1.5 rec, 15 yd, 0.06 TD |  |
| K | Harrison Butker | 9.8 | 1.9 FG, 2.6 XP |  |
| DL | Chris Jones | 3.4 | 1.1 solo, 1.2 ast, 0.35 sack, 0.34 PD, 0.00 INT |  |
| DL | George Karlaftis | 3.3 | 1.3 solo, 1.9 ast, 0.11 sack, 0.32 PD, 0.13 INT |  |
| LB | Nick Bolton | 8.3 | 4.9 solo, 5.1 ast, 0.07 sack, 0.44 PD, 0.08 INT |  |
| LB | Drue Tranquill | 5.9 | 3.6 solo, 3.7 ast, 0.00 sack, 0.26 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.4 | 1.1 solo, 1.4 ast, 0.00 sack, 0.03 PD, 0.03 INT |  |
| DB | Mansoor Delane | 7.4 | 4.7 solo, 2.0 ast, 0.00 sack, 0.93 PD, 0.25 INT |  |
| DB | Chamarri Conner | 5.4 | 3.5 solo, 1.7 ast, 0.13 sack, 0.34 PD, 0.11 INT |  |
| DB | L'Jarius Sneed | 5.1 | 3.9 solo, 2.4 ast, 0.00 sack, 0.55 PD, 0.00 INT | Questionable |

### NO @ NYG

Market: NYG +1.0, total 46.0. Sim: NO 23.5, NYG 22.6. NYG wins 47.3%, NO wins 52.7%. Median margin -1.0 for NYG.

| Team stat | NO | NYG |
|---|---|---|
| Plays | 64 | 62 |
| Pass attempts / completions | 35 / 23 | 30 / 19 |
| Passing yards | 239 | 193 |
| Rush attempts / yards | 27 / 113 | 29 / 123 |
| Sacks taken | 2.5 | 2.6 |
| Interceptions thrown | 0.8 | 0.5 |
| Passing / rushing TDs | 1.4 / 1.2 | 1.2 / 1.2 |
| Field goals | 1.7 | 1.7 |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 18.7 | 239 pass yd, 1.4 TD, 0.8 INT; 2.8 rush, 13 yd |  |
| RB | Kendre Miller | 5.3 | 5.7 car, 22 yd, 0.30 TD; 0.7 rec, 5 yd, 0.02 TD |  |
| RB | Audric Estimé | 4.9 | 4.6 car, 20 yd, 0.14 TD; 1.0 rec, 9 yd, 0.02 TD |  |
| RB | Alvin Kamara | 4.7 | 4.5 car, 18 yd, 0.24 TD; 1.7 rec, 10 yd, 0.04 TD | Questionable |
| WR | Chris Olave | 10.1 | 5.4 rec, 63 yd, 0.30 TD | Questionable |
| WR | Devaughn Vele | 7.8 | 3.3 rec, 32 yd, 0.22 TD |  |
| WR | Kevin Austin Jr. | 3.3 | 1.4 rec, 14 yd, 0.09 TD |  |
| WR | Bryce Lance | 2.3 | 1.0 rec, 10 yd, 0.05 TD |  |
| TE | Juwan Johnson | 8.7 | 3.7 rec, 37 yd, 0.23 TD |  |
| TE | Noah Fant | 4.0 | 1.4 rec, 12 yd, 0.24 TD |  |
| K | Charlie Smyth | 8.0 | 1.5 FG, 2.4 XP |  |
| DL | Chase Young | 5.5 | 1.4 solo, 1.1 ast, 0.79 sack, 0.25 PD, 0.00 INT |  |
| DL | Carl Granderson | 4.2 | 1.6 solo, 2.0 ast, 0.40 sack, 0.12 PD, 0.08 INT |  |
| LB | Pete Werner | 4.5 | 2.7 solo, 2.5 ast, 0.09 sack, 0.15 PD, 0.00 INT |  |
| LB | Danny Stutsman | 3.9 | 2.5 solo, 2.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Cameron Jordan | 3.6 | 1.4 solo, 1.4 ast, 0.41 sack, 0.04 PD, 0.00 INT |  |
| DB | Jonas Sanker | 5.0 | 3.3 solo, 2.2 ast, 0.00 sack, 0.13 PD, 0.06 INT |  |
| DB | Julian Blackmon | 4.7 | 2.9 solo, 2.4 ast, 0.00 sack, 0.17 PD, 0.15 INT |  |
| DB | Justin Reid | 4.6 | 3.0 solo, 2.2 ast, 0.00 sack, 0.19 PD, 0.03 INT |  |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jameis Winston | 15.1 | 193 pass yd, 1.2 TD, 0.5 INT; 1.3 rush, 6 yd |  |
| RB | Cam Skattebo | 10.6 | 11.4 car, 45 yd, 0.62 TD; 1.2 rec, 10 yd, 0.03 TD |  |
| RB | Tyrone Tracy Jr. | 5.5 | 5.1 car, 23 yd, 0.13 TD; 1.1 rec, 9 yd, 0.07 TD |  |
| RB | Devin Singletary | 5.3 | 4.6 car, 19 yd, 0.25 TD; 0.9 rec, 7 yd, 0.07 TD |  |
| WR | Malik Nabers | 9.8 | 4.1 rec, 42 yd, 0.27 TD |  |
| WR | Malachi Fields | 3.7 | 1.4 rec, 17 yd, 0.11 TD |  |
| WR | Darius Slayton | 3.5 | 1.4 rec, 16 yd, 0.08 TD |  |
| WR | Darnell Mooney | 2.2 | 1.2 rec, 13 yd, 0.06 TD | Questionable |
| TE | Isaiah Likely | 10.3 | 4.6 rec, 37 yd, 0.36 TD |  |
| TE | Theo Johnson | 2.3 | 1.2 rec, 14 yd, 0.09 TD | Questionable |
| K | Dominic Zvada | 9.7 | 2.0 FG, 2.3 XP |  |
| DL | Shelby Harris | 2.4 | 1.1 solo, 1.6 ast, 0.00 sack, 0.56 PD, 0.00 INT |  |
| DL | DJ Reader | 2.2 | 1.7 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Arvell Reese | 9.9 | 6.0 solo, 2.9 ast, 0.26 sack, 0.92 PD, 0.24 INT |  |
| LB | Tremaine Edmunds | 9.0 | 5.8 solo, 2.8 ast, 0.49 sack, 0.37 PD, 0.00 INT |  |
| LB | Abdul Carter | 3.0 | 1.2 solo, 1.6 ast, 0.45 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | Jevon Holland | 5.8 | 2.7 solo, 1.7 ast, 0.00 sack, 0.52 PD, 0.38 INT |  |
| DB | Deonte Banks | 4.8 | 1.7 solo, 1.0 ast, 0.00 sack, 1.20 PD, 0.15 INT |  |
| DB | Andru Phillips | 4.6 | 2.8 solo, 1.0 ast, 0.30 sack, 0.42 PD, 0.00 INT |  |

### NYJ @ NE

Market: NE -7.0, total 43.5. Sim: NYJ 18.4, NE 25.4. NE wins 70.7%, NYJ wins 29.3%. Median margin +6.8 for NE.

| Team stat | NYJ | NE |
|---|---|---|
| Plays | 61 | 61 |
| Pass attempts / completions | 34 / 21 | 31 / 21 |
| Passing yards | 207 | 252 |
| Rush attempts / yards | 25 / 100 | 28 / 127 |
| Sacks taken | 2.2 | 2.3 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.2 / 0.8 | 1.6 / 1.2 |
| Field goals | 1.4 | 1.9 |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brady Cook | 15.3 | 207 pass yd, 1.2 TD, 0.6 INT; 1.5 rush, 6 yd |  |
| RB | Braelon Allen | 10.3 | 12.4 car, 50 yd, 0.41 TD; 1.7 rec, 10 yd, 0.05 TD |  |
| RB | Isaiah Davis | 2.4 | 1.7 car, 8 yd, 0.06 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| RB | Khalil Herbert | 1.9 | 2.4 car, 10 yd, 0.03 TD; 0.4 rec, 3 yd, 0.01 TD |  |
| WR | Garrett Wilson | 12.5 | 5.1 rec, 51 yd, 0.39 TD |  |
| WR | Isaiah Williams | 6.3 | 2.7 rec, 25 yd, 0.14 TD |  |
| WR | Tim Patrick | 4.6 | 2.1 rec, 21 yd, 0.06 TD |  |
| WR | Sterling Shepard | 1.2 | 0.6 rec, 5 yd, 0.02 TD |  |
| TE | Kenyon Sadiq | 5.6 | 3.0 rec, 27 yd, 0.20 TD | Questionable |
| TE | Jeremy Ruckert | 3.8 | 1.8 rec, 12 yd, 0.14 TD |  |
| K | Jason Sanders | 8.0 | 1.6 FG, 1.9 XP |  |
| DL | Will McDonald IV | 3.9 | 1.2 solo, 1.2 ast, 0.47 sack, 0.00 PD, 0.00 INT |  |
| DL | Jowon Briggs | 3.4 | 1.1 solo, 2.1 ast, 0.33 sack, 0.00 PD, 0.00 INT |  |
| LB | David Bailey | 7.9 | 3.4 solo, 1.7 ast, 1.04 sack, 0.21 PD, 0.00 INT |  |
| LB | Demario Davis | 6.6 | 3.6 solo, 3.2 ast, 0.39 sack, 0.14 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 6.4 | 3.5 solo, 4.1 ast, 0.05 sack, 0.50 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 10.1 | 5.8 solo, 4.1 ast, 0.00 sack, 0.93 PD, 0.44 INT |  |
| DB | Dane Belton | 5.1 | 3.7 solo, 4.1 ast, 0.25 sack, 0.40 PD, 0.00 INT | Questionable |
| DB | Andre Cisco | 4.1 | 2.8 solo, 0.6 ast, 0.19 sack, 0.15 PD, 0.00 INT |  |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 21.5 | 252 pass yd, 1.6 TD, 0.6 INT; 4.6 rush, 21 yd |  |
| RB | Rhamondre Stevenson | 13.1 | 7.7 car, 37 yd, 0.41 TD; 3.3 rec, 29 yd, 0.17 TD |  |
| RB | TreVeyon Henderson | 6.8 | 8.9 car, 40 yd, 0.40 TD; 1.3 rec, 11 yd, 0.07 TD | Questionable |
| RB | Corey Kiner | 2.6 | 3.1 car, 14 yd, 0.07 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| WR | Romeo Doubs | 9.5 | 3.3 rec, 43 yd, 0.32 TD |  |
| WR | DeMario Douglas | 7.3 | 2.7 rec, 32 yd, 0.24 TD |  |
| WR | Efton Chism III | 5.1 | 1.9 rec, 22 yd, 0.15 TD |  |
| WR | Kyle Williams | 4.9 | 1.4 rec, 24 yd, 0.17 TD |  |
| TE | Hunter Henry | 10.2 | 4.1 rec, 46 yd, 0.25 TD |  |
| TE | Eli Raridon | 5.1 | 2.1 rec, 23 yd, 0.12 TD |  |
| K | Andy Borregales | 8.0 | 1.4 FG, 2.6 XP |  |
| DL | Christian Barmore | 2.2 | 0.9 solo, 0.5 ast, 0.26 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Taylor III | 1.7 | 0.6 solo, 0.6 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| LB | Elijah Ponder | 5.7 | 1.8 solo, 1.2 ast, 0.76 sack, 0.00 PD, 0.00 INT |  |
| LB | Robert Spillane | 4.5 | 2.7 solo, 2.8 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |
| LB | Christian Elliss | 3.7 | 2.8 solo, 3.2 ast, 0.10 sack, 0.09 PD, 0.00 INT | Questionable |
| DB | Kindle Vildor | 4.3 | 2.4 solo, 0.5 ast, 0.00 sack, 0.53 PD, 0.00 INT |  |
| DB | Marcus Jones | 3.4 | 2.5 solo, 1.0 ast, 0.08 sack, 0.54 PD, 0.16 INT | Questionable |
| DB | Craig Woodson | 3.2 | 2.4 solo, 1.7 ast, 0.00 sack, 0.30 PD, 0.12 INT | Questionable |

### PIT @ TB

Market: TB +2.5, total 39.5. Sim: PIT 20.9, TB 18.7. TB wins 42.2%, PIT wins 57.8%. Median margin -2.4 for TB.

| Team stat | PIT | TB |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 35 / 22 | 34 / 22 |
| Passing yards | 255 | 229 |
| Rush attempts / yards | 26 / 123 | 27 / 122 |
| Sacks taken | 1.9 | 2.4 |
| Interceptions thrown | 0.7 | 0.9 |
| Passing / rushing TDs | 1.3 / 0.9 | 1.2 / 0.8 |
| Field goals | 1.6 | 1.4 |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 17.8 | 255 pass yd, 1.3 TD, 0.7 INT; 1.5 rush, 7 yd |  |
| RB | Jaylen Warren | 20.2 | 15.0 car, 76 yd, 0.59 TD; 3.9 rec, 41 yd, 0.21 TD |  |
| RB | Rico Dowdle | 4.1 | 4.8 car, 19 yd, 0.09 TD; 1.4 rec, 14 yd, 0.04 TD | Questionable |
| RB | Travis Homer | 0.9 | 1.7 car, 7 yd, 0.03 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | DK Metcalf | 12.4 | 4.8 rec, 56 yd, 0.28 TD |  |
| WR | Germie Bernard | 9.7 | 4.2 rec, 46 yd, 0.13 TD |  |
| WR | Scott Miller | 2.9 | 1.4 rec, 13 yd, 0.04 TD |  |
| TE | Pat Freiermuth | 11.0 | 4.1 rec, 41 yd, 0.43 TD |  |
| TE | Darnell Washington | 6.7 | 2.7 rec, 31 yd, 0.15 TD |  |
| K | Chris Boswell | 8.3 | 1.7 FG, 2.1 XP |  |
| DL | Cameron Heyward | 4.7 | 2.1 solo, 2.3 ast, 0.26 sack, 0.39 PD, 0.00 INT |  |
| DL | Keeanu Benton | 2.1 | 1.5 solo, 1.4 ast, 0.08 sack, 0.20 PD, 0.00 INT | Questionable |
| LB | T.J. Watt | 6.8 | 1.9 solo, 1.0 ast, 0.65 sack, 0.46 PD, 0.20 INT |  |
| LB | Payton Wilson | 6.6 | 4.0 solo, 3.3 ast, 0.17 sack, 0.25 PD, 0.00 INT |  |
| LB | Patrick Queen | 5.2 | 2.5 solo, 4.3 ast, 0.00 sack, 0.21 PD, 0.10 INT |  |
| DB | Jaquan Brisker | 6.4 | 3.4 solo, 3.7 ast, 0.00 sack, 0.68 PD, 0.15 INT |  |
| DB | Robert Spears-Jennings | 3.8 | 2.3 solo, 0.9 ast, 0.00 sack, 0.46 PD, 0.21 INT |  |
| DB | Daylen Everette | 3.8 | 2.6 solo, 0.3 ast, 0.00 sack, 1.06 PD, 0.00 INT |  |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jalon Daniels | 16.9 | 229 pass yd, 1.2 TD, 0.9 INT; 4.5 rush, 21 yd |  |
| RB | Bucky Irving | 14.1 | 14.4 car, 66 yd, 0.38 TD; 2.6 rec, 18 yd, 0.16 TD |  |
| RB | Kenny Gainwell | 7.0 | 3.0 car, 13 yd, 0.04 TD; 2.6 rec, 19 yd, 0.19 TD |  |
| RB | Sean Tucker | 2.6 | 3.6 car, 15 yd, 0.24 TD; 0.2 rec, 2 yd, 0.02 TD | Questionable |
| WR | Emeka Egbuka | 9.8 | 4.1 rec, 41 yd, 0.17 TD |  |
| WR | Chris Godwin Jr. | 9.2 | 4.2 rec, 41 yd, 0.14 TD |  |
| WR | Ted Hurst III | 6.1 | 2.2 rec, 28 yd, 0.19 TD |  |
| WR | Tez Johnson | 4.0 | 1.3 rec, 20 yd, 0.08 TD |  |
| TE | Cade Otton | 8.9 | 4.1 rec, 40 yd, 0.14 TD |  |
| TE | Payne Durham | 0.8 | 0.4 rec, 4 yd, 0.01 TD |  |
| K | Chase McLaughlin | 8.4 | 1.7 FG, 1.9 XP |  |
| DL | A'Shawn Robinson | 3.2 | 0.9 solo, 2.2 ast, 0.18 sack, 0.20 PD, 0.18 INT |  |
| DL | Vita Vea | 2.1 | 0.9 solo, 1.3 ast, 0.09 sack, 0.30 PD, 0.00 INT |  |
| LB | Josiah Trotter | 9.0 | 4.9 solo, 3.8 ast, 0.18 sack, 0.17 PD, 0.18 INT |  |
| LB | Alex Anzalone | 5.3 | 1.8 solo, 3.5 ast, 0.21 sack, 0.26 PD, 0.28 INT |  |
| LB | Lavonte David | 4.3 | 2.6 solo, 1.5 ast, 0.11 sack, 0.08 PD, 0.00 INT |  |
| DB | Jacob Parrish | 6.6 | 4.0 solo, 1.0 ast, 0.00 sack, 1.29 PD, 0.27 INT |  |
| DB | Keionte Scott | 5.4 | 4.9 solo, 0.2 ast, 0.00 sack, 0.46 PD, 0.00 INT |  |
| DB | Tykee Smith | 4.5 | 3.1 solo, 1.4 ast, 0.00 sack, 0.27 PD, 0.03 INT |  |

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
| DB | Riley Moss | 3.5 | 2.5 solo, 1.3 ast, 0.05 sack, 1.02 PD, 0.15 INT | Questionable |

### TEN @ IND

Market: IND -7.0, total 44.5. Sim: TEN 19.1, IND 25.5. IND wins 68.3%, TEN wins 31.7%. Median margin +6.6 for IND.

| Team stat | TEN | IND |
|---|---|---|
| Plays | 61 | 62 |
| Pass attempts / completions | 35 / 22 | 32 / 20 |
| Passing yards | 231 | 218 |
| Rush attempts / yards | 23 / 93 | 28 / 103 |
| Sacks taken | 2.2 | 2.5 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.3 / 0.8 | 1.4 / 1.4 |
| Field goals | 1.5 | 1.9 |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 18.2 | 231 pass yd, 1.3 TD, 0.6 INT; 2.4 rush, 10 yd |  |
| RB | Tony Pollard | 10.2 | 13.4 car, 54 yd, 0.38 TD; 1.4 rec, 9 yd, 0.04 TD |  |
| RB | Tyjae Spears | 5.2 | 3.9 car, 15 yd, 0.10 TD; 3.0 rec, 18 yd, 0.06 TD | Questionable |
| RB | Nicholas Singleton | 1.0 | 2.0 car, 8 yd, 0.04 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Wan'Dale Robinson | 10.7 | 4.2 rec, 36 yd, 0.49 TD |  |
| WR | Carnell Tate | 10.1 | 4.4 rec, 50 yd, 0.12 TD |  |
| WR | Elic Ayomanor | 5.2 | 1.7 rec, 23 yd, 0.20 TD |  |
| WR | Chimere Dike | 4.6 | 2.0 rec, 18 yd, 0.14 TD |  |
| TE | Gunnar Helm | 3.6 | 1.8 rec, 14 yd, 0.08 TD |  |
| TE | Daniel Bellinger | 1.9 | 0.9 rec, 8 yd, 0.02 TD |  |
| K | Joey Slye | 7.0 | 1.4 FG, 1.9 XP |  |
| DL | Jeffery Simmons | 6.1 | 2.6 solo, 2.4 ast, 0.55 sack, 0.42 PD, 0.00 INT |  |
| DL | Jacob Martin | 2.6 | 0.7 solo, 0.2 ast, 0.52 sack, 0.25 PD, 0.00 INT |  |
| LB | Anthony Hill Jr. | 6.4 | 3.5 solo, 5.2 ast, 0.00 sack, 0.28 PD, 0.00 INT |  |
| LB | Cedric Gray | 6.0 | 3.9 solo, 3.3 ast, 0.10 sack, 0.07 PD, 0.00 INT |  |
| LB | Cody Barton | 4.0 | 1.8 solo, 2.9 ast, 0.03 sack, 0.39 PD, 0.03 INT |  |
| DB | Alontae Taylor | 4.7 | 3.6 solo, 1.1 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |
| DB | Amani Hooker | 3.8 | 3.7 solo, 1.4 ast, 0.00 sack, 0.32 PD, 0.11 INT | Questionable |
| DB | Terrell Burgess | 3.0 | 2.0 solo, 1.4 ast, 0.00 sack, 0.33 PD, 0.00 INT |  |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 17.4 | 218 pass yd, 1.4 TD, 0.6 INT; 2.3 rush, 9 yd |  |
| RB | Jonathan Taylor | 16.2 | 18.5 car, 65 yd, 0.86 TD; 2.3 rec, 21 yd, 0.08 TD |  |
| RB | Seth McGowan | 2.9 | 3.4 car, 13 yd, 0.09 TD; 0.5 rec, 5 yd, 0.02 TD |  |
| RB | DJ Giddens | 1.0 | 1.8 car, 7 yd, 0.05 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Keenan Allen | 10.0 | 3.8 rec, 36 yd, 0.44 TD |  |
| WR | Josh Downs | 6.7 | 3.5 rec, 42 yd, 0.20 TD | Questionable |
| WR | Laquon Treadwell | 4.0 | 1.6 rec, 21 yd, 0.06 TD |  |
| WR | Deion Burks | 1.6 | 0.6 rec, 7 yd, 0.02 TD |  |
| TE | Tyler Warren | 11.9 | 4.9 rec, 43 yd, 0.35 TD |  |
| TE | Mo Alie-Cox | 2.8 | 1.1 rec, 11 yd, 0.11 TD |  |
| K | Spencer Shrader | 11.6 | 2.4 FG, 2.6 XP |  |
| DL | DeForest Buckner | 5.1 | 1.6 solo, 2.4 ast, 0.58 sack, 0.31 PD, 0.00 INT |  |
| DL | Laiatu Latu | 3.8 | 1.5 solo, 1.0 ast, 0.39 sack, 0.42 PD, 0.03 INT |  |
| LB | Akeem Davis-Gaither | 6.6 | 4.4 solo, 4.0 ast, 0.00 sack, 0.21 PD, 0.00 INT |  |
| LB | Germaine Pratt | 5.3 | 2.9 solo, 2.3 ast, 0.00 sack, 0.58 PD, 0.11 INT |  |
| LB | Bryce Boettcher | 2.6 | 1.3 solo, 2.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Justin Walley | 6.3 | 3.5 solo, 2.1 ast, 0.23 sack, 0.59 PD, 0.00 INT |  |
| DB | Camryn Bynum | 4.5 | 3.1 solo, 1.3 ast, 0.04 sack, 0.27 PD, 0.10 INT |  |
| DB | A.J. Haulcy | 3.7 | 2.4 solo, 1.7 ast, 0.00 sack, 0.52 PD, 0.00 INT |  |

### WAS @ SF

Market: SF -7.5, total 50.5. Sim: WAS 21.4, SF 29.2. SF wins 73.1%, WAS wins 26.9%. Median margin +7.9 for SF.

| Team stat | WAS | SF |
|---|---|---|
| Plays | 62 | 61 |
| Pass attempts / completions | 33 / 20 | 31 / 21 |
| Passing yards | 221 | 244 |
| Rush attempts / yards | 27 / 123 | 28 / 128 |
| Sacks taken | 1.8 | 2.0 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.1 / 1.1 | 1.7 / 1.4 |
| Field goals | 1.6 | 2.2 |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jayden Daniels | 18.1 | 221 pass yd, 1.1 TD, 0.6 INT; 3.3 rush, 20 yd |  |
| RB | Jacory Croskey-Merritt | 7.4 | 9.0 car, 38 yd, 0.42 TD; 0.6 rec, 6 yd, 0.01 TD |  |
| RB | Rachaad White | 5.9 | 4.7 car, 20 yd, 0.10 TD; 1.6 rec, 12 yd, 0.11 TD |  |
| RB | Austin Ekeler | 3.6 | 2.9 car, 13 yd, 0.07 TD; 0.9 rec, 10 yd, 0.02 TD |  |
| WR | Terry McLaurin | 9.6 | 3.7 rec, 47 yd, 0.20 TD |  |
| WR | Stefon Diggs | 6.1 | 3.5 rec, 32 yd, 0.25 TD | Questionable |
| WR | Antonio Williams | 5.9 | 2.6 rec, 25 yd, 0.12 TD |  |
| WR | Treylon Burks | 4.1 | 1.4 rec, 17 yd, 0.17 TD |  |
| TE | Chig Okonkwo | 4.6 | 2.1 rec, 21 yd, 0.06 TD |  |
| TE | John Bates | 2.2 | 1.0 rec, 8 yd, 0.07 TD |  |
| K | Drew Stevens | 8.8 | 1.8 FG, 2.1 XP |  |
| DL | Daron Payne | 3.1 | 1.3 solo, 1.3 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| DL | Deatrich Wise | 3.0 | 3.0 solo, 0.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Sonny Styles | 6.5 | 2.6 solo, 4.0 ast, 0.15 sack, 0.58 PD, 0.18 INT |  |
| LB | Bobby Wagner | 5.1 | 2.7 solo, 2.9 ast, 0.18 sack, 0.21 PD, 0.05 INT |  |
| LB | Frankie Luvu | 4.4 | 2.4 solo, 2.5 ast, 0.13 sack, 0.22 PD, 0.00 INT |  |
| DB | Amik Robertson | 7.7 | 5.1 solo, 1.5 ast, 0.00 sack, 1.46 PD, 0.00 INT |  |
| DB | Rasul Douglas | 5.9 | 4.2 solo, 0.8 ast, 0.00 sack, 0.76 PD, 0.20 INT |  |
| DB | Jeremy Reaves | 5.6 | 3.7 solo, 2.3 ast, 0.00 sack, 0.50 PD, 0.06 INT |  |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 22.8 | 244 pass yd, 1.7 TD, 0.6 INT; 4.3 rush, 21 yd |  |
| RB | Christian McCaffrey | 21.9 | 14.2 car, 65 yd, 0.87 TD; 5.0 rec, 39 yd, 0.23 TD |  |
| RB | Kaelon Black | 4.6 | 6.8 car, 29 yd, 0.19 TD; 0.3 rec, 3 yd, 0.01 TD |  |
| RB | Kyle Juszczyk | 2.7 | 0.0 car, 0 yd, 0.00 TD; 1.4 rec, 15 yd, 0.13 TD | Questionable |
| WR | Mike Evans | 16.5 | 6.1 rec, 77 yd, 0.48 TD |  |
| WR | Brandin Cooks | 3.9 | 1.1 rec, 11 yd, 0.29 TD |  |
| WR | Jacob Cowing | 1.8 | 0.7 rec, 8 yd, 0.04 TD |  |
| WR | Jordan Watkins | 1.2 | 0.5 rec, 7 yd, 0.02 TD |  |
| TE | George Kittle | 15.2 | 5.9 rec, 66 yd, 0.47 TD |  |
| TE | Luke Farrell | 1.2 | 0.5 rec, 5 yd, 0.04 TD |  |
| K | Eddy Pineiro | 8.1 | 1.4 FG, 3.0 XP |  |
| DL | Gracen Halton | 4.9 | 1.9 solo, 1.4 ast, 0.26 sack, 0.23 PD, 0.00 INT |  |
| DL | Sebastian Valdez | 3.1 | 1.3 solo, 1.3 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| LB | Fred Warner | 9.2 | 4.5 solo, 5.5 ast, 0.09 sack, 0.58 PD, 0.00 INT |  |
| LB | Jaden Dugger | 4.3 | 2.7 solo, 1.5 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| LB | Tatum Bethune | 3.9 | 1.8 solo, 2.6 ast, 0.12 sack, 0.38 PD, 0.00 INT |  |
| DB | Ji'Ayir Brown | 5.7 | 3.4 solo, 3.0 ast, 0.00 sack, 0.45 PD, 0.08 INT |  |
| DB | Renardo Green | 5.6 | 2.8 solo, 1.5 ast, 0.00 sack, 0.88 PD, 0.39 INT |  |
| DB | Malik Mustapha | 4.4 | 2.6 solo, 1.9 ast, 0.00 sack, 0.42 PD, 0.04 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: SEA: Julian Neal, SEA: Jake Bobo, SEA: Chazz Surratt, SEA: Jadarian Price, SEA: Drake Thomas, SEA: Robbie Ouzts, SEA: Coby Bryant, SEA: Zach Charbonnet, DEN: Pat Bryant, DEN: Talanoa Hufanga, DEN: Jonah Coleman, DEN: Jonathon Cooper, DEN: Pat Surtain II, HOU: Henry To'oTo'o, HOU: Dylan Horton, HOU: David Montgomery, HOU: Jayden Higgins, HOU: Jaylin Smith, HOU: Mario Edwards, HOU: Christian Kirk, HOU: Ja'Marcus Ingram, HOU: Damone Clark, HOU: Jalen Pitre, HOU: British Brooks, HOU: E.J. Speed, JAX: BJ Green II, JAX: Caleb Ransaw, CHI: Dayo Odeyingbo, CHI: Ruben Hyppolite II, CHI: Nikola Kalinic, CHI: Kyler Gordon, CHI: T.J. Edwards, CHI: Brittain Brown, CHI: Joe Tryon-Shoyinka, ATL: James Pearce Jr., ATL: Jalon Walker, ATL: JD Bertrand, ATL: Ronnie Harrison, ATL: David Sills, ATL: A.J. Terrell, ATL: Yasir Abdullah, BAL: T.J. Tampa, BAL: Jacob Hummel, BAL: Ja'Kobi Lane, BAL: Durham Smythe, CLE: Dillon Gabriel, CLE: Mason Graham, CLE: Dylan Sampson, CLE: Alex Wright, CLE: Nathaniel Watson, CLE: Myles Garrett, CLE: Raheim Sanders, TEN: Kevin Winston Jr., TEN: Kendell Brooks, TEN: Jaylen Harrell, TEN: Darrell Baker Jr., IND: Alec Pierce, IND: Cameron Mitchell, IND: Arden Key, NYJ: Braiden McGregor, NYJ: Breece Hall, NYJ: David Onyemata, NYJ: Micheal Clemons, NYJ: Adonai Mitchell, NYJ: Joseph Ossai, NYJ: Tre Brown, NYJ: Arian Smith, NYJ: Marcelino McCrary-Ball, NYJ: Ja'Sir Taylor, NYJ: Omar Cooper Jr., NYJ: Tyler Baron, NE: Quintayvious Hutchins, NE: Reggie Gilliam, NE: Bryce Baringer, NE: Mack Hollins, NE: Harold Landry III, NE: A.J. Brown, NE: Dell Pettus, NO: Moliki Matavao, NO: Mason Tipton, NO: Travis Etienne, NO: Bryan Bresee, NYG: Jaxson Dart, NYG: Paulson Adebo, NYG: Brian Burns, NYG: Roy Robertson-Harris, NYG: Jarrick Bernard-Converse, NYG: Elijah Chatman, NYG: Chauncey Golston, NYG: Gunner Olszewski, NYG: Korie Black, NYG: DJ Davidson, NYG: Braxton Berrios, CAR: Cam Jackson, CAR: Mike Jackson, CAR: Jonathon Brooks, CAR: LaBryan Ray, CAR: Xavier Legette, CAR: Trevor Etienne, CAR: Nic Scourton, CAR: Bam Martin-Scott, CAR: Tershawn Wharton, CAR: Jaycee Horn, PHI: Jakorian Bennett, PHI: Grant Calcaterra, PHI: Tank Bigsby, PHI: Will Shipley, PHI: Jalyx Hunt, PIT: Ben Skowronek, PIT: Calvin Austin III, PIT: Darius Slay, PIT: Trey Sermon, PIT: Michael Pittman, PIT: Derrick Harmon, PIT: Adam Thielen, PIT: Roman Wilson, TB: Antoine Winfield Jr., TB: Teddy Bridgewater, TB: Markees Watts, TB: Baker Mayfield, TB: Jalen McMillan, ARI: Hunter Long, ARI: Zachary Carter, ARI: Will Johnson, ARI: Kitan Crawford, LA: Terrance Ferguson, LA: Ahkello Witherspoon, LA: Darious Williams, LA: Ronnie Rivers, LAC: Trey Lance, LAC: KeAndre Lambert-Smith, LAC: Denzel Perryman, LAC: Da'Shawn Hand, LAC: Tre Harris, LAC: David Njoku, KC: Isiah Pacheco, KC: Cooper McDonald, KC: Tyquan Thornton, KC: Joshua Williams, BUF: Tyrell Shavers, BUF: Jordan Hancock, LV: Dont'e Thornton Jr., LV: Jack Bech, LV: Jamal Adams, LV: Carter Runyon, DAL: Jalen Thompson, DAL: P.J. Locke, DAL: Jonathan Bullard, DAL: Marist Liufau, DAL: Malik Davis, GB: Collin Oliver, GB: Savion Williams, GB: Jayden Reed, GB: Warren Brinson, GB: Javon Hargrave, GB: Jordon Riley, GB: Josh Jacobs, GB: Micah Parsons, GB: Nate Hobbs, GB: Luke Musgrave, GB: Edgerrin Cooper, GB: Chris Brooks, WAS: Marcus Mariota, WAS: Jaylin Lane, WAS: Trey Amos, WAS: Jordan Magee, WAS: Jeremy McNichols, WAS: Jer'Zhan Newton, WAS: Leo Chenal, WAS: Nick Bellore, SF: Deebo Samuel Sr., SF: Alfred Collins, SF: Dre Greenlaw, SF: Ricky Pearsall, SF: C.J. West, SF: Marques Sigle, SF: Kalia Davis, SF: Isaac Guerendo, SF: Garret Wallow, SF: Demarcus Robinson, SF: Nick Martin, SF: Jake Tonges, SF: Sam Okuayinonu.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.9 | 9.3 to 37.7 |
| QB | Brock Purdy | SF | 20.6 | 8.1 to 34.3 |
| QB | Matthew Stafford | LA | 20.3 | 8.1 to 33.3 |
| QB | Drake Maye | NE | 19.8 | 7.9 to 32.6 |
| QB | Dak Prescott | DAL | 18.5 | 7.0 to 31.1 |
| QB | Jordan Love | GB | 18.1 | 7.1 to 30.5 |
| RB | Bijan Robinson | ATL | 23.6 | 9.3 to 39.3 |
| RB | Christian McCaffrey | SF | 22.4 | 8.4 to 38.4 |
| RB | Jaylen Warren | PIT | 21.1 | 7.5 to 36.9 |
| RB | Kyren Williams | LA | 19.4 | 6.3 to 34.1 |
| RB | Derrick Henry | BAL | 18.7 | 4.9 to 33.4 |
| RB | Kenneth Walker III | KC | 17.8 | 5.6 to 32.3 |
| RB | Jonathan Taylor | IND | 16.7 | 4.4 to 31.0 |
| RB | James Cook | BUF | 16.3 | 4.4 to 29.7 |
| RB | Ashton Jeanty | LV | 15.5 | 4.9 to 27.8 |
| RB | Emanuel Wilson | SEA | 14.6 | 3.4 to 27.9 |
| WR | Jaxon Smith-Njigba | SEA | 20.3 | 7.1 to 36.0 |
| WR | Puka Nacua | LA | 19.3 | 5.9 to 35.0 |
| WR | Mike Evans | SF | 17.4 | 4.7 to 32.2 |
| WR | CeeDee Lamb | DAL | 16.7 | 5.2 to 30.6 |
| WR | Zay Flowers | BAL | 15.1 | 4.0 to 28.6 |
| WR | Christian Watson | GB | 14.2 | 2.2 to 28.5 |
| WR | Drake London | ATL | 14.0 | 3.2 to 27.9 |
| WR | George Pickens | DAL | 13.8 | 3.3 to 26.9 |
| WR | Tetairoa McMillan | CAR | 13.6 | 3.2 to 26.8 |
| WR | Nico Collins | HOU | 13.3 | 2.7 to 26.2 |
| WR | Parker Washington | JAX | 13.3 | 2.4 to 26.4 |
| WR | Garrett Wilson | NYJ | 12.7 | 3.0 to 24.9 |
| TE | George Kittle | SF | 15.8 | 4.2 to 29.5 |
| TE | Trey McBride | ARI | 12.8 | 3.5 to 23.8 |
| TE | Tyler Warren | IND | 12.0 | 2.6 to 23.3 |
| TE | Pat Freiermuth | PIT | 11.1 | 1.8 to 22.4 |
| TE | Travis Kelce | KC | 10.8 | 1.7 to 21.8 |
| TE | Isaiah Likely | NYG | 10.4 | 1.9 to 20.5 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.2 | 9.4 to 36.5 |
| QB | Brock Purdy | SF | 19.9 | 8.2 to 32.7 |
| QB | Matthew Stafford | LA | 19.2 | 8.3 to 31.3 |
| QB | Drake Maye | NE | 18.9 | 7.9 to 31.1 |
| QB | Dak Prescott | DAL | 17.6 | 7.1 to 29.0 |
| QB | Jordan Love | GB | 17.2 | 7.3 to 28.4 |
| RB | Bijan Robinson | ATL | 20.2 | 8.0 to 33.8 |
| RB | Christian McCaffrey | SF | 19.3 | 6.7 to 33.7 |
| RB | Jaylen Warren | PIT | 18.2 | 6.4 to 31.9 |
| RB | Kyren Williams | LA | 17.2 | 5.4 to 30.5 |
| RB | Derrick Henry | BAL | 16.7 | 4.7 to 30.2 |
| RB | Kenneth Walker III | KC | 15.8 | 4.8 to 28.9 |
| RB | Jonathan Taylor | IND | 15.1 | 3.7 to 28.2 |
| RB | James Cook | BUF | 14.7 | 4.3 to 26.8 |
| RB | Ashton Jeanty | LV | 13.5 | 3.9 to 25.0 |
| RB | Emanuel Wilson | SEA | 13.4 | 3.1 to 25.8 |
| WR | Jaxon Smith-Njigba | SEA | 15.5 | 4.9 to 27.7 |
| WR | Puka Nacua | LA | 15.2 | 4.2 to 27.9 |
| WR | Mike Evans | SF | 13.5 | 3.1 to 25.1 |
| WR | CeeDee Lamb | DAL | 12.9 | 3.5 to 23.7 |
| WR | Christian Watson | GB | 11.8 | 1.5 to 23.3 |
| WR | Zay Flowers | BAL | 11.7 | 2.7 to 22.1 |
| WR | Drake London | ATL | 10.9 | 2.2 to 21.0 |
| WR | George Pickens | DAL | 10.8 | 2.2 to 21.0 |
| WR | Nico Collins | HOU | 10.6 | 1.7 to 21.1 |
| WR | Tetairoa McMillan | CAR | 10.6 | 2.1 to 20.7 |
| WR | Parker Washington | JAX | 10.6 | 1.5 to 21.0 |
| WR | DK Metcalf | PIT | 10.0 | 1.8 to 19.6 |
| TE | George Kittle | SF | 12.3 | 2.8 to 23.0 |
| TE | Trey McBride | ARI | 9.5 | 2.1 to 18.1 |
| TE | Tyler Warren | IND | 9.4 | 1.5 to 19.0 |
| TE | Pat Freiermuth | PIT | 8.9 | 1.0 to 18.6 |
| TE | Travis Kelce | KC | 8.6 | 0.9 to 17.7 |
| TE | Hunter Henry | NE | 8.1 | 1.0 to 16.7 |
| K | Spencer Shrader | IND | 10.8 | 1.0 to 22.4 |
| K | Ka'imi Fairbairn | HOU | 9.9 | 1.0 to 22.4 |
| K | Jason Myers | SEA | 9.4 | 1.0 to 21.4 |
| K | Harrison Butker | KC | 9.1 | 1.0 to 19.6 |

## 5. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses came from MFL at the time of the pull. Re-run Thursday morning and Sunday morning for fresh news.
- Weather, referee tendencies and in-game injuries are not modeled.