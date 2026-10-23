# Agent network: how directors talk to each other

Locked 2026-10-20 (Zac). Directors work with each other directly. A director does not
climb up to Jarvis to ask another desk for help.

## The rule

Need something another desk does? Send the task straight to them with the Agent tool,
using their agent name as `subagent_type`. Get the result back yourself. Jarvis sees
the outcome in your report and your log. Jarvis is not a switchboard.

## Handoff note (put this at the top of every task you send)

- FROM: your agent name
- TO: the agent
- TASK: one or two sentences
- FILES: full paths the receiver needs
- NEED BACK: what you want returned and in what form
- RULES THAT APPLY: book, venture, mode (GENERATE or SCRUB), anything locked

## Who anyone can call directly

| Desk | Call it for |
|---|---|
| script-room | any script. It runs its own bench (room-writer, originality, dialogue-doctor, clearance). Two passes before final |
| devils-advocate | a hostile read of any draft, plan, hook, listing, chapter before it ships |
| clearance | a quick copyright or fair use flag on anything public |
| marketing-director | any public copy, post, caption, thumbnail, cutdown. It routes its own departments |
| fiction-director | any book fact, canon, timeline or publishing question |
| any venture director | a fact or file from that venture |

## Who is called only through their boss

- copywriting, social-media, graphic-design, video-ugc, market-research: through marketing-director.
- room-writer, originality, dialogue-doctor: through script-room (clearance and devils-advocate may be called direct).
- fiction-researcher: through fiction-director.
- ebay-researcher: through ebay-director.
- shattered-empire-director and military-scifi-director: through fiction-director.

## Limits (these stop loops)

1. Never send a task back to a desk that is waiting on you.
2. No chains longer than two handoffs on one task. A third goes to Jarvis.
3. A desk may decline a handoff with a reason. The caller then goes to Jarvis.
4. Peers do not give each other orders about priority, money, schedule, or what Zac
   decided. Those go to Jarvis and Zac.
5. Decisions still go to `logs\DECISIONS.md`. Nobody answers one for Zac.
6. Review gates still apply (root CLAUDE.md, 19 OCT 26). Scripts: two passes through
   script-room. Public copy: marketing-director then no-ai-slop.
7. Zac's rules travel with the task: no em dashes, never invent lines in his writing,
   draft only, Zac posts.

## Reporting

- Result goes back to the caller, not to Jarvis.
- The caller puts one line in its own report: who it asked, what came back, file path.
- A handoff that fails or is not reachable is reported plainly. Do not fake it or do the
  other desk's job yourself.
- Anything a subagent cannot do (ask Zac a question, use a browser) goes up to Jarvis
  as a flag.
