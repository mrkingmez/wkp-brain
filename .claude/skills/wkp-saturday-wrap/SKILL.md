---
name: wkp-saturday-wrap
description: The Saturday week-wrap (added 2026-11-12, replaces the daily brief). What got done this week, what rolls to next week, Etsy/KP/WWD numbers only if data exists, fantasy week recap, top 5 open decisions, next week's calendar preview. Saves a .docx to D:\WKP Reports\Saturday Wrap\ and the .md to reports\saturday\. Trigger on 'saturday wrap', 'week wrap', 'wrap the week'.
---

# WKP Saturday Wrap

One week closed out, one week previewed. Runs Saturday morning. The Monday brief is the long forward-looking brief, this is the short backward-looking one. Zac has ADHD: tight, scannable, one screen per section, no padding. No em dashes, nothing generic. Internal document (exempt from no-ai-slop), but keep the voice plain.

## Sections (in this order)

1. **Done this week.** Pull from `TASKS.md` rows marked Done with a date in the last 7 days, `logs\*.md` entries dated in the window, and `git log --since="7 days ago" --oneline`. One line each, grouped by venture. Skip a venture with nothing rather than writing "no activity".
2. **Rolls to next week.** TASKS.md rows that are In Progress, Not Started with a date this coming week, or Blocked/Waiting on Zac. Say what each is waiting on.
3. **Numbers.** Etsy (WarriorKingDesigns and Kingdom Planners), WWD/YouTube, Instagram/Facebook. HONESTY RULE: only report a number that sits in a file under `D:\WKP\data\` dated within the last 10 days (Etsy is manual: `etsy-manual-YYYY-MM-DD.md`, typed by Zac, never exported). If the newest file is older, print "not available, last data file <name> dated <date>". Never estimate. Name the file next to every figure.
4. **Fantasy recap.** From `Fantasy-Football\LOG.md` and `Fantasy-Football\tracker\predictions.csv`: the week's lineup call, the pick'em card record, what the model got right and wrong. Honest hit rate, not a vibe. If scores are not in yet, say so.
5. **Open decisions, top 5.** From `logs\DECISIONS.md` entries with Status OPEN. Rank by money first, then public posting, then things blocking other work. Each: ID, one-line question, recommendation. Zac answers, nobody else.
6. **Next week's calendar.** Read both Google calendars (WWD calendar and personal) for Sunday through Saturday ahead via the calendar tools. List fixed commitments: FrostCast Wednesday 9 PM, release dates, fantasy lineup locks, deadlines in TASKS.md (e.g. Dec 1 VA tables). If the calendar tool is unavailable, say "calendar not available" and use only the dated TASKS.md rows.
7. **One recommendation.** One line: the first thing to do Monday and why.

## Output

- Working source: `D:\WKP\reports\saturday\YYYY-MM-DD-saturday-wrap.md` (git-tracked).
- Deliverable for Zac: `D:\WKP Reports\Saturday Wrap\YYYY-MM-DD - Saturday Wrap.docx` (the one place Zac looks, per root CLAUDE.md "Output document format"). Convert the .md with `python D:\WKP\.claude\skills\no-ai-slop\scripts\md_to_docx.py <in.md> <out.docx>`.
- Log one line in `logs\` that it ran. Do not commit or push unless asked.

## Do not

- Run on a day other than Saturday unless Zac asks.
- Invent a figure, a score or a calendar event. Name the source or say "not available".
- Surface DORMANT or ACTIVE-UNSCHEDULED ventures (root CLAUDE.md) unless they changed this week.
- Alert-engineer a missed run. A skipped week is acceptable occasionally (Zac, 2026-11-12).
