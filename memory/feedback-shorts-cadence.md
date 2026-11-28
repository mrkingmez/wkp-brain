---
name: feedback-shorts-cadence
description: FrostCast shorts posting cadence, locked 2026-11-11, FB+IG cut to two per day by Zac 2026-11-26
metadata:
  type: feedback
---

Zac, 2026-11-11, furious, said "for the final time": for FrostCast video shorts, YouTube is one a day INCLUDING Thursday, posted 6 to 7 PM. Facebook and Instagram: Thursday one post at 6 PM, then 4 to 5 posts a day Friday through Tuesday, and Wednesday only one morning post and one afternoon post. Find the best time for each post each day. Use the caption set format made the week before (EP 119 approved-copy JSON).

**CHANGE (Zac 2026-11-26): FB+IG two per day only** (every day Thu to Wed, so 14 clips a week), so only the best clips are seen. YouTube Shorts unchanged: one a day, 6 to 7 PM. Built into `WWD/opusclip/build_plan_csv.py --fbig-per-day 2` (default); the older 4 to 5 a day pattern is the superseded rule and schedule_week.py was not changed. Pick by Opus score plus the team's read, keep unverified numbers out of captions, spoilers late in the week.

**Why:** The scheduler script (schedule_week.py) still ran the old 31-slot heatmap and "IG +45, FB +90 after YouTube" stagger, and CLAUDE.md still said "31-slot volume locked", so the agents kept proposing the wrong plan. He had told us before and it did not stick.

**How to apply:** Before any shorts plan, read the cadence in root CLAUDE.md step 7. A week needs about 23 to 28 clips cleared for FB and IG (7 of them also go to YouTube). If fewer clear, say so and fix the pool, do not shrink the cadence. Never use the 31-slot SLOTS table. Links: [[feedback-own-the-operation]].
