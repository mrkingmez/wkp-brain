# IRFL Scoring Rules — Verified From League Settings

## DROP LOCATION
`D:\WKP\fantasy-football\`

## EXACT PHRASE FOR CLAUDE CODE
> Read FF-SCORING-RULES.md. Build league-scoring-rules.json from
> Section 1, then build the scoring function per Section 3. Before
> writing code, run the MFL rules export in Section 2 and tell me every
> place it disagrees with Section 1. Do not resolve a disagreement
> yourself — report it.

---

## Why this file exists

Sleeper's `pts_ppr` field is its own default scoring format. The IRFL
is a custom league and differs from it materially on both sides of the
ball. Verified example: Fred Warner projected at 7.23 tackles came back
with `pts_ppr` of 0.5. Under IRFL rules the same projection is worth
roughly seven points.

**Never read `pts_ppr` for any position.** Compute everything from raw
component stats using the table below.

---

## SECTION 1 — The rules, transcribed from league settings

Cross-checked 2026-09-13 against the live MFL TYPE=rules export: all 42
rules matched exactly, zero disagreements.

### Passing
| Rule | Value |
|---|---|
| Passing TD | 6 |
| Passing yards | 0.04 per yard (25 yards per point) |
| Interception thrown | minus 2 |
| Passing two point conversion | 2 |

### Rushing
| Rule | Value |
|---|---|
| Rushing TD | 6 |
| Rushing yards | 0.1 per yard (10 yards per point) |
| Rushing two point conversion | 2 |

### Receiving
| Rule | Value |
|---|---|
| Receiving TD | 6 |
| Receiving yards | 0.1 per yard |
| Reception | 1 (full PPR, no tight end premium observed) |
| Receiving two point conversion | 2 |

### Kicking
| Rule | Value |
|---|---|
| Field goal made, 0 to 30 yards | 3 flat |
| Field goal made, 31 to 99 yards | 0.1 per yard of length |
| Extra point | 1 |

Note: field goals over thirty yards score by distance, so a fifty yard
kick is worth five points and a thirty-two yard kick is worth 3.2.
Sleeper projections may not include projected field goal distance. If
they do not, kicker projections are approximations — label them as such
rather than presenting them at the same confidence as other positions.

### Returns
| Rule | Value |
|---|---|
| Punt return TD | 6 |
| Punt return yards | 0.05 per yard |
| Kickoff return TD | 6 |
| Kickoff return yards | 0.025 per yard |

### Fumbles
| Rule | Value |
|---|---|
| Fumble lost to opponent | minus 2 |
| Forced fumble | 2 |
| Fumble recovery from opponent | 2 |
| Defensive fumble recovery TD | 6 |
| Offensive fumble recovery TD | 6 |
| Opponent fumble recovery yards | 0.1 per yard |
| Own fumble recovery yards | 0.1 per yard |

### Defense — individual players
| Rule | Value |
|---|---|
| Tackle (solo) | 1 |
| Assist | 0.5 |
| Sack | 3 per full sack (confirmed) |
| Interception caught | 3 |
| Interception return yards | 0.1 per yard |
| Interception return TD | 6 |
| Pass defended | 1 |
| Safety | 4 |

**Solo and assisted tackles score at different rates.** This is the
single most important line in this file. Sleeper's `idp_tkl` is a
combined figure and using it will overvalue every defensive player by
roughly twenty to thirty percent. Use `idp_tkl_solo` and
`idp_tkl_ast` separately, always.

**Sacks — confirmed at three points per full sack.** The settings
display reads "1.5 point for every .5" because sacks are recorded in
half-sack increments. Zac confirmed this resolves to three points for a
full sack. Sleeper's `idp_sack` is a decimal figure, so multiply
directly by three — do not round half-sacks up or down.

### Special teams and blocks
| Rule | Value |
|---|---|
| Blocked field goal | 3 |
| Blocked field goal TD | 6 |
| Length of blocked FG TD | 0.1 per yard |
| Blocked punt | 3 |
| Blocked punt TD | 6 |
| Length of blocked punt TD | 0.1 per yard |
| Blocked extra point | 1 |
| Missed FG return TD | 6 |
| Length of missed FG return TD | 0.025 per yard |

**Completeness — confirmed.** Zac confirmed nothing appears below
Safeties in the league settings. Section 1 is the complete rule set. If
the MFL export in Section 2 returns rules not listed here, that is a
discrepancy worth reporting, not a gap to fill in silently.

---

## SECTION 2 — Cross-check against the machine-readable source

```
https://www44.myfantasyleague.com/2026/export?TYPE=rules&L=43094&APIKEY={key}&JSON=1
```

Parse it and diff it against Section 1.

**Report every disagreement to Zac. Resolve none of them yourself.**
Section 1 was transcribed from screenshots by eye, and the export is
authoritative — but a parsing error in the export is equally possible,
so a mismatch means one of the two is wrong and Zac decides which.

Also pull the starter requirements — how many at each slot, and which
positions each flex accepts — from `TYPE=league`. The optimizer needs
this and it is not in the scoring rules.

Once the diff is clean, write `league-scoring-rules.json` and treat it
as the single source of truth. Re-pull at the start of each season.

---

## SECTION 3 — The scoring function

One function, all positions. Takes raw component stats plus the rules
object, returns points.

Used in three places:
1. Sleeper **projections** — turns raw projected components into a
   real IRFL projection for lineup decisions.
2. Sleeper **weekly actuals** — same math, real stats, so projected
   versus actual is compared under identical rules.
3. Dashboard **live scoring** — note MFL's own live scoring export is
   authoritative during games. Use this function for projections and
   post-game analysis, not to second-guess MFL's live numbers.

**Any rule with no matching Sleeper component field gets logged as
unscorable, with its point value.** Do not silently drop it. Blocked
kicks and some return categories may have no projection field at all,
which is fine — but the gap must be visible, not invisible.

---

## SECTION 4 — Sanity check before trusting the output

Run the finished function against week 2 projections and show Zac the
top twenty at each position group.

Expected shapes:

- **Fred Warner should land near seven points**, not 0.5. If he is
  still under two, the tackle mapping is wrong. Stop and report.
- **Off-ball linebackers should outrank edge rushers.** One point per
  solo tackle beats three points per sack when the linebacker makes
  seven tackles and the edge rusher makes half a sack. Sleeper's
  default produced the opposite ordering, which is the error we are
  correcting.
- **Quarterbacks should rank higher than in standard formats**, since
  passing touchdowns are worth six rather than four.

If any of these come out backwards, report it rather than proceeding to
the optimizer.
