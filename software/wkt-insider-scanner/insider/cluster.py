"""Filings -> purchases -> clusters. Pure functions, no network, no clock.

Amendment rule (HEURISTIC, the XML does not name the filing it amends): a 4/A supersedes an EARLIER filing with the same
issuer CIK, the same set of reporting-owner CIKs and the same period of report, provided they share at least one
transaction date (or either has no rows). Two real separate Forms 4 for the same owners are only superseded if a 4/A
covers them, which is the known limit."""
import datetime as dt
import re
import statistics
from zoneinfo import ZoneInfo

from . import classify, form4

ET = ZoneInfo("America/New_York")


def _d(s):
    return dt.date.fromisoformat(s)


def supersede(filings):
    """Returns (kept, skips). Duplicate accessions are dropped first."""
    skips, seen, uniq = [], set(), []
    for f in filings:
        acc = f.get("accession")
        if acc in seen:
            skips.append({"accession": acc, "reason": "duplicate_accession"})
            continue
        seen.add(acc)
        uniq.append(f)

    def key(f):
        return (f["issuer_cik"], frozenset(o["cik"] for o in f["owners"]), f.get("period"))

    def dates(f):
        return {t["date"] for t in f["txns"] if t["date"]}

    def order(f):
        return (f.get("filing_date") or "", f.get("accepted_utc") or "", f.get("accession") or "")

    groups = {}
    for f in uniq:
        groups.setdefault(key(f), []).append(f)
    dead = {}
    for g in groups.values():
        amends = [f for f in g if f["form_type"] == "4/A"]
        for a in amends:
            for o in g:
                if o is a or order(o) >= order(a):
                    continue
                da, do = dates(a), dates(o)
                if not da or not do or (da & do):
                    dead.setdefault(o["accession"], a["accession"])
    kept = []
    for f in uniq:
        if f["accession"] in dead:
            skips.append({"accession": f["accession"], "reason": "superseded_by_4A", "superseded_by": dead[f["accession"]],
                          "issuer_cik": f["issuer_cik"], "ticker": f.get("ticker")})
        else:
            kept.append(f)
    return kept, skips


def to_purchases(filings, cfg):
    """One purchase record per kept P row. Filings with no P rows go to the skip list with the dropped counts."""
    kept_codes = cfg["filing"]["transaction_codes_kept"]
    purchases, skips = [], []
    for f in filings:
        rows, dropped = form4.split_rows(f, kept_codes)
        base = {"accession": f["accession"], "form_type": f["form_type"], "issuer_cik": f["issuer_cik"], "ticker": f.get("ticker"),
                "filing_date": f.get("filing_date"), "source_url": f.get("source_url")}
        if not rows:
            skips.append(dict(base, reason="no_open_market_purchase_rows", dropped_rows=dropped))
            continue
        if not f.get("filing_date"):
            skips.append(dict(base, reason="missing_filing_date", dropped_rows=dropped))
            continue
        lim = cfg["cluster"]["max_filing_lag_business_days"]
        late = [r for r in rows if classify.business_lag(r["date"], f["filing_date"]) > lim]
        if late:
            rows = [r for r in rows if r not in late]
            skips.append(dict(base, reason="late_filing_dropped", late_rows=len(late), max_lag_business_days=lim,
                              note="dropped, late: reported more than the limit after the trade date, so nobody could have seen it inside the window"))
            if not rows:
                continue
        if cfg["filing"]["exclude_10b5_1"] and f.get("rule_10b5_1") is True:
            skips.append(dict(base, reason="rule_10b5_1_excluded", rows=len(rows), note="purchase made under a 10b5-1 plan, scheduled not chosen"))
            continue
        if dropped:
            skips.append(dict(base, reason="non_P_rows_dropped", dropped_rows=dropped, note="filing kept, only these rows dropped"))
        owners = {}
        for o in f["owners"]:
            co = dict(classify.classify_owner(o, cfg), cik=o["cik"], name=o["name"])
            co["counts"], co["not_counted_reason"] = classify.count_decision(co, cfg)
            owners[o["cik"]] = co
            if not co["counts"]:
                skips.append(dict(base, reason="owner_not_counted", owner_cik=o["cik"], owner_type=co["type"], detail=co["not_counted_reason"]))
        fund, basis = classify.issuer_fund_like(f.get("issuer_name"), f.get("sic"), cfg)
        if fund and cfg["cluster"]["exclude_fund_issuers"]:
            skips.append(dict(base, reason="issuer_excluded_fund_like", basis=basis, note="closed-end fund, BDC, ETF or trust as issuer (heuristic), purchases not used", rows=len(rows)))
            continue
        fn = f.get("footnotes")
        for r in rows:
            readable = f.get("footnotes_readable") is True and isinstance(fn, dict)
            if readable and any(i not in fn for i in r.get("footnote_ids", [])):
                readable = False                     # a referenced footnote has no text: unreadable
            text = " ".join(fn.values()) if readable else ""
            kw = sorted({k for k in cfg["filing"]["offering_keywords"] if re.search(r"(?<![a-z0-9])" + re.escape(k.lower()) + r"(?![a-z0-9])", text.lower())})
            val = round(r["shares"] * r["price"], 2) if r["price"] is not None else None
            oc = classify.ownership_change(r["shares"], r["price"], r["post_shares"], cfg)
            purchases.append({
                "accession": f["accession"], "form_type": f["form_type"], "filing_date": f["filing_date"],
                "accepted_raw": f.get("accepted_utc"), "source_url": f.get("source_url"),
                "issuer_cik": f["issuer_cik"], "ticker": f.get("ticker"), "issuer_name": f.get("issuer_name"), "sic": f.get("sic"),
                "issuer_fund_like": fund, "issuer_fund_basis": basis,
                "rule_10b5_1": f.get("rule_10b5_1"), "joint_filing": len(f["owners"]) > 1,
                "txn_date": r["date"], "shares": r["shares"], "price": r["price"], "value": val,
                "post_shares": r["post_shares"], "ownership": r.get("ownership"), "change": oc,
                "lag_days": classify.lag_days(r["date"], f["filing_date"]),
                "price_missing": r["price"] is None,
                "fn_keywords": kw, "fn_readable": readable, "offering_unknown": False,
                "owners": owners,
            })
    purchases, s3 = screen_offering(purchases, cfg)
    return purchases, skips + s3


def screen_offering(purchases, cfg):
    """RULING 4. Same issuer, same trade date, same price, at least offering_min_owners distinct counting owners = offering-style group.
    A footnote keyword hit in the group excludes the group (logged with the matched words only, never the text). Footnotes unreadable = the
    group is UNKNOWN, kept but flagged, and any cluster that contains it FAILS (UNKNOWN is FAIL)."""
    need = cfg["filing"]["offering_min_owners"]
    groups = {}
    for i, p in enumerate(purchases):
        if p["price"] is not None:
            groups.setdefault((p["issuer_cik"], p["txn_date"], round(p["price"], 4)), []).append(i)
    drop, skips = set(), []
    for key, idx in sorted(groups.items()):
        owners = set()
        for i in idx:
            owners |= _counted(purchases[i], cfg)
        if len(owners) < need:
            continue
        kws = sorted({k for i in idx for k in purchases[i]["fn_keywords"]})
        if kws:
            drop |= set(idx)
            for acc in sorted({purchases[i]["accession"] for i in idx}):
                skips.append({"accession": acc, "reason": "offering_style_excluded", "issuer_cik": key[0], "txn_date": key[1], "price": key[2],
                              "owners_in_group": len(owners), "matched_words": kws})
        elif not all(purchases[i]["fn_readable"] for i in idx):
            for i in idx:
                purchases[i]["offering_unknown"] = True
            for acc in sorted({purchases[i]["accession"] for i in idx}):
                skips.append({"accession": acc, "reason": "offering_screen_unknown", "issuer_cik": key[0], "txn_date": key[1], "price": key[2],
                              "owners_in_group": len(owners), "note": "same-day same-price group and the footnotes could not be read: UNKNOWN, any cluster holding it FAILS"})
    return [p for i, p in enumerate(purchases) if i not in drop], skips


def _counted(p, cfg):
    """Owner CIKs of a purchase that count toward the distinct total."""
    return {c for c, o in p["owners"].items() if o["counts"]}


def _distinct(ps, cfg):
    s = set()
    for p in ps:
        s |= _counted(p, cfg)
    return s


def _windows(ps, cfg):
    """For each distinct transaction date e: purchases dated in [e - (N-1), e]. Returns list of (end_date, members)."""
    n = cfg["cluster"]["window_days"]
    ends = sorted({_d(p["txn_date"]) for p in ps})
    out = []
    for e in ends:
        lo = e - dt.timedelta(days=n - 1)
        out.append((e, [p for p in ps if lo <= _d(p["txn_date"]) <= e]))
    return out


def accept_instant(p, cfg):
    """(aware datetime in ET, basis). basis is 'time' when the filing carries a usable acceptance time, else 'date_only' and the
    instant is the END of the filing date (so nothing can be bought on that day). The raw time zone is NOT VERIFIED (timing.accepted_tz)."""
    fd = _d(p["filing_date"])
    raw = p.get("accepted_raw")
    if raw:
        try:
            naive = dt.datetime.fromisoformat(str(raw)[:19])
            if fd - dt.timedelta(days=4) <= naive.date() <= fd:
                return naive.replace(tzinfo=ZoneInfo(cfg["timing"]["accepted_tz"])).astimezone(ET), "time"
        except ValueError:
            pass
    return dt.datetime.combine(fd, dt.time(23, 59, 59), tzinfo=ET), "date_only"


def _signal(members, cfg):
    """RULING 1. The cluster exists only at the acceptance instant of the filing that brings the distinct-insider count to the minimum,
    counting only rows already accepted by then (amendment rows count from their own instant). Returns a dict or None."""
    need = cfg["cluster"]["min_insiders"]
    acc = {id(p): accept_instant(p, cfg) for p in members}
    for t in sorted({a[0] for a in acc.values()}):
        seen = [p for p in members if acc[id(p)][0] <= t]
        for _, w in _windows(seen, cfg):
            if len(_distinct(w, cfg)) >= need:
                completing = [p for p in seen if acc[id(p)][0] == t]
                return {"instant_et": t.isoformat(), "date": t.date().isoformat(),
                        "basis": "time" if any(acc[id(p)][1] == "time" for p in completing) else "date_only",
                        "completing_accessions": sorted({p["accession"] for p in completing}),
                        "contributing_accessions": sorted({p["accession"] for p in w})}
    return None


def find_clusters(purchases, cfg):
    need, watch, n = cfg["cluster"]["min_insiders"], cfg["cluster"]["watch_min_insiders"], cfg["cluster"]["window_days"]
    by_issuer = {}
    for p in purchases:
        if _counted(p, cfg):           # a purchase with no counting owner (10 percent owner only, entity) is logged elsewhere and never joins a cluster
            by_issuer.setdefault(p["issuer_cik"], []).append(p)
    out = []
    for icik, ps in sorted(by_issuer.items()):
        ps = sorted(ps, key=lambda p: (p["txn_date"], p["accession"]))
        wins = _windows(ps, cfg)
        used = set()
        for tier, lo, hi in (("COUNTED", need, 10 ** 6), ("WATCH", watch, need - 1)):
            qual = [(e, w) for e, w in wins if lo <= len(_distinct(w, cfg)) <= hi]
            groups, cur, last_end = [], [], None
            for e, w in qual:
                if cur and (e - last_end).days > n - 1:
                    groups.append(cur)
                    cur = []
                cur.append((e, w))
                last_end = e
            if cur:
                groups.append(cur)
            for g in groups:
                members, seen = [], set()
                for _, w in g:
                    for p in w:
                        k = id(p)
                        if k not in seen:
                            seen.add(k)
                            members.append(p)
                if tier == "WATCH" and any(id(p) in used for p in members):
                    continue
                if tier == "COUNTED":
                    used |= {id(p) for p in members}
                members.sort(key=lambda p: (p["txn_date"], p["accession"]))
                out.append(_record(tier, icik, members, cfg))
    return out


def _record(tier, icik, members, cfg):
    owners = {}
    for p in members:
        for c, o in p["owners"].items():
            e = owners.setdefault(c, {"cik": c, "name": o["name"], "type": o["type"], "roles": o["roles"],
                                       "officer_title": o["officer_title"], "is_ceo": o["is_ceo"], "is_cfo": o["is_cfo"],
                                       "sponsor_or_fund_affiliate": o["sponsor_or_fund_affiliate"],
                                       "sponsor_basis": o["sponsor_basis"], "counts": o["counts"], "not_counted_reason": o["not_counted_reason"],
                                       "n_purchases": 0, "total_value": 0.0})
            e["n_purchases"] += 1
            e["total_value"] = round(e["total_value"] + (p["value"] or 0.0), 2)
    counted = _distinct(members, cfg)
    unknown = sorted(c for c, o in owners.items() if o["type"] == "UNKNOWN" and o["counts"])
    status = tier
    if tier == "COUNTED" and unknown:
        status = "FAIL_UNKNOWN_TYPE"
    elif tier == "COUNTED" and any(p["offering_unknown"] for p in members):
        status = "FAIL_UNKNOWN_FOOTNOTE"
    kinds = {o["type"] for o in owners.values()}
    if any(o["sponsor_or_fund_affiliate"] for o in owners.values()) or members[0]["issuer_fund_like"]:
        ctype = "sponsor_or_fund"
    elif "ten_percent_owner" in kinds:
        ctype = "ten_percent_involved"
    elif any(o["is_ceo"] or o["is_cfo"] for o in owners.values()):
        ctype = "ceo_cfo_involved"
    elif kinds <= {"officer", "director"} and kinds:
        ctype = "officers_directors"
    else:
        ctype = "other_or_unknown"
    lags = [p["lag_days"] for p in members if p["lag_days"] is not None]
    sig = _signal(members, cfg) if tier == "COUNTED" else None
    signal = sig["date"] if sig else None
    accessions = sorted({p["accession"] for p in members})
    first = members[0]["txn_date"]
    comp = set(sig["completing_accessions"]) if sig else set()
    ticker_sig = next((p["ticker"] for p in members if p["accession"] in comp and p["ticker"]), None) or next((p["ticker"] for p in members if p["ticker"]), None)
    flags = []
    if len({p["ticker"] for p in members if p["ticker"]}) > 1:
        flags.append("ticker_changed_in_cluster")
    if len(accessions) < len(counted):
        flags.append("joint_filing_inflated: fewer filings than insiders")
    if any(p["rule_10b5_1"] is None for p in members):
        flags.append("rule_10b5_1_unknown(flag absent in the source, not excluded)")
    if any(p["change"]["uninformative"] for p in members):
        flags.append("has_uninformative_pct_change")
    if any(p["price_missing"] for p in members):
        flags.append("has_missing_price")
    if members[0]["issuer_fund_like"]:
        flags.append("issuer_fund_like(%s, heuristic)" % members[0]["issuer_fund_basis"])
    if any(p["form_type"] == "4/A" for p in members):
        flags.append("includes_amended_filing")
    return {
        "cluster_id": "%s-%s-%s" % ("C" if tier == "COUNTED" else "W", icik, first),
        "status": status, "counted": status == "COUNTED",
        "issuer": {"cik": icik, "ticker": ticker_sig, "ticker_basis": "ticker on the filing that completed the cluster (as of signal), matched by issuer CIK",
                   "tickers_seen": sorted({p["ticker"] for p in members if p["ticker"]}), "name": members[0]["issuer_name"], "sic": members[0]["sic"],
                   "fund_like": members[0]["issuer_fund_like"], "fund_basis": members[0]["issuer_fund_basis"]},
        "window": {"first_txn_date": first, "last_txn_date": members[-1]["txn_date"], "window_days_config": cfg["cluster"]["window_days"]},
        "n_distinct_insiders": len(counted), "n_distinct_insiders_all": len(owners), "unknown_type_ciks": unknown,
        "cluster_type": ctype, "signal": sig, "signal_filing_date": signal,
        "last_filing_date": max(p["filing_date"] for p in members),
        "lag_days": {"min": min(lags), "median": statistics.median(lags), "max": max(lags)} if lags else None,
        "total_value": round(sum(p["value"] or 0.0 for p in members), 2),
        "insiders": sorted(owners.values(), key=lambda o: o["cik"]),
        "purchases": [{"accession": p["accession"], "form_type": p["form_type"], "owner_ciks": sorted(p["owners"]),
                       "txn_date": p["txn_date"], "filing_date": p["filing_date"], "accepted_raw": p["accepted_raw"],
                       "lag_days": p["lag_days"], "shares": p["shares"], "price": p["price"], "value": p["value"],
                       "post_shares": p["post_shares"], "pct_change": p["change"]["pct_change"],
                       "pct_change_uninformative": p["change"]["uninformative"], "rule_10b5_1": p["rule_10b5_1"],
                       "joint_filing": p["joint_filing"], "source_url": p["source_url"],
                       "accepted_et": accept_instant(p, cfg)[0].isoformat(), "accept_basis": accept_instant(p, cfg)[1]} for p in members],
        "flags": flags, "accessions": accessions,
        "source_urls": sorted({p["source_url"] for p in members if p["source_url"]}),
        "heuristics": ["owner entity detection by name words", "issuer fund detection by SIC or name words", "4/A supersede matching by issuer, owners and period"],
    }
