# Pre-flight: Firefly image prompt card (stills, start frames, thumbnails, listing and social art)

Created 2026-11-22 by graphic-design from the Craft Brief. Paste into the hand-back with each item ticked and a one-line proof. One unticked item and the card does not go to Zac. Director spot-checks 1 in 3.

1. [ ] Lint: `python D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file <card>` exits PASS or an explained WARN. Proof: paste the line.
2. [ ] Zero negation words in the main prompt (no, not, without, never, nothing). Unwanted things are not mentioned at all. Proof: lint R1 count 0. (SOURCED G1, R2, A2 sibling, C1 COMMUNITY)
3. [ ] Order follows Adobe's labels: subject, background, then style, colour, lighting (A3 lists Subject, Background, Image type, Style, Colour, Lighting, Action). Lighting is last. 100 words or fewer. Proof: word count and the first noun of each clause.
4. [ ] No text, logo, numeral, flag lettering or insignia requested of the model. A plain empty zone is described as a picture for the overlay, and the overlay tool is named (code or Express). (PROVEN F3, SOURCED B1 text FAQ)
5. [ ] Platform spec is on the card with its source: YouTube 16:9, under 2 MB mobile, JPG or PNG (Y1); Etsy landscape or square, 2000 px, subject centered with border (E1); anything else marked NOT RETRIEVED. Output pixel size marked NOT VERIFIED for Zac to read.
6. [ ] Every panel tip carries SOURCED, PROVEN, COMMUNITY or PROPOSED, including content type, strength slider and negative box. The negative box is written as "not relied on". Reference slots say which slot and why. Proof: every bullet that starts with a panel verb (set, use, pick, upload) ends in a bracket tag.
7. [ ] House rules checked if patriotic or military: flag present and correct (13 stripes, stars on blue), people shown, all generations, no readable text, label as AI-generated. Not applicable otherwise, say so.
8. [ ] Not a WWD thumbnail (Matt makes those) and no real person and no brand mark. Never name another artist.
9. [ ] Fallback written (edit the near-miss with prompt to edit or Generative Fill, or a text-only rerun) and one-change retry written.
10. [ ] No credit number appears. Zac reads the figure at the Generate button. Log folder named.
11. [ ] No em dashes. `slop_check.py` exit 0 on any public copy on the card.
