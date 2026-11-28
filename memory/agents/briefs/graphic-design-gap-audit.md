# Gap audit: graphic-design (2026-11-22)

Builds on, does not repeat, `D:\WKP\data\firefly-prompt-guide\AUDIT-2026-11-22.md` (24 video prompts, 24 of 24 negation fails, lint table inside). Brief: `graphic-design-craft-brief.md`. This audit adds the NON-VIDEO outputs the first audit did not cover. Counts below come from a script run today, not from memory.

## Video side (summary, full table in the first audit)
All 18 logged clips and 24 prompts failed the maker guidance on negation, contradictions, start-frame re-description and missing end frames. Zac's cost: about 2,000 credits on the joust sting (his figure, not retrieved from the account) and 18 clips with no settings. Not repeated here.

## Image and graphic outputs on disk
| Output | Path | Departure from the brief | Cost |
|---|---|---|---|
| AKT Facebook image prompt (126 words) | `D:\WKP\scratch\akt\akt-prompts.md` prompt 1 | Main prompt carries 4 negations ("no text", "no letters", "no logos", "no crests with writing"). C1: a negation in a prompt adds the thing. Over A2's "longer prompts aren't always better" (126 words) | Unknown, result NOT SEEN by me. Risk: drawn lettering |
| AKT Instagram image prompt (129 words) | same file, prompt 2 | 7 negations in the main prompt ("no clouds", "no birds", "no objects", "no faces in detail", plus text, letters, logos). The empty-sky overlay zone was requested through negations, so the sky is the most likely thing to fill with clouds and birds | Unknown |
| AKT settings lines | same file | "Negative prompt box if offered" lists nouns. Reasonable, but the box is undocumented (A2 silent, C1 says the model does not understand negatives). Settings say "visual intensity mid" and "content type Art" with no source for either | Wasted variations if the box does not exist |
| Ian chain still cards R3b, H1, B1, W1 | `D:\WKP\Post-Production\reports\Ian-Trailer-Continuity-Chain-Prompts-2026-11-21.md` | NOT RUN. Negatives moved to a negative field (better than the main prompt), but every card depends on a field that has no Adobe page. Prompts run 101 to 139 words. Composition and Style strength numbers carry no source (A2 says only that a slider exists) and the doc admits UNTESTED. Pre-flight facts not source-linked. The character table carries negations ("No ring, watch or tattoo") that can leak into prompts | Not run, so no credits lost. Risk: first sitting wastes variations |
| WWD joust still prompts | `D:\WKP\data\firefly-prompt-guide\REBUILT-PROMPTS-2026-11-22.md` | Same optional negative box, nouns only. Within the rule. Lint PASS | Not run |
| Thumbnails, Etsy listing images, social graphics | none found | No prior output on disk for a real thumbnail or Etsy listing image from this agent (ETSY is on hold, WWD thumbnails are Matt's). First card of each type is in the drill | n/a |

## Ranked top 3 gaps (what cost or will cost most)
1. Negation and contradiction written into main prompts, for stills as well as video (24 video prompts, 2 AKT image prompts, character tables). Cost: the 2,000-credit sting. Fix: R1 plus the no-negative-box rule, lint on every card.
2. Settings and facts not verified against the panel or a source, then written as steps (end slot, negative box, strength midpoint, content type Art). Cost: wrong clicks, no way to separate causes. Fix: tag every panel tip and run the 30-second panel check first, which is already in REBUILT-PROMPTS.
3. Overlong, many-phrase image prompts and no platform spec on the card (126 to 139 words against A2). Cost: drift, plus an image that may not meet Etsy 2000 px or YouTube 2 MB. Fix: 100-word cap for stills, spec line with source (Y1, E1) on the card.

## Not audited
No thumbnail or Etsy listing output exists. The four older Ian prompts in the 2026-11-20 Post-Production file were superseded by the 11-21 chain doc and were not re-read.
