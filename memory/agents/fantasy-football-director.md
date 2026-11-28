# Lessons: fantasy-football-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\fantasy-football-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Refresh stats, odds, MFL, injuries and confirm starting QBs before every sim | evidence: memory\feedback-refresh-before-sims.md (Zac 2026-11-19) | CONFIRMED
- 2026-11-19 | First run after Wednesday practice reports, rerun Thursday and on any new info, report every change | evidence: memory\feedback-fantasy-timing.md | CONFIRMED
- 2026-11-19 | Keep the Week 10 Picks and Lineup phone doc layout every week | evidence: memory\feedback-fantasy-picks-format.md | CONFIRMED
- 2026-11-19 | A blank pick'em card is the trigger to produce picks; lineup calls need real research, not just projections | evidence: memory\topics\fantasy-football.md | NEW

## Lessons
- 2026-11-21 | After Thursday kickoff, mark that game's players locked: the sim still lists Schultz and Demercado as startable, so never offer them in a lineup or contingency | evidence: sim_2026_wk11_summary.csv rows vs HOU Thursday game | NEW
- 2026-11-21 | Web search for injury reports returns other seasons: check the date on every item and lean on the dated feeds (MFL, nflverse, ESPN) with the timestamp in the status line | evidence: nfl.com Week 11 page was 2025 | NEW
- 2026-11-22 | On a noon rerun, run the QB check before the build: the sim kept ARI on Beck until an override with Josh Johnson was set | evidence: ESPN feed 15:11Z | NEW

## DFS (own section, DFS only, never IRFL). Permanent record: `Fantasy-Football\dfs\LEARNING-LEDGER.md`
- 2026-11-22 | After every DFS slate score pool and entries from ESPN box scores (dashboard\dfs_live.py parse_game) when the local nflverse stats file lags, and write the row in LEARNING-LEDGER.md | evidence: stats_player_week_2026 held only the Thursday game; ESPN rebuild matched the 205.6 winner to the decimal | NEW
- 2026-11-22 | Do not blame exposure caps for a missed winner before checking the winner against the tier rules: Week 11 winner failed the ownership cap (207.7 vs 200) and chalk-pool minimum 5 (it had 4), not the caps | evidence: reports\Week11-DFS-After-Action-2026-11-22.md, caps loosened gave best 152.8 in every variant | NEW
- 2026-11-22 | Judge a rule change over 3 seeds, seed noise alone moves the 7-lineup mean about 10 points; the ownership-cap +60 test was better in 3 of 3 seeds (+9.5 avg), pool min 4 was mixed (+2.1) | evidence: wk11_backtest.py runs seeds 11, 12, 13 | NEW
- 2026-11-22 | Label every lineup with its source (model, rotowire, test and rule ID) and archive the exact entered file before lock: 5 of 7 Week 11 entries came from a patched scratch copy of dk_gpp.py | evidence: scratch\noon\dk_gpp_rw.py, build_sun6.log | NEW
- 2026-11-22 | Check seed notes against the entries file before repeating them: the Week 11 seed said Shakir was missing, he was in entry 5344796345 | evidence: DKEntries_week11_LINEUPS_UPLOAD.csv | CONFIRMED
- 2026-11-22 | Sub-$3,500 punts hit 13 or more about 12 percent of the time and the sim mean matched actual, so no punt rule; sim means are unbiased (bias +0.6, MAE 4.75), the miss was variance in the highest-total game | evidence: Week 11 after-action sections 2 and 4 | NEW
- 2026-11-22 | RotoWire injection is now an opt-in flag in dk_gpp.py (--rotowire csv, default off, flag-off output byte-identical to the pre-change file on Week 11 inputs); every build writes lineup_sources.csv (own, rotowire, patched) and archives the built file in entered_archive; copy any hand-patched uploaded file there too before lock | evidence: LEARNING-LEDGER.md section 7, regression run 2026-11-22 | NEW
- 2026-11-22 | Count every player across lineups and fix any chalk at 3 or more, and write the stats/injury/QB refresh with times, before a hand-off: the Week 11 noon note left a 4-lineup McBride exposure for Zac to cut and my self-drill failed criteria 1 and 2 | evidence: SOP\leveling\drills\fantasy-football-director-drill-1-result-2026-11-22.md, memory\agents\failures\fantasy-football-director.md (OPEN) | NEW
- 2026-11-22 | The DK official rules pages return 403 and nfl operations 404 to fetch: do not quote scoring or injury timing from memory, say NOT RETRIEVED and ask for the live DK page | evidence: craft brief section 4 | NEW
- 2026-11-24 | When the card writes favorites in mixed case and home in caps, convert to home-positive once and render the 'market now' column from the number, not by hand: I almost printed Colts -6.5 for a Giants-favored game | evidence: picks12.py, card row 21 | NEW
- 2026-11-24 | Thanksgiving week: first kickoff is Wed 8 PM ET (Odds API 2026-11-26T01:00Z), so rerun Wed noon and 6 PM ET; Sunday-team reports land Wed | evidence: Week 12 card | NEW
- 2026-11-25 | Pull the commissioner contract threads (messageBoardThread) for rules: R contracts last 3 years from taxi promotion, so Zac's 3 more seasons for Golden was really 2 | evidence: thread 6704138 | NEW
- 2026-11-25 | On a Wednesday rerun, query the ESPN league-wide injuries feed filtered to date 11/25 and to QBs: it surfaced the Pittsburgh Rudolph start that web search missed | evidence: Week 12 Wed rerun, #5 | NEW
- 2026-11-25 | Before grading any trade, compute the other side's cap room from MFL rosters first: a pending counter was $305 over the cap and could never process | evidence: Rebuild-Trade-Deadline-Plan-2026-11-25.md section 1 | NEW
- 2026-11-25 | Read the rendered MFL calendar page for the trade deadline: the raw TRADE event start and end are NFL week numbers, not dates | evidence: calfull.txt, Dec 3 8:15 PM ET | NEW
- 2026-11-25 | Never default to the card underdog on "no edge": the card is ATS, dogs and favorites cover equally (48.2 vs 49.4 on 800 picks) and dogs lose outright 66 percent; pick on line value of 1 point or more vs market first, then better team and healthier QB | evidence: Fantasy-Football\reports\Week12-Picks-REVISED-2026-11-25-wed.md, Zac complaint 2026-11-25 (18 of 20 dogs) | NEW
- 2026-11-25 | Grade every card the week it ends: 2026 cards were left green so no history existed; grade from nflverse games.parquet plus the card line and log it | evidence: 2026 NFL 80 of 147 ATS, Week 11 6 of 13 | NEW
- 2026-11-25 | Card lines 1+ point worse than the market for the pick hit 37.3 percent (n 169); 1+ better 55.1 percent (n 158); check this before keeping a frozen-line pick | evidence: same report | NEW
- 2026-11-25 | Card files: yellow = covered, red = did not cover, green = ungraded (verified against results); 2022 colors look unreliable | evidence: scratch\picks\g2.py | NEW
- 2026-11-25 | Check MFL player ids and contractYear first when Zac gives a vague contract number: $88 thru 2027 was Winfield | evidence: rosters.json | NEW
- 2026-11-25 | web search returns old-season injury items; the ESPN league injuries feed gave the dated Nacua, Penix and Williams status | evidence: espninj.json | CONFIRMED
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
