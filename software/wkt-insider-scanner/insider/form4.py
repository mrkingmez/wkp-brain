"""Form 4 XML parser (ownershipDocument). Pure function, no network.
Safety: a document with a DOCTYPE or ENTITY declaration is refused before parsing (no entity expansion, no external
entities), and size is capped. Element names follow the SEC ownership XML layout; the 10b5-1 field name aff10b5One is
BELIEVED (data-sourcing could not open the spec), so a missing field is recorded as None, never as False."""
import datetime as dt
import re
import xml.etree.ElementTree as ET

MAX_BYTES = 5_000_000


class Form4Error(ValueError):
    """Carries a short reason code for the skip log."""

    def __init__(self, code, detail=""):
        super().__init__(code + (": " + detail if detail else ""))
        self.code = code


def _text(el, path):
    if el is None:
        return None
    n = el.find(path)
    if n is None or n.text is None:
        return None
    t = n.text.strip()
    return t or None


def _val(el, path):
    """<path><value>x</value></path>, the SEC style, or <path>x</path>."""
    if el is None:
        return None
    n = el.find(path)
    if n is None:
        return None
    v = n.find("value")
    t = (v.text if v is not None else n.text)
    t = t.strip() if t else None
    return t or None


def _bool(s):
    if s is None:
        return None
    return s.strip().lower() in ("1", "true", "y", "yes")


def _num(s):
    if s is None:
        return None
    try:
        x = float(s.replace(",", ""))
    except ValueError:
        return None
    return x if x == x and x not in (float("inf"), float("-inf")) else None


def _date(s):
    if not s:
        return None
    try:
        return dt.date.fromisoformat(s.strip()[:10]).isoformat()
    except ValueError:
        return None


def parse_form4(xml_text, meta=None):
    """Returns a filing dict. Raises Form4Error(code) on anything unusable. meta may carry accession, filing_date,
    accepted_utc, source_url, form_type (used when the XML omits them)."""
    meta = meta or {}
    if isinstance(xml_text, bytes):
        if len(xml_text) > MAX_BYTES:
            raise Form4Error("too_large")
        try:
            xml_text = xml_text.decode("utf-8")
        except UnicodeDecodeError:
            raise Form4Error("bad_encoding")
    if len(xml_text) > MAX_BYTES:
        raise Form4Error("too_large")
    low = xml_text.lower()
    if "<!doctype" in low or "<!entity" in low:
        raise Form4Error("forbidden_doctype", "DOCTYPE or ENTITY declaration refused")
    try:
        root = ET.fromstring(xml_text.strip())
    except ET.ParseError as e:
        raise Form4Error("xml_parse_error", type(e).__name__)
    if root.tag != "ownershipDocument":
        raise Form4Error("not_ownership_document", root.tag[:40])
    doc_type = _text(root, "documentType") or meta.get("form_type")
    if doc_type not in ("4", "4/A"):
        raise Form4Error("not_form_4", str(doc_type)[:20])
    issuer = root.find("issuer")
    icik = _text(issuer, "issuerCik")
    if not icik or not icik.isdigit():
        raise Form4Error("missing_issuer_cik")
    owners = []
    for ro in root.findall("reportingOwner"):
        ocik = _text(ro, "reportingOwnerId/rptOwnerCik")
        if not ocik or not ocik.isdigit():
            raise Form4Error("missing_owner_cik")
        rel = ro.find("reportingOwnerRelationship")
        owners.append({
            "cik": ocik.lstrip("0") or "0",
            "name": _text(ro, "reportingOwnerId/rptOwnerName") or "",
            "is_director": _bool(_text(rel, "isDirector")),
            "is_officer": _bool(_text(rel, "isOfficer")),
            "is_ten_pct": _bool(_text(rel, "isTenPercentOwner")),
            "is_other": _bool(_text(rel, "isOther")),
            "officer_title": _text(rel, "officerTitle") or "",
            "other_text": _text(rel, "otherText") or "",
            "has_relationship_block": rel is not None,
        })
    if not owners:
        raise Form4Error("no_reporting_owner")
    txns, dropped = [], {}
    tbl = root.find("nonDerivativeTable")
    for t in (tbl.findall("nonDerivativeTransaction") if tbl is not None else []):
        code = _text(t, "transactionCoding/transactionCode") or "?"
        txns.append({
            "code": code,
            "date": _date(_val(t, "transactionDate")),
            "shares": _num(_val(t, "transactionAmounts/transactionShares")),
            "price": _num(_val(t, "transactionAmounts/transactionPricePerShare")),
            "acq_disp": _val(t, "transactionAmounts/transactionAcquiredDisposedCode"),
            "post_shares": _num(_val(t, "postTransactionAmounts/sharesOwnedFollowingTransaction")),
            "ownership": _val(t, "ownershipNature/directOrIndirectOwnership"),
            "security": _val(t, "securityTitle"),
            "footnote_ids": sorted({(e.get("id") or "").strip() for e in t.iter("footnoteId") if (e.get("id") or "").strip()}),
        })
    # Footnote text is untrusted free text. It is only ever matched against a fixed keyword list (cluster.to_purchases), never executed, never copied into outputs.
    fnotes = {}
    fn_root = root.find("footnotes")
    for e in (fn_root.findall("footnote") if fn_root is not None else [])[:60]:
        fid = (e.get("id") or "").strip()
        if fid:
            fnotes[fid] = ("".join(e.itertext()) or "")[:2000]
    deriv_rows = 0
    dtbl = root.find("derivativeTable")
    if dtbl is not None:
        deriv_rows = len(dtbl.findall("derivativeTransaction"))
    if deriv_rows:
        dropped["derivative"] = deriv_rows
    return {
        "accession": meta.get("accession"),
        "form_type": doc_type,
        "filing_date": _date(meta.get("filing_date")),
        "accepted_utc": meta.get("accepted_utc"),
        "source_url": meta.get("source_url"),
        "period": _date(_text(root, "periodOfReport")),
        "rule_10b5_1": _bool(_text(root, "aff10b5One")),
        "issuer_cik": icik.lstrip("0") or "0",
        "issuer_name": _text(issuer, "issuerName") or "",
        "ticker": (_text(issuer, "issuerTradingSymbol") or "").upper() or None,
        "sic": meta.get("sic"),
        "owners": owners,
        "txns": txns,
        "footnotes": fnotes, "footnotes_readable": True,     # XML route: parsed. The bulk-data route sets this False unless a footnote table is present
        "dropped_derivative_rows": deriv_rows,
    }


def split_rows(filing, kept_codes):
    """Return (purchase_rows, dropped_counts). A purchase must be code in kept_codes, acquired (A), with a date and
    positive shares. Anything else is counted by its code, never silently lost."""
    rows, dropped = [], {}
    if filing.get("dropped_derivative_rows"):
        dropped["derivative"] = filing["dropped_derivative_rows"]
    for t in filing["txns"]:
        if t["code"] not in kept_codes:
            dropped[t["code"]] = dropped.get(t["code"], 0) + 1
            continue
        if t["acq_disp"] not in (None, "A") or not t["date"] or not t["shares"] or t["shares"] <= 0:
            dropped["P_unusable"] = dropped.get("P_unusable", 0) + 1
            continue
        rows.append(t)
    return rows, dropped


SGML_ACCEPT = re.compile(r"<ACCEPTANCE-DATETIME>\s*(\d{14})")
SGML_XML = re.compile(r"<XML>\s*(.*?)\s*</XML>", re.S | re.I)


def from_submission_txt(text):
    """The EDGAR .txt full submission holds the header (acceptance time) and the XML. Returns (accepted_utc_iso, xml_text).
    The time zone of the header value is NOT VERIFIED, so it is kept as written (accepted_raw) and only the filing DATE is used for entry."""
    m = SGML_ACCEPT.search(text)
    acc = None
    if m:
        s = m.group(1)
        acc = "%s-%s-%sT%s:%s:%s" % (s[0:4], s[4:6], s[6:8], s[8:10], s[10:12], s[12:14])
    x = SGML_XML.search(text)
    if not x:
        raise Form4Error("no_xml_in_submission")
    body = x.group(1)
    if "<?xml" in body[:100]:
        body = body[body.index("?>") + 2:]
    return acc, body
