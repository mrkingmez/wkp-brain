# Teacher (opened 2026-11-12, Zac's yes)

A learning venture: a course website on Zac's home network where his wife learns to use AI the right way. Also a partner and learning tool for Zac. Not a business, not public, not for sale.

## Decisions (Zac, 2026-11-12)
- Opened as a venture. Status: ACTIVE, family use only.
- Her starting point: she does not know yet what she wants to use AI for. Course must start from "what is AI good and bad at" and let her find her own uses.
- Runs ONLY when Zac starts it. No always-on server. A static site served by Python uses zero tokens and zero money. Only an optional tutor panel (Claude API) would cost, and it is OFF until Zac says yes with a monthly cap.
- Zac wants to see her progress, BUT she has not been asked yet. Build the progress file locally, keep the viewer switched off until she says yes. Ask her first.

## Rules
- Home network only. Private network firewall rule, never port-forwarded, never on the internet.
- Free tools only. No spending, no signups, no downloads without Zac's yes (state name, source, size).
- Link out to Anthropic Academy, Elements of AI and similar. Copy nothing until the license is verified (AI Fluency OER files: authors say CC BY-NC-SA, Academy page shows only (c) Anthropic, unverified).
- Lessons we write ourselves: accuracy and hallucination checking, privacy, scams and deepfakes, when not to use AI. No open course covers these for adult everyday users.
- Writing rule applies: no em dashes, nothing generic. Lessons go through script-room, then qa-director.
- Honesty rule: no scam or accuracy statistic goes in a lesson unless the primary source was retrieved (FTC and FBI pages not yet verified).
- Local network note: the PAWS "never touch Columbia County network" rule is a PAWS rule, not this one, but keep this site on the home network only.

## Plan
1. Skeleton: MkDocs Material static site, Python 3.12 server, one real lesson, per-lesson JS quiz, progress endpoint writing a local file (about 10 h, estimate).
2. First lesson: "How to check what AI tells you."
3. Four modules: accuracy, privacy, scams, when not to use AI (about 23 to 32 h total, estimate).
4. Later, only with Zac's yes: tutor panel with a capped API budget, or Frappe LMS if the course outgrows about 15 lessons.

## Ownership
software-director builds, script-room writes lessons, qa-director checks, Zac approves. Research: `research\teacher\2026-11-12-education-resources.md`. Code lives in `Teacher\site\`.

## Added 2026-11-12 (Zac: "I want the repo in it, so she can advance, and practical exercises")
- Module 5, Advanced track: links page to rohitg00/ai-engineering-from-scratch (MIT, verified from the repo LICENSE and the GitHub API). Local copy in `vendor\` (gitignored, never run, no pip or npx). Opens after Modules 1 to 4.
- Practice pattern in `PRACTICE-PATTERN.md`. Lesson 1 practice written (3 tasks).
- Unlocking: `unlock_enabled` in `site\config.json`, default true. Progress viewer still OFF.
