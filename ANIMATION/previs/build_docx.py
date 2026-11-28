"""Builds the Previs Method deliverable docx (dated) from the md files and proof renders."""
import os
from docx import Document
from docx.shared import Inches, Pt

R = r"D:\WKP\ANIMATION\previs\renders"
d = Document()
st = d.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)


def H(t, l=1):
    d.add_heading(t, level=l)


def P(t):
    d.add_paragraph(t)


def B(t):
    d.add_paragraph(t, style="List Bullet")


def IMG(items, w):
    t = d.add_table(rows=2, cols=len(items))
    for i, (path, cap) in enumerate(items):
        t.cell(0, i).paragraphs[0].add_run().add_picture(path, width=Inches(w))
        t.cell(1, i).paragraphs[0].add_run(cap).font.size = Pt(9)


d.add_heading("Previs Method: a free Blender test for framing, hands, scale and camera", 0)
P("Date: 2026-11-24. Built by animation-director for Zac. Free only. No credits, no network, no Adobe, no git commit.")
H("The short version")
P("Before any engine credit is spent, a shot card (location, who stands where, which hand holds which prop, camera, lens) goes in, and the department gets back a gray still, a plan view from above, a 3 by 3 camera sheet and a report of numbers read from the scene. It is the Blender version of the plain bald-figure sketch stage in the prompting playbook.")
P("It fixes layout only: who stands where, which way they face, which hand holds what, how big things are, where the camera is, what the camera can see. It does not fix look. No costume, face, light mood, color, texture or style comes from it. The renders are gray on purpose.")
H("What was built and where it lives")
for t in [
    r"Folder: D:\WKP\ANIMATION\previs\ (previs.py is the one command, previs_lib.py the figure, props, room blocks, light marker and camera rig, build_shot.py the measuring and rendering, cards\ the shot cards, renders\ the output per card).",
    r"Template scene: D:\Blender Projects\Previs Template v1.blend (two stand-in figures, a prop, room blocks, 1 m ground grid, light marker, shot camera with settable lens on a Track To target, plan camera, nine sheet cameras, lens cheat sheet as a text block). Never overwritten; a change is v2.",
    r"Lens cheat sheet: D:\WKP\ANIMATION\previs\lens_cheatsheet.md, computed from sensor maths (full frame, 36 mm), with distances to frame a 1.75 m person in 16:9 and 9:16.",
    r"How-to: D:\WKP\ANIMATION\previs\HOWTO.md. One-page checklist: D:\WKP\ANIMATION\previs\CHECKLIST.md. Playbook pointers added in sections D2 and G of REFERENCE\PROMPTING-PLAYBOOK.md.",
    "Stand-in figure: gray head with a dark nose wedge (shows facing), torso, pelvis, two-bone arms and legs, hand blocks. BLUE hand is the character's own LEFT, RED is the character's own RIGHT, printed on every render. Hands go to named grip points on props. A hand that cannot reach is drawn straight and reported with the shortfall.",
]:
    B(t)
H("How to run it")
P(r"1. Copy cards\_card-template.json and fill it in. 2. Run: C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\ANIMATION\previs\previs.py <card.json> --plan --sheet. 3. Read REPORT.md (PASS and FAIL against the expect lines in the card, plus warnings), then the images. 4. Fix the card, rerun, keep the failed run as first-pass. A full run takes about 20 to 40 seconds. The full field list is in HOWTO.md.")

H("Proof 1: Ian trailer, garage wrench hand-off (R3b geometry)")
P("The card states the hand-off from the R3b card in the Continuity Chain Prompts: older man lets go at the top of the wrench, young man takes the shaft below, a clear gap of air, wrench vertical, hands only, the card's negative field says no face. The choice of RIGHT hand for both men is mine for the test; the R3b card gives only the side each arm comes from (older from the upper right, young from the lower left). Brandon is 1.80 m, the father 1.74 m, wrench 0.22 m.")
IMG([(R + r"\ian-garage-handoff-v1\shot_captioned.png", "Run 1. Profile staging, 2.0 m, 40 mm, 1.25 m high. Two expectations FAIL: both heads are in a hands-only shot."),
     (R + r"\ian-garage-handoff-v2-handsonly\shot_first_pass_FAIL.png", "Run 2, first pass. Hands-only camera. FAIL: Brandon's free LEFT hand (blue) is 63 percent visible, a third hand in frame."),
     (R + r"\ian-garage-handoff-v2-handsonly\shot_captioned.png", "Run 2, fixed. Camera 0.7 m back, 1.15 m high, 35 mm, aimed down. All six expectations PASS.")], 2.1)
IMG([(R + r"\ian-garage-handoff-v2-handsonly\plan_captioned.png", "Plan view from above. Green arrow is the camera, yellow arrow the light."),
     (R + r"\ian-garage-handoff-v1\sheet_3x3.png", "3 by 3 sheet of the Run 1 set: low, eye, high by three azimuths. The middle tile is the shot camera.")], 3.0)
P("What the previs caught or would have caught:")
for t in [
    "Framing against the card. The first staging put both heads in frame, which contradicts the R3b card (hands only, 'face' in the negative field). Two FAIL lines, read from the scene, before any credit. The fix was a camera move, not a prompt.",
    "A third hand. In the hands-only framing Brandon's unused left hand showed at 63 percent visible at the lower left. An image engine would likely draw it as a real hand. Moving it behind his body took it to 0 percent. This is the class of failure in the 2026-11-22 audit (one hand held the wrench while the other did the work). The previs does not stop an engine from doing it, it gives a layout to hold and a number to check against.",
    "Near hand versus holding hand. In the profile staging the father's near-camera hand is his empty LEFT (100 percent visible, holds nothing) and his holding RIGHT hand is the far one. A prompt that says 'the hand nearest the camera holds the wrench' would be wrong for him. The report names this per hand, so the prompt wording comes from the report.",
    "The gap. 'A clear gap of dark air' became a number: hand to hand 0.174 m, with the older hand 100 percent visible on screen-right and the young hand 74 percent visible on screen-left (partly behind his own forearm and the wrench).",
    "Scale and lens. 40 mm at 2.05 m framed a 1.80 m man at 98 percent of the 9:16 frame height, which matches the lens sheet formula, so the distance numbers can be trusted.",
]:
    B(t)

H("Proof 2: WWD intro frame, cold open shot 1")
P("Shot 1 in Cold-Open-Shot-List.md is 'WARDEN at his post, radio voice reaching out'. This is TEST BLOCKING written by animation for the previs, not Zac's approved design. The Warden's look is still a blocker in that file, so only layout is tested: seated at a desk, LEFT hand on a handheld mic, RIGHT hand on a radio dial, looking at the lens, 16:9, 50 mm, 1.30 m camera, light from the right. Which hand holds what is my choice for the test.")
IMG([(R + r"\wwd-coldopen-shot1-warden-v1\shot_first_pass.png", "First pass. FAIL: the left hand (blue) is drawn across the lower face."),
     (R + r"\wwd-coldopen-shot1-warden-v2\shot_captioned.png", "Second pass. Mic lowered and moved out 0.24 m, camera 12 degrees from the front. All five expectations PASS.")], 3.0)
IMG([(R + r"\wwd-coldopen-shot1-warden-v2\sheet_3x3.png", "3 by 3 sheet of the second pass.")], 5.5)
P("What the previs caught or would have caught:")
for t in [
    "A hand over the face. In the first pass the mic hand crossed the lower face from the 3/4 camera. The report flagged it automatically ('drawn over the face on screen') and the check failed. Fix: mic and hand moved out and down, camera nearer the front. Mic hand then 95 percent visible, radio hand 84 percent.",
    "A shelf line floating just over the head like a halo. I saw this on the render, the report does not flag it. It is still there in the second pass and I did not fix it. This is why a person must look at the image, and it is item 6 on the checklist.",
    "The 3 by 3 sheet shows the low angle puts the desk across the body and the high angle shows the whole room, which helps choose a camera for a cold open that needs the Warden seen with the radio.",
    "Which side of the frame the mic hand lands on (his left reads on the right of the frame when he faces the lens) is now a measured line, not something to remember.",
]:
    B(t)

H("Checklist before a previs is used as a structure reference")
t = d.add_table(rows=1, cols=2)
t.style = "Light Grid Accent 1"
t.rows[0].cells[0].text = "#"
t.rows[0].cells[1].text = "Confirm (where to read it)"
for ln in open(r"D:\WKP\ANIMATION\previs\CHECKLIST.md", encoding="utf-8").read().splitlines():
    if ln.startswith("| ") and ln[2].isdigit():
        p = [x.strip() for x in ln.strip("|").split("|")]
        c = t.add_row().cells
        c[0].text = p[0]
        c[1].text = p[1] + "  [" + p[2] + "]"
P("This previs fixes layout only, not look. Costume, face, light mood, color, texture, lens character and style come from the master references and the prompt.")

H("What worked and what did not")
for t_ in [
    "Worked: the card to scene to report loop, hand colors that make left and right readable at a glance, the visibility numbers by ray cast, the plan view, the 3 by 3 sheet, the expectation lines that turn a feeling into PASS or FAIL.",
    "Worked: four cards ran headless on this PC in Blender 5.2.4 with Workbench rendering, about 20 to 40 seconds each with all outputs.",
    "Did not work at first: I built the figures with their group empty at the shot position, so every limb was shifted twice. I caught it because the reported hand gap (0.174 m) did not match the picture, fixed it and reran everything.",
    "Did not work at first: 'head in frame' only tested the top of the head, so a nose showing at the edge counted as out of frame. It now tests seven points on the head.",
    "Limit: stand-ins are blocks and tubes. They do not show fingers, faces or clothing, and bodies can pass through each other (the report lists occluders so you can see it). Arms and legs use simple two-bone maths, seated pose is one fixed shape. The 'body percent of frame' line is not meaningful for a seated or cropped figure.",
    "Limit: after saving, moving parts in the Blender window does not re-solve the arms. The method is to change the card and rerun.",
]:
    B(t_)
H("Not verified")
for t_ in [
    "Blender MCP and the look tool were not available (connection refused, addon reports an outdated protocol). I read the renders as image files instead. Nothing touched Zac's open Blender or any of his files. All work ran in separate headless Blender processes.",
    "Whether Firefly, Veo or any engine actually holds a gray previs as a structure reference is UNTESTED and nothing was generated. It is playbook test T6 (sketch first) with a previs as the sketch. It needs a Firefly sitting with Zac, and the credit number is read at the button.",
    "The previs was not run through qa-director. Standards Section A items for sourced or textured assets do not apply, the stand-ins are layout tools, not assets for Unreal.",
    "The Ian hands (both RIGHT) and the WWD hand assignments are my test choices, not taken from Zac's approved cards.",
    "The Warden blocking is not approved art direction. The R3b view from under the car (looking up at the dark underside) is approximated by a straight-on camera, and the underside is look, which the previs does not cover.",
]:
    B(t_)
out = r"D:\WKP Reports\Previs Method\2026-11-24 - Previs Method.docx"
os.makedirs(os.path.dirname(out), exist_ok=True)
d.save(out)
print(out, os.path.getsize(out))
