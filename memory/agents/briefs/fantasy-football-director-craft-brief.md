# Craft Brief: fantasy-football-director, DFS side only

Written 2026-11-22 by fantasy-football-director (self-run leveling job, Wave 1). Review by director/qa-director NOT done. Scope: DraftKings DFS (fun money, Zac enters by hand). The IRFL dynasty league is out of scope and was not touched.
Tool versions: DraftKings web contests as of Week 11 2026; nflverse via nflreadr; stale after 2027-02-20 (90 days) or on a DK scoring change.
Tags: SOURCED = verbatim quote from a page retrieved today. PROVEN = worked twice in our logged outputs. COMMUNITY. PROPOSED = our idea, untested.
Quotes are copied from the fetch result. The fetch tool caps each quote at about 125 characters, so most quotes are short. Where a page was only summarized by the tool, I say PARAPHRASE and do not mark it as a quote.

## 1. What world-class DFS decision support looks like (each line tied to a source)
1. Tournament lineups are built for the top of the payout curve, so variance is wanted inside a lineup and correlation is managed between lineups (S2, SOURCED).
2. Teammates and opponents in the same game are correlated, and a builder that ignores this mis-prices stacks and bring-backs (S2, SOURCED).
3. Late swap exists in some contests: a spot locks the moment that player's game kicks off, and a swap must react to confirmed information, not rumor (S5, S6, COMMUNITY plus unverified DK mirror).
4. Availability comes from dated official reports. The NFL's own Week 11 injury page is the primary feed, and its game-status words are Questionable, Doubtful, Out (S3, SOURCED). "Questionable" means uncertain, not 50 percent (S4, news report of the 2016 policy).
5. Data we score against must be the maker's own dated release, with its licence respected (S1, SOURCED).
6. A claim that a rule "lost" or "won" a slate needs more than one slate. This one is our own lesson, PROVEN in `LEARNING-LEDGER.md` (seed noise about 10 points of 7-lineup mean).

## 2. Sources (6 retrieved, 2 community; 2 official pages NOT RETRIEVED)

### S1. nflverse GitHub organization (PRIMARY, maker)
URL https://github.com/nflverse , retrieved 2026-11-22.
- "nflverse is a collection of data and R packages designed for NFL analytics!"
- "Most data is stored in releases of the nflverse/nflverse-data repository, in various formats (e.g. csv, parquet, and rds)."
- PARAPHRASE (not a quote): most data is licensed CC-BY 4.0, FTN data CC-BY-SA 4.0. Attribution is owed if we ever publish anything built on it. Our DFS output is private, so no change today.
Dictionary page https://nflreadr.nflverse.com/articles/dictionary_player_stats.html and the raw Rmd: NOT RETRIEVED for the `fantasy_points` rows (page body held no table). We cannot say from a source how nflverse's `fantasy_points` is calculated, so DK points must be computed by our own scorer, which is what `dk_actual.py` and the ESPN parser do.

### S2. Hunter, Vielma, Zaman, "Picking Winners in Daily Fantasy Sports Using Integer Programming" (PRIMARY, academic)
URLs https://arxiv.org/abs/1604.01455v3 (abstract) and https://ar5iv.arxiv.org/html/1604.01455 (full text, first 100,000 of 135,868 characters read), retrieved 2026-11-22. v1 April 2016, v3 January 2019.
- "We find that the correlation is negative for goalies and skaters on opposing teams." (hockey, Sec 3.3)
- "By putting all players from a single line in a lineup, we are essentially increasing the variance of the lineup." (Sec 4.2)
- "The negative correlation is something we want to avoid within a lineup as it would reduce the overall variance."
- "the contest payoff structure is so asymmetric" (their stated reason high-variance lineups profit, Sec 5.5)
- PARAPHRASE of the abstract: the entries are chosen as a portfolio, approximating the chance at least one wins with pairwise correlations under a Gaussian model, then built by integer programming for high expected score, enough variance, and low correlation with earlier entries.
Caveat: the paper is hockey and baseball, with football only mentioned as an extension in v1. Transfer to NFL is PROPOSED, not proven.

### S3. NFL.com official injury report page (PRIMARY, league, dated)
URL https://www.nfl.com/injuries/ , retrieved 2026-11-22.
- Page title as shown: "Official Latest NFL Injury Report for Players - Week 11 of the 2026 Season".
- Practice-status labels listed: "Did Not Participate In Practice," "Limited Participation in Practice," "Full Participation in Practice"; game-status labels "Questionable," "Doubtful," "Out".
- The page does not define the terms or give timing. Definitions and the submission deadline were NOT RETRIEVED from the league (https://operations.nfl.com/gameday/analytics/injury-report/ and /injury-reports/ both returned 404).

### S4. ABC7 report of the NFL injury report policy change (SECONDARY, news, 2016-08-22)
URL https://abc7.com/post/nfl-removes-probable-designation-from-team-injury-reports/1478760/ , retrieved 2026-11-22. This reports the league policy, it is not the policy. Whether the 2016 wording is still current in 2026 is NOT VERIFIED.
- Questionable: players are "uncertain" to play.
- Doubtful: "unlikely" to participate. Out: "will not play."
- PARAPHRASE: if there is any doubt, the player "should be listed as 'questionable.'"
Use: Questionable is an unknown, not a coin flip. Our own file uses 40 percent for Questionable with no practice and 75 percent for limited or full (Fantasy-Football CLAUDE.md rule 4, 2026-11-12). That number is ours (PROVEN on n=57 per that file, not a league figure).

### S5. DraftKings help text as mirrored on a Zendesk site (COMMUNITY, unverified mirror)
URL https://z3nbetting.zendesk.com/hc/en-us/articles/32244586615956-When-do-lineup-entries-and-edits-close-US , retrieved 2026-11-22, article posted 2024-11-18. I could not confirm this is DraftKings' own page.
- "Players can make lineup edits leading up to each game's lock time."
- "Athletes cannot be added or removed from a lineup once their contest's lock time has passed."
- "Lineup edits close when the contest locks" (contests without late swap).
Official DraftKings pages https://www.draftkings.com/help/rules/nfl and /rules/nfl/classic: NOT RETRIEVED (HTTP 403 on both). Scoring values (4 points per passing TD, 3 point 300 yard bonus) appear only in a web-search summary of the official page and are not quoted here. Rule to follow: the live DK scoring page, opened by Zac, wins over anything we cache.

### S6. Stokastic, "NFL DFS Late Swap: How To Use Late Games To Win GPPs" (COMMUNITY, practitioner, published 2026-08-31)
URL https://www.stokastic.com/articles/nfl-dfs/nfl-dfs-late-swap , retrieved 2026-11-22.
- "Once a player's game kicks off, that spot locks for good."
- "A lineup that locks entirely at 1:00 p.m. has no late-swap ability at all."
- "Swap On Confirmed Inactives, Not Rumors."
- "lock every finished game at variance 0 so the Sims stop guessing at scores you already have"
Use: Zac's Week 11 contest was "Early Only" with all games at 1:00 PM, so late swap did not exist for it (PROVEN by the DK file: every kickoff 01:00PM ET). The noon rerun is therefore the last chance, and the inactive-list check at about 11:30 AM to 12:00 PM ET is the real lever.

Other pages seen only as search-result titles (Footballguys, Fantasy Alarm, Establish The Run, RotoWire leverage columns, 2026 weeks 1 to 6) were NOT fetched. I cite nothing from them.

## 3. What this changes in our work
- Treat every Q tag as unknown until a dated official or team-site report resolves it, and write the resolving source and time in the status line (S3, S4, S6).
- Never present a build as "late swappable" unless the contest supports it; check the contest name for "Early Only" and the kickoff list first (S5, S6).
- A portfolio, not seven independent best lineups: report pairwise overlap and the largest single-player count, and make sure the 7 differ on the high-variance piece (S2, PROPOSED for NFL).
- A stack is a deliberate correlation choice: QB plus pass catcher plus opposing bring-back, written down per lineup (S2 for the principle, PROPOSED for football numbers).
- Our own fixed rule stays: any player in 3 or more lineups, and any player whose QB or team total changed, is flagged and fixed before hand-off (PROVEN failure, Week 11, `memory\feedback-dfs-concentration-check.md`).
- One slate is noise. No rule change from one slate (our LEDGER, PROVEN, seed spread about 10 points).
- DK points come from our scorer, not nflverse `fantasy_points` (S1 gap).

## 4. Open questions the sources did not answer
1. The exact DK Classic scoring table and roster rules from DK's own page (403). Needed before any scoring-code audit.
2. The league's current injury-report timing and the current wording of designations.
3. Whether football tournament leverage numbers (ownership versus finish) hold for a 14-team early slate with a $1 entry and a small field. No retrieved source covers it.
4. Real ownership percentages. Ours (`dk_own.py`) is an estimate and has never been measured against DK's own ownership.
5. Contest payout table and cash line for the contest Zac enters.
