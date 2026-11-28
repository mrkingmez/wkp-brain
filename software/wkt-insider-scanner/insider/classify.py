"""Insider type, sponsor/fund flags, ownership-change math. Heuristics are labeled as such in the output."""
import re


def _words(name):
    return set(re.findall(r"[a-z0-9\.]+", (name or "").lower()))


def is_entity_name(name, cfg):
    """HEURISTIC: an owner name containing a company-style word is treated as an entity, not a person."""
    ent = {w.lower() for w in cfg["classify"]["entity_words"]}
    ws = _words(name)
    ws |= {w.strip(".") for w in ws}
    return bool(ws & ent)


def classify_owner(owner, cfg):
    """Type from the filing's relationship fields. officer > director > ten_percent_owner > other. No role flag at all = UNKNOWN (counts as FAIL)."""
    c = cfg["classify"]
    roles = []
    if owner.get("is_officer"):
        roles.append("officer")
    if owner.get("is_director"):
        roles.append("director")
    if owner.get("is_ten_pct"):
        roles.append("ten_percent_owner")
    if owner.get("is_other"):
        roles.append("other")
    title = owner.get("officer_title") or ""
    ceo = bool(re.search(c["ceo_regex"], title, re.I)) if owner.get("is_officer") else False
    cfo = bool(re.search(c["cfo_regex"], title, re.I)) if owner.get("is_officer") else False
    entity = is_entity_name(owner.get("name"), cfg)
    return {"type": roles[0] if roles else "UNKNOWN", "roles": roles, "officer_title": title, "is_ceo": ceo, "is_cfo": cfo,
            "entity_name_heuristic": entity,
            "sponsor_or_fund_affiliate": bool(entity),
            "sponsor_basis": "heuristic: owner name looks like an entity" if entity else None}


def issuer_fund_like(name, sic, cfg):
    """HEURISTIC, labeled. SIC wins when the source gives one."""
    c = cfg["classify"]
    if sic and str(sic) in {str(x) for x in c["fund_sic_codes"]}:
        return True, "sic"
    ws = _words(name)
    if ws & {w.lower() for w in c["fund_issuer_words"]}:
        return True, "name_heuristic"
    low = " ".join((name or "").lower().split())
    if any(ph.lower() in low for ph in c.get("fund_issuer_phrases", [])):
        return True, "name_heuristic"
    return False, None


def count_decision(owner, cfg):
    """RULING 3. (counts, reason). An owner counts toward the minimum only if officer or director is ticked and the name does not look like an entity.
    UNKNOWN type (no box ticked) is let through as 'pending' so the cluster can FAIL on it, never pass on it. Reasons are logged, never silent."""
    cl = cfg["cluster"]
    if cl["exclude_entity_owners"] and owner["entity_name_heuristic"]:
        return False, "entity_filer(name heuristic)"
    if owner["type"] == "UNKNOWN":
        return True, "UNKNOWN_type(fails the cluster)"
    if not (set(owner["roles"]) & set(cl["count_roles"])):
        return False, "not_officer_or_director(%s only)" % owner["type"]
    return True, None


def ownership_change(shares, price, post_shares, cfg):
    """Percent change in holdings from this buy, and whether it is uninformative (over the limit on a tiny base)."""
    c = cfg["classify"]
    if post_shares is None or shares is None:
        return {"pre_shares": None, "pct_change": None, "uninformative": None, "why": "post-transaction holdings missing"}
    pre = post_shares - shares
    if pre <= 0:
        return {"pre_shares": max(pre, 0.0), "pct_change": None, "uninformative": True, "why": "new position (no prior holdings)"}
    pct = shares / pre * 100.0
    tiny = price is not None and pre * price < c["tiny_base_usd"]
    unin = bool(pct > c["pct_change_uninformative_over"] and tiny)
    return {"pre_shares": pre, "pct_change": round(pct, 2), "uninformative": unin,
            "why": "over %s percent on a base under $%s" % (c["pct_change_uninformative_over"], c["tiny_base_usd"]) if unin else None}


def lag_days(txn_date, filing_date):
    import datetime as dt
    if not txn_date or not filing_date:
        return None
    return (dt.date.fromisoformat(filing_date) - dt.date.fromisoformat(txn_date)).days


def business_lag(txn_date, filing_date):
    """Weekdays from txn date to filing date (Mon to Fri, no holiday calendar: a holiday makes the lag read one day long, never short)."""
    import datetime as dt
    if not txn_date or not filing_date:
        return None
    a, b = dt.date.fromisoformat(txn_date), dt.date.fromisoformat(filing_date)
    if b < a:
        return 0
    n, d = 0, a
    while d < b:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n
