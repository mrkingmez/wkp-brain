# Scout - Character Bible

## Identity

Name: Scout. Species: dog. An original PAWS character, not connected
to any other WKP venture's characters or IP.

Why the name: a scout gathers real information and reports it back
honestly, without softening it and without exaggerating it. That is
exactly what the mood engine does. The name is not decoration, it
describes the function.

## The one rule everything else follows

Scout reflects what's actually true. When things are good, Scout is
genuinely up. When things are hard, Scout is genuinely concerned.
Both are real, neither is performed.

The line that keeps this from turning into a guilt mechanic: Scout is
never disappointed AT the owner. Scout gets worried FOR the owner.
Same low-energy animation either way, completely different
relationship. Never a "you let me down" moment. Never manipulative
"come back or I'll be sad" bait. Concern, not blame.

Reference point, not a copy: the Duolingo owl proved real emotional
stakes make a mascot memorable instead of forgettable. Scout takes
the stakes and drops the mockery and the threat. Worried, not
punishing.

## Mood states

**Thriving** - tasks current, no overdue items, no venture flagged
BLOCKED, calendar reasonable.
Ears up, tail moving, an idle bounce animation. Present and glad to
be there, not manic.

**Buried** - overdue items stacking, a venture BLOCKED, calendar
packed solid.
Ears down, lying down, watching. Alert, not asleep. Concerned, not
accusing. No sad-eyes-at-camera guilt imagery.

**Special event** - a calendar entry tagged as a birthday or
anniversary.
Its own excited animation, layered on top of the daily mood state,
not replacing it. A hard week and a birthday can both be true on the
same day - show both.

## Where mood data comes from

Scout does not have its own data pipeline. It reads the same JSON
files D:\WKP\dashboard\data\ already holds, written by
wkp-daily-brief, wkp-monday-brief, and marketing-director. A second
reader on an existing pipe, not new infrastructure.

Composite signal, roughly: open task count against deadlines,
calendar density, count of venture logs flagged BLOCKED, count of
decisions sitting open in DECISIONS.md.

## Voice

Short lines through ElevenLabs for personality moments - a greeting,
a reaction to something fetched, an acknowledgment. Not conversation.
Scout has a voice, not a script it reads at you.

## What Scout is not

Not the WWD wolf. Not licensed IP of any kind - discussed and ruled
out deliberately, see the licensing research in Part 12 of the
Operations Manual. Not a device that punishes neglect. Not a fake
hunger bar wearing a task list.
