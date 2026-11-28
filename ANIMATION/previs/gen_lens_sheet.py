"""Writes lens_cheatsheet.md from the sensor maths (36 mm full-frame width, sensor_fit AUTO as in previs_lib)."""
import math
S = 36.0
rows = [(14, "ultra wide, interiors, distortion at edges"), (18, "very wide, tight rooms, vehicles interior"), (24, "wide establishing, handheld feel"),
        (28, "wide, street level, group of people in a room"), (35, "the everyday cinema lens, our default habit"), (50, "natural, close to what the eye sees, medium shots"),
        (85, "portrait, close-ups, flattens depth"), (100, "tight close-up, inserts, hands"), (135, "very tight, compressed depth, far inserts")]
def fov(sensor, f): return 2 * math.degrees(math.atan(sensor / 2 / f))
out = ["# Lens cheat sheet (previs)", "",
       "Sensor width 36 mm (full frame). Blender fits the sensor to the LONGER side of the frame (sensor_fit AUTO), so in 9:16 the 36 mm runs up and down. Numbers are computed by `gen_lens_sheet.py`, not typed.", "",
       "Distance column: metres from the camera to a standing 1.75 m person so the whole body fits with a 10 percent margin, and to frame a head-and-shoulders (0.60 m tall) with 10 percent margin.", "",
       "| Lens mm | Long-edge FOV deg | 16:9 vertical FOV deg | Full body 16:9 (m) | Full body 9:16 (m) | Head and shoulders 16:9 (m) | Head and shoulders 9:16 (m) | Use |",
       "|---|---|---|---|---|---|---|---|"]
for f, use in rows:
    lf = fov(S, f)
    v169 = fov(S * 9 / 16, f)
    fb169 = 1.75 * 1.1 * f / (S * 9 / 16)
    fb916 = 1.75 * 1.1 * f / S
    hs169 = 0.60 * 1.1 * f / (S * 9 / 16)
    hs916 = 0.60 * 1.1 * f / S
    out.append("| %d | %.1f | %.1f | %.1f | %.1f | %.1f | %.1f | %s |" % (f, lf, v169, fb169, fb916, hs169, hs916, use))
out += ["", "## Heights and angles", "",
        "| Camera height (m) | Reads as |", "|---|---|",
        "| 0.3 to 0.6 | low angle, looks up at people, floor and legs, hero or threat |",
        "| 1.2 to 1.4 | seated eye level or chest height, neutral for seated people |",
        "| 1.5 to 1.7 | standing eye level, neutral |",
        "| 2.5 to 4 | high angle, shows layout and who stands where, small or weak feel |",
        "| 20 and up, straight down | plan view, use it for who stands where (the previs makes this automatically with --plan) |", "",
        "## Reading the numbers", "",
        "- A longer lens makes the same distance look tighter and flattens depth. A wider lens needs less distance and bends the edges.",
        "- Previs lens numbers are GEOMETRY. An image or video engine reads 'a 35 mm lens' as a mood word and will not match the exact field of view. Use the previs to settle framing and who stands where, then write the framing in plain words (shot size, angle, which side) in the prompt.",
        "- Keep one lens habit across a sequence (playbook B3). If the previs shot list mixes 24 and 85 mm without a reason, ask why.", ""]
open("lens_cheatsheet.md", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out[:16]))
