# SCAFFOLD-HANDOFF-FANTASY-WK1.md — Week 1 Card Update

Addressed to: Claude Code, running inside the wkp-brain repo (D:\WKP)
Applied by: Zac, via "read SCAFFOLD-HANDOFF-FANTASY-WK1.md and apply it"

## Prerequisite
This assumes `SCAFFOLD-HANDOFF-FANTASY.md` was already applied — the
Fantasy-Football venture folder, director, and skill already exist. If
`D:\WKP\Fantasy-Football\CLAUDE.md` does NOT exist yet, stop and run
that scaffold first; this one only edits/adds, it doesn't build the
base structure.

## What this does
Updates the venture to handle the real Week 1 card structure — which
turned out to be bigger than the original build assumed. Three things:
1. Replaces `CLAUDE.md` and `SKILL.md` in full (both fully owned by
   this venture, safe to overwrite completely — not root repo files).
2. Creates one new file: `FUTURES-PICKS.md`.
3. Creates one new folder: `cards\`, and moves the Week 1 card into it.

This is an ADD to the venture, still does not touch root CLAUDE.md,
LOCAL-PATHS.md, or anything outside the Fantasy-Football folder and its
one agent/skill files.

---

## PART 1 — Replace this file in full
**Path:** `D:\WKP\Fantasy-Football\CLAUDE.md`
(Overwrite entirely — this is the updated version, not a merge.)

```markdown
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

## Card structure (updated after seeing the actual Week 1 card)
Every weekly card has three parts on different resolution timelines:
1. **20-game ATS pool** — the recurring weekly pick. Normally locks
   Thursday kickoff; check the actual card, since the NFL schedule can
   move the lock (Week 1 2026 is a Wednesday opener).
2. **Eliminator Challenge (EC)** — one team per week, marked with an X
   in a yellow box, season-long survivor-style side pool. Logged
   weekly in `FUTURES-PICKS.md` even though it's a recurring pick, since
   it's tracked across the whole season.
3. **Season-long futures** — Super Bowl winner, 14 playoff seeds, and
   the final NCAA CFP top 12 in order. Made once, on the Week 1 card,
   graded only at season's end. Live in `FUTURES-PICKS.md`, never
   graded against a weekly result.

Cards live in `cards\` inside this venture folder
(`Fantasy-Football\cards\2026-wkN-card.xls`). Picks get entered directly
into the card file's blank cells — the card is the record, there's no
separate answer sheet.

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

```

## PART 2 — Replace this file in full
**Path:** `D:\WKP\.claude\skills\fantasy-football-data\SKILL.md`
(Overwrite entirely — this is the updated version, not a merge.)

```markdown
---
name: fantasy-football-data
description: Pulls live data for Zac's IRFL dynasty league and pick'em pool — MFL roster/player exports and current NFL/CFB odds. Use when the fantasy-football-director agent needs fresh roster status, player ID lookups, or a current line pull, or when Zac directly asks to "pull my roster", "check the odds", or "refresh my fantasy data". Read-only against both APIs; never writes to MFL or submits anything.
---

# Fantasy Football Data

## Config (safe to keep in plain text — not secret)
- MFL_HOST = www44
- MFL_LEAGUE_ID = 43094
- MFL_YEAR = 2026
- MFL_FRANCHISE_ID = 0012 (Caerellius Lions)

## Credentials (env vars only — see SETUP-TOKENS.md, never hardcode)
- MFL_API_KEY
- ODDS_API_KEY

## Roster pull
```
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=rosters&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
```
Returns every franchise's roster by numeric player ID, salary,
contractStatus, contractYear, and status (ROSTER / TAXI_SQUAD /
INJURED_RESERVE). Franchise 0012 is Caerellius Lions.

## Player ID map
```
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=players&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
```
Large, mostly-static file — every player MFL tracks, with id, name,
position, and current NFL team. Cache this locally (`players-cache.json`
in this skill's folder) and only re-pull if a roster ID doesn't resolve,
or once a week during the season to catch trades/signings. Don't re-pull
it on every call — it rarely changes.

## What MFL will NOT give you
Raw player stats (passing yards, tackles, etc.) are blocked by MFL's own
licensing terms — this is deliberate on their end, not a bug or a gap to
route around. For box scores, ask Zac for a screenshot of MFL's live-
scoring page and read the numbers off that.

## Odds pull
Current NFL and CFB spreads via The Odds API. Two paths depending on
where this is running:
- **In Claude chat**: use the connected Composio `the_odds_api` toolkit.
- **In Claude Code / local scripts**: call directly with `ODDS_API_KEY`
  as a query param or header per The Odds API's own docs — check
  api.the-odds-api.com/v4 endpoints for the current spec, since their
  API version can change.

Compare against Zac's uploaded Monday card. A line that's moved 2+
points from his frozen number is the signal to flag.

## Network note (chat environment only)
`web_fetch` in the chat interface cannot reach myfantasyleague.com
directly (domain not on the allowlist, and it also blocks robots).
When running from chat rather than Claude Code, ask Zac to paste the
URL into his browser and return the raw output — same workaround
already in use for this league.

## Pick'em card structure
The weekly card (an .xls file Zac uploads, saved to
`Fantasy-Football\cards\`) is not just 20 ATS games. Every card has
three parts, and they resolve on different timelines — don't conflate
them:

1. **20-game ATS pool** — the recurring weekly pick, spread across
   however many game-days that week has. Normally locks at Thursday
   kickoff; deviates when the NFL schedule deviates (Week 1 2026 is a
   Wednesday opener, so that week's lock moved up a day — always check
   the actual date on the card rather than assuming Thursday).
2. **Eliminator Challenge (EC)** — a single team picked each week,
   marked with an X in a yellow box next to that team on the card.
   Season-long survivor-style side pool, separate scoring from the ATS
   pool. Track picks week-to-week in case the pool disallows repeat
   picks — confirm the actual rule with Zac before assuming either way.
3. **Season-long futures (Week 1 card only, this season)** — Super Bowl
   winner, all 14 playoff seeds (7 AFC + 7 NFC), and the final NCAA CFP
   top 12 in exact predicted order. These do not resolve weekly. They
   resolve at season's end. Do not try to grade them against weekly
   results — they live in `FUTURES-PICKS.md` in the venture folder,
   checked only once real playoff seeding / CFP rankings / a Super Bowl
   winner actually exist.

The card also carries a point-value table for Super Bowl winner picks
(longshot teams score more if correct than favorites). Read that table
directly off whichever card carried it — don't assume it's the same
every season.

## Where picks actually get entered
Directly into the card file itself — the blank cells adjacent to each
label are the input fields (yellow-box legend on the card explains
this). Never build a parallel answer sheet; the card *is* the record.

```

## PART 3 — Create this new file
**Path:** `D:\WKP\Fantasy-Football\FUTURES-PICKS.md`

```markdown
# Futures Picks — 2026 Season

Made once, on the Week 1 card, resolved only at season's end. Do not
grade these weekly — nothing here has an answer until the actual event
happens. This file just holds what was predicted so it can be checked
against reality when the season closes.

Source card: `cards\2026-wk1-card.xls`

## Super Bowl Winner
Prediction: _(fill in from the card once Zac has decided)_
Point value if correct: _(per the card's associated point-value table)_

## AFC Playoff Seeds
| Seed | Predicted Team |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |

## NFC Playoff Seeds
| Seed | Predicted Team |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |

## Final NCAA CFP Top 12 (predicted end-of-season order)
| Rank | Predicted Team |
|---|---|
| 1 (National Champion) | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |
| 6 | |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |

## Eliminator Challenge — weekly log
One team per week, season-long survivor pool. Log each week's pick here
even though it's a weekly action, since it's a running season record,
not a one-time future.

| Week | Team Picked | Result |
|---|---|---|
| 1 | | |

## Grading (fill in only once the season actually ends)
- Super Bowl winner correct? —
- Playoff seeds correct (out of 14) —
- CFP top 12 correct (exact position, out of 12) —

```

## PART 4 — Move the Week 1 card
Zac has a file called `CODENAME_Week1_Entry.xls` (or similar — confirm
the actual filename in his Downloads folder). Move it to:

**Path:** `D:\WKP\Fantasy-Football\cards\2026-wk1-card.xls`

Create the `cards\` folder if it doesn't exist. Do not rename the
original file if Zac has already renamed it himself — check first.

## PART 5 — Append one line to LOG.md
**Path:** `D:\WKP\Fantasy-Football\LOG.md`
Append this single line above the "New entries go above this line"
marker — do not touch anything else in the file:

```
2026-09-0X | WEEK 1 | Week 1 card structure confirmed (ATS + Eliminator Challenge + season futures); skill and CLAUDE.md updated; card filed under cards\ | Fantasy-Football\cards\2026-wk1-card.xls
```

Replace `2026-09-0X` with today's actual date.

---

## PART 6 — Do NOT touch
- Root `D:\WKP\CLAUDE.md` — still no venture-status-board entry
- `LOCAL-PATHS.md` — still not needed
- `fantasy-football-director.md` — this update doesn't require director
  changes; its Monday/Lineup/Card/Recap modes already cover this

## PART 7 — Verification checklist
- [ ] `CLAUDE.md` replaced, contains the new "Card structure" section
- [ ] `SKILL.md` replaced, contains the new "Pick'em card structure" section
- [ ] `FUTURES-PICKS.md` created at the venture root
- [ ] `cards\2026-wk1-card.xls` exists (or flag if the source file
      couldn't be located — don't guess a path)
- [ ] One line appended to `LOG.md`, nothing else in that file changed
- [ ] Root CLAUDE.md and LOCAL-PATHS.md unchanged

## PART 8 — Close out
1. Move this scaffold file itself to
   `D:\WKP\Fantasy-Football\SCAFFOLD-HANDOFF-FANTASY-WK1.md` as a
   build record.
2. `git add`, commit ("Fantasy Football — Week 1 card structure update:
   futures picks + eliminator challenge"), push.
3. Report back: every file created/replaced, the card's actual source
   path if different from assumed, and anything flagged for Zac's
   decision instead of guessed.
