---
name: wkp-daily-brief
description: RETIRED 2026-11-12 (Zac, no more daily briefs; only the Monday brief and the Saturday wrap remain). Do not run, do not schedule. Kept for reference. Was - the single-screen daily rundown, ready when Zac walks
  into the office. Short. Trigger on 'daily brief', 'what's today',
  'my day'.
---
 
# WKP Daily Brief

> **RETIRED 2026-11-12.** Zac's call: no more daily briefs. Use `wkp-monday-brief` (Monday) and `wkp-saturday-wrap` (Saturday). Scheduled task `WKP-daily-brief` should be disabled (command in the 2026-11-12 report, Zac or Jarvis runs it).
 
## Shape
This fits on one screen. If it does not fit, it is too long.
The Monday brief is the long one. This is not.
 
## Sections
 
**Today** - date, day of week, weather for Grovetown GA: high, low,
conditions, one line.
 
**Calendar** - today only. Both calendars. Time, title, which
calendar.
 
**Top three** - the three things that actually need doing today,
pulled from TASKS.md and open build steps. Three. Not a list of
everything.
 
**Blocked** - anything waiting on Zac specifically. One line each.
 
**Yesterday** - what completed, one line. Skip the section entirely
if nothing did rather than writing 'no activity'.
 
## Output
Rendered to the dashboard. Also writeable to
D:\WKP\reports\daily\YYYY-MM-DD.md when asked.
 
## Rules
No preamble. No greeting. Start at 'Today'.
No em dashes.
