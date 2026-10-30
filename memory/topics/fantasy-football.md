---
name: fantasy-football
description: "How the weekly pick'em card and IRFL lineup workflow actually works — corrected 2026-09-15 after a subagent misread a blank card as \"nothing to log yet\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5068502a-676d-4fde-9afd-8985d28f90f9
  modified: 2026-10-23T01:34:51.220Z
---

## The blank pick'em card is the trigger, not something to wait on

Zac drops a blank, frozen-line card in `Fantasy-Football\cards\` every
week (e.g. `CODENAME_Week2 Entry.xls`). That blank card **is** the
normal weekly input — he is not filling it out first. The
fantasy-football-director's job on seeing it is to fill in picks
(against the spread AND straight-up, plus the Monday-night tiebreaker)
and hand back a finished model card, not to check whether picks are
already on it and report back empty-handed.

**Why:** on 2026-09-15 a subagent run correctly identified the Week 2
card was blank via `pickem_card.py` but then treated that as "nothing
to log this session" and stopped, asking Zac to go fill out his own
picks first. Zac's correction: "I give you a blank card and you give
me what you think is going to win... I will do my own card later."

**The real three-card weekly cycle:**
1. **Model card** — this venture's job, produced from the blank card
   before Thursday kickoff. Pick every game ATS and straight-up, set
   the MNF tiebreaker off a shaded-under Vegas total.
2. **Zac's card** — he fills his own out separately and later, from
   his own read. Not the model's job to produce.
3. **Reality** — actual results after MNF.

All three get graded against each other after Monday Night Football to
build the season prediction model (`tracker\predictions.csv`,
`grader.py`). Full workflow now locked in
`Fantasy-Football\CLAUDE.md` under "Pick'em model (card decisions)."

**How to apply:** any time a blank/frozen card shows up, immediately
produce and hand back the model's picks — do not wait for or ask about
Zac's own card.

## Straight-up picks are NFL only (2026-10-07)
Zac: the straight-up card (winners only, no spread) is NFL only, no college.
ATS still covers all 20 games. Pickups docs live in per-week folders
(`Week N\`) with the .md copies in `Claude MD Files\` (see
`Fantasy-Football\CLAUDE.md`).

## 90-day no-team rule (2026-10-07)
Zac: in the IRFL rules, a player with no NFL team for 90 days has no dead
cap penalty when cut. Locked in `Fantasy-Football\CLAUDE.md` under "Dead cap
on drops". Open: does a practice-squad signing count as "with a team" and
does it restart the clock (affects Shepard; Andersen is clear 2026-11-05).
Ask Zac, don't assume.

## Lineup calls need real research, not a projections lookup

Same correction, same session: "just do your own comparison and not
just look at projected points, research and find me the best lineup."
Consensus projection numbers alone are not the model — snap share,
target share, opponent matchup, game script, and current injury news
have to actually be weighed per player. Deliverable is a specific
recommended lineup with reasoning on the close calls, not a table of
projected points. Locked in `Fantasy-Football\CLAUDE.md` under "Roster
maximizer model (lineup decisions)."

See [[wkp-ops]] for the general fire-and-forget/take-initiative rule
this reinforces — don't stop and hand back a status report when the
actual ask was a deliverable.

## Weather rule (Zac, 2026-10-22)
Wind, rain and snow all factor into a game, unless it is a dome. My weather_signal.py test only covered wind, temp, roof and surface (wind >= 15 mph took ~2 pts off the total; nothing at play level). Precipitation was not tested separately. **How to apply:** flag weather for every outdoor game in picks and lineup calls; consider testing rain/snow in ff-play-sim. See [[wkp-ops]].

## Simulation project (2026-10-15)
Zac wants simulations with real coaching tendencies for lineups and picks, modeled on a gambler friend who
does the same for DraftKings/FanDuel DFS (not sportsbooks, not legal in GA) using nflverse Next Gen Stats plus
the last 2-3 seasons of coaching data. Built `.claude/skills/ff-simulator/` same night. Honest backtest result:
about 3-6% lower error than a plain recent average at QB/RB/WR/TE/K, a tie on IDP, so the value is ranges and
correlations, not magic. First-year coaches (BAL Minter, CLE Monken, LV Kubiak, MIA Hafley) fall back to team
history plus league mean. Gambler friend's second source arrives 2026-10-16. Tracker: only Weeks 1 and 6 are logged.
**How to apply:** run the simulator for every lineup call, state its limits, and log picks to the tracker BEFORE kickoff, not after.
See [[wkp-ops]].

## Zac never picks against Detroit (2026-10-29)
Zac's own card always takes the Lions unless he knows they are bad that year. It is loyalty, not a read on the game. Week 8 he took DET -3.5 when the model had MIN +3.5.
**Why:** his team. **How to apply:** the model card still picks Detroit games on the numbers. Do not argue Zac off Detroit. When grading model vs Zac, call out Detroit games separately so the loyalty pick does not skew the read on his other calls.
