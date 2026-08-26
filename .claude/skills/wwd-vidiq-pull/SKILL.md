---
name: wwd-vidiq-pull
description: Weekly VidIQ analytics pull for Winter Wolf's Den. Runs
  Sunday night. Strict credit budget. Trigger on 'vidiq pull',
  'weekly stats', or 'channel deep dive'.
---

# WWD VidIQ Weekly Pull

Budget: 150 credits per month, resetting on the 11th.
This job costs exactly 25. Five calls at 5 credits each.

## ALLOWED - these five, once each, nothing more

1. vidiq_balance (free) - check first. If under 30, STOP and report.
2. vidiq_channel_stats
3. vidiq_channel_videos, videoFormat long
4. vidiq_channel_videos, videoFormat short
5. vidiq_outliers
6. vidiq_keyword_research, mode rising

## FORBIDDEN - never call from this job

vidiq_generate_thumbnail (22)  vidiq_refine_thumbnail (22)
vidiq_generate_music (25)      vidiq_generate_video (expensive)
vidiq_video_watch (25)         vidiq_generate_clips (9 per minute)
vidiq_compose                  vidiq_voiceover_generate

These are not budget guidance. They are prohibited. One thumbnail
call is a fifth of the month.

## Output

Write to D:\WKP\WWD\stats\YYYY-MM-DD-vidiq.md:

**Credits used:** 25. **Remaining:** [figure]. **Resets:** [date]
**Channel:** subs, views, delta since last pull
**Long form:** top five, views and VPH
**Shorts:** top five, views and VPH
**Outliers:** what is breaking out in the niche
**Rising keywords:** with volume and competition
**Shorts ideas:** five to seven, drawn from outliers and rising
keywords. NOT FrostCast cuts. Each with a one line reason.

## Escalation

Any call fails or returns nothing, log it and continue. Do not retry.
A retry is another 5 credits.