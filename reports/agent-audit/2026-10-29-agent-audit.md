# Agent Audit - 2026-10-29

**What was counted:** every time an agent was actually launched, across all 110 saved Claude sessions from 2026-09-28 to 2026-10-29. Launches made by one agent inside another count too. Sessions before 9/28 are not on disk, so older use is not counted. Mentions in logs are not counted, only real launches.

32 agents on the roster. 22 got launched at least once. 10 got launched zero times.

## Never launched (0 in the last month)

| Agent | Why |
|---|---|
| etsy-director | Etsy work is stuck on Zac, not on the agent. The Kingdom Planners shop needs the $29 fee, the budget file is lost, and the listing photos need Zac's screenshots. Its last real run was the 9/24 prep batch. |
| kdp-director | KDP was moved to active-unscheduled on 9/1. By the rules, it is not surfaced. |
| paws-director | PAWS is blocked on PAWS-001 (task source) and PAWS-004 (hours per week). Hardware buying is paused for cost. The 10/15 Scout sim was built in the main session, not through this director. |
| shattered-empire-director | Zac is revising the Story Guide himself, and the rule is to leave it alone. The one book job this month, the dextrocardia research, went through fiction-director instead. |
| military-scifi-director | Stellar Dominion is dormant. |
| devils-advocate | Nothing calls it. The review gates go through script-room, clearance and rights, and devils-advocate isn't in any of those chains. Earlier work used a general-purpose agent as a stand-in when it wouldn't load. |
| dialogue-doctor | script-room only ran 4 times, and none of those runs needed a dialogue pass. |
| graphic-design | It has no image tool that works. Higgsfield is at 0 credits, and Firefly is something Zac clicks himself. So thumbnails and cards go to wwd-vfx, which builds them in Python. |
| video-ugc | The shorts are built by the WWD review pipeline (shorts-factory) and not through marketing, so this agent never gets the job. |
| market-research | marketing-director goes straight to copywriting and social-media. Research went to venture-scout and VidIQ instead. |

## Barely used (1 to 3 launches)

| Agent | Launches | Why |
|---|---|---|
| wwd-music | 2 | No music goes in the videos. Zac adds the intro and outro himself, and the run sheets say no music beds. |
| clearance, originality, room-writer | 3 each | These only run inside script-room, and only one script went through the room this month (the Ian trailer). |
| ebay-researcher | 0 (named once in a log) | The category pick (EBAY-001) was approved 2026-10-24, but the scheduled scans were never set up. Corrected 2026-10-29: an earlier version of this report said EBAY-001 was still open. |

## Most used

wwd-director 21, general-purpose 20, wwd-vfx 10, fantasy-football-director 10, marketing-director 9, wwd-rights 8, social-media 8.

## What this says

1. **Most idle agents are blocked by a decision, not broken.** KP, PAWS, KDP, eBay research and both book directors are waiting on Zac's calls. The main ones are the $29 fee, PAWS-001 and 004, EBAY-001, and the Story Guide.
2. **general-purpose at 20 is a red flag.** That's work landing on a generic agent when a specialist exists. Some of it was before the WWD benches loaded on 10/26.
3. **The marketing departments for visuals (graphic-design, video-ugc) are duplicates in practice.** WWD's own benches do that work. Either wire them into a real job or fold them.
4. **devils-advocate is orphaned.** It should either go into the review gates (for example, one pass before an upload package ships) or be retired.

## Recommendations (Zac's call, nothing changed)

- Answer PAWS-001 and PAWS-004, and set up the eBay researcher routine (EBAY-001 is already approved).
- Add devils-advocate as one pass in the WWD upload package gate, or retire it.
- Fold graphic-design and video-ugc into wwd-vfx and shorts-factory, or give them Etsy and KP image jobs once the shop is live.
- Leave the dormant-venture directors alone. Idle is correct for them.
