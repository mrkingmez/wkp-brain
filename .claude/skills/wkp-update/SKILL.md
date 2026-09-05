---
name: wkp-update
description: Interactive check-in session - pulls every open task and
  open decision across all ventures, reads them back one venture at a
  time, and writes Zac's spoken status updates straight into TASKS.md
  and the DECISIONS.md files as he gives them. Trigger on 'time for an
  update', 'update time', 'let's do updates', 'run the update', 'update
  check-in', or 'it's update time'.
---

# WKP Update

## What this is
A live back-and-forth, not a report. Pull every open item, read it back
one venture at a time, take Zac's answer, write it to the real file
before moving to the next. This is the Midday/Evening accountability
rhythm from root CLAUDE.md, run on demand instead of on a clock.

## Source of truth
Do not go looking for a saved daily brief or Monday brief file. The
daily brief only gets written to disk when someone specifically asks
for that (see its own skill spec), so a file trail is not guaranteed
to exist on any given day. Both briefs are themselves generated from
the same two sources below, so reading those directly is equivalent to
"what was on the brief" and always works:

- **TASKS.md** - every row not marked Done.
- **Every DECISIONS.md in the repo** - glob `**/DECISIONS.md`, do not
  hardcode the list. New ventures add their own decision queue and
  this skill has to pick them up without a rebuild. Currently:
  `logs\DECISIONS.md` and `PAWS\decisions\DECISIONS.md`.

## Scope
Every open item, every venture - including ACTIVE-UNSCHEDULED and
DORMANT ventures per the status board in root CLAUDE.md. Jarvis hides
those from daily planning; this skill does not. A stale item on an
unscheduled venture is exactly the kind of thing that should surface
at a deliberate check-in, even though it never makes a rushed morning
brief.

## Flow

1. Read TASKS.md in full.
2. Glob and read every DECISIONS.md.
3. Group everything by venture, roughly in the order of the venture
   status board (MAIN EFFORT first, then ACTIVE, then
   ACTIVE-UNSCHEDULED, then DORMANT).
4. Walk one venture at a time. For each open task and each OPEN or
   PARTIAL decision, read it back in one line, plain language, no
   jargon. Wait for Zac's answer before moving to the next.
5. Interpret the answer the way ME.md says to - phonetic, voice-to-text,
   don't flag typos or word substitutions. "Roger" and "copy" mean yes,
   move on with no change.
6. The moment an answer lands, write it. Do not batch changes for the
   end of the session:
   - Task done, in progress, blocked, or notes changed -> edit that row
     in TASKS.md immediately.
   - Decision resolved -> mark RESOLVED in that file, with the answer
     and today's date, in place.
   - New task or decision surfaces mid-conversation -> file it in the
     right place immediately, per the CLAUDE.md rule that updates get
     flagged and filed the same turn they come up, never batched.
   If the session gets cut short, everything answered so far is
   already on disk.
7. If Zac says to skip a venture or an item, skip it and move on.
   Silence or an unclear answer is not a decision - ask once, plainly,
   and move on if it is still unclear rather than guessing what he
   meant.
8. When every venture is covered, give a short recap - what changed,
   counts only, not a full re-print of every line. Then stop.

## Rules
- This is a conversation with writes, not a document. Do not produce a
  formatted report as the output.
- No em dashes.
- Never invent a status Zac did not give. If he says nothing about an
  item, it stays exactly as it was - do not mark something Done because
  it sounds like it should be.
- A decision only gets marked RESOLVED on Zac's explicit word. An
  update that sounds like progress but is not a final answer stays
  OPEN.
- Unsure which venture or file a spoken update is about? Say which item
  is unclear and ask, rather than guessing and filing it in the wrong
  place.

## Escalation
This runs in the main window with Zac present, not as a background
agent - you CAN and should ask him directly the moment something is
ambiguous. The "cannot ask a question" rule for queued agents does not
apply here.

## Output
No new file by default. Updates land directly in TASKS.md and the
relevant DECISIONS.md files, in place. If Zac asks for a written
recap of the session, save one to `D:\WKP\logs\update-YYYY-MM-DD.md`.
