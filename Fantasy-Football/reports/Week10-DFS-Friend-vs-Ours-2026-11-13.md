# Week 10 DFS: Friend's three early lineups vs our three (Friday 2026-11-13)

Decision support only. Nothing was entered, nothing spent, no account touched. The friend's projections and ownership are his paid data: keep this file local.

## Headline

1. **Correction to your read:** the L2 WR "T. McMillan" is Tetairoa McMillan (Carolina, at NO, $6,700), not Terry McLaurin. Everything else you read from the three screenshots checked out (names, salaries, projections, ownership, stack labels). Totals on the screenshots: salary 49,800 / 49,900 / 49,800, his projection 138.0 / 134.3 / 134.0, ownership sum 205% / 189% / 167%.
2. **Only one QB gate failure, Mahomes (L3):** he misses the top-12 ceiling test (rank 14 of 61 in our sim). He passes the other four gate tests (salary, starter, implied total, opponent defense). See the gate table.
3. **Kenneth Walker III (L3 RB2, $9,200) is Questionable with a groin injury and did not practice** on the NFL.com Week 10 report (fetched 2026-11-13; the page does not state which day). Our own salary file and our status file did NOT flag him. That is a gap in our data and I have not fixed it (see the Walker section for the one-line change). L3 depends on him and on Mahomes in the same game.
4. **Overlap is heavy only on L3 vs our A (6 of 9).** L1 and L2 are far from each other (0 shared) and from ours (1 to 4). The most useful thing his three do for you is cover players we ignore: Jefferson, McMillan, Kelce, Pitts, Meyers, Walker, Hall, Tyson.
5. **Our sim ranks ours above his, but we built ours on that sim, so that ranking is flattered and is not evidence.** By his own projections the two sets are level (his L1 138.0 vs our A 138.2).

## The friend's three, verified against the screenshots

| Slot | L1 | L2 | L3 |
|---|---|---|---|
| QB | Josh Allen 7,500 (BUF at NYJ, 14%) | Tyler Shough 5,600 (NO vs CAR, 21%) | Patrick Mahomes 6,000 (KC at ATL, 11%) |
| RB | Chuba Hubbard 7,200 (33%) | Bijan Robinson 8,200 (36%) | Bijan Robinson 8,200 (36%) |
| RB | Ollie Gordon II 5,800 (17%) | Breece Hall 5,900 (13%) | Kenneth Walker III 9,200 (20%, Q) |
| WR | Drake London 6,600 (28%) | Tetairoa McMillan 6,700 (23%) | Laquon Treadwell 3,000 (4%) |
| WR | Tank Dell 3,900 (6%) | Jordyn Tyson 5,000 (12%) | Drake London 6,600 (28%) |
| WR | Jakobi Meyers 4,200 (19%, Q per our file) | Chris Olave 7,000 (28%) | Parker Washington 6,200 (18%) |
| TE | Tyler Warren 4,400 (31%) | Kyle Pitts Sr. 3,800 (16%) | Tyler Warren 4,400 (31%) |
| FLEX | Justin Jefferson 6,800 (32%) | Travis Kelce 4,700 (17%) | Greg Dulcich 3,300 (8%) |
| DST | Texans 3,400 (26%) | Colts 3,000 (22%) | Packers 2,900 (11%) |
| Salary | 49,800 | 49,900 | 49,800 |
| His proj | 138.0 | 134.3 | 134.0 |
| Own sum (screenshot) | 205% | 189% | 167% |
| Stack (his label) | none | QB+2 and 1 bring-back | QB+1 and 2 bring-backs |

Ownership note: our tool shows 212 / 194 / 171 for his lineups, not 205 / 189 / 167. The difference is our own rescale of the WR ownership after we removed scratched players from his file (documented in the Three Lines report, factor 1.081). Use the screenshot numbers as his, ours as the adjusted ones.

File typed from the screenshots: `D:\WKP\data\dfs-friend\friend_lineups_2026-11-13.txt` (real). The fake test file `D:\WKP\Fantasy-Football\dfs\friend_lineups_FAKE_TEST.txt` was not touched.

## Our three (for reference)

A (floor): Shough, Bijan, Gordon, Olave, London, Washington, Warren, Dulcich, Packers. B (balanced): Allen, Bijan, Hubbard, London, Shakir, Douglas, Warren, Dulcich, Colts. C (leverage): Lawrence, Bijan, Gordon, Watson, Washington, Douglas, Warren, Dulcich, Texans.

## Overlap

Players shared, of 9 (from dfs_compare.py):

| | Our A | Our B | Our C |
|---|---|---|---|
| Friend L1 | 3 (Gordon, London, Warren) | 4 (Allen, Hubbard, London, Warren) | 3 (Gordon, Warren, Texans) |
| Friend L2 | 3 (Shough, Bijan, Olave) | 2 (Bijan, Colts) | 1 (Bijan) |
| Friend L3 | 6 (Bijan, London, Washington, Warren, Dulcich, Packers) | 4 (Bijan, London, Warren, Dulcich) | 4 (Bijan, Washington, Warren, Dulcich) |

Between his own three: L1 and L2 share 0, L1 and L3 share 2 (London, Warren), L2 and L3 share 1 (Bijan).

Across all six lineups, how many contain each shared player: Bijan Robinson 5, Tyler Warren 5, Drake London 4, Greg Dulcich 4, Ollie Gordon II 3, Parker Washington 3, and two each for Allen, Shough, Hubbard, Olave, Texans, Colts, Packers.

Only on his side: Jefferson, McMillan, Walker, Meyers, Kelce, Pitts, Tyson, Hall, Mahomes, Dell, Treadwell. Only on ours: Lawrence, Watson, Shakir, Douglas.

## Salary, projection, ownership, sim

| Lineup | Salary | Proj (his file) | Own sum (tool) | Own avg | Chalk pool count | Sim avg | Sim p25 | Sim p90 |
|---|---|---|---|---|---|---|---|---|
| F1 | 49,800 | 138.0 | 212 | 23.6 | 5 | 120.9 | 101.1 | 157.8 |
| F2 | 49,900 | 134.3 | 194 | 21.6 | 5 | 108.8 | 88.7 | 146.5 |
| F3 | 49,800 | 134.0 | 171 | 19.0 | 6 | 117.0 | 95.0 | 158.1 |
| Our A | 50,000 | 138.2 | 204 | 22.6 | 6 | 127.4 | 106.1 | 167.7 |
| Our B | 49,900 | 136.8 | 187 | 20.8 | 5 | 127.3 | 107.0 | 165.4 |
| Our C | 50,000 | 130.5 | 164 | 18.2 | 5 | 129.0 | 106.9 | 170.5 |

**Say it plainly:** our sim was used to pick our three, so it scores them well by construction. His lineups were built from his projections and the sim never saw them. The sim says P(his best of three beats our best of three) is 0.38, and each single head-to-head ranges 0.26 to 0.42, but that is a statement about the sim, not about Sunday. By his projections the sets are level. DST uses a normal curve from his projection, not DK DST scoring. Treat sim numbers as "which lineup has the higher ceiling in our model," nothing more.

Honest read: the sim is much cooler on his high-owned WRs (Jefferson, Olave, London) and on Mahomes than his file is. That gap (his F2 sim average of 108.8 is the lowest of the six) is the thing to watch, and nobody has shown which source is right. The sim backtest is thin.

## QB gate (friend's rules, applied by our code)

Rule from his process: no QB under $5,000; a low-owned QB needs a confirmed starter, implied total 21 or more, a top-12 ceiling at the position, and an opponent defense outside the top 8. Our code applies it to all QBs, which is stricter than his rule (his applies it to low-owned QBs).

| QB | Salary | Own | Implied | Sim ceiling rank (of 61) | Opp defense rank (1 = toughest) | Starter | Result |
|---|---|---|---|---|---|---|---|
| Allen (L1) | 7,500 | 13.9% | 30.3 | 1 | 16 | expected | PASS |
| Shough (L2) | 5,600 | 21.0% | 25.5 | 8 | 10 | expected | PASS |
| **Mahomes (L3)** | 6,000 | 10.5% | 25.7 | **14** | 27 | Full practice, backup Fields also Full | **FAIL (ceiling only)** |

Mahomes: $6,000 passes, implied 25.7 passes, ATL defense rank 27 passes, starter status is good (Full participation on the NFL.com report, 2026-11-13). The single miss is the ceiling rank, 14 against a cutoff of 12. His sim average is 13.3 against 20.3 in his file, a 6.9 point gap, the largest of any player on the slate. At 10.5% ownership he sits right at his own 10% "low-owned" line, so under his literal rule the gate may not even apply to him; under our stricter code it fails. Case for him: big implied total, weak ATL defense by our metric, and he is cheap for that. Case against: our sim does not see the ceiling. This is a judgment call, and it is Zac's.

Under rule R1 in the Three Lines report: his QBs are not different from ours except Mahomes. Allen and Shough are already ours. Mahomes fails a gate item we can verify, so R1 says keep ours and flag his. We do not copy him.

## Kenneth Walker III (Q) check

Source: NFL.com Week 10 injury report (nfl.com/injuries/league/2026/reg10), fetched 2026-11-13. Chiefs table: Kenneth Walker III, RB, groin, Did Not Participate, game status Questionable. The page does not say which practice day this is. A web search for a Chiefs-era Week 10 update returned nothing usable, only old Seahawks items and August Chiefs items, so there is no beat-writer confirmation. Treat the status as "Questionable, groin, did not practice, day unstated, no further news found."

Same report, Chiefs: Travis Kelce Full (L2 FLEX), Mahomes Full, Jaydn Ott RB Limited, Questionable (hamstring), Rashee Rice and Xavier Worthy Full. Falcons list shows no Bijan, London or Pitts, so none of them carries a designation.

What it means for L3: Walker is a $9,200 RB2, the biggest salary slot after Bijan, and also Mahomes' stack partner. If he is inactive at 11:30 AM Sunday, L3 loses its RB2 and its stack, leaves $9,200 to spend, and Ott or the KC backup gets his work. It is the single point of failure for L3.

Our data gap: Walker was in our chalk pool at 20.4%, but our DraftKings salary file carried no Q tag for him and `dfs_status_2026-11-15.json` had no practice entry for him, so our code did not flag him. He is in none of our three lineups, so nothing we built is affected. I have not edited the status file (it is the Sunday refresh input and you asked for decision support only); add `"Kenneth Walker III": "DNP"` to its "practice" block if you want the Sunday rebuild to exclude him.

## What the shared players mean for your choice

- **Bijan and Warren are in 5 of the 6 lineups.** If you enter ours plus his mix, you are heavily long Bijan/Warren. Our three already hold both in all three. Entering his L1 or L2 instead of one of ours would be the way to cut concentration: L1 has Warren but not Bijan, L2 has Bijan but not Warren.
- **L2 is the least-overlapping with ours** (1 to 3 shared) and the only lineup with no overlap with L1. It has the lowest sim numbers of the six and the Shough stack (Shough, Olave, Tyson) plus McMillan as bring-back and two KC/ATL game pieces (Pitts, Kelce, plus Bijan). Shough is also our A's QB. Hedging by taking L2 means doubling up on NO/CAR game outcomes with A.
- **L1 and our B share Allen, Hubbard, London, Warren.** If you enter both you are paying twice for the same QB. L1 is the no-stack build; B stacks Allen with Shakir.
- **L3 and our A share 6 players.** Entering both is close to one lineup twice. L3 adds the Mahomes/Walker KC pairing, which our code fails and the injury report puts at risk.
- **Our C (Lawrence, Watson, Douglas, Texans) shares the least with L1 to L3**, so if you want a mix that diversifies, C plus one or two of his is the cleanest.

I am not picking for you. Both views are laid out, and you decide.

## Recheck after Sunday 11:30 AM inactives

He sent these Friday, earlier than the 12 PM Sunday plan, so the Sunday refresh can still change things. Lineups that need a recheck, in order:

1. **F3:** Walker (Q, groin, DNP), plus Mahomes confirmation and Ott (Q) for the KC backfield. If Walker is out, F3 is broken.
2. **F1:** Jakobi Meyers (Q on our DraftKings salary file, Limited on our NFL.com practice entry in `dfs_status_2026-11-15.json`, 2026-11-13; his screenshot shows no Q tag; JAX at TEN). Also Hubbard, Gordon (MIA RB room; Achane is on IR per the Three Lines report), Allen as expected starter.
3. **F2:** the NO/CAR game pieces (Shough, Olave, Tyson, McMillan) and Hall. None is on our practice list with a designation as of 2026-11-13, but our injury list is a single NFL.com fetch with one status per player. No source confirms starters.
4. **Ours:** Gordon (A and C, MIA RB room), Warren (all three, IND), and the three QBs, as already in the Three Lines runbook. Our Meyers exposure is zero.
5. Any QB scratch (Allen, Shough, Mahomes, Lawrence) kills that lineup outright. No QB is confirmed by a named source for any of them.

Commands for Sunday (from `D:\WKP\Fantasy-Football\dfs`): `python dfs_compare.py "D:\WKP\data\dfs-friend\friend_lineups_2026-11-13.txt"`. If he changes a lineup, edit that file or send a new one and rerun.

## Not verified

- Depth charts and starters were not confirmed from team sources for any QB.
- The NFL.com report does not show the practice day, so Walker's Friday status is not date-pinned.
- Ownership is the friend's projection; not verified.
- Sim figures are model output on the same draws that picked our three.
- Walker status is from one fetch of NFL.com plus a search that found nothing newer.

## Sources

NFL.com Week 10 2026 injury report, https://www.nfl.com/injuries/league/2026/reg10 (fetched 2026-11-13). Screenshots at D:\Draft Kings\Week 10\lineup 1.png, lineup 2.png, lineup 3.png. Compare output saved at `D:\WKP\scratch\compare_out.txt`.
