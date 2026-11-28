"""Two adapters that turn official SEC data into the same filing dicts form4.parse_form4 makes.

A. Insider Transactions Data Sets (quarterly bulk zip, one request per quarter, lags up to about 3 months): history and backtests.
   Column names come from the data set readme as data-sourcing read it (2026-11-26). The real header was NOT VERIFIED
   (no live pull yet), so columns are matched through alias lists and a missing required column stops with a clear error.
B. EDGAR daily index (form.YYYYMMDD.idx) plus one .txt submission per Form 4: fresh filings. The index layout and the
   acceptance-time field are NOT VERIFIED against a live file, the parser is tolerant and every miss is logged as a skip.
Neither adapter touches the network itself: the caller passes a SecClient (or bytes in tests)."""
import csv
import datetime as dt
import io
import re
import zipfile

from . import form4

TABLE_ALIASES = {
    "SUBMISSION": {
        "accession": ["ACCESSION_NUMBER"], "filing_date": ["FILING_DATE"], "doc_type": ["DOCUMENT_TYPE"],
        "period": ["PERIOD_OF_REPORT"], "issuer_cik": ["ISSUERCIK"], "issuer_name": ["ISSUERNAME"],
        "ticker": ["ISSUERTRADINGSYMBOL"], "aff10b5": ["AFF10B5ONE"],
    },
    "REPORTINGOWNER": {
        "accession": ["ACCESSION_NUMBER"], "owner_cik": ["RPTOWNERCIK"], "owner_name": ["RPTOWNERNAME"],
        "relationship": ["RPTOWNER_RELATIONSHIP"], "title": ["RPTOWNER_TITLE"], "other_text": ["RPTOWNER_TXT"],
    },
    "FOOTNOTES": {"accession": ["ACCESSION_NUMBER"], "fn_id": ["FOOTNOTE_ID"], "fn_text": ["FOOTNOTE_TXT"]},
    "NONDERIV_TRANS": {
        "accession": ["ACCESSION_NUMBER"], "date": ["TRANS_DATE"], "code": ["TRANS_CODE"], "shares": ["TRANS_SHARES"],
        "price": ["TRANS_PRICEPERSHARE"], "acq_disp": ["TRANS_ACQUIRED_DISP_CD"], "post": ["SHRS_OWND_FOLWNG_TRANS"],
        "ownership": ["DIRECT_INDIRECT_OWNERSHIP"], "security": ["SECURITY_TITLE"],
    },
}
REQUIRED_COLS = {
    "FOOTNOTES": ["accession", "fn_id", "fn_text"],
    "SUBMISSION": ["accession", "filing_date", "doc_type", "issuer_cik"],
    "REPORTINGOWNER": ["accession", "owner_cik", "relationship"],
    "NONDERIV_TRANS": ["accession", "date", "code", "shares", "price", "post"],
}


class DatasetFormatError(ValueError):
    pass


def _norm_date(s):
    s = (s or "").strip()
    for fmt in ("%d-%b-%Y", "%Y-%m-%d", "%Y%m%d", "%m/%d/%Y"):
        try:
            return dt.datetime.strptime(s.upper() if "%b" in fmt else s, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def _num(s):
    try:
        x = float((s or "").replace(",", ""))
        return x if x == x else None
    except ValueError:
        return None


def _tsv(zf, table):
    names = {n.upper(): n for n in zf.namelist()}
    want = table + ".TSV"
    if want not in names:
        raise DatasetFormatError("zip has no %s" % want)
    info = zf.getinfo(names[want])
    if info.file_size > 2_000_000_000:
        raise DatasetFormatError("table too large")
    f = io.TextIOWrapper(zf.open(names[want]), encoding="utf-8", errors="replace", newline="")
    rd = csv.reader(f, delimiter="\t")
    header = next(rd, None)
    if not header:
        raise DatasetFormatError("%s is empty" % table)
    up = [h.strip().upper() for h in header]
    idx = {}
    for key, aliases in TABLE_ALIASES[table].items():
        for a in aliases:
            if a in up:
                idx[key] = up.index(a)
                break
    miss = [k for k in REQUIRED_COLS[table] if k not in idx]
    if miss:
        raise DatasetFormatError("%s is missing columns for: %s (header read: %d columns)" % (table, ", ".join(miss), len(up)))
    for row in rd:
        if len(row) < len(up):
            row = row + [""] * (len(up) - len(row))
        yield {k: row[i].strip() for k, i in idx.items()}


def _owner_flags(rel):
    r = (rel or "").lower().replace(" ", "")
    return {"is_director": "director" in r, "is_officer": "officer" in r, "is_ten_pct": "tenpercent" in r or "10percent" in r or "10%" in r,
            "is_other": "other" in r}


def filings_from_dataset_zip(zip_bytes, source_url, fetched_utc=None, only_filing_between=None):
    """Returns (filings, skips). Only Form 4 and 4/A with at least one non-derivative P row are built (the rest are counted)."""
    skips = []
    try:
        zf = zipfile.ZipFile(io.BytesIO(zip_bytes))
    except zipfile.BadZipFile:
        raise DatasetFormatError("not a zip file")
    sub = {}
    other_forms = 0
    for r in _tsv(zf, "SUBMISSION"):
        if r["doc_type"] not in ("4", "4/A"):
            other_forms += 1
            continue
        fd = _norm_date(r["filing_date"])
        if only_filing_between and fd and not (only_filing_between[0] <= fd <= only_filing_between[1]):
            continue
        sub[r["accession"]] = r
    txns = {}
    for r in _tsv(zf, "NONDERIV_TRANS"):
        if r["accession"] in sub:
            txns.setdefault(r["accession"], []).append(r)
    fnotes, fn_ok = {}, False
    if any(n.upper() == "FOOTNOTES.TSV" for n in zf.namelist()):
        try:
            for r in _tsv(zf, "FOOTNOTES"):
                if r["accession"] in sub:
                    fnotes.setdefault(r["accession"], {})[r["fn_id"]] = (r.get("fn_text") or "")[:2000]
            fn_ok = True
        except DatasetFormatError:
            fn_ok = False       # header not as expected (NOT VERIFIED layout): footnotes stay unreadable, which fails the offering screen
    owners = {}
    for r in _tsv(zf, "REPORTINGOWNER"):
        if r["accession"] in sub:
            owners.setdefault(r["accession"], []).append(r)
    out = []
    for acc, s in sub.items():
        if not owners.get(acc):
            skips.append({"accession": acc, "reason": "no_reporting_owner_rows", "source_url": source_url})
            continue
        ow = []
        for o in owners[acc]:
            fl = _owner_flags(o["relationship"])
            ow.append(dict({"cik": (o["owner_cik"].lstrip("0") or "0"), "name": o.get("owner_name", ""), "officer_title": o.get("title", ""),
                            "other_text": o.get("other_text", ""), "has_relationship_block": bool(o["relationship"])}, **fl))
        tx = [{"code": t["code"] or "?", "date": _norm_date(t["date"]), "shares": _num(t["shares"]), "price": _num(t["price"]),
               "acq_disp": t.get("acq_disp") or None, "post_shares": _num(t["post"]), "ownership": t.get("ownership"),
               "security": t.get("security")} for t in txns.get(acc, [])]
        a10 = s.get("aff10b5")
        out.append({"accession": acc, "form_type": s["doc_type"], "filing_date": _norm_date(s["filing_date"]), "accepted_utc": None,
                    "source_url": source_url, "period": _norm_date(s.get("period")), "rule_10b5_1": (a10.lower() in ("1", "true", "y")) if a10 else None,
                    "issuer_cik": s["issuer_cik"].lstrip("0") or "0", "issuer_name": s.get("issuer_name", ""),
                    "ticker": (s.get("ticker") or "").upper() or None, "sic": None, "owners": ow, "txns": tx, "dropped_derivative_rows": 0,
                    "footnotes": fnotes.get(acc, {}) if fn_ok else None, "footnotes_readable": bool(fn_ok)})
    return out, skips, {"other_form_types_ignored": other_forms, "fetched_utc": fetched_utc}


IDX_LINE = re.compile(r"^(4|4/A)\s{2,}(.+?)\s{2,}(\d+)\s+(\d{8}|\d{4}-\d{2}-\d{2})\s+(edgar/data/\S+)\s*$")


def parse_daily_index(text):
    """Returns a list of dicts: form_type, company, cik, filing_date, path. One per ACCESSION (a Form 4 is listed once per filer)."""
    seen, out = set(), []
    for line in text.splitlines():
        m = IDX_LINE.match(line.rstrip())
        if not m:
            continue
        path = m.group(5)
        acc = path.rsplit("/", 1)[-1].replace(".txt", "")
        if acc in seen:
            continue
        seen.add(acc)
        d = m.group(4)
        d = "%s-%s-%s" % (d[0:4], d[4:6], d[6:8]) if len(d) == 8 else d
        out.append({"form_type": m.group(1), "company": m.group(2).strip(), "cik": m.group(3), "filing_date": d, "path": path, "accession": acc})
    return out


def daily_index_url(day):
    q = (day.month - 1) // 3 + 1
    return "https://www.sec.gov/Archives/edgar/daily-index/%d/QTR%d/form.%s.idx" % (day.year, q, day.strftime("%Y%m%d"))


def submission_url(entry):
    return "https://www.sec.gov/Archives/" + entry["path"]


def collect_live(client, cfg, since, until):
    """Route B. since and until are dates. Returns (filings, skips, urls). Request count is capped by sec.max_filings_per_run."""
    filings, skips, urls = [], [], []
    entries = []
    d = since
    while d <= until:
        if d.weekday() < 5:
            u = daily_index_url(d)
            urls.append(u)
            try:
                got = client.fetch(u)
                entries += parse_daily_index(got.body.decode("utf-8", errors="replace"))
            except Exception as e:
                if type(e).__name__ == "SecStop":
                    raise
                skips.append({"reason": "daily_index_unavailable", "date": d.isoformat(), "detail": type(e).__name__, "source_url": u})
        d += dt.timedelta(days=1)
    budget = cfg["sec"]["max_filings_per_run"]
    for i, e in enumerate(entries):
        if i >= budget:
            skips.append({"accession": e["accession"], "reason": "over_request_budget", "filing_date": e["filing_date"], "issuer_or_filer_cik": e["cik"]})
            continue
        u = submission_url(e)
        try:
            got = client.fetch(u)
            acc_time, xml = form4.from_submission_txt(got.body.decode("utf-8", errors="replace"))
            f = form4.parse_form4(xml, {"accession": e["accession"], "filing_date": e["filing_date"], "accepted_utc": acc_time,
                                        "source_url": u, "form_type": e["form_type"]})
            filings.append(f)
            urls.append(u)
        except form4.Form4Error as fe:
            skips.append({"accession": e["accession"], "reason": "parse_failed:" + fe.code, "filing_date": e["filing_date"], "source_url": u})
        except Exception as ex:
            if type(ex).__name__ == "SecStop":
                raise
            skips.append({"accession": e["accession"], "reason": "fetch_failed:" + type(ex).__name__, "filing_date": e["filing_date"], "source_url": u})
    return filings, skips, urls
