import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_ROW_HEIGHT_RULE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import content_a as A, content_b as B, content_c as C, content_d as D, content_e as E, content_f as F
from quotes import Q as QUOTES

OUT_DOCX = r"D:\WKP Reports\Story Bible Answer Sheet\2026-11-21 - Shattered Empire Story Bible Answer Sheet.docx"
OUT_MD = r"D:\WKP\Shattered-Empire\third_draft\2026-11-21 - Shattered Empire Story Bible Answer Sheet.md"

# ---------- parse old questions ----------
OLDQ = {}
cur_ch = ""
for line in open(r"D:\WKP\Shattered-Empire\third_draft\Story_Guide_Update_Sheet.md", encoding="utf-8"):
    m = re.match(r"### (.+)", line)
    if m:
        cur_ch = m.group(1).strip()
    m = re.match(r"- Q(\d+) \[[^\]]+\] (.*)", line.strip())
    if m:
        OLDQ[int(m.group(1))] = (cur_ch, m.group(2).strip().replace(": ", ". ").replace(":", "."))

# ---------- numbering ----------
order = []  # (section, kind, obj)
def add(sec, kind, obj):
    order.append((sec, kind, obj))

for b in C.BEATS: add(3, "beat", b)
for q in C.STORY_Q: add(3, "q", q)
for q in C.CHAR_Q: add(4, "q", q)
for s in D.SPEECH: add(5, "speech", s)
add(5, "support", None)
for t in D.GENERAL_SPEECH_Q: add(5, "q", dict(k=t[0], q=t[1], d=t[2], o=t[3], r=t[4]))
for r in D.REGIONS: add(6, "region", r)
for t in D.REGION_Q: add(6, "q", dict(k=t[0], q=t[1], d=t[2], o=t[3], r=t[4]))
for sub, lst in E.WORLD.items():
    add(7, "sub", sub)
    for q in lst: add(7, "q", q)
for q in E.BOOK2_Q: add(8, "q", q)
for q in F.S9_SINGLE: add(9, "q", q)
for bt in F.BATCHES: add(9, "batch", bt)
for q in F.S10_SINGLE: add(10, "q", q)
for p in F.PITCHES: add(10, "pitch", p)

KEY = {}
n = 0
for i, (sec, kind, obj) in enumerate(order):
    if kind == "sub":
        continue
    n += 1
    if kind == "support":
        k = "support"
    elif kind == "pitch":
        k = obj[0]
    else:
        k = obj["k"]
    if k in KEY:
        raise SystemExit("duplicate key " + k)
    KEY[k] = n
    order[i] = (sec, kind, obj, n)
order = [o if len(o) == 4 else (o[0], o[1], o[2], None) for o in order]
TOTAL = n

def R(text):
    def rep(m):
        k = m.group(1)
        if k not in KEY:
            raise SystemExit("missing key " + k)
        return "S%d" % KEY[k]
    return re.sub(r"\[\[([a-z0-9_]+)\]\]", rep, text)

# ---------- coverage of old questions ----------
covered = set()
blob = []
for sec, kind, obj, num in order:
    if kind in ("q", "beat"):
        blob.append(" ".join(str(v) for v in obj.values()))
    if kind == "batch":
        covered.update(obj["rows"])
for t in B.CLOSED_OLD + B.GUIDE_ONLY:
    blob.append(" ".join(t))
for t in A.RULED_NO:
    blob.append(" ".join(t))
for m in re.finditer(r"Q(\d+)", " ".join(blob)):
    covered.add(int(m.group(1)))
missing = sorted(set(OLDQ) - covered)

# ---------- docx helpers ----------
doc = Document()
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)
for s in doc.sections:
    s.left_margin = s.right_margin = Inches(0.8)
    s.top_margin = s.bottom_margin = Inches(0.7)

MD = []

def para(text, bold=False, size=None, italic=False, color=None, align=None, space_after=4):
    p = doc.add_paragraph()
    r = p.add_run(R(text))
    r.bold = bold
    r.italic = italic
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor(*color)
    if align: p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    return p

def labeled(label, text):
    p = doc.add_paragraph()
    a = p.add_run(label + ". ")
    a.bold = True
    p.add_run(R(text))
    p.paragraph_format.space_after = Pt(3)
    MD.append("**%s.** %s\n" % (label, R(text)))

def heading(text, level):
    h = doc.add_heading(R(text), level=level)
    MD.append("%s %s\n" % ("#" * (level + 1), R(text)))
    return h

def set_cell_shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)

def no_split(row):
    trPr = row._tr.get_or_add_trPr()
    cs = OxmlElement("w:cantSplit"); trPr.append(cs)

def answer_box(label="Your answer", height=1.1):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    row = t.rows[0]
    row.height = Inches(height)
    row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    no_split(row)
    c = row.cells[0]
    r = c.paragraphs[0].add_run(label)
    r.font.size = Pt(8); r.font.color.rgb = RGBColor(120, 120, 120)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    MD.append("**%s**\n\n> &nbsp;\n>\n> &nbsp;\n>\n> &nbsp;\n" % label)

def table(headers, rows, widths=None, height=None, header_fill="D9E2F3"):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.paragraphs[0].add_run(h).bold = True
        set_cell_shade(c, header_fill)
    hdr = t.rows[0]._tr.get_or_add_trPr(); th = OxmlElement("w:tblHeader"); hdr.append(th)
    for r in rows:
        cells = t.add_row().cells
        for i, v in enumerate(r):
            cells[i].paragraphs[0].add_run(R(str(v))).font.size = Pt(9.5)
        row = t.rows[-1]
        no_split(row)
        if height:
            row.height = Inches(height); row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    MD.append("| " + " | ".join(headers) + " |")
    MD.append("|" + "---|" * len(headers))
    for r in rows:
        MD.append("| " + " | ".join(R(str(v)).replace("|", "/") for v in r) + " |")
    MD.append("")

def pagebreak():
    doc.add_page_break()

def mdp(text):
    MD.append(R(text) + "\n")

def qblock(num, q):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_before = Pt(8)
    r = p.add_run("S%d. " % num); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
    r2 = p.add_run(R(q["q"])); r2.bold = True; r2.font.size = Pt(12)
    MD.append("### S%d. %s\n" % (num, R(q["q"])))
    for lab, key in (("Where this comes from", "d"), ("Options", "o"), ("My recommendation", "r")):
        pp = doc.add_paragraph(); pp.paragraph_format.keep_with_next = True; pp.paragraph_format.space_after = Pt(2)
        a = pp.add_run(lab + ". "); a.bold = True
        b = pp.add_run(R(q[key]))
        if key == "d": b.font.size = Pt(9.5)
        MD.append("**%s.** %s\n" % (lab, R(q[key])))
    answer_box()

def quotes_for(key):
    return QUOTES.get(key, [])

# ---------- TITLE ----------
para(A.TITLE, bold=True, size=22, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
para(A.SUBTITLE, bold=True, size=14, align=WD_ALIGN_PARAGRAPH.CENTER)
para(A.DATELINE, italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
MD.append("# %s\n\n**%s**\n\n*%s*\n" % (A.TITLE, A.SUBTITLE, A.DATELINE))
heading("How to upload this to your Claude project", 2)
for l in A.UPLOAD_NOTE: para(l); mdp(l)

heading("Section 0. Locked decisions", 1)
for lid, head, body, tail in A.LOCKED_NOW:
    t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
    c = t.rows[0].cells[0]; set_cell_shade(c, "FCE4D6")
    r = c.paragraphs[0].add_run("%s. %s" % (lid, head)); r.bold = True; r.font.size = Pt(13)
    c.add_paragraph(body); c.add_paragraph(tail)
    doc.add_paragraph()
    MD.append("> **%s. %s**\n> %s\n> %s\n" % (lid, head, body, tail))
para("Older suggestions now RULED NO by L1 (not asked again)", bold=True); mdp("**Older suggestions now RULED NO by L1 (not asked again)**")
table(["Where it came from", "What it said", "Ruling"], A.RULED_NO, widths=[1.8, 2.6, 2.6])
para("I searched the Pitch Report, the 2,111 edit cards, the Update Sheet, the Editor Packet and both Story Guides. None of them proposed cutting a named team member outright. The rows above are the only places that leaned toward fewer people.", italic=True, size=9.5)
mdp("*I searched the Pitch Report, the 2,111 edit cards, the Update Sheet, the Editor Packet and both Story Guides. None of them proposed cutting a named team member outright. The rows above are the only places that leaned toward fewer people.*")
pagebreak()

# ---------- TALLY ----------
heading("Tally index", 1)
secnames = {3: "Story-level questions and the major beats", 4: "Character questions", 5: "Speech and accent lock, by person", 6: "Region speech lock", 7: "World-building and rules", 8: "Book 2 and beyond", 9: "Edit-card questions, grouped by theme", 10: "Zac-only decisions, the guide, length and structure pitches"}
rows = []
for s in range(3, 11):
    nums = [o[3] for o in order if o[0] == s and o[3]]
    rows.append(["Section %d" % s, secnames[s], "S%d to S%d" % (min(nums), max(nums)), str(len(nums))])
rows.insert(0, ["Section 0", "Locked now (teams stay full size, this sheet is final)", "L1, L2", "0 to answer"])
rows.insert(1, ["Section 2", "Already locked, with sources", "%d items" % len(B.LOCKED), "0 to answer"])
batch_rows = sum(len(b["rows"]) for b in F.BATCHES) + len(D.SUPPORT)
rows.append(["Total", "Numbered questions (batch tables add %d tick rows)" % batch_rows, "S1 to S%d" % TOTAL, str(TOTAL)])
table(["Section", "What is in it", "Numbers", "Count"], rows, widths=[1.0, 3.8, 1.3, 0.9])
para("Start here. These settle the most edits.", bold=True); mdp("**Start here. These settle the most edits.**")
sh = []
for k in F.START_HERE:
    num = KEY[k]
    obj = [o for o in order if o[3] == num][0]
    txt = ("Pitch %s. " % obj[2][1] + obj[2][3]) if obj[1] == "pitch" else obj[2].get("q", obj[2].get("title"))
    sh.append(["S%d" % num, txt[:120] + ("..." if len(txt) > 120 else ""), ""])
table(["Number", "Question", "Done"], sh, widths=[0.8, 5.5, 0.7])
pagebreak()

# ---------- SECTION 1 ----------
heading("Section 1. How to use this sheet", 1)
for l in A.HOW_TO_USE: para(l); mdp(l)
pagebreak()

# ---------- SECTION 2 ----------
heading("Section 2. Already locked. Do not re-ask.", 1)
para("You already decided these. They are not asked again anywhere in this sheet. If one is wrong, strike it and write the fix in the margin.")
mdp("You already decided these. They are not asked again anywhere in this sheet. If one is wrong, strike it and write the fix in the margin.")
table(["Item", "What is locked", "Where it is locked"], B.LOCKED, widths=[1.5, 3.7, 1.8])
heading("Answers the Guide gives that you never ruled on directly", 2)
para("These stand unless you strike them. Tick Strike to reopen one.")
mdp("These stand unless you strike them. Tick Strike to reopen one.")
table(["Item", "What the Guide says", "Note", "Strike"], [list(r) + [""] for r in B.GUIDE_ONLY], widths=[1.4, 2.8, 2.2, 0.6])
heading("Old questions these locks already close", 2)
table(["Old question", "Closed by"], B.CLOSED_OLD, widths=[2.6, 4.4])
pagebreak()

# ---------- SECTIONS 3 to 10 ----------
cur = None
for sec, kind, obj, num in order:
    if sec != cur:
        if cur is not None: pagebreak()
        cur = sec
        heading("Section %d. %s" % (sec, secnames[sec]), 1)
        if sec == 3:
            para("Part A is the spine of the book, beat by beat. Each beat says what happens, why it matters, what I am unsure about, and points to the question that settles it. Write yes if the summary is right. Part B is the story-level questions.")
            mdp("Part A is the spine of the book, beat by beat. Write yes if the summary is right. Part B is the story-level questions.")
            heading("Part A. The major beats", 2)
        if sec == 5:
            for l in D.SPEECH_INTRO: para(l); mdp(l)
        if sec == 6:
            para(D.REGION_INTRO); mdp(D.REGION_INTRO)
        if sec == 8:
            heading("What Book 1 sets up", 2)
            for l in E.BOOK2_SETUP: para(l); mdp(l)
            heading("A better way, where I see one (opinions, marked as opinions)", 2)
            for l in E.BETTER_WAYS: para(l); mdp(l)
            answer_box("Your notes on any of the opinions above", 1.3)
            heading("Book 2 questions", 2)
        if sec == 9:
            para(F.S9_INTRO); mdp(F.S9_INTRO)
        if sec == 10:
            pass
    if kind == "sub":
        heading(obj, 2); continue
    if kind == "beat":
        p = doc.add_paragraph(); p.paragraph_format.keep_with_next = True; p.paragraph_format.space_before = Pt(8)
        r = p.add_run("S%d. " % num); r.bold = True; r.font.size = Pt(12); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        r2 = p.add_run(obj["title"]); r2.bold = True; r2.font.size = Pt(12)
        MD.append("### S%d. %s\n" % (num, obj["title"]))
        for lab, key in (("What happens", "what"), ("Why it matters", "why"), ("What I am unsure about", "unsure"), ("My recommendation", "r")):
            labeled(lab, obj[key])
        answer_box("Your answer (yes if the summary is right, or what to change)", 0.9)
        if obj is C.BEATS[-1]:
            heading("Part B. Story-level questions", 2)
        continue
    if kind == "q":
        if sec == 10 and obj["k"] == F.S10_SINGLE[0]["k"]:
            heading("Part A. The guide, length and the line pass", 2)
        qblock(num, obj); continue
    if kind == "speech":
        p = doc.add_paragraph(); p.paragraph_format.keep_with_next = True; p.paragraph_format.space_before = Pt(10)
        r = p.add_run("S%d. %s" % (num, obj["name"])); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        MD.append("### S%d. %s\n" % (num, obj["name"]))
        labeled("Region", obj["region"])
        labeled("How they talk on the page now", obj["talk"])
        labeled("What they never say", obj["never"])
        labeled("How to show the accent on the page, my recommendation", obj["page"])
        labeled("Under pressure", obj["pressure"])
        labeled("Options", "Lock it as written above, lock it with your changes in the table, or write your own rules.")
        qs = quotes_for(obj["quotes"])
        pp = doc.add_paragraph(); pp.add_run("Lines from your chapters, word for word.").bold = True
        MD.append("**Lines from your chapters, word for word.**\n")
        for qt, ch in qs:
            chn = "Prologue" if ch == "00" else "Ch %s" % ch
            b = doc.add_paragraph(style="List Bullet"); b.add_run('"%s" (%s)' % (qt, chn)).italic = True
            MD.append('- *"%s"* (%s)' % (qt, chn))
        MD.append("")
        if obj["open"]:
            labeled("Open question", obj["open"])
        t = doc.add_table(rows=0, cols=2); t.style = "Table Grid"
        for lab, h in (("How I want them to sound, in my words", 1.0), ("Accent method (circle) spelling, word order, rhythm only, none", 0.45), ("Words or sayings only they use", 0.6), ("Words they never say", 0.6), ("Region or accent different from above? Who and why", 0.6), ("Lock my recommendation? yes or no", 0.4)):
            row = t.add_row(); row.height = Inches(h); row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST; no_split(row)
            c0 = row.cells[0]; c0.width = Inches(2.3); c0.paragraphs[0].add_run(lab).font.size = Pt(9.5); set_cell_shade(c0, "F2F2F2")
            row.cells[1].width = Inches(4.7)
            MD.append("**%s**\n\n> &nbsp;\n" % lab)
        doc.add_paragraph()
        continue
    if kind == "support":
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10)
        r = p.add_run("S%d. Supporting voices" % num); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        MD.append("### S%d. Supporting voices\n" % num)
        para(D.SUPPORT_INTRO); mdp(D.SUPPORT_INTRO)
        rows = []
        for i, (nm, rg, rd, qk) in enumerate(D.SUPPORT, 1):
            ql = quotes_for(qk)
            line = '"%s" (%s)' % (ql[0][0], "Prologue" if ql[0][1] == "00" else "Ch " + ql[0][1]) if ql else "not on the page"
            rows.append(["S%d.%d" % (num, i), nm, rg, rd, line, ""])
        table(["No.", "Who", "Where from", "My read", "Their line", "Your change"], rows, widths=[0.55, 1.0, 0.9, 1.6, 1.8, 1.15], height=0.5)
        continue
    if kind == "region":
        p = doc.add_paragraph(); p.paragraph_format.keep_with_next = True; p.paragraph_format.space_before = Pt(10)
        r = p.add_run("S%d. %s" % (num, obj["name"])); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        MD.append("### S%d. %s\n" % (num, obj["name"]))
        labeled("Status", obj["status"])
        labeled("Shared speech rules", obj["rules"])
        labeled("Who speaks this way", obj["who"])
        labeled("Options", "Lock as written, lock with changes, or reopen.")
        labeled("My recommendation", "Lock as written. Locked items are already your rulings, proposed items come from your own pages.")
        answer_box("Your changes to these rules (or yes to lock)", 0.8)
        para("Same region, different accent (Book 2 ready)", bold=True, size=10); mdp("**Same region, different accent (Book 2 ready)**")
        table(["Who", "How they sound different", "Why"], [["", "", ""]] * 3, widths=[1.6, 2.9, 2.5], height=0.4)
        continue
    if kind == "batch":
        p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10)
        r = p.add_run("S%d. %s" % (num, obj["title"])); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        MD.append("### S%d. %s\n" % (num, obj["title"]))
        para(obj["intro"]); mdp(obj["intro"])
        labeled("Options", "Keep or Change on each row, or one answer for the whole table.")
        labeled("My recommendation", "The pick on each card in the edit cards. Where a row asks for a fact only you know, write it in Note.")
        rows = []
        for i, qn_ in enumerate(obj["rows"], 1):
            ch, txt = OLDQ[qn_]
            rows.append(["S%d.%d" % (num, i), "Q%d, %s" % (qn_, ch), txt, "", "", ""])
        table(["No.", "Old Q", "The question", "Keep", "Change", "Note"], rows, widths=[0.55, 0.85, 3.6, 0.5, 0.6, 0.9], height=0.45)
        answer_box("One answer for the whole table, if you prefer", 0.6)
        continue
    if kind == "pitch":
        k, pn, typ, summ, pick = obj
        if k == "p1":
            heading("Part B. Structure pitches", 2)
            para(F.PITCH_INTRO); mdp(F.PITCH_INTRO)
        q = dict(q="Pitch %s (%s). %s" % (pn, typ, summ), d="Story Pitch Report 2026-11-19, Pitch %s. Full write-up there, with what it grows, the ripple and the cost." % pn,
                 o="Yes, No, Maybe, or Yes with changes.", r=pick)
        qblock(num, q)
        continue

pagebreak()
heading("Sources used and what was not checked", 1)
srcs = [
 "Story Guide Update Sheet 2026-11-20 (docx and md), 28 story-level and 338 chapter questions.",
 "Garkins Canon Note and Ch 16 Insert 2026-11-20.",
 "Third Draft edit cards (55 files, 2,111 cards) and the 2026-11-04 Third Draft Editorial Report questions list.",
 "Story Pitch Report and Scene Map 2026-11-19 (33 pitches, 2 wild cards, 12 duplicates).",
 "The_Patience_of_the_Dark_Story_Guide v2 (2026-10-05) and Story Guide Draft 3 (2026-11-04), Master Character Annex Rebuilt v0.1, Aether Stone Magic System (through the Guide's Part Three), Editor Packet Third Draft, your First pass notes, the Third Draft Master Prompt locked decisions, the canon ledger and voice table.",
 "Fact-research brief, 2026-11-21 debut epic fantasy word count norms.",
 "Not checked. Google Drive copies were not opened, so a newer Drive edit of the manuscript or Guide is not ruled out. The Aether Stone doc was used through the Guide, not reread line by line. The edit cards were not reread one by one, their questions were taken from the report list. Word savings are estimates. Agent word limits beyond two confirmed sources are not verified.",
 "Every sample line in Section 5 was checked by script against the chapter text files and found word for word.",
]
for s_ in srcs: para(s_, size=10); mdp(s_)

os.makedirs(os.path.dirname(OUT_DOCX), exist_ok=True)
doc.save(OUT_DOCX)
open(OUT_MD, "w", encoding="utf-8").write("\n".join(MD))
print("TOTAL S", TOTAL, "batch rows", batch_rows)
print("uncovered old Q", missing)
