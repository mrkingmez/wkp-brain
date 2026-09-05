@../ME.md
@../projects.md

# Fantasy Football — Venture CLAUDE.md

## Status
PERSONAL. Off the WKP income venture board — does not compete with Kingdom
Planners, WWD, or any business venture for build hours or scheduling.
Goal is competitive: bragging rights and the league trophy, not revenue.
Real weekly deadlines still apply (see below), so this folder is fully
built out like an active venture even though it stays off the board.

## What this venture is
Two competitions, one repo:

1. **Dynasty fantasy league** — Imperium Romanum Fantasy League (IRFL).
   12 teams, 3 divisions (Italia, Macedonia, Aegyptus). Team: Caerellius
   Lions, franchise ID 0012. Full PPR, heavy IDP scoring (8 of 17 starters
   are defensive: DT+DE, LB, CB+S combined pool). $5000 soft salary cap,
   contracts tracked through 2028. 2026 is an all-in year — win it now,
   before a likely rebuild.
2. **Pick'em pool** — long-running league with army buddies (Brad, Rice,
   others), 12+ years running. 20-game card: 4-6 college games plus all
   pro games, against the spread. Commissioner sets the line Monday and
   it's frozen all week. Underdog wins ties. Monday-night total-points
   is the tiebreaker. Card locks at Thursday-night kickoff — except
   Week 1 2026, which is a Wednesday opener (Sept 9, 8:20pm ET), so that
   week's deadline moves up a day. Historical 12-year hit rate is ~62%
   against the spread, likely because the line is frozen Monday and
   real money moves the number Tue-Thu.

## Hard deadlines
- Lineup and pick'em card: locked at kickoff of the first game of the
  week (normally Thursday night, Wednesday for Week 1 2026).
- No agent submits anything on MFL or the pick'em platform. This folder
  is decision support only — Zac makes the final call and submits by hand.

## League IDs / config (not secret, safe to keep in plain files)
- MFL host: www44
- MFL league ID: 43094
- MFL season year: 2026
- MFL username: mrzacking

## Credentials (never in files — env vars only, see SETUP-TOKENS.md)
- MFL_API_KEY — read access to roster/player exports
- ODDS_API_KEY — The Odds API, NFL + CFB spreads

## Known platform constraints
- MFL's API will not return raw player stats (licensing restriction,
  confirmed in their own developer terms). Box scores have to come from
  a screenshot of MFL's live-scoring page each week — this cannot be
  automated around, it's a deliberate ToS block, not a technical gap.
- Odds API is connected two ways: through Composio for in-chat pulls,
  and via ODDS_API_KEY for anything Claude Code runs locally. Same key,
  two paths — use whichever surface you're in.

## Roster maximizer model (lineup decisions)
Per player, per week: consensus projection, snap % trend (last 3 games),
target share / touch share (last 3 games), opponent points-allowed to
that position, game total + spread. Weight recency > name recognition.
Full PPR inflates pass-catching backs and slot WRs relative to standard
scoring. IDP scoring here is volume-heavy (1pt/tackle, 3pt/sack), so
high-tackle LBs often outscore big-play DBs — rank the combined S/CB
pool by projected points, not by position label.

## Pick'em model (card decisions)
Compare Zac's uploaded Monday card (the frozen baseline) against current
lines pulled Wednesday/Thursday. Flag any game where the line moved 2+
points — that's the edge, since the frozen number goes stale against a
market that keeps updating on injuries and sharp money. Monday-night
tiebreaker: use the Vegas over/under, shaded slightly under (posted
primetime totals skew a touch high).

## Escalation
Flag to Zac, don't guess, on: any player tagged questionable/doubtful
with no clear source, any line move that looks like a data error rather
than real movement, and anything that would require submitting a pick
or lineup on his behalf.

## Logging
Every director session ends with a one-line entry in `LOG.md` in this
folder — date, week number, mode, and a pointer to any deliverable
produced. Newest on top. This is the season's record; without it the
roster model has no history to weight against and Zac has no way to
check whether the pick'em edge is actually beating 62% ATS.

## Jarvis integration
No manual registration needed. Claude Code auto-discovers everything in
`.claude/agents/` and `.claude/skills/` — placing the director and skill
files in the right folders (see repo structure below) is the whole
setup. Jarvis just needs to recognize casual cues like "it's Monday" or
"let's pull stuff" and hand off; the director's own description field
carries those trigger phrases, and the director itself resolves which
mode (Monday / Lineup / Card / Recap) a vague nudge means — see
`fantasy-football-director.md` for that logic. This venture is not on
the main venture status board (personal, not income), so it won't
appear there — that's expected, not a gap.

## Repo structure (once built tonight)
```
D:\WKP\Fantasy-Football\
  CLAUDE.md          <- this file
  LOG.md             <- season activity log
D:\WKP\.claude\agents\
  fantasy-football-director.md
D:\WKP\.claude\skills\fantasy-football-data\
  SKILL.md
```
