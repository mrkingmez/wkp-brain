"""audit_asset.py - read-only quality audit for Blender mesh objects (verified on Blender 5.2.4).

Run inside Blender (execute_blender_code or Text editor). Never modifies anything.
In execute_blender_code:
    import runpy
    ns = runpy.run_path(r"D:\WKP\.claude\skills\blender-asset-quality\scripts\audit_asset.py")
    ns["audit"](["SM_Crate"], kind="prop")      # list of object names
    ns["audit"](None)                           # all selected mesh objects
From a shell (headless):  blender -b file.blend --python audit_asset.py -- SM_Crate
Returns a list of dicts and prints a PASS/WARN/FAIL block per object.
kind picks the triangle budget: prop, hero_prop, character_game, character_hero,
environment_piece, background.
"""
import bpy, bmesh, math, sys

BUDGET = {"prop": 5000, "hero_prop": 30000, "character_game": 60000,
          "character_hero": 150000, "environment_piece": 20000, "background": 1500}
EPS = 1e-4


def _bm_stats(obj, use_evaluated):
    """Stats from the evaluated mesh (modifiers included) or the base mesh."""
    ev = None
    if use_evaluated:
        dg = bpy.context.evaluated_depsgraph_get()
        ev = obj.evaluated_get(dg)
        me = ev.to_mesh()
    else:
        me = obj.data
    bm = bmesh.new()
    bm.from_mesh(me)
    bm.verts.ensure_lookup_table(); bm.edges.ensure_lookup_table(); bm.faces.ensure_lookup_table()
    tris = sum(len(f.verts) - 2 for f in bm.faces)
    quads = sum(1 for f in bm.faces if len(f.verts) == 4)
    ngons = sum(1 for f in bm.faces if len(f.verts) > 4)
    non_manifold = sum(1 for e in bm.edges if not e.is_manifold)   # boundary, >2 faces, wire
    boundary = sum(1 for e in bm.edges if e.is_boundary)
    wire = sum(1 for e in bm.edges if e.is_wire)
    loose_v = sum(1 for v in bm.verts if not v.link_edges)
    zero_area = sum(1 for f in bm.faces if f.calc_area() < 1e-10)
    seen, dup = set(), 0
    for v in bm.verts:
        k = (round(v.co.x, 5), round(v.co.y, 5), round(v.co.z, 5))
        if k in seen:
            dup += 1
        else:
            seen.add(k)
    visited, islands = set(), 0
    for f in bm.faces:
        if f.index in visited:
            continue
        islands += 1
        stack = [f]
        while stack:
            cur = stack.pop()
            if cur.index in visited:
                continue
            visited.add(cur.index)
            for e in cur.edges:
                for nf in e.link_faces:
                    if nf.index not in visited:
                        stack.append(nf)
    out = dict(verts=len(bm.verts), faces=len(bm.faces), tris=tris, quads=quads, ngons=ngons,
               non_manifold_edges=non_manifold, boundary_edges=boundary, loose_verts=loose_v,
               loose_edges=wire, zero_area_faces=zero_area, duplicate_verts=dup, islands=islands)
    if non_manifold == 0 and len(bm.faces) > 0:
        vol = 0.0
        for f in bm.faces:
            vs = [v.co for v in f.verts]
            for i in range(1, len(vs) - 1):
                vol += vs[0].dot(vs[i].cross(vs[i + 1])) / 6.0
        out["signed_volume"] = round(vol, 6)   # negative on a closed mesh = inside-out normals
    bm.free()
    if ev is not None:
        ev.to_mesh_clear()
    return out


def _uv_stats(obj):
    me = obj.data
    res = dict(uv_layers=[l.name for l in me.uv_layers], uv_out_of_0_1=0)
    if not me.uv_layers:
        return res
    out = 0
    for d in me.uv_layers.active.data:
        u, v = d.uv
        if u < -EPS or u > 1 + EPS or v < -EPS or v > 1 + EPS:
            out += 1
    res["uv_out_of_0_1"] = out
    bm = bmesh.new()
    bm.from_mesh(me)
    uvl = bm.loops.layers.uv.active
    ratios, uv_total = [], 0.0
    for f in bm.faces:
        a3 = f.calc_area()
        if a3 < 1e-10:
            continue
        pts = [l[uvl].uv for l in f.loops]
        a2 = 0.0
        for i in range(1, len(pts) - 1):
            a2 += abs((pts[i] - pts[0]).cross(pts[i + 1] - pts[0])) / 2.0
        uv_total += a2
        ratios.append(math.sqrt(a2 / a3))
    bm.free()
    if ratios:
        mn, mx = min(ratios), max(ratios)
        res["uv_area_used"] = round(uv_total, 3)   # >1.0 means overlap (or tiling)
        res["texel_density_spread"] = round(mx / mn, 2) if mn > 0 else float("inf")  # target < 2
    return res


def audit(names=None, kind="prop", use_evaluated=True, expected_prefix=None):
    if names is None:
        objs = [o for o in bpy.context.selected_objects if o.type == "MESH"]
    else:
        objs = [bpy.data.objects[n] for n in names]
    results = []
    for o in objs:
        if o.type != "MESH":
            print(f"SKIP {o.name} ({o.type})")
            continue
        r = dict(name=o.name)
        r["dimensions_m"] = tuple(round(x, 4) for x in o.dimensions)
        r["scale"] = tuple(round(x, 4) for x in o.scale)
        r["unapplied_scale"] = any(abs(s - 1) > EPS for s in o.scale)
        r["unapplied_rotation"] = o.rotation_mode != "QUATERNION" and any(abs(a) > EPS for a in o.rotation_euler)
        r["negative_scale"] = any(s < 0 for s in o.scale)
        r["origin_world"] = tuple(round(x, 4) for x in o.matrix_world.translation)
        r["modifiers"] = [(m.name, m.type) for m in o.modifiers]
        r["shape_keys"] = bool(o.data.shape_keys)
        r["vertex_groups"] = len(o.vertex_groups)
        slots = o.material_slots
        r["material_slots"] = len(slots)
        r["empty_slots"] = sum(1 for s in slots if s.material is None)
        used = set(p.material_index for p in o.data.polygons)
        r["unused_slots"] = sum(1 for i in range(len(slots)) if i not in used)
        r["data_users"] = o.data.users
        r.update(_bm_stats(o, use_evaluated))
        r.update(_uv_stats(o))
        r["has_uv"] = bool(r["uv_layers"])
        issues = []
        for s in slots:
            if s.material and s.material.node_tree:
                for n in s.material.node_tree.nodes:
                    if n.type == "TEX_IMAGE":
                        if n.image is None:
                            issues.append(f"{s.material.name}:empty_image_node")
                        else:
                            w, h = n.image.size
                            if w == 0:
                                issues.append(f"{n.image.name}:no_pixels_or_missing_file")
                            elif (w & (w - 1)) or (h & (h - 1)):
                                issues.append(f"{n.image.name}:not_power_of_two {w}x{h}")
        r["texture_issues"] = issues
        fails, warns = [], []
        if r["unapplied_scale"]: fails.append("scale is not 1,1,1 (apply scale)")
        if r["unapplied_rotation"] and not o.parent: warns.append("non-zero rotation (apply if not intentional)")
        if r["negative_scale"]: fails.append("negative scale")
        if r["ngons"]: warns.append(f"{r['ngons']} n-gons")
        if r["non_manifold_edges"]: warns.append(f"{r['non_manifold_edges']} non-manifold edges (fine only for intentional open shells such as cloth or hair cards)")
        if r["loose_verts"] or r["loose_edges"]: fails.append("loose geometry")
        if r["zero_area_faces"]: fails.append("zero-area faces")
        if r["duplicate_verts"]: warns.append(f"{r['duplicate_verts']} duplicate verts (merge by distance)")
        if not r["has_uv"]: fails.append("no UV map")
        if r.get("uv_area_used", 0) > 1.05: warns.append("UV area over 1.0: overlap (ok only for mirrored or tiling)")
        if r["uv_out_of_0_1"]: warns.append(f"{r['uv_out_of_0_1']} UV corners outside 0-1 (ok for tiling or UDIM)")
        if r.get("texel_density_spread", 1) > 2.5: warns.append(f"texel density spread {r['texel_density_spread']} (target under 2)")
        if r["empty_slots"]: fails.append("empty material slot")
        if r["unused_slots"]: warns.append("unused material slot(s)")
        if issues: warns.append("texture issues: " + "; ".join(issues))
        if r.get("signed_volume", 1) < 0: fails.append("closed mesh is inside-out (recalculate normals)")
        lim = BUDGET.get(kind)
        if lim and r["tris"] > lim: fails.append(f"{r['tris']} tris is over the {kind} budget {lim}")
        if max(o.dimensions) < 0.001 or max(o.dimensions) > 1000: warns.append("size looks wrong for metres")
        if expected_prefix and not o.name.startswith(expected_prefix): warns.append(f"name does not start with {expected_prefix}")
        tail = o.name.rsplit(".", 1)[-1]
        if "." in o.name and tail.isdigit(): warns.append("name has a .001 style suffix")
        r["FAIL"], r["WARN"] = fails, warns
        r["verdict"] = "FAIL" if fails else ("WARN" if warns else "PASS")
        results.append(r)
        print(f"[{r['verdict']}] {o.name} dims={r['dimensions_m']} tris={r['tris']} quads={r['quads']} ngons={r['ngons']} "
              f"nonmanifold={r['non_manifold_edges']} loose={r['loose_verts']}/{r['loose_edges']} uv={r['uv_layers']} "
              f"slots={r['material_slots']} scale={r['scale']} mods={[m[1] for m in r['modifiers']]}")
        for x in fails: print("   FAIL:", x)
        for x in warns: print("   WARN:", x)
    us = bpy.context.scene.unit_settings
    print(f"SCENE units: system={us.system} scale_length={us.scale_length}"
          + ("  <-- should be METRIC and 1.0" if us.system != "METRIC" or abs(us.scale_length - 1) > 1e-6 else ""))
    orph = {k: sum(1 for x in getattr(bpy.data, k) if x.users == 0) for k in ("meshes", "materials", "images")}
    print("ORPHANS (0 users):", orph)
    return results


if "--" in sys.argv:
    _argv = sys.argv[sys.argv.index("--") + 1:]
    if _argv:
        audit(_argv)
