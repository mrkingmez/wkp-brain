---
name: feedback-refresh-before-sims
description: Always refresh nflverse stats, odds, MFL and injury data before running any fantasy or DFS simulation (Zac 2026-11-19)
metadata:
  type: feedback
---

Zac, 2026-11-19: "we should refresh before we do any sims from now on." Applies to IRFL, pick'em and DraftKings sims, every run and every rerun.

**Why:** the Week 11 DK builder was found running on nflverse stats that stop at Week 9, and the Week 11 IRFL sims used the wrong starting QBs (Wentz, Winston, McKee) until overrides were added.
**How to apply:** before any sim, pull fresh nflverse stats, odds, MFL roster and injury or inactive news, then confirm the starting QB for each team from a dated source. State the refresh time in the output. See [[feedback-fantasy-timing]] and [[feedback-fantasy-picks-format]].
