# DraftKings Week 11: Explainer and Runbook

Early games only, 7 lineups at $1. Built 2026-11-19. Decision support only: Zac enters, Zac pays, Zac uploads. No agent logs in to DraftKings.

Where things live: every DraftKings file stays in `D:\Draft Kings\Week 11\` (outside the repo). This document holds method only, no player lines.

## Part 1. The friend's method in one page

**The big idea.** Treat your 7 lineups like a small investment mix, not one perfect lineup. A few safe popular players keep the floor up. A few low-owned players give you the shot at first place.

**Step by step, the way he does it.**
1. **Start from his projection file.** One row per player with points, price and how popular the player will be.
2. **Build a chalk pool.** Chalk means the players most people will use. Take the 6 most popular RBs, WRs and TEs, plus the 6 highest projected at each spot. Every lineup uses some of these.
3. **Pick the QB carefully.** Never a QB under $5,000. A low-owned QB has to pass a gate: confirmed starter, his team expected to score 21 or more, a top-12 ceiling, and facing a defense outside the top 8. He says QB choice is where money is won or lost.
4. **Stack.** Pair the QB with his own receivers. Add one player from the other team (a bring-back) when the game should be high scoring. Never 3 or more bring-backs.
5. **Do not force players.** Use caps and limits, not locks.
6. **Timing.** Rough set early, recheck when inactives land about 11:30 AM ET, final build about an hour before lock, then stop.
7. **Review every week.** Compare projected and real ownership, and how far each lineup was from the cash line.

**What each column in his file means.**

| Column | Plain meaning | How we use it |
|---|---|---|
| My Proj | Projected DraftKings points | Base score |
| Value | Points per $1,000 of salary | Shown, the sim handles price |
| My Own | Projected percent of the field using him | Chalk pool and leverage (lower = more leverage) |
| Saber Team | Vegas expected points for his team (not fantasy points) | QB gate (21 or more) |
| Saber Total | Vegas total for the whole game | Bring-back rule (high totals need a bring-back) |
| dk_25 to dk_99 percentile | Results of his 100,000 simulations per player. dk_50 is a middle game, dk_95 is a 1-in-20 big game | The heart of our simulation: each player's range |
| dk_std | How swingy the player is | Backup when percentiles are blank |
| dk_points | His simulation average (can differ from My Proj) | Not used |
| Status | O = out, D = doubtful, Q = questionable | O and D removed, Q kept and flagged |
| Adj Own, Min Exp, Max Exp, SS Proj, Live Proj, Actual | His tool's extras (Actual fills after games) | Not used |
| fd_, yahoo_, ob_ columns | FanDuel, Yahoo and other sites | Always ignored |

His sims give each player's range on his own. They do not say how players move together (a QB and his WR rise together). Our step adds that.

## Part 2. What our pipeline adds

Script: `D:\WKP\Fantasy-Football\dfs\dk_gpp.py`, checker `dk_validate.py` in the same folder. Plain Python (numpy and scipy) on Zac's PC. No paid service, no login.

1. **Slate filter.** Keeps only teams on the 1:00 PM ET Sunday games and drops any international game. The team list lives in `slate_week11.json`. If the DK salary file is there too, the script cross-checks every kickoff time.
2. **Correlated simulation, 20,000 slates.** Each player's score comes from the friend's percentile curve. We tie players together: a shootout lifts both sides, a QB moves with his own WR and TE, and a DST moves opposite the offense it faces. These tie-in weights are OUR assumption, not the friend's.
3. **Three lineup types**, built under the $50,000 cap:
   - **Core (2 lineups):** 5 or more chalk-pool players, QB plus 2 receivers, total ownership 200 percent or less.
   - **Balanced (2):** 4 or more chalk-pool players, total ownership 160 percent or less.
   - **Leverage (3):** QB must pass the gate and be under 15 percent owned, 2 or more players under 10 percent owned, total ownership 135 percent or less.
   - Every lineup: QB salary $5,000 or more, a low-owned QB must pass the gate, a bring-back when the game total is at or above the slate middle, no more than 2 bring-backs, no defense facing our own players, no more than 4 players from one team.
4. **Picking the 7.** In each simulated Sunday, a lineup "wins" if it beats the top 1 percent of all candidate lineups. A win counts less when many people would likely have the same lineup. Lineups are picked one by one to win in different Sundays. Limits: a player in at most 4 of 7, a QB in at most 2, any two lineups share at most 5 players.
5. **Fills the DK template** in row order and writes a plain upload file too.
6. **Checks the written file:** salary cap, every slot legal, no duplicate lineups, no player from a non-early team, every ID in the friend's file and the DK salary file, no player marked out, entry fee total.

## Part 3. Week 11 schedule check

The early slate is 7 games, all 1:00 PM ET Sunday 11/22: MIA at BUF, NO at CHI, TEN at DAL, TB at DET, ARI at KC, PIT at PHI, BAL at CAR. Source: ESPN Week 11 scoreboard, pulled 2026-11-18.

The only Week 11 international game is MIN at SF in Mexico City, Sunday 8:20 PM ET (NBC). It is not on the early slate. It is in the exclude list anyway. Sources: ESPN scoreboard (venue Estadio Banorte) and the NFL international games schedule (nfl.com, profootballhof.com).

## Part 4. Week 10 dry run results

Run on the Week 10 friend file. Outputs are in `D:\Draft Kings\Week 10\dryrun\` (`build_report.txt` has the lineups).

- **Filtering:** 356 rows in, 35 extra columns ignored, 53 out or doubtful players dropped, 115 playable players. All 14 teams on the 1:00 PM games; the DK salary file showed only 1:00 PM kickoffs. NE at DET (Munich, 9:30 AM) was not in the file and is on the exclude list.
- **Build:** 99 core, 119 balanced and 120 leverage candidate lineups, then 7 picked. 4 different QBs. Ownership sums 111 to 195 percent (the friend's 3 Week 10 lineups ran 167 to 222). 40 different players. Nobody in more than 4 of 7. Any two lineups share at most 3 players. Run time about 45 seconds.
- **Our simulation:** at least one of the 7 beat the top-1 percent line in 13.7 percent of 20,000 simulated Sundays. That is our model's number, not a real win rate.
- **Real DK template (3 entries):** filled, validation PASS, entry fees $3.00. The script warned that lineups 4 to 7 had no entry rows and put them in the plain upload file.
- **Mock 7-entry template (fake entry IDs, dry run only):** 7 filled, validation PASS, fees $7.00. Upload file also PASS.
- **Deliberately broken copy:** the checker caught all 4 breaks (duplicate lineup, over the cap, unknown ID, QB in an RB slot) and exited FAIL.
- **Not done:** scoring the dry-run lineups against real Week 10 points. Our local stats stop at Week 9 and the friend file's Actual column is blank.

**Template format, worked out from the Week 10 samples:** header `Entry ID, Contest Name, Contest ID, Entry Fee, QB, RB, RB, WR, WR, WR, TE, FLEX, DST`. One row per paid entry. Entry ID, Contest ID and fee come from DK and are never changed. Player cells hold the bare DK ID (Zac's Week 10 file used bare IDs). `--name-id` writes `Name (ID)` instead if DK ever asks for it. Entry fee in the Week 10 contest: $1 (NFL $15K First Down, 20 entry max, Early Only), so 7 entries = $7.

## Part 5. Rotowire verdict

**What it is good for:** one free page that shows every game's expected starters, Q and D tags, an inactives box per game, weather and the betting line. The inactives box fills in about 90 minutes before kickoff (11:30 AM ET for the early games). That is the 11:30 AM recheck in one screen.

**Pages checked on 2026-11-19:**
- `rotowire.com/football/lineups.php`: starters, injury tags, inactives box ("Not Yet Available" until announced), weather, spread and total. No paywall seen.
- `rotowire.com/football/inactives.php`: inactive lists per team as they come out. Says inactives come 90 minutes before kickoff. Subscribe banners, no paywall on the list.
- `rotowire.com/football/injury-report.php`: linked from those pages, not opened.

**What costs money:** the "Daily Fantasy (DFS and Picks)" plan has their optimizer (up to 300 lineups), their projections, ownership projections and news alerts for late scratches (RotoWire help center). I could not get a current price: the rates page did not load for me. Old search snippets showed several monthly figures, but I cannot confirm any of them. **Zac does not need the paid plan.** The friend's file already covers projections and ownership, and our script is the optimizer.

**How it fits:** Saturday, glance at the Q tags. Sunday 11:30 to 11:45 AM ET, open the lineups page and look at each early game's inactives box.

**Best free backups:**
1. Team X (Twitter) accounts and the NFL app: the official inactive list goes out 90 minutes before kickoff.
2. NFL.com injury reports: Friday afternoon game statuses (Out, Doubtful, Questionable) for Sunday.
3. Fantasy Alarm inactives page and RotoBaller inactives articles: free lists that update Sunday morning.
4. ESPN injury pages, for a second look.

## Part 6. Runbook (all times ET)

**Saturday 11/21**
1. **Morning, when the friend's file arrives.** Save it into `D:\Draft Kings\Week 11\` and keep his file name.
2. **On DraftKings (Zac only, this spends $7).** Open the early-only NFL contest. Enter it 7 times at $1 with any legal lineup (DK's own quick fill is fine, it gets replaced). Check: 7 entries, $7 total.
3. **Download the entries template.** DraftKings, then Lineups, then Edit Entries (or Upcoming), then Download. Save it into `D:\Draft Kings\Week 11\`. (I have not seen DK's current menus, so the button names may differ a little. It is the same download you did in Week 10.)
4. **Download the salary file.** On the contest page, Export to CSV (DKSalaries). Save it into the same folder. It lets the script check kickoff times and out tags.
5. **Run the build.** Tell Jarvis "build my DK lineups", or run this yourself (one line):
   `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\Fantasy-Football\dfs\dk_gpp.py --friend "D:\Draft Kings\Week 11\<friend file>.csv" --template "D:\Draft Kings\Week 11\<entries file>.csv" --dk-salaries "D:\Draft Kings\Week 11\<DKSalaries file>.csv" --slate "D:\Draft Kings\Week 11\slate_week11.json" --outdir "D:\Draft Kings\Week 11\sat"`
6. **Check the last lines of `build_report.txt`.** Both checks must say RESULT: PASS. If either says FAIL, do not upload.
7. **Upload.** DraftKings, then Lineups, then Edit Entries, then Upload, then pick the file ending in `- FILLED.csv`. Open the contest and confirm all 7 entries show the new lineups.
8. **Saturday evening.** Look at the Q players listed in the report against Friday's game statuses. Write down any that are now Out.

**Sunday 11/22**
1. **9:30 to 10:00 AM.** If the friend sends a new file, save it next to the old one (do not overwrite).
2. **10:00 to 11:00 AM.** Read the morning news for game-time decisions. Nothing to rebuild yet unless someone is ruled out.
3. **11:30 AM. Inactives drop.** Open the RotoWire lineups page or the team X accounts. Write down every player in our 7 lineups who is inactive.
4. **11:35 to 12:15 PM. Final build.** Download a fresh entries template (same entry IDs) and rerun step 5 with the newest friend file, output to `D:\Draft Kings\Week 11\sun`, plus the inactive names: `--out "Name One;Name Two"`. Add `--drop-q` if any Q player is still unclear. For only one or two swaps, editing those players by hand on DK is fine (DK lets you change any player until his game locks).
5. **By 12:30 PM.** Both checks PASS, upload, open the contest, confirm all 7 lineups.
6. **12:45 PM. Stop.** No more rebuilding (the friend's rule). Everything locks at 1:00 PM.

**Monday.** Send the final contest results (score per lineup, finish, cash line, winnings) so the tracker can be filled. The review step (`dfs_review.py`) is still built for 3 lineups and needs a small update for 7.

## Part 7. Questions for Zac

1. **Contest:** all 7 entries in one $1 early-only contest (Week 10 was the $15K First Down, 20 entry max), or split them the way the friend advises (single-entry and 3 to 5 max contests first)?
2. **Sunday file:** will the friend send an updated file Sunday morning, and about what time?
3. **Who runs Saturday:** should Jarvis run the build when you drop the files, or do you want to paste the one command yourself?
4. **Week 10 entries:** the file `entries ... (1).csv` holds a different 3 lineups than the friend's. Were those your entered lineups, and how did they finish? That starts the tracker.

## Notes and limits

- The tie-in weights in the simulation, the duplicate estimate and the 10 and 15 percent "low-owned" lines are our assumptions. They are stated in the script header.
- The defense-vs-QB part of the gate uses our local 2026 stats, which stop at Week 9. Refresh them before Saturday's build or that check is a week stale.
- Simulation tool: `dk_gpp.py` (numpy and scipy), 20,000 correlated slates, seed 11, 120 solves per lineup type. This agent ran on Opus 5.5. The numbers above are from that run only.
