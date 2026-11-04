# WWD VidIQ deep-dive raw pulls, 2026-11-02

Channel: Winter Wolf's Den, UC2BmJmKYi9JozKblfJ_jHsQ (@winterwolfsden). VidIQ signed in via mattkhouriewrites@gmail.com (owner-authorized, so YouTube Analytics API worked).
Credits: balance at start 55 (task brief said about 75; the real balance was 55). Spent 55. Balance now 0. Resets 2026-11-11.
Calls that charged: 11 analytics/video/comment/similar calls at 5 credits each. One subscriber_insights call returned "report generation pending" (no charge) and the retry failed for lack of credits.
Channel public count today: 742 subscribers, 1,087,122 views, 3,493 videos (vidiq_user_channels). Studio page shows 742 and "3.4K videos".

## A. Monthly (YouTube Analytics, month dimension, 2026-05 to 2026-10)
| Month | Views | Engaged views | Minutes watched | Subs gained | Subs lost | Net | Likes | Comments | Shares | Avg view duration (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-05 | 33,740 | 10,166 | 14,391 | 11 | 3 | +8 | 361 | 50 | 15 | 81 |
| 2026-06 | 22,579 | 9,102 | 12,645 | 19 | 6 | +13 | 248 | 28 | 6 | 81 |
| 2026-07 | 30,930 | 14,027 | 18,008 | 11 | 5 | +6 | 432 | 50 | 8 | 75 |
| 2026-08 | 36,725 | 14,636 | 14,498 | 17 | 3 | +14 | 521 | 34 | 1 | 57 |
| 2026-09 | 21,455 | 6,932 | 10,176 | 13 | 4 | +9 | 304 | 37 | 7 | 85 |
| 2026-10 | 14,094 | 4,670 | 12,317 | 6 | 6 | 0 | 295 | 27 | 15 | 156 |
Note: views definition changed 2026-08-27 (about 1.7 to 1.9x higher on long-form), so use engaged views for before and after.

## B. Daily, 2026-08-04 to 2026-10-31 (views, gained, lost, minutes)
Totals for the window: gained 36, lost 13, net +23 (the Oct 4 to Oct 31 slice: gained 6, lost 6).
Days with any loss: 08-16, 08-23, 08-24, 09-06, 09-11, 09-20, 09-26, 10-07, 10-08, 10-16, 10-23, 10-28, 10-29.
Days with 2+ gained: 08-21 (2), 08-22 (2), 09-13 (2), 10-08 (3).
Zero gained from 10-23 through 10-31 (9 days). Lost 10-23, 10-28, 10-29.
Daily views, selected: 08-08 4,013; 08-22 3,383; 09-04..09-07 about 2,000 a day; 10-05 97; 10-06 85; 10-24 1,640; 10-30 1,332; Oct median day about 320.
Average daily views by block: Oct 1-15 about 270; Oct 9-15 327; Oct 16-22 561; Oct 23-31 688.
Full daily rows are in the tool output and were not stored; recompute needs 5 credits.

## C. Content type, 2026-08-04 to 2026-11-01
| Type | Views | Engaged | Minutes | Gained | Lost | AVD (s) | Avg % viewed |
|---|---|---|---|---|---|---|---|
| videoOnDemand (long-form) | 3,816 | 2,022 | 10,094 | 9 | 0 | 298 | 16.6 |
| liveStream (FrostCast and streams) | 2,205 | 823 | 15,572 | 4 | 0 | 1,131 | 20.2 |
| shorts | 63,785 | 22,602 | 10,766 | 15 | 1 | 26 | 50.8 |
| unspecified | 0 | 0 | 0 | 8 | 12 | 0 | 0 |
Subs per 1,000 views: shorts 0.24, long-form 2.36, live 1.81.
12 of the 13 losses in the window sit in "unspecified" (not tied to any content type). Cause not retrievable.

## D. Traffic sources, same window
SHORTS 47,573 (AVD 26s, 52.2%); YT_SEARCH 15,243 (AVD 40s, 14.9%); SUBSCRIBER 3,249 (AVD 1,079s, 32%); YT_OTHER_PAGE 1,470; RELATED_VIDEO 1,151 (AVD 256s, 10%); EXT_URL 511; YT_CHANNEL 230; NO_LINK_OTHER 169; HASHTAGS 94; PLAYLIST 50; NOTIFICATION 46; SHORTS_CONTENT_LINKS 6; SOUND_PAGE 2; END_SCREEN 1.

## E. Subscribed vs not, same window
SUBSCRIBED viewers: 1,679 views, 16,968 minutes, AVD 1,063s, 437 likes, 2 shares.
UNSUBSCRIBED viewers: 68,116 views, 19,463 minutes, AVD 45s, 659 likes, 21 shares.
Subscribers are 2.4% of views and 46.6% of minutes watched.

## F. Per-video, 2026-09-01 to 2026-11-01, sorted by minutes watched (top rows; ID, views, minutes, AVD s, avg % viewed, gained, lost)
CHDOw5FS0C0 FrostCast 110: 310, 1,924, 1,250, 22.4%, 1, 0
kDruxzJffNI FrostCast 117: 157, 1,483, 1,083, 16.1%, 0, 0
JJrECo2y9zk FrostCast 115: 64, 1,462, 2,248, 35.4%, 2, 0
aWlD-14TOvk FrostCast 116: 104, 1,298, 1,555, 23.5%, 0, 0
WG_ijLGBtOw FrostCast 112: 158, 1,227, 1,632, 27.5%, 0, 0
Q1RV2WW8O5w FrostCast 111: 186, 1,095, 1,056, 17.2%, 0, 0
kYsixGzX3PQ FrostCast 118: 248, 1,080, 787, 15.2%, 0, 0
OQIgysPt5pQ Carrie review: 201, 1,055, 569, 24.0%, 0, 0
tU_d49ta-vs Crystal Lake review: 390, 870, 501, 23.4%, 1, 0
CbXSuRQvdoo Heat first watch: 454, 735, 177, 8.3%, 0, 0
sfTT-aERFEc Terminator 2: 329, 579, 242, 11.3%, 2, 0
Odf-DCtiK9I FrostCast 113: 136, 577, 566, 12.7%, 0, 0
vOeZNpWPV10 Clayface review: 205, 521, 230, 17.0%, 0, 0
K89XHcRL9n4 Good Boy: 256, 455, 248, 24.5%, 0, 0
rU72L1R7ZY4 Street Fighter: 246, 449, 424, 34.0%, 0, 0
5uic8suLRrk FrostCast 114: 519, 391, 283, 7.1%, 0, 0
GR7A4iRlNao Other Mommy: 129, 378, 269, 23.5%, 0, 0
kzQibNjH48g Whisper Man: 132, 368, 498, 32.8%, 0, 0
v0BmrD94kow COD Short: 1,046, 359, 43, 121.9%, 0, 0
s9tvpaPKDBA Vision Quest 1+2: 81, 319, 367, 24.5%, 0, 0
RWzwu6eS3rY Vision Quest 3+4: 53, 257, 549, 47.5%, 0, 0 (posted 10-31, young)
UY5YFV5dt0U Undertone: 60, 212, 633, 25.2%, 0, 0
GtwGHXXTEZ4 (title not pulled): 177, 175, 145, 4.8%, 1, 0
Shorts with high views: ajOuGj-vgW4 936; 0pDGh6482XA 1,037; rJ0lhmWrPLc (Stewart tribute) 1,139, 71 likes; p1aeyKBIuFQ 574; CbEZ0KYmBTM 755; Ea7J4A1av_Q 917.
Video-level subs: only 7 gained and 0 lost across the whole Sep 1 to Nov 1 per-video list. All attributed gains came from FrostCast 110, 115 (2), Crystal Lake, T2 (2), and GtwGHXXTEZ4.
Earlier call (Aug 4 to Nov 1, sorted by subs lost): the only video with an attributed loss was fHJCzxjhUUc (476 views, 2 gained, 1 lost, AVD 16s, title not pulled).
The Last House (RdVLW9ljuP4), Aug: 51 views, AVD 388s, 1 gained.

## G. Comments (channel-wide, newest 50 threads, 2026-09-09 to 2026-11-01)
Positive or neutral: T2 ("favourite Terminator film", "that MUSIC"), Crystal Lake "Nice job gents", Stewart tribute RIPs, requests "Need the Clayface review" (10-27), Pendragon Cycle suggestion.
Negative: "These guys are complete dumbasses and their opinions are shit" (Green Lantern Short, 10-26); "You didn't even flop idiot" (FrostCast 118); Mass Effect Short "This clown actually thinks the Veilguard team and the Mass Effect team are the same people" (11-01, a factual correction); Lanterns debate pushback (9-13); "Ralf Finnys" mispronunciation jab (9-24).
Zero comments mention intros, AI footage, audio levels, captions, spoilers or the Vision Quest focus. 50 threads is one page only.

## H. VidIQ similar channels (sorted by 30-day sub growth; field units as returned)
Never Seen It Podcast 366 subs, avg views 616, subsGrowth30d 43.53, viewsGrowth30d 20.55
also podcast 1,000 subs, avg 547, 32.8, 2.59
Southern Fried Cinema Siblings 385, avg 558, 4.9, 8.06
Reel Filmology 1,090, avg 1,188, 4.81, 11.04 (channelType short)
Media Byte 713, avg 910, 2.89, 14.29
The A&J Experience 1,240, avg 577, 2.48, 9.8
Potts Take 493, avg 1,164, 2.07, 2.73
D-WIZZLE 683, avg 248, 1.04, 2.98
Talkin' TV 967, avg 463, 0.94, 2.12
Jeek Nation 396, avg 994, 0.76, 0.61
Myths & Mischief 626, avg 904, 0, 0.96
Regular Exclusive Movies & TV 263, avg 641, -0.38, 0.76
WWD lifetime average: 1,087,122 views / 3,493 videos = about 311 per video.
Not pulled: what these channels do (needs video calls).

## I. Playlists on the channel (from the public Playlists page, scraped via Chrome 2026-11-02)
See D:\WKP\WWD\data\video-inventory.md.

## J. Not retrieved
subscriber_insights (best time to post, audience overlap) pending then out of credits; per-video retention curves; CTR and impressions (not exposed by these calls); hourly first-48h views; age and geography; video transcripts; competitor video detail; Instagram/Facebook data newer than 2026-10-19.
