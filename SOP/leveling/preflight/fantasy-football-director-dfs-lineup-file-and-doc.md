# Pre-flight: DFS lineup file and doc (fantasy-football-director, DFS only)

Created 2026-11-22. Paste into the hand-back with each item ticked and a one-line proof. One unticked item means the file does not go to Zac. Director spot-checks 1 in 3. Agents never enter lineups or spend.

1. [ ] Contest named in the doc, with whether late swap exists (check "Early Only" and the kickoff list in the DK salary file). Proof: contest name and kickoff times quoted.
2. [ ] Refresh line written: stats, odds, injuries, starting QBs, each with source and ET timestamp (or "not needed, reason").
3. [ ] Every player in the file checked against the DK salary file Status column AND our injury file; any disagreement listed with the resolving dated source (NFL.com, team site, ESPN feed).
4. [ ] Player count table: every player's lineup count and ownership estimate. Any chalk player in 3 or more lineups is fixed or justified in one written line. Proof: the table is in the doc.
5. [ ] Any player whose QB or team implied total changed since the last build is listed and re-checked.
6. [ ] The fix was made by me. No "cut it by hand if you like" lines.
7. [ ] `dk_validate.py` result pasted (PASS line), plus salary at or under 50,000 and 7 distinct lineups.
8. [ ] Each lineup has a source label (model, rotowire, test and rule ID) and the exact built file is copied to `entered_archive` before lock.
9. [ ] Every instruction to Zac tagged PROVEN (log path), SOURCED (URL, date, quote) or PROPOSED (the cheap test).
10. [ ] Ownership numbers labelled ESTIMATE; real ownership marked NOT KNOWN.
11. [ ] NOT VERIFIED list at the bottom (weather, depth chart roles if no dated source).
12. [ ] No em dashes (`slop_check.py` exit 0 if the doc is public; this doc is internal, so a grep for the dash character).
