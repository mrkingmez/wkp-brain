# last30days brief: Robert Pattinson James Bond
Date: 2026-11-17. Window the engine used: 2026-10-18 to 2026-11-17. Run by the last30days-researcher spec (run through a general-purpose agent until the spec loads). Engine v4.3.2, commit a854f3bc.

## Question
Zac heard Robert Pattinson was named the new James Bond. Is it true, who is reporting it, and what are people saying? Do not assume it is true.

## Short answer
Four news outlet headlines say it is official, all dated 2026-11-16: the Guardian, Variety, Sky News and BBC (seen as links shared on Hacker News). Video coverage on YouTube is dated 2026-11-16 and 2026-11-17. So it is not a rumor in the sources the engine reached. Caveat: the engine returns headlines and snippets, not article bodies. I did not open the outlet pages (this agent's only job is last30days), so each outlet claim below is "headline seen", not "article read". fact-research should read the Variety or BBC page before anything public repeats details.

## How it ran
- Run 1: `--quick`, five free sources requested. The engine reduced the plan to one subquery and only Reddit and Hacker News ran. Result: 4 HN items, Reddit 0. About 7 seconds.
- Run 2: default depth, same plan (3 subqueries, five sources requested). 38.3 seconds engine time, 39 seconds wall clock. Results below.
- Guardrails followed: GEMINI_API_KEY and GOOGLE_API_KEY unset, no keys, cookies off, robots respected, output only in D:\WKP\scratch\last30days\out, no publish, no wizard.

## Per-source counts (run 2)
| Source | Returned | Engagement | Notes |
|---|---|---|---|
| YouTube (yt-dlp) | 12 videos, transcripts for 4 of 12, comments for 3 | 2,980,761 views, 90,649 likes, 10,099 comments | Worked. Two videos had no captions. |
| Hacker News | 5 stories | 101 points, 100 comments | Worked. Carries the outlet links. |
| Polymarket | 12 markets | odds only | Worked, but none is about Bond casting (see below). |
| GitHub | 3 items | 1 comment | Noise: automated issues in one podcast app's repo that mention the headline. Not evidence. |
| Reddit | 0 | none | Not reachable: Brave and Startpage throttled, DDG empty, no listings. |

## Confirmed (headline from a news outlet, dated 2026-11-16)
All four arrived as Hacker News posts linking to the outlet. I saw titles and HN comments only.
1. Guardian, "New James Bond Announced and the Name's Pattinson, Robert Pattinson", 2026-11-16, 40 pts, 47 comments on HN. https://www.theguardian.com/film/2026/nov/16/new-james-bond-announced-and-the-names-pattinson-robert-pattinson
2. Variety, "Robert Pattinson Is Officially James Bond", 2026-11-16, 41 pts, 50 comments. https://variety.com/2026/film/global/robert-pattinson-new-james-bond-007-1236946655/
3. Sky News, "Robert Pattinson confirmed as new James Bond", 2026-11-16, 4 pts. https://news.sky.com/story/robert-pattinson-confirmed-as-new-james-bond-13612738
4. BBC live page, "Robert Pattinson is the new James Bond", 2026-11-16, 13 pts. https://www.bbc.co.uk/news/live/ckg5j69ndv2vt

Corroborating but second-hand (not outlets): Looper's video quotes Pattinson thanking director Denis Villeneuve ("James Bond is one of the most legendary characters in cinema and to be entrusted with 007 is the honor of a lifetime"). WatchMojo's transcript says he was "officially announced as the next Bond in November 2026" and that Amazon MGM oversees Bond 26. A Hacker News commenter says Villeneuve will direct and Steven Knight is involved. These details come from auto-generated transcripts and a forum comment, so they are unverified until a primary source is read.

## Rumor, speculation and opinion (do not present as fact)
- WatchMojo transcript: Josh O'Connor, Callum Turner, Jack Lowden and Nicholas Hoult "reportedly in the running" before the announcement. Reported by a video channel, auto-transcript spelling is garbled. Rumor.
- Beyond The Trailer (122,995 views, live stream): talks about Batman and DC implications and a viewer poll ("73% positive"). Opinion and an audience poll, not data on the public.
- A video titled "007 JAMES BOND Official Teaser (2028) Robert Pattinson" appeared (comment by @Mahone2010, 1,500 likes). The title says "Official Teaser" but nothing in the results shows an official source. Treat as fan-made or clickbait until proven. Do not cite as a real teaser.
- Fan comment mood is mixed: top comments joke ("AI won't take our job, Robert Pattinson will", 4,300 likes) or complain ("ABSOLUTELY HATE IT"). HN commenters mostly approve, with the point that the franchise skipped an unknown actor and went with a bankable star.

## Top items (YouTube, all dated within the window)
| Date | Channel | Title | Views | Link |
|---|---|---|---|---|
| 2026-11-16 | James Bond 007 | Robert Pattinson is James Bond | 1,766,526 (68,681 likes, 5,400 comments) | https://www.youtube.com/watch?v=K3elJwmxsRA |
| 2026-11-16 | Looper | Robert Pattinson's James Bond Casting Has Everyone Saying The Same Thing | 183,539 | https://www.youtube.com/watch?v=5FRjAjRrAow |
| 2026-11-17 | Lessons in Internet Culture | Robert Pattinson Is James Bond | 167,747 | https://www.youtube.com/watch?v=45rvv2VxSDA |
| 2026-11-16 | Beyond The Trailer | Robert Pattinson cast as James Bond - REACTION & FULL BREAKDOWN! Goodbye, Batman?! | 122,995 | https://www.youtube.com/watch?v=EK2ouHnrwNo |
| 2026-11-17 | WatchMojo.com | 3 Reasons Robert Pattinson Will Be A Great James Bond | 40,599 | https://www.youtube.com/watch?v=ITIsvT-ubuw |
| 2026-11-17 | The Rogue Director | New James Bond Actor Robert Pattinson (Official Reaction Video) | 477 | https://www.youtube.com/watch?v=ph7F94agNr8 |

The channel "James Bond 007" is a franchise-named YouTube channel. Its ownership was not checked, so I do not call it official.

## Polymarket
12 markets returned, none about the Bond casting. They are Oscar, Golden Globe and Google-search markets that name Pattinson (for example Best Actor nominations 36%, Golden Globes Best Actor Drama nominee 64%, #1 searched actor on Google 2026 at 14.2%). Not evidence on Bond. Odds are as the engine printed them on 2026-11-17.

## What the engine could not reach
- Reddit: 0 items. Reddit is the usual home of casting discussion and is missing from this brief.
- X, TikTok, Instagram, Facebook: not in the free source set.
- The text of the news articles themselves (the engine gives headlines and snippets).
- Transcripts for 2 of 6 videos tried (no captions).
- No official studio or Amazon MGM source was returned. None of the four outlet items is a studio press release.

## Hand to fact-research
Open the Variety and BBC pages and confirm: the announcement date and who announced it, the director, the release window, and the rumored shortlist. Nothing public should carry these details until that is done.

## Verdict on last30days
It earned its place on this test, with one condition. The first test returned almost nothing (Reddit 403, Hacker News only). This time, default depth returned 32 items from four sources in 39 seconds. It found the four outlet headlines, the date (2026-11-16), real audience numbers (about 3 million YouTube views across the 12 videos) and a spread of opinion, and it surfaced a suspicious "official teaser" video. The condition: use default depth, never `--quick` (quick dropped YouTube, Polymarket and GitHub entirely), and plan for Reddit coming back empty. Weak spots: GitHub returns junk for news topics, Polymarket only helps when a market exists, and it cannot confirm anything by itself, so every brief ends with a fact-research hand-off.

Raw files in D:\WKP\scratch\last30days\out\: pattinson-bond-stdout.md and pattinson-bond-stderr.log (run 1), pattinson-bond-run2-stdout.md and pattinson-bond-run2-stderr.log (run 2), robert-pattinson-james-bond-raw-2026-11-17.md (raw).
