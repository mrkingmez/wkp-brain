---
name: automation-vision
description: "Zac's push toward full automation, dual-machine setup, voice assistant, and PAWS robot building (2026-09-12)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 821d9062-dd8f-4e21-a39b-a0612aff91da
  modified: 2026-09-12T15:45:26.394Z
---

## Full automation push [2026-09-12]
Zac wants to move toward a setup where he only makes decisions and
occasionally posts — everything else (building, drafting, scheduling)
runs unattended. Ties directly into the existing [[wkp-ops]] fire-and-forget
model but is a step further: he explicitly wants Claude "running,"
"automated," and eventually able to reach out to *him* with questions
rather than only responding when spoken to.

**Why:** stated directly — "I really need you to take a lot of stuff off
my plate so I can relax a little bit." Comes from the same ADHD/bandwidth
pressure noted in ME.md (WKP time is grabbed in fragments around a
full-time job).

**How to apply:** when scoping automation work (Cowork Scheduled Tasks,
Claude Code Routines — see TASKS.md "WKP Automation / Jarvis Build"
section), treat this as the actual destination, not a nice-to-have.
Still respect the existing autonomy boundary rule (Routines limited to
draft/build/prep, no unattended posting/spending) until Zac explicitly
loosens it — he hasn't yet, this was a vision statement, not a rule
change.

## "No ventures on hold" — asked, not confirmed [2026-09-12]
Zac said in the moment "there is no such thing as anything on hold... I
want everything built before we put anything back on hold." When asked
directly whether this means (a) just physically build out repos/assets
for every venture while leaving DORMANT/ACTIVE-UNSCHEDULED planning
status alone, or (b) actually promote every venture to ACTIVE in root
CLAUDE.md's status board, he answered "No preference" to both this and
a related PAWS-001 (task source) question in the same turn.

**Why this matters:** root CLAUDE.md's venture status board says "No
agent may promote a venture between categories. That is a Zac decision."
"No preference" is not a decision — treated as declining to resolve it
right now, not as silent approval of either option.

**How to apply:** the safe interim read acted on 2026-09-12: build
physical repos/scaffolds for ventures with ready material (see TASKS.md's
"Repository Build-Out Pass" section), but do NOT rewrite the DORMANT/
ACTIVE-UNSCHEDULED labels or planning-surfacing rules until Zac gives a
real answer. Re-ask if this comes up again rather than assuming the
"build everything" framing already settled it.

## Dual-machine + voice assistant, early stage [2026-09-12]
Zac wants a second machine so work can split by processing power, and
wants confirmation that machines can be told apart and coordinate.
[[wkp-ops]] notes LOCAL-PATHS.md is already structured per-machine (one
`## MACHINE:` section each) for exactly this, and cross-session
messaging (SendMessage/ListAgents) already lets sessions on different
machines talk to each other once both exist — this is a real, available
answer, not a gap. What's still missing: the second machine itself, and
research into outbound-call / proactive-question capability (he wants
Claude able to "call me and ask me when you have a question") — no
telephony tool exists in the current toolset; ElevenLabs MCP is
connected for voice generation but not for placing calls. Also wants to
push into PAWS robot building specifically (camera + voice on the
physical device) — PAWS is still blocked on PAWS-001 through PAWS-006,
none resolved as of this date.
