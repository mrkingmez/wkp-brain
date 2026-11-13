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

## Opus Clip affiliate, link received [2026-11-12]
Zac got his OpusClip affiliate link on 2026-11-12 (he applied under WWD-2026-11-05-01, option A/B). The link itself is NOT in the repo yet: where it lives is TBD (Surfshark's links sit in this file and `L:\Winter Wolfs Den review show\Sponsors\Surfshark\`, mirror that once Zac pastes it). Terms from the 2026-11-05 research (`WWD\reports\Monetization-Options.md`, not yet re-verified against OpusClip's own page): 25% recurring, 20 dollar first payout, no paid ads with the link, deactivated after 6 months of no traffic. Not stated yet and needed from Zac: the actual link, the confirmed terms, the program's disclosure wording.

**How to apply:** Never invent or guess the link. Any public copy that carries it needs an FTC disclosure (affiliate/material connection) in the copy itself, run through marketing-director (and the writing room), then `no-ai-slop` (`slop_check.py` for the mechanical pass). Link-based tracking means "link in the description", not a spoken code, unless OpusClip says otherwise. Public posting still needs Zac's yes with the exact post. Tracking row: TASKS.md "Opus Clip affiliate link".

**UPDATE 2026-11-12, link and terms received from Opus's correction email (Zac pasted it):**
- Affiliate link: https://clip.opus.pro/auth/oauth/login?coupon_code=40OFF&via=winterwolf
- It gives the audience 40% off their first month of Monthly Pro. Opus supplied the discount, so the earlier "no discounts without written approval" concern is covered for this coupon only. Do not invent other offers or stack discounts.
- Tracking id is `via=winterwolf`. The first launch email had a wrong link, use only this one.
- Still unconfirmed from the email: commission rate and length, cookie window, payout minimum, logo rules. Check the affiliate dashboard.
- The push packet is `WWD\reports\OpusClip-Affiliate-Push-Packet.md`. Matt's yes is still needed before any public use.

**Opus Clip affiliate terms read 2026-11-12 (https://www.opus.pro/affiliate-terms, Zac supplied the URL):**
- Commission 25% of Essential and Pro plans. Annual plans pay once. Monthly plans pay up to 12 consecutive renewals, stop if the referral cancels.
- Payout around the 15th for the prior month, can take up to 45 days. PayPal or bank. May need a W-9. No payout minimum stated. No cookie window stated (Rewardful tracks from first click).
- Must disclose affiliation in all marketing, with "ad" or "advertisement" where law requires. No fixed wording.
- Banned: paid ads of any kind with the link, buying brand domains or keywords, brand names in account names, unauthorized discounts or coupons, fake or expired coupons, implying Opus endorsement, spam.
- The 40OFF coupon is not mentioned in the terms, it came from Opus in the correction email. Keep that email as the written approval, share only that coupon, invent no other offers.
- Logos: current, unaltered, brand guidelines (not on the page). License revocable any time.
- Rates and terms can change immediately on notice. Opus can remove an affiliate without warning. Commissions can be reversed for cancellations and refunds.
- No inactivity rule on this page. The older FAQ's "deactivated after 6 months with no traffic" is not confirmed in the terms.
- Not addressed: self-referral, YouTube Shorts rules.

## Amazon Associates, joined [2026-11-12]
Zac says WWD is now part of the Amazon Associates program (he signed up himself). Not in the repo yet: the tracking ID, which account it sits under, and the approval terms. Rules to apply: Amazon requires a clear affiliate disclosure on every page or post that carries a link ("As an Amazon Associate I earn from qualifying purchases" or close wording, in the post itself), links only in places Amazon allows (not in emails, offline, or on certain social posts without checking the Operating Agreement), and Amazon can close accounts that do not make 3 qualifying sales in 180 days (from earlier research, verify on Amazon). Any public copy with an Amazon link goes through marketing-director, then slop_check.py and no-ai-slop, and posting needs Zac's yes. Use for Den Files book links (WWD-2026-11-05-02) once an episode has a book.
