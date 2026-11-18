"""Regenerates the WKP org chart (HTML, PNG, DOCX) from D:\\WKP\\data\\org-chart-data.json.
Run: python D:\\WKP\\data\\build_org_chart.py
PNG uses headless Microsoft Edge to render the same SVG the HTML page shows.
"""
import json, math, os, subprocess, sys, html, textwrap

DATA = r"D:\WKP\data\org-chart-data.json"
OUT = r"D:\WKP Reports\Org Chart"
STAMP = "2026-11-17"
BASE = f"{STAMP} - WKP Org Chart"
HTML_PATH = os.path.join(OUT, BASE + ".html")
PNG_PATH = os.path.join(OUT, BASE + ".png")
DOCX_PATH = os.path.join(OUT, BASE + ".docx")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

d = json.load(open(DATA, encoding="utf-8"))
AGENTS = {a["id"]: a for a in d["agents"]}
GROUPS = d["skill_groups"]
W = 5000
AW, AH, AGP, PAD, HDR = 370, 100, 25, 30, 78
BGAP = 55
X0 = 160
e = html.escape


def est(text, size):
    return len(text) * size * 0.56


def txt(x, y, s, size, cls="", anchor="start", avail=None, extra=""):
    ex = ""
    if avail and est(s, size) > avail:
        ex = f' textLength="{avail:.0f}" lengthAdjust="spacingAndGlyphs"'
    return f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" class="{cls}" text-anchor="{anchor}"{ex} {extra}>{e(s)}</text>'


def wrap(s, n):
    return textwrap.wrap(s, n) or [""]


# ---------------------------------------------------------------- block layout
def block_items(dept):
    """Return (items, height). items are dicts with relative positions inside the block."""
    cols = dept["cols"]
    inner = cols * AW + (cols - 1) * AGP
    items = []
    y = HDR + 15
    items.append(dict(t="boss", id=dept["boss"], x=PAD, y=y, w=inner, h=AH))
    boss_bottom = y + AH
    y += AH + AGP
    last_mid = boss_bottom
    for sec in dept["sections"]:
        if "note" in sec:
            items.append(dict(t="note", s=sec["note"], x=PAD, y=y + 18))
            y += 50
            continue
        y0 = y
        if sec.get("frame"):
            y += 46
        ag = sec.get("agents", [])
        rows = math.ceil(len(ag) / cols) if ag else 0
        for i, aid in enumerate(ag):
            r, c = divmod(i, cols)
            items.append(dict(t="agent", id=aid, x=PAD + c * (AW + AGP), y=y + r * (AH + AGP), w=AW, h=AH))
            last_mid = y + r * (AH + AGP) + AH / 2
        y += rows * (AH + AGP)
        if sec.get("ref"):
            ref = sec["ref"]
            items.append(dict(t="ref", id=ref["id"], note=ref["note"], x=PAD, y=y, w=inner, h=AH))
            last_mid = y + AH / 2
            y += AH + AGP
        if sec.get("frame"):
            items.append(dict(t="frame", label=sec["frame"], x=PAD - 14, y=y0, w=inner + 28, h=y - y0 - AGP + 12))
            y += 10
    height = y - AGP + PAD
    return items, height, inner, boss_bottom, last_mid


def build():
    svg = []
    defs_css = ""
    pos = {}      # agent id -> (x,y,w,h) absolute
    blocks = {}   # dept id -> (x,y,w,h)
    shapes = []   # block drawings
    lines_back = []
    ticks = []

    # ---- row B
    rowB = [x for x in d["departments"] if x["row"] == "B"]
    rowC1 = [x for x in d["departments"] if x["row"] == "C1"]
    rowC2 = [x for x in d["departments"] if x["row"] == "C2"]
    lay = {x["id"]: block_items(x) for x in d["departments"]}

    def row_dims(row):
        return max(lay[x["id"]][1] for x in row)

    hB, hC1, hC2 = row_dims(rowB), row_dims(rowC1), row_dims(rowC2)
    ZAC_Y, JAR_Y = 30, 215
    BUS1 = 440
    B_TOP = 500
    B_BOT = B_TOP + hB
    SH1_TOP = B_BOT + 210
    # group heights
    def lines_of(g):
        return [s for s in d["skills"] if s["group"] == g]
    GW = 460
    LH = 29
    sh1_groups = ["etsy", "wwd", "channel", "fiction", "fantasy", "trading", "jarvis"]
    sh2_groups = ["writing", "design", "anim"]
    gh1 = max(70 + len(lines_of(g)) * LH + 24 for g in sh1_groups)
    gh2 = max(70 + len(lines_of(g)) * LH + 24 for g in sh2_groups)
    SH1_H = 66 + gh1 + 20
    SH2_TOP = SH1_TOP + SH1_H + 40
    SH2_H = 66 + gh2 + 20
    BUS2 = SH2_TOP + SH2_H + 85
    C1_TOP = SH2_TOP + SH2_H + 190
    C1_BOT = C1_TOP + hC1
    BUS3 = C1_BOT + 75
    C2_TOP = C1_BOT + 150
    C2_BOT = C2_TOP + hC2
    BUS4 = C2_BOT + 75
    D_TOP = C2_BOT + 150

    def place_row(row, top, rowh):
        x = X0
        for dep in row:
            items, h, inner, bb, lm = lay[dep["id"]]
            w = inner + 2 * PAD
            blocks[dep["id"]] = (x, top, w, rowh)
            for it in items:
                if it["t"] in ("boss", "agent", "ref"):
                    if it["t"] != "ref":
                        pos[it["id"]] = (x + it["x"], top + it["y"], it["w"], it["h"])
            x += w + BGAP

    place_row(rowB, B_TOP, hB)
    place_row(rowC1, C1_TOP, hC1)
    place_row(rowC2, C2_TOP, hC2)

    # ---- draw blocks
    def draw_block(dep, row_kind):
        bx, by, bw, bh = blocks[dep["id"]]
        items, h, inner, bb, lm = lay[dep["id"]]
        cls = "blk venture" if dep["kind"] == "venture" else "blk shared"
        g = [f'<g class="dept" data-dept="{dep["id"]}">']
        g.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="22" class="{cls}"/>')
        g.append(txt(bx + PAD, by + 50, dep["name"], 25, "btitle", avail=bw - 2 * PAD))
        # trunk
        cx = bx + PAD + inner / 2
        if dep["sections"]:
            g.append(f'<line x1="{cx}" y1="{by + bb}" x2="{cx}" y2="{by + lm}" class="trunk"/>')
        for it in items:
            if it["t"] == "frame":
                g.append(f'<rect x="{bx + it["x"]}" y="{by + it["y"]}" width="{it["w"]}" height="{it["h"]}" rx="14" class="frame"/>')
                g.append(txt(bx + it["x"] + 14, by + it["y"] + 31, it["label"], 20, "flabel"))
            elif it["t"] == "note":
                g.append(txt(bx + it["x"], by + it["y"] + 8, it["s"], 17, "note", avail=inner))
        for it in items:
            if it["t"] in ("boss", "agent"):
                g.append(agent_box(it["id"], bx + it["x"], by + it["y"], it["w"], it["h"], it["t"] == "boss"))
            elif it["t"] == "ref":
                g.append(ref_box(it["id"], it["note"], bx + it["x"], by + it["y"], it["w"], it["h"]))
        g.append("</g>")
        return "".join(g)

    def agent_box(aid, x, y, w, h, boss=False):
        a = AGENTS[aid]
        st = a["status"]
        cls = "ag" + (" boss" if boss else "") + (" planned" if st == "planned" else "") + (" builtin" if st == "builtin" else "")
        s = [f'<g class="{cls}" data-id="{aid}" tabindex="0">']
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="abox"/>')
        s.append(txt(x + 14, y + 40, aid, 21, "aname", avail=w - 28 - (90 if st == "planned" else 0)))
        s.append(txt(x + 14, y + 74, a["job"], 18, "ajob", avail=w - 28))
        if st == "planned":
            s.append(f'<rect x="{x + w - 92}" y="{y + 8}" width="82" height="22" rx="6" class="ptag"/>' + txt(x + w - 51, y + 24, "PLANNED", 14, "ptagt", "middle"))
        if st == "builtin":
            s.append(txt(x + w - 12, y + 24, "built-in", 14, "ptagt2", "end"))
        s.append(f'<title>{e(aid)}: {e(a["desc"])}</title></g>')
        return "".join(s)

    def ref_box(aid, note, x, y, w, h):
        a = AGENTS[aid]
        s = [f'<g class="ag ref" data-id="{aid}" tabindex="0">']
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" class="abox refbox"/>')
        s.append(txt(x + 14, y + 38, f"{aid} (link)", 21, "aname", avail=w - 28))
        s.append(txt(x + 14, y + 72, note, 17, "ajob", avail=w - 28))
        s.append(f'<title>{e(aid)} lives in Marketing: {e(a["desc"])}</title></g>')
        return "".join(s)

    for dep in rowB + rowC1 + rowC2:
        shapes.append(draw_block(dep, dep["row"]))

    # ---- reporting lines
    rl = []
    jar_cx = 2500
    rl.append(f'<line x1="{jar_cx}" y1="{JAR_Y + 130}" x2="{jar_cx}" y2="{BUS1}" class="rep"/>')
    bx_list = [blocks[x["id"]][0] + blocks[x["id"]][2] / 2 for x in rowB]
    rl.append(f'<line x1="60" y1="{BUS1}" x2="{max(bx_list)}" y2="{BUS1}" class="rep"/>')
    rl.append(f'<line x1="60" y1="{BUS1}" x2="60" y2="{BUS4}" class="rep"/>')
    for dep in rowB:
        x, y, w, h = blocks[dep["id"]]
        rl.append(f'<line x1="{x + w / 2}" y1="{BUS1}" x2="{x + w / 2}" y2="{y}" class="rep"/>')

    def bus(y, row, tops):
        xs = [blocks[x["id"]][0] + blocks[x["id"]][2] / 2 for x in row]
        rl.append(f'<line x1="60" y1="{y}" x2="{max(xs)}" y2="{y}" class="rep"/>')
        for dep in row:
            x, yy, w, h = blocks[dep["id"]]
            rl.append(f'<line x1="{x + w / 2}" y1="{y}" x2="{x + w / 2}" y2="{tops}" class="rep"/>')
    bus(BUS2, rowC1, C1_TOP)
    bus(BUS3, rowC2, C2_TOP)

    # ---- library
    lib = []
    gx = {}
    def desired_center(g):
        tgt = GROUPS[g]["targets"][0]
        for dep in d["departments"]:
            if dep.get("boss") == tgt:
                x, y, w, h = blocks[dep["id"]]
                return x + w / 2
        return 0
    prev_end = X0 - 20
    for g in sh1_groups[:-1]:
        cx = desired_center(g)
        x = max(cx - GW / 2, prev_end + 20, X0)
        gx[g] = x
        prev_end = x + GW
    gx["jarvis"] = 3900
    # shelf 2: writing centered between its two targets
    def mid(ids):
        cs = []
        for t in ids:
            for dep in d["departments"]:
                if dep.get("boss") == t:
                    x, y, w, h = blocks[dep["id"]]
                    cs.append(x + w / 2)
        return sum(cs) / len(cs)
    prev_end = X0 - 20
    for g in sh2_groups:
        cx = mid(GROUPS[g]["targets"]) if g != "writing" else mid(["script-room", "marketing-director"])
        x = max(cx - GW / 2, prev_end + 20, X0)
        gx[g] = x
        prev_end = x + GW
    # bands
    lib.append(f'<g class="lib"><rect x="{X0 - 40}" y="{SH1_TOP}" width="{W - 2 * (X0 - 40)}" height="{SH1_H}" rx="22" class="blk support"/>')
    lib.append(txt(X0 - 10, SH1_TOP + 46, "LIBRARY DEPARTMENT, shelf 1 of 2: venture and Jarvis skills (colored line = who uses the skill group)", 25, "btitle"))
    lib.append(f'<rect x="{X0 - 40}" y="{SH2_TOP}" width="{W - 2 * (X0 - 40)}" height="{SH2_H}" rx="22" class="blk support"/>')
    lib.append(txt(X0 - 10, SH2_TOP + 46, "LIBRARY DEPARTMENT, shelf 2 of 2: shared department skills   ( * = account skill, not in the repo )", 25, "btitle"))
    lib.append(f'<line x1="60" y1="{SH1_TOP + SH1_H / 2}" x2="{X0 - 40}" y2="{SH1_TOP + SH1_H / 2}" class="rep"/>')
    lib.append(f'<line x1="60" y1="{SH2_TOP + SH2_H / 2}" x2="{X0 - 40}" y2="{SH2_TOP + SH2_H / 2}" class="rep"/>')
    skill_lines = []
    chips = {}
    for g in sh1_groups + sh2_groups:
        top = SH1_TOP + 66 if g in sh1_groups else SH2_TOP + 66
        hgt = gh1 if g in sh1_groups else gh2
        x = gx[g]
        col = GROUPS[g]["color"] if g != "jarvis" else "var(--jc)"
        sk = lines_of(g)
        lib.append(f'<g class="gbox" data-g="{g}" tabindex="0"><rect x="{x}" y="{top}" width="{GW}" height="{hgt}" rx="14" class="gb"/>'
                   f'<rect x="{x}" y="{top}" width="14" height="{hgt}" rx="6" style="fill:{col}"/>')
        lib.append(txt(x + 30, top + 36, GROUPS[g]["name"], 22, "gtitle", avail=GW - 44))
        for i, s_ in enumerate(sk):
            nm = s_["name"] + (" *" if s_["source"].startswith("account") else "") + (" (retired)" if "RETIRED" in s_["note"] else "") + (" (empty)" if "holds no SKILL" in s_["note"] else "")
            lib.append(txt(x + 30, top + 68 + i * LH, nm, 18, "sk", avail=GW - 44))
        lib.append("</g>")
        # lines
        cx = x + GW / 2
        for k, t in enumerate(GROUPS[g]["targets"]):
            if g == "jarvis":
                # up the right margin to Jarvis
                y1 = top + hgt / 2
                path = f"M {x + GW} {y1} L 4880 {y1} L 4880 395 L 2900 395 L 2900 {JAR_Y + 70} L 2800 {JAR_Y + 70}"
                skill_lines.append(f'<path d="{path}" class="sl" data-g="{g}" style="stroke:{col}"/>')
                continue
            tdep = [dd for dd in d["departments"] if dd.get("boss") == t][0]
            bx_, by_, bw_, bh_ = blocks[tdep["id"]]
            if g in sh1_groups:
                y0, y1 = top, by_ + bh_
                x1 = bx_ + bw_ / 2
            else:
                y0, y1 = top + hgt, by_
                x1 = bx_ + bw_ / 2 + 70
            x0 = cx + (k - (len(GROUPS[g]["targets"]) - 1) / 2) * 60
            ym = (y0 + y1) / 2
            skill_lines.append(f'<path d="M {x0:.0f} {y0} C {x0:.0f} {ym} {x1:.0f} {ym} {x1:.0f} {y1}" class="sl" data-g="{g}" style="stroke:{col}"/>')
            chips.setdefault(t, []).append(g)
    lib.append("</g>")

    # chips on boss boxes
    chip_svg = []
    for t, gl in chips.items():
        x, y, w, h = pos[t]
        for k, g in enumerate(gl):
            chip_svg.append(f'<circle cx="{x + w - 20 - 26 * k}" cy="{y + 20}" r="10" class="chip" data-g="{g}" style="fill:{GROUPS[g]["color"]}"/>')
    # Jarvis chip handled with box

    # ---- top: Zac, Jarvis
    top = []
    top.append(f'<g class="ag zac" data-id="zac"><rect x="2240" y="{ZAC_Y}" width="520" height="80" rx="14" class="zacbox"/>'
               + txt(2500, ZAC_Y + 36, "ZAC (owner)", 26, "zname", "middle") + txt(2500, ZAC_Y + 64, "decides money and public posting", 18, "zjob", "middle") + '<title>Zac: owner. Decides anything that spends money or posts publicly.</title></g>')
    top.append(f'<line x1="2500" y1="{ZAC_Y + 80}" x2="2500" y2="{JAR_Y}" class="rep"/>')
    top.append(f'<g class="ag jarv" data-id="jarvis" tabindex="0"><rect x="2200" y="{JAR_Y}" width="600" height="130" rx="16" class="jbox"/>'
               + txt(2500, JAR_Y + 54, "JARVIS", 38, "jname", "middle") + txt(2500, JAR_Y + 92, "CEO and general: plans, routes, reviews", 22, "jjob", "middle")
               + '<circle cx="2770" cy="' + str(JAR_Y + 22) + '" r="11" class="chip" style="fill:var(--jc);stroke:#fff;stroke-width:2"/><title>Jarvis: main session, the CEO</title></g>')
    top.append(f'<g class="ag builtin" data-id="claude-code-guide" tabindex="0"><rect x="1250" y="{JAR_Y + 15}" width="400" height="100" rx="12" class="abox builtin"/>'
               + txt(1264, JAR_Y + 55, "claude-code-guide", 21, "aname") + txt(1264, JAR_Y + 89, "Looks up Claude Code answers", 18, "ajob", avail=372)
               + txt(1638, JAR_Y + 38, "built-in", 14, "ptagt2", "end") + '<title>claude-code-guide: Jarvis research assistant (built-in helper, no repo spec)</title></g>')
    top.append(f'<path d="M 1450 {JAR_Y + 115} L 1450 {JAR_Y + 123} L 2200 {JAR_Y + 123}" class="dot"/>')
    top.append(f'<g class="ag" data-id="chief-of-staff" tabindex="0"><rect x="1700" y="{JAR_Y + 15}" width="400" height="100" rx="12" class="abox"/>'
               + txt(1714, JAR_Y + 55, "chief-of-staff", 21, "aname") + txt(1714, JAR_Y + 89, "Jarvis assistant: tasks, queue, briefs", 18, "ajob", avail=372)
               + '<title>chief-of-staff: standing assistant to Jarvis (live agent)</title></g>')
    top.append(f'<line x1="2100" y1="{JAR_Y + 65}" x2="2200" y2="{JAR_Y + 65}" class="rep"/>')

    # legend
    leg = [f'<g class="legend"><rect x="3300" y="18" width="1500" height="172" rx="14" class="blk support"/>']
    leg.append(txt(3320, 46, "COLOR LEGEND  (click a color to isolate its lines)", 20, "btitle"))
    gl = list(GROUPS.keys())
    for i, g in enumerate(gl):
        col = GROUPS[g]["color"] if g != "jarvis" else "var(--jc)"
        cx_ = 3320 + (i // 5) * 740
        cy_ = 74 + (i % 5) * 22
        leg.append(f'<g class="lg" data-g="{g}"><line x1="{cx_}" y1="{cy_ - 6}" x2="{cx_ + 60}" y2="{cy_ - 6}" style="stroke:{col};stroke-width:8;stroke-linecap:round"/>'
                   + txt(cx_ + 76, cy_, GROUPS[g]["name"], 18, "lgt") + '</g>')
    leg.append("</g>")
    leg.append(f'<g class="legend2"><rect x="{X0}" y="125" width="2600" height="62" rx="12" class="blk support"/>'
               f'<line x1="{X0 + 20}" y1="156" x2="{X0 + 90}" y2="156" class="rep"/>' + txt(X0 + 104, 163, "reports to", 18, "lgt")
               + f'<rect x="{X0 + 260}" y="138" width="70" height="36" rx="7" class="abox"/>' + txt(X0 + 345, 163, "live agent (spec file on disk)", 18, "lgt")
               + f'<rect x="{X0 + 580}" y="138" width="70" height="36" rx="7" class="abox planned" style="stroke-dasharray:8 5"/>' + txt(X0 + 665, 163, "planned (no spec file)", 18, "lgt")
               + f'<rect x="{X0 + 910}" y="138" width="70" height="36" rx="7" class="abox builtin"/>' + txt(X0 + 995, 163, "built-in helper", 18, "lgt")
               + f'<rect x="{X0 + 1200}" y="138" width="70" height="36" rx="7" class="abox boss"/>' + txt(X0 + 1285, 163, "director or boss", 18, "lgt")
               + f'<circle cx="{X0 + 1520}" cy="156" r="10" style="fill:#D55E00"/>' + txt(X0 + 1540, 163, "dot = skill group line lands here", 18, "lgt") + "</g>")
    title = [txt(X0, 62, "WARRIOR KING PRODUCTIONS: ORGANIZATION CHART", 44, "title"),
             txt(X0, 100, f"As of {d['generated']}. Zac, Jarvis, directors, benches. Library, Reference and Shipping departments below.", 22, "subtitle")]

    # ---- Row D: reference + shipping
    ref = []
    conns = d["connectors"]
    cols = 6
    BW, BH, BG = 440, 200, 20
    rw = cols * BW + (cols - 1) * BG + 2 * PAD
    nrows = math.ceil(len(conns) / cols)
    tools_lines = wrap("LOCAL TOOLS (verified by running each one): " + "; ".join(t["name"] + " at " + t["where"] for t in d.get("tools", [])) + ".", 205)
    na_lines = wrap("AVAILABLE, NOT CONNECTED (installed, no authorization): " + ", ".join(d["not_authorized"]) + ".   OTHER (not WKP relevant): " + "; ".join(d["other_connectors"]) + ".", 205)
    ref_h = HDR + 10 + nrows * (BH + BG) + 30 + (len(tools_lines) + len(na_lines)) * 26 + 70
    ref.append(f'<g class="dept"><rect x="{X0}" y="{D_TOP}" width="{rw}" height="{ref_h}" rx="22" class="blk support"/>')
    ref.append(txt(X0 + PAD, D_TOP + 50, "REFERENCE DEPARTMENT: CONNECTORS (MCP servers and external accounts) and who uses them", 25, "btitle", avail=rw - 2 * PAD))
    for i, cn in enumerate(conns):
        r, c = divmod(i, cols)
        x = X0 + PAD + c * (BW + BG)
        y = D_TOP + HDR + r * (BH + BG)
        ok = cn["status"] == "connected"
        na = "not authorized" in cn["status"]
        scls = "cok" if ok else ("cna" if na else "cweb")
        ref.append(f'<g class="cn" data-cn="{i}" tabindex="0"><rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="12" class="abox {"" if ok else "dashed"}"/>')
        ref.append(txt(x + 14, y + 38, cn["name"], 22, "aname", avail=BW - 28))
        ref.append(txt(x + 14, y + 66, cn["status"], 17, scls, avail=BW - 28))
        for j, ln in enumerate(wrap("Used by: " + cn["used_by"], 48)[:4]):
            ref.append(txt(x + 14, y + 98 + j * 24, ln, 17, "ajob"))
        ref.append(f'<title>{e(cn["name"])} ({e(cn["status"])}). Used by: {e(cn["used_by"])}. Basis: {e(cn["basis"])}. {e(cn["note"])}</title></g>')
    ny = D_TOP + HDR + nrows * (BH + BG) + 8
    for j, ln in enumerate(tools_lines):
        ref.append(txt(X0 + PAD, ny + 20 + j * 26, ln, 18, "aname"))
    ny += len(tools_lines) * 26 + 20
    for j, ln in enumerate(na_lines):
        ref.append(txt(X0 + PAD, ny + 20 + j * 26, ln, 18, "note"))
    ref.append("</g>")
    # shipping
    sx = X0 + rw + 70
    sw = W - 120 - sx
    ship = []
    sb = d["shipping"]
    sbw = (sw - 2 * PAD - AGP) / 2
    ship_h = max(ref_h, HDR + 15 + 4 * (95 + AGP) + 150)
    ship.append(f'<g class="dept"><rect x="{sx}" y="{D_TOP}" width="{sw}" height="{ship_h}" rx="22" class="blk support"/>')
    ship.append(txt(sx + PAD, D_TOP + 50, "SHIPPING DEPARTMENT: how product leaves the company", 25, "btitle", avail=sw - 2 * PAD))
    for i, it in enumerate(sb):
        r, c = divmod(i, 2)
        later = it["status"] == "later"
        span = later
        x = sx + PAD + (0 if span else c * (sbw + AGP))
        w_ = (sw - 2 * PAD) if span else sbw
        y = D_TOP + HDR + 15 + (3 if later else r) * (95 + AGP)
        cls = "abox later" if later else "abox"
        ship.append(f'<g class="ag" data-id="{it["id"]}"><rect x="{x}" y="{y}" width="{w_}" height="95" rx="12" class="{cls}"/>'
                    + txt(x + 14, y + 38, it["name"], 22, "aname" + (" later" if later else ""), avail=w_ - 28)
                    + txt(x + 14, y + 72, it["job"], 18, "ajob" + (" later" if later else ""), avail=w_ - 28)
                    + f'<title>{e(it["name"])}: {e(it["job"])}</title></g>')
    ry = D_TOP + HDR + 15 + 4 * (95 + AGP) + 10
    for j, ln in enumerate(["Gate before anything ships:", "department boss approves, qa-director PASS,", "Jarvis reviews, then Zac.", "Zac posts. Agents never post.", "Physical products: far future, greyed out."]):
        ship.append(txt(sx + PAD, ry + j * 27, ln, 19, "note" if j != 3 else "aname"))
    ship.append("</g>")
    ship_stub = [f'<line x1="60" y1="{BUS4}" x2="{X0 + rw / 2}" y2="{BUS4}" class="rep"/>',
                 f'<line x1="{X0 + rw / 2}" y1="{BUS4}" x2="{X0 + rw / 2}" y2="{D_TOP}" class="rep"/>',
                 f'<line x1="{X0 + rw / 2}" y1="{BUS4}" x2="{sx + sw / 2}" y2="{BUS4}" class="rep"/>',
                 f'<line x1="{sx + sw / 2}" y1="{BUS4}" x2="{sx + sw / 2}" y2="{D_TOP}" class="rep"/>']
    # ---- routing lines (service departments to the directors that must use them)
    routes_svg = []
    route_dots = []
    offs = {}
    dep_of_boss = {dd["boss"]: dd["id"] for dd in d["departments"]}
    for rt in d.get("routes", []):
        sx0, sy0, sw0, sh0 = pos[rt["id"]]
        n = len(rt["to"])
        for k, tgt in enumerate(rt["to"]):
            bx_, by_, bw_, bh_ = blocks[dep_of_boss[tgt]]
            c = offs.get(tgt, 0)
            offs[tgt] = c + 1
            x1 = bx_ + 40 + (c * 21) % max(60, bw_ - 80)
            y1 = by_ + bh_
            x0 = sx0 + sw0 * 0.42 + k * (sw0 * 0.52 / max(1, n - 1)) if n > 1 else sx0 + sw0 / 2
            y0 = sy0 + 4
            ym = (y0 + y1) / 2
            pth = f"M {x0:.0f} {y0:.0f} C {x0:.0f} {ym:.0f} {x1:.0f} {ym:.0f} {x1:.0f} {y1:.0f}"
            ttl = f"<title>{e(rt['id'])} to {e(tgt)}: {e(rt['what'])}</title>"
            routes_svg.append(f'<g class="rt" data-g="r-{rt["id"]}"><path d="{pth}" class="rth"/><path d="{pth}" class="rtl" style="stroke:{rt["color"]}"/>{ttl}</g>')
            route_dots.append(f'<g class="rt" data-g="r-{rt["id"]}"><circle cx="{x1:.0f}" cy="{y1}" r="9" style="fill:{rt["color"]};stroke:var(--bg);stroke-width:3"/><circle cx="{x0:.0f}" cy="{y0:.0f}" r="7" style="fill:{rt["color"]};stroke:var(--bg);stroke-width:3"/>{ttl}</g>')
    # routes legend (top, under the color legend)
    rleg = [f'<g class="legend3"><rect x="3300" y="200" width="1500" height="{50 + 28 * len(d.get("routes", []))}" rx="14" class="blk support"/>']
    rleg.append(txt(3320, 228, "SERVICE ROUTING LINES  (dashed, from the service desk up to who must use it; click to isolate)", 20, "btitle"))
    for i, rt in enumerate(d.get("routes", [])):
        yy = 258 + i * 28
        rleg.append(f'<g class="lg" data-g="r-{rt["id"]}"><line x1="3320" y1="{yy - 6}" x2="3390" y2="{yy - 6}" style="stroke:{rt["color"]};stroke-width:7;stroke-dasharray:14 7"/>'
                    + txt(3406, yy, rt["id"] + ": " + rt["what"], 17, "lgt", avail=1370) + "</g>")
    rleg.append("</g>")

    # ---- Row E: Library shelf 3 (repos)
    E_TOP = D_TOP + max(ref_h, ship_h) + 70
    rp = d.get("repos", {})
    cols3 = [("INSTALLED (on disk now)", rp.get("installed", []), "#17803d"), ("APPROVED OR RECOMMENDED, NOT INSTALLED (needs Zac's yes)", rp.get("approved", []), "#b4580a")]
    CW = (W - 2 * (X0 - 40) - 3 * 40 - 40) / 3
    nmax = max(len(c[1]) for c in cols3)
    keep_lines = wrap(rp.get("keep_out", ""), 78)
    box_h = 70 + max(nmax * 74, len(keep_lines) * 26) + 20
    E_H = 66 + box_h + 24
    lib3 = [f'<g class="lib3"><rect x="{X0 - 40}" y="{E_TOP}" width="{W - 2 * (X0 - 40)}" height="{E_H}" rx="22" class="blk support"/>',
            txt(X0 - 10, E_TOP + 46, "LIBRARY DEPARTMENT, shelf 3 of 3: repos and outside tools (what we run, what is waiting, what stays out) and the department each serves", 25, "btitle")]
    for i, (ttl_, items, col) in enumerate(cols3):
        bx = X0 - 10 + i * (CW + 40)
        lib3.append(f'<rect x="{bx}" y="{E_TOP + 66}" width="{CW}" height="{box_h}" rx="14" class="gb"/><rect x="{bx}" y="{E_TOP + 66}" width="14" height="{box_h}" rx="6" style="fill:{col}"/>')
        lib3.append(txt(bx + 30, E_TOP + 66 + 36, ttl_, 21, "gtitle", avail=CW - 44))
        for j, it in enumerate(items):
            yy = E_TOP + 66 + 70 + j * 74
            lib3.append(txt(bx + 30, yy, it["name"], 18, "aname", avail=CW - 44))
            lib3.append(txt(bx + 30, yy + 24, "serves: " + it["serves"], 16, "ajob", avail=CW - 44))
            lib3.append(txt(bx + 30, yy + 46, it["note"], 15, "sk", avail=CW - 44))
    bx = X0 - 10 + 2 * (CW + 40)
    lib3.append(f'<rect x="{bx}" y="{E_TOP + 66}" width="{CW}" height="{box_h}" rx="14" class="gb"/><rect x="{bx}" y="{E_TOP + 66}" width="14" height="{box_h}" rx="6" style="fill:#7a7a7a"/>')
    lib3.append(txt(bx + 30, E_TOP + 66 + 36, "KEEP OUT (read, rejected for now)", 21, "gtitle", avail=CW - 44))
    for j, ln in enumerate(keep_lines):
        lib3.append(txt(bx + 30, E_TOP + 66 + 70 + j * 26, ln, 17, "sk"))
    lib3.append("</g>")
    lib3.append(f'<line x1="60" y1="{BUS4}" x2="60" y2="{E_TOP + E_H / 2}" class="rep"/><line x1="60" y1="{E_TOP + E_H / 2}" x2="{X0 - 40}" y2="{E_TOP + E_H / 2}" class="rep"/>')
    H = E_TOP + E_H + 120
    ship_stub += lib3
    chip_svg += route_dots + rleg
    foot = [txt(X0, H - 60, "Reporting lines: AGENT-NETWORK.md and each agent spec. Connector status: callable in the build session, not read from settings. Source data: D:\\WKP\\data\\org-chart-data.json", 17, "note")]

    body = "".join(title + leg + top + rl + ship_stub + skill_lines + routes_svg + shapes + lib + chip_svg + ref + ship + foot)
    return body, H, dict(pos=pos, blocks=blocks)


CSS = """
:root{--bg:#f6f4ef;--fg:#1d2433;--sub:#55607a;--venture:#e3edfa;--shared:#e4f3e8;--support:#f1eadb;--box:#ffffff;--bord:#8a96ad;--boss:#1f3a5f;--bosst:#fff;--line:#3b4560;--trunk:#9aa6bd;--jc:#222222;--frame:#9aa6bd;--zac:#5b2a86;--ok:#17803d;--na:#b4580a;--web:#556;--card:#fff}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#12161f;--fg:#e8ecf5;--sub:#a9b4cc;--venture:#1b2a42;--shared:#17332a;--support:#2a2519;--box:#1c2333;--bord:#5d6b88;--boss:#3a63a0;--bosst:#fff;--line:#c4ccdd;--trunk:#4a5672;--jc:#f2f2f2;--frame:#5d6b88;--zac:#8d5cc4;--ok:#5fd38a;--na:#ffb15c;--web:#b7c0d6;--card:#1a2030}}
:root[data-theme=dark]{--bg:#12161f;--fg:#e8ecf5;--sub:#a9b4cc;--venture:#1b2a42;--shared:#17332a;--support:#2a2519;--box:#1c2333;--bord:#5d6b88;--boss:#3a63a0;--bosst:#fff;--line:#c4ccdd;--trunk:#4a5672;--jc:#f2f2f2;--frame:#5d6b88;--zac:#8d5cc4;--ok:#5fd38a;--na:#ffb15c;--web:#b7c0d6;--card:#1a2030}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font-family:"Segoe UI",Arial,sans-serif}
header{padding:16px;display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between}
h1{font-size:1.25rem;margin:0}.sub{color:var(--sub);font-size:.9rem;margin:2px 0 0}
.controls button{background:var(--card);color:var(--fg);border:1px solid var(--bord);border-radius:8px;padding:6px 12px;margin-left:6px;font-size:.9rem;cursor:pointer}
.chart{overflow:auto;border-top:1px solid var(--bord);border-bottom:1px solid var(--bord);max-height:86vh}
svg{display:block;width:100%;min-width:1300px;height:auto;font-family:"Segoe UI",Arial,sans-serif}
.title{fill:var(--fg);font-weight:700}.subtitle,.note,.lgt{fill:var(--sub)}.lgt{fill:var(--fg)}
.blk{stroke:var(--bord);stroke-width:2}.blk.venture{fill:var(--venture)}.blk.shared{fill:var(--shared)}.blk.support{fill:var(--support)}
.btitle{fill:var(--fg);font-weight:700;letter-spacing:.3px}.frame{fill:none;stroke:var(--frame);stroke-width:2;stroke-dasharray:10 6}.flabel{fill:var(--sub);font-weight:700}
.abox{fill:var(--box);stroke:var(--bord);stroke-width:2.5}.ag{cursor:pointer}.ag:hover .abox,.ag:focus .abox,.ag.pin .abox{stroke:var(--fg);stroke-width:5}
.boss .abox{fill:var(--boss);stroke:var(--boss)}.boss .aname{fill:var(--bosst)}.boss .ajob{fill:#dbe6f7}
.aname{fill:var(--fg);font-weight:700}.ajob{fill:var(--sub)}.planned .abox{stroke-dasharray:9 6;fill:transparent}.builtin .abox,.abox.builtin{stroke-dasharray:3 5}
.ptag{fill:#d98b00}.ptagt{fill:#fff;font-weight:700}.ptagt2{fill:var(--sub);font-style:italic}.refbox{stroke-dasharray:9 5;fill:transparent}
.abox.dashed{stroke-dasharray:9 6}.cok{fill:var(--ok);font-weight:700}.cna{fill:var(--na);font-weight:700}.cweb{fill:var(--web);font-weight:700}
.abox.later{fill:#d7d7d7;stroke:#9a9a9a;stroke-dasharray:10 6;opacity:.7}.aname.later,.ajob.later{fill:#7a7a7a}
.zacbox{fill:var(--zac)}.zname,.zjob{fill:#fff}.zname{font-weight:700}.jbox{fill:var(--boss);stroke:var(--fg);stroke-width:4}.jname{fill:#fff;font-weight:800;letter-spacing:3px}.jjob{fill:#dbe6f7}
.rep{stroke:var(--line);stroke-width:4;fill:none}.trunk{stroke:var(--trunk);stroke-width:4}.dot{stroke:var(--line);stroke-width:4;stroke-dasharray:3 7}
.sl{fill:none;stroke-width:7;stroke-linecap:round;opacity:.85}svg.focus .sl{opacity:.06}svg.focus .sl.on{opacity:1;stroke-width:11}svg.focus .gbox:not(.on){opacity:.35}
.gb{fill:var(--box);stroke:var(--bord);stroke-width:2}.gtitle{fill:var(--fg);font-weight:700}.sk{fill:var(--sub)}.gbox,.lg{cursor:pointer}.gbox:hover .gb{stroke:var(--fg);stroke-width:4}
.chip{stroke:var(--box);stroke-width:2}
.rth{fill:none;stroke:var(--bg);stroke-width:8;opacity:.8;stroke-linecap:round}.rtl{fill:none;stroke-width:3.2;stroke-dasharray:14 7;stroke-linecap:round}svg.focus .rt{opacity:.06}svg.focus .rt.on{opacity:1}
#tip{position:fixed;pointer-events:none;background:var(--card);color:var(--fg);border:1px solid var(--bord);border-radius:10px;padding:10px 12px;max-width:360px;font-size:.85rem;box-shadow:0 6px 24px rgba(0,0,0,.25);display:none;z-index:9}
#tip b{display:block;font-size:.95rem;margin-bottom:3px}#tip span{color:var(--sub);display:block;margin-top:4px;font-size:.78rem}
section.lists{padding:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
details{background:var(--card);border:1px solid var(--bord);border-radius:10px;padding:8px 12px}summary{cursor:pointer;font-weight:700}
details li{margin:3px 0;font-size:.88rem;list-style:none}details ul{padding-left:0}details code{color:var(--sub)}
.shot header,.shot .lists,.shot #tip{display:none}.shot .chart{max-height:none;overflow:visible;border:0}.shot svg{width:5000px;min-width:0}
@media print{:root{--bg:#fff}body{background:#fff}header .controls,#tip{display:none}.chart{max-height:none;overflow:visible}svg{min-width:0}@page{size:landscape;margin:8mm}}
@media (max-width:700px){header{padding:12px}}
"""

JS = """
const AG=__AG__, CN=__CN__;
const tip=document.getElementById('tip'), svg=document.getElementById('org');
if(location.search.indexOf('shot')>-1){document.body.classList.add('shot');document.documentElement.setAttribute('data-theme','light')}
function show(h,ev){tip.innerHTML=h;tip.style.display='block';move(ev)}
function move(ev){let x=ev.clientX+16,y=ev.clientY+16;const r=tip.getBoundingClientRect();if(x+r.width>innerWidth-8)x=ev.clientX-r.width-16;if(y+r.height>innerHeight-8)y=ev.clientY-r.height-16;tip.style.left=Math.max(8,x)+'px';tip.style.top=Math.max(8,y)+'px'}
function agentHtml(id){const a=AG[id];if(!a)return null;return '<b>'+a.id+(a.status==='planned'?' (PLANNED)':'')+'</b>'+a.job+'<br>'+a.desc+'<span>Reports to: '+a.reports_to+(a.spec_file?'<br>Spec: '+a.spec_file:'<br>No spec file')+'<br>Model: '+a.model+'<br>Tools: '+a.tools+'</span>'}
svg.addEventListener('mousemove',ev=>{const g=ev.target.closest('.ag,.cn,.gbox');if(!g){tip.style.display='none';return}
 let h=null;if(g.classList.contains('ag'))h=agentHtml(g.dataset.id)||('<b>'+g.querySelector('title').textContent+'</b>');
 else if(g.classList.contains('cn')){const c=CN[g.dataset.cn];h='<b>'+c.name+'</b>'+c.status+'<br>Used by: '+c.used_by+'<span>Basis: '+c.basis+(c.note?'<br>'+c.note:'')+'</span>'}
 else{h='<b>'+g.querySelector('.gtitle').textContent+'</b>Click to isolate this group\\'s lines'}
 show(h,ev)});
svg.addEventListener('mouseleave',()=>tip.style.display='none');
svg.addEventListener('click',ev=>{const a=ev.target.closest('.ag');if(a){a.classList.toggle('pin');return}
 const g=ev.target.closest('.gbox,.lg');if(g)focus(g.dataset.g)});
let cur=null;
function focus(k){svg.querySelectorAll('.on').forEach(n=>n.classList.remove('on'));if(cur===k){cur=null;svg.classList.remove('focus');return}
 cur=k;svg.classList.add('focus');svg.querySelectorAll('[data-g="'+k+'"]').forEach(n=>n.classList.add('on'))}
let z=100;const set=()=>{svg.style.width=z+'%'};
document.getElementById('zin').onclick=()=>{z=Math.min(300,z+25);set()};
document.getElementById('zout').onclick=()=>{z=Math.max(100,z-25);set()};
document.getElementById('zfit').onclick=()=>{z=100;set();if(cur)focus(cur)};
document.getElementById('theme').onclick=()=>{const r=document.documentElement;const dark=getComputedStyle(r).getPropertyValue('--bg').trim()==='#12161f';r.setAttribute('data-theme',dark?'light':'dark')};
"""


def html_page(body, H):
    ag = {k: dict(id=v["id"], job=v["job"], desc=v["desc"], reports_to=v["reports_to"], status=v["status"], spec_file=v["spec_file"], model=v["model"], tools=v["tools"]) for k, v in AGENTS.items()}
    # lists
    lists = []
    for dep in d["departments"]:
        li = [f'<li><b>{e(dep["boss"])}</b> <code>boss</code><br>{e(AGENTS[dep["boss"]]["job"])}</li>']
        for sec in dep["sections"]:
            for aid in sec.get("agents", []):
                li.append(f'<li><b>{e(aid)}</b><br>{e(AGENTS[aid]["job"])}</li>')
        lists.append(f'<details><summary>{e(dep["name"])}</summary><ul>{"".join(li)}</ul></details>')
    nspec = sum(1 for a in AGENTS.values() if a["spec_exists"])
    sub = f"{len(AGENTS)} agents shown ({nspec} live with spec files), {len(d['departments'])} department blocks plus Library, Reference and Shipping, {len(d['skills'])} skills, {len(d['connectors'])} connectors drawn. Hover or tap a box for details."
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WKP Org Chart</title><style>{CSS}</style></head><body>
<header><div><h1>Warrior King Productions: Organization Chart</h1><p class="sub">{e(sub)}</p></div>
<div class="controls"><button id="zout">Zoom out</button><button id="zfit">Fit</button><button id="zin">Zoom in</button><button id="theme">Light / dark</button></div></header>
<div class="chart"><svg id="org" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="WKP organization chart">{body}</svg></div>
<div id="tip"></div>
<section class="lists">{''.join(lists)}</section>
<script>{JS.replace('__AG__', json.dumps(ag)).replace('__CN__', json.dumps(d['connectors']))}</script></body></html>"""


def make_png(H):
    url = "file:///" + HTML_PATH.replace("\\", "/").replace(" ", "%20") + "?shot=1"
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{int(H) + 140}",
                    "--force-device-scale-factor=1", "--virtual-time-budget=4000", f"--screenshot={PNG_PATH}", url], check=True, timeout=240)


def make_docx(H):
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.section import WD_ORIENT
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    doc = Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Inches(11), Inches(8.5)
    for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, m, Inches(0.5))
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10)
    doc.add_heading("Warrior King Productions: Organization Chart", 0)
    nspec = sum(1 for a in AGENTS.values() if a["spec_exists"])
    planned = [a["id"] for a in AGENTS.values() if a["status"] == "planned"]
    doc.add_paragraph(f"Built {d['generated']} from the repo agent specs, AGENT-NETWORK.md and the skill folders. {len(AGENTS)} agents shown ({nspec} live, each with a spec file in D:\\WKP\\.claude\\agents), "
                      f"{len(d['departments'])} department blocks plus the Library, Reference and Shipping departments, {len(d['skills'])} skills, {len(d['connectors'])} connectors drawn "
                      f"plus {len(d['not_authorized'])} installed but not authorized. Planned agents with no spec file: {', '.join(planned) if planned else 'none'}.")
    doc.add_paragraph("Page 2 is the whole chart on one page. Pages 3 to 6 are the same chart cut into four quarters so the labels are readable on paper. The interactive version is the .html file in this folder.")
    doc.add_page_break()
    doc.add_picture(PNG_PATH, width=Inches(7.9))
    doc.paragraphs[-1].alignment = 1
    im = Image.open(PNG_PATH)
    w, h = im.size
    for r in range(2):
        for c in range(2):
            doc.add_page_break()
            crop = im.crop((c * w // 2, r * h // 2, (c + 1) * w // 2, (r + 1) * h // 2))
            tp = os.path.join(r"D:\WKP\scratch", f"orgchart_tile_{r}{c}.png")
            crop.save(tp)
            doc.add_picture(tp, width=Inches(7.4))
            doc.paragraphs[-1].alignment = 1
    doc.add_page_break()

    def table(headers, rows, widths=None):
        t = doc.add_table(rows=1, cols=len(headers)); t.style = "Light Grid Accent 1"
        for i, hh in enumerate(headers):
            t.rows[0].cells[i].text = hh
        for r in rows:
            cells = t.add_row().cells
            for i, v in enumerate(r):
                cells[i].text = str(v)
        for row in t.rows:
            for i, cell in enumerate(row.cells):
                for p in cell.paragraphs:
                    for run in p.runs:
                        run.font.size = Pt(8.5)
                if widths:
                    cell.width = Inches(widths[i])
        doc.add_paragraph()

    doc.add_heading("Agents by department", 1)
    doc.add_paragraph("Jarvis (Ares) is the CEO. chief-of-staff is his standing assistant. claude-code-guide is the built-in research helper (no repo spec).")
    table(["Agent", "Job", "Reports to", "Status", "Spec file"], [[a["id"], a["job"], a["reports_to"], a["status"], a["spec_file"] or "none"] for a in [AGENTS["jarvis"], AGENTS["claude-code-guide"], AGENTS["chief-of-staff"]]], [1.8, 2.6, 1.4, 1.0, 3.0])
    for dep in d["departments"]:
        doc.add_heading(dep["name"], 2)
        ids = [dep["boss"]]
        for sec_ in dep["sections"]:
            ids += sec_.get("agents", [])
        rows = []
        for aid in ids:
            a = AGENTS[aid]
            role = "boss" if aid == dep["boss"] else "bench"
            rows.append([aid + (" (" + role + ")"), a["job"] + ". " + a["desc"], a["reports_to"], a["status"], a["model"], a["tools"]])
        for sec_ in dep["sections"]:
            if sec_.get("ref"):
                rows.append([sec_["ref"]["id"] + " (link only)", sec_["ref"]["note"], "marketing-director", "live", AGENTS[sec_["ref"]["id"]]["model"], "see Marketing"])
        table(["Agent", "Job", "Reports to", "Status", "Model", "Tools"], rows, [1.7, 3.6, 1.2, 0.7, 0.6, 2.2])
    doc.add_heading("Library: skills and who they connect to", 1)
    doc.add_paragraph("Line color in the chart equals the skill group. Skills marked account live in the Claude account skill list, not in D:\\WKP\\.claude\\skills.")
    rows = []
    for gk, g in GROUPS.items():
        for s_ in [x for x in d["skills"] if x["group"] == gk]:
            conn = ", ".join(g["targets"]) + (("; also " + s_["also"]) if s_["also"] else "")
            rows.append([g["name"], s_["name"], s_["source"], conn, s_["note"]])
    table(["Group (line color)", "Skill", "Source", "Connects to", "Note"], rows, [1.6, 2.2, 1.2, 3.2, 1.8])
    doc.add_heading("Library shelf 3: repos and outside tools", 1)
    rp = d.get("repos", {})
    table(["State", "Repo or tool", "Serves", "Note"], [["installed", r_["name"], r_["serves"], r_["note"]] for r_ in rp.get("installed", [])] + [["not installed", r_["name"], r_["serves"], r_["note"]] for r_ in rp.get("approved", [])], [1.2, 3.0, 2.2, 3.4])
    doc.add_paragraph("Keep out: " + rp.get("keep_out", ""))
    doc.add_heading("Service routing lines (who must use which desk)", 1)
    table(["Service desk", "What it is for", "Lines go to"], [[r_["id"], r_["what"], ", ".join(r_["to"])] for r_ in d.get("routes", [])], [1.6, 3.4, 5.0])
    doc.add_heading("Reference: connectors", 1)
    table(["Connector", "Status", "Used by", "Basis"], [[c["name"], c["status"], c["used_by"], c["basis"] + (". " + c["note"] if c["note"] else "")] for c in d["connectors"]], [2.0, 1.6, 3.0, 3.2])
    doc.add_paragraph("Available, not connected: " + ", ".join(d["not_authorized"]) + ".")
    doc.add_paragraph("Other, not WKP relevant: " + "; ".join(d["other_connectors"]) + ".")
    doc.add_heading("Local tools (verified by running)", 1)
    table(["Tool", "Where", "Serves"], [[t_["name"], t_["where"], t_["serves"]] for t_ in d.get("tools", [])], [3.0, 4.0, 3.0])
    doc.add_heading("Shipping", 1)
    table(["Channel", "What it is", "Status"], [[s_["name"], s_["job"], s_["status"]] for s_ in d["shipping"]], [2.2, 4.8, 1.2])
    doc.add_paragraph("Gate before anything ships: department boss approves, qa-director PASS, Jarvis reviews, then Zac. Zac posts. Agents never post.")
    doc.add_heading("Notes and limits", 1)
    for n in d["notes"]:
        doc.add_paragraph(n, style="List Bullet")
    doc.save(DOCX_PATH)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    body, H, info = build()
    open(HTML_PATH, "w", encoding="utf-8").write(html_page(body, H))
    print("html", os.path.getsize(HTML_PATH), "H", H)
    if "--no-png" not in sys.argv:
        make_png(H)
        print("png ok")
        make_docx(H)
        print("docx ok")
