# Week 8 Full Simulation Report - 28 OCT 2026

Decision support only. Nothing was submitted anywhere. ff-simulator ran 10,000 versions of each of the 14 NFL games (anchored on the live market line, each head coach's tendencies, the merged injury file from 8:06 PM ET, and recent usage). ff-play-sim ran 1,500 play-by-play versions of each game (not anchored on the market). Lineup numbers blend the two with the backtest weights (QB 0.9, K 0.5, RB 0.15, WR 0.2, TE 0.2 on the play sim); defenders use the old sim only. Byes: NO, NYG, SF, HOU.

## 1. IRFL lineup


| Slot | Start | Team | Blend pts | Why, in one line |
|---|---|---|---|---|
| QB | **Jacoby Brissett** | ARI | 23.7 | ARI starter Weeks 5 to 7 (35 to 52 dropbacks a game, nflverse); no designation (ESPN 10/26). At DAL, total 54.5. Both sims rank him well over Goff (16.1) and Williams (15.3). |
| RB | **Rachaad White** | WAS | 9.9 | Lead back with Croskey-Merritt on IR (MFL IR, back about 11/23); WAS off a bye; no designation (nflverse ACT 10/28). |
| RB | **Rico Dowdle** | PIT | 8.5 | 15 touches last week (9 carries, 6 catches, ESPN 10/25). Warren is the lead back and one preview calls Dowdle a sit (Big Lead 10/28). Best of a thin group: Spears and B. Robinson are both Questionable. |
| WR | **Zay Flowers** | BAL | 16.9 | 8 of 11 for 137 and a TD in Week 7 (ESPN 10/25); Lamar expected back (Yahoo 10/28). |
| WR | **Justin Jefferson** | MIN | 13.7 | 4 of 7 for 44 in Week 7 (ESPN 10/25); no designation found this week. |
| WR | **Jameson Williams** | DET | 10.4 | 5 of 9, 91 yards, 2 TDs in Week 7 (ESPN 10/26); Gibbs DNP (shoulder) could push more volume to the passing game. |
| WR | **Ryan Flournoy** | DAL | 9.4 | 4 to 9 targets every week, 68 to 87% of snaps (Weeks 5 to 6); Pickens limited and Turpin DNP Wednesday (Blogging The Boys 10/28). Tied with Allen; see WR4 note. |
| TE | **T.J. Hockenson** | MIN | 10.7 | Back from the concussion, 4 of 5 for 35 and a TD in Week 7 (ESPN 10/25). Beats LaPorta (8.6) and Goedert (8.0) on the blend. |
| PK | **Evan McPherson** | CIN | 9.1 | CIN -10.5 at home, 5 PATs last week (ESPN 10/25). Small edge over Folk (8.5) and Bates (8.4). |
| DL | **Aidan Hutchinson** | DET | 5.5 | Every-down edge (90% snaps Week 5); no designation (nflverse ACT 10/28). |
| DL | **D.J. Wonnum** | DET | 4.3 | About half the snaps (49% Week 5); best of the rest (Davis 3.1, Kancey 1.1; T. Robinson on IR). |
| LB | **Bobby Okereke** | CAR | 8.0 | 10 tackles in Week 7 (ESPN 10/28), 98% snaps Week 6. Plays Thursday. |
| LB | **Jack Gibbens** | ARI | 5.4 | 7 tackles in Week 7 (ESPN 10/28), 76 to 84% snaps. |
| LB | **Justin Strnad** | DEN | 4.7 | 89 to 90% snaps Weeks 5 to 6; no designation (nflverse ACT 10/28). |
| DB | **Nick Scott** | CAR | 5.5 | 100% snaps Week 6; no designation found. Plays Thursday. |
| DB | **D.J. Reed** | DET | 5.4 | 99% snaps Week 5; no designation (nflverse ACT 10/28). |
| DB | **Kamren Kinchens** | LAR | 4.6 | 56 to 67% snaps; beats Moss (4.3, 24% snaps Week 6), Mukuba (4.0), Molden (3.9). |

Projected 155.9 (10th to 90th: 122 to 192). Opponent's saved lineup projects 140.4. **Win chance about 65%.** The lineup saved on MFL right now projects 126.0 and wins about 35%. It starts Sanker (NO is on bye, scores 0), Michael Carter (2.2), Dodson (1.1), Goff, LaPorta, Bates, Moss and Golden. The recommended lineup beats it in 86% of sims by about 30 points.

**Changes to make on MFL:** Goff to Brissett, Carter to White, Golden to Flournoy (unless Golden is active, see below), LaPorta to Hockenson, Bates to McPherson, Dodson to Gibbens, Moss to Scott, Sanker to Reed.

Other lineup builds on the old sim alone (EXPECTED, SAFE, CONTINGENCY) all land at 154.0 and match this lineup except Bates at kicker and Allen at WR4; the blend moves kicker to McPherson. Full pick reasoning, start/sit calls and the check list are in the Week 8 pick doc.

## 2. Winners and pick'em

The old sim's win odds are the market's odds by design. The play sim column is its own margin with 1.5 points of home field added. The card pick is centered on the market plus 15% of the gap to the play sim, because neither the play sim (269-game backtest, no information beyond the closing line) nor the EPA power rating (416 games, blend error 9.70 vs market 9.56) beat the market.

| # | Game | Card | Market | Play sim | ATS pick | Cover | SU pick (win %) |
|---|---|---|---|---|---|---|---|
| 1 | Carolina Panthers at Green Bay Packers | Green Bay -3.5 | -3.5 | -3.1 | Carolina +3.5 | 50.2% | Packers (60%) |
| 2 | Arizona Wildcats at Texas Tech Red Raiders | Texas Tech -3.5 | -3.5 | n/a | Arizona +3.5 | 50.0% | n/a |
| 3 | Boston College Eagles at Duke Blue Devils | Duke -7.5 | -7.0 | n/a | Boston College +7.5 | 51.3% | n/a |
| 4 | Wisconsin Badgers at Iowa Hawkeyes | Iowa -3.5 | -3.5 | n/a | Wisconsin +3.5 | 50.0% | n/a |
| 5 | Kansas State Wildcats at Colorado Buffaloes | Kansas State -2.5 | +1.5 | n/a | Colorado +2.5 | 60.2% | n/a |
| 6 | Ohio State Buckeyes at USC Trojans | Ohio State -6.5 | -6.5 | n/a | Usc +6.5 | 50.0% | n/a |
| 7 | Oregon State Beavers at Fresno State Bulldogs | Oregon State -5.5 | -5.5 | n/a | Fresno State +5.5 | 50.0% | n/a |
| 8 | Baltimore Ravens at Buffalo Bills | Buffalo -3.5 | -3.0 | -3.5 | Baltimore +3.5 | 51.3% | Bills (59%) |
| 9 | Tennessee Titans at Cincinnati Bengals | Cincinnati -10.5 | -10.5 | -10.9 | Cincinnati -10.5 | 50.2% | Bengals (79%) |
| 10 | Arizona Cardinals at Dallas Cowboys | Dallas -6.5 | -7.0 | -4.8 | Dallas -6.5 | 50.5% | Cowboys (69%) |
| 11 | Minnesota Vikings at Detroit Lions | Detroit -3.5 | -3.5 | +0.2 | Minnesota +3.5 | 51.7% | Lions (59%) |
| 12 | Las Vegas Raiders at New York Jets | Ny Jets -1.5 | -1.5 | -2.7 | NY Jets -1.5 | 50.5% | Jets (55%) |
| 13 | Cleveland Browns at Pittsburgh Steelers | Pittsburgh -3.5 | -3.5 | -4.8 | Pittsburgh -3.5 | 50.6% | Steelers (61%) |
| 14 | Atlanta Falcons at Tampa Bay Buccaneers | Tampa Bay -2.5 | -2.5 | +2.4 | Atlanta +2.5 | 52.2% | Buccaneers (55%) |
| 15 | Indianapolis Colts at Jacksonville Jaguars | Jacksonville -7.5 | -10.0 | -13.1 | Jacksonville -7.5 | 58.9% | Jaguars (79%) |
| 16 | Los Angeles Chargers at Los Angeles Rams | La Rams -6.5 | -6.5 | -12.1 | LA Rams -6.5 | 52.5% | Rams (71%) |
| 17 | New England Patriots at Miami Dolphins | New England -7.5 | -7.0 | -9.1 | Miami +7.5 | 50.6% | Patriots (71%) |
| 18 | Kansas City Chiefs at Denver Broncos | Kansas City -1.5 | -1.5 | -0.7 | Denver +1.5 | 50.4% | Chiefs (54%) |
| 19 | Philadelphia Eagles at Washington Commanders | Washington -3.5 | -5.5 | -2.0 | Washington -3.5 | 54.4% | Commanders (65%) |
| 20 | Chicago Bears at Seattle Seahawks | Seattle -2.5 | -3.0 | -8.4 | Seattle -2.5 | 54.0% | Seahawks (61%) |

Market and play sim numbers are shown from the card favorite's side (minus = favored).

Eliminator: Zac is out of EC2 (Week 6), so no pick. For reference only, the safest market favorites are CIN 79.5%, JAX 78.4%, DAL and NE 70.9%.

## 3. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ DAL

Market: DAL -7.0, total 54.5. Sim: ARI 23.9, DAL 30.7. DAL wins 69.5%, ARI wins 30.5%. Median margin +6.9 for DAL.

| Team stat | ARI | DAL |
|---|---|---|
| Plays | 65 | 65 |
| Pass attempts / completions | 39 / 25 | 35 / 22 |
| Passing yards | 270 | 267 |
| Rush attempts / yards | 24 / 103 | 28 / 127 |
| Sacks taken | 2.2 | 2.3 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.7 / 0.9 | 1.9 / 1.4 |
| Field goals | 1.8 | 2.3 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 22.0 | 270 pass yd, 1.7 TD, 0.7 INT; 2.9 rush, 13 yd |  |
| RB | Tyler Allgeier | 7.8 | 7.0 car, 26 yd, 0.26 TD; 1.9 rec, 16 yd, 0.04 TD |  |
| RB | Jeremiyah Love | 6.2 | 8.9 car, 37 yd, 0.26 TD; 1.4 rec, 11 yd, 0.10 TD | Questionable |
| RB | Bam Knight | 6.1 | 4.7 car, 24 yd, 0.16 TD; 1.2 rec, 11 yd, 0.06 TD |  |
| WR | Michael Wilson | 13.7 | 5.3 rec, 63 yd, 0.35 TD |  |
| WR | Kendrick Bourne | 7.8 | 3.6 rec, 36 yd, 0.11 TD |  |
| WR | Reggie Virgil | 3.2 | 1.3 rec, 16 yd, 0.05 TD |  |
| WR | Xavier Weaver | 0.9 | 0.5 rec, 5 yd, 0.01 TD | Questionable |
| TE | Trey McBride | 17.9 | 8.0 rec, 72 yd, 0.47 TD |  |
| TE | Elijah Higgins | 4.8 | 2.1 rec, 22 yd, 0.09 TD |  |
| K | Chad Ryland | 9.9 | 2.0 FG, 2.4 XP |  |
| DL | Darius Robinson | 2.9 | 1.1 solo, 1.9 ast, 0.25 sack, 0.00 PD, 0.00 INT |  |
| DL | Roy Lopez | 2.9 | 1.2 solo, 2.0 ast, 0.18 sack, 0.20 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.5 | 3.2 solo, 4.1 ast, 0.05 sack, 0.11 PD, 0.00 INT |  |
| LB | Mack Wilson | 5.3 | 3.0 solo, 3.9 ast, 0.00 sack, 0.10 PD, 0.00 INT |  |
| LB | Cody Simon | 3.3 | 1.7 solo, 2.4 ast, 0.03 sack, 0.05 PD, 0.00 INT |  |
| DB | Budda Baker | 7.3 | 3.6 solo, 3.1 ast, 0.39 sack, 0.54 PD, 0.13 INT |  |
| DB | Denzel Burke | 4.4 | 2.5 solo, 1.0 ast, 0.00 sack, 0.78 PD, 0.15 INT |  |
| DB | Dadrion Taylor-Demerson | 3.4 | 2.6 solo, 1.5 ast, 0.00 sack, 0.07 PD, 0.00 INT |  |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 22.1 | 267 pass yd, 1.9 TD, 0.7 INT; 2.2 rush, 10 yd |  |
| RB | Javonte Williams | 15.4 | 14.7 car, 67 yd, 0.86 TD; 1.8 rec, 13 yd, 0.12 TD |  |
| RB | Tyler Goodson | 3.9 | 4.7 car, 20 yd, 0.13 TD; 0.5 rec, 5 yd, 0.03 TD |  |
| RB | Jaydon Blue | 2.1 | 2.7 car, 12 yd, 0.14 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | CeeDee Lamb | 17.0 | 6.1 rec, 73 yd, 0.62 TD |  |
| WR | George Pickens | 9.8 | 4.7 rec, 62 yd, 0.38 TD | Questionable |
| WR | Ryan Flournoy | 9.1 | 3.5 rec, 41 yd, 0.25 TD |  |
| WR | KaVontae Turpin | 2.1 | 0.6 car, 3 yd, 0.06 TD; 0.8 rec, 10 yd, 0.07 TD | Questionable |
| TE | Jake Ferguson | 5.5 | 2.2 rec, 18 yd, 0.25 TD |  |
| TE | Brevyn Spann-Ford | 2.7 | 1.1 rec, 12 yd, 0.06 TD |  |
| K | Brandon Aubrey | 10.0 | 1.8 FG, 3.1 XP |  |
| DL | Quinnen Williams | 3.2 | 1.9 solo, 1.2 ast, 0.43 sack, 0.19 PD, 0.05 INT | Questionable |
| DL | Otito Ogbonnia | 2.7 | 1.9 solo, 1.6 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Dee Winters | 4.0 | 3.2 solo, 1.9 ast, 0.00 sack, 0.23 PD, 0.22 INT | Questionable |
| LB | DeMarvion Overshown | 4.0 | 1.9 solo, 1.7 ast, 0.00 sack, 0.51 PD, 0.26 INT |  |
| LB | Jaishawn Barham | 4.0 | 2.7 solo, 2.1 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Caleb Downs | 5.0 | 4.3 solo, 2.9 ast, 0.11 sack, 0.12 PD, 0.00 INT | Questionable |
| DB | Joey Porter Jr. | 4.8 | 2.6 solo, 1.1 ast, 0.00 sack, 1.67 PD, 0.00 INT |  |
| DB | DaRon Bland | 3.9 | 2.8 solo, 1.0 ast, 0.00 sack, 0.66 PD, 0.00 INT |  |

### ATL @ TB

Market: TB -2.5, total 45.0. Sim: ATL 21.2, TB 23.8. TB wins 57.9%, ATL wins 42.1%. Median margin +2.6 for TB.

| Team stat | ATL | TB |
|---|---|---|
| Plays | 62 | 64 |
| Pass attempts / completions | 32 / 20 | 32 / 20 |
| Passing yards | 227 | 198 |
| Rush attempts / yards | 29 / 128 | 29 / 130 |
| Sacks taken | 2.0 | 2.4 |
| Interceptions thrown | 0.7 | 0.8 |
| Passing / rushing TDs | 1.2 / 1.1 | 1.5 / 1.1 |
| Field goals | 1.6 | 1.8 |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 16.1 | 227 pass yd, 1.2 TD, 0.7 INT; 2.5 rush, 9 yd |  |
| RB | Bijan Robinson | 19.5 | 17.3 car, 82 yd, 0.61 TD; 3.8 rec, 31 yd, 0.16 TD |  |
| RB | Brian Robinson | 5.0 | 7.3 car, 29 yd, 0.41 TD; 0.7 rec, 6 yd, 0.02 TD | Questionable |
| WR | Drake London | 13.7 | 5.3 rec, 69 yd, 0.25 TD |  |
| WR | Jahan Dotson | 6.1 | 2.0 rec, 31 yd, 0.17 TD |  |
| WR | Zachariah Branch | 2.8 | 1.4 rec, 11 yd, 0.03 TD |  |
| WR | Olamide Zaccheaus | 1.4 | 0.9 rec, 7 yd, 0.04 TD | Questionable |
| TE | Kyle Pitts | 9.8 | 4.0 rec, 38 yd, 0.33 TD |  |
| TE | Austin Hooper | 2.9 | 1.3 rec, 12 yd, 0.08 TD |  |
| K | Nick Folk | 8.6 | 1.7 FG, 2.2 XP |  |
| DL | Za'Darius Smith | 3.3 | 0.8 solo, 0.3 ast, 0.74 sack, 0.12 PD, 0.00 INT |  |
| DL | Gervon Dexter Sr. | 3.2 | 1.3 solo, 1.4 ast, 0.23 sack, 0.10 PD, 0.00 INT |  |
| LB | Kendal Daniels | 7.5 | 5.1 solo, 1.3 ast, 0.15 sack, 0.34 PD, 0.20 INT |  |
| LB | Harold Perkins Jr. | 4.5 | 2.7 solo, 2.3 ast, 0.07 sack, 0.14 PD, 0.00 INT |  |
| LB | Divine Deablo | 3.4 | 2.8 solo, 2.6 ast, 0.02 sack, 0.25 PD, 0.00 INT | Questionable |
| DB | Xavier Watts | 6.7 | 3.5 solo, 2.7 ast, 0.05 sack, 0.46 PD, 0.20 INT |  |
| DB | Jessie Bates | 6.6 | 3.0 solo, 2.7 ast, 0.00 sack, 0.59 PD, 0.19 INT |  |
| DB | C.J. Henderson | 6.3 | 4.0 solo, 1.0 ast, 0.00 sack, 1.16 PD, 0.05 INT |  |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Baker Mayfield | 16.6 | 198 pass yd, 1.5 TD, 0.8 INT; 2.2 rush, 11 yd |  |
| RB | Bucky Irving | 14.3 | 14.8 car, 64 yd, 0.54 TD; 2.4 rec, 15 yd, 0.17 TD |  |
| RB | Kenny Gainwell | 5.0 | 4.3 car, 20 yd, 0.09 TD; 1.8 rec, 13 yd, 0.17 TD | Questionable |
| RB | Sean Tucker | 3.0 | 3.1 car, 14 yd, 0.25 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Chris Godwin Jr. | 9.4 | 4.3 rec, 39 yd, 0.20 TD |  |
| WR | Emeka Egbuka | 7.6 | 4.2 rec, 36 yd, 0.32 TD | Questionable |
| WR | Ted Hurst III | 5.7 | 2.1 rec, 25 yd, 0.18 TD |  |
| WR | Tez Johnson | 4.6 | 1.5 rec, 20 yd, 0.16 TD |  |
| TE | Cade Otton | 6.8 | 3.1 rec, 29 yd, 0.15 TD |  |
| TE | Payne Durham | 0.8 | 0.3 rec, 3 yd, 0.01 TD |  |
| K | Chase McLaughlin | 9.7 | 1.9 FG, 2.4 XP |  |
| DL | A'Shawn Robinson | 3.0 | 0.7 solo, 1.9 ast, 0.09 sack, 0.28 PD, 0.27 INT |  |
| DL | Vita Vea | 2.4 | 1.0 solo, 1.2 ast, 0.20 sack, 0.22 PD, 0.00 INT |  |
| LB | Josiah Trotter | 6.4 | 4.5 solo, 5.0 ast, 0.09 sack, 0.47 PD, 0.09 INT | Questionable |
| LB | David Walker | 4.6 | 2.4 solo, 1.1 ast, 0.55 sack, 0.00 PD, 0.00 INT |  |
| LB | Alex Anzalone | 4.4 | 2.1 solo, 2.9 ast, 0.11 sack, 0.14 PD, 0.14 INT |  |
| DB | Jacob Parrish | 6.1 | 3.8 solo, 0.8 ast, 0.00 sack, 1.35 PD, 0.15 INT |  |
| DB | Keionte Scott | 5.9 | 4.1 solo, 1.7 ast, 0.17 sack, 0.45 PD, 0.00 INT |  |
| DB | Tykee Smith | 4.9 | 2.6 solo, 2.7 ast, 0.00 sack, 0.26 PD, 0.14 INT |  |

### BAL @ BUF

Market: BUF -3.0, total 54.0. Sim: BAL 25.5, BUF 28.6. BUF wins 59.5%, BAL wins 40.5%. Median margin +3.1 for BUF.

| Team stat | BAL | BUF |
|---|---|---|
| Plays | 61 | 62 |
| Pass attempts / completions | 31 / 21 | 31 / 20 |
| Passing yards | 234 | 246 |
| Rush attempts / yards | 28 / 133 | 30 / 135 |
| Sacks taken | 1.8 | 2.1 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.4 / 1.4 | 1.5 / 1.6 |
| Field goals | 1.9 | 2.2 |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Lamar Jackson | 14.7 | 175 pass yd, 1.0 TD, 0.4 INT; 3.0 rush, 16 yd | Questionable |
| RB | Derrick Henry | 16.1 | 18.1 car, 81 yd, 0.95 TD; 1.1 rec, 9 yd, 0.09 TD |  |
| RB | Justice Hill | 4.6 | 2.1 car, 11 yd, 0.06 TD; 1.6 rec, 12 yd, 0.05 TD |  |
| RB | Rasheen Ali | 1.3 | 0.8 car, 4 yd, 0.02 TD; 0.3 rec, 3 yd, 0.03 TD |  |
| WR | Zay Flowers | 16.9 | 6.2 rec, 77 yd, 0.44 TD |  |
| WR | Rashod Bateman | 5.2 | 2.0 rec, 25 yd, 0.11 TD |  |
| WR | Ja'Kobi Lane | 4.1 | 2.0 rec, 18 yd, 0.06 TD |  |
| WR | Devontez Walker | 2.7 | 0.8 rec, 11 yd, 0.13 TD |  |
| TE | Mark Andrews | 6.6 | 3.2 rec, 25 yd, 0.15 TD |  |
| TE | Josh Cuevas | 4.4 | 1.7 rec, 19 yd, 0.14 TD |  |
| K | Tyler Loop | 8.9 | 1.7 FG, 2.6 XP |  |
| DL | Travis Jones | 3.1 | 1.5 solo, 1.3 ast, 0.17 sack, 0.07 PD, 0.00 INT |  |
| DL | Nnamdi Madubuike | 3.0 | 2.1 solo, 1.2 ast, 0.10 sack, 0.00 PD, 0.00 INT |  |
| LB | Trenton Simpson | 5.8 | 3.3 solo, 3.1 ast, 0.14 sack, 0.09 PD, 0.09 INT |  |
| LB | Roquan Smith | 5.1 | 3.7 solo, 4.0 ast, 0.19 sack, 0.07 PD, 0.06 INT | Questionable |
| LB | Mike Green | 2.8 | 1.2 solo, 0.7 ast, 0.37 sack, 0.00 PD, 0.00 INT |  |
| DB | K'Von Wallace | 6.0 | 4.0 solo, 0.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Marlon Humphrey | 4.9 | 2.6 solo, 1.2 ast, 0.03 sack, 0.89 PD, 0.12 INT |  |
| DB | Kyle Hamilton | 4.9 | 4.5 solo, 2.1 ast, 0.00 sack, 0.46 PD, 0.10 INT | Questionable |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 24.4 | 246 pass yd, 1.5 TD, 0.6 INT; 6.9 rush, 31 yd |  |
| RB | James Cook | 15.7 | 16.8 car, 77 yd, 0.78 TD; 1.5 rec, 16 yd, 0.08 TD |  |
| RB | Ty Johnson | 6.4 | 2.0 car, 8 yd, 0.10 TD; 2.1 rec, 24 yd, 0.11 TD |  |
| RB | Ray Davis | 3.0 | 2.4 car, 11 yd, 0.06 TD; 0.6 rec, 6 yd, 0.05 TD |  |
| WR | Khalil Shakir | 8.7 | 3.5 rec, 39 yd, 0.21 TD |  |
| WR | Keon Coleman | 7.6 | 2.6 rec, 34 yd, 0.28 TD |  |
| WR | DJ Moore | 4.4 | 2.2 rec, 26 yd, 0.16 TD | Questionable |
| WR | Josh Palmer | 3.2 | 1.0 rec, 15 yd, 0.12 TD |  |
| TE | Dalton Kincaid | 5.6 | 3.1 rec, 35 yd, 0.16 TD | Questionable |
| TE | Dawson Knox | 4.2 | 1.7 rec, 15 yd, 0.16 TD |  |
| K | Tyler Bass | 10.4 | 2.0 FG, 2.9 XP |  |
| DL | Deone Walker | 2.8 | 1.3 solo, 1.7 ast, 0.07 sack, 0.44 PD, 0.00 INT |  |
| DL | DeWayne Carter | 2.5 | 1.3 solo, 1.2 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| LB | Greg Rousseau | 5.4 | 1.6 solo, 1.3 ast, 0.69 sack, 0.56 PD, 0.00 INT |  |
| LB | Terrel Bernard | 5.1 | 3.4 solo, 2.8 ast, 0.00 sack, 0.15 PD, 0.00 INT |  |
| LB | Dorian Williams | 4.7 | 2.3 solo, 3.6 ast, 0.00 sack, 0.23 PD, 0.13 INT |  |
| DB | Cole Bishop | 5.4 | 3.6 solo, 2.9 ast, 0.00 sack, 0.31 PD, 0.03 INT |  |
| DB | Christian Benford | 4.8 | 2.7 solo, 1.1 ast, 0.04 sack, 0.78 PD, 0.08 INT |  |
| DB | Davison Igbinosun | 4.7 | 2.6 solo, 1.9 ast, 0.00 sack, 1.18 PD, 0.00 INT |  |

### CAR @ GB

Market: GB -3.5, total 47.0. Sim: CAR 21.8, GB 25.3. GB wins 60.6%, CAR wins 39.4%. Median margin +3.8 for GB.

| Team stat | CAR | GB |
|---|---|---|
| Plays | 62 | 61 |
| Pass attempts / completions | 34 / 21 | 32 / 20 |
| Passing yards | 240 | 232 |
| Rush attempts / yards | 25 / 107 | 27 / 104 |
| Sacks taken | 2.3 | 2.1 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.4 / 0.9 | 1.5 / 1.2 |
| Field goals | 1.6 | 1.9 |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 18.5 | 240 pass yd, 1.4 TD, 0.7 INT; 3.1 rush, 13 yd |  |
| RB | Chuba Hubbard | 13.7 | 14.5 car, 62 yd, 0.51 TD; 2.2 rec, 16 yd, 0.14 TD |  |
| RB | AJ Dillon | 2.3 | 3.7 car, 14 yd, 0.07 TD; 0.3 rec, 2 yd, 0.00 TD |  |
| RB | Anthony Tyus III | 1.6 | 1.2 car, 6 yd, 0.17 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Tetairoa McMillan | 13.6 | 5.3 rec, 64 yd, 0.32 TD |  |
| WR | Jalen Coker | 10.3 | 4.2 rec, 45 yd, 0.26 TD |  |
| WR | John Metchie III | 4.6 | 1.9 rec, 19 yd, 0.12 TD |  |
| WR | Brycen Tremayne | 2.1 | 0.9 rec, 11 yd, 0.03 TD |  |
| TE | Darren Waller | 6.0 | 2.1 rec, 26 yd, 0.23 TD |  |
| TE | Tommy Tremble | 5.2 | 2.2 rec, 20 yd, 0.17 TD |  |
| K | Ryan Fitzgerald | 8.3 | 1.6 FG, 2.2 XP |  |
| DL | Derrick Brown | 4.0 | 2.1 solo, 1.9 ast, 0.09 sack, 0.65 PD, 0.00 INT |  |
| DL | Aaron Hall | 2.2 | 0.8 solo, 2.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 8.2 | 3.6 solo, 2.7 ast, 0.34 sack, 0.43 PD, 0.28 INT |  |
| LB | Bobby Okereke | 8.0 | 4.6 solo, 2.5 ast, 0.19 sack, 0.89 PD, 0.13 INT |  |
| LB | Nick Hampton | 3.9 | 2.9 solo, 2.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Will Lee III | 5.6 | 2.8 solo, 2.0 ast, 0.00 sack, 1.07 PD, 0.00 INT |  |
| DB | Nick Scott | 5.5 | 4.1 solo, 2.0 ast, 0.00 sack, 0.17 PD, 0.04 INT |  |
| DB | Tre'von Moehrig | 4.2 | 2.8 solo, 1.8 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 18.2 | 232 pass yd, 1.5 TD, 0.7 INT; 1.5 rush, 6 yd |  |
| RB | MarShawn Lloyd | 8.2 | 7.1 car, 25 yd, 0.50 TD; 1.3 rec, 10 yd, 0.08 TD |  |
| RB | Josh Jacobs | 7.7 | 5.7 car, 23 yd, 0.26 TD; 1.5 rec, 14 yd, 0.17 TD |  |
| RB | Pierre Strong | 7.5 | 5.3 car, 20 yd, 0.13 TD; 2.4 rec, 19 yd, 0.08 TD |  |
| WR | Christian Watson | 11.9 | 3.9 rec, 55 yd, 0.42 TD |  |
| WR | Matthew Golden | 7.9 | 3.8 rec, 48 yd, 0.31 TD | Questionable |
| WR | Savion Williams | 2.9 | 0.8 car, 4 yd, 0.02 TD; 1.1 rec, 11 yd, 0.04 TD |  |
| WR | Bo Melton | 1.7 | 0.7 rec, 7 yd, 0.05 TD |  |
| TE | Tucker Kraft | 8.1 | 3.4 rec, 32 yd, 0.25 TD |  |
| TE | Jonnu Smith | 1.7 | 0.7 rec, 8 yd, 0.03 TD |  |
| K | Trey Smack | 8.5 | 1.6 FG, 2.6 XP |  |
| DL | Barryn Sorrell | 2.6 | 1.4 solo, 1.4 ast, 0.12 sack, 0.00 PD, 0.00 INT |  |
| DL | Anthony Campbell | 2.5 | 1.4 solo, 0.0 ast, 0.32 sack, 0.31 PD, 0.00 INT | Questionable |
| LB | Isaiah McDuffie | 4.9 | 2.9 solo, 2.7 ast, 0.01 sack, 0.03 PD, 0.03 INT |  |
| LB | Lukas Van Ness | 3.6 | 1.9 solo, 1.2 ast, 0.37 sack, 0.00 PD, 0.00 INT |  |
| LB | Ty'Ron Hopper | 3.0 | 1.3 solo, 2.0 ast, 0.00 sack, 0.27 PD, 0.12 INT |  |
| DB | Evan Williams | 8.0 | 4.4 solo, 3.1 ast, 0.10 sack, 0.71 PD, 0.26 INT |  |
| DB | Brandon Cisse | 6.3 | 3.6 solo, 1.0 ast, 0.21 sack, 1.03 PD, 0.18 INT |  |
| DB | Xavier McKinney | 5.9 | 2.9 solo, 2.4 ast, 0.11 sack, 0.52 PD, 0.32 INT |  |

### CHI @ SEA

Market: SEA -3.0, total 46.5. Sim: CHI 21.7, SEA 24.9. SEA wins 59.3%, CHI wins 40.7%. Median margin +3.3 for SEA.

| Team stat | CHI | SEA |
|---|---|---|
| Plays | 66 | 61 |
| Pass attempts / completions | 35 / 23 | 31 / 20 |
| Passing yards | 223 | 240 |
| Rush attempts / yards | 29 / 117 | 28 / 119 |
| Sacks taken | 2.5 | 2.4 |
| Interceptions thrown | 0.8 | 0.8 |
| Passing / rushing TDs | 1.3 / 1.1 | 1.4 / 1.3 |
| Field goals | 1.6 | 1.9 |

**CHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Caleb Williams | 16.5 | 223 pass yd, 1.3 TD, 0.8 INT; 3.0 rush, 13 yd |  |
| RB | D'Andre Swift | 12.1 | 11.4 car, 44 yd, 0.48 TD; 2.8 rec, 18 yd, 0.07 TD |  |
| RB | Kyle Monangai | 5.0 | 7.8 car, 33 yd, 0.26 TD; 1.0 rec, 8 yd, 0.03 TD | Questionable |
| RB | Roschon Johnson | 4.7 | 3.2 car, 12 yd, 0.10 TD; 1.5 rec, 12 yd, 0.03 TD |  |
| WR | Luther Burden III | 13.1 | 0.7 car, 3 yd, 0.01 TD; 5.2 rec, 58 yd, 0.29 TD |  |
| WR | Rome Odunze | 7.7 | 3.4 rec, 38 yd, 0.10 TD |  |
| WR | Kalif Raymond | 6.7 | 3.2 rec, 25 yd, 0.16 TD |  |
| WR | Jahdae Walker | 2.1 | 0.7 rec, 6 yd, 0.14 TD |  |
| TE | Colston Loveland | 11.3 | 5.0 rec, 41 yd, 0.37 TD |  |
| TE | Sam Roush | 1.0 | 0.5 rec, 4 yd, 0.01 TD |  |
| K | Cairo Santos | 8.2 | 1.6 FG, 2.2 XP |  |
| DL | Austin Booker | 4.7 | 2.3 solo, 1.0 ast, 0.50 sack, 0.15 PD, 0.00 INT |  |
| DL | Montez Sweat | 2.5 | 0.9 solo, 0.9 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Bush | 5.3 | 3.1 solo, 2.3 ast, 0.13 sack, 0.10 PD, 0.00 INT |  |
| LB | T.J. Edwards | 3.3 | 2.1 solo, 1.8 ast, 0.03 sack, 0.44 PD, 0.17 INT | Questionable |
| LB | D'Marco Jackson | 3.1 | 1.3 solo, 1.9 ast, 0.04 sack, 0.21 PD, 0.17 INT |  |
| DB | Dillon Thieneman | 6.4 | 3.1 solo, 3.1 ast, 0.25 sack, 0.61 PD, 0.12 INT |  |
| DB | Kyler Gordon | 4.9 | 1.2 solo, 0.5 ast, 0.86 sack, 0.00 PD, 0.00 INT |  |
| DB | Cam Lewis | 3.6 | 3.0 solo, 1.1 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |

**SEA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Sam Darnold | 17.5 | 240 pass yd, 1.4 TD, 0.8 INT; 1.7 rush, 8 yd |  |
| RB | Emanuel Wilson | 11.0 | 13.5 car, 54 yd, 0.57 TD; 0.9 rec, 9 yd, 0.09 TD |  |
| RB | George Holani | 5.7 | 4.0 car, 16 yd, 0.18 TD; 1.5 rec, 13 yd, 0.05 TD |  |
| RB | Zach Charbonnet | 4.5 | 4.9 car, 24 yd, 0.33 TD; 0.9 rec, 8 yd, 0.03 TD | Questionable |
| WR | Jaxon Smith-Njigba | 21.9 | 7.8 rec, 100 yd, 0.65 TD |  |
| WR | Cooper Kupp | 6.1 | 2.6 rec, 27 yd, 0.15 TD |  |
| WR | Rashid Shaheed | 4.2 | 2.2 rec, 23 yd, 0.09 TD | Questionable |
| WR | Tory Horton | 3.2 | 1.1 rec, 13 yd, 0.13 TD |  |
| TE | AJ Barner | 6.9 | 2.9 rec, 27 yd, 0.14 TD |  |
| TE | Eric Saubert | 1.5 | 0.5 rec, 5 yd, 0.07 TD |  |
| K | Jason Myers | 10.1 | 2.0 FG, 2.6 XP |  |
| DL | Byron Murphy II | 3.8 | 1.6 solo, 2.0 ast, 0.39 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Williams | 3.4 | 1.7 solo, 1.2 ast, 0.31 sack, 0.15 PD, 0.00 INT |  |
| LB | Ernest Jones | 9.5 | 4.9 solo, 4.9 ast, 0.35 sack, 0.37 PD, 0.17 INT |  |
| LB | Drake Thomas | 4.6 | 3.2 solo, 3.1 ast, 0.10 sack, 0.26 PD, 0.19 INT | Questionable |
| LB | Derick Hall | 3.6 | 1.2 solo, 1.2 ast, 0.41 sack, 0.07 PD, 0.00 INT |  |
| DB | Nick Emmanwori | 6.0 | 3.9 solo, 1.6 ast, 0.32 sack, 0.26 PD, 0.04 INT |  |
| DB | Devon Witherspoon | 5.6 | 3.6 solo, 2.3 ast, 0.00 sack, 0.61 PD, 0.04 INT |  |
| DB | Julian Love | 4.7 | 2.4 solo, 1.4 ast, 0.00 sack, 0.87 PD, 0.24 INT |  |

### CLE @ PIT

Market: PIT -3.5, total 39.5. Sim: CLE 18.0, PIT 21.6. PIT wins 60.4%, CLE wins 39.6%. Median margin +3.6 for PIT.

| Team stat | CLE | PIT |
|---|---|---|
| Plays | 62 | 64 |
| Pass attempts / completions | 34 / 22 | 34 / 22 |
| Passing yards | 237 | 209 |
| Rush attempts / yards | 26 / 107 | 26 / 125 |
| Sacks taken | 2.5 | 2.8 |
| Interceptions thrown | 0.8 | 0.6 |
| Passing / rushing TDs | 1.1 / 0.8 | 1.4 / 0.9 |
| Field goals | 1.4 | 1.6 |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Deshaun Watson | 17.3 | 237 pass yd, 1.1 TD, 0.8 INT; 4.6 rush, 21 yd |  |
| RB | Quinshon Judkins | 9.6 | 9.6 car, 36 yd, 0.32 TD; 2.3 rec, 16 yd, 0.05 TD |  |
| RB | Dylan Sampson | 3.1 | 2.7 car, 12 yd, 0.05 TD; 1.3 rec, 12 yd, 0.05 TD | Questionable |
| RB | Audric Estimé | 2.6 | 4.0 car, 16 yd, 0.18 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | KC Concepcion | 9.5 | 1.0 car, 4 yd, 0.01 TD; 4.2 rec, 42 yd, 0.10 TD |  |
| WR | Denzel Boston | 8.6 | 2.9 rec, 40 yd, 0.29 TD |  |
| WR | Jerry Jeudy | 6.0 | 2.8 rec, 27 yd, 0.09 TD |  |
| WR | Isaiah Bond | 3.1 | 1.2 rec, 17 yd, 0.03 TD |  |
| TE | Harold Fannin Jr. | 9.3 | 3.6 rec, 36 yd, 0.33 TD |  |
| TE | Blake Whiteheart | 1.3 | 0.4 rec, 5 yd, 0.07 TD |  |
| K | Andre Szmyt | 8.6 | 1.8 FG, 1.8 XP |  |
| DL | Adin Huntington | 3.3 | 1.0 solo, 1.7 ast, 0.39 sack, 0.00 PD, 0.00 INT |  |
| DL | Sam Williams | 3.3 | 1.9 solo, 1.4 ast, 0.16 sack, 0.16 PD, 0.00 INT |  |
| LB | Quincy Williams | 7.5 | 4.2 solo, 3.0 ast, 0.19 sack, 0.31 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 6.0 | 3.7 solo, 5.8 ast, 0.18 sack, 0.16 PD, 0.00 INT | Questionable |
| LB | Jerome Baker | 1.2 | 0.3 solo, 1.2 ast, 0.02 sack, 0.00 PD, 0.00 INT |  |
| DB | Ronnie Hickman Jr. | 6.0 | 3.1 solo, 3.0 ast, 0.08 sack, 0.39 PD, 0.09 INT |  |
| DB | Denzel Ward | 4.7 | 1.8 solo, 1.4 ast, 0.00 sack, 1.09 PD, 0.28 INT |  |
| DB | Tyson Campbell | 4.5 | 2.4 solo, 1.9 ast, 0.00 sack, 0.53 PD, 0.00 INT |  |

**PIT**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Aaron Rodgers | 16.8 | 209 pass yd, 1.4 TD, 0.6 INT; 1.7 rush, 7 yd |  |
| RB | Jaylen Warren | 18.7 | 15.3 car, 76 yd, 0.62 TD; 3.3 rec, 32 yd, 0.17 TD |  |
| RB | Rico Dowdle | 8.8 | 6.4 car, 28 yd, 0.12 TD; 2.9 rec, 20 yd, 0.08 TD |  |
| WR | DK Metcalf | 12.0 | 5.1 rec, 51 yd, 0.25 TD |  |
| WR | Germie Bernard | 10.9 | 5.2 rec, 43 yd, 0.23 TD |  |
| WR | Ben Skowronek | 1.0 | 0.5 rec, 5 yd, 0.08 TD | Questionable |
| TE | Pat Freiermuth | 8.1 | 3.3 rec, 28 yd, 0.31 TD |  |
| TE | Darnell Washington | 6.1 | 2.5 rec, 21 yd, 0.26 TD |  |
| K | Chris Boswell | 9.5 | 1.9 FG, 2.2 XP |  |
| DL | Cameron Heyward | 4.0 | 1.8 solo, 1.9 ast, 0.21 sack, 0.42 PD, 0.00 INT |  |
| DL | Keeanu Benton | 2.8 | 1.5 solo, 1.4 ast, 0.05 sack, 0.42 PD, 0.00 INT |  |
| LB | Payton Wilson | 7.3 | 4.2 solo, 3.3 ast, 0.13 sack, 0.34 PD, 0.15 INT |  |
| LB | Patrick Queen | 5.8 | 2.9 solo, 3.7 ast, 0.15 sack, 0.32 PD, 0.08 INT |  |
| LB | T.J. Watt | 5.6 | 1.4 solo, 1.1 ast, 0.61 sack, 0.27 PD, 0.14 INT |  |
| DB | Jamel Dean | 6.3 | 2.7 solo, 1.4 ast, 0.00 sack, 1.47 PD, 0.21 INT |  |
| DB | Jaquan Brisker | 5.2 | 3.0 solo, 3.2 ast, 0.00 sack, 0.41 PD, 0.09 INT |  |
| DB | Jalen Ramsey | 4.6 | 3.6 solo, 2.6 ast, 0.30 sack, 0.29 PD, 0.00 INT | Questionable |

### IND @ JAX

Market: JAX -10.0, total 46.5. Sim: IND 18.2, JAX 28.4. JAX wins 78.2%, IND wins 21.8%. Median margin +10.4 for JAX.

| Team stat | IND | JAX |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 35 / 21 | 32 / 20 |
| Passing yards | 215 | 261 |
| Rush attempts / yards | 26 / 98 | 29 / 113 |
| Sacks taken | 2.3 | 1.9 |
| Interceptions thrown | 0.9 | 0.6 |
| Passing / rushing TDs | 1.0 / 0.9 | 1.7 / 1.4 |
| Field goals | 1.4 | 2.1 |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 14.1 | 215 pass yd, 1.0 TD, 0.9 INT; 2.3 rush, 9 yd |  |
| RB | Jonathan Taylor | 14.3 | 16.4 car, 59 yd, 0.62 TD; 2.3 rec, 22 yd, 0.05 TD |  |
| RB | Seth McGowan | 3.1 | 4.2 car, 17 yd, 0.07 TD; 0.5 rec, 4 yd, 0.01 TD |  |
| WR | Keenan Allen | 9.8 | 4.5 rec, 40 yd, 0.23 TD |  |
| WR | Josh Downs | 8.0 | 3.5 rec, 37 yd, 0.12 TD |  |
| WR | Laquon Treadwell | 4.1 | 1.8 rec, 20 yd, 0.04 TD |  |
| WR | Deion Burks | 2.2 | 0.9 rec, 10 yd, 0.02 TD |  |
| TE | Tyler Warren | 7.3 | 4.4 rec, 33 yd, 0.23 TD | Questionable |
| TE | Mo Alie-Cox | 3.0 | 1.0 rec, 9 yd, 0.19 TD |  |
| K | Spencer Shrader | 10.0 | 2.2 FG, 1.8 XP |  |
| DL | DeForest Buckner | 4.8 | 1.7 solo, 2.5 ast, 0.42 sack, 0.35 PD, 0.00 INT |  |
| DL | Adetomiwa Adebawore | 4.3 | 1.4 solo, 1.7 ast, 0.64 sack, 0.16 PD, 0.00 INT |  |
| LB | Akeem Davis-Gaither | 6.2 | 4.1 solo, 4.1 ast, 0.00 sack, 0.11 PD, 0.00 INT |  |
| LB | Jaylon Carlies | 2.3 | 1.0 solo, 1.3 ast, 0.00 sack, 0.18 PD, 0.17 INT |  |
| LB | Bryce Boettcher | 1.8 | 1.2 solo, 2.5 ast, 0.00 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | A.J. Haulcy | 4.5 | 2.9 solo, 2.6 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |
| DB | Justin Walley | 4.1 | 3.2 solo, 1.7 ast, 0.13 sack, 0.34 PD, 0.00 INT | Questionable |
| DB | Camryn Bynum | 4.1 | 2.6 solo, 1.2 ast, 0.00 sack, 0.31 PD, 0.19 INT |  |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 22.2 | 261 pass yd, 1.7 TD, 0.6 INT; 4.0 rush, 17 yd |  |
| RB | Bhayshul Tuten | 12.6 | 13.7 car, 52 yd, 0.56 TD; 1.6 rec, 16 yd, 0.19 TD |  |
| RB | Chris Rodriguez Jr. | 6.5 | 7.4 car, 31 yd, 0.49 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| RB | LeQuint Allen Jr. | 1.5 | 1.0 car, 4 yd, 0.03 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| WR | Parker Washington | 13.8 | 4.6 rec, 68 yd, 0.41 TD |  |
| WR | Jakobi Meyers | 8.0 | 4.1 rec, 49 yd, 0.26 TD | Questionable |
| WR | Brian Thomas Jr. | 5.4 | 2.0 rec, 25 yd, 0.16 TD |  |
| WR | Josh Cameron | 4.1 | 1.4 rec, 17 yd, 0.16 TD |  |
| TE | Brenton Strange | 10.5 | 4.4 rec, 47 yd, 0.24 TD |  |
| TE | Nate Boerkircher | 3.0 | 1.2 rec, 11 yd, 0.13 TD |  |
| K | Cam Little | 9.3 | 1.7 FG, 2.9 XP |  |
| DL | Josh Hines-Allen | 4.1 | 1.8 solo, 1.4 ast, 0.34 sack, 0.22 PD, 0.00 INT |  |
| DL | Travon Walker | 2.9 | 1.2 solo, 1.5 ast, 0.26 sack, 0.13 PD, 0.00 INT |  |
| LB | Foyesade Oluokun | 7.4 | 4.4 solo, 3.6 ast, 0.00 sack, 0.40 PD, 0.19 INT |  |
| LB | Ventrell Miller | 4.7 | 2.3 solo, 2.5 ast, 0.08 sack, 0.48 PD, 0.05 INT |  |
| LB | Branson Combs | 2.2 | 1.3 solo, 1.0 ast, 0.08 sack, 0.00 PD, 0.00 INT |  |
| DB | Travis Hunter | 5.4 | 2.4 solo, 1.5 ast, 0.00 sack, 1.07 PD, 0.40 INT |  |
| DB | Jarrian Jones | 5.1 | 3.0 solo, 0.9 ast, 0.00 sack, 0.93 PD, 0.21 INT |  |
| DB | Antonio Johnson | 4.2 | 3.1 solo, 1.4 ast, 0.10 sack, 0.46 PD, 0.21 INT | Questionable |

### KC @ DEN

Market: DEN +1.5, total 40.5. Sim: KC 21.0, DEN 19.5. DEN wins 45.2%, KC wins 54.8%. Median margin -1.6 for DEN.

| Team stat | KC | DEN |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 33 / 21 | 34 / 21 |
| Passing yards | 214 | 216 |
| Rush attempts / yards | 26 / 120 | 26 / 98 |
| Sacks taken | 2.7 | 2.0 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.3 / 0.9 | 1.3 / 0.8 |
| Field goals | 1.6 | 1.5 |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 16.6 | 214 pass yd, 1.3 TD, 0.7 INT; 2.3 rush, 10 yd |  |
| RB | Kenneth Walker III | 17.3 | 15.1 car, 76 yd, 0.60 TD; 2.9 rec, 19 yd, 0.25 TD |  |
| RB | Kareem Hunt | 4.3 | 4.7 car, 19 yd, 0.17 TD; 0.7 rec, 6 yd, 0.02 TD |  |
| RB | Emmett Johnson | 4.0 | 2.1 car, 9 yd, 0.04 TD; 1.4 rec, 13 yd, 0.04 TD |  |
| WR | Xavier Worthy | 7.7 | 3.4 rec, 32 yd, 0.17 TD |  |
| WR | Rashee Rice | 6.4 | 3.4 rec, 36 yd, 0.23 TD | Questionable |
| WR | Jalen Royals | 2.8 | 1.1 rec, 9 yd, 0.12 TD |  |
| WR | Andrew Armstrong | 2.5 | 1.2 rec, 11 yd, 0.04 TD |  |
| TE | Travis Kelce | 9.7 | 3.9 rec, 39 yd, 0.30 TD |  |
| TE | Noah Gray | 4.0 | 1.8 rec, 19 yd, 0.05 TD |  |
| K | Harrison Butker | 9.3 | 1.9 FG, 2.1 XP |  |
| DL | George Karlaftis | 3.8 | 1.3 solo, 1.9 ast, 0.18 sack, 0.63 PD, 0.10 INT |  |
| DL | Chris Jones | 3.1 | 1.0 solo, 1.1 ast, 0.36 sack, 0.27 PD, 0.00 INT |  |
| LB | Nick Bolton | 7.9 | 4.6 solo, 5.2 ast, 0.05 sack, 0.33 PD, 0.05 INT |  |
| LB | Drue Tranquill | 6.4 | 3.7 solo, 4.2 ast, 0.00 sack, 0.19 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.9 | 1.2 solo, 1.5 ast, 0.00 sack, 0.13 PD, 0.13 INT |  |
| DB | Nohl Williams | 5.5 | 2.7 solo, 1.8 ast, 0.13 sack, 1.01 PD, 0.15 INT |  |
| DB | Chamarri Conner | 5.4 | 3.2 solo, 1.9 ast, 0.25 sack, 0.25 PD, 0.07 INT |  |
| DB | Mansoor Delane | 5.3 | 3.0 solo, 2.0 ast, 0.00 sack, 0.95 PD, 0.13 INT |  |

**DEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bo Nix | 17.6 | 216 pass yd, 1.3 TD, 0.6 INT; 4.0 rush, 17 yd |  |
| RB | RJ Harvey | 11.1 | 5.8 car, 21 yd, 0.19 TD; 3.5 rec, 31 yd, 0.21 TD |  |
| RB | J.K. Dobbins | 7.9 | 10.6 car, 37 yd, 0.35 TD; 1.2 rec, 8 yd, 0.03 TD |  |
| RB | Jonah Coleman | 4.4 | 3.9 car, 17 yd, 0.12 TD; 1.0 rec, 9 yd, 0.02 TD |  |
| WR | Courtland Sutton | 8.2 | 3.2 rec, 34 yd, 0.26 TD |  |
| WR | Jaylen Waddle | 7.5 | 4.4 rec, 42 yd, 0.23 TD | Questionable |
| WR | Troy Franklin | 3.9 | 1.7 rec, 17 yd, 0.08 TD |  |
| WR | Marvin Mims Jr. | 2.8 | 1.7 rec, 16 yd, 0.05 TD | Questionable |
| TE | Evan Engram | 5.3 | 2.4 rec, 23 yd, 0.11 TD |  |
| TE | Nate Adkins | 2.2 | 0.6 rec, 6 yd, 0.18 TD |  |
| K | Wil Lutz | 9.0 | 1.9 FG, 2.0 XP |  |
| DL | Malcolm Roach | 3.7 | 1.5 solo, 1.4 ast, 0.37 sack, 0.39 PD, 0.00 INT |  |
| DL | Zach Allen | 2.8 | 1.1 solo, 1.8 ast, 0.45 sack, 0.27 PD, 0.00 INT | Questionable |
| LB | Alex Singleton | 8.9 | 5.4 solo, 5.7 ast, 0.15 sack, 0.20 PD, 0.00 INT |  |
| LB | Justin Strnad | 4.6 | 2.3 solo, 2.8 ast, 0.13 sack, 0.28 PD, 0.00 INT |  |
| LB | Nik Bonitto | 4.0 | 1.4 solo, 0.8 ast, 0.57 sack, 0.05 PD, 0.00 INT |  |
| DB | Ja'Quan McMillian | 6.6 | 3.0 solo, 0.8 ast, 0.32 sack, 1.11 PD, 0.23 INT |  |
| DB | Brandon Jones | 6.5 | 3.8 solo, 2.6 ast, 0.00 sack, 0.60 PD, 0.20 INT |  |
| DB | Riley Moss | 4.2 | 2.0 solo, 1.4 ast, 0.05 sack, 0.98 PD, 0.12 INT |  |

### LAC @ LA

Market: LA -6.5, total 45.0. Sim: LAC 19.4, LA 25.7. LA wins 68.0%, LAC wins 32.0%. Median margin +6.3 for LA.

| Team stat | LAC | LA |
|---|---|---|
| Plays | 64 | 64 |
| Pass attempts / completions | 35 / 21 | 34 / 22 |
| Passing yards | 217 | 247 |
| Rush attempts / yards | 26 / 114 | 28 / 127 |
| Sacks taken | 2.4 | 2.5 |
| Interceptions thrown | 0.9 | 0.9 |
| Passing / rushing TDs | 1.2 / 0.9 | 1.6 / 1.2 |
| Field goals | 1.5 | 1.9 |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.9 | 217 pass yd, 1.2 TD, 0.9 INT; 4.1 rush, 21 yd |  |
| RB | Omarion Hampton | 10.1 | 10.6 car, 42 yd, 0.44 TD; 1.9 rec, 12 yd, 0.06 TD |  |
| RB | Kimani Vidal | 6.5 | 5.3 car, 24 yd, 0.22 TD; 1.3 rec, 11 yd, 0.09 TD |  |
| RB | Keaton Mitchell | 6.4 | 4.8 car, 21 yd, 0.08 TD; 2.0 rec, 12 yd, 0.12 TD |  |
| WR | Quentin Johnston | 5.9 | 2.1 rec, 30 yd, 0.12 TD |  |
| WR | Tre Harris | 4.6 | 2.7 rec, 30 yd, 0.07 TD | Questionable |
| WR | Ladd McConkey | 4.3 | 2.2 rec, 26 yd, 0.17 TD | Questionable |
| WR | KeAndre Lambert-Smith | 3.9 | 1.8 rec, 15 yd, 0.10 TD |  |
| TE | Oronde Gadsden II | 5.0 | 2.2 rec, 20 yd, 0.14 TD |  |
| TE | Charlie Kolar | 4.3 | 2.2 rec, 19 yd, 0.05 TD |  |
| K | Cameron Dicker | 8.6 | 1.8 FG, 2.0 XP |  |
| DL | Justin Eboigbe | 2.9 | 1.4 solo, 1.3 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| DL | Teair Tart | 2.0 | 1.3 solo, 1.2 ast, 0.00 sack, 0.10 PD, 0.00 INT |  |
| LB | Tuli Tuipulotu | 6.0 | 2.0 solo, 1.9 ast, 0.45 sack, 0.37 PD, 0.12 INT |  |
| LB | Daiyan Henley | 5.4 | 2.6 solo, 3.1 ast, 0.06 sack, 0.22 PD, 0.05 INT |  |
| LB | Caleb Murphy | 4.7 | 2.1 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Cam Hart | 4.8 | 2.6 solo, 1.2 ast, 0.00 sack, 0.83 PD, 0.27 INT |  |
| DB | Tony Jefferson | 4.5 | 2.9 solo, 1.8 ast, 0.00 sack, 0.31 PD, 0.08 INT |  |
| DB | Elijah Molden | 3.9 | 2.4 solo, 2.3 ast, 0.00 sack, 0.07 PD, 0.07 INT |  |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 18.5 | 247 pass yd, 1.6 TD, 0.9 INT; 1.6 rush, 6 yd |  |
| RB | Kyren Williams | 17.2 | 14.4 car, 66 yd, 0.62 TD; 3.5 rec, 28 yd, 0.15 TD |  |
| RB | Blake Corum | 9.8 | 9.8 car, 46 yd, 0.42 TD; 1.1 rec, 11 yd, 0.10 TD |  |
| WR | Puka Nacua | 20.1 | 0.9 car, 4 yd, 0.07 TD; 7.8 rec, 85 yd, 0.53 TD |  |
| WR | Konata Mumpfield | 3.9 | 1.5 rec, 18 yd, 0.11 TD |  |
| WR | Xavier Smith | 1.7 | 0.7 rec, 9 yd, 0.02 TD |  |
| WR | Tutu Atwell | 1.4 | 0.6 rec, 7 yd, 0.02 TD |  |
| TE | Tyler Higbee | 8.6 | 3.6 rec, 38 yd, 0.21 TD |  |
| TE | Colby Parkinson | 5.2 | 2.9 rec, 26 yd, 0.27 TD | Questionable |
| K | Brandon McManus | 8.1 | 1.4 FG, 2.6 XP |  |
| DL | Braden Fiske | 2.3 | 1.1 solo, 0.9 ast, 0.25 sack, 0.00 PD, 0.00 INT |  |
| DL | Aaron Donald | 1.8 | 1.0 solo, 0.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Byron Young | 5.4 | 1.9 solo, 2.9 ast, 0.62 sack, 0.00 PD, 0.00 INT |  |
| LB | Omar Speights | 4.9 | 3.1 solo, 2.0 ast, 0.19 sack, 0.10 PD, 0.00 INT |  |
| LB | Nate Landman | 4.9 | 3.8 solo, 3.6 ast, 0.05 sack, 0.16 PD, 0.04 INT | Questionable |
| DB | Quentin Lake | 8.0 | 4.5 solo, 2.5 ast, 0.00 sack, 1.14 PD, 0.28 INT |  |
| DB | Jaylen Watson | 4.8 | 2.0 solo, 1.3 ast, 0.00 sack, 1.68 PD, 0.18 INT |  |
| DB | Kamren Kinchens | 4.7 | 3.0 solo, 2.3 ast, 0.05 sack, 0.32 PD, 0.00 INT |  |

### LV @ NYJ

Market: NYJ -1.5, total 45.5. Sim: LV 22.0, NYJ 23.5. NYJ wins 54.2%, LV wins 45.8%. Median margin +1.4 for NYJ.

| Team stat | LV | NYJ |
|---|---|---|
| Plays | 61 | 60 |
| Pass attempts / completions | 35 / 22 | 32 / 21 |
| Passing yards | 251 | 228 |
| Rush attempts / yards | 24 / 90 | 26 / 109 |
| Sacks taken | 2.4 | 2.5 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.5 / 0.9 | 1.6 / 1.0 |
| Field goals | 1.7 | 1.7 |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 18.6 | 251 pass yd, 1.5 TD, 0.6 INT; 1.8 rush, 6 yd |  |
| RB | Ashton Jeanty | 16.1 | 14.0 car, 47 yd, 0.47 TD; 3.9 rec, 35 yd, 0.25 TD |  |
| RB | Mike Washington Jr. | 4.5 | 5.4 car, 23 yd, 0.21 TD; 0.5 rec, 4 yd, 0.02 TD |  |
| RB | Dylan Laube | 1.6 | 0.6 car, 3 yd, 0.13 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| WR | Tre Tucker | 10.2 | 3.5 rec, 47 yd, 0.31 TD |  |
| WR | Cody White | 3.4 | 1.1 rec, 13 yd, 0.15 TD |  |
| WR | Jalen Nailor | 3.2 | 1.4 rec, 14 yd, 0.06 TD |  |
| WR | Tyler Lockett | 2.4 | 1.0 rec, 10 yd, 0.07 TD |  |
| TE | Brock Bowers | 9.0 | 4.7 rec, 54 yd, 0.34 TD | Questionable |
| TE | Michael Mayer | 7.5 | 3.4 rec, 34 yd, 0.13 TD |  |
| K | Matt Gay | 10.2 | 2.1 FG, 2.2 XP |  |
| DL | Maxx Crosby | 3.7 | 1.5 solo, 1.7 ast, 0.30 sack, 0.09 PD, 0.00 INT |  |
| DL | Malcolm Koonce | 2.9 | 0.9 solo, 0.6 ast, 0.44 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 9.3 | 4.7 solo, 5.2 ast, 0.15 sack, 0.33 PD, 0.19 INT |  |
| LB | Quay Walker | 4.7 | 3.1 solo, 4.0 ast, 0.30 sack, 0.00 PD, 0.00 INT | Questionable |
| LB | Tommy Eichenberg | 2.3 | 1.3 solo, 1.9 ast, 0.00 sack, 0.06 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 6.9 | 4.5 solo, 2.2 ast, 0.12 sack, 0.11 PD, 0.00 INT |  |
| DB | Hezekiah Masses | 4.7 | 2.4 solo, 1.3 ast, 0.00 sack, 0.68 PD, 0.32 INT |  |
| DB | Treydan Stukes | 4.2 | 2.6 solo, 2.2 ast, 0.00 sack, 0.29 PD, 0.10 INT |  |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Geno Smith | 18.2 | 228 pass yd, 1.6 TD, 0.6 INT; 2.3 rush, 9 yd |  |
| RB | Braelon Allen | 8.6 | 11.4 car, 52 yd, 0.45 TD; 2.0 rec, 13 yd, 0.07 TD | Questionable |
| RB | Breece Hall | 5.7 | 8.5 car, 33 yd, 0.31 TD; 1.2 rec, 12 yd, 0.04 TD | Questionable |
| RB | Isaiah Davis | 2.9 | 1.9 car, 8 yd, 0.08 TD; 0.7 rec, 8 yd, 0.02 TD |  |
| WR | Garrett Wilson | 10.1 | 4.1 rec, 43 yd, 0.30 TD |  |
| WR | Omar Cooper Jr. | 7.4 | 2.4 rec, 35 yd, 0.26 TD |  |
| WR | Adonai Mitchell | 4.8 | 1.9 rec, 21 yd, 0.14 TD |  |
| WR | Isaiah Williams | 3.7 | 1.5 rec, 15 yd, 0.10 TD |  |
| TE | Mason Taylor | 5.7 | 2.2 rec, 20 yd, 0.25 TD |  |
| TE | Kenyon Sadiq | 4.6 | 1.8 rec, 17 yd, 0.12 TD |  |
| K | Jason Sanders | 9.1 | 1.8 FG, 2.4 XP |  |
| DL | Jowon Briggs | 3.6 | 1.4 solo, 2.4 ast, 0.28 sack, 0.00 PD, 0.00 INT |  |
| DL | Will McDonald IV | 3.1 | 1.1 solo, 0.9 ast, 0.31 sack, 0.00 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.4 | 3.7 solo, 4.3 ast, 0.05 sack, 0.69 PD, 0.00 INT |  |
| LB | Demario Davis | 6.6 | 3.8 solo, 2.4 ast, 0.28 sack, 0.72 PD, 0.00 INT |  |
| LB | Nate Lynn | 5.6 | 2.0 solo, 1.0 ast, 1.02 sack, 0.00 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 8.3 | 4.6 solo, 4.1 ast, 0.00 sack, 0.44 PD, 0.21 INT |  |
| DB | Dane Belton | 7.2 | 4.2 solo, 4.0 ast, 0.16 sack, 0.46 PD, 0.00 INT |  |
| DB | Azareye'h Thomas | 3.7 | 2.2 solo, 2.0 ast, 0.00 sack, 0.58 PD, 0.00 INT |  |

### MIN @ DET

Market: DET -3.5, total 46.0. Sim: MIN 21.3, DET 24.7. DET wins 59.8%, MIN wins 40.2%. Median margin +3.4 for DET.

| Team stat | MIN | DET |
|---|---|---|
| Plays | 60 | 65 |
| Pass attempts / completions | 32 / 21 | 34 / 22 |
| Passing yards | 222 | 234 |
| Rush attempts / yards | 25 / 107 | 28 / 112 |
| Sacks taken | 2.4 | 3.5 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 1.5 / 0.8 | 1.6 / 1.1 |
| Field goals | 1.6 | 1.9 |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kyler Murray | 18.4 | 222 pass yd, 1.5 TD, 0.6 INT; 3.5 rush, 17 yd |  |
| RB | Aaron Jones | 9.0 | 11.7 car, 47 yd, 0.41 TD; 2.7 rec, 18 yd, 0.10 TD | Questionable |
| RB | Jordan Mason | 5.0 | 6.1 car, 28 yd, 0.24 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| RB | Demond Claiborne | 1.2 | 1.0 car, 4 yd, 0.02 TD; 0.4 rec, 3 yd, 0.00 TD |  |
| WR | Justin Jefferson | 13.6 | 5.1 rec, 57 yd, 0.47 TD |  |
| WR | Jordan Addison | 8.1 | 2.8 rec, 34 yd, 0.26 TD |  |
| WR | Jauan Jennings | 2.4 | 1.1 rec, 11 yd, 0.04 TD |  |
| WR | Tai Felton | 1.7 | 0.7 rec, 8 yd, 0.03 TD |  |
| TE | T.J. Hockenson | 10.5 | 4.4 rec, 39 yd, 0.39 TD |  |
| TE | Gavin Bartholomew | 4.4 | 2.1 rec, 19 yd, 0.07 TD |  |
| K | Will Reichard | 10.9 | 2.3 FG, 2.1 XP |  |
| DL | Jalen Redmond | 4.0 | 2.0 solo, 1.6 ast, 0.16 sack, 0.34 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 2.3 | 1.1 solo, 1.5 ast, 0.16 sack, 0.00 PD, 0.00 INT |  |
| LB | Blake Cashman | 11.0 | 5.2 solo, 5.6 ast, 0.67 sack, 0.78 PD, 0.00 INT |  |
| LB | Dallas Turner | 6.3 | 1.9 solo, 1.6 ast, 0.91 sack, 0.06 PD, 0.00 INT |  |
| LB | Andrew Van Ginkel | 5.9 | 1.7 solo, 1.8 ast, 0.62 sack, 0.41 PD, 0.15 INT |  |
| DB | Byron Murphy | 5.6 | 2.5 solo, 1.2 ast, 0.00 sack, 0.91 PD, 0.48 INT |  |
| DB | Josh Metellus | 5.3 | 3.2 solo, 3.0 ast, 0.06 sack, 0.42 PD, 0.00 INT |  |
| DB | James Pierre | 4.9 | 3.8 solo, 0.5 ast, 0.00 sack, 0.43 PD, 0.14 INT |  |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 18.6 | 234 pass yd, 1.6 TD, 0.6 INT; 1.9 rush, 7 yd |  |
| RB | Jahmyr Gibbs | 17.8 | 22.9 car, 92 yd, 0.96 TD; 4.3 rec, 32 yd, 0.25 TD | Questionable |
| RB | Sione Vaki | 1.7 | 2.1 car, 9 yd, 0.04 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| WR | Amon-Ra St. Brown | 11.2 | 6.3 rec, 63 yd, 0.41 TD | Questionable |
| WR | Jameson Williams | 10.3 | 3.6 rec, 46 yd, 0.36 TD |  |
| WR | Isaac TeSlaa | 4.1 | 1.5 rec, 19 yd, 0.12 TD |  |
| TE | Sam LaPorta | 9.0 | 3.6 rec, 37 yd, 0.28 TD |  |
| TE | Brock Wright | 1.4 | 0.7 rec, 5 yd, 0.02 TD |  |
| K | Jake Bates | 9.2 | 1.8 FG, 2.5 XP |  |
| DL | Aidan Hutchinson | 5.5 | 1.8 solo, 1.4 ast, 0.83 sack, 0.18 PD, 0.04 INT |  |
| DL | D.J. Wonnum | 4.4 | 1.1 solo, 0.8 ast, 0.85 sack, 0.11 PD, 0.00 INT |  |
| LB | Jack Campbell | 8.1 | 5.1 solo, 4.8 ast, 0.04 sack, 0.17 PD, 0.00 INT |  |
| LB | Derrick Barnes | 5.1 | 2.8 solo, 1.8 ast, 0.28 sack, 0.24 PD, 0.12 INT |  |
| LB | Malcolm Rodriguez | 1.9 | 1.2 solo, 0.9 ast, 0.07 sack, 0.00 PD, 0.00 INT |  |
| DB | Chuck Clark | 6.4 | 3.6 solo, 2.7 ast, 0.15 sack, 0.32 PD, 0.12 INT |  |
| DB | D.J. Reed | 5.4 | 3.9 solo, 1.5 ast, 0.00 sack, 0.57 PD, 0.04 INT |  |
| DB | Christian Izien | 5.2 | 3.5 solo, 1.7 ast, 0.22 sack, 0.19 PD, 0.00 INT |  |

### NE @ MIA

Market: MIA +7.0, total 44.0. Sim: NE 25.5, MIA 18.5. MIA wins 30.2%, NE wins 69.8%. Median margin -6.9 for MIA.

| Team stat | NE | MIA |
|---|---|---|
| Plays | 61 | 59 |
| Pass attempts / completions | 31 / 21 | 30 / 19 |
| Passing yards | 266 | 209 |
| Rush attempts / yards | 28 / 124 | 27 / 122 |
| Sacks taken | 2.1 | 2.2 |
| Interceptions thrown | 0.8 | 0.7 |
| Passing / rushing TDs | 1.6 / 1.2 | 1.0 / 1.0 |
| Field goals | 1.9 | 1.4 |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 22.3 | 266 pass yd, 1.6 TD, 0.8 INT; 4.5 rush, 22 yd |  |
| RB | Rhamondre Stevenson | 14.3 | 8.4 car, 37 yd, 0.41 TD; 3.2 rec, 37 yd, 0.22 TD |  |
| RB | TreVeyon Henderson | 8.2 | 8.0 car, 35 yd, 0.34 TD; 1.3 rec, 12 yd, 0.06 TD |  |
| RB | Corey Kiner | 3.0 | 4.4 car, 20 yd, 0.10 TD; 0.2 rec, 3 yd, 0.00 TD |  |
| WR | DeMario Douglas | 9.2 | 3.5 rec, 40 yd, 0.29 TD |  |
| WR | A.J. Brown | 5.5 | 2.9 rec, 34 yd, 0.16 TD | Questionable |
| WR | Efton Chism III | 4.6 | 1.7 rec, 21 yd, 0.13 TD |  |
| WR | Kyle Williams | 4.1 | 1.2 rec, 21 yd, 0.14 TD |  |
| TE | Hunter Henry | 12.1 | 4.7 rec, 55 yd, 0.32 TD |  |
| TE | Eli Raridon | 6.7 | 2.4 rec, 31 yd, 0.22 TD |  |
| K | Andy Borregales | 8.4 | 1.6 FG, 2.6 XP |  |
| DL | Christian Barmore | 2.6 | 0.9 solo, 0.3 ast, 0.46 sack, 0.00 PD, 0.00 INT |  |
| DL | Milton Williams | 2.1 | 1.2 solo, 0.9 ast, 0.15 sack, 0.00 PD, 0.00 INT |  |
| LB | Christian Elliss | 5.9 | 3.6 solo, 3.4 ast, 0.07 sack, 0.19 PD, 0.00 INT |  |
| LB | Elijah Ponder | 4.7 | 1.6 solo, 1.0 ast, 0.63 sack, 0.00 PD, 0.00 INT |  |
| LB | Robert Spillane | 3.8 | 2.1 solo, 3.0 ast, 0.00 sack, 0.03 PD, 0.00 INT |  |
| DB | Marcus Jones | 5.2 | 2.6 solo, 1.7 ast, 0.19 sack, 0.50 PD, 0.11 INT |  |
| DB | Craig Woodson | 4.4 | 2.5 solo, 2.0 ast, 0.00 sack, 0.29 PD, 0.10 INT |  |
| DB | Kevin Byard | 3.8 | 2.3 solo, 2.4 ast, 0.00 sack, 0.29 PD, 0.00 INT |  |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Malik Willis | 18.4 | 209 pass yd, 1.0 TD, 0.7 INT; 6.3 rush, 34 yd |  |
| RB | Ollie Gordon II | 9.0 | 11.1 car, 50 yd, 0.43 TD; 0.9 rec, 6 yd, 0.02 TD |  |
| RB | Jaylen Wright | 4.1 | 6.1 car, 24 yd, 0.15 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| RB | DJ Herman | 1.1 | 0.0 car, 0 yd, 0.00 TD; 0.5 rec, 6 yd, 0.01 TD |  |
| WR | Caleb Douglas | 7.8 | 2.2 rec, 33 yd, 0.38 TD |  |
| WR | Malik Washington | 7.3 | 1.3 car, 6 yd, 0.05 TD; 4.2 rec, 38 yd, 0.14 TD | Questionable |
| WR | Chris Bell | 4.5 | 2.0 rec, 22 yd, 0.06 TD |  |
| WR | Kevin Coleman Jr. | 4.4 | 1.7 rec, 15 yd, 0.20 TD |  |
| TE | Greg Dulcich | 6.3 | 3.7 rec, 40 yd, 0.11 TD | Questionable |
| TE | Will Kacmarek | 1.2 | 0.8 rec, 7 yd, 0.02 TD | Questionable |
| K | Riley Patterson | 7.6 | 1.5 FG, 1.9 XP |  |
| DL | Zach Sieler | 3.5 | 1.6 solo, 1.2 ast, 0.42 sack, 0.00 PD, 0.00 INT |  |
| DL | Zeek Biggers | 1.7 | 0.6 solo, 1.6 ast, 0.06 sack, 0.13 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 7.3 | 4.0 solo, 5.6 ast, 0.00 sack, 0.14 PD, 0.14 INT |  |
| LB | Jordyn Brooks | 7.1 | 4.0 solo, 5.3 ast, 0.04 sack, 0.25 PD, 0.00 INT |  |
| LB | Joshua Uche | 3.7 | 1.6 solo, 2.4 ast, 0.16 sack, 0.00 PD, 0.00 INT |  |
| DB | Chris Johnson | 4.9 | 2.9 solo, 2.6 ast, 0.00 sack, 0.22 PD, 0.00 INT |  |
| DB | Michael Taaffe | 4.1 | 2.4 solo, 2.8 ast, 0.00 sack, 0.31 PD, 0.31 INT | Questionable |
| DB | Dante Trader Jr. | 3.1 | 2.1 solo, 2.8 ast, 0.00 sack, 0.28 PD, 0.07 INT | Questionable |

### PHI @ WAS

Market: WAS -5.5, total 40.0. Sim: PHI 17.2, WAS 22.7. WAS wins 66.4%, PHI wins 33.6%. Median margin +5.5 for WAS.

| Team stat | PHI | WAS |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 33 / 20 | 31 / 19 |
| Passing yards | 209 | 208 |
| Rush attempts / yards | 27 / 116 | 28 / 124 |
| Sacks taken | 2.2 | 2.1 |
| Interceptions thrown | 0.6 | 0.6 |
| Passing / rushing TDs | 0.9 / 1.0 | 1.3 / 1.2 |
| Field goals | 1.3 | 1.7 |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tanner McKee | 13.2 | 209 pass yd, 0.9 TD, 0.6 INT; 1.7 rush, 7 yd |  |
| RB | Saquon Barkley | 10.9 | 18.2 car, 81 yd, 0.80 TD; 1.0 rec, 7 yd, 0.02 TD | Questionable |
| RB | Elijah Mitchell | 7.4 | 5.6 car, 23 yd, 0.11 TD; 2.2 rec, 20 yd, 0.05 TD |  |
| WR | DeVonta Smith | 6.6 | 3.8 rec, 39 yd, 0.17 TD | Questionable |
| WR | Makai Lemon | 6.5 | 3.2 rec, 26 yd, 0.11 TD |  |
| WR | Dontayvion Wicks | 4.4 | 2.5 rec, 29 yd, 0.09 TD | Questionable |
| WR | Darius Cooper | 3.6 | 1.3 rec, 16 yd, 0.13 TD |  |
| TE | Dallas Goedert | 7.1 | 3.3 rec, 30 yd, 0.15 TD |  |
| TE | Eli Stowers | 1.1 | 0.5 rec, 5 yd, 0.01 TD |  |
| K | Jake Elliott | 6.1 | 1.2 FG, 1.7 XP |  |
| DL | Jalen Carter | 3.9 | 1.0 solo, 1.3 ast, 0.39 sack, 0.37 PD, 0.00 INT |  |
| DL | Jordan Davis | 3.1 | 1.2 solo, 2.8 ast, 0.11 sack, 0.12 PD, 0.00 INT |  |
| LB | Zack Baun | 5.9 | 3.0 solo, 4.2 ast, 0.02 sack, 0.57 PD, 0.04 INT |  |
| LB | Jeremiah Trotter Jr. | 4.3 | 3.0 solo, 1.9 ast, 0.07 sack, 0.11 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 3.9 | 3.2 solo, 2.7 ast, 0.06 sack, 0.06 PD, 0.00 INT | Questionable |
| DB | Cooper DeJean | 6.1 | 3.7 solo, 2.4 ast, 0.00 sack, 0.76 PD, 0.14 INT |  |
| DB | Quinyon Mitchell | 5.1 | 3.2 solo, 1.1 ast, 0.00 sack, 1.05 PD, 0.11 INT |  |
| DB | Riq Woolen | 4.6 | 2.8 solo, 1.1 ast, 0.00 sack, 0.94 PD, 0.00 INT |  |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Marcus Mariota | 16.5 | 208 pass yd, 1.3 TD, 0.6 INT; 3.0 rush, 14 yd |  |
| RB | Rachaad White | 9.3 | 7.8 car, 32 yd, 0.18 TD; 2.2 rec, 17 yd, 0.20 TD |  |
| RB | Austin Ekeler | 4.4 | 3.6 car, 15 yd, 0.08 TD; 1.2 rec, 11 yd, 0.04 TD |  |
| RB | Jeremy McNichols | 3.1 | 3.0 car, 12 yd, 0.07 TD; 0.8 rec, 6 yd, 0.03 TD |  |
| WR | Stefon Diggs | 7.6 | 4.3 rec, 37 yd, 0.36 TD | Questionable |
| WR | Antonio Williams | 6.7 | 2.9 rec, 31 yd, 0.14 TD |  |
| WR | Treylon Burks | 4.2 | 2.0 rec, 25 yd, 0.20 TD | Questionable |
| WR | Dyami Brown | 3.4 | 1.5 rec, 16 yd, 0.05 TD |  |
| TE | Chig Okonkwo | 7.1 | 3.3 rec, 33 yd, 0.10 TD |  |
| TE | Ben Sinnott | 1.8 | 0.8 rec, 8 yd, 0.04 TD |  |
| K | Drew Stevens | 8.6 | 1.7 FG, 2.3 XP |  |
| DL | Daron Payne | 3.0 | 1.3 solo, 1.3 ast, 0.25 sack, 0.00 PD, 0.00 INT |  |
| DL | Tim Settle | 2.3 | 0.5 solo, 1.0 ast, 0.10 sack, 0.17 PD, 0.00 INT |  |
| LB | Sonny Styles | 7.6 | 3.6 solo, 4.5 ast, 0.12 sack, 0.71 PD, 0.14 INT |  |
| LB | Frankie Luvu | 4.9 | 2.3 solo, 3.0 ast, 0.12 sack, 0.33 PD, 0.00 INT |  |
| LB | Bobby Wagner | 4.7 | 2.5 solo, 2.6 ast, 0.19 sack, 0.19 PD, 0.05 INT |  |
| DB | Amik Robertson | 7.2 | 4.7 solo, 2.1 ast, 0.00 sack, 1.21 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 5.7 | 3.7 solo, 2.4 ast, 0.00 sack, 0.61 PD, 0.06 INT |  |
| DB | Rasul Douglas | 5.4 | 3.5 solo, 1.1 ast, 0.00 sack, 0.83 PD, 0.17 INT |  |

### TEN @ CIN

Market: CIN -10.5, total 46.5. Sim: TEN 18.1, CIN 28.6. CIN wins 78.3%, TEN wins 21.7%. Median margin +10.3 for CIN.

| Team stat | TEN | CIN |
|---|---|---|
| Plays | 60 | 63 |
| Pass attempts / completions | 35 / 22 | 35 / 24 |
| Passing yards | 217 | 274 |
| Rush attempts / yards | 22 / 101 | 26 / 101 |
| Sacks taken | 3.1 | 2.6 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.3 / 0.7 | 1.9 / 1.2 |
| Field goals | 1.3 | 2.1 |

**TEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Cam Ward | 16.3 | 217 pass yd, 1.3 TD, 0.7 INT; 2.0 rush, 9 yd |  |
| RB | Tony Pollard | 11.4 | 13.6 car, 62 yd, 0.45 TD; 1.5 rec, 10 yd, 0.04 TD |  |
| RB | Tyjae Spears | 4.5 | 2.8 car, 12 yd, 0.07 TD; 2.5 rec, 15 yd, 0.06 TD | Questionable |
| RB | Michael Carter | 2.4 | 2.0 car, 9 yd, 0.04 TD; 0.6 rec, 6 yd, 0.02 TD |  |
| WR | Wan'Dale Robinson | 9.1 | 4.0 rec, 29 yd, 0.36 TD |  |
| WR | Carnell Tate | 8.9 | 4.8 rec, 53 yd, 0.31 TD | Questionable |
| WR | Elic Ayomanor | 5.2 | 1.8 rec, 24 yd, 0.17 TD |  |
| WR | Chimere Dike | 3.6 | 1.5 rec, 14 yd, 0.12 TD |  |
| TE | Gunnar Helm | 3.8 | 1.9 rec, 15 yd, 0.08 TD |  |
| TE | Daniel Bellinger | 1.9 | 0.9 rec, 8 yd, 0.03 TD |  |
| K | Joey Slye | 7.7 | 1.6 FG, 1.8 XP |  |
| DL | Jeffery Simmons | 7.2 | 2.7 solo, 2.5 ast, 0.69 sack, 0.51 PD, 0.00 INT |  |
| DL | Jermaine Johnson II | 3.5 | 1.3 solo, 1.3 ast, 0.51 sack, 0.00 PD, 0.00 INT |  |
| LB | Anthony Hill Jr. | 7.5 | 3.8 solo, 5.9 ast, 0.00 sack, 0.38 PD, 0.00 INT |  |
| LB | Cedric Gray | 5.3 | 3.5 solo, 3.2 ast, 0.06 sack, 0.00 PD, 0.00 INT |  |
| LB | Cody Barton | 3.1 | 1.6 solo, 2.5 ast, 0.00 sack, 0.24 PD, 0.00 INT |  |
| DB | Amani Hooker | 6.1 | 3.8 solo, 2.4 ast, 0.00 sack, 0.38 PD, 0.24 INT |  |
| DB | Kevin Winston Jr. | 5.7 | 3.8 solo, 2.8 ast, 0.05 sack, 0.09 PD, 0.00 INT |  |
| DB | Cordale Flott | 4.5 | 2.3 solo, 1.1 ast, 0.00 sack, 0.43 PD, 0.43 INT |  |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 23.1 | 274 pass yd, 1.9 TD, 0.6 INT; 2.6 rush, 11 yd |  |
| RB | Chase Brown | 17.3 | 14.3 car, 54 yd, 0.58 TD; 4.3 rec, 29 yd, 0.23 TD |  |
| RB | Samaje Perine | 7.5 | 6.5 car, 26 yd, 0.37 TD; 1.2 rec, 10 yd, 0.10 TD |  |
| RB | Tahj Brooks | 0.8 | 1.1 car, 5 yd, 0.03 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Tee Higgins | 14.9 | 5.1 rec, 75 yd, 0.39 TD |  |
| WR | Ja'Marr Chase | 11.4 | 5.8 rec, 64 yd, 0.50 TD | Questionable |
| WR | Dohnte Meyers | 5.1 | 2.2 rec, 23 yd, 0.10 TD |  |
| WR | Mitchell Tinsley | 3.3 | 1.2 rec, 15 yd, 0.09 TD |  |
| TE | Mike Gesicki | 6.8 | 2.2 rec, 26 yd, 0.34 TD |  |
| TE | Drew Sample | 3.2 | 1.3 rec, 12 yd, 0.11 TD |  |
| K | Evan McPherson | 8.5 | 1.5 FG, 2.9 XP |  |
| DL | Boye Mafe | 5.2 | 1.4 solo, 1.0 ast, 0.87 sack, 0.20 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 4.5 | 1.5 solo, 1.2 ast, 0.75 sack, 0.23 PD, 0.00 INT |  |
| LB | Demetrius Knight Jr. | 6.5 | 3.0 solo, 3.8 ast, 0.17 sack, 0.29 PD, 0.19 INT |  |
| LB | Barrett Carter | 6.5 | 3.0 solo, 4.2 ast, 0.17 sack, 0.54 PD, 0.05 INT |  |
| LB | Jack Kiser | 2.4 | 1.9 solo, 1.0 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Bryan Cook | 5.1 | 3.4 solo, 1.6 ast, 0.13 sack, 0.00 PD, 0.00 INT |  |
| DB | Jordan Battle | 5.1 | 3.7 solo, 2.2 ast, 0.00 sack, 0.54 PD, 0.41 INT | Questionable |
| DB | Daxton Hill | 4.8 | 3.0 solo, 1.3 ast, 0.00 sack, 0.90 PD, 0.00 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: CAR: Chandler Zavala, CAR: Xavier Legette, CAR: Jaelan Phillips, CAR: Ja'Seem Reed, CAR: Damien Lewis, CAR: Jonathon Brooks, CAR: Mike Jackson, CAR: Nic Scourton, CAR: Cam Jackson, CAR: Thomas Incoom, CAR: Jimmy Horn Jr., CAR: Robert Rochell, CAR: Taylor Moton, CAR: Krys Barnes, CAR: LaBryan Ray, CAR: Maema Njongmeta, CAR: Jaycee Horn, CAR: Ikem Ekwonu, CAR: Corey Thornton, GB: Jonathan Ford, GB: Luke Musgrave, GB: Travis Glover, GB: Sean Rhyan, GB: Micah Parsons, GB: Edgerrin Cooper, GB: Shemar Bartholomew, GB: Chris Brooks, GB: Jacob Monk, GB: Drake Dabney, GB: Zaire Franklin, GB: Javon Hargrave, GB: Collin Oliver, GB: Arron Mosby, GB: Johnathan Baldwin, GB: Warren Brinson, GB: John FitzPatrick, GB: Skyy Moore, GB: Jayden Reed, GB: Nate Hobbs, GB: Zach Bako-Bewele, BAL: Jovaughn Gwyn, BAL: Jacob Hummel, BAL: Carl Lawson, BAL: Chris Moore, BAL: T.J. Tampa, BAL: Durham Smythe, BAL: Carl Jones, BAL: Tavius Robinson, BAL: Amani Oruwariye, BUF: Anthony Kendall, BUF: Tre'Davious White, BUF: Shaq Thompson, BUF: Mecole Hardman, BUF: Jordan Hancock, BUF: Keonta Jenkins, BUF: Trent Sherfield, BUF: Phidarian Mathis, BUF: C.J. Gardner-Johnson, BUF: Frank Gore Jr., BUF: Kani Walker, BUF: Tyrell Shavers, BUF: Andre Jones Jr., TEN: Jerrick Reed II, TEN: Darrell Baker Jr., TEN: Isaiah Oliver, TEN: Erick Hallett, TEN: Kaiir Elam, TEN: Kendell Brooks, TEN: Kalel Mullings, TEN: Xavier Restrepo, TEN: Mohamoud Diabate, TEN: Joe Bachie, TEN: Jaylen Harrell, TEN: Dorian Mausi, CIN: Jalen Davis, CIN: Erick All, CIN: Howard Cross III, CIN: Kyle Dugger, CIN: Kendall Milton, CIN: Andrei Iosivas, CIN: Jake Browning, CIN: Bralyn Lux, CIN: Tanner Hudson, CIN: Isaiah Foskey, CIN: Geno Stone, CIN: Swayze Bozeman, CIN: Ke'Shawn Williams, ARI: Hunter Long, ARI: Isaiah Adams, ARI: Art Green, ARI: Paris Johnson Jr., ARI: Wydett Williams Jr., ARI: Zachary Carter, ARI: Elijah Jones, ARI: BJ Ojulari, ARI: Jared Harrison-Hunte, ARI: Kedon Slovis, ARI: Josiah Deguara, ARI: Will Johnson, ARI: Jalen Brooks, DAL: Trikweze Bridges, DAL: Emari Demercado, DAL: Curtis Robinson, DAL: Jonathan Bullard, DAL: Malik Davis, DAL: Hakeem Adeniji, DAL: Marist Liufau, DAL: Jalen Thompson, DAL: Reddy Steward, DAL: P.J. Locke, MIN: Tavierre Thomas, MIN: Josh Oliver, MIN: Taki Taimani, MIN: Jeshaun Jones, MIN: C.J. Ham, MIN: Ty Chandler, MIN: Tyler Batty, MIN: Donovan Jackson, MIN: DeeJay Dallas, DET: Kingsley Eguakun, DET: Avonte Maddox, DET: Devin White, DET: Thomas Harper, DET: Ben Bartch, DET: Terrion Arnold, DET: Nick Whiteside, DET: Tom Kennedy, IND: Alec Pierce, IND: Johnathan Edwards, IND: Eric Johnson, IND: Arden Key, IND: Nick Westbrook-Ikhine, IND: Cam Taylor-Britt, IND: Danny Pinter, IND: Cameron Mitchell, IND: Germaine Pratt, JAX: Caleb Ransaw, JAX: Emmanuel Ogbah, JAX: BJ Green II, JAX: Cam'Ron Silmon-Craig, JAX: Austin Johnson, JAX: Nick Mullens, JAX: Anton Harrison, JAX: Austin Trammell, JAX: Patrick Mekari, LV: Tim Keenan III, LV: Darnay Holmes, LV: Chigozie Anusiem, LV: Jon Rhattigan, LV: Greedy Vance, LV: Carter Runyon, LV: Jonah Laulu, LV: Elandon Roberts, LV: Deven Thompkins, LV: Jack Bech, LV: Jamal Adams, LV: Will Putnam, LV: Shedrick Jackson, LV: Jacob Bobenmoyer, NYJ: Keidron Smith, NYJ: Samuel Womack, NYJ: Payton Page, NYJ: Brady Cook, NYJ: Micheal Clemons, NYJ: Dean Clark, NYJ: Jordan Clark, NYJ: Jamaal Pritchett, NYJ: David Onyemata, NYJ: Sterling Shepard, NYJ: Ja'Sir Taylor, NYJ: Troy Reeder, NYJ: Kingsley Jonathan, NYJ: Braiden McGregor, NYJ: Eric Watts, NYJ: Francisco Mauigoa, NYJ: Arian Smith, NYJ: Tre Brown, NYJ: Marcelino McCrary-Ball, CLE: Nathaniel Watson, CLE: Carsen Ryan, CLE: Teven Jenkins, CLE: Raheim Sanders, CLE: Ethan Pocic, CLE: Gage Larvadain, CLE: KT Leveston, CLE: Myles Garrett, CLE: Alex Wright, CLE: Jerome Ford, CLE: Brenden Bates, CLE: Sam Kamara, PIT: Darius Slay, PIT: Michael Pittman, PIT: Derrick Harmon, PIT: Brandon Smith, PIT: Rayshawn Jenkins, PIT: Calvin Austin III, PIT: Sebastian Castro, PIT: Sebastian Joseph-Day, PIT: Scott Miller, PIT: Logan Lee, PIT: Adam Thielen, PIT: Roman Wilson, PIT: Esezi Otomewo, ATL: Jammie Robinson, ATL: Khalil Herbert, ATL: Dylan Drummond, ATL: Jack Nelson, ATL: Brian Asamoah II, ATL: Michael Jerrell, ATL: Yasir Abdullah, ATL: Ronnie Harrison, ATL: James Pearce Jr., ATL: Natrone Brooks, ATL: Jalon Walker, ATL: JD Bertrand, TB: Josh Williams, TB: Josh Hayes, TB: Christian Rozeboom, TB: Markees Watts, TB: Jalen McMillan, TB: Mike Jordan, TB: Teddy Bridgewater, TB: Owen Wright, LAC: Bobby Hart, LAC: Alec Ingold, LAC: Amar Johnson, LAC: Da'Shawn Hand, LAC: Patrick Herbert, LAC: Isas Waxter, LAC: David Njoku, LAC: Jaret Patterson, LAC: Trey Pipkins, LAC: Trevor Penning, LAC: Trey Lance, LAC: Daniel Brunskill, LAC: Austin Deculus, LAC: Denzel Perryman, LAC: Marquez Valdes-Scantling, LAC: Rashawn Slater, LA: Blake Grupe, LA: Kobie Turner, LA: Ronnie Rivers, LA: Justin Dedich, LA: Tanner Ingle, LA: Derion Kendrick, LA: Davante Adams, LA: Terrance Ferguson, LA: Darious Williams, LA: Poona Ford, LA: Ahkello Witherspoon, KC: Esa Pole, KC: Ethan Downs, KC: Justin Watson, KC: Marcus Harris, KC: Josh Simmons, KC: Tyquan Thornton, KC: Brashard Smith, KC: Zacch Pickens, KC: Shane Buechele, KC: Cole Christiansen, KC: Isiah Pacheco, DEN: Michael Bandy, DEN: Frank Crum, DEN: Sean Fresch, DEN: Taylor Rapp, DEN: Tyler Badie, DEN: Jonah Elliss, DEN: Pat Bryant, DEN: Kolbe Katsis, NE: Jeremiah Pharms Jr., NE: Bradyn Swinson, NE: Lan Larison, NE: Quintayvious Hutchins, NE: Eric Gregory, NE: Mack Hollins, NE: Dell Pettus, NE: Alijah Vera-Tucker, NE: Reggie Gilliam, NE: Bryce Baringer, NE: Jose Ramirez, NE: Harold Landry III, NE: Marte Mapu, NE: Jack Westover, NE: Mike Onwenu, NE: Romeo Doubs, NE: K.J. Britt, MIA: Quinton Bell, MIA: Liam Anderson, MIA: Keith Cooper Jr., MIA: Ethan Bonner, MIA: Zane Gonzalez, MIA: Julian Hill, MIA: De'Von Achane, MIA: Ryan Miller, PHI: Will Shipley, PHI: Cole Wisniewski, PHI: Zach Ertz, PHI: Brandon Johnson, PHI: Dameon Pierce, PHI: Xavier Gipson, PHI: Jalen Hurts, PHI: Jakorian Bennett, PHI: Keyshawn James-Newby, PHI: E.J. Jenkins, PHI: Andre' Sam, PHI: Tank Bigsby, WAS: Terry McLaurin, WAS: Nick Bellore, WAS: Ricky Barber, WAS: Josh Johnson, WAS: Austin Keys, WAS: Laremy Tunsil, WAS: Tyler Biadasz, WAS: Leo Chenal, WAS: Jer'Zhan Newton, WAS: T.J. Maguranyanga, WAS: Jaylin Lane, WAS: Jacory Croskey-Merritt, WAS: Ale Kaho, WAS: Javontae Jean-Baptiste, WAS: Jalyn Holmes, WAS: Craig Reynolds, WAS: Jake Moody, CHI: Braxton Jones, CHI: Kaden Davis, CHI: Beau Gardner, CHI: Nikola Kalinic, CHI: Buddy Johnson, CHI: Cole Kmet, CHI: Dayo Odeyingbo, CHI: Brittain Brown, CHI: Nick McCloud, CHI: Joe Tryon-Shoyinka, CHI: Ruben Hyppolite II, SEA: Robbie Ouzts, SEA: AJ Finley, SEA: Elijah Arroyo, SEA: Trevon Diggs, SEA: Jake Bobo, SEA: Jimmy Ciarlo, SEA: Coby Bryant, SEA: Julian Neal, SEA: Jadarian Price, SEA: Montorie Foster Jr.

## 4. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 22.7 | 9.3 to 37.6 |
| QB | Joe Burrow | CIN | 21.1 | 8.4 to 34.6 |
| QB | Drake Maye | NE | 20.9 | 8.3 to 34.9 |
| QB | Trevor Lawrence | JAX | 20.5 | 8.1 to 33.9 |
| QB | Jacoby Brissett | ARI | 20.3 | 7.9 to 33.7 |
| QB | Dak Prescott | DAL | 20.0 | 7.6 to 33.3 |
| RB | Bijan Robinson | ATL | 20.4 | 7.4 to 35.1 |
| RB | Jaylen Warren | PIT | 19.5 | 6.5 to 34.2 |
| RB | Jahmyr Gibbs | DET | 18.8 | 0.0 to 39.5 |
| RB | Kenneth Walker III | KC | 18.0 | 5.8 to 32.0 |
| RB | Kyren Williams | LA | 17.8 | 5.9 to 31.6 |
| RB | Chase Brown | CIN | 17.6 | 6.0 to 30.9 |
| RB | Derrick Henry | BAL | 17.1 | 4.3 to 31.6 |
| RB | James Cook | BUF | 16.5 | 4.7 to 30.3 |
| RB | Ashton Jeanty | LV | 16.4 | 5.0 to 29.7 |
| RB | Javonte Williams | DAL | 15.9 | 4.1 to 30.0 |
| WR | Jaxon Smith-Njigba | SEA | 23.3 | 7.9 to 40.1 |
| WR | Puka Nacua | LA | 21.2 | 7.2 to 37.2 |
| WR | CeeDee Lamb | DAL | 17.7 | 4.9 to 32.8 |
| WR | Zay Flowers | BAL | 17.7 | 5.2 to 32.3 |
| WR | Tee Higgins | CIN | 15.7 | 3.6 to 30.3 |
| WR | Parker Washington | JAX | 14.5 | 2.9 to 28.9 |
| WR | Drake London | ATL | 14.3 | 3.5 to 27.6 |
| WR | Michael Wilson | ARI | 14.2 | 3.4 to 27.5 |
| WR | Tetairoa McMillan | CAR | 14.1 | 3.4 to 27.4 |
| WR | Justin Jefferson | MIN | 14.0 | 3.5 to 26.7 |
| WR | Luther Burden III | CHI | 13.5 | 3.4 to 26.3 |
| WR | Christian Watson | GB | 12.3 | 1.9 to 24.8 |
| TE | Trey McBride | ARI | 18.6 | 6.4 to 33.4 |
| TE | Hunter Henry | NE | 12.4 | 2.5 to 24.4 |
| TE | Colston Loveland | CHI | 11.4 | 2.6 to 21.9 |
| TE | Brenton Strange | JAX | 10.7 | 2.0 to 21.6 |
| TE | T.J. Hockenson | MIN | 10.7 | 1.8 to 21.2 |
| TE | Kyle Pitts | ATL | 9.9 | 1.5 to 20.0 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Josh Allen | BUF | 21.9 | 9.3 to 36.3 |
| QB | Joe Burrow | CIN | 19.9 | 8.6 to 32.3 |
| QB | Drake Maye | NE | 19.9 | 8.3 to 32.9 |
| QB | Trevor Lawrence | JAX | 19.5 | 8.2 to 31.9 |
| QB | Jacoby Brissett | ARI | 19.2 | 8.1 to 31.6 |
| QB | Dak Prescott | DAL | 19.0 | 7.8 to 31.1 |
| RB | Bijan Robinson | ATL | 17.6 | 6.4 to 30.4 |
| RB | Jaylen Warren | PIT | 17.0 | 5.6 to 29.8 |
| RB | Jahmyr Gibbs | DET | 16.2 | 0.0 to 34.4 |
| RB | Kenneth Walker III | KC | 15.8 | 4.9 to 28.4 |
| RB | Derrick Henry | BAL | 15.6 | 4.0 to 29.0 |
| RB | Kyren Williams | LA | 15.5 | 4.9 to 27.8 |
| RB | Chase Brown | CIN | 15.1 | 4.6 to 27.2 |
| RB | James Cook | BUF | 15.0 | 4.3 to 27.3 |
| RB | Javonte Williams | DAL | 14.5 | 3.6 to 27.5 |
| RB | Ashton Jeanty | LV | 14.2 | 3.8 to 26.4 |
| WR | Jaxon Smith-Njigba | SEA | 18.0 | 5.8 to 31.6 |
| WR | Puka Nacua | LA | 16.2 | 5.1 to 28.9 |
| WR | CeeDee Lamb | DAL | 14.0 | 3.3 to 26.1 |
| WR | Zay Flowers | BAL | 13.8 | 3.6 to 25.4 |
| WR | Tee Higgins | CIN | 12.3 | 2.6 to 23.7 |
| WR | Parker Washington | JAX | 11.6 | 1.9 to 22.7 |
| WR | Justin Jefferson | MIN | 11.1 | 2.1 to 21.6 |
| WR | Michael Wilson | ARI | 11.1 | 2.3 to 21.3 |
| WR | Drake London | ATL | 11.0 | 2.4 to 21.1 |
| WR | Tetairoa McMillan | CAR | 10.9 | 2.2 to 20.9 |
| WR | Luther Burden III | CHI | 10.5 | 2.3 to 20.3 |
| WR | Christian Watson | GB | 10.0 | 1.2 to 20.3 |
| TE | Trey McBride | ARI | 13.9 | 4.0 to 25.4 |
| TE | Hunter Henry | NE | 9.7 | 1.6 to 19.3 |
| TE | Colston Loveland | CHI | 8.8 | 1.4 to 17.8 |
| TE | T.J. Hockenson | MIN | 8.4 | 0.9 to 17.6 |
| TE | Brenton Strange | JAX | 8.3 | 1.2 to 16.8 |
| TE | Kyle Pitts | ATL | 7.8 | 0.7 to 16.6 |
| K | Will Reichard | MIN | 10.1 | 1.0 to 22.4 |
| K | Tyler Bass | BUF | 9.7 | 2.0 to 20.0 |
| K | Matt Gay | LV | 9.5 | 1.0 to 21.0 |
| K | Jason Myers | SEA | 9.4 | 1.0 to 20.0 |

Salary files: **not available.** No DraftKings or FanDuel salary CSV for this slate is on disk, so no salary-cap lineups were built. The projections are saved at D:\WKP Reports\Fantasy Simulator Report\Week 8 Full Simulation6-10-28 - Week 8 DFS Projections.csv. Drop the salary file in and run dfs_optimize.py to build lineups.

## 5. Limits

- Game scores in section 3 come from the market-anchored sim, so they match the market line and total by construction.
- The play sim runs about 1.3 points per team light on totals; its margins, not its totals, are used above.
- No play-caller field exists, so head coaches stand in for coordinators who call plays.
- Injury status as of 8:06 PM ET Wednesday. Official Wednesday reports for Sunday games were only partly in the feeds. Re-run Thursday morning and Sunday morning.
- Weather is not modeled. Wind of 15 mph or more has historically cut about 2 points off totals.
- Defender points are mostly noise at the player-week level: no method beat a plain recent average in the backtest.