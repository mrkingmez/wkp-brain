"""
WKP Previs library (Blender 5.2.x, bpy only, no add-ons, no network, no credits).

Builds gray stand-in figures, location blocks, props, a light marker and a
camera rig from a plain dict (a "shot card"), then reports framing facts.

Coordinates (metres, 1 Blender unit = 1 m):
  +X = right of the front camera, +Y = away from the front camera, +Z = up.
  A camera at azimuth 0 stands on the -Y side and looks toward +Y.
  Compass facing (degrees): 0 faces +Y, 90 faces +X, 180 faces -Y, 270 faces -X.
  LEFT and RIGHT hands are the CHARACTER's own hands, not the screen's.
  Left hand = BLUE, right hand = RED. The dark wedge on the head is the nose (facing).
Every object made here is named PV_* so cleanup and audits are exact.
"""
import math
import bpy
import bmesh
from mathutils import Vector, Matrix

GRAY_FIG = (0.55, 0.55, 0.57, 1)
GRAY_NOSE = (0.18, 0.18, 0.2, 1)
GRAY_LOC = (0.80, 0.80, 0.78, 1)
GRAY_PROP = (0.68, 0.64, 0.55, 1)
GRAY_GROUND = (0.62, 0.62, 0.62, 1)
GRID_LINE = (0.25, 0.25, 0.25, 1)
BLUE = (0.10, 0.30, 0.95, 1)   # LEFT hand
RED = (0.95, 0.12, 0.08, 1)    # RIGHT hand
YELLOW = (1.0, 0.85, 0.0, 1)   # light marker
GREEN = (0.1, 0.7, 0.2, 1)     # camera marker (plan view)

# ---------------------------------------------------------------- helpers

def _mat(name, rgba):
    m = bpy.data.materials.get(name)
    if m is None:
        m = bpy.data.materials.new(name)
    m.diffuse_color = rgba            # Workbench reads this
    try:
        p = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
        p.inputs["Base Color"].default_value = rgba
    except Exception:
        pass
    return m


_unit = {}


def _unit_mesh(kind):
    """Shared unit meshes: box 1x1x1, cylinder r=1 depth=1 along Z, sphere r=1, cone r=1 depth=1."""
    if kind in _unit and _unit[kind].name in bpy.data.meshes:
        return _unit[kind]
    me = bpy.data.meshes.new("PV_unit_" + kind)
    bm = bmesh.new()
    if kind == "box":
        bmesh.ops.create_cube(bm, size=1.0)
    elif kind == "cyl":
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=16,
                              radius1=1.0, radius2=1.0, depth=1.0)
    elif kind == "sphere":
        bmesh.ops.create_uvsphere(bm, u_segments=20, v_segments=12, radius=1.0)
    elif kind == "cone":
        bmesh.ops.create_cone(bm, cap_ends=True, cap_tris=False, segments=16,
                              radius1=1.0, radius2=0.0, depth=1.0)
    bm.to_mesh(me)
    bm.free()
    for p in me.polygons:
        p.use_smooth = kind in ("sphere",)
    _unit[kind] = me
    return me


def _obj(name, kind, coll, mat, loc=(0, 0, 0), scale=(1, 1, 1), quat=None, parent=None):
    ob = bpy.data.objects.new(name, _unit_mesh(kind))
    ob.location = loc
    ob.scale = scale
    if quat is not None:
        ob.rotation_mode = 'QUATERNION'
        ob.rotation_quaternion = quat
    coll.objects.link(ob)
    ob.color = mat.diffuse_color          # Workbench 'OBJECT' colour mode reads this
    if not ob.data.materials:
        ob.data.materials.append(mat)
    ob.material_slots[0].link = 'OBJECT'  # shared mesh, per-object material
    ob.material_slots[0].material = mat
    if parent is not None:
        ob.parent = parent
    return ob


def _between(name, a, b, radius, coll, mat, parent=None, kind="cyl"):
    a, b = Vector(a), Vector(b)
    d = b - a
    ln = max(d.length, 1e-4)
    q = d.normalized().to_track_quat('Z', 'Y')
    return _obj(name, kind, coll, mat, loc=(a + b) / 2, scale=(radius, radius, ln), quat=q, parent=parent)


def _box(name, center, size, coll, mat, quat=None, parent=None):
    return _obj(name, "box", coll, mat, loc=center, scale=size, quat=quat, parent=parent)


def _dir_quat(forward, up=Vector((0, 0, 1))):
    """Quaternion whose local +Y points along `forward`, local Z kept up."""
    return Vector(forward).normalized().to_track_quat('Y', 'Z')


def _ik(root, target, l1, l2, pole):
    """Analytic two-bone IK. Returns (mid, end, shortfall). pole = direction the joint bends toward."""
    root, target = Vector(root), Vector(target)
    d = target - root
    dist = d.length
    reach = l1 + l2
    short = 0.0
    if dist > reach - 1e-4:
        short = dist - reach
        dist = reach - 1e-4
        d = d.normalized() * dist
        target = root + d
    if dist < abs(l1 - l2) + 1e-4:
        dist = abs(l1 - l2) + 1e-4
    dn = d.normalized()
    a = (l1 * l1 - l2 * l2 + dist * dist) / (2 * dist)
    h = math.sqrt(max(l1 * l1 - a * a, 0.0))
    p = Vector(pole) - dn * Vector(pole).dot(dn)
    if p.length < 1e-5:
        p = Vector((0, 0, 1)) - dn * dn.z
    p.normalize()
    mid = root + dn * a + p * h
    return mid, target, short


# ---------------------------------------------------------------- figure

def _char_pt(report, name, part):
    """Point of another character. Works for characters listed later in the card (uses card position and height)."""
    if name in report["_chars"]:
        return report["_chars"][name][part]
    c = report["_card_chars"][name]
    z = 0.93 * c.get("height", 1.75) if part == "head" else 0.52 * c.get("height", 1.75)
    return Vector((c["pos"][0], c["pos"][1], z))


def build_figure(spec, coll, report):
    """Plain gray stand-in. spec keys: name, height, build, pos [x,y], facing_deg | facing_to,
    pose stand|sit, seat_height, left_hand / right_hand, look_at."""
    nm = spec["name"]
    H = float(spec.get("height", 1.75))
    bw = {"lean": 0.9, "average": 1.0, "adult": 1.0, "stocky": 1.15, "child": 1.0}.get(spec.get("build", "average"), 1.0)
    pos = spec.get("pos", [0, 0])
    px, py = float(pos[0]), float(pos[1])
    # facing
    if "facing_to" in spec:
        t = spec["facing_to"]
        tp = Vector(t) if isinstance(t, (list, tuple)) else _char_pt(report, t, "pelvis")
        v = Vector((tp[0] - px, tp[1] - py, 0))
        fa = math.degrees(math.atan2(v.x, v.y))
    else:
        fa = float(spec.get("facing_deg", 0))
    f = Vector((math.sin(math.radians(fa)), math.cos(math.radians(fa)), 0))
    right = Vector((f.y, -f.x, 0))     # f x z : the character's own right
    left = -right
    pose = spec.get("pose", "stand")
    if pose == "lie":
        return build_figure_lie(spec, coll, report)
    if pose == "sit":
        hip_h = float(spec.get("seat_height", 0.45)) + 0.07 * H
    elif pose == "crouch":
        hip_h = float(spec.get("crouch_hip", 0.30)) * H
    else:
        hip_h = 0.52 * H
    pelvis = Vector((px, py, hip_h))
    sh_h = hip_h + 0.30 * H
    sw = 0.13 * H * bw                 # half shoulder width
    hw = 0.055 * H * bw                # half hip width
    u_arm, f_arm, hand_len = 0.17 * H, 0.15 * H, 0.10 * H
    thigh, shin = 0.240 * H, 0.235 * H
    mat_f = _mat("PV_M_figure", GRAY_FIG)
    mat_n = _mat("PV_M_nose", GRAY_NOSE)
    mat_l = _mat("PV_M_handL_blue", BLUE)
    mat_r = _mat("PV_M_handR_red", RED)

    root = bpy.data.objects.new("PV_fig_" + nm, None)
    root.empty_display_type = 'PLAIN_AXES'
    root.empty_display_size = 0.15
    root.location = (0, 0, 0)   # children use WORLD coordinates, so the group empty stays at the origin
    coll.objects.link(root)

    def P(n):
        return "PV_%s_%s" % (nm, n)

    # torso and pelvis
    tq = _dir_quat(f)
    _box(P("torso"), pelvis + Vector((0, 0, 0.17 * H)), (2 * sw * 0.95, 0.12 * H * bw, 0.30 * H), coll, mat_f, tq, root)
    _box(P("pelvis"), pelvis, (2 * hw * 1.5, 0.11 * H * bw, 0.10 * H), coll, mat_f, tq, root)
    # neck, head, nose
    neck_b = Vector((px, py, sh_h))
    head_c = Vector((px, py, sh_h + 0.115 * H))
    _between(P("neck"), neck_b, neck_b + Vector((0, 0, 0.05 * H)), 0.03 * H, coll, mat_f, root)
    hd = _obj(P("head"), "sphere", coll, mat_f, loc=head_c, scale=(0.060 * H, 0.068 * H, 0.078 * H),
              quat=_dir_quat(f), parent=root)
    look = f
    if "look_at" in spec:
        la = spec["look_at"]
        lp = Vector(la) if isinstance(la, (list, tuple)) else _char_pt(report, la, "head")
        look = (lp - head_c).normalized()
        hd.rotation_quaternion = look.to_track_quat('Y', 'Z')
    # nose wedge: cone pointing along look
    nose_c = head_c + look * 0.075 * H
    _obj(P("nose"), "cone", coll, mat_n, loc=nose_c,
         scale=(0.016 * H, 0.016 * H, 0.04 * H), quat=look.to_track_quat('Z', 'Y'), parent=root)
    # NOTE the cone's tip is local +Z; to_track_quat('Z','Y') points local Z along look.
    # legs
    pole_f = f + Vector((0, 0, 0.0))
    feet = {}
    for side, sgn, key in ((right, 1, "R"), (left, -1, "L")):
        hip = pelvis + side * hw * 0.9 - Vector((0, 0, 0.02 * H))
        if pose == "sit":
            ankle = Vector((hip.x + f.x * thigh * 0.95, hip.y + f.y * thigh * 0.95, 0.04 * H))
        else:
            ankle = Vector((hip.x, hip.y, 0.04 * H))
            if "stance" in spec and key in spec["stance"]:
                ankle = Vector((spec["stance"][key][0], spec["stance"][key][1], 0.04 * H))
        knee, ankle2, short = _ik(hip, ankle, thigh, shin, f * 1.0 + Vector((0, 0, 0.1)))
        mat = mat_f
        _between(P("thigh" + key), hip, knee, 0.045 * H * bw, coll, mat, root)
        _between(P("shin" + key), knee, ankle2, 0.038 * H * bw, coll, mat, root)
        fq = _dir_quat(f)
        _box(P("foot" + key), Vector((ankle2.x, ankle2.y, 0.02 * H)) + f * 0.04 * H,
             (0.045 * H * 1.2, 0.14 * H, 0.04 * H), coll, mat_f, fq, root)
        feet[key] = ankle2
        if short > 0.005:
            report["warnings"].append("%s %s leg cannot reach its foot target by %.2f m" % (nm, key, short))

    # arms
    hands = {}
    for key, side, mat in (("L", left, mat_l), ("R", right, mat_r)):
        shoulder = Vector((px, py, sh_h - 0.02 * H)) + side * sw
        hspec = spec.get("left_hand" if key == "L" else "right_hand")
        target = None
        holds = None
        if hspec:
            if "holds" in hspec:
                holds = hspec["holds"]
                gp = report["_props"][holds["prop"]]["grips"][holds.get("at", "center")]
                target = Vector(gp)
            elif "reach" in hspec:
                target = Vector(hspec["reach"])
            elif "on" in hspec:           # rest on a surface point
                target = Vector(hspec["on"])
        if target is None:
            target = shoulder + side * 0.02 * H + Vector((0, 0, -(u_arm + f_arm) * 0.96)) + f * 0.02 * H
            pole = -f + side * 0.3
        else:
            pole = Vector((0, 0, -1)) * 0.8 + side * 0.9 - f * 0.1
        # wrist sits a half hand before the target
        u = (target - shoulder)
        u = u.normalized() if u.length > 1e-4 else f
        wrist_t = target - u * hand_len * 0.5
        elbow, wrist, short = _ik(shoulder, wrist_t, u_arm, f_arm, pole)
        if short > 0.005:
            report["warnings"].append("%s %s arm falls short of its target by %.2f m (previs shows a straight arm)" % (nm, key, short))
        _between(P("uarm" + key), shoulder, elbow, 0.032 * H * bw, coll, mat_f, root)
        _between(P("farm" + key), elbow, wrist, 0.027 * H * bw, coll, mat_f, root)
        hdir = (wrist - elbow).normalized()
        hc = wrist + hdir * hand_len * 0.5
        hq = hdir.to_track_quat('Y', 'Z')
        hob = _box(P("hand" + key), hc, (0.04 * H * 1.1, hand_len, 0.025 * H * 1.6), coll, mat, hq, root)
        # small shoulder ball
        _obj(P("sh" + key), "sphere", coll, mat_f, loc=shoulder, scale=(0.04 * H,) * 3, parent=root)
        hands[key] = {"obj": hob.name, "center": hc, "holds": holds, "shortfall": short}
    return {"root": root, "pos": (px, py), "facing_deg": fa, "right": right, "pelvis": pelvis, "head": head_c,
            "hands": hands, "feet": feet, "height": H, "look": look, "pose": pose}


def build_figure_lie(spec, coll, report):
    """Supine stand-in lying on its back (creeper). spec: pos [x,y] (pelvis), head_dir_deg (compass the HEAD points),
    pelvis_z (default 0.17), left_hand / right_hand as for build_figure. Face points up (+Z)."""
    nm = spec["name"]
    H = float(spec.get("height", 1.75))
    bw = {"lean": 0.9, "average": 1.0, "adult": 1.0, "stocky": 1.15, "child": 1.0}.get(spec.get("build", "average"), 1.0)
    px, py = [float(v) for v in spec.get("pos", [0, 0])]
    hd_deg = float(spec.get("head_dir_deg", 0))
    ax = Vector((math.sin(math.radians(hd_deg)), math.cos(math.radians(hd_deg)), 0))   # pelvis -> head
    up = Vector((0, 0, 1))
    right = up.cross(ax)          # character's own right when lying face up (forward = +Z): Z x ax
    right = Vector((0, 0, 1)).cross(ax)
    left = -right
    zc = float(spec.get("pelvis_z", 0.17))
    pelvis = Vector((px, py, zc))
    sw = 0.13 * H * bw
    hw = 0.055 * H * bw
    u_arm, f_arm, hand_len = 0.17 * H, 0.15 * H, 0.10 * H
    thigh, shin = 0.240 * H, 0.235 * H
    mat_f = _mat("PV_M_figure", GRAY_FIG)
    mat_n = _mat("PV_M_nose", GRAY_NOSE)
    mat_l = _mat("PV_M_handL_blue", BLUE)
    mat_r = _mat("PV_M_handR_red", RED)
    root = bpy.data.objects.new("PV_fig_" + nm, None)
    root.empty_display_type = 'PLAIN_AXES'
    root.empty_display_size = 0.15
    coll.objects.link(root)

    def P(n):
        return "PV_%s_%s" % (nm, n)
    tq = _dir_quat(ax)
    sh_c = pelvis + ax * 0.30 * H
    _box(P("torso"), pelvis + ax * 0.17 * H, (2 * sw * 0.95, 0.30 * H, 0.12 * H * bw), coll, mat_f, tq, root)
    _box(P("pelvis"), pelvis, (2 * hw * 1.5, 0.10 * H, 0.11 * H * bw), coll, mat_f, tq, root)
    neck_b = sh_c
    head_c = sh_c + ax * 0.115 * H + Vector((0, 0, 0.0))
    _between(P("neck"), neck_b, neck_b + ax * 0.05 * H, 0.03 * H, coll, mat_f, root)
    _obj(P("head"), "sphere", coll, mat_f, loc=head_c, scale=(0.060 * H, 0.078 * H, 0.068 * H), quat=tq, parent=root)
    look = up
    nose_c = head_c + look * 0.075 * H
    _obj(P("nose"), "cone", coll, mat_n, loc=nose_c, scale=(0.016 * H, 0.016 * H, 0.04 * H),
         quat=look.to_track_quat('Z', 'Y'), parent=root)
    feet = {}
    for side, key in ((right, "R"), (left, "L")):
        hip = pelvis + side * hw * 0.9
        ankle = hip - ax * (thigh + shin) * 0.995
        _between(P("thigh" + key), hip, hip - ax * thigh, 0.045 * H * bw, coll, mat_f, root)
        _between(P("shin" + key), hip - ax * thigh, ankle, 0.038 * H * bw, coll, mat_f, root)
        _box(P("foot" + key), ankle - ax * 0.04 * H, (0.045 * H * 1.2, 0.14 * H, 0.04 * H), coll, mat_f, tq, root)
        feet[key] = ankle
    hands = {}
    for key, side, mat in (("L", left, mat_l), ("R", right, mat_r)):
        shoulder = sh_c + side * sw
        hspec = spec.get("left_hand" if key == "L" else "right_hand")
        target = None
        holds = None
        if hspec:
            if "holds" in hspec:
                holds = hspec["holds"]
                target = Vector(report["_props"][holds["prop"]]["grips"][holds.get("at", "center")])
            elif "reach" in hspec:
                target = Vector(hspec["reach"])
            elif "on" in hspec:
                target = Vector(hspec["on"])
        if target is None:
            target = shoulder - ax * (u_arm + f_arm) * 0.96   # relaxed at his side along the body
            target.z = zc + 0.02
        u = target - shoulder
        u = u.normalized() if u.length > 1e-4 else side
        wrist_t = target - u * hand_len * 0.5
        elbow, wrist, short = _ik(shoulder, wrist_t, u_arm, f_arm, side * 0.3 + Vector((0, 0, 0.4)))
        if short > 0.005:
            report["warnings"].append("%s %s arm falls short of its target by %.2f m (previs shows a straight arm)" % (nm, key, short))
        _between(P("uarm" + key), shoulder, elbow, 0.032 * H * bw, coll, mat_f, root)
        _between(P("farm" + key), elbow, wrist, 0.027 * H * bw, coll, mat_f, root)
        hdir = (wrist - elbow).normalized()
        hc = wrist + hdir * hand_len * 0.5
        hob = _box(P("hand" + key), hc, (0.04 * H * 1.1, hand_len, 0.025 * H * 1.6), coll, mat, hdir.to_track_quat('Y', 'Z'), root)
        _obj(P("sh" + key), "sphere", coll, mat_f, loc=shoulder, scale=(0.04 * H,) * 3, parent=root)
        hands[key] = {"obj": hob.name, "center": hc, "holds": holds, "shortfall": short}
    return {"root": root, "pos": (px, py), "facing_deg": hd_deg, "right": right, "pelvis": pelvis, "head": head_c,
            "hands": hands, "feet": feet, "height": H, "look": look, "pose": "lie"}


# ---------------------------------------------------------------- props and location

def build_prop(spec, coll, report):
    mat = _mat("PV_M_prop", GRAY_PROP)
    nm = spec["name"]
    loc = Vector(spec.get("loc", [0, 0, 0]))
    rotz = math.radians(spec.get("rot_z_deg", 0))
    size = spec.get("size", [0.1, 0.1, 0.1])
    kind = {"box": "box", "cylinder": "cyl", "sphere": "sphere"}.get(spec.get("type", "box"), "box")
    q = Matrix.Rotation(rotz, 4, 'Z').to_quaternion()
    if "tilt_deg" in spec:       # [rx, ry, rz] full rotation in degrees overrides rot_z
        r = [math.radians(a) for a in spec["tilt_deg"]]
        from mathutils import Euler
        q = Euler(r, 'XYZ').to_quaternion()
    if kind == "cyl":
        sc = (size[0] / 2, size[1] / 2, size[2])
    elif kind == "sphere":
        sc = (size[0] / 2, size[1] / 2, size[2] / 2)
    else:
        sc = tuple(size)
    ob = _obj("PV_prop_" + nm, kind, coll, mat, loc=loc, scale=sc, quat=q)
    # jaw marker so a wrench or tool shows its working end (optional)
    if spec.get("end_marker"):
        em = spec["end_marker"]                   # local offset of working end
        _obj("PV_prop_%s_end" % nm, "sphere", coll, _mat("PV_M_nose", GRAY_NOSE),
             loc=loc + q @ Vector(em), scale=(0.02, 0.02, 0.02))
    grips = {}
    for k, lp in spec.get("grips", {}).items():
        grips[k] = loc + q @ Vector(lp)
        _obj("PV_grip_%s_%s" % (nm, k), "sphere", coll, _mat("PV_M_light", YELLOW), loc=grips[k],
             scale=(0.012, 0.012, 0.012))
    grips.setdefault("center", loc)
    report["_props"][nm] = {"grips": grips, "obj": ob.name}
    return ob


def build_location(loc, coll, report):
    gm = _mat("PV_M_ground", GRAY_GROUND)
    lm = _mat("PV_M_location", GRAY_LOC)
    size = loc.get("size", [8, 8, 3])
    w, d, h = size
    cx, cy = loc.get("center", [0, 0])
    # ground slab
    _box("PV_ground", (cx, cy, -0.01), (w + 2, d + 2, 0.02), coll, gm)
    # 1 m grid lines (thin dark boxes) so scale reads in every render
    lines = _mat("PV_M_grid", GRID_LINE)
    nx, ny = int(w // 1), int(d // 1)
    for i in range(-nx // 2, nx // 2 + 1):
        _box("PV_grid_x%d" % i, (cx + i, cy, 0.001), (0.012, d, 0.002), coll, lines)
    for j in range(-ny // 2, ny // 2 + 1):
        _box("PV_grid_y%d" % j, (cx, cy + j, 0.001), (w, 0.012, 0.002), coll, lines)
    # walls: list of "walls" in the card e.g. ["back","left"] build thin slabs at the room edge
    for side in loc.get("walls", []):
        t = 0.08
        if side == "back":
            _box("PV_wall_back", (cx, cy + d / 2, h / 2), (w, t, h), coll, lm)
        elif side == "front":
            _box("PV_wall_front", (cx, cy - d / 2, h / 2), (w, t, h), coll, lm)
        elif side == "left":
            _box("PV_wall_left", (cx - w / 2, cy, h / 2), (t, d, h), coll, lm)
        elif side == "right":
            _box("PV_wall_right", (cx + w / 2, cy, h / 2), (t, d, h), coll, lm)
        elif side == "ceiling":
            _box("PV_ceiling", (cx, cy, h), (w, d, 0.06), coll, lm)
    for b in loc.get("blocks", []):
        q = Matrix.Rotation(math.radians(b.get("rot_z_deg", 0)), 4, 'Z').to_quaternion()
        c = Vector(b["loc"])
        s = b["size"]
        _box("PV_blk_" + b["name"], (c.x, c.y, c.z + s[2] / 2 if b.get("on_ground", True) else c.z), s, coll, lm, q)


def build_light_marker(light, center, coll):
    """Yellow arrow 3 m from the centre showing where light comes FROM and which way it travels."""
    az = math.radians(light.get("azimuth_deg", 45))   # compass: 0 = from +Y side, 90 = from +X side
    el = math.radians(light.get("elevation_deg", 40))
    frm = Vector((math.sin(az) * math.cos(el), math.cos(az) * math.cos(el), math.sin(el)))
    pos = Vector(center) + frm * float(light.get("marker_distance", 3.5))
    mat = _mat("PV_M_light", YELLOW)
    to = Vector(center) - pos
    q = to.normalized().to_track_quat('Z', 'Y')
    tail = pos
    tip = pos + to.normalized() * 0.9
    _between("PV_light_shaft", tail, tail + to.normalized() * 0.6, 0.03, coll, mat)
    _between("PV_light_head", tail + to.normalized() * 0.6, tip, 0.08, coll, mat, kind="cone")
    _obj("PV_light_sun", "sphere", coll, mat, loc=tail - to.normalized() * 0.15, scale=(0.12,) * 3)
    return frm


# ---------------------------------------------------------------- camera rig

def make_camera(name, coll, loc, target, lens, sensor=36.0, ortho=False, ortho_scale=10.0):
    cd = bpy.data.cameras.new("PV_camdata_" + name)
    cd.lens = lens
    cd.sensor_width = sensor
    cd.sensor_fit = 'AUTO'
    cd.clip_start, cd.clip_end = 0.05, 200
    if ortho:
        cd.type = 'ORTHO'
        cd.ortho_scale = ortho_scale
    cam = bpy.data.objects.new("PV_cam_" + name, cd)
    cam.location = loc
    coll.objects.link(cam)
    tgt = bpy.data.objects.new("PV_camtarget_" + name, None)
    tgt.empty_display_type = 'SPHERE'
    tgt.empty_display_size = 0.12
    tgt.location = target
    coll.objects.link(tgt)
    con = cam.constraints.new('TRACK_TO')
    con.target = tgt
    con.track_axis = 'TRACK_NEGATIVE_Z'
    con.up_axis = 'UP_Y'
    return cam, tgt


def orbit_pos(target, distance, azimuth_deg, height):
    """Camera position from a target: azimuth 0 = on the -Y side looking +Y, +90 = on the +X side."""
    a = math.radians(azimuth_deg)
    t = Vector(target)
    return Vector((t.x + math.sin(a) * distance, t.y - math.cos(a) * distance, height))


def setup_render(scene, w, h, engine="BLENDER_WORKBENCH", light_from=None):
    scene.render.engine = engine
    scene.render.resolution_x, scene.render.resolution_y = w, h
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.film_transparent = False
    sh = scene.display.shading
    sh.light = 'STUDIO'
    sh.color_type = 'OBJECT'      # use object color so shared meshes keep their own colours
    sh.show_shadows = True
    sh.shadow_intensity = 0.35
    sh.show_cavity = False
    if hasattr(scene.display, "render_aa"):
        scene.display.render_aa = '8'
    if light_from is not None:
        # the shadow direction vector points the way the light travels
        scene.display.light_direction = (-light_from).normalized()
    w_ = scene.world or bpy.data.worlds.new("PV_world")
    scene.world = w_
    w_.color = (0.86, 0.88, 0.9)
    scene.view_settings.view_transform = 'Standard'
    scene.display_settings.display_device = 'sRGB'
