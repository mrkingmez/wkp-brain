---
name: marketing-sponsors
description: "WWD sponsor/affiliate deal handling and marketing department structure — Surfshark terms, and Zac's rule for how to frame POW/MIA content."
metadata: 
  node_type: memory
  type: project
  originSessionId: a563d0ca-2570-462a-b6b9-d1507d02c753
  modified: 2026-09-14T17:34:29.295Z
---

## Surfshark affiliate deal — WWD's first sponsor [2026-09-14]
Not a flat-fee sponsorship — a revenue-share affiliate program (approved
2026-09-11, thewinterwolfsden@gmail.com). VPN 40% rev share, Antivirus 60%,
Adblock 60%. Payout threshold $100 net (~5 conversions). **No discount code
exists** — it's link-based tracking only via `aff_id` in the URL, so sponsor
reads should point to "the link in the description," never a spoken code.

Surfshark's onboarding email had a bug — the first tracking links used the
wrong `aff_id` (1768) and got corrected same-day to `aff_id=47475`. Always
use the corrected links:
- VPN: `https://get.surfshark.net/aff_c?offer_id=926&aff_id=47475`
- Antivirus: `https://get.surfshark.net/aff_c?offer_id=934&aff_id=47475`
- Adblock: `https://get.surfshark.net/aff_c?offer_id=1498&aff_id=47475`

Zac says there's a 90-day cookie window and real money riding on it (his
info — not independently re-verified against Surfshark's T&Cs page, since
the link wasn't extractable from the source email PDF). Full sponsor-read
scripts and the week's social calendar live at
`L:\Winter Wolfs Den review show\Sponsors\Surfshark\` and
`L:\Winter Wolfs Den review show\2026-09-14 Week of Sep 14\04 Upload Packages\`.

**How to apply:** Any future WWD sponsor/affiliate deal — check whether it's
flat-fee or rev-share before drafting a read, since the CTA language differs
(a code to say on-air vs. "link in the description"). Route new sponsor
onboarding emails through the same research-then-brief pattern: read the
actual email, don't assume terms.

## Marketing subagent structure — spec → live pattern [2026-09-14]
WKP's marketing department has a director (`marketing-director`) plus four
worker subagents (`copywriting`, `social-media`, `graphic-design`,
`video-ugc`), each fully spec'd in `.claude\agents\_spec\` but starting
dormant — only `marketing-director` and `market-research` were live before
2026-09-14. Each spec file says "reports to marketing-director only" and
is explicitly "drop-in ready — move it into `.claude\agents\` to activate."

marketing-director's first real assignment (Surfshark campaign + weekly
social calendar, 2026-09-14) hand-built everything itself because the
4 workers were still dormant, and flagged that gap in its own report.
Zac's response: "spin them up... bring them to live and pass on their
instructions." All 4 moved to `.claude\agents\` same day, status banners
updated SPEC'D→LIVE.

**How to apply:** marketing-director should now delegate real work to these
four rather than hand-building it — copy to `copywriting`, posting
schedules to `social-media`, visual assets to `graphic-design`, clips to
`video-ugc`. If marketing-director (or any director) starts hand-building
work that belongs to a dormant department again, that's the signal to ask
Zac whether it's time to spin that one up too, rather than letting it
become a standing workaround.

## POW/MIA content — never center it on Zac himself [2026-09-14]
When WWD posts about POW/MIA Recognition Day (3rd Friday of September) or
any similar remembrance content, keep it entirely about the missing/
captured service members — never reference Zac's own veteran status or
frame it around him. His exact words, given specifically as the framing
for this content: "Let's keep it about them the MIA and POWs. I made it
home. They haven't yet, until they all come home."

**Why:** This is a deliberate, values-driven line he drew, not an oversight
to fix. He offered the phrase "until they all come home" himself for use
in the copy — fine to echo the sentiment, but never attribute it to him by
name or make the post about his own service.

**How to apply:** Applies to Constitution Day, Memorial Day, Veterans Day,
and any other remembrance/military-honor post WWD does — check whether Zac
has given specific framing guidance before defaulting to a generic
"thank you to all who served" angle that could read as being about him.
