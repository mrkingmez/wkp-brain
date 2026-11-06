# Week 9 Full Simulation, Thursday Rerun - 5 NOV 2026 (11:15 AM ET)

Decision support only. Nothing was submitted on MFL or the pick'em platform. Zac enters everything by hand. Card and IRFL lineup lock at Thursday kickoff, Jacksonville at Baltimore, 8:15 PM ET (01:15Z Friday).

This is the Thursday rerun after Wednesday practice reports. It supersedes the Tuesday 11/3 report (`Week9-Full-Simulation-2026-11-03.md`), which stays on file. Inputs: Odds API 9-book pull 11/5 (data\fantasy-wk9-odds-2026-11-05.json, 494 requests left), merged injury file as of 11/5 15:49Z (MFL, NFL practice report via nflverse, ESPN news and transactions), fresh MFL roster pull 11/5, old sim 4,000 runs per game, play sim 1,500 runs per game rerun this morning.

## 0. WHAT CHANGED SINCE TUESDAY (every change, however small)

**Pick'em card: ONE pick flips, 19 of 20 are unchanged.**

1. **#18 Arizona at Seattle: SEATTLE -11.5 becomes ARIZONA +11.5.** Market moved from Seattle -12.0 to Seattle -8.5 (9 books, range 8.5 to 9.0), total 41.5 to 39.5. The card froze at Seattle -11.5, so the card now gives you 3.0 points of value on Arizona. Cover odds for ARI +11.5 are 58.7% (Seattle -11.5 would be 41.3%). Driver: Sam Darnold ruled out for Sunday (quad), Drew Lock slated to start with an elbow Questionable tag (section 3). Straight-up pick stays Seattle (74% now, was 81%). Logged to the tracker before kickoff as source `model_thu_rerun` (the Tuesday `model` row is untouched and this row supersedes it for this game).
2. SU picks: none changed. All 15 NFL straight-up picks are the same teams. Win odds moved (table below).
3. College picks: none changed. Notre Dame moved 2.0 more points (market ND -5.5 to -7.5, total 57.5 to 55.0). Your card has ND -3.5, so that pick gets stronger (cover 55.1% to 60.2%). I found no 2026 news explaining the move: line value only. Other college moves: BYU at Utah market Utah -5.0 to -4.5, Alabama at LSU LSU -5.5 to -6.0. Texas at Missouri and Colorado at Arizona State did not move.
4. Tiebreaker: unchanged, Buffalo 24, Minnesota 21 (total 45). Market total still 45.5, Buffalo went from -3.0 to -3.5.
5. Cleveland at New Orleans: market moved 1.5 toward the Saints (NO -1.5 to NO -3.0), total 43.0 to 42.5. Pick stays Cleveland +3.5, but the value shrank from 2.0 points to 0.5, so cover odds fall from 55.3% to 51.8% (relabel MED to LOW). Probable driver: Deshaun Watson in concussion protocol (section 3).
6. Smaller line moves, all picks hold: DAL at IND 0.5 (IND +6.5 cover 53.1% to 54.5%), DEN at CAR 0.5 (CAR +3.5, 52.6% to 54.0%), LAR at WAS 1.0 (WAS +5.5, 50.5% to 53.1%, now an actual market edge instead of a number-only lean), NYJ at KC 0.5 toward KC (NYJ +10.5, 54.7% to 53.5%), BUF at MIN 0.5 (BUF -2.5, 50.1% to 51.4%). Totals moved on several games (table). No other spread moved.
7. Confidence relabels (cover odds only): ND MED (60.2%), ARI MED (58.7%), IND and CAR MED-LOW, CLE down to LOW. Everything else LOW. Expected ATS wins on the 20-pick card: 10.4 on Tuesday, 10.6 now (Tuesday method: market plus 15% of the play sim gap, NFL sd 13.2, college sd 15.5).

| # | Game | Card line | Tue market | Thu market | Move | Total Tue to Thu | Tue pick (cover) | Thu pick (cover) | Changed? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | JAX at BAL | JAX -8.5 | JAX -10 | JAX -10 | 0 | 40 to 39.5 | JAX -8.5 (52.1%) | JAX -8.5 (52.5%) | no |
| 2 | Texas at Missouri | Texas -3.5 | Texas -2.5 | Texas -2.5 | 0 | 43 to 43 | Missouri +3.5 (52.6%) | Missouri +3.5 (52.6%) | no |
| 3 | BYU at Utah | Utah -5.5 | Utah -5 | Utah -4.5 | -0.5 | 48.5 to 48.5 | BYU +5.5 (51.3%) | BYU +5.5 (52.6%) | no |
| 4 | Alabama at LSU | LSU -4.5 | LSU -5.5 | LSU -6 | +0.5 | 52.5 to 52.5 | LSU -4.5 (52.6%) | LSU -4.5 (53.9%) | no |
| 5 | Colorado at Arizona State | Arizona State -3.5 | Arizona State -3 | Arizona State -3 | 0 | 48.5 to 48.5 | Colorado +3.5 (51.3%) | Colorado +3.5 (51.3%) | no |
| 6 | Miami at Notre Dame | Notre Dame -3.5 | Notre Dame -5.5 | Notre Dame -7.5 | +2.0 | 57.5 to 55 | Notre Dame -3.5 (55.1%) | Notre Dame -3.5 (60.2%) | no |
| 7 | DET at MIA | DET -7.5 | DET -7 | DET -7 | 0 | 50.5 to 50.5 | MIA +7.5 (51.0%) | MIA +7.5 (51.1%) | no |
| 8 | CIN at ATL | CIN -3.5 | CIN -3 | CIN -3 | 0 | 52.5 to 52.5 | ATL +3.5 (51.8%) | ATL +3.5 (52.1%) | no |
| 9 | DAL at IND | DAL -6.5 | DAL -6 | DAL -5.5 | +0.5 | 51.5 to 51.5 | IND +6.5 (53.1%) | IND +6.5 (54.5%) | no |
| 10 | NYJ at KC | KC -10.5 | KC -9.5 | KC -10 | +0.5 | 47.5 to 47.5 | NYJ +10.5 (54.7%) | NYJ +10.5 (53.5%) | no |
| 11 | CLE at NO | NO -3.5 | NO -1.5 | NO -3 | +1.5 | 43 to 42.5 | CLE +3.5 (55.3%) | CLE +3.5 (51.8%) | no |
| 12 | NYG at PHI | NYG -3.5 | NYG -3 | NYG -3 | 0 | 40 to 38.5 | PHI +3.5 (51.6%) | PHI +3.5 (52.1%) | no |
| 13 | LAR at WAS | LAR -5.5 | LAR -5.5 | LAR -4.5 | +1.0 | 47.5 to 48 | WAS +5.5 (50.5%) | WAS +5.5 (53.1%) | no |
| 14 | DEN at CAR | DEN -3.5 | DEN -3 | DEN -2.5 | +0.5 | 43.5 to 44 | CAR +3.5 (52.6%) | CAR +3.5 (54.0%) | no |
| 15 | HOU at LAC | HOU -5.5 | HOU -4.5 | HOU -4.5 | 0 | 40.5 to 40.5 | LAC +5.5 (52.7%) | LAC +5.5 (52.5%) | no |
| 16 | GB at NE | NE -3.5 | NE -3 | NE -3 | 0 | 47 to 45.5 | GB +3.5 (50.9%) | GB +3.5 (50.8%) | no |
| 17 | LV at SF | SF -9.5 | SF -10 | SF -10 | 0 | 53 to 52.5 | SF -9.5 (51.9%) | SF -9.5 (51.7%) | no |
| 18 | ARI at SEA | SEA -11.5 | SEA -12 | SEA -8.5 | -3.5 | 41.5 to 39.5 | SEA -11.5 (50.7%) | ARI +11.5 (58.7%) | FLIP |
| 19 | TB at CHI | CHI -5.5 | CHI -6 | CHI -6 | 0 | 47 to 47.5 | CHI -5.5 (50.1%) | CHI -5.5 (50.3%) | no |
| 20 | BUF at MIN | BUF -2.5 | BUF -3 | BUF -3.5 | -0.5 | 45.5 to 45.5 | BUF -2.5 (50.1%) | BUF -2.5 (51.4%) | no |

Move column = change in the home team's margin (negative means the line moved toward the visitor). Cover % is for the pick shown.

**SU picks and win odds**

| # | Game | Tue SU pick | Thu SU pick | Win % Tue to Thu |
|---|---|---|---|---|
| 1 | JAX at BAL | JAX | JAX | 76% to 76% |
| 7 | DET at MIA | DET | DET | 71% to 71% |
| 8 | CIN at ATL | CIN | CIN | 59% to 58% |
| 9 | DAL at IND | DAL | DAL | 66% to 65% |
| 10 | NYJ at KC | KC | KC | 75% to 76% |
| 11 | CLE at NO | NO | NO | 55% to 59% |
| 12 | NYG at PHI | NYG | NYG | 59% to 58% |
| 13 | LAR at WAS | LAR | LAR | 66% to 63% |
| 14 | DEN at CAR | DEN | DEN | 58% to 57% |
| 15 | HOU at LAC | HOU | HOU | 64% to 64% |
| 16 | GB at NE | NE | NE | 60% to 60% |
| 17 | LV at SF | SF | SF | 78% to 78% |
| 18 | ARI at SEA | SEA | SEA | 81% to 74% |
| 19 | TB at CHI | CHI | CHI | 66% to 66% |
| 20 | BUF at MIN | BUF | BUF | 58% to 59% |

**IRFL lineup: the recommended 17 holds, same names as Tuesday.** Changes in the inputs:

- Bobby Okereke (CAR LB) is now **Questionable, foot, did not practice Wednesday** (MFL 11/5 15:01Z, NFL practice report 11/5, ESPN 11/5 02:12Z). He was clean on Tuesday. Sim average falls from 7.7 to 5.7 because he plays about 75% of runs. He still beats Dodson (1.1), so he stays, but he is now a Friday-report watch item.
- Wonnum (DET DL, concussion) and D.J. Reed (DET CB, hip): both did not practice Wednesday, still Questionable. Davis (PHI DL, thumb, full practice) and Sanker stay in over them.
- Brian Robinson (ATL RB): still Questionable, hamstring, limited Wednesday (Falcons estimated report via ESPN 11/4, NFL report 11/5). RB2 is a coin flip between Robinson (5.0 blend) and Mike Washington Jr. (4.9, on your taxi). Same as Tuesday.
- Keenan Allen (IND WR): did not practice Wednesday, listed "not injury related, resting player" (NFL practice report 11/5). He is your WR alternate.
- Hockenson, Goff, White, Jefferson, J. Williams, Golden, Bates, Hutchinson, Gibbens, Strnad, Mukuba, Scott: no designation anywhere. Hockenson is clean (an artifact in the first Thursday run had flagged him, see section 2).
- **Flowers (BAL WR): the QB situation got worse (section 3).** Lamar Jackson is officially Out, Brissett was traded to Baltimore but is not expected to be available until Week 10, so Joe Fagnano is the projected starter tonight. The sims do not model this (Flowers 14.2 blend). Decision for Zac below.
- Blend numbers moved by 0.6 or less on almost everyone except Okereke, White (+1.2 on the blend) and Goedert/Schultz (bench TEs). Old sim lineup average was 150.1 on Tuesday, 152.0 now (same 17, different dice, corrected roster).

## 1. DECISIONS FOR ZAC BEFORE 8:15 PM ET KICKOFF

1. **Change the card: Arizona +11.5 instead of Seattle -11.5** (game 18). Everything else on the card stays as entered Tuesday. If you already typed Seattle, this is the one edit. SU for that game stays Seattle.
2. **Flowers tonight, 50/50 call.** Case to keep: best WR option by a wide margin on projection (14.2 vs Allen 10.7, Flournoy 10.0), the sim's recent usage already includes Jackson being out since last weekend, and the lock is per kickoff so you can still see inactives. Case to bench: backup QB Fagnano starting (Brissett not available), game total 39.5 is the lowest on the slate, and Flowers caught 0 of 5 targets Sunday. If you bench him the swap is Allen (IND) or Flournoy (DAL), both Sunday players. My lean is keep Flowers, LOW confidence. Check Baltimore's inactives about 6:45 PM ET before lock.
3. **RB2: Robinson (Q, ATL) versus Washington Jr. (taxi, LV).** Unchanged from Tuesday. Robinson plays Sunday so Friday's report is useful, but the lineup locks Thursday. Starting Washington requires promoting him off taxi (salary 80, through 2028). That is a promotion, not a drop, so no dead cap. No drop is proposed this week, so no dead cap applies anywhere.
4. **Confirm your saved MFL lineup.** I could not read it (section 2). Last known sheet from Tuesday starts Dowdle (PIT, on bye = 0), Flournoy, McPherson, Wonnum, Reed, Kinchens. Changes to make on MFL are unchanged: Dowdle to Robinson (or Washington), Flournoy to Golden, McPherson to Bates, Wonnum to Davis, Reed to Sanker, Kinchens to Mukuba. Keep Goff, White, Flowers, Jefferson, J. Williams, Hockenson, Hutchinson, Okereke, Gibbens, Strnad, Scott.
5. Roster housekeeping: Brissett (ARI on your roster, salary 100 through 2026) was traded to BAL per ESPN. No effect this week. Troy Andersen still shows FA, Questionable (knee). Eliminator: no pick, Zac out of EC2 as of Week 8, confirm on the tracker.

## 2. THE JENKINS / CROSKEY-MERRITT QUESTION, RESOLVED

Those two names are not on your saved lineup. They are hard-coded in `optimize.py` as the default "sheet" (the Week 6 sheet), and the Thursday optimize run was launched without `--roster` and `--sheet`, so it used the default **Week 6 roster file** (`scratch\wk6_roster.json`) and that old sheet. Consequences of that run: no Sanker in the pool, stale injury flags (it showed Hockenson Questionable, Okereke clean), and the "sheet lineup not found" message. I reran optimize with the fresh MFL pull (`scratch\ff9\thu_roster.json`) and the Tuesday sheet. Use the numbers in this report, not the earlier Thursday output. `data\ff-simulator\sim_2026_wk9_lineups.json` now holds the corrected lineups.

Both players are also correctly excluded on their own merits: Jacory Croskey-Merritt (WAS RB) is on NFL injured reserve with a groin injury, expected back Nov 23, and sits in your MFL IR slot (MFL 11/5 15:01Z). Rayshawn Jenkins (BAL S) is on Baltimore's practice squad (nflverse roster status DEV/P07, 11/5 15:26Z). Neither is startable.

Current saved MFL lineup: **not available**. The MFL `lineup` export is rejected for this key ("must go to api.myfantasyleague.com" on every host tried) and `weeklyResults` carries no starters before kickoff. The Tuesday sheet is the last version I have. Please look at the live lineup page.

Tool bug for the main session (not changed by me): `optimize.py` defaults to the Week 6 roster and sheet, so `run.py` must pass `--roster` and `--sheet` every week.

## 3. THE QB / WR STORIES, VERIFIED

Web search returned only 2025 and September 2026 articles for these (it found Darnold's Week 2 glute injury, not this week's), so nothing below is corroborated by an independent web article. Sources are the ESPN player-news feed and the official NFL practice report as published through nflverse, timestamps in Z.

- **Cleveland, Watson down / Sanders up: PARTLY confirmed.** Watson (QB, concussion) was placed in the protocol after symptoms Monday and did not participate in Wednesday practice (NFL practice report 11/5 15:22Z; ESPN 11/4 22:36Z). Official game status is "none yet", MFL lists him Questionable with a Nov 8 return. ESPN 11/4 15:07Z says Shedeur Sanders "could be needed to start" at New Orleans. So Sanders is likely but not confirmed. The market moved 1.5 points toward New Orleans, consistent with that. Friday's report decides it. (Sanders is on your taxi squad, no lineup effect.)
- **Seattle, Darnold out / Lock start: CONFIRMED by ESPN.** Darnold (QB, quadriceps) ruled out for Sunday's game against Arizona, week-to-week (ESPN, Brady Henderson, 11/5 15:41Z; MFL Out, return Nov 15). Drew Lock (elbow) is slated to start per Andrew Siciliano (ESPN 11/4 19:03Z) but carries a Questionable tag in MFL (return Nov 8); nflverse roster shows him active. Who starts if Lock sits: **not available**. The market moved Seattle from -12.0 to -8.5, which drove the pick flip.
- **Detroit, Amon-Ra St. Brown Questionable: CONFIRMED.** Ribs, limited participant Wednesday (Nolan Bianchi, Detroit News via ESPN 11/4 21:05Z; NFL practice report 11/5: limited). MFL Questionable, return Nov 8. Matters to you through Goff, J. Williams and LaPorta (if he sits, Williams's targets go up). Friday's report decides it. He is not on your roster.
- **Two more stories found while checking.** (a) Baltimore: Lamar Jackson is officially Out (thumb, NFL report game status Out, 11/5 15:22Z; back Dec 13). The Brissett trade from Arizona was being finalized (ESPN, Adam Schefter, 11/4 19:50Z), he is not expected to be available until Week 10, and Joe Fagnano is the projected starter tonight (ESPN 11/5 00:14Z). I could not verify trade completion or Fagnano's start with a second source. (b) Arizona: with Brissett gone, who starts at QB for ARI is **not available**; the market already reflects it.

## 4. HOW THE PICKS WERE REDONE

Same method as Tuesday: each game's center = today's market median plus 15% of the gap to the play sim margin (neither the play sim nor the EPA rating beat the market in backtests), NFL sd 13.2, college sd 15.5, pick the side the card line favors against that center, every line ends in .5. The play sim was rerun with the corrected injury file, so its margins moved a little (JAX by 5.5, SEA by 9.1, CIN by 1.6). One correction to Tuesday's doc: the pick-by-pick note for GB at NE said "play sim GB by 4.4", but its own table had it right (New England by 4.4). The pick (GB +3.5 against a NE -3.0 market) does not change.

## 5. FRIDAY AND SUNDAY CHECK LIST (what would change the lineup or card)

- Thursday about 6:45 PM ET: Baltimore inactives. Flowers out or Fagnano confirmed as a problem means swap Flowers for Allen. Lock is 8:15 PM ET.
- Friday report: Okereke (foot, DNP Wednesday). If Out, LB3 becomes Dodson (CAR, 1.1), a big hole. Robinson (ATL): Out means Washington Jr. or Demercado (0.5). Wonnum and Reed. St. Brown. Watson versus Sanders at CLE (changes CLE +3.5 only if the line swings back). Lock at SEA (ARI +11.5 gets better if Lock sits).
- Sunday morning: rerun build_injuries, run_week, optimize (with `--roster` and `--sheet`) and the play sim once inactives post. The card is locked by then, so this is for the IRFL lineup only.
- Not checked: weather (Minnesota is a dome per general knowledge, not verified).

## 5b. Sources (dated)

ESPN player news feed items 10/28 to 11/5 (Watson, Sanders, Darnold, Lock, St. Brown, Brissett, Fagnano, Okereke, Wonnum, Reed, Robinson). NFL practice reports 11/5 15:22Z via nflverse. MFL injury export and rosters 11/5 15:01Z and 15:57Z. ESPN transactions 11/2 to 11/5. The Odds API 9-book pull 11/5 morning. nflverse play-by-play and stats through Week 8. Web searches for the three QB stories returned older seasons only.


## 6. Sim lineups (old sim only, corrected Week 9 roster)

| Lineup | Average | 10th | 90th |
|---|---|---|---|
| 1 EXPECTED (highest average) | 152.0 | 115.1 | 190.8 |
| 2 SAFE (protects a lead) | 152.0 | 115.4 | 190.7 |
| 3 BALANCED UPSIDE (75th percentile) | 152.0 | 115.1 | 190.8 |
| 4 SWING (90th percentile, for an underdog) | 152.0 | 115.1 | 190.8 |
| 5 CONTINGENCY (every Questionable out) | 142.9 | 108.3 | 179.7 |

**1 EXPECTED (highest average)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 22.1 | 7.1 to 38.8 |  |
| RB | White, Rachaad | WAS | 12.2 | 2.9 to 23.0 |  |
| RB | Robinson, Brian | ATL | 5.5 | 0.0 to 14.8 | Questionable, plays about 75% of sims. |
| WR | Flowers, Zay | BAL | 13.9 | 4.0 to 25.0 |  |
| WR | Jefferson, Justin | MIN | 13.8 | 3.6 to 25.5 |  |
| WR | Williams, Jameson | DET | 12.2 | 2.0 to 23.9 |  |
| WR | Golden, Matthew | GBP | 11.2 | 2.0 to 21.6 |  |
| TE | Hockenson, T.J. | MIN | 11.2 | 2.2 to 21.4 |  |
| PK | Bates, Jake | DET | 9.8 | 2.0 to 20.0 |  |
| DL | Hutchinson, Aidan | DET | 5.0 | 1.0 to 10.0 |  |
| DL | Wonnum, D.J. | DET | 2.7 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.7 | 0.0 to 12.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.4 | 2.0 to 9.5 |  |
| LB | Strnad, Justin | DEN | 4.3 | 1.5 to 8.0 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Scott, Nick | CAR | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.1 |  |

**2 SAFE (protects a lead)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 22.1 | 7.1 to 38.8 |  |
| RB | White, Rachaad | WAS | 12.2 | 2.9 to 23.0 |  |
| RB | Robinson, Brian | ATL | 5.5 | 0.0 to 14.8 | Questionable, plays about 75% of sims. |
| WR | Flowers, Zay | BAL | 13.9 | 4.0 to 25.0 |  |
| WR | Jefferson, Justin | MIN | 13.8 | 3.6 to 25.5 |  |
| WR | Williams, Jameson | DET | 12.2 | 2.0 to 23.9 |  |
| WR | Golden, Matthew | GBP | 11.2 | 2.0 to 21.6 |  |
| TE | Hockenson, T.J. | MIN | 11.2 | 2.2 to 21.4 |  |
| PK | Bates, Jake | DET | 9.8 | 2.0 to 20.0 |  |
| DL | Hutchinson, Aidan | DET | 5.0 | 1.0 to 10.0 |  |
| DL | Davis, Jordan | PHI | 2.7 | 0.5 to 5.5 | differs from lineup 1 |
| LB | Gibbens, Jack | ARI | 5.4 | 2.0 to 9.5 |  |
| LB | Okereke, Bobby | CAR | 5.7 | 0.0 to 12.0 | Questionable, plays about 75% of sims. |
| LB | Strnad, Justin | DEN | 4.3 | 1.5 to 8.0 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Scott, Nick | CAR | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.1 |  |

**3 BALANCED UPSIDE (75th percentile)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 22.1 | 7.1 to 38.8 |  |
| RB | White, Rachaad | WAS | 12.2 | 2.9 to 23.0 |  |
| RB | Robinson, Brian | ATL | 5.5 | 0.0 to 14.8 | Questionable, plays about 75% of sims. |
| WR | Flowers, Zay | BAL | 13.9 | 4.0 to 25.0 |  |
| WR | Jefferson, Justin | MIN | 13.8 | 3.6 to 25.5 |  |
| WR | Williams, Jameson | DET | 12.2 | 2.0 to 23.9 |  |
| WR | Golden, Matthew | GBP | 11.2 | 2.0 to 21.6 |  |
| TE | Hockenson, T.J. | MIN | 11.2 | 2.2 to 21.4 |  |
| PK | Bates, Jake | DET | 9.8 | 2.0 to 20.0 |  |
| DL | Hutchinson, Aidan | DET | 5.0 | 1.0 to 10.0 |  |
| DL | Wonnum, D.J. | DET | 2.7 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.7 | 0.0 to 12.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.4 | 2.0 to 9.5 |  |
| LB | Strnad, Justin | DEN | 4.3 | 1.5 to 8.0 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Scott, Nick | CAR | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.1 |  |

**4 SWING (90th percentile, for an underdog)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 22.1 | 7.1 to 38.8 |  |
| RB | White, Rachaad | WAS | 12.2 | 2.9 to 23.0 |  |
| RB | Robinson, Brian | ATL | 5.5 | 0.0 to 14.8 | Questionable, plays about 75% of sims. |
| WR | Jefferson, Justin | MIN | 13.8 | 3.6 to 25.5 |  |
| WR | Flowers, Zay | BAL | 13.9 | 4.0 to 25.0 |  |
| WR | Williams, Jameson | DET | 12.2 | 2.0 to 23.9 |  |
| WR | Golden, Matthew | GBP | 11.2 | 2.0 to 21.6 |  |
| TE | Hockenson, T.J. | MIN | 11.2 | 2.2 to 21.4 |  |
| PK | Bates, Jake | DET | 9.8 | 2.0 to 20.0 |  |
| DL | Hutchinson, Aidan | DET | 5.0 | 1.0 to 10.0 |  |
| DL | Wonnum, D.J. | DET | 2.7 | 0.0 to 7.0 | Questionable, plays about 75% of sims. |
| LB | Okereke, Bobby | CAR | 5.7 | 0.0 to 12.0 | Questionable, plays about 75% of sims. |
| LB | Gibbens, Jack | ARI | 5.4 | 2.0 to 9.5 |  |
| LB | Strnad, Justin | DEN | 4.3 | 1.5 to 8.0 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Scott, Nick | CAR | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.1 |  |

**5 CONTINGENCY (every Questionable out)**

| Slot | Player | Team | Avg | Range (10th to 90th) | Note |
|---|---|---|---|---|---|
| QB | Goff, Jared | DET | 22.1 | 7.1 to 38.8 |  |
| RB | White, Rachaad | WAS | 12.2 | 2.9 to 23.0 |  |
| RB | Demercado, Emari | HOU | 0.5 | -0.2 to 1.4 | differs from lineup 1 |
| WR | Flowers, Zay | BAL | 13.9 | 4.0 to 25.0 |  |
| WR | Jefferson, Justin | MIN | 13.8 | 3.6 to 25.5 |  |
| WR | Williams, Jameson | DET | 12.2 | 2.0 to 23.9 |  |
| WR | Golden, Matthew | GBP | 11.2 | 2.0 to 21.6 |  |
| TE | Hockenson, T.J. | MIN | 11.2 | 2.2 to 21.4 |  |
| PK | Bates, Jake | DET | 9.8 | 2.0 to 20.0 |  |
| DL | Hutchinson, Aidan | DET | 5.0 | 1.0 to 10.0 |  |
| DL | Davis, Jordan | PHI | 2.7 | 0.5 to 5.5 | differs from lineup 1 |
| DL | Kancey, Calijah | TBB | 1.6 | 0.0 to 3.5 | differs from lineup 1 |
| LB | Gibbens, Jack | ARI | 5.4 | 2.0 to 9.5 |  |
| LB | Strnad, Justin | DEN | 4.3 | 1.5 to 8.0 |  |
| DB | Mukuba, Andrew | PHI | 5.8 | 2.0 to 10.0 |  |
| DB | Scott, Nick | CAR | 5.8 | 2.0 to 10.0 |  |
| DB | Sanker, Jonas | NOS | 5.3 | 2.0 to 9.1 |  |

Lineups 1 and 3 are identical; 1 and 4 are identical; 3 and 4 are identical. Your roster has few real choices this week (the only live decisions are QB, the last DB slot and the last WR slot), so the five lineups collapse. Averages shift by about half a point between runs because the dice differ.

Not simulated this week (bye, no team, or no recent usage): Robinson, Tavius (BAL); Barton, Cody (TEN); Andersen, Troy (FA); Dowdle, Rico (PIT); Spears, Tyjae (TEN); Carter, Michael (TEN); Jenkins, Rayshawn (BAL); Ridley, Calvin (TEN); Shepard, Sterling (NYJ).

When the two free agents land (a safety and a defensive end), I will add them for Week 7. Defensive line is the thinnest group: Davis and Kancey are the only two playable linemen this week.

## 7. Game by game: simulated box scores

Player lines are averages across the simulated games where he plays; Questionable players are marked. Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.

### ARI @ SEA

Market: SEA -8.5, total 39.5. Sim: ARI 15.8, SEA 23.9. SEA wins 73.2%, ARI wins 26.8%. Median margin +8.4 for SEA.

| Team stat | ARI | SEA |
|---|---|---|
| Plays | 65 | 61 |
| Pass attempts / completions | 39 / 24 | 30 / 19 |
| Passing yards | 219 | 230 |
| Rush attempts / yards | 24 / 98 | 29 / 123 |
| Sacks taken | 2.7 | 2.1 |
| Interceptions thrown | 1.0 | 0.7 |
| Passing / rushing TDs | 1.1 / 0.6 | 1.4 / 1.2 |
| Field goals | 1.2 | 1.8 |

**ARI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jacoby Brissett | 15.9 | 219 pass yd, 1.1 TD, 1.0 INT; 4.5 rush, 16 yd |  |
| RB | Tyler Allgeier | 12.3 | 11.8 car, 50 yd, 0.35 TD; 2.8 rec, 19 yd, 0.10 TD |  |
| RB | Bam Knight | 4.5 | 6.6 car, 28 yd, 0.10 TD; 1.4 rec, 11 yd, 0.04 TD | Questionable |
| WR | Michael Wilson | 11.2 | 0.5 car, 2 yd, 0.01 TD; 6.6 rec, 64 yd, 0.29 TD | Questionable |
| WR | Reggie Virgil | 2.7 | 1.3 rec, 12 yd, 0.04 TD |  |
| TE | Trey McBride | 18.0 | 9.3 rec, 67 yd, 0.35 TD |  |
| TE | Elijah Higgins | 4.9 | 2.5 rec, 20 yd, 0.07 TD |  |
| K | Chad Ryland | 9.1 | 2.0 FG, 1.6 XP |  |
| DL | Andrew Billings | 2.9 | 1.2 solo, 1.1 ast, 0.35 sack, 0.00 PD, 0.00 INT |  |
| DL | Darius Robinson | 2.8 | 1.2 solo, 1.9 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Jack Gibbens | 5.4 | 2.9 solo, 4.6 ast, 0.03 sack, 0.08 PD, 0.00 INT |  |
| LB | Mack Wilson | 4.9 | 2.6 solo, 3.9 ast, 0.00 sack, 0.06 PD, 0.00 INT |  |
| LB | Zaven Collins | 3.3 | 1.6 solo, 1.0 ast, 0.23 sack, 0.13 PD, 0.00 INT |  |
| DB | Budda Baker | 6.5 | 3.1 solo, 3.3 ast, 0.28 sack, 0.39 PD, 0.07 INT |  |
| DB | Denzel Burke | 4.3 | 2.5 solo, 0.7 ast, 0.00 sack, 0.87 PD, 0.11 INT |  |
| DB | Andrew Wingard | 4.2 | 2.7 solo, 1.9 ast, 0.00 sack, 0.09 PD, 0.09 INT |  |

**SEA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drew Lock | 16.2 | 230 pass yd, 1.4 TD, 0.7 INT | Questionable |
| RB | Emanuel Wilson | 9.5 | 11.8 car, 48 yd, 0.49 TD; 0.7 rec, 8 yd, 0.07 TD |  |
| RB | Zach Charbonnet | 6.5 | 4.9 car, 23 yd, 0.30 TD; 1.2 rec, 10 yd, 0.04 TD |  |
| RB | Jadarian Price | 5.1 | 5.4 car, 24 yd, 0.12 TD; 1.0 rec, 9 yd, 0.04 TD |  |
| WR | Jaxon Smith-Njigba | 19.6 | 6.8 rec, 92 yd, 0.60 TD |  |
| WR | Cooper Kupp | 5.4 | 2.1 rec, 23 yd, 0.18 TD |  |
| WR | Rashid Shaheed | 3.7 | 1.9 rec, 20 yd, 0.08 TD | Questionable |
| WR | Tory Horton | 3.6 | 1.4 rec, 15 yd, 0.12 TD |  |
| TE | AJ Barner | 6.1 | 2.5 rec, 25 yd, 0.12 TD |  |
| TE | Eric Saubert | 1.3 | 0.5 rec, 5 yd, 0.05 TD |  |
| K | Jason Myers | 9.5 | 1.9 FG, 2.5 XP |  |
| DL | Byron Murphy II | 3.5 | 1.5 solo, 1.9 ast, 0.36 sack, 0.00 PD, 0.00 INT |  |
| DL | Leonard Williams | 2.5 | 1.7 solo, 1.2 ast, 0.27 sack, 0.16 PD, 0.00 INT | Questionable |
| LB | Ernest Jones | 9.9 | 5.0 solo, 5.4 ast, 0.33 sack, 0.55 PD, 0.17 INT |  |
| LB | Drake Thomas | 5.8 | 2.7 solo, 3.6 ast, 0.11 sack, 0.26 PD, 0.18 INT |  |
| LB | DeMarcus Lawrence | 3.5 | 1.2 solo, 1.5 ast, 0.09 sack, 0.40 PD, 0.00 INT |  |
| DB | Devon Witherspoon | 5.9 | 3.9 solo, 2.5 ast, 0.00 sack, 0.54 PD, 0.04 INT |  |
| DB | Nick Emmanwori | 5.7 | 3.5 solo, 1.8 ast, 0.32 sack, 0.26 PD, 0.04 INT |  |
| DB | Julian Love | 5.0 | 2.8 solo, 1.5 ast, 0.00 sack, 0.80 PD, 0.21 INT |  |

### BUF @ MIN

Market: MIN +3.5, total 45.5. Sim: BUF 24.4, MIN 21.1. MIN wins 39.3%, BUF wins 60.7%. Median margin -3.5 for MIN.

| Team stat | BUF | MIN |
|---|---|---|
| Plays | 63 | 59 |
| Pass attempts / completions | 30 / 19 | 33 / 21 |
| Passing yards | 209 | 215 |
| Rush attempts / yards | 30 / 136 | 25 / 104 |
| Sacks taken | 3.2 | 2.0 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.3 / 1.4 | 1.5 / 0.8 |
| Field goals | 1.8 | 1.6 |

**BUF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Josh Allen | 20.0 | 209 pass yd, 1.3 TD, 0.7 INT; 6.3 rush, 29 yd |  |
| RB | James Cook | 14.4 | 16.0 car, 73 yd, 0.68 TD; 1.5 rec, 13 yd, 0.06 TD |  |
| RB | Ty Johnson | 5.7 | 2.1 car, 8 yd, 0.08 TD; 2.1 rec, 19 yd, 0.07 TD |  |
| RB | Ray Davis | 2.8 | 2.7 car, 13 yd, 0.07 TD; 0.5 rec, 5 yd, 0.03 TD |  |
| WR | Khalil Shakir | 8.0 | 3.6 rec, 35 yd, 0.16 TD |  |
| WR | Keon Coleman | 5.9 | 2.3 rec, 25 yd, 0.20 TD |  |
| WR | DJ Moore | 5.1 | 2.5 rec, 29 yd, 0.21 TD | Questionable |
| WR | Josh Palmer | 1.8 | 0.9 rec, 11 yd, 0.09 TD | Questionable |
| TE | Dalton Kincaid | 7.5 | 3.1 rec, 34 yd, 0.17 TD |  |
| TE | Dawson Knox | 3.5 | 1.6 rec, 12 yd, 0.12 TD |  |
| K | Tyler Bass | 10.3 | 2.1 FG, 2.5 XP |  |
| DL | Deone Walker | 2.7 | 1.1 solo, 1.6 ast, 0.07 sack, 0.53 PD, 0.00 INT |  |
| DL | Landon Jackson | 2.3 | 0.8 solo, 1.4 ast, 0.24 sack, 0.13 PD, 0.00 INT |  |
| LB | Greg Rousseau | 5.8 | 1.7 solo, 1.2 ast, 0.78 sack, 0.79 PD, 0.00 INT |  |
| LB | Terrel Bernard | 4.8 | 3.1 solo, 3.0 ast, 0.00 sack, 0.08 PD, 0.00 INT |  |
| LB | Dorian Williams | 4.3 | 1.9 solo, 3.1 ast, 0.00 sack, 0.19 PD, 0.13 INT |  |
| DB | Cole Bishop | 5.3 | 3.2 solo, 2.3 ast, 0.14 sack, 0.26 PD, 0.00 INT |  |
| DB | Davison Igbinosun | 4.6 | 2.0 solo, 1.7 ast, 0.00 sack, 1.22 PD, 0.19 INT |  |
| DB | Christian Benford | 4.2 | 2.2 solo, 1.1 ast, 0.04 sack, 0.84 PD, 0.07 INT |  |

**MIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kyler Murray | 14.1 | 162 pass yd, 1.1 TD, 0.5 INT; 3.8 rush, 18 yd | Questionable |
| RB | Aaron Jones | 11.6 | 11.1 car, 45 yd, 0.42 TD; 2.6 rec, 17 yd, 0.08 TD |  |
| RB | Jordan Mason | 4.7 | 6.6 car, 28 yd, 0.22 TD; 0.3 rec, 3 yd, 0.02 TD |  |
| RB | Demond Claiborne | 1.0 | 0.9 car, 4 yd, 0.01 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| WR | Justin Jefferson | 13.8 | 5.4 rec, 53 yd, 0.51 TD |  |
| WR | Jordan Addison | 8.5 | 3.0 rec, 38 yd, 0.22 TD |  |
| WR | Jauan Jennings | 2.6 | 1.2 rec, 11 yd, 0.04 TD |  |
| WR | Tai Felton | 1.7 | 0.7 rec, 8 yd, 0.03 TD |  |
| TE | T.J. Hockenson | 11.2 | 4.5 rec, 41 yd, 0.43 TD |  |
| TE | Gavin Bartholomew | 3.7 | 1.8 rec, 16 yd, 0.06 TD |  |
| K | Will Reichard | 10.1 | 2.1 FG, 2.1 XP |  |
| DL | Jalen Redmond | 3.6 | 1.9 solo, 1.4 ast, 0.12 sack, 0.37 PD, 0.00 INT |  |
| DL | Levi Drake Rodriguez | 2.0 | 1.0 solo, 1.3 ast, 0.12 sack, 0.00 PD, 0.00 INT |  |
| LB | Blake Cashman | 9.9 | 5.0 solo, 5.3 ast, 0.49 sack, 0.61 PD, 0.00 INT |  |
| LB | Eric Wilson | 6.1 | 3.1 solo, 3.1 ast, 0.42 sack, 0.07 PD, 0.00 INT |  |
| LB | Andrew Van Ginkel | 6.0 | 1.7 solo, 1.7 ast, 0.80 sack, 0.32 PD, 0.11 INT |  |
| DB | Josh Metellus | 5.9 | 3.6 solo, 3.5 ast, 0.04 sack, 0.48 PD, 0.00 INT |  |
| DB | Byron Murphy | 5.8 | 3.2 solo, 1.3 ast, 0.00 sack, 0.72 PD, 0.36 INT |  |
| DB | James Pierre | 4.8 | 3.0 solo, 0.6 ast, 0.00 sack, 0.50 PD, 0.30 INT |  |

### CIN @ ATL

Market: ATL +3.0, total 52.5. Sim: CIN 27.8, ATL 24.9. ATL wins 41.2%, CIN wins 58.8%. Median margin -3.0 for ATL.

| Team stat | CIN | ATL |
|---|---|---|
| Plays | 63 | 62 |
| Pass attempts / completions | 36 / 25 | 31 / 19 |
| Passing yards | 271 | 218 |
| Rush attempts / yards | 24 / 100 | 29 / 138 |
| Sacks taken | 2.7 | 2.8 |
| Interceptions thrown | 0.8 | 0.8 |
| Passing / rushing TDs | 1.9 / 1.1 | 1.4 / 1.3 |
| Field goals | 2.1 | 1.8 |

**CIN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Burrow | 23.0 | 271 pass yd, 1.9 TD, 0.8 INT; 2.7 rush, 11 yd |  |
| RB | Chase Brown | 17.1 | 13.6 car, 56 yd, 0.51 TD; 4.7 rec, 28 yd, 0.21 TD |  |
| RB | Samaje Perine | 6.8 | 6.1 car, 25 yd, 0.32 TD; 1.1 rec, 9 yd, 0.08 TD |  |
| WR | Ja'Marr Chase | 15.9 | 6.5 rec, 67 yd, 0.46 TD |  |
| WR | Tee Higgins | 15.3 | 5.6 rec, 75 yd, 0.38 TD |  |
| WR | Dohnte Meyers | 4.8 | 2.2 rec, 22 yd, 0.07 TD |  |
| WR | Mitchell Tinsley | 2.8 | 1.1 rec, 12 yd, 0.07 TD |  |
| TE | Mike Gesicki | 7.0 | 2.4 rec, 28 yd, 0.29 TD |  |
| TE | Drew Sample | 2.8 | 1.2 rec, 10 yd, 0.09 TD |  |
| K | Evan McPherson | 8.1 | 1.4 FG, 2.8 XP |  |
| DL | Boye Mafe | 5.8 | 2.0 solo, 0.9 ast, 0.79 sack, 0.15 PD, 0.00 INT |  |
| DL | Dexter Lawrence | 5.5 | 2.0 solo, 1.6 ast, 0.70 sack, 0.17 PD, 0.00 INT |  |
| LB | Barrett Carter | 6.5 | 3.3 solo, 4.3 ast, 0.13 sack, 0.42 PD, 0.04 INT |  |
| LB | Demetrius Knight Jr. | 6.3 | 3.3 solo, 3.4 ast, 0.13 sack, 0.21 PD, 0.15 INT |  |
| LB | Joe Giles-Harris | 1.5 | 1.0 solo, 0.9 ast, 0.00 sack, 0.07 PD, 0.00 INT |  |
| DB | Jordan Battle | 5.7 | 4.5 solo, 2.4 ast, 0.00 sack, 0.69 PD, 0.32 INT | Questionable |
| DB | Bryan Cook | 4.9 | 3.3 solo, 1.7 ast, 0.09 sack, 0.00 PD, 0.00 INT |  |
| DB | Daxton Hill | 4.7 | 3.3 solo, 1.0 ast, 0.00 sack, 0.67 PD, 0.00 INT |  |

**ATL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Michael Penix Jr. | 17.0 | 218 pass yd, 1.4 TD, 0.8 INT; 3.1 rush, 12 yd |  |
| RB | Bijan Robinson | 20.2 | 17.8 car, 89 yd, 0.69 TD; 3.4 rec, 28 yd, 0.19 TD |  |
| RB | Brian Robinson | 5.5 | 6.7 car, 30 yd, 0.47 TD; 0.7 rec, 6 yd, 0.02 TD | Questionable |
| WR | Drake London | 13.1 | 5.0 rec, 64 yd, 0.28 TD |  |
| WR | Jahan Dotson | 7.4 | 2.2 rec, 40 yd, 0.20 TD |  |
| WR | Olamide Zaccheaus | 2.1 | 1.0 rec, 8 yd, 0.05 TD |  |
| WR | Chris Blair | 0.7 | 0.3 rec, 3 yd, 0.01 TD |  |
| TE | Kyle Pitts | 10.2 | 4.1 rec, 37 yd, 0.41 TD |  |
| TE | Austin Hooper | 3.0 | 1.3 rec, 12 yd, 0.09 TD |  |
| K | Nick Folk | 8.4 | 1.6 FG, 2.5 XP |  |
| DL | Za'Darius Smith | 3.2 | 0.8 solo, 0.3 ast, 0.73 sack, 0.13 PD, 0.00 INT |  |
| DL | Gervon Dexter Sr. | 3.1 | 1.4 solo, 1.3 ast, 0.18 sack, 0.10 PD, 0.00 INT |  |
| LB | Kendal Daniels | 8.2 | 5.3 solo, 2.4 ast, 0.14 sack, 0.34 PD, 0.18 INT |  |
| LB | Harold Perkins Jr. | 5.5 | 3.1 solo, 2.3 ast, 0.26 sack, 0.12 PD, 0.00 INT |  |
| LB | Divine Deablo | 3.1 | 2.5 solo, 2.4 ast, 0.02 sack, 0.26 PD, 0.00 INT | Questionable |
| DB | Jessie Bates | 6.9 | 3.2 solo, 2.5 ast, 0.00 sack, 0.56 PD, 0.19 INT |  |
| DB | Xavier Watts | 6.8 | 3.5 solo, 3.4 ast, 0.05 sack, 0.42 PD, 0.18 INT |  |
| DB | C.J. Henderson | 6.4 | 4.0 solo, 1.5 ast, 0.00 sack, 1.06 PD, 0.05 INT |  |

### CLE @ NO

Market: NO -3.0, total 42.5. Sim: CLE 19.8, NO 22.8. NO wins 59.9%, CLE wins 40.1%. Median margin +3.1 for NO.

| Team stat | CLE | NO |
|---|---|---|
| Plays | 62 | 64 |
| Pass attempts / completions | 34 / 22 | 34 / 23 |
| Passing yards | 234 | 214 |
| Rush attempts / yards | 25 / 107 | 28 / 111 |
| Sacks taken | 3.0 | 2.4 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.2 / 0.9 | 1.3 / 1.2 |
| Field goals | 1.5 | 1.7 |

**CLE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Deshaun Watson | 14.3 | 174 pass yd, 0.9 TD, 0.5 INT; 4.6 rush, 20 yd | Questionable |
| RB | Quinshon Judkins | 9.9 | 10.1 car, 39 yd, 0.35 TD; 2.2 rec, 16 yd, 0.04 TD |  |
| RB | Dylan Sampson | 5.7 | 2.4 car, 11 yd, 0.05 TD; 2.1 rec, 19 yd, 0.05 TD |  |
| RB | Audric Estimé | 2.7 | 3.5 car, 15 yd, 0.21 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | KC Concepcion | 8.9 | 0.9 car, 4 yd, 0.02 TD; 3.9 rec, 39 yd, 0.11 TD |  |
| WR | Denzel Boston | 6.8 | 3.3 rec, 38 yd, 0.34 TD | Questionable |
| WR | Jerry Jeudy | 5.2 | 2.4 rec, 23 yd, 0.09 TD |  |
| WR | Isaiah Bond | 2.3 | 0.9 rec, 12 yd, 0.03 TD |  |
| TE | Harold Fannin Jr. | 11.6 | 4.4 rec, 47 yd, 0.40 TD |  |
| TE | Blake Whiteheart | 1.4 | 0.5 rec, 5 yd, 0.08 TD |  |
| K | Andre Szmyt | 8.8 | 1.8 FG, 2.0 XP |  |
| DL | Adin Huntington | 3.4 | 1.0 solo, 1.6 ast, 0.47 sack, 0.00 PD, 0.00 INT |  |
| DL | Mason Graham | 3.4 | 1.6 solo, 1.2 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| LB | Carson Schwesinger | 5.9 | 3.8 solo, 5.9 ast, 0.14 sack, 0.13 PD, 0.00 INT | Questionable |
| LB | Quincy Williams | 5.6 | 3.8 solo, 3.0 ast, 0.14 sack, 0.43 PD, 0.00 INT | Questionable |
| LB | Jerome Baker | 1.1 | 0.3 solo, 1.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Ronnie Hickman Jr. | 5.9 | 3.1 solo, 3.1 ast, 0.06 sack, 0.32 PD, 0.07 INT |  |
| DB | Grant Delpit | 5.2 | 3.1 solo, 1.7 ast, 0.17 sack, 0.37 PD, 0.08 INT |  |
| DB | Denzel Ward | 5.1 | 1.8 solo, 1.3 ast, 0.00 sack, 1.20 PD, 0.39 INT |  |

**NO**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tyler Shough | 18.4 | 214 pass yd, 1.3 TD, 0.6 INT; 4.0 rush, 19 yd |  |
| RB | Kendre Miller | 8.4 | 10.5 car, 37 yd, 0.40 TD; 1.3 rec, 8 yd, 0.04 TD |  |
| RB | Alvin Kamara | 6.9 | 5.8 car, 23 yd, 0.30 TD; 2.6 rec, 18 yd, 0.12 TD | Questionable |
| RB | CJ Donaldson | 2.1 | 3.0 car, 14 yd, 0.07 TD; 0.5 rec, 4 yd, 0.02 TD | Questionable |
| WR | Chris Olave | 13.1 | 5.6 rec, 58 yd, 0.29 TD |  |
| WR | Devaughn Vele | 8.4 | 3.7 rec, 34 yd, 0.22 TD |  |
| WR | Bryce Lance | 3.1 | 1.3 rec, 11 yd, 0.10 TD |  |
| WR | Barion Brown | 1.4 | 0.6 rec, 6 yd, 0.02 TD |  |
| TE | Juwan Johnson | 7.1 | 3.2 rec, 29 yd, 0.18 TD |  |
| TE | Noah Fant | 3.2 | 1.3 rec, 10 yd, 0.15 TD |  |
| K | Daniel Carlson | 7.6 | 1.4 FG, 2.3 XP |  |
| DL | Chase Young | 6.3 | 1.4 solo, 1.3 ast, 1.08 sack, 0.36 PD, 0.00 INT |  |
| DL | Carl Granderson | 5.5 | 1.5 solo, 2.5 ast, 0.82 sack, 0.11 PD, 0.07 INT |  |
| LB | Pete Werner | 5.7 | 3.1 solo, 3.3 ast, 0.21 sack, 0.27 PD, 0.00 INT |  |
| LB | Kaden Elliss | 4.1 | 2.7 solo, 2.5 ast, 0.00 sack, 0.14 PD, 0.00 INT |  |
| LB | Danny Stutsman | 3.5 | 2.2 solo, 2.4 ast, 0.00 sack, 0.13 PD, 0.00 INT |  |
| DB | Jonas Sanker | 5.3 | 3.7 solo, 2.1 ast, 0.00 sack, 0.23 PD, 0.04 INT |  |
| DB | Julian Blackmon | 5.3 | 2.8 solo, 2.5 ast, 0.00 sack, 0.30 PD, 0.29 INT |  |
| DB | Martin Emerson | 4.5 | 3.3 solo, 0.3 ast, 0.00 sack, 0.89 PD, 0.44 INT | Questionable |

### DAL @ IND

Market: IND +5.5, total 51.5. Sim: DAL 28.3, IND 23.1. IND wins 34.4%, DAL wins 65.6%. Median margin -5.3 for IND.

| Team stat | DAL | IND |
|---|---|---|
| Plays | 65 | 63 |
| Pass attempts / completions | 35 / 22 | 34 / 21 |
| Passing yards | 266 | 233 |
| Rush attempts / yards | 28 / 117 | 27 / 118 |
| Sacks taken | 2.1 | 2.2 |
| Interceptions thrown | 0.6 | 0.8 |
| Passing / rushing TDs | 1.8 / 1.2 | 1.3 / 1.2 |
| Field goals | 2.1 | 1.7 |

**DAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Dak Prescott | 22.1 | 266 pass yd, 1.8 TD, 0.6 INT; 2.8 rush, 12 yd |  |
| RB | Javonte Williams | 15.1 | 16.4 car, 67 yd, 0.84 TD; 1.7 rec, 12 yd, 0.10 TD |  |
| RB | Tyler Goodson | 4.4 | 5.1 car, 21 yd, 0.12 TD; 0.8 rec, 8 yd, 0.04 TD |  |
| RB | Hunter Luepke | 1.7 | 1.0 car, 4 yd, 0.02 TD; 0.5 rec, 5 yd, 0.02 TD |  |
| WR | CeeDee Lamb | 17.1 | 6.4 rec, 74 yd, 0.55 TD |  |
| WR | Ryan Flournoy | 9.8 | 3.6 rec, 42 yd, 0.32 TD |  |
| WR | George Pickens | 9.1 | 4.4 rec, 59 yd, 0.33 TD | Questionable |
| WR | KaVontae Turpin | 2.0 | 0.5 car, 2 yd, 0.06 TD; 0.7 rec, 9 yd, 0.06 TD | Questionable |
| TE | Jake Ferguson | 3.7 | 2.0 rec, 17 yd, 0.21 TD | Questionable |
| TE | Brevyn Spann-Ford | 3.4 | 1.5 rec, 15 yd, 0.05 TD |  |
| K | Brandon Aubrey | 10.2 | 2.0 FG, 2.8 XP |  |
| DL | Quinnen Williams | 5.1 | 2.2 solo, 1.4 ast, 0.61 sack, 0.16 PD, 0.04 INT |  |
| DL | Elijah Garcia | 2.6 | 1.0 solo, 1.9 ast, 0.22 sack, 0.00 PD, 0.00 INT |  |
| LB | Shemar James | 4.9 | 3.1 solo, 2.2 ast, 0.03 sack, 0.16 PD, 0.15 INT |  |
| LB | DeMarvion Overshown | 4.5 | 2.0 solo, 2.3 ast, 0.00 sack, 0.38 PD, 0.20 INT |  |
| LB | Dee Winters | 3.5 | 2.8 solo, 1.7 ast, 0.00 sack, 0.19 PD, 0.18 INT | Questionable |
| DB | Caleb Downs | 4.3 | 3.8 solo, 2.6 ast, 0.08 sack, 0.09 PD, 0.00 INT | Questionable |
| DB | DaRon Bland | 3.9 | 2.7 solo, 0.8 ast, 0.00 sack, 0.79 PD, 0.00 INT |  |
| DB | Malik Hooker | 3.6 | 2.2 solo, 2.1 ast, 0.00 sack, 0.36 PD, 0.00 INT |  |

**IND**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Daniel Jones | 16.9 | 233 pass yd, 1.3 TD, 0.8 INT; 2.3 rush, 10 yd |  |
| RB | Jonathan Taylor | 15.8 | 14.4 car, 60 yd, 0.73 TD; 2.5 rec, 26 yd, 0.07 TD |  |
| RB | Seth McGowan | 3.4 | 4.1 car, 19 yd, 0.10 TD; 0.4 rec, 4 yd, 0.02 TD |  |
| RB | DJ Giddens | 1.5 | 2.3 car, 11 yd, 0.06 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Keenan Allen | 11.0 | 4.8 rec, 49 yd, 0.23 TD |  |
| WR | Josh Downs | 9.3 | 3.6 rec, 41 yd, 0.27 TD |  |
| WR | Laquon Treadwell | 4.1 | 1.7 rec, 21 yd, 0.05 TD |  |
| WR | Deion Burks | 2.1 | 0.8 rec, 10 yd, 0.03 TD |  |
| TE | Tyler Warren | 9.8 | 4.3 rec, 35 yd, 0.26 TD |  |
| TE | Mo Alie-Cox | 3.3 | 1.0 rec, 10 yd, 0.23 TD |  |
| K | Spencer Shrader | 9.6 | 2.0 FG, 2.3 XP |  |
| DL | DeForest Buckner | 4.7 | 1.7 solo, 2.4 ast, 0.42 sack, 0.36 PD, 0.00 INT |  |
| DL | Adetomiwa Adebawore | 4.2 | 1.3 solo, 1.7 ast, 0.59 sack, 0.33 PD, 0.00 INT |  |
| LB | Akeem Davis-Gaither | 4.5 | 3.9 solo, 4.1 ast, 0.00 sack, 0.11 PD, 0.00 INT | Questionable |
| LB | CJ Allen | 3.4 | 1.5 solo, 2.2 ast, 0.27 sack, 0.00 PD, 0.00 INT |  |
| LB | Germaine Pratt | 3.1 | 1.4 solo, 2.0 ast, 0.00 sack, 0.33 PD, 0.07 INT |  |
| DB | A.J. Haulcy | 4.5 | 3.1 solo, 2.2 ast, 0.00 sack, 0.26 PD, 0.00 INT |  |
| DB | Camryn Bynum | 4.1 | 2.6 solo, 1.2 ast, 0.00 sack, 0.32 PD, 0.21 INT |  |
| DB | Justin Walley | 3.9 | 3.1 solo, 1.6 ast, 0.14 sack, 0.33 PD, 0.00 INT | Questionable |

### DEN @ CAR

Market: CAR +2.5, total 44.0. Sim: DEN 23.1, CAR 21.0. CAR wins 43.5%, DEN wins 56.5%. Median margin -2.4 for CAR.

| Team stat | DEN | CAR |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 33 / 21 | 34 / 21 |
| Passing yards | 215 | 219 |
| Rush attempts / yards | 26 / 110 | 26 / 108 |
| Sacks taken | 2.1 | 2.6 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.4 / 0.9 |
| Field goals | 1.7 | 1.6 |

**DEN**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bo Nix | 19.7 | 215 pass yd, 1.5 TD, 0.6 INT; 4.8 rush, 22 yd |  |
| RB | Jonah Coleman | 9.5 | 7.0 car, 32 yd, 0.30 TD; 2.0 rec, 22 yd, 0.06 TD |  |
| RB | J.K. Dobbins | 9.2 | 12.5 car, 47 yd, 0.44 TD; 1.1 rec, 8 yd, 0.03 TD |  |
| RB | Adam Prentice | 0.7 | 0.3 car, 2 yd, 0.00 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| WR | Jaylen Waddle | 11.7 | 4.6 rec, 45 yd, 0.41 TD |  |
| WR | Courtland Sutton | 9.3 | 3.7 rec, 40 yd, 0.28 TD |  |
| WR | Marvin Mims Jr. | 4.8 | 0.8 car, 4 yd, 0.01 TD; 2.1 rec, 19 yd, 0.06 TD |  |
| WR | Troy Franklin | 3.7 | 1.7 rec, 16 yd, 0.08 TD |  |
| TE | Evan Engram | 5.2 | 2.2 rec, 22 yd, 0.13 TD |  |
| TE | Nate Adkins | 3.5 | 0.9 rec, 7 yd, 0.30 TD |  |
| K | Wil Lutz | 9.0 | 1.8 FG, 2.4 XP |  |
| DL | Malcolm Roach | 4.2 | 1.8 solo, 1.3 ast, 0.49 sack, 0.36 PD, 0.00 INT |  |
| DL | Zach Allen | 3.6 | 0.9 solo, 1.7 ast, 0.40 sack, 0.37 PD, 0.00 INT |  |
| LB | Alex Singleton | 9.6 | 5.5 solo, 6.0 ast, 0.27 sack, 0.31 PD, 0.00 INT |  |
| LB | Justin Strnad | 4.3 | 2.3 solo, 2.3 ast, 0.11 sack, 0.26 PD, 0.00 INT |  |
| LB | Nik Bonitto | 3.8 | 1.4 solo, 0.7 ast, 0.52 sack, 0.04 PD, 0.00 INT |  |
| DB | Ja'Quan McMillian | 5.7 | 2.7 solo, 1.1 ast, 0.22 sack, 0.93 PD, 0.17 INT |  |
| DB | Brandon Jones | 4.6 | 3.6 solo, 2.3 ast, 0.00 sack, 0.52 PD, 0.17 INT | Questionable |
| DB | Riley Moss | 4.4 | 2.2 solo, 1.4 ast, 0.04 sack, 1.04 PD, 0.12 INT |  |

**CAR**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Bryce Young | 17.3 | 219 pass yd, 1.4 TD, 0.7 INT; 2.6 rush, 11 yd |  |
| RB | Chuba Hubbard | 15.6 | 16.2 car, 68 yd, 0.56 TD; 2.9 rec, 19 yd, 0.14 TD |  |
| RB | AJ Dillon | 2.1 | 3.3 car, 13 yd, 0.06 TD; 0.3 rec, 2 yd, 0.00 TD |  |
| RB | Trevor Etienne | 1.3 | 1.4 car, 6 yd, 0.03 TD; 0.3 rec, 3 yd, 0.00 TD |  |
| WR | Tetairoa McMillan | 13.1 | 5.4 rec, 59 yd, 0.32 TD |  |
| WR | Jalen Coker | 9.7 | 3.9 rec, 42 yd, 0.27 TD |  |
| WR | John Metchie III | 4.5 | 2.1 rec, 17 yd, 0.12 TD |  |
| WR | Brycen Tremayne | 2.0 | 0.9 rec, 10 yd, 0.02 TD |  |
| TE | Darren Waller | 5.2 | 1.9 rec, 21 yd, 0.21 TD |  |
| TE | Tommy Tremble | 4.9 | 2.1 rec, 18 yd, 0.16 TD |  |
| K | Ryan Fitzgerald | 8.5 | 1.7 FG, 2.1 XP |  |
| DL | Derrick Brown | 3.8 | 2.0 solo, 1.9 ast, 0.08 sack, 0.58 PD, 0.00 INT |  |
| DL | Aaron Hall | 2.2 | 0.8 solo, 2.2 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Devin Lloyd | 7.5 | 3.5 solo, 3.0 ast, 0.28 sack, 0.34 PD, 0.23 INT |  |
| LB | Bobby Okereke | 5.7 | 4.3 solo, 2.4 ast, 0.15 sack, 0.72 PD, 0.10 INT | Questionable |
| LB | Nick Hampton | 3.2 | 1.4 solo, 1.4 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Nick Scott | 5.8 | 3.9 solo, 2.0 ast, 0.00 sack, 0.31 PD, 0.03 INT |  |
| DB | Zakee Wheatley | 5.3 | 3.1 solo, 1.2 ast, 0.00 sack, 0.73 PD, 0.22 INT |  |
| DB | Tre'von Moehrig | 4.4 | 3.0 solo, 1.8 ast, 0.17 sack, 0.00 PD, 0.00 INT |  |

### DET @ MIA

Market: MIA +7.0, total 50.5. Sim: DET 29.0, MIA 21.7. MIA wins 28.9%, DET wins 71.1%. Median margin -7.2 for MIA.

| Team stat | DET | MIA |
|---|---|---|
| Plays | 65 | 59 |
| Pass attempts / completions | 34 / 23 | 31 / 19 |
| Passing yards | 276 | 221 |
| Rush attempts / yards | 29 / 129 | 26 / 120 |
| Sacks taken | 2.3 | 2.4 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.8 / 1.3 | 1.2 / 1.1 |
| Field goals | 2.2 | 1.6 |

**DET**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jared Goff | 22.1 | 276 pass yd, 1.8 TD, 0.6 INT; 1.9 rush, 7 yd |  |
| RB | Jahmyr Gibbs | 25.9 | 22.4 car, 101 yd, 1.11 TD; 4.2 rec, 36 yd, 0.29 TD |  |
| RB | Sione Vaki | 2.9 | 3.5 car, 16 yd, 0.09 TD; 0.4 rec, 4 yd, 0.00 TD |  |
| WR | Amon-Ra St. Brown | 12.7 | 6.7 rec, 74 yd, 0.48 TD | Questionable |
| WR | Jameson Williams | 12.2 | 3.7 rec, 56 yd, 0.48 TD |  |
| WR | Isaac TeSlaa | 4.5 | 1.5 rec, 22 yd, 0.14 TD |  |
| TE | Sam LaPorta | 10.0 | 3.7 rec, 44 yd, 0.32 TD |  |
| TE | Tyler Conklin | 1.7 | 0.8 rec, 8 yd, 0.03 TD |  |
| K | Jake Bates | 9.8 | 1.8 FG, 3.0 XP |  |
| DL | Aidan Hutchinson | 5.0 | 2.0 solo, 1.1 ast, 0.69 sack, 0.15 PD, 0.04 INT |  |
| DL | Alim McNeill | 3.0 | 0.8 solo, 1.0 ast, 0.51 sack, 0.11 PD, 0.00 INT |  |
| LB | Derrick Barnes | 4.4 | 2.4 solo, 1.7 ast, 0.23 sack, 0.20 PD, 0.10 INT |  |
| LB | Malcolm Rodriguez | 2.0 | 1.3 solo, 1.1 ast, 0.07 sack, 0.00 PD, 0.00 INT |  |
| LB | Trevor Nowaske | 1.9 | 1.4 solo, 0.9 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Chuck Clark | 5.6 | 3.3 solo, 2.3 ast, 0.12 sack, 0.25 PD, 0.09 INT |  |
| DB | Roger McCreary | 4.7 | 2.8 solo, 0.9 ast, 0.09 sack, 0.97 PD, 0.00 INT |  |
| DB | D.J. Reed | 4.1 | 3.3 solo, 1.4 ast, 0.00 sack, 0.86 PD, 0.16 INT | Questionable |

**MIA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Malik Willis | 19.6 | 221 pass yd, 1.2 TD, 0.7 INT; 5.6 rush, 30 yd |  |
| RB | Ollie Gordon II | 10.5 | 13.2 car, 58 yd, 0.56 TD; 0.8 rec, 6 yd, 0.02 TD |  |
| RB | Jaylen Wright | 3.1 | 5.6 car, 22 yd, 0.16 TD; 0.4 rec, 5 yd, 0.01 TD | Questionable |
| RB | DJ Herman | 1.0 | 0.0 car, 0 yd, 0.00 TD; 0.4 rec, 5 yd, 0.01 TD |  |
| WR | Malik Washington | 10.7 | 1.1 car, 5 yd, 0.05 TD; 4.4 rec, 41 yd, 0.23 TD |  |
| WR | Caleb Douglas | 8.4 | 2.8 rec, 38 yd, 0.32 TD |  |
| WR | Kevin Coleman Jr. | 5.8 | 2.0 rec, 21 yd, 0.29 TD |  |
| WR | Chris Bell | 5.4 | 2.3 rec, 25 yd, 0.07 TD |  |
| TE | Greg Dulcich | 8.7 | 3.8 rec, 42 yd, 0.13 TD |  |
| TE | Will Kacmarek | 1.2 | 0.7 rec, 7 yd, 0.03 TD | Questionable |
| K | Riley Patterson | 7.8 | 1.5 FG, 2.2 XP |  |
| DL | Zach Sieler | 2.9 | 1.9 solo, 1.6 ast, 0.38 sack, 0.00 PD, 0.00 INT | Questionable |
| DL | Jordan Phillips | 1.9 | 1.0 solo, 1.8 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Jordyn Brooks | 7.7 | 4.6 solo, 5.6 ast, 0.04 sack, 0.25 PD, 0.00 INT |  |
| LB | Jacob Rodriguez | 7.7 | 3.7 solo, 6.0 ast, 0.00 sack, 0.12 PD, 0.12 INT |  |
| LB | Joshua Uche | 4.7 | 2.2 solo, 2.1 ast, 0.35 sack, 0.00 PD, 0.00 INT |  |
| DB | Chris Johnson | 4.8 | 3.0 solo, 2.7 ast, 0.00 sack, 0.18 PD, 0.00 INT |  |
| DB | Michael Taaffe | 4.1 | 2.5 solo, 3.0 ast, 0.00 sack, 0.29 PD, 0.28 INT | Questionable |
| DB | Dante Trader Jr. | 3.2 | 2.5 solo, 2.8 ast, 0.00 sack, 0.31 PD, 0.07 INT | Questionable |

### GB @ NE

Market: NE -3.0, total 45.5. Sim: GB 21.3, NE 24.3. NE wins 59.3%, GB wins 40.7%. Median margin +3.0 for NE.

| Team stat | GB | NE |
|---|---|---|
| Plays | 61 | 61 |
| Pass attempts / completions | 33 / 21 | 31 / 21 |
| Passing yards | 231 | 253 |
| Rush attempts / yards | 25 / 93 | 28 / 120 |
| Sacks taken | 2.5 | 2.1 |
| Interceptions thrown | 0.7 | 0.7 |
| Passing / rushing TDs | 1.3 / 1.0 | 1.5 / 1.1 |
| Field goals | 1.6 | 1.8 |

**GB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jordan Love | 16.8 | 231 pass yd, 1.3 TD, 0.7 INT; 1.3 rush, 5 yd |  |
| RB | Josh Jacobs | 9.8 | 8.1 car, 28 yd, 0.38 TD; 2.2 rec, 15 yd, 0.19 TD |  |
| RB | MarShawn Lloyd | 6.3 | 6.1 car, 20 yd, 0.31 TD; 1.2 rec, 9 yd, 0.06 TD |  |
| RB | Pierre Strong | 4.9 | 3.6 car, 13 yd, 0.08 TD; 1.6 rec, 13 yd, 0.05 TD |  |
| WR | Matthew Golden | 11.2 | 4.3 rec, 50 yd, 0.31 TD |  |
| WR | Christian Watson | 9.1 | 4.4 rec, 60 yd, 0.33 TD | Questionable |
| WR | Savion Williams | 3.0 | 0.9 car, 4 yd, 0.02 TD; 1.2 rec, 12 yd, 0.03 TD |  |
| WR | Bo Melton | 1.5 | 0.6 rec, 6 yd, 0.03 TD |  |
| TE | Tucker Kraft | 8.6 | 3.8 rec, 34 yd, 0.24 TD |  |
| TE | Jonnu Smith | 1.5 | 0.7 rec, 7 yd, 0.02 TD |  |
| K | Trey Smack | 7.6 | 1.5 FG, 2.2 XP |  |
| DL | Brenton Cox Jr. | 3.3 | 1.5 solo, 0.9 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| DL | Barryn Sorrell | 3.2 | 1.8 solo, 1.2 ast, 0.24 sack, 0.00 PD, 0.00 INT |  |
| LB | Isaiah McDuffie | 4.9 | 2.8 solo, 3.1 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Ty'Ron Hopper | 4.8 | 2.0 solo, 2.0 ast, 0.15 sack, 0.63 PD, 0.23 INT |  |
| LB | Lukas Van Ness | 4.3 | 2.0 solo, 1.5 ast, 0.44 sack, 0.16 PD, 0.00 INT |  |
| DB | Evan Williams | 7.9 | 4.8 solo, 3.2 ast, 0.09 sack, 0.54 PD, 0.19 INT |  |
| DB | Brandon Cisse | 5.5 | 2.9 solo, 1.2 ast, 0.16 sack, 1.10 PD, 0.14 INT |  |
| DB | Xavier McKinney | 5.4 | 2.7 solo, 2.2 ast, 0.08 sack, 0.55 PD, 0.26 INT |  |

**NE**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Drake Maye | 21.4 | 253 pass yd, 1.5 TD, 0.7 INT; 4.6 rush, 20 yd |  |
| RB | Rhamondre Stevenson | 13.6 | 9.0 car, 39 yd, 0.38 TD; 3.3 rec, 31 yd, 0.19 TD |  |
| RB | TreVeyon Henderson | 5.2 | 7.0 car, 30 yd, 0.29 TD; 1.1 rec, 10 yd, 0.04 TD | Questionable |
| RB | Corey Kiner | 2.9 | 4.5 car, 20 yd, 0.09 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | DeMario Douglas | 9.6 | 3.5 rec, 43 yd, 0.31 TD |  |
| WR | Efton Chism III | 5.8 | 2.4 rec, 26 yd, 0.14 TD |  |
| WR | A.J. Brown | 4.6 | 2.6 rec, 28 yd, 0.14 TD | Questionable |
| WR | Kyle Williams | 4.5 | 1.3 rec, 21 yd, 0.19 TD |  |
| TE | Hunter Henry | 8.2 | 4.7 rec, 50 yd, 0.27 TD | Questionable |
| TE | Eli Raridon | 6.2 | 2.4 rec, 27 yd, 0.19 TD |  |
| K | Andy Borregales | 8.0 | 1.5 FG, 2.5 XP |  |
| DL | Cory Durden | 2.6 | 1.2 solo, 1.6 ast, 0.22 sack, 0.00 PD, 0.00 INT |  |
| DL | Milton Williams | 2.3 | 1.2 solo, 1.3 ast, 0.14 sack, 0.00 PD, 0.00 INT |  |
| LB | Christian Elliss | 6.1 | 3.5 solo, 3.9 ast, 0.14 sack, 0.18 PD, 0.00 INT |  |
| LB | Elijah Ponder | 4.7 | 1.4 solo, 1.0 ast, 0.67 sack, 0.15 PD, 0.00 INT |  |
| LB | Robert Spillane | 3.9 | 1.9 solo, 3.0 ast, 0.00 sack, 0.32 PD, 0.00 INT |  |
| DB | Marcus Jones | 5.4 | 2.8 solo, 1.8 ast, 0.18 sack, 0.62 PD, 0.10 INT |  |
| DB | Craig Woodson | 4.4 | 2.5 solo, 2.3 ast, 0.00 sack, 0.28 PD, 0.10 INT |  |
| DB | Christian Gonzalez | 3.7 | 2.9 solo, 0.6 ast, 0.00 sack, 0.49 PD, 0.00 INT |  |

### HOU @ LAC

Market: LAC +4.5, total 40.5. Sim: HOU 22.4, LAC 18.0. LAC wins 36.5%, HOU wins 63.5%. Median margin -4.5 for LAC.

| Team stat | HOU | LAC |
|---|---|---|
| Plays | 63 | 63 |
| Pass attempts / completions | 34 / 22 | 34 / 21 |
| Passing yards | 251 | 225 |
| Rush attempts / yards | 27 / 98 | 27 / 105 |
| Sacks taken | 2.4 | 2.8 |
| Interceptions thrown | 0.7 | 1.0 |
| Passing / rushing TDs | 1.5 / 1.0 | 1.1 / 0.8 |
| Field goals | 1.7 | 1.4 |

**HOU**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | C.J. Stroud | 19.9 | 251 pass yd, 1.5 TD, 0.7 INT; 3.6 rush, 13 yd |  |
| RB | Woody Marks | 11.8 | 16.5 car, 58 yd, 0.50 TD; 1.6 rec, 13 yd, 0.06 TD |  |
| RB | Nick Chubb | 1.6 | 1.9 car, 8 yd, 0.11 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| RB | Dare Ogunbowale | 1.4 | 0.7 car, 3 yd, 0.07 TD; 0.3 rec, 4 yd, 0.01 TD |  |
| WR | Nico Collins | 10.6 | 3.6 rec, 50 yd, 0.28 TD |  |
| WR | Xavier Hutchinson | 7.0 | 0.7 car, 3 yd, 0.02 TD; 2.6 rec, 30 yd, 0.16 TD |  |
| WR | Marvin Harrison Jr. | 6.3 | 2.3 rec, 24 yd, 0.26 TD |  |
| WR | Kayshon Boutte | 4.7 | 2.0 rec, 23 yd, 0.06 TD |  |
| TE | Dalton Schultz | 9.0 | 4.2 rec, 40 yd, 0.15 TD |  |
| TE | Foster Moreau | 4.3 | 1.4 rec, 11 yd, 0.31 TD |  |
| K | Ka'imi Fairbairn | 10.8 | 2.3 FG, 2.3 XP |  |
| DL | Will Anderson Jr. | 6.1 | 2.1 solo, 1.9 ast, 0.88 sack, 0.11 PD, 0.00 INT |  |
| DL | Danielle Hunter | 4.8 | 1.3 solo, 1.4 ast, 0.70 sack, 0.42 PD, 0.00 INT |  |
| LB | Azeez Al-Shaair | 4.8 | 3.1 solo, 5.2 ast, 0.00 sack, 0.38 PD, 0.10 INT | Questionable |
| LB | Henry To'oTo'o | 4.4 | 1.8 solo, 3.5 ast, 0.13 sack, 0.24 PD, 0.00 INT |  |
| LB | Jake Hansen | 4.0 | 1.9 solo, 2.3 ast, 0.12 sack, 0.25 PD, 0.12 INT |  |
| DB | M.J. Stewart | 7.4 | 4.1 solo, 3.8 ast, 0.28 sack, 0.55 PD, 0.00 INT |  |
| DB | Kamari Lassiter | 7.0 | 4.5 solo, 1.9 ast, 0.15 sack, 0.86 PD, 0.08 INT |  |
| DB | Calen Bullock | 5.0 | 2.9 solo, 1.6 ast, 0.00 sack, 0.68 PD, 0.21 INT |  |

**LAC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Justin Herbert | 16.4 | 225 pass yd, 1.1 TD, 1.0 INT; 4.3 rush, 20 yd |  |
| RB | Omarion Hampton | 9.7 | 10.8 car, 39 yd, 0.42 TD; 1.8 rec, 12 yd, 0.06 TD |  |
| RB | Kimani Vidal | 6.3 | 5.5 car, 22 yd, 0.21 TD; 1.3 rec, 10 yd, 0.10 TD |  |
| RB | Keaton Mitchell | 6.3 | 4.9 car, 19 yd, 0.08 TD; 2.0 rec, 13 yd, 0.11 TD |  |
| WR | Ladd McConkey | 6.3 | 2.4 rec, 31 yd, 0.14 TD |  |
| WR | Tre Harris | 5.9 | 2.6 rec, 30 yd, 0.06 TD |  |
| WR | Quentin Johnston | 5.8 | 2.2 rec, 30 yd, 0.11 TD |  |
| WR | KeAndre Lambert-Smith | 2.9 | 1.3 rec, 12 yd, 0.07 TD |  |
| TE | Oronde Gadsden II | 5.6 | 2.5 rec, 23 yd, 0.14 TD |  |
| TE | Charlie Kolar | 4.1 | 1.9 rec, 18 yd, 0.05 TD |  |
| K | Cameron Dicker | 8.6 | 1.8 FG, 1.8 XP |  |
| DL | Justin Eboigbe | 3.0 | 1.5 solo, 1.7 ast, 0.18 sack, 0.00 PD, 0.00 INT |  |
| DL | Teair Tart | 1.9 | 1.3 solo, 1.1 ast, 0.00 sack, 0.09 PD, 0.00 INT |  |
| LB | Tuli Tuipulotu | 6.0 | 2.1 solo, 1.8 ast, 0.53 sack, 0.33 PD, 0.10 INT |  |
| LB | Daiyan Henley | 3.9 | 2.6 solo, 3.0 ast, 0.05 sack, 0.19 PD, 0.05 INT | Questionable |
| LB | Troy Dye | 3.8 | 1.9 solo, 1.1 ast, 0.14 sack, 0.27 PD, 0.00 INT |  |
| DB | Tony Jefferson | 4.6 | 2.7 solo, 2.3 ast, 0.00 sack, 0.26 PD, 0.07 INT |  |
| DB | Cam Hart | 4.3 | 2.1 solo, 1.5 ast, 0.00 sack, 0.69 PD, 0.25 INT |  |
| DB | Tarheeb Still | 4.0 | 2.2 solo, 1.5 ast, 0.00 sack, 0.48 PD, 0.15 INT |  |

### JAX @ BAL

Market: BAL +10.0, total 39.5. Sim: JAX 24.9, BAL 14.8. BAL wins 22.4%, JAX wins 77.6%. Median margin -9.9 for BAL.

| Team stat | JAX | BAL |
|---|---|---|
| Plays | 62 | 60 |
| Pass attempts / completions | 31 / 20 | 31 / 20 |
| Passing yards | 257 | 223 |
| Rush attempts / yards | 29 / 114 | 27 / 120 |
| Sacks taken | 2.0 | 2.0 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.5 / 1.2 | 0.8 / 0.8 |
| Field goals | 1.8 | 1.1 |

**JAX**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Trevor Lawrence | 20.4 | 257 pass yd, 1.5 TD, 0.6 INT; 3.7 rush, 15 yd |  |
| RB | Bhayshul Tuten | 9.5 | 13.9 car, 54 yd, 0.52 TD; 1.6 rec, 19 yd, 0.18 TD | Questionable |
| RB | Chris Rodriguez Jr. | 6.3 | 7.1 car, 29 yd, 0.43 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| RB | Ameer Abdullah | 1.6 | 2.5 car, 9 yd, 0.05 TD; 0.2 rec, 2 yd, 0.00 TD |  |
| WR | Parker Washington | 12.0 | 4.1 rec, 59 yd, 0.32 TD |  |
| WR | Jakobi Meyers | 9.6 | 3.8 rec, 45 yd, 0.21 TD |  |
| WR | Brian Thomas Jr. | 5.1 | 1.9 rec, 22 yd, 0.17 TD |  |
| WR | Josh Cameron | 3.3 | 1.2 rec, 15 yd, 0.11 TD |  |
| TE | Brenton Strange | 9.6 | 4.0 rec, 46 yd, 0.19 TD |  |
| TE | Nate Boerkircher | 3.3 | 1.1 rec, 13 yd, 0.15 TD |  |
| K | Cam Little | 8.6 | 1.6 FG, 2.5 XP |  |
| DL | Josh Hines-Allen | 4.1 | 2.0 solo, 1.3 ast, 0.33 sack, 0.15 PD, 0.00 INT |  |
| DL | Travon Walker | 2.3 | 1.3 solo, 1.4 ast, 0.35 sack, 0.11 PD, 0.00 INT | Questionable |
| LB | Foyesade Oluokun | 7.2 | 4.1 solo, 3.5 ast, 0.14 sack, 0.27 PD, 0.16 INT |  |
| LB | Ventrell Miller | 4.1 | 2.2 solo, 2.1 ast, 0.06 sack, 0.36 PD, 0.04 INT |  |
| LB | Branson Combs | 2.7 | 1.4 solo, 0.8 ast, 0.06 sack, 0.28 PD, 0.14 INT |  |
| DB | Antonio Johnson | 5.0 | 2.9 solo, 1.4 ast, 0.08 sack, 0.36 PD, 0.15 INT |  |
| DB | Jalen Huskey | 4.7 | 1.0 solo, 2.0 ast, 0.91 sack, 0.00 PD, 0.00 INT |  |
| DB | Travis Hunter | 4.7 | 2.4 solo, 1.3 ast, 0.00 sack, 0.77 PD, 0.28 INT |  |

**BAL**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Joe Fagnano | 14.3 | 223 pass yd, 0.8 TD, 0.7 INT; 4.4 rush, 19 yd |  |
| RB | Derrick Henry | 13.7 | 18.1 car, 79 yd, 0.62 TD; 1.2 rec, 9 yd, 0.05 TD |  |
| RB | Justice Hill | 5.9 | 2.8 car, 14 yd, 0.04 TD; 2.3 rec, 16 yd, 0.05 TD |  |
| RB | Rasheen Ali | 1.2 | 1.0 car, 4 yd, 0.01 TD; 0.3 rec, 3 yd, 0.02 TD |  |
| WR | Zay Flowers | 13.9 | 5.4 rec, 68 yd, 0.25 TD |  |
| WR | Rashod Bateman | 4.8 | 2.0 rec, 25 yd, 0.06 TD |  |
| WR | Ja'Kobi Lane | 3.6 | 1.7 rec, 17 yd, 0.03 TD |  |
| WR | Devontez Walker | 2.2 | 0.8 rec, 10 yd, 0.07 TD |  |
| TE | Mark Andrews | 6.2 | 3.3 rec, 25 yd, 0.09 TD |  |
| TE | Josh Cuevas | 3.9 | 1.6 rec, 18 yd, 0.08 TD |  |
| DL | Nnamdi Madubuike | 3.2 | 1.8 solo, 1.6 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| DL | Travis Jones | 2.9 | 1.3 solo, 1.7 ast, 0.16 sack, 0.07 PD, 0.00 INT |  |
| LB | Roquan Smith | 7.4 | 3.9 solo, 4.1 ast, 0.18 sack, 0.31 PD, 0.05 INT |  |
| LB | Trenton Simpson | 5.6 | 3.2 solo, 3.0 ast, 0.14 sack, 0.08 PD, 0.08 INT |  |
| LB | Mike Green | 3.1 | 1.2 solo, 1.3 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| DB | Kyle Hamilton | 6.4 | 4.6 solo, 2.0 ast, 0.00 sack, 0.41 PD, 0.10 INT |  |
| DB | K'Von Wallace | 5.8 | 4.5 solo, 0.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DB | Malaki Starks | 4.9 | 3.2 solo, 2.4 ast, 0.06 sack, 0.16 PD, 0.00 INT |  |

### LA @ WAS

Market: WAS +4.5, total 48.0. Sim: LA 26.3, WAS 21.9. WAS wins 36.0%, LA wins 63.9%. Median margin -4.5 for WAS.

| Team stat | LA | WAS |
|---|---|---|
| Plays | 64 | 61 |
| Pass attempts / completions | 34 / 22 | 32 / 20 |
| Passing yards | 242 | 220 |
| Rush attempts / yards | 28 / 134 | 27 / 123 |
| Sacks taken | 2.5 | 2.1 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.7 / 1.2 | 1.2 / 1.1 |
| Field goals | 1.9 | 1.6 |

**LA**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Matthew Stafford | 19.1 | 242 pass yd, 1.7 TD, 0.7 INT; 1.4 rush, 6 yd |  |
| RB | Kyren Williams | 17.1 | 14.5 car, 68 yd, 0.61 TD; 3.3 rec, 27 yd, 0.14 TD |  |
| RB | Blake Corum | 10.4 | 10.1 car, 51 yd, 0.44 TD; 1.1 rec, 11 yd, 0.10 TD |  |
| WR | Puka Nacua | 21.6 | 0.8 car, 4 yd, 0.05 TD; 8.6 rec, 88 yd, 0.63 TD |  |
| WR | Konata Mumpfield | 3.7 | 1.4 rec, 17 yd, 0.11 TD |  |
| WR | Tutu Atwell | 2.5 | 1.0 rec, 13 yd, 0.04 TD |  |
| TE | Tyler Higbee | 8.2 | 3.4 rec, 36 yd, 0.21 TD |  |
| TE | Colby Parkinson | 5.0 | 2.7 rec, 25 yd, 0.24 TD | Questionable |
| K | Brandon McManus | 7.9 | 1.4 FG, 2.7 XP |  |
| DL | Braden Fiske | 2.2 | 1.1 solo, 0.9 ast, 0.21 sack, 0.00 PD, 0.00 INT |  |
| DL | Aaron Donald | 1.9 | 1.2 solo, 0.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Nate Landman | 6.3 | 4.0 solo, 3.1 ast, 0.04 sack, 0.12 PD, 0.03 INT |  |
| LB | Omar Speights | 4.9 | 3.1 solo, 2.0 ast, 0.16 sack, 0.22 PD, 0.00 INT |  |
| LB | Byron Young | 4.6 | 1.7 solo, 2.4 ast, 0.49 sack, 0.00 PD, 0.00 INT |  |
| DB | Quentin Lake | 8.0 | 4.0 solo, 2.9 ast, 0.00 sack, 1.21 PD, 0.40 INT |  |
| DB | Kamren Kinchens | 4.6 | 3.1 solo, 2.4 ast, 0.05 sack, 0.23 PD, 0.00 INT |  |
| DB | Josh Wallace | 4.3 | 2.7 solo, 1.1 ast, 0.00 sack, 0.61 PD, 0.13 INT |  |

**WAS**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Marcus Mariota | 16.7 | 220 pass yd, 1.2 TD, 0.6 INT; 3.0 rush, 14 yd |  |
| RB | Rachaad White | 12.2 | 10.2 car, 43 yd, 0.47 TD; 2.4 rec, 17 yd, 0.20 TD |  |
| RB | Austin Ekeler | 5.3 | 6.3 car, 27 yd, 0.15 TD; 0.9 rec, 8 yd, 0.03 TD |  |
| WR | Stefon Diggs | 10.5 | 4.3 rec, 39 yd, 0.38 TD |  |
| WR | Antonio Williams | 7.9 | 3.5 rec, 37 yd, 0.14 TD |  |
| WR | Treylon Burks | 5.0 | 2.3 rec, 33 yd, 0.20 TD | Questionable |
| WR | Dyami Brown | 2.8 | 1.3 rec, 13 yd, 0.04 TD |  |
| TE | Chig Okonkwo | 7.4 | 3.4 rec, 35 yd, 0.10 TD |  |
| TE | Ben Sinnott | 1.7 | 0.8 rec, 8 yd, 0.03 TD |  |
| K | Drew Stevens | 9.4 | 1.9 FG, 2.3 XP |  |
| DL | Dorance Armstrong | 3.8 | 1.8 solo, 1.7 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| DL | Shy Tuttle | 2.6 | 1.4 solo, 1.2 ast, 0.36 sack, 0.00 PD, 0.00 INT | Questionable |
| LB | Sonny Styles | 7.6 | 3.8 solo, 4.5 ast, 0.10 sack, 0.58 PD, 0.12 INT |  |
| LB | Frankie Luvu | 5.3 | 2.5 solo, 3.6 ast, 0.11 sack, 0.27 PD, 0.00 INT |  |
| LB | K'Lavon Chaisson | 4.7 | 1.8 solo, 1.3 ast, 0.55 sack, 0.00 PD, 0.00 INT |  |
| DB | Amik Robertson | 6.9 | 4.4 solo, 2.3 ast, 0.00 sack, 1.00 PD, 0.00 INT |  |
| DB | Jeremy Reaves | 5.8 | 3.7 solo, 2.7 ast, 0.00 sack, 0.54 PD, 0.07 INT |  |
| DB | Rasul Douglas | 5.5 | 3.2 solo, 0.9 ast, 0.00 sack, 0.90 PD, 0.34 INT |  |

### LV @ SF

Market: SF -10.0, total 52.5. Sim: LV 21.0, SF 31.2. SF wins 78.4%, LV wins 21.6%. Median margin +10.2 for SF.

| Team stat | LV | SF |
|---|---|---|
| Plays | 61 | 61 |
| Pass attempts / completions | 36 / 23 | 30 / 20 |
| Passing yards | 261 | 230 |
| Rush attempts / yards | 23 / 79 | 28 / 133 |
| Sacks taken | 2.1 | 2.4 |
| Interceptions thrown | 0.7 | 0.6 |
| Passing / rushing TDs | 1.4 / 0.9 | 1.9 / 1.5 |
| Field goals | 1.6 | 2.4 |

**LV**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Kirk Cousins | 19.1 | 261 pass yd, 1.4 TD, 0.7 INT; 2.0 rush, 6 yd |  |
| RB | Ashton Jeanty | 14.2 | 10.8 car, 35 yd, 0.37 TD; 3.9 rec, 37 yd, 0.19 TD |  |
| RB | Mike Washington Jr. | 5.0 | 7.6 car, 28 yd, 0.23 TD; 0.4 rec, 4 yd, 0.01 TD |  |
| RB | Dylan Laube | 1.2 | 0.5 car, 2 yd, 0.09 TD; 0.3 rec, 2 yd, 0.00 TD |  |
| WR | Tre Tucker | 8.9 | 3.2 rec, 42 yd, 0.23 TD |  |
| WR | Jalen Nailor | 4.3 | 1.9 rec, 17 yd, 0.12 TD |  |
| WR | Cody White | 3.1 | 1.1 rec, 13 yd, 0.12 TD |  |
| WR | Jack Bech | 2.7 | 1.1 rec, 12 yd, 0.07 TD |  |
| TE | Brock Bowers | 13.1 | 5.1 rec, 57 yd, 0.39 TD |  |
| TE | Michael Mayer | 8.2 | 3.8 rec, 37 yd, 0.12 TD |  |
| K | Matt Gay | 9.5 | 2.0 FG, 2.2 XP |  |
| DL | Maxx Crosby | 3.8 | 1.4 solo, 1.7 ast, 0.38 sack, 0.07 PD, 0.00 INT |  |
| DL | Malcolm Koonce | 2.7 | 0.9 solo, 0.6 ast, 0.38 sack, 0.00 PD, 0.00 INT |  |
| LB | Nakobe Dean | 8.6 | 4.0 solo, 6.1 ast, 0.11 sack, 0.24 PD, 0.14 INT |  |
| LB | Quay Walker | 6.1 | 3.0 solo, 4.6 ast, 0.23 sack, 0.00 PD, 0.00 INT |  |
| LB | Tommy Eichenberg | 2.4 | 1.4 solo, 1.6 ast, 0.00 sack, 0.19 PD, 0.00 INT |  |
| DB | Jeremy Chinn | 7.6 | 4.5 solo, 2.8 ast, 0.10 sack, 0.24 PD, 0.14 INT |  |
| DB | Treydan Stukes | 4.6 | 2.7 solo, 2.7 ast, 0.00 sack, 0.38 PD, 0.07 INT |  |
| DB | Eric Stokes | 4.2 | 2.8 solo, 1.1 ast, 0.06 sack, 0.39 PD, 0.00 INT |  |

**SF**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Brock Purdy | 22.3 | 230 pass yd, 1.9 TD, 0.6 INT; 4.0 rush, 19 yd |  |
| RB | Christian McCaffrey | 15.2 | 12.8 car, 60 yd, 0.89 TD; 4.5 rec, 33 yd, 0.22 TD | Questionable |
| RB | Kaelon Black | 6.6 | 7.8 car, 35 yd, 0.33 TD; 0.5 rec, 4 yd, 0.03 TD |  |
| RB | Kyle Juszczyk | 3.5 | 0.0 car, 0 yd, 0.00 TD; 1.2 rec, 11 yd, 0.19 TD |  |
| WR | Mike Evans | 8.3 | 3.8 rec, 52 yd, 0.34 TD | Questionable |
| WR | Deebo Samuel Sr. | 5.3 | 1.4 car, 8 yd, 0.04 TD; 2.1 rec, 23 yd, 0.26 TD | Questionable |
| WR | Jordan Watkins | 3.9 | 1.4 rec, 21 yd, 0.06 TD |  |
| WR | Brandin Cooks | 3.1 | 1.0 rec, 10 yd, 0.19 TD |  |
| TE | George Kittle | 12.8 | 4.8 rec, 52 yd, 0.47 TD |  |
| TE | Luke Farrell | 0.8 | 0.3 rec, 3 yd, 0.02 TD |  |
| K | Eddy Pineiro | 7.9 | 1.3 FG, 3.2 XP |  |
| DL | Gracen Halton | 4.3 | 1.5 solo, 0.9 ast, 0.46 sack, 0.17 PD, 0.00 INT |  |
| DL | Keion White | 3.0 | 0.9 solo, 1.1 ast, 0.44 sack, 0.03 PD, 0.00 INT |  |
| LB | Fred Warner | 8.7 | 4.8 solo, 5.2 ast, 0.05 sack, 0.40 PD, 0.00 INT |  |
| LB | Dre Greenlaw | 5.9 | 3.4 solo, 4.3 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Jaden Dugger | 4.7 | 3.3 solo, 1.6 ast, 0.19 sack, 0.00 PD, 0.00 INT |  |
| DB | Ji'Ayir Brown | 5.2 | 3.3 solo, 2.6 ast, 0.00 sack, 0.34 PD, 0.07 INT |  |
| DB | Renardo Green | 4.6 | 2.4 solo, 1.1 ast, 0.00 sack, 0.63 PD, 0.33 INT |  |
| DB | Malik Mustapha | 4.6 | 2.8 solo, 2.0 ast, 0.00 sack, 0.46 PD, 0.03 INT |  |

### NYG @ PHI

Market: PHI +3.0, total 38.5. Sim: NYG 20.7, PHI 17.8. PHI wins 40.8%, NYG wins 59.2%. Median margin -3.2 for PHI.

| Team stat | NYG | PHI |
|---|---|---|
| Plays | 62 | 62 |
| Pass attempts / completions | 30 / 19 | 32 / 20 |
| Passing yards | 204 | 198 |
| Rush attempts / yards | 30 / 127 | 27 / 118 |
| Sacks taken | 2.1 | 2.2 |
| Interceptions thrown | 0.6 | 0.7 |
| Passing / rushing TDs | 1.1 / 1.1 | 0.9 / 1.0 |
| Field goals | 1.6 | 1.3 |

**NYG**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Jameis Winston | 15.4 | 204 pass yd, 1.1 TD, 0.6 INT; 2.3 rush, 9 yd |  |
| RB | Cam Skattebo | 8.2 | 14.0 car, 61 yd, 0.49 TD; 1.1 rec, 9 yd, 0.03 TD | Questionable |
| RB | Devin Singletary | 6.4 | 5.5 car, 24 yd, 0.31 TD; 1.1 rec, 8 yd, 0.06 TD |  |
| RB | Najee Harris | 3.0 | 5.6 car, 22 yd, 0.12 TD; 0.1 rec, 1 yd, 0.00 TD |  |
| WR | Malik Nabers | 12.9 | 5.5 rec, 60 yd, 0.26 TD |  |
| WR | Malachi Fields | 4.9 | 1.9 rec, 24 yd, 0.11 TD |  |
| WR | Darnell Mooney | 2.8 | 1.1 rec, 11 yd, 0.05 TD |  |
| WR | Darius Slayton | 2.6 | 1.1 rec, 12 yd, 0.06 TD |  |
| TE | Isaiah Likely | 10.1 | 4.3 rec, 38 yd, 0.35 TD |  |
| TE | Theo Johnson | 2.6 | 1.0 rec, 12 yd, 0.08 TD |  |
| K | Dominic Zvada | 8.6 | 1.7 FG, 2.1 XP |  |
| DL | DJ Reader | 2.6 | 1.9 solo, 1.5 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| DL | Shelby Harris | 2.1 | 1.0 solo, 1.6 ast, 0.00 sack, 0.31 PD, 0.00 INT |  |
| LB | Arvell Reese | 8.5 | 5.3 solo, 2.5 ast, 0.23 sack, 0.51 PD, 0.13 INT |  |
| LB | Micah McFadden | 3.2 | 2.9 solo, 0.7 ast, 0.00 sack, 0.00 PD, 0.00 INT |  |
| LB | Abdul Carter | 2.5 | 1.2 solo, 1.5 ast, 0.32 sack, 0.00 PD, 0.00 INT | Questionable |
| DB | Jevon Holland | 5.6 | 2.9 solo, 1.7 ast, 0.00 sack, 0.52 PD, 0.29 INT |  |
| DB | Deonte Banks | 4.4 | 1.6 solo, 1.1 ast, 0.00 sack, 1.30 PD, 0.11 INT |  |
| DB | Greg Newsome II | 4.3 | 2.3 solo, 1.3 ast, 0.00 sack, 0.89 PD, 0.15 INT |  |

**PHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Tanner McKee | 13.8 | 198 pass yd, 0.9 TD, 0.7 INT; 3.4 rush, 15 yd |  |
| RB | Saquon Barkley | 12.5 | 22.4 car, 97 yd, 0.94 TD; 0.9 rec, 7 yd, 0.03 TD | Questionable |
| RB | Jaydon Blue | 1.2 | 0.0 car, 0 yd, 0.00 TD; 0.6 rec, 6 yd, 0.01 TD |  |
| WR | Makai Lemon | 7.5 | 3.7 rec, 29 yd, 0.15 TD |  |
| WR | DeVonta Smith | 6.2 | 3.7 rec, 36 yd, 0.17 TD | Questionable |
| WR | Dontayvion Wicks | 4.1 | 2.4 rec, 26 yd, 0.08 TD | Questionable |
| WR | Darius Cooper | 4.1 | 1.5 rec, 16 yd, 0.17 TD |  |
| TE | Dallas Goedert | 7.6 | 3.6 rec, 29 yd, 0.16 TD |  |
| TE | Eli Stowers | 2.8 | 1.3 rec, 14 yd, 0.03 TD |  |
| K | Jake Elliott | 4.7 | 1.2 FG, 1.8 XP | Questionable |
| DL | Jalen Carter | 4.3 | 1.1 solo, 1.6 ast, 0.47 sack, 0.44 PD, 0.00 INT |  |
| DL | Jordan Davis | 2.7 | 1.2 solo, 2.4 ast, 0.08 sack, 0.09 PD, 0.00 INT |  |
| LB | Zack Baun | 6.0 | 3.1 solo, 3.9 ast, 0.01 sack, 0.45 PD, 0.04 INT |  |
| LB | Jeremiah Trotter Jr. | 5.1 | 3.7 solo, 2.3 ast, 0.06 sack, 0.09 PD, 0.00 INT |  |
| LB | Jihaad Campbell | 3.7 | 3.1 solo, 2.7 ast, 0.06 sack, 0.06 PD, 0.00 INT | Questionable |
| DB | Andrew Mukuba | 5.8 | 3.6 solo, 2.6 ast, 0.00 sack, 0.28 PD, 0.10 INT |  |
| DB | Cooper DeJean | 5.3 | 3.1 solo, 2.4 ast, 0.00 sack, 0.63 PD, 0.12 INT |  |
| DB | Quinyon Mitchell | 4.8 | 3.2 solo, 0.9 ast, 0.00 sack, 0.88 PD, 0.09 INT |  |

### NYJ @ KC

Market: KC -10.0, total 47.5. Sim: NYJ 18.7, KC 28.8. KC wins 77.5%, NYJ wins 22.5%. Median margin +10.3 for KC.

| Team stat | NYJ | KC |
|---|---|---|
| Plays | 60 | 62 |
| Pass attempts / completions | 34 / 22 | 33 / 21 |
| Passing yards | 242 | 243 |
| Rush attempts / yards | 24 / 98 | 27 / 124 |
| Sacks taken | 2.0 | 2.2 |
| Interceptions thrown | 0.7 | 0.5 |
| Passing / rushing TDs | 1.3 / 0.8 | 1.8 / 1.3 |
| Field goals | 1.4 | 2.1 |

**NYJ**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Geno Smith | 16.8 | 242 pass yd, 1.3 TD, 0.7 INT; 1.9 rush, 7 yd |  |
| RB | Braelon Allen | 11.3 | 11.6 car, 52 yd, 0.42 TD; 2.1 rec, 13 yd, 0.05 TD |  |
| RB | Breece Hall | 4.5 | 7.1 car, 26 yd, 0.20 TD; 1.2 rec, 10 yd, 0.03 TD | Questionable |
| RB | Isaiah Davis | 2.7 | 2.0 car, 8 yd, 0.06 TD; 0.7 rec, 7 yd, 0.02 TD |  |
| WR | Garrett Wilson | 8.3 | 4.8 rec, 50 yd, 0.23 TD | Questionable |
| WR | Adonai Mitchell | 7.4 | 2.8 rec, 35 yd, 0.19 TD |  |
| WR | Omar Cooper Jr. | 6.7 | 2.3 rec, 32 yd, 0.21 TD |  |
| WR | Isaiah Williams | 4.0 | 1.6 rec, 16 yd, 0.12 TD |  |
| TE | Mason Taylor | 4.3 | 2.5 rec, 21 yd, 0.19 TD | Questionable |
| TE | Kenyon Sadiq | 4.2 | 1.8 rec, 18 yd, 0.08 TD |  |
| K | Jason Sanders | 9.3 | 2.0 FG, 1.9 XP |  |
| DL | Will McDonald IV | 3.3 | 1.1 solo, 1.0 ast, 0.41 sack, 0.00 PD, 0.00 INT |  |
| DL | Jowon Briggs | 3.2 | 1.3 solo, 2.4 ast, 0.20 sack, 0.00 PD, 0.00 INT |  |
| LB | Jamien Sherwood | 7.7 | 4.0 solo, 4.8 ast, 0.04 sack, 0.57 PD, 0.00 INT |  |
| LB | Demario Davis | 5.9 | 3.3 solo, 3.1 ast, 0.20 sack, 0.53 PD, 0.00 INT |  |
| LB | David Bailey | 5.0 | 2.7 solo, 1.9 ast, 0.69 sack, 0.12 PD, 0.00 INT | Questionable |
| DB | Dane Belton | 8.1 | 5.2 solo, 3.9 ast, 0.14 sack, 0.55 PD, 0.00 INT |  |
| DB | Minkah Fitzpatrick | 7.8 | 4.0 solo, 4.8 ast, 0.00 sack, 0.55 PD, 0.14 INT |  |
| DB | Azareye'h Thomas | 3.6 | 1.8 solo, 2.5 ast, 0.00 sack, 0.58 PD, 0.00 INT |  |

**KC**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Patrick Mahomes | 21.5 | 243 pass yd, 1.8 TD, 0.5 INT; 2.4 rush, 11 yd |  |
| RB | Kenneth Walker III | 19.6 | 17.1 car, 81 yd, 0.88 TD; 2.9 rec, 21 yd, 0.25 TD |  |
| RB | Emmett Johnson | 7.1 | 2.1 car, 9 yd, 0.06 TD; 1.9 rec, 28 yd, 0.19 TD |  |
| RB | Kareem Hunt | 4.1 | 4.3 car, 18 yd, 0.19 TD; 0.5 rec, 6 yd, 0.03 TD |  |
| WR | Xavier Worthy | 7.9 | 3.3 rec, 33 yd, 0.21 TD |  |
| WR | Rashee Rice | 7.6 | 3.8 rec, 40 yd, 0.37 TD | Questionable |
| WR | Jalen Royals | 2.7 | 1.0 rec, 9 yd, 0.12 TD |  |
| WR | Cyrus Allen | 2.5 | 1.0 rec, 12 yd, 0.05 TD |  |
| TE | Travis Kelce | 7.5 | 3.8 rec, 45 yd, 0.32 TD | Questionable |
| TE | Noah Gray | 4.8 | 1.8 rec, 20 yd, 0.17 TD |  |
| K | Harrison Butker | 9.7 | 1.8 FG, 2.9 XP |  |
| DL | George Karlaftis | 4.7 | 1.3 solo, 1.6 ast, 0.32 sack, 1.06 PD, 0.09 INT |  |
| DL | Chris Jones | 2.8 | 0.9 solo, 1.0 ast, 0.31 sack, 0.27 PD, 0.00 INT |  |
| LB | Nick Bolton | 7.7 | 4.6 solo, 5.1 ast, 0.05 sack, 0.26 PD, 0.05 INT |  |
| LB | Drue Tranquill | 6.1 | 3.7 solo, 3.7 ast, 0.00 sack, 0.18 PD, 0.00 INT |  |
| LB | Jack Cochrane | 2.8 | 1.2 solo, 1.6 ast, 0.00 sack, 0.11 PD, 0.12 INT |  |
| DB | Nohl Williams | 5.1 | 2.5 solo, 1.9 ast, 0.13 sack, 0.87 PD, 0.13 INT |  |
| DB | Chamarri Conner | 5.0 | 3.1 solo, 1.8 ast, 0.18 sack, 0.22 PD, 0.08 INT |  |
| DB | Mansoor Delane | 3.5 | 2.6 solo, 1.7 ast, 0.00 sack, 0.86 PD, 0.12 INT | Questionable |

### TB @ CHI

Market: CHI -6.0, total 47.5. Sim: TB 20.8, CHI 26.6. CHI wins 67.4%, TB wins 32.6%. Median margin +5.7 for CHI.

| Team stat | TB | CHI |
|---|---|---|
| Plays | 63 | 66 |
| Pass attempts / completions | 33 / 21 | 33 / 22 |
| Passing yards | 223 | 241 |
| Rush attempts / yards | 28 / 134 | 31 / 128 |
| Sacks taken | 2.6 | 2.1 |
| Interceptions thrown | 0.9 | 0.7 |
| Passing / rushing TDs | 1.3 / 1.0 | 1.5 / 1.4 |
| Field goals | 1.6 | 2.0 |

**TB**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Baker Mayfield | 16.1 | 223 pass yd, 1.3 TD, 0.9 INT; 2.0 rush, 10 yd |  |
| RB | Bucky Irving | 14.4 | 13.8 car, 65 yd, 0.50 TD; 2.4 rec, 17 yd, 0.17 TD |  |
| RB | Kenny Gainwell | 6.1 | 6.2 car, 31 yd, 0.12 TD; 1.8 rec, 15 yd, 0.14 TD | Questionable |
| RB | Sean Tucker | 2.0 | 2.1 car, 10 yd, 0.17 TD; 0.0 rec, 0 yd, 0.00 TD |  |
| WR | Chris Godwin Jr. | 9.9 | 4.4 rec, 44 yd, 0.18 TD |  |
| WR | Emeka Egbuka | 8.0 | 4.3 rec, 41 yd, 0.30 TD | Questionable |
| WR | Ted Hurst III | 6.1 | 2.1 rec, 28 yd, 0.18 TD |  |
| WR | Tez Johnson | 4.4 | 1.5 rec, 21 yd, 0.13 TD |  |
| TE | Cade Otton | 7.2 | 3.2 rec, 33 yd, 0.13 TD |  |
| TE | Payne Durham | 0.8 | 0.4 rec, 4 yd, 0.01 TD |  |
| K | Chase McLaughlin | 9.9 | 2.1 FG, 2.1 XP |  |
| DL | A'Shawn Robinson | 3.0 | 0.6 solo, 2.0 ast, 0.09 sack, 0.42 PD, 0.24 INT |  |
| DL | Vita Vea | 2.3 | 1.0 solo, 1.2 ast, 0.18 sack, 0.18 PD, 0.00 INT |  |
| LB | Josiah Trotter | 8.3 | 4.3 solo, 5.2 ast, 0.08 sack, 0.38 PD, 0.08 INT |  |
| LB | Alex Anzalone | 6.0 | 2.2 solo, 3.1 ast, 0.10 sack, 0.50 PD, 0.48 INT |  |
| LB | David Walker | 4.4 | 2.4 solo, 1.1 ast, 0.51 sack, 0.00 PD, 0.00 INT |  |
| DB | Jacob Parrish | 7.1 | 4.0 solo, 1.2 ast, 0.00 sack, 1.54 PD, 0.29 INT |  |
| DB | Keionte Scott | 5.4 | 3.7 solo, 1.4 ast, 0.15 sack, 0.56 PD, 0.00 INT |  |
| DB | Zyon McCollum | 5.1 | 2.6 solo, 0.8 ast, 0.00 sack, 0.94 PD, 0.33 INT |  |

**CHI**

| Pos | Player | IRFL pts | Stat line | Note |
|---|---|---|---|---|
| QB | Caleb Williams | 18.8 | 241 pass yd, 1.5 TD, 0.7 INT; 2.9 rush, 12 yd |  |
| RB | D'Andre Swift | 14.3 | 13.4 car, 52 yd, 0.72 TD; 2.7 rec, 19 yd, 0.08 TD |  |
| RB | Kyle Monangai | 5.2 | 7.5 car, 34 yd, 0.29 TD; 0.9 rec, 8 yd, 0.03 TD | Questionable |
| RB | Roschon Johnson | 4.8 | 3.5 car, 14 yd, 0.12 TD; 1.3 rec, 12 yd, 0.04 TD |  |
| WR | Luther Burden III | 14.2 | 0.7 car, 3 yd, 0.02 TD; 5.3 rec, 61 yd, 0.42 TD |  |
| WR | Rome Odunze | 8.4 | 3.4 rec, 45 yd, 0.10 TD |  |
| WR | Kalif Raymond | 6.4 | 2.9 rec, 25 yd, 0.17 TD |  |
| WR | Zavion Thomas | 1.9 | 0.9 rec, 8 yd, 0.03 TD |  |
| TE | Colston Loveland | 12.0 | 5.1 rec, 46 yd, 0.41 TD |  |
| TE | Sam Roush | 0.9 | 0.4 rec, 4 yd, 0.01 TD |  |
| K | Cairo Santos | 8.9 | 1.7 FG, 2.7 XP |  |
| DL | Jeffery Simmons | 8.5 | 3.1 solo, 3.0 ast, 0.99 sack, 0.99 PD, 0.00 INT |  |
| DL | Austin Booker | 4.8 | 2.2 solo, 1.1 ast, 0.48 sack, 0.28 PD, 0.00 INT |  |
| LB | Devin Bush | 6.0 | 3.6 solo, 2.2 ast, 0.29 sack, 0.09 PD, 0.00 INT |  |
| LB | T.J. Edwards | 4.1 | 2.1 solo, 1.5 ast, 0.02 sack, 0.38 PD, 0.14 INT |  |
| LB | D'Marco Jackson | 2.7 | 1.1 solo, 1.5 ast, 0.04 sack, 0.19 PD, 0.17 INT |  |
| DB | Dillon Thieneman | 6.2 | 3.2 solo, 3.0 ast, 0.22 sack, 0.52 PD, 0.09 INT |  |
| DB | Kyler Gordon | 4.4 | 1.2 solo, 0.4 ast, 0.70 sack, 0.22 PD, 0.00 INT |  |
| DB | Tyrique Stevenson | 3.7 | 2.6 solo, 1.1 ast, 0.00 sack, 0.63 PD, 0.00 INT |  |

Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: JAX: Patrick Mekari, JAX: Cam'Ron Silmon-Craig, JAX: Caleb Ransaw, JAX: Nick Mullens, JAX: Eric Murray, JAX: Dawuane Smoot, JAX: Austin Trammell, JAX: Emmanuel Ogbah, JAX: Anton Harrison, JAX: Austin Johnson, JAX: DaVon Hamilton, JAX: BJ Green II, BAL: David Ojabo, BAL: Lamar Jackson, BAL: Carl Jones, BAL: Jaylinn Hawkins, BAL: Tavius Robinson, BAL: Tyler Loop, BAL: Tyler Huntley, BAL: Chris Moore, BAL: Jovaughn Gwyn, BAL: Adisa Isaac, BAL: Jacob Hummel, BAL: Durham Smythe, CIN: McKinnley Jackson, CIN: Jake Browning, CIN: Bralyn Lux, CIN: Isaiah Foskey, CIN: Erick All, CIN: Howard Cross III, CIN: Andrei Iosivas, CIN: Jalen Davis, CIN: Ke'Shawn Williams, CIN: Tanner Hudson, CIN: Cashius Howell, CIN: Swayze Bozeman, ATL: JD Bertrand, ATL: Jack Nelson, ATL: Natrone Brooks, ATL: Brian Asamoah II, ATL: Ronnie Harrison, ATL: Zachariah Branch, ATL: Samson Ebukam, ATL: Jalon Walker, ATL: Bralen Trice, ATL: Yasir Abdullah, ATL: Khalil Herbert, ATL: Dylan Drummond, ATL: James Pearce Jr., ATL: Michael Jerrell, ATL: Jammie Robinson, DEN: Jonah Elliss, DEN: Kolbe Katsis, DEN: Tyler Badie, DEN: RJ Harvey, DEN: Pat Bryant, DEN: Cody Schrader, DEN: Michael Bandy, DEN: Sean Fresch, CAR: Marco Wilson, CAR: Jonathon Brooks, CAR: Cam Jackson, CAR: Xavier Legette, CAR: Krys Barnes, CAR: Jaycee Horn, CAR: Ja'Seem Reed, CAR: Thomas Incoom, CAR: Corey Thornton, CAR: Ikem Ekwonu, CAR: Mike Jackson, CAR: Taylor Moton, CAR: Nic Scourton, CAR: Akayleb Evans, CAR: LaBryan Ray, CAR: Jimmy Horn Jr., DAL: Curtis Robinson, DAL: Josh Butler, DAL: Jonathan Bullard, DAL: Malik Davis, DAL: James Mitchell, DAL: Jalen Thompson, DAL: Phil Mafah, DAL: Reddy Steward, DAL: Caelen Carson, DAL: Hakeem Adeniji, DAL: Marist Liufau, DAL: Trikweze Bridges, IND: Johnathan Edwards, IND: Eric Johnson, IND: Alec Pierce, IND: Arden Key, IND: Cameron Mitchell, IND: Nick Westbrook-Ikhine, IND: Carl Lawson, IND: Cam Taylor-Britt, IND: Danny Pinter, NYJ: Sterling Shepard, NYJ: Micheal Clemons, NYJ: Troy Reeder, NYJ: Samuel Womack, NYJ: Jamaal Pritchett, NYJ: T'Vondre Sweat, NYJ: Keidron Smith, NYJ: Max Mitchell, NYJ: Arian Smith, NYJ: Kingsley Jonathan, NYJ: Braiden McGregor, NYJ: David Onyemata, NYJ: Francisco Mauigoa, NYJ: Marcelino McCrary-Ball, NYJ: Brady Cook, NYJ: Eric Watts, NYJ: Ja'Sir Taylor, NYJ: Stone Smartt, NYJ: Jordan Clark, KC: Isiah Pacheco, KC: Shane Buechele, KC: Zacch Pickens, KC: Marcus Harris, KC: Justin Watson, KC: Brashard Smith, KC: Esa Pole, KC: Ethan Downs, KC: Tyquan Thornton, KC: Josh Simmons, KC: L'Jarius Sneed, KC: Cole Christiansen, DET: Terrion Arnold, DET: Ben Bartch, DET: Avonte Maddox, DET: Thomas Harper, DET: Tom Kennedy, DET: Nick Whiteside, DET: Devin White, DET: Jimmy Rolder, MIA: Ethan Bonner, MIA: Caleb Johnson, MIA: Julian Hill, MIA: Ryan Miller, MIA: De'Von Achane, MIA: Keith Cooper Jr., MIA: Zane Gonzalez, MIA: Rob Beal Jr., MIA: Liam Anderson, MIA: Quinton Bell, CLE: Gage Larvadain, CLE: Raheim Sanders, CLE: Jerome Ford, CLE: KT Leveston, CLE: Teven Jenkins, CLE: Ethan Pocic, CLE: Carsen Ryan, CLE: Alex Wright, CLE: Nathaniel Watson, CLE: Sam Kamara, CLE: Cedric Tillman, CLE: Myles Garrett, CLE: Brenden Bates, NO: Charlie Smyth, NO: Jalen Cropper, NO: Mason Tipton, NO: Jayden Price, NO: Dillon Radunz, NO: Jack Stoll, NO: Moliki Matavao, NO: Devin Neal, NO: Fadil Diggs, NO: Travis Etienne, NO: Kevin Austin Jr., NO: Jonah Williams, NO: Bryan Bresee, NO: Kelvin Banks Jr., NYG: Raheem Layne, NYG: Eric Gray, NYG: Braxton Berrios, NYG: Chauncey Golston, NYG: DJ Davidson, NYG: Jalin Hyatt, NYG: Dalen Cambre, NYG: Roy Robertson-Harris, NYG: Odell Beckham Jr., NYG: Elijah Chatman, NYG: Gunner Olszewski, NYG: Tyrone Tracy Jr., NYG: Jihad Ward, NYG: Jaxson Dart, NYG: Rico Payton, NYG: Tremaine Edmunds, NYG: Korie Black, NYG: Brian Burns, PHI: Zach Ertz, PHI: Keyshawn James-Newby, PHI: Brandon Johnson, PHI: Tank Bigsby, PHI: Will Shipley, PHI: Dameon Pierce, PHI: Jalen Hurts, PHI: Jakorian Bennett, PHI: Andre' Sam, PHI: E.J. Jenkins, PHI: Cole Wisniewski, PHI: Elijah Mitchell, LA: Darious Williams, LA: Joshua Karty, LA: Justin Dedich, LA: Derion Kendrick, LA: Tanner Ingle, LA: Kobie Turner, LA: Ahkello Witherspoon, LA: Dean Connors, LA: Xavier Smith, LA: Jaylen Watson, LA: Davante Adams, LA: Ronnie Rivers, LA: Blake Grupe, LA: Terrance Ferguson, LA: Jake McQuaide, LA: Poona Ford, WAS: Jer'Zhan Newton, WAS: Jeremy McNichols, WAS: Craig Reynolds, WAS: T.J. Maguranyanga, WAS: Tyler Biadasz, WAS: Drake Jackson, WAS: Ricky Barber, WAS: Jake Moody, WAS: Daron Payne, WAS: Austin Keys, WAS: Josh Johnson, WAS: Javontae Jean-Baptiste, WAS: Ale Kaho, WAS: Leo Chenal, WAS: Javon Kinlaw, WAS: Laremy Tunsil, WAS: Jaylin Lane, WAS: Jacory Croskey-Merritt, WAS: Terry McLaurin, WAS: Nick Bellore, HOU: Damone Clark, HOU: Jayden Higgins, HOU: David Montgomery, HOU: Jaylin Smith, HOU: E.J. Speed, HOU: Lewis Bond, HOU: Dylan Horton, HOU: Mario Edwards, HOU: British Brooks, HOU: Jamal Hill, HOU: Kenneth Murray, Jr., HOU: George Odum, HOU: Aiden Fisher, HOU: Myles Bryant, HOU: Bryce Hall, HOU: Jaylin Noel, HOU: Jawhar Jordan, LAC: Alec Ingold, LAC: Amar Johnson, LAC: Da'Shawn Hand, LAC: Jaret Patterson, LAC: Daniel Brunskill, LAC: David Njoku, LAC: Rashawn Slater, LAC: Bobby Hart, LAC: Trey Pipkins, LAC: Patrick Herbert, LAC: Derwin James, LAC: Austin Deculus, LAC: Denzel Perryman, LAC: Trevor Penning, LAC: Trey Lance, LV: Jamal Adams, LV: Chigozie Anusiem, LV: Tim Keenan III, LV: Darnay Holmes, LV: Shedrick Jackson, LV: Zamir White, LV: Patrick Johnson, LV: Carter Runyon, LV: Greedy Vance, LV: Cian Slone, LV: Deven Thompkins, LV: Jon Rhattigan, SF: Kalia Davis, SF: Isaac Guerendo, SF: Sam Okuayinonu, SF: Alfred Collins, SF: Jalen Graham, SF: Demarcus Robinson, SF: KhaDarel Hodge, SF: Ricky Pearsall, SF: Jake Tonges, SF: Eric Kendricks, SF: Ogbo Okoronkwo, SF: C.J. West, SF: Nick Martin, GB: Drake Dabney, GB: Shemar Bartholomew, GB: John FitzPatrick, GB: Collin Oliver, GB: Chris Brooks, GB: Micah Parsons, GB: Javon Hargrave, GB: Jacob Monk, GB: Nate Hobbs, GB: Jayden Reed, GB: Jonathan Ford, GB: Arron Mosby, GB: Luke Musgrave, GB: Skyy Moore, GB: Zach Bako-Bewele, GB: Johnathan Baldwin, GB: Edgerrin Cooper, GB: Warren Brinson, NE: Jack Westover, NE: Alijah Vera-Tucker, NE: Terrell Jennings, NE: Harold Landry III, NE: K.J. Britt, NE: Quintayvious Hutchins, NE: Dell Pettus, NE: Reggie Gilliam, NE: Jose Ramirez, NE: Mike Onwenu, NE: Romeo Doubs, NE: Mack Hollins, NE: Chad Muma, NE: Bradyn Swinson, NE: Eric Gregory, NE: Jeremiah Pharms Jr., ARI: Jalen Brooks, ARI: Jeremiyah Love, ARI: BJ Ojulari, ARI: Zachary Carter, ARI: PJ Mustipher, ARI: Paris Johnson Jr., ARI: Elijah Jones, ARI: Kenny Yeboah, ARI: Will Johnson, ARI: Kendrick Bourne, ARI: Art Green, ARI: Jared Harrison-Hunte, ARI: Wydett Williams Jr., ARI: Jaden Davis, ARI: Isaiah Adams, ARI: Hunter Long, SEA: Coby Bryant, SEA: Robbie Ouzts, SEA: Montorie Foster Jr, SEA: Sam Darnold, SEA: Julian Neal, SEA: Elijah Arroyo, SEA: Trevon Diggs, SEA: Jimmy Ciarlo, SEA: AJ Finley, SEA: Jake Bobo, TB: Josh Williams, TB: Josh Hayes, TB: Mike Jordan, TB: Chris Braswell, TB: Devin Culp, TB: Yaya Diaby, TB: Christian Rozeboom, TB: Markees Watts, TB: Jalen McMillan, CHI: Joe Tryon-Shoyinka, CHI: Buddy Johnson, CHI: Cole Kmet, CHI: Nikola Kalinic, CHI: Dayo Odeyingbo, CHI: Beau Gardner, CHI: Braxton Jones, CHI: Kaden Davis, CHI: Brittain Brown, BUF: Tyrell Shavers, BUF: Shaq Thompson, BUF: Keonta Jenkins, BUF: Tre'Davious White, BUF: Kani Walker, BUF: Trent Sherfield, BUF: Mecole Hardman, BUF: Jordan Hancock, BUF: Frank Gore Jr., BUF: Geno Stone, BUF: Andre Jones Jr., BUF: Phidarian Mathis, MIN: Ty Chandler, MIN: Josh Oliver, MIN: Donovan Jackson, MIN: Tavierre Thomas, MIN: Jeshaun Jones, MIN: C.J. Ham, MIN: Ben Sims, MIN: DeeJay Dallas, MIN: Tyler Batty, MIN: Taki Taimani.

## 8. DraftKings and FanDuel

Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, -1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. The tool that builds them is `dfs_optimize.py` and it is ready for that file.

**Top projected, DraftKings**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 21.1 | 8.3 to 34.5 |
| QB | Jared Goff | DET | 20.2 | 7.9 to 33.2 |
| QB | Dak Prescott | DAL | 20.2 | 8.3 to 34.1 |
| QB | Drake Maye | NE | 20.0 | 7.8 to 33.6 |
| QB | Brock Purdy | SF | 19.7 | 7.5 to 33.3 |
| QB | Patrick Mahomes | KC | 19.0 | 7.0 to 32.2 |
| RB | Jahmyr Gibbs | DET | 27.6 | 11.1 to 45.6 |
| RB | Bijan Robinson | ATL | 21.4 | 7.8 to 36.1 |
| RB | Kenneth Walker III | KC | 20.5 | 7.2 to 35.3 |
| RB | Kyren Williams | LA | 17.6 | 5.8 to 31.3 |
| RB | Chase Brown | CIN | 17.4 | 6.3 to 30.1 |
| RB | Jonathan Taylor | IND | 16.1 | 4.7 to 29.6 |
| RB | Chuba Hubbard | CAR | 16.1 | 5.0 to 29.1 |
| RB | Javonte Williams | DAL | 15.6 | 3.7 to 29.2 |
| RB | Christian McCaffrey | SF | 15.5 | 0.0 to 32.6 |
| RB | James Cook | BUF | 15.0 | 4.0 to 28.0 |
| WR | Puka Nacua | LA | 22.7 | 8.2 to 38.8 |
| WR | Jaxon Smith-Njigba | SEA | 20.8 | 6.6 to 36.5 |
| WR | CeeDee Lamb | DAL | 17.9 | 5.2 to 33.4 |
| WR | Ja'Marr Chase | CIN | 16.5 | 4.9 to 30.3 |
| WR | Tee Higgins | CIN | 16.0 | 4.2 to 30.3 |
| WR | Luther Burden III | CHI | 14.7 | 3.9 to 27.7 |
| WR | Zay Flowers | BAL | 14.5 | 3.9 to 27.7 |
| WR | Justin Jefferson | MIN | 14.1 | 3.6 to 26.9 |
| WR | Drake London | ATL | 13.6 | 3.0 to 26.9 |
| WR | Chris Olave | NO | 13.5 | 3.6 to 26.2 |
| WR | Tetairoa McMillan | CAR | 13.5 | 3.4 to 26.1 |
| WR | Amon-Ra St. Brown | DET | 13.4 | 0.0 to 30.2 |
| TE | Trey McBride | ARI | 18.6 | 7.1 to 32.8 |
| TE | Brock Bowers | LV | 13.5 | 3.0 to 26.3 |
| TE | George Kittle | SF | 13.1 | 2.8 to 25.0 |
| TE | Colston Loveland | CHI | 12.3 | 2.5 to 23.8 |
| TE | Harold Fannin Jr. | CLE | 11.8 | 2.1 to 23.6 |
| TE | T.J. Hockenson | MIN | 11.3 | 2.2 to 22.3 |

**Top projected, FanDuel**

| Pos | Player | Team | Avg | 10th to 90th |
|---|---|---|---|---|
| QB | Joe Burrow | CIN | 20.0 | 8.5 to 32.7 |
| QB | Dak Prescott | DAL | 19.2 | 8.4 to 31.9 |
| QB | Brock Purdy | SF | 19.1 | 7.6 to 32.0 |
| QB | Drake Maye | NE | 19.1 | 7.9 to 31.9 |
| QB | Jared Goff | DET | 19.1 | 8.0 to 31.1 |
| QB | Patrick Mahomes | KC | 18.3 | 7.1 to 30.6 |
| RB | Jahmyr Gibbs | DET | 23.8 | 9.2 to 40.2 |
| RB | Bijan Robinson | ATL | 18.5 | 7.0 to 31.2 |
| RB | Kenneth Walker III | KC | 18.2 | 6.2 to 31.9 |
| RB | Kyren Williams | LA | 15.4 | 4.7 to 27.7 |
| RB | Chase Brown | CIN | 14.8 | 4.9 to 26.4 |
| RB | Jonathan Taylor | IND | 14.5 | 3.9 to 26.8 |
| RB | Javonte Williams | DAL | 14.3 | 3.3 to 26.7 |
| RB | Chuba Hubbard | CAR | 14.1 | 4.1 to 25.6 |
| RB | James Cook | BUF | 13.6 | 3.7 to 25.7 |
| RB | Christian McCaffrey | SF | 13.3 | 0.0 to 28.8 |
| WR | Puka Nacua | LA | 17.3 | 5.6 to 30.3 |
| WR | Jaxon Smith-Njigba | SEA | 16.2 | 4.9 to 29.0 |
| WR | CeeDee Lamb | DAL | 13.9 | 3.4 to 26.1 |
| WR | Ja'Marr Chase | CIN | 12.7 | 3.1 to 23.4 |
| WR | Tee Higgins | CIN | 12.5 | 3.0 to 23.3 |
| WR | Luther Burden III | CHI | 11.6 | 2.6 to 21.9 |
| WR | Zay Flowers | BAL | 11.2 | 2.7 to 21.0 |
| WR | Justin Jefferson | MIN | 11.1 | 2.1 to 21.9 |
| WR | Drake London | ATL | 10.6 | 2.1 to 20.6 |
| WR | Tetairoa McMillan | CAR | 10.4 | 2.2 to 20.1 |
| WR | Jameson Williams | DET | 10.4 | 1.2 to 21.2 |
| WR | Chris Olave | NO | 10.3 | 2.2 to 20.3 |
| TE | Trey McBride | ARI | 13.3 | 4.3 to 23.8 |
| TE | Brock Bowers | LV | 10.6 | 1.9 to 20.7 |
| TE | George Kittle | SF | 10.4 | 1.6 to 20.5 |
| TE | Colston Loveland | CHI | 9.5 | 1.4 to 19.2 |
| TE | Harold Fannin Jr. | CLE | 9.4 | 1.2 to 19.3 |
| TE | T.J. Hockenson | MIN | 8.9 | 1.1 to 18.3 |
| K | Ka'imi Fairbairn | HOU | 10.0 | 1.0 to 21.6 |
| K | Tyler Bass | BUF | 9.6 | 1.0 to 20.0 |
| K | Brandon Aubrey | DAL | 9.5 | 2.0 to 20.0 |
| K | Will Reichard | MIN | 9.4 | 1.0 to 21.0 |

## 9. Limits

- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.
- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.
- Injury statuses came from MFL at the time of the pull. Re-run Thursday morning and Sunday morning for fresh news.
- Weather, referee tendencies and in-game injuries are not modeled.