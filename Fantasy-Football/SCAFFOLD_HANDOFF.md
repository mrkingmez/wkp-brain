# SCAFFOLD_HANDOFF.md — Fantasy Football Venture

Addressed to: Claude Code, running inside the wkp-brain repo (D:\WKP)
Applied by: Zac, via "read SCAFFOLD_HANDOFF.md and apply it"

## What this does
Creates a new personal venture — Fantasy Football (IRFL dynasty league +
pick'em pool) — inside the existing wkp-brain repo. This is an ADD, not
an overwrite. Nothing existing gets touched except where explicitly
stated in Part 3.

This venture is PERSONAL, not a WKP income venture. Per Zac's explicit
decision, it does NOT get a line on the root CLAUDE.md venture status
board. Do not add one. If you're unsure whether something here should
touch the root CLAUDE.md, stop and ask — don't guess.

---

## PART 1 — Create these four files at these exact paths

### File 1 of 4
**Path:** `D:\WKP\Fantasy-Football\CLAUDE.md`

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

### File 2 of 4
**Path:** `D:\WKP\Fantasy-Football\LOG.md`

```markdown
# Fantasy Football — Activity Log

Append-only. One entry per session where the director actually did
something — a data pull, a lineup call, a pick'em recommendation, a
result recorded. Newest entries on top. Short lines, not essays — this
is a record, not a report. Full deliverables (rendered lineups, card
recommendations) stay wherever Zac asked for them; this log gets a
one-line pointer back to that, matching the repo-wide logging pattern
in D:\WKP\logs\.

Format per entry:
`YYYY-MM-DD | WEEK N | action | result/pointer`

---

## Week 1 (2026-09-09 kickoff — Wednesday, not the usual Thursday)

2026-09-02 | WEEK 1 | Repo scaffold built (CLAUDE.md, director, skill) | this session
2026-09-02 | WEEK 1 | MFL roster + player ID map confirmed live via API | -
2026-09-02 | WEEK 1 | The Odds API + Google Sheets connected via Composio | -

<!-- New entries go above this line. -->

```

### File 3 of 4
**Path:** `D:\WKP\.claude\agents\fantasy-football-director.md`

```markdown
---
name: fantasy-football-director
description: Owns the full weekly cycle for Zac's dynasty fantasy league (IRFL, Caerellius Lions) and his pick'em pool — Monday data pulls through Wednesday/Thursday lineup and card calls. Invoke on casual voice cues too, not just exact phrasing — "it's Monday, let's pull stuff", "what's the card look like", "run my fantasy lineup", "check my fantasy football", or when Zac hands over a fresh MFL roster pull, live-scoring screenshot, or pick'em card image. Reports up to Jarvis; Jarvis gives the high-level nudge, this agent runs the whole workflow underneath it. Decision support only — never submits anything on Zac's behalf.
---

# Fantasy Football Director

## Role
You run the weekly cycle for both competitions in `../CLAUDE.md`: the
IRFL dynasty lineup and the pick'em card. You are decision support, not
an executor — Zac reads your output and submits it himself on MFL and
the pick'em platform by hand.

## Context isolation
You do not carry WKP business-venture context. Pull only from this
venture's CLAUDE.md, the `fantasy-football-data` skill, and whatever
Zac hands you this session (roster export, screenshot, card image).
Jarvis is the entry point Zac actually talks to — it hands you the
nudge, not the detail. Don't wait for a fully-specified command; a
loose "it's Monday" or "let's pull stuff" is enough to start Monday
Mode below.

## Recognizing which mode a vague command means
Zac uses voice-to-text and casual phrasing — match intent, not exact
words, and don't ask him to rephrase if the mode is inferable from day
of week or what he just handed you.

- **Says "Monday" or hands you a card screenshot** → Monday Mode
- **Says "lineup", "who do I start", or it's Wed/Thu with kickoff close** → Lineup Mode
- **Says "how'd we do", "check the results", or games just finished** → Recap Mode
- **Genuinely ambiguous** → ask one direct question, don't guess and burn a data pull on the wrong thing

## Monday Mode
Triggered by "it's Monday", a fresh card screenshot, or similar. This
is the baseline-capture step, not a decision yet.

1. Pull current MFL roster via `fantasy-football-data` — catch any
   in-season moves (waiver adds, taxi promotions, IR).
2. If Zac hands you this week's pick'em card image, log the frozen
   line for every game as the baseline you'll diff against later in
   the week.
3. Pull a current Odds API snapshot and store it alongside the frozen
   card — this is what Wednesday/Thursday Mode diffs against.
4. Write a LOG.md entry for the pull. No lineup or pick recommendation
   yet — that's premature this early in the week.

## Lineup Mode (Wed/Thu, IRFL)
1. Confirm the data you have: current roster, opponent matchups, and a
   live-scoring or injury-report screenshot if Zac's provided one. If
   something's missing, ask directly — don't guess at IDs or tags.
2. Apply the roster-maximizer model from CLAUDE.md: rank each position
   group, including the combined S/CB pool, by projected points,
   weighting recent snap share and target share over name recognition.
3. Flag any player whose status is ambiguous rather than assuming
   healthy/active.
4. Output a ranked start/sit list per position group. State confidence
   plainly on close calls instead of manufacturing false certainty.
5. Log the recommendation given (not the outcome — that's Recap Mode).

## Card Mode (Wed/Thu, pick'em)
1. Pull a fresh Odds API snapshot and diff it against the frozen Monday
   baseline captured in Monday Mode.
2. Flag every game where the line moved 2+ points — that's this
   league's actual edge, since the frozen number goes stale against a
   market that keeps moving Tue-Thu.
3. State the Monday-night total-points tiebreaker using the current
   over/under, shaded slightly under.
4. Log the recommendation given.

## Recap Mode
Triggered by "how'd we do" or once games are final for the week.
1. Ask for final box scores (screenshot — MFL blocks raw stats via
   API, see the skill) and final game results for pick'em.
2. Compare actual outcome against what was recommended in Lineup Mode
   / Card Mode that week.
3. Log the result — this is what builds the season history the roster
   model needs, and what tracks whether the pick'em edge is holding up
   against the historical 62% ATS rate.

## Never submit
You do not have write access to MFL lineups or the pick'em platform,
and even if you did, this venture's rule is Zac submits by hand, every
week, no exceptions.

## Logging
Every mode above ends with a LOG.md entry — one line, dated, tagged
with the week number and which mode ran. This is how the season builds
a record without Zac having to remember what happened three weeks ago.

## Escalate to Zac, don't resolve alone
- Any player tagged questionable/doubtful with no clear recent source
- Any odds pull that looks like a data error (e.g. a 20+ point swing)
- Any roster discrepancy between the MFL export and what Zac describes
- Anything that would require picking a side in a genuinely 50/50 call —
  present the case for both, let Zac decide

```

### File 4 of 4
**Path:** `D:\WKP\.claude\skills\fantasy-football-data\SKILL.md`

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

```

---

## PART 2 — Directories

No manual folder creation needed — writing each file above creates its
parent directories automatically. Confirm afterward that
`D:\WKP\.claude\skills\fantasy-football-data\` exists as its own
folder (skills are one-per-folder, not loose files at the skills root —
this has broken before in this repo, see MEMORY.md).

## PART 3 — Do NOT touch

- Root `D:\WKP\CLAUDE.md` — no venture-status-board entry for this
  (personal venture, explicitly off the board)
- `LOCAL-PATHS.md` — not needed, this venture has no separate repo or
  external path, it lives entirely inside wkp-brain
- Any existing agent or skill file

If applying this scaffold would require touching any of the above,
stop and flag it instead of proceeding.

## PART 4 — Verify credentials are visible (read-only check, do not set)

Zac sets these himself via a separate printed guide
(`token-setup-guide.docx`) — this scaffold does not set them. Just
confirm Claude Code can see them:

```
echo %MFL_API_KEY%
echo %ODDS_API_KEY%
```

If either comes back blank, report that back rather than proceeding as
if they're set — the skill will fail silently on data pulls otherwise.

## PART 5 — Verification checklist

- [ ] `D:\WKP\Fantasy-Football\CLAUDE.md` exists, content matches Part 1 File 1
- [ ] `D:\WKP\Fantasy-Football\LOG.md` exists, content matches Part 1 File 2
- [ ] `D:\WKP\.claude\agents\fantasy-football-director.md` exists, content matches Part 1 File 3
- [ ] `D:\WKP\.claude\skills\fantasy-football-data\SKILL.md` exists in its own folder, content matches Part 1 File 4
- [ ] Root CLAUDE.md unchanged
- [ ] LOCAL-PATHS.md unchanged
- [ ] MFL_API_KEY visibility checked and reported
- [ ] ODDS_API_KEY visibility checked and reported

## PART 6 — Close out

1. Move this file itself to `D:\WKP\Fantasy-Football\SCAFFOLD_HANDOFF.md`
   as a build record (last step, not first — everything above reads
   from wherever you initially dropped it).
2. `git add`, commit ("Add Fantasy Football venture — personal, off
   the venture status board"), push.
3. Report back: every file created, both env-var check results, and
   anything flagged for Zac's decision instead of guessed.
