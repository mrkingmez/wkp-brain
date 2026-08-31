# MILITARY RESEARCH MASTER PROMPT
### Warrior King Productions — Research Standard v1.0

---

## HOW TO USE THIS

Paste everything below the line marked **PROMPT BEGINS** into a new conversation. Replace `[SUBJECT]` with your battle, campaign, commander, siege, or operation. Fill in the two optional fields if relevant; delete them if not.

Recommended model: **Opus** for the research pass. Sonnet for later scripting from the output.

---

# PROMPT BEGINS

You are conducting a professional-grade military history research report on:

**SUBJECT:** [SUBJECT]
**PERIOD/THEATER (optional):** [___]
**SPECIFIC QUESTION I'M INVESTIGATING (optional):** [___]

Follow the standards below exactly. They are not stylistic preferences — they are the methodology.

---

## PART I — GOVERNING RULES

These override any other instinct you have about how to write history.

**Rule 1 — Evidence tagging is mandatory.**
Every substantive claim carries one of four tags:

- **[ESTABLISHED]** — Multiple independent primary or contemporary sources agree.
- **[SUPPORTED]** — One primary source, no contradicting evidence.
- **[CONTESTED]** — Sources conflict. You must state who says what and why they differ.
- **[SPECULATIVE]** — Inference, reconstruction, or reasoning from analogy. No direct evidence.

Do not use percentages or numeric confidence scores. They are false precision. Use only the four bands.

**Rule 2 — "Unknown" is a valid and expected answer.**
Where the record does not preserve something, say so plainly. A report with twenty honest "unknown" entries is more useful than one with twenty invented details. Never generate a plausible-sounding detail to fill a gap.

**Rule 3 — Citation discipline.**
Name specific works, authors, archives, record groups, or document collections wherever possible. If you cannot verify that a citation exists as you've stated it, write: *"Attribution uncertain — verify before use."* Never produce a citation you are not confident is real. This is the highest-priority rule in the document.

**Rule 4 — No modern moral framework imposed on historical actors.**
Judge decisions against the information, doctrine, technology, and constraints available to the people making them. You may note where a decision violated the norms of its own era — that is historical analysis. You may not evaluate historical figures against twenty-first-century values.

**Rule 5 — Multi-national historiography required.**
Do not rely solely on Anglophone or American academic sources. Where the subject involves non-English-speaking participants, explicitly consult and represent how their own historians treat it. Flag where national historiographies diverge and characterize the disagreement rather than picking a winner by default.

**Rule 6 — No manufactured balance.**
If scholarly consensus is genuinely settled, say so. Do not invent a minority position for symmetry. Conversely, if the "textbook" version is contested by serious scholarship, lead with that.

**Rule 7 — Scope scaling.**
Match depth to significance. A decisive multi-army campaign warrants the full report. A minor engagement warrants a compressed version — Sections 1, 3, 5, 7, and 9 only. State at the top which tier you're producing and why.

---

## PART II — SOURCE HANDLING

**Do not rank sources on a fixed ladder.** Source authority is claim-dependent. Match the source class to the claim type:

| Claim type | Sources with actual authority | Sources that mislead here |
|---|---|---|
| Commander's intent and planning | Orders, staff papers, pre-battle correspondence, war diaries | Post-war memoirs (self-justifying), soldier accounts (no visibility) |
| Order of battle, unit strength | Official returns, muster rolls, logistics records | Contemporary press, enemy estimates |
| Terrain, weather, conditions on the ground | Soldier diaries and letters, unit war diaries, local records, archaeology, modern terrain analysis | Staff-level records (abstracted away from ground truth) |
| Sequence and timing of events | Multiple independent accounts cross-checked; time-stamped signals traffic | Any single narrative account |
| Casualties | Own-side returns (undercount), medical and burial records, archaeological evidence | Enemy claims, contemporary reporting, victor's official totals |
| Aftermath and consequence | Later administrative, economic, and political records | Immediate post-battle rhetoric on either side |
| Individual experience and morale | Letters, diaries, contemporary interviews | Official records of any kind |

**Excluded outright:** conspiracy literature, fringe revisionism, and unsourced internet content. Do not include these even to debunk them, unless I specifically ask about a named claim.

**Memoir caution:** post-war memoirs are primary sources for the author's *self-presentation*, not necessarily for events. Treat accordingly and say so when leaning on one.

---

## PART III — REPORT STRUCTURE

### 1. Executive Summary
Six to ten sentences. What happened, who won, why it mattered, and what the single most contested question about it is.

### 2. Strategic Context
The war or campaign this sits inside. What each side was trying to achieve at the theater level. What had happened in the preceding weeks or months that set the conditions.

### 3. Forces and Order of Battle
Composition, strength, command structure, and quality of each force. Tag strength figures — these are frequently [CONTESTED]. Note where returns are missing entirely.

### 4. Battlefield Reconstruction
Reconstruct the physical environment. For **every** variable, tag it:
`[SOURCED]` — recorded in the historical record
`[COMPUTED]` — calculable (sunrise, sunset, moon phase, tidal state)
`[INFERRED]` — reasoned from regional climate data or seasonal norms
`[UNKNOWN]` — not preserved

Variables: terrain and elevation, watercourses, roads and approaches, forest and vegetation, ground firmness and mud, crops and seasonal cover, visibility, sunrise/sunset, moon phase, temperature, precipitation, wind, fog, dust.

Then: **how each of these materially shaped a specific decision or outcome.** Do not list conditions without connecting them to consequences.

Environmental detail is where fabrication is most tempting and most invisible. `[UNKNOWN]` should appear frequently in this section for pre-modern engagements. If it doesn't, you are inventing.

### 5. Narrative of the Engagement
Chronological. Phase by phase. Tag the sequence where accounts diverge — say explicitly: "Source A places this before the flank attack; Source B after; the difference matters because ___."

### 6. Source Analysis
For each major source, cover: what it is, who produced it, when, and what it has authority over.

**Bias flagging is claim-specific, not categorical.** Do not run a checklist of bias types against every source. Flag a bias only where it materially distorts a specific claim in this report — and when you do, state what the undistorted version likely looks like.

### 7. Operational Analysis
**Provide the inputs. Stop short of the verdict.**

Lay out, without concluding:
- Stated objective of each commander
- Assumptions each was operating on
- Which assumptions proved false, and when they'd have known
- Intelligence available, intelligence absent, intelligence available but disregarded
- Logistical constraints enabling or foreclosing options
- The decision points — moments where a different choice was genuinely available
- The point of no return, and whether the outcome was still recoverable after it
- Cascading failures: which errors compounded downstream
- Underdiscussed good decisions
- Celebrated decisions that don't survive scrutiny
- What modern staff colleges draw from this engagement, if anything

Present these as findings for the reader to reason from. Offer a verdict only if I ask for one.

### 8. Causation Test
Applied to any claim that this engagement "changed" something:

- What concretely changed as a direct result?
- What would have happened anyway on existing trajectory?
- What is the shortest defensible causal chain from this event to the claimed consequence — and where is the weakest link in it?
- Which competing factors are usually credited to this battle but belong elsewhere?
- If the outcome had reversed, what specifically would be different within five years? Within twenty?

Be adversarial here. The default failure mode in popular military history is inflating causal weight. Attack the causal claim before endorsing it.

### 9. Historiographical Assessment

**Consensus position** — what the weight of scholarship holds.
**Minority position** — only if one genuinely exists, with its strongest evidence.
**National divergence** — where different countries' historians read it differently, and why.
**My assessment** — clearly labeled as analysis, not fact. Must include: *what evidence would change this assessment.*

### 10. Research Gaps
- Questions the evidence currently cannot answer
- Documents that would resolve them if found or declassified
- Direct contradictions between sources that remain unreconciled
- Where archaeology is incomplete or unattempted
- Specific archives, collections, museums, and works for deeper study

---

## PART IV — OUTPUT DISCIPLINE

- Plain declarative prose. No dramatization, no "little did they know," no invented dialogue or interior thought.
- Every number carries its source and its tag.
- If you are uncertain whether something is true, say you are uncertain. Do not hedge with vague qualifiers — name the specific uncertainty.
- Close with a short list of the three claims in your own report you consider weakest, and why.

# PROMPT ENDS

---

## APPENDIX — QUICK VARIANTS

**Compressed pass (screening a topic before committing research time):**
Add at the top: *"Tier 2 only — Sections 1, 3, 5, 7, 9. Under 1,500 words."*

**Causation-only pass (Hidden Hinge candidate screening):**
Add: *"Run Section 8 only, applied to the claim that [SUBJECT] was decisive for [OUTCOME]. Be maximally adversarial toward the causal claim."*

**Terrain-only pass (visual and production reference):**
Add: *"Run Section 4 only, at maximum detail, with the four-tag environmental system."*
