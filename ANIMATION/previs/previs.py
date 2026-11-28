"""
Previs wrapper. Run with normal Python (Pillow needed) :
  python previs.py <card.json> [--out DIR] [--plan] [--sheet] [--guides]
Builds the gray blocking in headless Blender, renders the shot (and plan, 3x3 sheet), checks the
card's "expect" lines against numbers read from the scene, and writes:
  shot.png (captioned), plan.png, sheet.png, report.json, REPORT.md, <id>.blend
No credits, no network, no Adobe. Never touches any open Blender session.
"""
import sys, os, json, subprocess, argparse, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
BLENDER = r"C:\Blender\5.2.4\blender.exe"

ap = argparse.ArgumentParser()
ap.add_argument("card")
ap.add_argument("--out")
ap.add_argument("--plan", action="store_true")
ap.add_argument("--sheet", action="store_true")
ap.add_argument("--guides", action="store_true", help="draw rule-of-thirds lines on shot.png")
a = ap.parse_args()

card = json.load(open(a.card, encoding="utf-8"))
out = a.out or os.path.join(HERE, "renders", card["id"])
os.makedirs(out, exist_ok=True)
cmd = [BLENDER, "-b", "--factory-startup", "--python", os.path.join(HERE, "build_shot.py"), "--",
       os.path.abspath(a.card), out] + (["--plan"] if a.plan else []) + (["--sheet"] if a.sheet else [])
r = subprocess.run(cmd, capture_output=True, text=True)
if "PREVIS_OK" not in r.stdout:
    print(r.stdout[-3000:], r.stderr[-3000:])
    sys.exit("previs build failed")

from PIL import Image, ImageDraw, ImageFont
rep = json.load(open(os.path.join(out, "report.json"), encoding="utf-8"))


def font(sz):
    for f in (r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\segoeui.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


# ---- expectations
results = []
for e in card.get("expect", []):
    ch = rep["characters"].get(e.get("char"))
    label = e.get("note", json.dumps(e))
    if "gap_between" in e:
        pair = e["gap_between"]
        match = [g for g in rep["hand_gaps_m"] if g["between"] == pair]
        # gap list holds only the 4 smallest; recompute not needed for the proof cards
        ok = bool(match) and e.get("min", 0) <= match[0]["m"] <= e.get("max", 99)
        results.append((ok, label, "gap %s m" % (match[0]["m"] if match else "not in the 4 smallest")))
        continue
    if ch is None:
        results.append((False, label, "character not found"))
        continue
    if "hand" in e:
        h = ch["hands"][e["hand"]]
        checks = []
        if "visible_min" in e:
            checks.append((h["visible_pct"] >= e["visible_min"], "visible %d%% (need %d)" % (h["visible_pct"], e["visible_min"])))
        if "over_face" in e:
            checks.append((h["over_face"] == e["over_face"], "hand over face %s (need %s)" % (h["over_face"], e["over_face"])))
        if "visible_max" in e:
            checks.append((h["visible_pct"] <= e["visible_max"], "visible %d%% (allowed up to %d)" % (h["visible_pct"], e["visible_max"])))
        if "screen_side" in e:
            checks.append((h["side_on_screen"] == e["screen_side"], "on %s (need %s)" % (h["side_on_screen"], e["screen_side"])))
        if "holds" in e:
            checks.append((h["holds"] == e["holds"], "holds %s (need %s)" % (h["holds"], e["holds"])))
        if e.get("in_frame"):
            checks.append((h["in_frame"], "in frame %s" % h["in_frame"]))
        results.append((all(c[0] for c in checks), label, "; ".join(c[1] for c in checks)))
    else:
        checks = []
        if "head_in_frame" in e:
            checks.append((ch["head_in_frame"] == e["head_in_frame"], "head in frame %s (need %s)" % (ch["head_in_frame"], e["head_in_frame"])))
        if "head_visible_max" in e:
            checks.append((ch["head_visible_pct"] <= e["head_visible_max"], "head visible %s%% (allowed up to %d)" % (ch["head_visible_pct"], e["head_visible_max"])))
        if "feet_in_frame" in e:
            checks.append((ch["feet_in_frame"] == e["feet_in_frame"], "feet in frame %s (need %s)" % (ch["feet_in_frame"], e["feet_in_frame"])))
        if "facing_dot_min" in e:
            checks.append((ch["faces_camera_dot"] >= e["facing_dot_min"], "facing dot %.2f (need %.2f)" % (ch["faces_camera_dot"], e["facing_dot_min"])))
        if "body_pct_min" in e:
            checks.append((ch["body_height_pct_of_frame"] >= e["body_pct_min"], "body %.0f%% of frame (need %d)" % (ch["body_height_pct_of_frame"], e["body_pct_min"])))
        results.append((all(c[0] for c in checks), label, "; ".join(c[1] for c in checks)))
rep["expect_results"] = [{"pass": ok, "expect": l, "measured": m} for ok, l, m in results]
json.dump(rep, open(os.path.join(out, "report.json"), "w", encoding="utf-8"), indent=1)

# ---- caption the shot
shot = Image.open(os.path.join(out, "shot.png")).convert("RGB")
cam = rep["camera"]
cap = "%s | %s | %s mm | cam %.2f m high | HFOV %.0f VFOV %.0f | blue = LEFT hand, red = RIGHT hand, dark wedge = nose | GRAY LAYOUT ONLY, NOT LOOK" % (
    card["id"], rep["ratio"], ("%g" % cam["lens_mm"]), cam["height_m"], cam["hfov_deg"], cam["vfov_deg"])
if a.guides:
    d = ImageDraw.Draw(shot)
    for i in (1, 2):
        d.line([(shot.width * i / 3, 0), (shot.width * i / 3, shot.height)], fill=(255, 255, 255), width=1)
        d.line([(0, shot.height * i / 3), (shot.width, shot.height * i / 3)], fill=(255, 255, 255), width=1)
fs = max(12, shot.width // 70) if shot.width >= shot.height else max(11, shot.width // 38)
f = font(fs)
words, lines, cur = cap.split(" "), [], ""
for w in words:
    if f.getlength(cur + " " + w) > shot.width - 16:
        lines.append(cur)
        cur = w
    else:
        cur = (cur + " " + w).strip()
lines.append(cur)
bar = Image.new("RGB", (shot.width, (fs + 4) * len(lines) + 8), (20, 20, 20))
bd = ImageDraw.Draw(bar)
for i, ln in enumerate(lines):
    bd.text((8, 4 + i * (fs + 4)), ln, fill=(240, 240, 240), font=f)
final = Image.new("RGB", (shot.width, shot.height + bar.height))
final.paste(shot, (0, 0))
final.paste(bar, (0, shot.height))
final.save(os.path.join(out, "shot_captioned.png"))

# ---- plan caption
if a.plan and os.path.exists(os.path.join(out, "plan.png")):
    p = Image.open(os.path.join(out, "plan.png")).convert("RGB")
    d = ImageDraw.Draw(p)
    d.text((10, 8), "PLAN VIEW from above. Up the page = +Y. Green arrow = camera. Yellow = light. Grid = 1 m", fill=(0, 0, 0), font=font(15))
    p.save(os.path.join(out, "plan_captioned.png"))

# ---- 3x3 sheet
if a.sheet and os.path.exists(os.path.join(out, "sheet.json")):
    sj = json.load(open(os.path.join(out, "sheet.json")))
    t00 = Image.open(os.path.join(out, "tile_00.png"))
    tw, th = t00.size
    t00.close()
    sheet = Image.new("RGB", (tw * 3 + 8, th * 3 + 8), (30, 30, 30))
    fl = font(14)
    for r_ in range(3):
        for c_ in range(3):
            t = Image.open(os.path.join(out, "tile_%d%d.png" % (r_, c_))).convert("RGB")
            ImageDraw.Draw(t).rectangle([0, 0, 245, 20], fill=(20, 20, 20))
            ImageDraw.Draw(t).text((4, 2), "%s %s az %+d%s" % (sj["heights"][r_][0], "%.1fm" % sj["heights"][r_][1], sj["azimuths"][c_], "  (SHOT CAM)" if (r_ == 1 and c_ == 1) else ""), fill=(255, 255, 255), font=fl)
            sheet.paste(t, (c_ * (tw + 4), r_ * (th + 4)))
    sheet.save(os.path.join(out, "sheet_3x3.png"))
    for r_ in range(3):
        for c_ in range(3):
            os.remove(os.path.join(out, "tile_%d%d.png" % (r_, c_)))

# ---- REPORT.md
L = ["# Previs report: %s" % card.get("title", card["id"]), "",
     "Built %s. Gray layout only, fixes WHO STANDS WHERE, WHICH HAND, SCALE, CAMERA. It does not fix look." % datetime.date.today().isoformat(), "",
     "Action: %s" % card.get("action", ""), "",
     "## Camera", "",
     "- ratio %s, %dx%d px, lens %g mm on a %g mm sensor, HFOV %.1f deg, VFOV %.1f deg" % (rep["ratio"], rep["res"][0], rep["res"][1], cam["lens_mm"], cam["sensor_width_mm"], cam["hfov_deg"], cam["vfov_deg"]),
     "- camera at %s (height %.2f m), looking at %s" % (cam["loc"], cam["height_m"], cam["target"]), "",
     "## Characters (read from the scene)", ""]
for nm, c in rep["characters"].items():
    L.append("- **%s**: %.2f m, %s, facing %.0f deg, %.2f m from camera, seen from the %s, body is %.0f%% of frame height, head in frame %s, feet in frame %s" % (
        nm, c["height_m"], c["pose"], c["facing_deg"], c["dist_to_camera_m"], c["view_of_character"], c["body_height_pct_of_frame"], c["head_in_frame"], c["feet_in_frame"]))
    for k, h in c["hands"].items():
        L.append("  - %s hand (%s): on %s, %d%% visible%s, holds %s%s" % (
            k, h["colour"], h["side_on_screen"], h["visible_pct"], (" (hidden by %s)" % ", ".join(h["occluded_by"])) if h["occluded_by"] else "",
            h["holds"] or "nothing", (", REACH SHORT by %.2f m" % h["reach_shortfall_m"]) if h["reach_shortfall_m"] > 0.005 else ""))
L += ["", "Closest hand to hand distances (m): " + "; ".join("%s = %s" % (g["between"], g["m"]) for g in rep["hand_gaps_m"]), "",
      "## Card expectations", ""]
for x in rep["expect_results"]:
    L.append("- %s: %s (%s)" % ("PASS" if x["pass"] else "FAIL", x["expect"], x["measured"]))
L += ["", "## Warnings from the scene", ""] + (["- " + w for w in rep["warnings"]] or ["- none"])
open(os.path.join(out, "REPORT.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("OK", out)
print("\n".join(L))
