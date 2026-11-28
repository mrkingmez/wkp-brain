---
name: feedback-dfs-concentration-check
description: Before handing over DFS lineups, check ownership and concentration of any single player, especially after a QB change, and fix it without asking Zac
metadata:
  type: feedback
---

dk_validate passes salary, exposure cap 4, QB limit and overlap, but it does not catch one chalk player (McBride, 47% own) carrying 4 of 7 lineups after his QB changed to a backup (Josh Johnson, ARI implied 12.5). Zac 2026-11-22: "so why didn't you do that? That is the part of your learn isn't it", under time pressure before the 1 PM lock.

**Why:** I told him to upload as is, asked him to approve a swap that was my job, and miscounted exposure first. He had to run errands and lost time.

**How to apply:** On every DFS build and rerun, list each player's lineup count and ownership, flag any chalk player in 3 or more lineups and any player whose QB or team total changed, then fix it (swap, revalidate with dk_validate, place the file with a backup) and report the result, not a question. Verify counts per lineup, not by grepping stack lines. See [[feedback-noon-check-is-ff-job]], [[feedback-take-initiative]].
