# Leveling task: graphic-design

Wave 1. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` (read it first). Created 2026-11-22 by chief-of-staff. Jarvis launches this as one job. Run as `graphic-design` (spec `D:\WKP\.claude\agents\graphic-design.md`), or through a general-purpose agent running that spec. Grader: qa-director (qa-media bench for the image checks), never the agent itself.

Budget (write it in the ledger row first): about 90 minutes, free sources only, $0, no credits spent, nothing posted. Read `memory\MEMORY.md`, `memory\agents\graphic-design.md` and `SOP\SOP-Output-Locations-and-Formats.md` before starting.

## Why this agent is wave 1
Wrote beginner Firefly and Veo prompts that failed. `data\firefly-prompt-guide\LESSONS.md` logs failure patterns F1 onward (for example a named thing gets drawn even when the prompt says to avoid it). Zac spent about 2,000 credits on one joust sting, his figure, not retrieved from the account.

## Step 1: Craft Brief (`memory\agents\briefs\graphic-design-craft-brief.md`)
Retrieve and quote (URL, retrieved date, verbatim quote). The list below is a starting set written without fetching anything: confirm each page resolves, drop dead ones, add better ones found. Write NOT RETRIEVED for any page that cannot be fetched. Never fill from memory.
- Adobe Firefly help pages on text-to-video, image-to-video, start and end frame, camera motion and prompt writing (helpx.adobe.com Firefly section)
- Google DeepMind Veo prompt guide and Google Cloud Vertex AI Veo prompt guide (cloud.google.com docs, ai.google.dev Veo docs)
- Adobe Firefly release notes or blog posts on the partner models Zac's menu lists (Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray) with model tier names
- Runway and Kling official prompting guides for the partner models
- Adobe Firefly image prompt guide (style reference, composition reference, structure reference, negative text)
- Two named practitioners with dated tutorials on image-to-video continuity
Target 5 to 10 retrieved sources, at most 2 community. Local material to read as input, not as proof: `data\firefly-prompt-guide\QUICK-CARD.md`, `LESSONS.md`, `.claude\agents\_spec\graphic-design-reference.md`, `data\firefly-prompt-log\README.md`. Check every [U] tip against a retrieved source and mark it PROVEN, SOURCED or PROPOSED.

## Step 2: Gap audit (`memory\agents\briefs\graphic-design-gap-audit.md`)
Audit the 18 clips and notes in `data\firefly-prompt-log\` (5 joust, 13 garage) and the four Ian still prompts in `Post-Production\reports\Ian-Trailer-Continuity-Chain-Prompts-2026-11-21.md` (NOT RUN). For each prompt: which maker guidance it ignored, what the clip showed (graphic-design already wrote contact sheets in `scratch\ffl\`, reuse them).
Finish with the 3 gaps that cost the most.

## Step 3: Drill (write the pass bar BEFORE running; file `SOP\leveling\drills\graphic-design-drill-1.md`)
REPLAY drill, no credits: take 3 shots whose clips already exist on disk (for example garage clips 4, 7 and the joust sting). Without looking at the result notes, write the prompt, model tier, start frame use and settings.txt you would run, with each instruction tagged. The grader compares to what the clips actually showed and to the retrieved guidance. Criteria (write final numbers before the run): (1) no unwanted item named in the positive prompt, (2) positives only for what must appear, (3) start frame and tier recorded, (4) camera and motion terms taken from the maker guide with quote, (5) every instruction tagged, (6) a cheapest-test plan with exact credit cost shown BEFORE any run (cost NOT RETRIEVED unless read from the Firefly panel), (7) predicts the known failure on at least 2 of 3 shots. Pass: 6 of 7 with 1, 5 and 6 CRITICAL. A live generation drill only with Zac's yes and exact cost.
Graded by qa-director (qa-media bench for the image checks). Result saved beside the drill with date and grader.

## Step 4: Pre-flight checklists (`SOP\leveling\preflight\<output-type>.md`)
Output types to cover: Firefly image prompt card, Firefly or Veo video prompt card with settings.txt, redo plan (Redo A to C)
6 to 12 yes or no items each. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (Part 7).

## Step 5: Report back
Hand back: paths of the brief, audit, drill, result and checklists; the failure entries opened (if any) in `memory\agents\failures\graphic-design.md`; the level the evidence supports (a proposal, the grader signs); a ledger row in `logs\agent-runs.md`; one lesson appended to the agent's lessons file. Chief-of-staff then updates `memory\agents\LEVELS.md`.
