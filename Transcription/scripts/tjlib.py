"""Shared helpers for the Transcription business scripts.

Plain Python 3.12, no network. Needs openpyxl (installed) for the tracker.
Paths are set here once. Client files live in JOBS_ROOT (outside the repo).
"""
import csv
import datetime as dt
import json
import os
import re
import sys

JOBS_ROOT = os.environ.get("TJ_JOBS_ROOT", r"D:\Transcription Jobs")
TRACKER_DIR = os.environ.get("TJ_TRACKER_DIR", r"D:\WKP Reports\Transcription Tracker")
TRACKER_XLSX = os.path.join(TRACKER_DIR, "Transcription Tracker.xlsx")
TRACKER_CSV = os.path.join(TRACKER_DIR, "Transcription Tracker.csv")
TEMPLATE_DIR = os.path.join(JOBS_ROOT, "_template")

GIGS = {1: "sermons", 2: "podcast", 3: "captions", 4: "general"}
GIG_NAMES = {1: "Church sermons", 2: "Podcasts and audio shows",
             3: "Video captions (subtitle files)", 4: "General transcription (anything else)"}
WAITING = ("Zac", "agent", "buyer", "none")
CATEGORIES = ("machine", "proofreading", "conversion", "admin")
CAT_COL = {"machine": "Min machine", "proofreading": "Min proofreading",
           "conversion": "Min conversion", "admin": "Min admin"}

# (header, kind). kind: in = typed/script input, calc = formula column
COLUMNS = [
    ("Job ID", "in"), ("Status", "in"), ("Date received", "in"), ("Gig (1-4)", "in"),
    ("Fiverr order #", "in"), ("Buyer handle", "in"), ("Audio minutes", "in"),
    ("Audio quality 1-5", "in"), ("Speakers", "in"), ("Requested file types", "in"),
    ("Due date", "in"), ("Delivered date", "in"), ("On time", "calc"),
    ("Price", "in"), ("Fiverr fee (Zac enters, NOT verified)", "in"), ("Net", "calc"),
    ("Min machine", "in"), ("Min proofreading", "in"), ("Min conversion", "in"),
    ("Min admin", "in"), ("Total min worked", "calc"), ("Revisions", "in"),
    ("Review received", "in"), ("Waiting on", "in"), ("$ per audio min", "calc"),
    ("$ per hour worked", "calc"), ("Work-min per audio-min", "calc"), ("Notes", "in"),
]
HEAD = [c[0] for c in COLUMNS]
CALC = {c[0] for c in COLUMNS if c[1] == "calc"}
DATE_COLS = {"Date received", "Due date", "Delivered date"}
NUM_COLS = {"Audio minutes", "Audio quality 1-5", "Speakers", "Price",
            "Fiverr fee (Zac enters, NOT verified)", "Min machine", "Min proofreading",
            "Min conversion", "Min admin", "Revisions", "Gig (1-4)"}
FEE = "Fiverr fee (Zac enters, NOT verified)"


# ---------------------------------------------------------------- job folders
def today():
    return dt.date.today().isoformat()


def slug(text):
    return re.sub(r"[^A-Za-z0-9_-]+", "", text.strip().replace(" ", "-"))


def find_job(ref):
    """ref = full path, folder name, or a job ID like JOB-20261113-001."""
    if os.path.isdir(ref):
        return os.path.abspath(ref)
    if os.path.isdir(JOBS_ROOT):
        for name in sorted(os.listdir(JOBS_ROOT)):
            if name.startswith("_"):
                continue
            if name == ref or name.startswith(ref + "_") or name.startswith(ref):
                p = os.path.join(JOBS_ROOT, name)
                if os.path.isdir(p):
                    return p
    sys.exit(f"Job not found: {ref}  (looked in {JOBS_ROOT})")


def job_id_of(folder):
    m = re.match(r"(JOB-\d{8}-\d{3})", os.path.basename(folder))
    if not m:
        sys.exit(f"Folder name does not start with a job ID: {folder}")
    return m.group(1)


def read_job_json(folder):
    p = os.path.join(folder, "job.json")
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}


def write_job_json(folder, data):
    with open(os.path.join(folder, "job.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def next_job_number(date_str):
    """Highest NNN used today across folders AND tracker rows, plus one."""
    stamp = date_str.replace("-", "")
    used = [0]
    pat = re.compile(rf"JOB-{stamp}-(\d{{3}})")
    if os.path.isdir(JOBS_ROOT):
        for n in os.listdir(JOBS_ROOT):
            m = pat.match(n)
            if m:
                used.append(int(m.group(1)))
    if os.path.isfile(TRACKER_CSV):
        with open(TRACKER_CSV, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                m = pat.match(row.get("Job ID", ""))
                if m:
                    used.append(int(m.group(1)))
    return max(used) + 1


# ---------------------------------------------------------------- notes.md
LOG_MARK = "<!-- TIMER-LOG-END -->"
ISSUE_MARK = "<!-- ISSUES-END -->"


def append_to_notes(folder, line, marker=LOG_MARK):
    p = os.path.join(folder, "notes.md")
    if not os.path.isfile(p):
        return
    with open(p, encoding="utf-8") as f:
        text = f.read()
    if marker in text:
        text = text.replace(marker, line + "\n" + marker, 1)
    else:
        text += "\n" + line + "\n"
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)


# ---------------------------------------------------------------- clock state
def clock_path(folder):
    return os.path.join(folder, ".clock.json")


def load_clock(folder):
    p = clock_path(folder)
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {"totals": {c: 0.0 for c in CATEGORIES}, "running": None, "since": None,
            "paused": None}


def save_clock(folder, state):
    with open(clock_path(folder), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------- tracker
def _num(v):
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _date(v):
    if v is None or v == "":
        return None
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    try:
        return dt.date.fromisoformat(str(v)[:10])
    except ValueError:
        return None


def compute(row):
    """Python twin of the sheet formulas. Used for the CSV mirror and for tests."""
    out = {}
    due, deliv = _date(row.get("Due date")), _date(row.get("Delivered date"))
    out["On time"] = "" if not deliv or not due else ("yes" if deliv <= due else "no")
    price, fee = _num(row.get("Price")), _num(row.get(FEE))
    net = None if price is None or fee is None else price - fee
    out["Net"] = "" if net is None else round(net, 2)
    mins = [_num(row.get(CAT_COL[c])) or 0.0 for c in CATEGORIES]
    total = sum(mins)
    out["Total min worked"] = round(total, 1)
    audio = _num(row.get("Audio minutes"))
    out["$ per audio min"] = "" if net is None or not audio else round(net / audio, 3)
    out["$ per hour worked"] = "" if net is None or total <= 0 else round(net / (total / 60), 2)
    out["Work-min per audio-min"] = "" if not audio or total <= 0 else round(total / audio, 2)
    return out


def _check_writable(path):
    if os.path.exists(path):
        try:
            with open(path, "ab"):
                pass
        except PermissionError:
            sys.exit(f"Cannot write {path}. Close it in Excel and run again. Nothing was changed.")


def _formula(col, r, L):
    g = lambda h: f"{L[h]}{r}"
    if col == "On time":
        return f'=IF(OR({g("Due date")}="",{g("Delivered date")}=""),"",IF({g("Delivered date")}<={g("Due date")},"yes","no"))'
    if col == "Net":
        return f'=IF(OR({g("Price")}="",{g(FEE)}=""),"",{g("Price")}-{g(FEE)})'
    if col == "Total min worked":
        return f'=SUM({g("Min machine")}:{g("Min admin")})'
    if col == "$ per audio min":
        return f'=IF(OR({g("Net")}="",N({g("Audio minutes")})=0),"",{g("Net")}/{g("Audio minutes")})'
    if col == "$ per hour worked":
        return f'=IF(OR({g("Net")}="",N({g("Total min worked")})=0),"",{g("Net")}/({g("Total min worked")}/60))'
    if col == "Work-min per audio-min":
        return f'=IF(OR(N({g("Audio minutes")})=0,N({g("Total min worked")})=0),"",{g("Total min worked")}/{g("Audio minutes")})'
    raise KeyError(col)


def _letters():
    from openpyxl.utils import get_column_letter
    return {h: get_column_letter(i + 1) for i, h in enumerate(HEAD)}


def _make_workbook():
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.formatting.rule import FormulaRule
    wb = Workbook()
    ws = wb.active
    ws.title = "Jobs"
    ws.append(HEAD)
    L = _letters()
    for i, h in enumerate(HEAD, 1):
        c = ws.cell(1, i)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F3864" if h not in CALC else "7F7F7F")
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.column_dimensions[L[h]].width = 16
    ws.column_dimensions[L["Notes"]].width = 40
    ws.column_dimensions[L["Requested file types"]].width = 22
    ws.row_dimensions[1].height = 48
    ws.freeze_panes = "B2"
    dv_w = DataValidation(type="list", formula1='"Zac,agent,buyer,none"', allow_blank=True)
    dv_g = DataValidation(type="list", formula1='"1,2,3,4"', allow_blank=True)
    dv_q = DataValidation(type="list", formula1='"1,2,3,4,5"', allow_blank=True)
    for dv, h in ((dv_w, "Waiting on"), (dv_g, "Gig (1-4)"), (dv_q, "Audio quality 1-5")):
        ws.add_data_validation(dv)
        dv.add(f"{L[h]}2:{L[h]}1000")
    ws.conditional_formatting.add(
        f"A2:{L['Notes']}1000",
        FormulaRule(formula=[f'${L["Waiting on"]}2="Zac"'],
                    fill=PatternFill("solid", bgColor="FFE699")))
    # Summary sheet by gig
    sm = wb.create_sheet("Summary by gig")
    heads = ["Gig", "Name", "Jobs", "Audio minutes", "Price total", "Net total (fee entered)",
             "Hours worked (jobs with net)", "$ per audio min", "$ per hour worked",
             "Work-min per audio-min", "On-time rate", "Avg audio quality", "Waiting on Zac"]
    sm.append(heads)
    for i in range(1, len(heads) + 1):
        c = sm.cell(1, i)
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="1F3864")
        c.alignment = Alignment(wrap_text=True, vertical="top")
        sm.column_dimensions[c.column_letter].width = 18
    sm.column_dimensions["B"].width = 36
    R = lambda h: f"Jobs!${L[h]}$2:${L[h]}$1000"
    for r, g in enumerate((1, 2, 3, 4), 2):
        sm.cell(r, 1, g)
        sm.cell(r, 2, GIG_NAMES[g])
        sm.cell(r, 3, f'=COUNTIF({R("Gig (1-4)")},A{r})')
        sm.cell(r, 4, f'=SUMIFS({R("Audio minutes")},{R("Gig (1-4)")},A{r})')
        sm.cell(r, 5, f'=SUMIFS({R("Price")},{R("Gig (1-4)")},A{r})')
        sm.cell(r, 6, f'=SUMIFS({R("Net")},{R("Gig (1-4)")},A{r})')
        sm.cell(r, 7, f'=SUMIFS({R("Total min worked")},{R("Gig (1-4)")},A{r},{R("Net")},">-1000000")/60')
        sm.cell(r, 8, f'=IFERROR(F{r}/SUMIFS({R("Audio minutes")},{R("Gig (1-4)")},A{r},{R("Net")},">-1000000"),"")')
        sm.cell(r, 9, f'=IFERROR(F{r}/G{r},"")')
        sm.cell(r, 10, f'=IFERROR(SUMIFS({R("Total min worked")},{R("Gig (1-4)")},A{r})/D{r},"")')
        sm.cell(r, 11, f'=IFERROR(COUNTIFS({R("Gig (1-4)")},A{r},{R("On time")},"yes")/(COUNTIFS({R("Gig (1-4)")},A{r},{R("On time")},"yes")+COUNTIFS({R("Gig (1-4)")},A{r},{R("On time")},"no")),"")')
        sm.cell(r, 12, f'=IFERROR(AVERAGEIFS({R("Audio quality 1-5")},{R("Gig (1-4)")},A{r}),"")')
        sm.cell(r, 13, f'=COUNTIFS({R("Gig (1-4)")},A{r},{R("Waiting on")},"Zac")')
    sm.cell(6, 1, "All")
    for col in "CDEFG":
        sm[f"{col}6"] = f"=SUM({col}2:{col}5)"
    sm["H6"] = '=IFERROR(F6/SUMIFS(' + R("Audio minutes") + ',' + R("Net") + ',">-1000000"),"")'
    sm["I6"] = '=IFERROR(F6/G6,"")'
    sm["M6"] = "=SUM(M2:M5)"
    sm.cell(8, 1, "Net needs the Fiverr fee, which Zac types into the Jobs sheet. The fee is NOT verified by any script. Dollar-per-hour figures only count jobs that have a fee entered.")
    for sheet_row in range(2, 7):
        for col, fmt in (("E", "$#,##0.00"), ("F", "$#,##0.00"), ("G", "0.0"), ("H", "$0.000"),
                         ("I", "$#,##0.00"), ("J", "0.00"), ("K", "0%"), ("L", "0.0")):
            sm[f"{col}{sheet_row}"].number_format = fmt
    return wb


def _row_values(ws, r, L):
    row = {}
    for h in HEAD:
        if h in CALC:
            continue
        v = ws[f"{L[h]}{r}"].value
        row[h] = v
    return row


def tracker_rows():
    """All rows as dicts: input cells as stored, calc columns recomputed."""
    if not os.path.isfile(TRACKER_XLSX):
        return []
    from openpyxl import load_workbook
    wb = load_workbook(TRACKER_XLSX)
    ws = wb["Jobs"]
    L = _letters()
    rows = []
    for r in range(2, ws.max_row + 1):
        if not ws[f"{L['Job ID']}{r}"].value:
            continue
        row = _row_values(ws, r, L)
        row.update(compute(row))
        rows.append(row)
    return rows


def write_csv_mirror(rows=None):
    rows = tracker_rows() if rows is None else rows
    os.makedirs(TRACKER_DIR, exist_ok=True)
    with open(TRACKER_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEAD)
        for row in rows:
            out = []
            for h in HEAD:
                v = row.get(h)
                if isinstance(v, (dt.datetime, dt.date)):
                    v = _date(v).isoformat()
                out.append("" if v is None else v)
            w.writerow(out)


def _set_cell(ws, r, L, h, v):
    c = ws[f"{L[h]}{r}"]
    if h in DATE_COLS:
        d = _date(v)
        c.value = d
        if d:
            c.number_format = "yyyy-mm-dd"
    elif h in NUM_COLS and _num(v) is not None:
        n = _num(v)
        c.value = int(n) if n == int(n) and h in ("Gig (1-4)", "Speakers", "Revisions", "Audio quality 1-5") else n
    else:
        c.value = None if v == "" else v


def tracker_upsert(job_id, fields):
    """Create the workbook if needed, then update or append the row for job_id.
    fields = {header: value}. Calc columns are ignored (they are formulas)."""
    _check_writable(TRACKER_XLSX)
    _check_writable(TRACKER_CSV)
    os.makedirs(TRACKER_DIR, exist_ok=True)
    if os.path.isfile(TRACKER_XLSX):
        from openpyxl import load_workbook
        wb = load_workbook(TRACKER_XLSX)
    else:
        wb = _make_workbook()
    ws = wb["Jobs"]
    L = _letters()
    target = None
    last = 1
    for r in range(2, ws.max_row + 1):
        v = ws[f"{L['Job ID']}{r}"].value
        if v:
            last = r
        if v == job_id:
            target = r
    if target is None:
        target = last + 1
        ws[f"{L['Job ID']}{target}"] = job_id
        for h in HEAD:
            if h in CALC:
                ws[f"{L[h]}{target}"] = _formula(h, target, L)
        for h in ("$ per audio min", "$ per hour worked", "Work-min per audio-min", "Total min worked"):
            ws[f"{L[h]}{target}"].number_format = "0.00"
        ws[f"{L['Net']}{target}"].number_format = "$#,##0.00"
        ws[f"{L['Price']}{target}"].number_format = "$#,##0.00"
        ws[f"{L[FEE]}{target}"].number_format = "$#,##0.00"
    for h, v in fields.items():
        if h not in HEAD:
            sys.exit(f"Unknown tracker column: {h}")
        if h in CALC or h == "Job ID":
            continue
        _set_cell(ws, target, L, h, v)
    wb.save(TRACKER_XLSX)
    write_csv_mirror()
    return target


def tracker_get(job_id):
    for row in tracker_rows():
        if row.get("Job ID") == job_id:
            return row
    return None


def tracker_delete(job_id):
    """Remove a row (used only to clean up the fake test job)."""
    _check_writable(TRACKER_XLSX)
    from openpyxl import load_workbook
    wb = load_workbook(TRACKER_XLSX)
    ws = wb["Jobs"]
    L = _letters()
    for r in range(2, ws.max_row + 1):
        if ws[f"{L['Job ID']}{r}"].value == job_id:
            ws.delete_rows(r)
            # formulas moved up keep stale row numbers, so rewrite them
            for rr in range(r, ws.max_row + 1):
                if ws[f"{L['Job ID']}{rr}"].value:
                    for h in HEAD:
                        if h in CALC:
                            ws[f"{L[h]}{rr}"] = _formula(h, rr, L)
            wb.save(TRACKER_XLSX)
            write_csv_mirror()
            return True
    return False
