# Teacher venture: free education resources and LAN course architecture

Date: 2026-11-12. Read-only research. Nothing downloaded, installed, signed up for or posted. "Retrieved" means read from a page or the GitHub API today. "Not verified" means I could not retrieve it. Builds on `research\tools\2026-11-10-batch-B-skills-and-learning.md` (AI Engineering from Scratch, rohitg00, MIT, 542 lessons, verdict MAYBE LATER). That verdict stands for this use: it is an engineer curriculum, too heavy for a beginner wife-on-a-LAN course. Not redone here.

## Key finding on licensing (read first)

Only the AI Fluency materials are both on-topic and possibly reusable, and the sources disagree:
- aifluencyframework.org (retrieved): "All course materials including videos freely available under the CC BY-NC-SA license." Site and framework: copyright 2025 Rick Dakan and Joseph Feller, CC BY-NC-SA.
- academy.claude.com (retrieved): shows only "(c) 2026 Anthropic PBC", no license or reuse terms.
- So: link to Anthropic Academy for the videos. Adapt text only after reading the license on the downloadable OER files. CC BY-NC-SA is fine for a private home course (non-commercial), but adaptations must credit the authors and carry the same license.
- Elements of AI is NOT reusable. Its FAQ (retrieved): "(C) 2018 MinnaLearn and the University of Helsinki, all rights reserved ... may not be reproduced, distributed or transmitted ... without the prior written permission". Link only.

## A. Free AI literacy and prompting courses for non-programmers

| # | Name | URL | Teaches | Level | Format | License or terms as stated | Cost | Use | Fit |
|---|---|---|---|---|---|---|---|---|---|
| 1 | AI Fluency: Framework and Foundations (Anthropic; authors Dakan and Feller) | https://academy.claude.com/ and https://aifluencyframework.org/ | The 4Ds: Delegation, Description, Discernment, Diligence. Working with AI effectively, efficiently, ethically, safely. Academy: 14 lessons, 1 quiz, about 4 h. aifluencyframework.org says 12 lessons, 3 to 4 h (counts differ, not reconciled) | Not stated; reads beginner | Video, reading, quiz, self-paced | aifluencyframework.org: CC BY-NC-SA. Academy page: no terms, (c) Anthropic | Free (no certificate mentioned) | Link now. Adapt only after checking OER file license | HIGH |
| 2 | AI capabilities and limitations (Anthropic Academy) | https://academy.claude.com/ | Mental model of what LLMs can and cannot do. 13 lessons, 1 quiz, about 3.5 h | Not stated | Course | No terms listed, (c) Anthropic | Free | Link only | HIGH (limits, hallucination) |
| 3 | Building effective human-agent teams (beta) | https://academy.claude.com/ | Multi-user AI work, 5 lessons, 45 min | Not stated | Course | No terms listed | Free | Link only | LOW (workplace team focus) |
| 4 | AI Fluency for Students, Teaching AI Fluency, for Educators | https://aifluencyframework.org/ | Framework variants: Students 5 lessons about 3 h; Teaching 7 lessons about 5 to 6 h; Educators 4 lessons about 3 h | Not stated | Course | CC BY-NC-SA per the site | Free | Link; Students variant may suit her | MEDIUM |
| 5 | Elements of AI (Univ. of Helsinki, MinnaLearn) | https://www.elementsofai.com/ | What AI is, how it works, limits, society | Beginner, no coding | Self-paced online | All rights reserved (quoted above) | Free to take | Link only, never copy | MEDIUM (concepts more than hands-on prompting) |
| 6 | OpenAI Academy | not opened | AI foundations, ChatGPT use, workshops | Beginner | Self-paced | Not verified (secondary blogs only, they disagree on sign-up and certificate terms) | Described as free by secondary sources | Link only after checking terms | MEDIUM |
| 7 | Microsoft Learn AI courses | https://learn.microsoft.com | AI fundamentals tracks | Beginner to intermediate | Modules | Reuse terms not verified. A secondary 2026 guide says courses are free with a Microsoft account, exams $99 to $165 | Courses free, exams paid | Link only | LOW to MEDIUM (Microsoft-tool slant) |
| 8 | Google AI Essentials (Coursera) | https://grow.google/certificates/ai-essentials | Everyday AI use at work | Beginner | Video | Not verified | Secondary sources: 7-day trial, then $49 a month, about $100 to $150 total | Skip, costs money | LOW |
| 9 | DeepLearning.AI short courses, AI for Everyone | https://learn.deeplearning.ai | Mostly developer short courses; AI for Everyone is non-technical | Mixed | Video | Not verified. Secondary 2026 guide: videos free, quizzes and certificates need Pro at $25 a month. AI for Everyone price not retrieved | Mixed | Link only | LOW (mostly programmer content) |
| 10 | fast.ai Practical Deep Learning | https://course.fast.ai/ | Coding deep learning | Programmer | Video and notebooks | Conflicting secondary info (Apache vs "Other"); Apache 2.0 is documented for the fastai library, not clearly the course | Free | Skip | LOW (wrong audience) |

## B. Open-licensed content we may legally reuse (licenses retrieved via GitHub API or license text today unless marked)

| Name | URL | What | License | Reuse | Fit |
|---|---|---|---|---|---|
| anthropics/courses | https://github.com/anthropics/courses | 5 notebook courses: API fundamentals, prompt engineering interactive tutorial, real-world prompting, prompt evaluations, tool use. Archived by owner 2026-09-15 (read-only), about 23k stars | CC BY-NC 4.0 (retrieved from LICENSE) | Copy and adapt for noncommercial use with credit | LOW to MEDIUM. Developer notebooks needing an API key and spend; prompting concepts adaptable, format not wife-friendly |
| AI Fluency OER files | https://aifluencyframework.org/ | Source documents, media assets, papers | CC BY-NC-SA (site statement) | Adapt with credit, same license | HIGH |
| microsoft/generative-ai-for-beginners | https://github.com/microsoft/generative-ai-for-beginners | Lessons on building with generative AI | MIT, 123,415 stars, pushed 2026-11-12, not archived | Reuse with notice | LOW (builder audience) |
| microsoft/AI-For-Beginners | https://github.com/microsoft/AI-For-Beginners | 12-week classic AI/ML curriculum | MIT, 70,737 stars, pushed 2026-11-04 | Reuse with notice | LOW (code and math heavy) |
| UVA Fostering AI Literacy (Pressbooks) | https://pressbooks.library.virginia.edu/ai-literacy/ | AI literacy guide, activities | CC BY-NC-SA per search result, not opened | Adapt with credit | LOW (written for college instructors) |
| AI and Metaliteracy OER Toolkit | https://metaliteracy.org/ml-in-practice/how-to-access-the-ai-metaliteracy-oer-toolkit/ | 5 modules, AI and information literacy | CC BY-SA 4.0 per search result, not opened | Adapt with credit | MEDIUM (evaluation skills; audience not verified) |
| MIT AI literacy units | https://c2c.sbcss.net/resources/mit-ai-literacy-units | K-12 AI literacy units | "Creative Commons", variant not verified | Check first | LOW (ages 5 to 18) |
| rohitg00/ai-engineering-from-scratch | see 2026-11-10 report | Engineer curriculum | MIT | Reuse | LOW |

Honest gap: I found no ready-made open course covering hallucination, privacy and scams for adult everyday users. Best plan: write our own short lessons (original text, so we own it) and link out to the free courses for depth.

## C. Platforms and site generators for a LAN

| Name | URL | What | License (retrieved) | Activity | Hardware and difficulty on one Windows 11 PC | Fit |
|---|---|---|---|---|---|---|
| MkDocs Material | https://github.com/squidfunk/mkdocs-material | Static site from Markdown, search, nav. pip install | MIT, 27,611 stars, pushed 2026-11-07 | Active | Trivial. No database. Theme maintenance status not verified | HIGH |
| Quarto | https://github.com/quarto-dev/quarto-cli | Publishing system, websites, books | GPL-3.0 (tool only, our content stays ours), pushed 2026-11-10 | Active | Easy installer, no database | MEDIUM |
| Docusaurus | https://github.com/facebook/docusaurus | Docs site, React, needs Node | MIT, pushed 2026-11-12 | Active | Moderate (Node toolchain) | MEDIUM |
| Jupyter Book | https://github.com/jupyter-book/jupyter-book | Books from Markdown and notebooks | BSD-3-Clause, pushed 2026-11-04 | Active | Easy, notebook focus is overkill | LOW |
| Frappe LMS | https://github.com/frappe/lms | Full LMS: lessons from text, video, quizzes, assignments; progress by batch; certification mentioned | AGPL-3.0, 3,416 stars, pushed 2026-11-12 | Very active | Docs list Docker, Docker Compose and Git, or bench. No official Windows path found, so Docker Desktop or WSL2. RAM minimums not retrieved. Moderate to hard | MEDIUM |
| Moodle | https://github.com/moodle/moodle | Full LMS, quizzes, completion tracking | GPL-3.0, 7,608 stars, pushed 2026-11-12 | Very active | Needs web server, PHP, database. Docs note Windows is poor for large sites, XAMPP bundles unmaintained and may miss version minimums, WSL route exists. Moodle docs page returned 403, so exact requirements not retrieved. Heavy admin for one learner | LOW |
| Chamilo LMS | https://github.com/chamilo/chamilo-lms | Lighter LMS | GPL-3.0, 1,023 stars, pushed 2026-11-13 | Active | PHP and database, smaller community | LOW |
| Open edX | https://github.com/openedx/edx-platform | Large MOOC platform | AGPL-3.0, 8,233 stars, pushed 2026-11-12 | Very active | Heavy multi-service stack; specifics not retrieved | LOW |
| H5P library | https://github.com/h5p/h5p-php-library | Interactive content for LMSs | API returned NOASSERTION ("Other"), not verified | Active | Plugs into an LMS, not stand-alone | LOW |
| Canvas OSS | https://github.com/instructure/canvas-lms | LMS | Not retrieved | n/a | Not checked | LOW |

## D. Responsible-AI and safety modules for a beginner course

Proposed list (our own writing, outside links for depth):
1. What AI is and is not: predicts text, does not "know" (Anthropic "AI capabilities and limitations" for depth).
2. Hallucinations and accuracy: ask for sources, open them, cross-check a second way, never trust a number or quote you did not verify. Exercise: five AI answers, some wrong, she finds the errors.
3. Privacy: what not to paste (SSN, bank numbers, medical details, passwords, other people's private info), account and history settings. Check the provider's current settings pages when writing (not retrieved here).
4. Scams and deepfakes: per FTC and FBI guidance as reported by secondary news sites today, scammers can clone a voice from a short clip. Do not trust the voice, hang up and call back on a known number, treat gift card, wire or crypto requests as red flags, agree a family code word. Report at ReportFraud.ftc.gov and IC3.gov. NOT verified against primary pages; open consumer.ftc.gov and ic3.gov before writing. The "22,364 AI-linked IC3 complaints, about $893 million, 2025" figure came from one news report and is not verified.
5. When NOT to use AI: medical, legal, financial decisions without a professional, anything private, anything where being wrong hurts someone.
6. Good prompting: the 4Ds from AI Fluency as the spine; give context, goal, format, then iterate.
7. Honesty and credit: say when AI helped, do not pass AI text off as personal testimony, check quotes and copyright.
8. Partnership habits: review before sending, the human makes the decision.

## E. Recommended architecture (simplest that works)

Phase 1: MkDocs Material static site plus a tiny Python progress helper.
- Content: one Markdown file per lesson, 15 to 20 minutes each, ending with a "Check yourself" quiz and a "Try it" exercise. Links out to Anthropic Academy and the other free courses for video depth.
- Serve: `pip install mkdocs-material`, `mkdocs build`, then serve the built folder with Python 3.12 (`python -m http.server 8080 --bind 0.0.0.0`, or a small Flask or FastAPI app). Add a Windows Defender Firewall inbound rule for that port, Private network only, and reserve a fixed IP or hostname on the router. Home LAN only, no port forwarding, no internet exposure.
- Quizzes: plain JavaScript multiple choice inside each lesson page, answers and explanations included. No extra service. Free-text "Try it" items are self-checked against a model answer, not auto-graded.
- Progress: (a) simplest, browser localStorage ticks in her browser only; (b) better, the small Python server takes a POST on lesson complete and quiz score and writes one JSON or SQLite file on Zac's PC, so progress survives a cleared browser and Zac can see it (partnership view). Store only pass/fail, score and date.
- Practice: she uses her real AI chat in another tab. The site never holds API keys. Run cost: $0 beyond any AI subscription she already has.
- Upgrade path if the course passes about 15 lessons or Zac wants accounts, grading and certificates: Frappe LMS in Docker Desktop (AGPL-3.0, free). Decide after Phase 1.

Why not Moodle, Open edX or Canvas: built for hundreds of learners, heavy stacks to maintain on Windows, for one learner.

Rough hours (my estimate, not measured):
- Site scaffold, theme, LAN serve, firewall, fixed address: 3 to 4 h
- Progress helper (JSON or SQLite POST, simple admin page for Zac): 4 to 6 h
- Quiz component plus one template lesson: 3 to 4 h
- Write modules 1 to 4 (what AI is, accuracy, privacy, scams) with quizzes and exercises, including fact-check against primary FTC and FBI pages: 10 to 14 h
- Review (qa-director, plus the wife as tester): 3 to 4 h
- Total about 23 to 32 h for a 4-module first course; about 10 h to a working skeleton with one real lesson.

## Open questions for Zac
1. Which AI tool does she use today (ChatGPT, Claude, Gemini, Copilot)? Lessons should show her tool.
2. Reading and quizzes only, or video too? Video means linking to Anthropic Academy or Zac recording short screen captures.
3. Is an always-on small Python server on his main PC OK, or start it only when needed?
4. Should Zac see her progress, or stay private to her browser? She should be asked.
5. Confirm the AI Fluency license by reading the OER download's license page before copying anything (the Academy page shows only (c) Anthropic).
6. Ownership: Teacher folder with a CLAUDE.md, software-director builds, script-room writes the lesson words (org rule), qa-director checks. New venture, so Zac approves it.

## Sources (read 2026-11-12)
- https://academy.claude.com/ and https://aifluencyframework.org/ (WebFetch)
- https://github.com/anthropics/courses and its raw LICENSE (WebFetch)
- https://www.elementsofai.com/faq/how-is-the-content-licensed (WebFetch)
- GitHub API repo endpoints: frappe/lms, moodle/moodle, chamilo/chamilo-lms, openedx/edx-platform, facebook/docusaurus, quarto-dev/quarto-cli, squidfunk/mkdocs-material, jupyter-book/jupyter-book, microsoft/generative-ai-for-beginners, microsoft/AI-For-Beginners, h5p/h5p-php-library
- Search summaries only (secondary, not opened): Frappe install docs, OpenAI Academy, Microsoft Learn, Google AI Essentials, DeepLearning.AI, fast.ai, FTC and FBI voice cloning coverage, Moodle Windows docs, UVA, metaliteracy and MIT OER listings.
Not retrieved: Moodle and Open edX hardware minimums, Canvas OSS license, OpenAI Academy terms, AI for Everyone price, primary FTC and FBI pages, MkDocs Material maintenance status.
