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


## Her tools (Zac, 2026-11-13)
She has FREE Claude (used once, a prompt Zac wrote to clean out her email) and FREE ChatGPT. Nothing paid. Lessons must work on the free tiers of both, with no paid features, and must not use the shared WWD Firefly/Veo credits. Free-tier limits and image features are unverified until a fact-research pass checks the vendors own pages.

## Restructured 2026-11-13 (Zac: first build was only safety lessons, he found that insulting)
- Home page is now a pick-your-path page with four tracks: 1 Start Here (what AI is, what Claude is, prompting basics to advanced), 2 Make Things (pictures, video, postcards, printables, selling), 3 Build and Automate (advanced end = old Module 5 doorway, `build-automate/advanced.md`), 4 Stay Safe (short).
- Only one lesson exists: "How to check what AI tells you", now `stay-safe/check-what-ai-tells-you.md`, quiz and practice intact. Other Stay Safe lessons are placeholders. Tracks 1 to 3 list working titles as "Coming soon". Writing room writes the lessons after the research report lands.
- `unlock_enabled` is false, nothing locked. Unlock code kept. Progress viewer still OFF.
- Old module-N URLs redirect (301) via `OLD_URLS` in `site\serve.py`. Quiz progress key changed to `stay-safe/check-what-ai-tells-you`.

## Update 2026-11-14 (Zac)
She WILL have a paid version of Claude (plan not yet named by Zac: ask which). Add a "Claude power tools" section covering Projects, Skills and connectors (MCP), written only from primary-source facts about the paid plan, every paid-only feature marked as paid. Earlier lessons stay free-tier safe. The four GitHub repos Zac sent were meant as a scope map ("what people put in their teaching repos") so the course is fully inclusive, not as content to copy. Zac also wants vetted YouTube videos that give correct information, linked per lesson (link only, checked against official docs, dated).

## Answers 2026-11-14 (Zac)
- Her plan: Claude Pro, same as Zac. Her computer: Mac. Real accounts: Zac believes yes, the course may teach connecting her real accounts (his hedged word, "I believe"; confirm with her before she connects anything). Safety design stays: read-only first, one account at a time, approve every action, she decides, never Zac or an agent connecting for her.
- Effect: lessons can name Pro, use Mac steps (Command, TextEdit Make Plain Text, Finder), Mac-only Skill recording in Cowork is now in scope as an optional lesson. Research, Projects, Skills, connectors, memory all assumed available on Pro, still "check your own screen" for menu names and the pack conflicts.
