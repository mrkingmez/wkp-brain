---
name: kp-planner
description: Weekly listing batch scheduler for Kingdom Planners.
  Same cap logic as WarriorKingDesigns, shared across both shops.
  Trigger on 'kp planner', 'this week's kp listings', 'schedule kp
  batch'.
---

# Kingdom Planners Planner

## The cap
3 listings/day, 8/week, BOTH SHOPS COMBINED, locked until 15 NOV.
This is in root CLAUDE.md. Before scheduling anything, check how
many WarriorKingDesigns listings already went out this week - this
skill does not have its own separate budget.

## Open architecture question
There is no confirmed shared counter between this skill and
WarriorKingDesigns' listing tooling yet. Until one exists, ask Zac
directly how many listings shipped this week from either shop before
scheduling more. Do not assume zero.

## Output
A dated batch plan for the week, product name, target publish day,
which format (VA tracker style vs new spreadsheet), staying inside
whatever room is left in the combined cap.

## Escalation
If the combined cap is already met or unclear, queue a decision.
Never schedule past a cap you have not confirmed.