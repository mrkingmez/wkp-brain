# Format - BUILD GUIDE

## What this produces
A printable, step-by-step guide Zac can work through without asking a
single follow-up question. If he has to ask how to do a step, the guide
failed.

## Structure
1. What you are building, one paragraph, and what it does when finished.
2. Parts required - reference hardware\PAWS-BOM.xlsx by row. Do NOT
   restate prices in prose.
3. Tools required, with a note on which are one-time purchases.
4. Safety and hard limits before any assembly step.
5. Numbered steps. Every step is an action, not a note to self.
6. Verification after each phase - what proves the step worked.
7. Troubleshooting - the three most likely failure points and the fix.

## Rules
Every command copy-pasteable. Every click named.
Software angle limits on servos BEFORE the first animation loop, always.
Capacitors across every servo, stated as a step, not a footnote.
State machine tested on PC before it touches hardware.
Money written out in full. No symbols that break text to speech.
Never a single-source part. Three options minimum, from the BOM.

## Output
docs\PAWS-<device>-Build-Guide-v<N>.md
