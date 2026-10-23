# IRFL Week 7 lineup (Caerellius Lions, 0012) - 2026-10-21
Decision support only. Zac sets the lineup by hand on MFL.
Data: fresh MFL roster/injuries/projections pulled 2026-10-21 ~3 PM ET; sim re-run (10,000 sims, wk7_odds.json) so injuries are current. Byes this week: BUF, JAX, LAC, WAS.

## EXPECTED lineup (sim mean 149.6, 10th 111.9, 90th 189.4; MFL projection for same 17: 147.5)
| Slot | Player | Mean | 10th-90th |
|---|---|---|---|
| QB | Goff (DET) | 21.1 | 6.4-37.8 |
| RB | B. Robinson (ATL) | 7.7 | 0.4-17.1 |
| RB | Dowdle (PIT) | 6.6 | 0.9-13.5 |
| WR | Flowers (BAL) | 14.7 | 4.1-26.6 |
| WR | J. Jefferson (MIN) | 13.9 | 3.0-26.5 |
| WR | Ja. Williams (DET) | 10.8 | 1.5-21.3 |
| WR | Golden (GB) | 10.6 | 1.4-21.1 |
| TE | LaPorta (DET) | 9.5 | 1.2-19.3 |
| PK | Bates (DET) | 9.6 | 2.0-20.0 |
| DL | Hutchinson (DET) | 5.5 | 1.0-10.5 |
| DL | Wonnum (DET) | 5.4 | 1.0-11.0 |
| DL | T. Robinson (BAL) | 4.9 | 1.0-9.5 |
| LB | Okereke (CAR) | 8.1 | 3.0-14.0 |
| LB | Gibbens (ARI) | 5.1 | 2.0-9.0 |
| LB | Strnad (DEN) | 5.0 | 1.5-9.0 |
| DB | Reed (DET) | 5.7 | 2.0-10.0 |
| DB | N. Scott (CAR) | 5.7 | 2.0-10.0 |

SAFE (mean 149.6, 10th 111.5, MFL proj 150.5) and UPSIDE (mean 149.6, 90th 189.4) are the same 17 with two exceptions: SAFE swaps T. Robinson (DL) for Sanker (NOS, DB), i.e. a 2 DL / 3 LB / 3 DB split. UPSIDE is identical to EXPECTED (Wonnum/Hutchinson order only). Differences are noise-level (0.1 pt).

## Close calls (starter vs best bench)
- DL3 T. Robinson 4.9 vs Sanker (as DB3) 4.8: coin flip, 0.1.
- PK Bates 9.6 vs McPherson 8.7 vs Folk 8.4: 0.9.
- DB2 Scott 5.7 vs Sanker 4.8 / Kinchens 4.7 / Moss 4.7: 0.9.
- WR4 Golden 10.6 vs Allen 9.2 (1.4) vs Flournoy 8.2.
- LB3 Strnad 5.0 vs Barton 3.5: 1.5 (Gibbens 5.1 is in the same tier).
- TE LaPorta 9.5 vs Schultz 8.2: 1.3.
- RB2 Dowdle 6.6 vs Spears 4.6 (questionable): 2.0.
- QB Goff 21.1 vs C. Williams 18.7: 2.4. Note MFL's own projection ranks Goff 24.8, Williams 24.2, Brissett 23.9, so the sim is lower and flatter than MFL.

## Bench
C. Williams, Brissett, Spears (Q), M. Carter, Demercado, Allen, Flournoy, Ridley (1.9), Schultz, Hockenson (Q), McPherson, Folk, Davis (Q), Kancey, Barton, Dodson, Reid, Sanker, Kinchens, Moss, Mukuba, Jenkins, Anderson, Wright. Out of play: White and Croskey-Merritt (WAS bye / IR), Molden (LAC bye), Andersen (FA, no team), Shepard (FA). IR/taxi/suspended not eligible.

## MFL lineup currently set vs optimizer
MFL shows: C. Williams, B. Robinson, R. White, Allen, Flowers, Golden, Ridley, Goedert, Folk, J. Davis, T. Robinson, Gibbens, Okereke, Strnad, Jenkins, Kinchens, Sanker.
- Rachaad White is on a WAS bye (0 points) and is the biggest hole. Ridley (1.9) is weak too.
- Sim mean 117.1 (MFL projection 129.4) vs 149.6 for EXPECTED. EXPECTED beats it in 85% of simulated weeks, average gain +32.6.
- Moves: White out for Dowdle, Ridley out for Jefferson and Williams (WR slots), Williams for Goff at QB, Goedert for LaPorta, Folk for Bates, Davis (Q) for Hutchinson/Wonnum, Jenkins/Kinchens/Sanker for Reed/Scott. If MFL's saved lineup is only an auto-fill default, none of this has been set yet.

## Opponent and win probability
Week 7 opponent: Plautianus Chiefs (0010). MFL's own matchup spread has Zac -24.9.
Their currently set lineup includes Josh Allen (BUF bye), Rousseau (BUF bye), McLaurin (WAS bye, MFL Out), Walker (JAX bye) and McConkey (LAC bye, Q). Their QBs on the roster (Allen, Lawrence) are both on byes. Sim mean for their set lineup 111.8 (sd 22.9).
Win probability: EXPECTED 84.5%, SAFE 84.3%, UPSIDE 84.5%, current MFL sheet 56.8%. Caveat: this is against their lineup as set today; they can still change it, and my web check of their players was not done.

## Status checks (current-info rule)
Web searches returned mostly 2025-season or undated pages. Nothing below is confirmed for the 2026 Week 7 report.
- Golden (GB): on active roster per MFL (activated, per TASKS 10/15). Snap share and role for 2026 Week 7: unconfirmed.
- Sanker (NOS S) and T. Robinson (BAL DE): rostered (new, salary 10, no contract year - the FA bids). Search found only 2025 items, including a 2025 broken foot for Robinson. 2026 Week 7 status: unconfirmed. Confirm both are active before kickoff. Robinson is the one to check, he is a DL starter in EXPECTED.
- J. Davis (PHI DT, MFL: Questionable, ankle), Spears (TEN RB, Questionable, undisclosed), Hockenson (MIN TE, Questionable, concussion), Andersen (FA LB, Questionable, knee): no clear recent source found. Flagged, not guessed. Davis is on the MFL sheet but the optimizer does not start him.
- Everyone else: MFL injury export shows no designation, but depth chart and snap role not independently verified.
- Friday/Sunday checks: Davis, Spears, Hockenson statuses; T. Robinson and Sanker activity; Goff and Jefferson (MIN) any late tag; re-run run_week.py 2026 7 and optimize.py Sunday morning.

## Model limits
No offensive coordinator column (play-caller not captured for defensive-minded HCs); first-year coaches lean on team history; injury news only as fresh as the MFL export; single-game output is noisy (backtest only 3-6% better than a recent average for QB/RB/WR/TE/K, tie on IDP); kickers use a flat 3.75 per FG. Sim is market-anchored. Sim means run lower than MFL projections (Goff, Jenkins notably).

## Files changed
optimize.py and roster_compare.py got optional --roster (and --sheet in optimize.py); defaults still read wk6_roster.json. Week 7 roster: D:\WKP\scratch\wk7_roster.json. Pre-rerun sim backup: D:\WKP\scratch\wk7_bak\.
