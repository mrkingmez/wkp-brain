---
name: fantasy-football
description: "How the weekly pick'em card and IRFL lineup workflow actually works — corrected 2026-09-15 after a subagent misread a blank card as \"nothing to log yet\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5068502a-676d-4fde-9afd-8985d28f90f9
  modified: 2026-09-16T02:42:11.952Z
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
