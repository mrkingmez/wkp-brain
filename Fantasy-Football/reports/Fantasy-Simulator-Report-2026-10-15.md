# Fantasy Simulator Report - 15 OCT 2026

Built overnight on Zac's go. Decision support only: nothing was submitted anywhere.
Lock for Week 6 is Thursday 10/15 at 8:15 PM ET (Seattle at Denver).

## 1. What exists now

| Piece | What it does | Where |
|---|---|---|
| Play-by-play, 2023 to 2026 | Three-plus seasons of every NFL play, refreshed tonight | `D:\WKP\data\nfl\pbp\` |
| Coaching tendency table | Per coach: pass rate, pass over expected, red-zone mix, 4th-down aggression, how they change when trailing or leading, pace. Recent games count more. Thin samples are pulled toward league average. | `D:\WKP\data\ff-simulator\coach_tendencies_2026_wk6.csv` |
| Game simulator | Plays every game 4,000 times from the live betting line, turns the score script into pass and run volume using each coach's own habits, splits it among players, scores it with your IRFL rules (IDP included) | `D:\WKP\.claude\skills\ff-simulator\` |
| Lineup optimizer | Tries every legal slot split (17 starters, 8 IDP) and returns an EXPECTED, a SAFE and an UPSIDE lineup | same skill, `optimize.py` |
| Pick'em probabilities | Turns the gap between the frozen card number and today's market into a cover probability | `pickem_probs.py` |
| Tracker | Week 6 NFL picks logged (14 rows) | `Fantasy-Football\tracker\predictions.csv` |

Next Gen Stats is already in the data layer (added earlier tonight). Your gambler friend's method goes in on top of this tomorrow.

## 2. How good is it, honestly

Two real tests, both run only on information that existed before each game.

**Coaching model.** Predicting a team's early-down pass rate in a game, it beat the league average by 3 percent over 493 team-games (5 percent in 2026 alone) and beat a plain team average by 2 percent. Small but real. One game of play-calling is mostly noise, so do not expect miracles from coach habits alone. Their value is in the season-long traits: pace, pass over expected, 4th-down aggression.

**Full simulator, 18 weeks (2025 week 6 through 2026 week 5), 14,848 player-weeks.** Compared with simply averaging a player's recent games:
- QB, RB, WR, TE, K: simulator error about 3 to 6 percent lower than the plain average, once QBs who were replaced by injuries are set aside (a Thursday run knows about injuries, a backtest does not).
- Defenders (DL, LB, DB): a tie. Tackles and sacks are steady, and the simulation adds nothing the average does not already know.
- Ranges: after calibration, 80 to 82 percent of actual scores land inside the simulated 10th to 90th range for RB, WR, TE, DB, LB, DL. Before calibration it was 67 to 72 percent, too tight.
- The simulator still runs about 1.3 to 1.9 points light on RB, WR and TE who actually play. The blend that backtested best was 60 to 100 percent simulation and the rest recent average.

Plain read: it is a better decision tool than a projections table because it gives ceilings, floors and correlations. It is not a crystal ball, and it cannot find edges the betting market does not already price.

## 3. Week 6 lineup, simulation vs the sheet

Simulated averages (IRFL points):

| Lineup | Average | Beats the other |
|---|---|---|
| Simulation EXPECTED | 125.4 | in 79% of simulated weeks |
| Week 6 sheet lineup | 117.1 | |

The sim lineup differs from the sheet in four spots:

| Slot | Sheet | Simulation | Why |
|---|---|---|---|
| RB | Rachaad White (WAS) 5.9 | Brian Robinson (ATL) 8.4 | Robinson has 51 carries in 5 games this year, White 29 in 4 (White has more targets, 10 to 4). Atlanta's game total is 51. I have not checked team news on either back. |
| LB | Tyrel Dodson (CAR) 1.9 | Jack Gibbens (ARI) 5.3 | Gibbens: 13 solo and 22 assisted tackles in 5 games. Dodson has played 2 games this year (1 solo, 6 assisted). |
| DB | Jenkins (PIT) 3.4 and Mukuba (PHI) 3.1 | Nick Scott (CAR) 5.4 and Riley Moss (DEN) 3.6 | Moss is Questionable. SAFE lineup keeps Jenkins instead of Moss. |
| Rest | same | same | Brissett, Flowers, Allen, Flournoy, Schultz, Goedert, Folk, Davis, Kancey, Okereke, Strnad, Kinchens |

Other calls:
- **Quarterback: keep Brissett (18.1).** Caleb Williams comes out at 15.0 with a very wide range (Questionable, hamstring).
- **Matthew Golden (taxi):** if your league lets you activate him before lock he adds about 2.4 points (127.8 average). Worth doing only if it is free.
- **Defensive line is the weak spot.** Only Davis (3.1) and Kancey (0.7) are playable. Wonnum and Hutchinson are on bye. A waiver DL would likely add 2 to 4 points.
- **Questionable players** (Moss, Spears, Dowdle, Williams) play in 75 percent of simulated weeks.

Small honest caution: gains of a few points at one slot are inside the noise of one game. The RB and LB swaps are the two I would act on, because they are volume driven.

## 4. Week 6 pick'em, cover probabilities

Real NFL results land within about 12.7 points of the closing line (measured over 2,639 games). Using that:

| Game | Your pick | Card line | Market now | Cover chance |
|---|---|---|---|---|
| CHI at ATL | Atlanta +3.5 | CHI -3.5 | CHI -1.0 | 57.8% |
| CAR at PHI | Carolina +1.5 | PHI -1.5 | CAR -1.0 | 57.8% |
| BUF at LV | Las Vegas +6.5 | BUF -6.5 | BUF -4.5 | 56.2% |
| SEA at DEN | Denver +3.5 | SEA -3.5 | SEA -2.5 | 53.1% |
| BAL at CLE | Baltimore -4.5 | | BAL -5.0 | 51.6% |
| NO at NYG | NY Giants +1.5 | | NO -1.0 | 51.6% |
| Five games where card equals market (ARI-LAR, DAL-GB, HOU-JAX, PIT-TB, WSH-SF) | | | | 50.0% |
| TEN at IND, NYJ at NE, LAC at KC | | | half a point worse | 48.4% |

Expected result: about 7.2 ATS wins from the 14 NFL games, and 8.8 straight-up wins. No pick here is a lock; the three real edges are Atlanta, Carolina and Las Vegas because the frozen card sits 2 to 2.5 points away from today's market.

**Eliminator (market win chance):** LA Rams 83.7%, KC 73.5%, SF 72.2%, IND and NE 70.9%, BAL 65.3%. The Rams are still the safest. Check your used-teams list first; the tracker has no Eliminator history before this week.

## 5. Coaches worth knowing (as of week 6)

Most pass-heavy versus expectation: Zac Taylor CIN (+6.0), Andy Reid KC (+3.2), Sean McVay LA (+2.6), Jonathan Gannon ARI (+2.1).
Most run-leaning: John Harbaugh NYG (-6.5), Minter BAL (-6.3), Raheem Morris ATL (-6.3), Matt LaFleur GB (-4.9).

First-time head coaches this year (no history under their own name): Minter BAL, Monken CLE, Kubiak LV, Hafley MIA. Coaches with only one prior season as head coach: Ben Johnson CHI, Schottenheimer DAL, Coen JAX, Kellen Moore NO, Aaron Glenn NYJ. For these the model leans on the team's own recent plays and the league average, and says how much data sits behind each number.

Gap: nflverse does not tell us who calls the plays, so a head coach who hands play-calling to a coordinator is represented by the team's recent offense blended with him.

## 6. What is still open

1. Your gambler friend's FanDuel lineup source (tomorrow). Goes in as extra features.
2. A DraftKings / FanDuel salary-cap mode: needs that slate's salary file (the site's CSV download) and each site's scoring rules.
3. Tracker: only Week 1 and Week 6 are logged. Weeks 2, 3 and 5 pick docs exist; Week 4 has none. Logging them now would be after the fact, so they need a clearly labelled backfill and your OK.
4. Matthew Golden: can you activate a taxi player before lock?
5. Nothing from tonight is committed to git. All files are local.
