# WWD Subscriber Loss Deep Dive

Date: 2026-11-02. Scope: read-only. Nothing was posted, edited or changed on any platform. Internal report, exempt from the public-copy writing rules.
Raw pulls: `D:\WKP\data\wwd-vidiq-deepdive-2026-11-02.md`. Companion files: `D:\WKP\WWD\data\video-inventory.md`, `D:\WKP\WWD\data\post-times.md`.

## 1. Headline

The premise needs one correction before the diagnosis. YouTube Analytics (owner access, through VidIQ) does NOT show more subscribers lost than gained over the last 90 days. It shows 36 gained and 13 lost from 2026-08-04 to 10-31, net +23, and 77 gained and 27 lost from May through October, net +50. The channel count moved 744 on 10-26 to 742 today.

What is true, and is the real problem:
- Gains collapsed. Monthly gains went 17 (Aug), 13 (Sep), 6 (Oct) while monthly losses crept 3, 4, 6. October net is 0.
- The last 9 days (10-23 to 10-31) had 0 gained and 3 lost.
- 12 of the 13 losses in the 90-day window are not tied to any video or content type, so they cannot be matched to an upload.
- The scale is tiny. At 742 subscribers, 6 losses a month is 0.8%. One subscriber is 0.13% of the channel. Single days are noise.

The structural cause: the channel gets 91% of its views from Shorts that convert at 0.24 subscribers per 1,000 views, while the long-form and live videos convert at about 2.4 and 1.8 per 1,000 but pull only 3,816 and 2,205 views in 90 days. Views are not the problem. Almost nobody who watches is positioned to subscribe.

## 2. The facts

### 2.1 Channel trend (YouTube Analytics, owner-authorized)

| Month | Views | Engaged views | Minutes | Gained | Lost | Net |
|---|---|---|---|---|---|---|
| May | 33,740 | 10,166 | 14,391 | 11 | 3 | +8 |
| Jun | 22,579 | 9,102 | 12,645 | 19 | 6 | +13 |
| Jul | 30,930 | 14,027 | 18,008 | 11 | 5 | +6 |
| Aug | 36,725 | 14,636 | 14,498 | 17 | 3 | +14 |
| Sep | 21,455 | 6,932 | 10,176 | 13 | 4 | +9 |
| Oct | 14,094 | 4,670 | 12,317 | 6 | 6 | 0 |

- Views fell 62% from August to October; engaged views fell 68%. YouTube changed its view count on 2026-08-27 (about 1.7 to 1.9x more views on long-form), which should have pushed later months UP, so the decline is understated if anything.
- The Aug and early Sept highs come from a handful of spike days (Aug 8: 4,013 views; Aug 22: 3,383; Sept 4 to 7 about 2,000 a day). Which Shorts caused them was not pulled. October has no spike days until 10-24 and 10-30.
- Minutes watched held up (12,317 in Oct vs 14,498 in Aug), because long-form and FrostCast minutes carry it. Average view duration rose from 57s to 156s as the Shorts share fell.
- Today: 742 subscribers, 1,087,122 lifetime views, 3,493 videos, lifetime average about 311 views per video.

### 2.2 Who is watching

- Window 2026-08-04 to 11-01: 68,116 views from non-subscribers (average 45 seconds) and 1,679 from subscribers (average 1,063 seconds).
- Subscribers are 2.4% of views and 46.6% of minutes watched. The 742 are the real audience, and they are small.
- Traffic: Shorts feed 47,573, YouTube search 15,243 (average view 40s), subscriber feed 3,249, other YouTube pages 1,470, related videos 1,151, external 511, channel page 230, playlists 50, notifications 46, end screens 1.
- The end screen driving 1 view in 90 days is a finding by itself. Cards and end screens are not moving anyone.

### 2.3 Shorts vs long vs live (Aug 4 to Nov 1)

| Type | Views | Minutes | Avg view | Gained | Lost | Subs per 1,000 views |
|---|---|---|---|---|---|---|
| Shorts | 63,785 | 10,766 | 26s (50.8%) | 15 | 1 | 0.24 |
| Long-form | 3,816 | 10,094 | 298s (16.6%) | 9 | 0 | 2.36 |
| Live (FrostCast) | 2,205 | 15,572 | 1,131s (20.2%) | 4 | 0 | 1.81 |
| Unspecified | n/a | n/a | n/a | 8 | 12 | n/a |

- Shorts bring 15 of the 28 attributable gains and only 1 of the 13 losses. By attribution, Shorts are not the direct source of unsubscribes. They are a weak source of subscribers.
- Long-form and live earn 70% of watch time from 8% of views.

### 2.4 Uploads vs subscriber movement (days matched to nearest uploads; times ET)

| Subscriber event | Nearest uploads | Read |
|---|---|---|
| 8/16 lost, 8/23 lost, 8/24 lost | Shorts spike days 8/21 to 8/24 (2 gained 8/21, 2 gained 8/22) | gains and losses on the same Shorts-driven days |
| 9/6 lost | 9/4 to 9/7 Shorts spike (about 2,000 views a day); Whisper Man posted 9/7 | same pattern |
| 9/11, 9/20, 9/26 lost | no long upload nearby | unexplained |
| 10/5 gained 1 | none | |
| 10/7 lost 1, 10/8 gained 3 lost 1 | Heat posted 10/6 9:30 PM, FrostCast 115 live 10/7 and VOD 10/8 | FrostCast 115 has 2 attributed gains, the most of any video; Heat 0 |
| 10/16 lost | FrostCast 116 VOD 10/15; the 5-Shorts-a-day run starts about 10/16 | |
| 10/21, 10/22 gained 1 each | Crystal Lake review 10/21 9:00 AM | Crystal Lake has 1 attributed gain |
| 10/23 lost | Shorts burst; VQ 1+2 review posted 10/24 | 0 gains 10/23 to 10/31 |
| 10/28 lost, 10/29 lost | Clayface review 10/27 11:00 AM; FrostCast 118 live 10/28 night, VOD 10/29 | EP118 has the hostile "You didn't even flop idiot" comment |

Only seven gains and zero losses attach to any video in the Sept 1 to Nov 1 per-video list: FrostCast 110 (1), FrostCast 115 (2), Crystal Lake (1), Terminator 2 (2), and one video whose title was not pulled (GtwGHXXTEZ4, 1). The one video with an attributed loss in the full window is fHJCzxjhUUc (476 views, average view 16s, 2 gained, 1 lost, title not pulled). So the sub movement cannot be tied to a specific bad video. Everything about specific uploads below is correlation on very small counts.

### 2.5 Per-video (Sept 1 to Nov 1; views, average view, percent of video watched, subs gained)

| Video | Views | Avg view | % viewed | Gained |
|---|---|---|---|---|
| FrostCast 110 | 310 | 20:50 | 22.4 | 1 |
| FrostCast 115 | 64 | 37:28 | 35.4 | 2 |
| FrostCast 112 | 158 | 27:12 | 27.5 | 0 |
| FrostCast 116 | 104 | 25:55 | 23.5 | 0 |
| FrostCast 117 | 157 | 18:03 | 16.1 | 0 |
| FrostCast 118 | 248 | 13:07 | 15.2 | 0 |
| FrostCast 114 | 519 | 4:43 | 7.1 | 0 |
| Heat first watch (35:26) | 454 | 2:57 | 8.3 | 0 |
| Terminator 2 (35:37) | 329 | 4:02 | 11.3 | 2 |
| Crystal Lake (35:44) | 390 | 8:21 | 23.4 | 1 |
| Carrie (39:30) | 201 | 9:29 | 24.0 | 0 |
| Street Fighter (20:47) | 246 | 7:04 | 34.0 | 0 |
| Clayface review (22:41) | 205 | 3:50 | 17.0 | 0 |
| Other Mommy (19:07) | 129 | 4:29 | 23.5 | 0 |
| Good Boy (16:53) | 256 | 4:08 | 24.5 | 0 |
| Whisper Man (25:22) | 132 | 8:18 | 32.8 | 0 |
| Vision Quest 1+2 (25:00) | 81 | 6:07 | 24.5 | 0 |
| Vision Quest 3+4 (19:18, posted 10/31) | 53 | 9:09 | 47.5 | 0 |

CTR, impressions and retention curves were not available from these calls. They are in Studio.

## 3. Content analysis

- **What gains subscribers:** FrostCast (3 of the 7 video-attributed gains came from episodes 110 and 115) and classic or search-friendly reviews (Terminator 2: 2, Crystal Lake: 1). These are the videos where viewers watch 20+ minutes. A subscriber needs a reason to expect more, and long watching is that reason.
- **What does not:** Shorts (0.24 per 1,000), series coverage that has no search demand (Vision Quest 1+2: 81 views and 0 gains after 8 days, the weakest October review).
- **Topic drift:** Vision Quest and Clayface are Marvel and DC and are on brand. The drift is in the Shorts batch. Of the 50 Shorts from 10-23 to 11-03, topics include sports streaming (five Shorts, 3 to 8 views each), Halloween decorations and costumes (3 and 12 views), BioWare and Mass Effect, Narnia, Netflix layoffs, Call of Duty, AI fan fiction, a cult mystery. 32 of 50 sit at 35 views or less. The Call of Duty Short is the second most viewed (1,048 views) and sits outside the nerd-verse core; it brought 0 subs that we can attribute.
- **Cadence and bursts:** Shorts went to about 5 a day from 10-16 (50 Shorts in about 10 days), alongside 8 long reviews in 20 days and the weekly FrostCast. Daily views went from about 330 (Oct 9 to 15) to about 560 (Oct 16 to 22) to about 690 (Oct 23 to 31), roughly 1.7 to 2x, but gains went from 4 (Oct 1 to 15) to 2 (Oct 16 to 31) and losses from 2 to 4. The volume lifted views and did not lift subscribers.
- **Spoiler Shorts:** the Ultron Short was held per the notes. Nothing in the data tests the spoiler hypothesis.
- **Title and thumbnail vs delivery:** Heat (8.3% watched, average view 2:57 of 35:26) and Terminator 2 (11.3%) pull search traffic and lose most of it early. The Heat title leads with "Why Winter Wolf Says They Cannot Make Movies Like This Anymore" which may not match what a person searching "Heat 1995" wants. The Clayface review (17.0%, 3:50 of 22:41) caught the searching crowd but did not hold it. CTR is not available, so the promise-versus-delivery read is a hypothesis only.
- **Production flaws we flagged internally (stuck captions, black tails, trailer flash with a platform bug, AI-footage opener, long intros, audio levels):** no comment in the 50 threads pulled mentions any of them, and Vision Quest 3+4 (with the Firefly opener) has the best percent-watched of the set (47.5%, young and small). No evidence they cause loss. No evidence they do not; retention curves were not pulled.
- **Comments:** 50 threads from 9-09 to 11-01. Positive: T2 ("that music"), Crystal Lake ("nice job gents"), Stewart tribute, a request for the Clayface review, a series suggestion. Negative: "These guys are complete dumbasses" (a Green Lantern Short), "You didn't even flop idiot" (FrostCast 118), a factual-error jab on the Mass Effect Short (confused the Veilguard and Mass Effect teams), Lanterns pushback (9-13), a name mispronunciation jab (9-24). The hostile comments are on DC-critical Shorts and FrostCast 118, i.e. the verdict-first, DC-negative takes. The sample is one page and the negative ones are 5 of 50.

## 4. Audience and competitors

- Who is leaving: not available. subscriber_insights (overlap, best time, activity) was still generating on the first call and the retry had no credits. Age, geography, returning-viewer split and per-video "subscribers lost" were not pulled.
- Peers VidIQ matched to us (all small): Never Seen It Podcast (366 subs, average 616 views a video, 30-day growth reported 43.5), also podcast (1,000 subs, 32.8), Southern Fried Cinema Siblings (385, 4.9), Reel Filmology (1,090, 4.81, Shorts-focused), Media Byte (713, 2.89), The A&J Experience (1,240, 2.48). Peers' average views per video are 250 to 1,190 against our 311 lifetime. Two podcast-style channels lead growth. Why they grow was not checked (needs video pulls). Our 30-day growth is +0.4% (3 on 741).
- Outside sources (search results; the pages were not fully opened, and several are creator blogs, not research):
  - vidIQ's "6 Honest Reasons You Might Be Losing YouTube Subscribers" (https://vidiq.com/blog/post/losing-youtube-subscribers/): some churn is normal even on large channels; people unsubscribe when a channel keeps appearing in their feed and they will not watch.
  - subscribr.ai, miraflow.ai and ytgrowth.io posts on Shorts: Shorts are discovery, not loyalty; Shorts viewers and long-form viewers are largely different people; Shorts subscribers do not follow into long-form. One secondhand citation of a 2024 academic study claims long-form views fell after Shorts arrived; I could not verify it.
  - A vidIQ-hosted discussion (rosetta.to) notes subscriber growth did not recover after Shorts player changes in March 2026. One creator's view.
  - Net: these support the pattern we see, they do not prove it for WWD.

## 5. Hypotheses ranked by evidence

| # | Hypothesis | Strength | Data behind it | Confirming test |
|---|---|---|---|---|
| 1 | Almost no viewer is in a position to subscribe: 91% of views are 26-second Shorts or 40-second search views from non-subscribers, converting at 0.24 and about 2 per 1,000 | STRONG | 2.3 to 2.4 above; subscribed viewers are 2.4% of views | Add subscribe asks to long-form, then watch subs per 1,000 long-form views (baseline 2.4) |
| 2 | Gains fell because long-form and FrostCast discovery is thin and decays (reviews 50 to 450 views, FrostCast 30 to 310), not because losses surged | STRONG | Gains 17, 13, 6; losses 3, 4, 6; engaged views down 68% Aug to Oct | Track weekly long-form views and gains side by side |
| 3 | Search-evergreen and FrostCast content produces the subscribers; series coverage and clip Shorts do not | MEDIUM | 7 attributed gains: FrostCast 110/115, T2, Crystal Lake; VQ 1+2 weakest October review | Next two classic or first-watch reviews vs next two series reviews |
| 4 | The October Shorts burst (about 5 a day, partly off-niche) raised views and did nothing for subscribers, and may bring low-intent viewers | MEDIUM to WEAK | Views 330 to 690 a day; subs +4/-2 then +2/-4; 0 gains the last 9 days; 32 of 50 Shorts under 36 views | Cut to 1 on-niche Short a day for 4 weeks and compare weekly net subs |
| 5 | Retention on search-driven reviews is poor (Heat 8%, T2 11%, Clayface 17%) so the algorithm sends little more traffic, and viewers do not stay long enough to subscribe | MEDIUM | 2.5 table; CTR and curves not available | Pull Studio retention curves for those three, rewrite the first 30 seconds on the next two reviews |
| 6 | Opinionated DC-critical takes draw drive-by hostile viewers from the Shorts feed, then they leave | WEAK | 5 negative of 50 comments, all on DC takes; no unsub link | Studio "subscribers lost by video" card plus comment tracking |
| 7 | Unattributed losses (12 of 13) are partly outside our control (inactive or deleted accounts, YouTube cleanups, deleted videos) | WEAK | Entire 12 sit in "unspecified"; not verified | Ask: was any video deleted or made private around 8/16, 8/23, 8/24, 9/6, 9/11, 9/20, 9/26, 10/7, 10/8, 10/16, 10/23, 10/28, 10/29? Check Studio subscriber list |
| 8 | Production flaws (stuck captions, black tails, blurred or unblurred logo flash, AI opener, long intros, audio) are driving people off | WEAK, no evidence either way | No comment mentions them; VQ 3+4 retention is fine | Retention-curve drop points on those videos in Studio |
| 9 | Spoiler Shorts or Shorts/title mismatch cause unsubscribes | WEAK, untested | Nothing in data | Not testable without per-video lost counts |

## 6. Recommendations (all reversible, all free)

1. **Shorts diet for 4 weeks.** Cap Shorts at 1 a day, only DC, Marvel, Vision Quest, Clayface or the week's review, and drop sports streaming, Halloween, BioWare, Narnia and Netflix-news Shorts. Keep going through the writing room and marketing gates. Measure weekly net subscribers (gained minus lost), total Shorts views, long-form views. Baseline: last 4 weeks net +0; target net at least +3 a week with long-form views not falling. Revert if total engaged views drop more than 30% with no gain change.
2. **Put the subscribe ask where watching peaks, not at the end.** Spoken ask (Zac's warm-connective voice) on the first strong joke or verdict, a pinned comment, and a real end screen with a real next video and a playlist. End screens produced 1 view in 90 days, so there is no baseline to lose. Measure subs per 1,000 long-form views (baseline 2.36). Needs Matt's OK as a show-format change.
3. **Link Shorts to long videos.** Every Short gets the "related video" link to its full review or episode, and a pinned comment pointing to it. Measure related-video views (baseline 1,151 in 90 days) and long-form views from Shorts.
4. **Time reviews to the search window.** For new releases, publish within 24 hours of the hosts recording, before or at the search peak. Clayface's review went up 10-27 as search interest was already peaking. Measure first-7-day views and search-sourced views against the October review average of about 285.
5. **Repair the first 30 seconds on the search reviews.** Pull Studio retention curves for Heat, T2 and Clayface (free), find the first big drop, and test a shorter hook and title that matches the search intent on the next two reviews. Measure percent watched vs the current 24% middle of the pack.
6. **Treat series coverage as a test, not a default.** Vision Quest 1+2 got 81 views in 8 days. Try one combined season wrap review at the finale instead of per-pair reviews and compare views and gains to the pair reviews. Matt and Zac's call (partnership). Measure views at day 7 and attributed gains.
7. **Run a timing test and read Studio's audience clock.** Get "When your viewers are on YouTube" from Studio today, then put two comparable reviews in different slots. Details in `post-times.md`. Weak signal at our size, do not over-read.
8. **Close the data gaps (free, before 2026-11-11).** From Studio: subscribers lost by video, audience returning vs new, retention curves, impressions CTR for the last 8 reviews, and confirm no videos were deleted on loss days. On 11-11 spend credits on subscriber_insights and per-video hourly stats.

## 7. What could not be retrieved

- Credits: started with 55 (the brief said about 75), spent 55, balance 0, resets 2026-11-11. 11 charged calls.
- subscriber_insights (audience overlap, best-time windows): pending, then no credits.
- Per-video retention curves, CTR, impressions, hourly first-48-hour views, age and geography, per-video subscribers lost beyond the sorted lists, video transcripts, competitor video detail, Facebook data, Instagram data after 2026-10-19.
- Playlist URLs and IDs (the page text gave names and counts only; scripting the page was blocked).
- Titles for five video IDs that appear in the analytics (fHJCzxjhUUc, GtwGHXXTEZ4, 0pDGh6482XA, ajOuGj-vgW4, CbEZ0KYmBTM).
- Which Shorts caused the Aug 8, Aug 22 and early Sept view spikes.
- Why the 12 unattributed losses happened.
