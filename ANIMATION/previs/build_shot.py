"""
Runs INSIDE Blender (headless):
  C:\\Blender\\5.2.4\\blender.exe -b --factory-startup --python build_shot.py -- <card.json> <outdir> [--plan] [--sheet]
Normally you call previs.py (the wrapper) instead. Never run this against Zac's open .blend.
Writes into <outdir>: shot.png, plan.png, tile_RC.png, report.json, <id>.blend (a copy of the built scene).
"""
import sys, os, json, math
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import bpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
import previs_lib as pv

argv = sys.argv[sys.argv.index("--") + 1:]
card_path, outdir = argv[0], argv[1]
want_plan = "--plan" in argv
want_sheet = "--sheet" in argv
card = json.load(open(card_path, encoding="utf-8"))
os.makedirs(outdir, exist_ok=True)

# clean factory scene
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o)
scene = bpy.context.scene
scene.name = "PV_" + card["id"]
coll = bpy.data.collections.new("PV_" + card["id"])
scene.collection.children.link(coll)

report = {"id": card["id"], "title": card.get("title", ""), "warnings": [], "_chars": {}, "_props": {}}

# ratio and resolution
ratios = {"16:9": (16, 9), "9:16": (9, 16), "1:1": (1, 1), "4:5": (4, 5), "2.39:1": (239, 100), "4:3": (4, 3)}
rw, rh = ratios[card.get("ratio", "16:9")]
long_px = int(card.get("res_long", 1280))
if rw >= rh:
    W, Hh = long_px, int(round(long_px * rh / rw))
else:
    Hh, W = long_px, int(round(long_px * rw / rh))

# location, props, characters
pv.build_location(card.get("location", {}), coll, report)
for p in card.get("props", []):
    pv.build_prop(p, coll, report)
chars = {}
report["_card_chars"] = {c["name"]: c for c in card.get("characters", [])}
for c in card.get("characters", []):
    info = pv.build_figure(c, coll, report)
    chars[c["name"]] = info
    report["_chars"][c["name"]] = {"pelvis": info["pelvis"], "head": info["head"]}

# subject centre
pts = [i["pelvis"] for i in chars.values()] or [Vector((0, 0, 1))]
centre = sum(pts, Vector()) / len(pts)
centre.z = float(card.get("camera", {}).get("target_height", centre.z))

# light
light = card.get("light", {"azimuth_deg": 60, "elevation_deg": 40})
frm = pv.build_light_marker(light, (centre.x, centre.y, 0.0), coll)

# camera
cc = card.get("camera", {})
tgt = cc.get("target", "centroid")
if isinstance(tgt, str):
    tvec = centre if tgt == "centroid" else (chars[tgt]["head"] if cc.get("target_part") == "head" else chars[tgt]["pelvis"])
else:
    tvec = Vector(tgt)
if "loc" in cc:
    cloc = Vector(cc["loc"])
else:
    cloc = pv.orbit_pos(tvec, float(cc.get("distance", 5)), float(cc.get("azimuth_deg", 0)), float(cc.get("height", 1.5)))
lens = float(cc.get("lens_mm", 35))
cam, ctgt = pv.make_camera("shot", coll, cloc, tvec, lens)
scene.camera = cam
pv.setup_render(scene, W, Hh, light_from=frm)
if "roll_deg" in cc:
    cam.constraints[0].up_axis = 'UP_Y'
bpy.context.view_layer.update()

# hide-only-in-some-renders objects
ceilings = [o for o in bpy.data.objects if o.name == "PV_ceiling"]
helpers = [o for o in bpy.data.objects if o.name.startswith(("PV_camtarget",))]
for h in helpers:
    h.hide_render = True


def render(path, camobj, hide_ceiling=False):
    for c in ceilings:
        c.hide_render = hide_ceiling
    scene.camera = camobj
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)


# ---------- report numbers
dg = bpy.context.evaluated_depsgraph_get()
IGNORE = ("PV_light_", "PV_grip_", "PV_camtarget", "PV_grid_", "PV_cam_")


def first_hit(origin, target_pt):
    """Cast from origin toward target_pt, skipping helper objects. Returns (hit_obj_name, hit_dist) or (None, None)."""
    d = target_pt - origin
    total = d.length
    dn = d.normalized()
    o = origin.copy()
    travelled = 0.0
    for _ in range(12):
        hit, loc_, nor, idx, ob, mw = scene.ray_cast(dg, o, dn, distance=max(total - travelled, 0.001))
        if not hit:
            return None, None
        if ob.name.startswith(IGNORE):
            step = (loc_ - o).length + 0.002
            o = o + dn * step
            travelled += step
            continue
        return ob.name, travelled + (loc_ - o).length
    return None, None


camloc = cam.matrix_world.translation
sens_w = cam.data.sensor_width
aspect = W / Hh
if aspect >= 1:
    hfov = 2 * math.degrees(math.atan(sens_w / 2 / lens))
    vfov = 2 * math.degrees(math.atan((sens_w / aspect) / 2 / lens))
else:
    vfov = 2 * math.degrees(math.atan(sens_w / 2 / lens))
    hfov = 2 * math.degrees(math.atan((sens_w * aspect) / 2 / lens))
rep = {"id": card["id"], "title": card.get("title", ""), "ratio": card.get("ratio", "16:9"), "res": [W, Hh],
       "camera": {"loc": [round(v, 3) for v in camloc], "height_m": round(camloc.z, 3), "lens_mm": lens,
                  "sensor_width_mm": sens_w, "hfov_deg": round(hfov, 1), "vfov_deg": round(vfov, 1),
                  "target": [round(v, 3) for v in tvec]},
       "light": {"from_azimuth_deg": light.get("azimuth_deg"), "elevation_deg": light.get("elevation_deg")},
       "characters": {}, "props": {}, "warnings": report["warnings"]}


def proj(p):
    v = world_to_camera_view(scene, cam, Vector(p))
    return v.x, v.y, v.z


for nm, info in chars.items():
    head_top = Vector((info["head"].x, info["head"].y, info["height"] * 0.995))
    feet = Vector((info["pos"][0], info["pos"][1], 0.0))
    hx, hy, hz = proj(head_top)
    fx, fy, fz = proj(feet)
    cinfo = {"height_m": info["height"], "facing_deg": round(info["facing_deg"], 1), "pose": info["pose"],
             "dist_to_camera_m": round((info["pelvis"] - camloc).length, 2),
             "head_top_screen": [round(hx, 3), round(hy, 3)], "feet_screen": [round(fx, 3), round(fy, 3)],
             "body_height_pct_of_frame": round(abs(hy - fy) * 100, 1),
             "head_in_frame": any((lambda v: 0 <= v[0] <= 1 and 0 <= v[1] <= 1 and v[2] > 0)(proj(info["head"] + Vector(o_))) for o_ in
                                  ((0, 0, 0), (0.07 * info["height"], 0, 0), (-0.07 * info["height"], 0, 0), (0, 0.07 * info["height"], 0),
                                   (0, -0.07 * info["height"], 0), (0, 0, 0.08 * info["height"]), (0, 0, -0.08 * info["height"]))),
             "feet_in_frame": 0 <= fx <= 1 and 0 <= fy <= 1 and fz > 0,
             "head_visible_pct": None,
             "hands": {}}
    _hs = [info["head"] + Vector(o_) * info["height"] for o_ in ((0, 0, 0), (0.05, 0, 0), (-0.05, 0, 0), (0, 0.05, 0), (0, -0.05, 0), (0, 0, 0.05), (0, 0, -0.05))]
    _vis = 0
    for _s in _hs:
        _x, _y, _z = proj(_s)
        if not (0 <= _x <= 1 and 0 <= _y <= 1 and _z > 0):
            continue
        _hn, _hd = first_hit(camloc, _s)
        if _hn is None or (_hn.startswith("PV_" + nm + "_head")) or (_hd is not None and _hd > (_s - camloc).length - 0.03):
            _vis += 1
    cinfo["head_visible_pct"] = round(100 * _vis / len(_hs))
    # facing the camera? dot of facing with direction to camera
    f = Vector((math.sin(math.radians(info["facing_deg"])), math.cos(math.radians(info["facing_deg"])), 0))
    tocam = (camloc - info["pelvis"]).normalized()
    cinfo["faces_camera_dot"] = round(f.dot(Vector((tocam.x, tocam.y, 0)).normalized()), 2)
    cinfo["view_of_character"] = ("front" if cinfo["faces_camera_dot"] > 0.7 else "back" if cinfo["faces_camera_dot"] < -0.7
                                  else "side/three-quarter")
    for key in ("L", "R"):
        h = info["hands"][key]
        ho = bpy.data.objects[h["obj"]]
        mw = ho.matrix_world
        samples = [mw @ Vector((sx * 0.4, sy * 0.4, sz * 0.4)) for sx in (-1, 0, 1) for sy in (-1, 0, 1) for sz in (-1, 1)]
        samples.append(mw.translation.copy())
        vis = 0
        occ = {}
        for s in samples:
            x, y, z = proj(s)
            if not (0 <= x <= 1 and 0 <= y <= 1 and z > 0):
                continue
            # nudge target slightly toward the camera so the hand's own surface is not the hit
            hn, hd = first_hit(camloc, s)
            if hn is None or hn == ho.name:
                vis += 1
            else:
                dist_s = (s - camloc).length
                if hd is not None and hd > dist_s - 0.03:
                    vis += 1
                else:
                    occ[hn] = occ.get(hn, 0) + 1
        cx, cy, cz = proj(h["center"])
        holds = h["holds"]
        # does this hand sit over the face on screen? (hand closer to camera than the head, inside the head's screen circle)
        hcx, hcy, hcz = proj(info["head"])
        r_px = abs(proj(info["head"] + Vector((0, 0, 0.078 * info["height"])))[1] - hcy) * Hh
        over_face = any((lambda q: q[2] < hcz and math.hypot((q[0] - hcx) * W, (q[1] - hcy) * Hh) < r_px)(proj(s_)) for s_ in samples)
        if over_face:
            rep["warnings"].append("%s %s hand (%s) is drawn over the face on screen" % (nm, key, "BLUE" if key == "L" else "RED"))
        cinfo["hands"][key] = {
            "colour": "BLUE" if key == "L" else "RED",
            "screen_xy": [round(cx, 3), round(cy, 3)],
            "side_on_screen": "screen-left" if cx < 0.5 else "screen-right",
            "in_frame": 0 <= cx <= 1 and 0 <= cy <= 1 and cz > 0,
            "visible_pct": round(100 * vis / len(samples)),
            "occluded_by": occ,
            "holds": (holds["prop"] + ":" + holds.get("at", "center")) if holds else None,
            "over_face": bool(over_face),
            "reach_shortfall_m": round(h["shortfall"], 3)}
    rep["characters"][nm] = cinfo
for pn, pi in report["_props"].items():
    rep["props"][pn] = {"grips_world": {k: [round(c, 3) for c in v] for k, v in pi["grips"].items()}}
# hand-to-hand gaps between different characters
gaps = []
names = list(chars)
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        for a in "LR":
            for b in "LR":
                d = (chars[names[i]]["hands"][a]["center"] - chars[names[j]]["hands"][b]["center"]).length
                gaps.append({"between": "%s.%s / %s.%s" % (names[i], a, names[j], b), "m": round(d, 3)})
rep["hand_gaps_m"] = sorted(gaps, key=lambda g: g["m"])[:4]
# frame warnings
for nm, c in rep["characters"].items():
    if not c["head_in_frame"]:
        rep["warnings"].append("%s head is outside the frame" % nm)
    for k, h in c["hands"].items():
        if h["holds"] and h["visible_pct"] < 50:
            rep["warnings"].append("%s %s hand (%s) holds %s but only %d%% of it is visible to this camera%s" % (
                nm, k, h["colour"], h["holds"], h["visible_pct"], (", hidden by " + ", ".join(h["occluded_by"])) if h["occluded_by"] else ""))
json.dump(rep, open(os.path.join(outdir, "report.json"), "w", encoding="utf-8"), indent=1)

# ---------- renders
render(os.path.join(outdir, "shot.png"), cam)

if want_plan:
    xs = [info_["pos"][0] for info_ in chars.values()] + [camloc.x, tvec.x]
    ys = [info_["pos"][1] for info_ in chars.values()] + [camloc.y, tvec.y]
    span = max(max(xs) - min(xs), max(ys) - min(ys)) + 3.0
    cx_, cy_ = (max(xs) + min(xs)) / 2, (max(ys) + min(ys)) / 2
    # plan marker: green camera wedge pointing at the target
    gm = pv._mat("PV_M_cam", pv.GREEN)
    d = (Vector((tvec.x, tvec.y, 0)) - Vector((camloc.x, camloc.y, 0))).normalized()
    a0 = Vector((camloc.x, camloc.y, 0.05))
    pv._between("PV_plan_camshaft", a0, a0 + d * 0.5, 0.06, coll, gm)
    pv._between("PV_plan_camhead", a0 + d * 0.5, a0 + d * 0.9, 0.16, coll, gm, kind="cone")
    pv._between("PV_plan_view_line", a0, Vector((tvec.x, tvec.y, 0.05)), 0.012, coll, gm)
    pcam, ptgt = pv.make_camera("plan", coll, (cx_, cy_, 30), (cx_, cy_, 0), 50, ortho=True, ortho_scale=span)
    ptgt.hide_render = True
    pcam.constraints.remove(pcam.constraints[0])
    pcam.rotation_euler = (0, 0, 0)         # looking straight down, +Y up the page
    for o in bpy.data.objects:
        if o.name.startswith("PV_plan_"):
            o.hide_render = False
    side = int(min(W, Hh) if min(W, Hh) > 700 else 900)
    scene.render.resolution_x = scene.render.resolution_y = side
    render(os.path.join(outdir, "plan.png"), pcam, hide_ceiling=True)
    for o in bpy.data.objects:
        if o.name.startswith("PV_plan_"):
            o.hide_render = True
    scene.render.resolution_x, scene.render.resolution_y = W, Hh

if want_sheet:
    base_az = float(cc.get("azimuth_deg", 0))
    dist = (camloc - Vector((tvec.x, tvec.y, camloc.z))).length
    heights = [("low", 0.5), ("eye", camloc.z), ("high", 3.5)]
    azs = [base_az - 55, base_az, base_az + 55]
    scene.render.resolution_x, scene.render.resolution_y = (640, int(640 * Hh / W)) if W >= Hh else (int(640 * W / Hh), 640)
    for r, (hn, hh) in enumerate(heights):
        for c, az in enumerate(azs):
            t = Vector((tvec.x, tvec.y, tvec.z))
            tc, tt = pv.make_camera("tile%d%d" % (r, c), coll, pv.orbit_pos(t, dist, az, hh), t, lens)
            tt.hide_render = True
            render(os.path.join(outdir, "tile_%d%d.png" % (r, c)), tc, hide_ceiling=(hn == "high"))
    scene.render.resolution_x, scene.render.resolution_y = W, Hh
    scene.camera = cam
    json.dump({"azimuths": azs, "heights": heights}, open(os.path.join(outdir, "sheet.json"), "w"))

for c in ceilings:
    c.hide_render = False
cs = os.path.join(here, "lens_cheatsheet.md")
if os.path.exists(cs) and "PV_LensCheatSheet" not in bpy.data.texts:
    t_ = bpy.data.texts.new("PV_LensCheatSheet")
    t_.write(open(cs, encoding="utf-8").read() + "\n\nHands: BLUE = character's LEFT, RED = RIGHT. Dark wedge = nose. +Y away from front camera, +X right.\n")
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(outdir, card["id"] + ".blend"), copy=True)
print("PREVIS_OK", outdir)
