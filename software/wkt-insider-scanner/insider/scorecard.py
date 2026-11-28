"""insider-scorecard.md writer. Reads forward-returns.jsonl. Only lines under the CURRENT config hash are counted
(a changed config restarts the counts); the latest line per cluster wins. Plain statistics, no model."""
import statistics

ILLIQUID = ("illiquid_price", "illiquid_volume")


def latest_per_cluster(records, chash):
    cur, old = {}, 0
    for r in records:
        if r.get("config_hash") != chash:
            old += 1
            continue
        cur[r["cluster_id"]] = r
    return list(cur.values()), old


def _stats(vals):
    if not vals:
        return None
    return {"n": len(vals), "median": statistics.median(vals), "mean": sum(vals) / len(vals),
            "hit": sum(1 for v in vals if v > 0) / len(vals)}


def collect(recs, ledger, h, bps, key=None, only=None, drop_illiquid=False):
    vals, pend, unk = [], 0, 0
    for r in recs:
        if r.get("excluded"):
            continue
        if only and not only(r):
            continue
        if drop_illiquid and any(t in ILLIQUID for t in r["tags"]):
            continue
        hz = r["ledgers"][ledger]["horizons"].get(str(h), {})
        s = hz.get("state")
        if s == "OK":
            vals.append(hz["excess"][str(bps)])
        elif s == "PENDING":
            pend += 1
        else:
            unk += 1
    return _stats(vals), pend, unk


def coverage(recs, cfg):
    """RULING 2, line one of the scorecard: how many scored clusters have no usable price history. Never silent."""
    excl = [r for r in recs if r.get("excluded")]
    recs = [r for r in recs if not r.get("excluded")]
    n = len(recs)
    miss = sum(1 for r in recs if r.get("data_status") == "MISSING")
    ended = sum(1 for r in recs if r.get("data_status") == "DELISTED_OR_ENDED")
    lim = cfg["forward"]["missing_best_case_over_pct"]
    pct = (100.0 * miss / n) if n else 0.0
    line = "Price coverage: %d of %d scored clusters MISSING (no usable bars, %.1f%%), %d DELISTED_OR_ENDED (marked to the last print)." % (miss, n, pct, ended)
    if excl:
        line += " Excluded at scoring (new listing or listing age UNKNOWN), not in any figure below: %d." % len(excl)
    if n and pct > lim:
        line += " **BEST CASE, SURVIVOR-BIASED: more than %s%% of clusters are missing, so every result below is an upper bound only.**" % lim
    return line


def _usd(x, usd):
    return "%s$%.2f" % ("-" if x < 0 else "+", abs(x) * usd)


def _fmt(st, usd=15):
    """RULING 9: every percent has its dollar figure next to it, at a position of usd dollars."""
    if not st:
        return "no data"
    return "n=%d, median %+.2f%% (%s on $%g), mean %+.2f%% (%s), hit rate %.0f%%" % (
        st["n"], st["median"] * 100, _usd(st["median"], usd), usd, st["mean"] * 100, _usd(st["mean"], usd), st["hit"] * 100)


def header_lines(cfg):
    f = cfg["forward"]
    return ["**%d counted clusters can KILL this signal. Nothing this year can PROMOTE it from forward data alone** (the effect is small next to the noise: a forward sample this size can show no edge, never prove one)." % f["min_counted_for_verdict"],
            "A pass here is a request to Zac for a locked-rule change. It is never adopted automatically. This signal has NO sizing and NO trade authority and does not feed the stock watcher.",
            "Dollar figures sit next to every percent, at a $%g position (25 percent of the $60 account). A real edge at this size is a learning result, not a funding source." % f["position_usd"], ""]


def primary_values(recs, cfg):
    """RULING 7. The one pre-registered test: zac ledger, one horizon, net of cost, excess against both benchmarks.
    UNFILLED clusters cannot be bought, so they have no return, and they are counted in the tradability figures instead (ruling 5)."""
    pt = cfg["primary_test"]
    ledger, h = pt["ledger"], str(pt["horizon_trading_days"])
    benches = list(cfg["forward"]["benchmarks"])
    out = {"vals": {b: [] for b in benches}, "pending": 0, "unknown": 0, "unfilled": 0, "fill_unknown": 0, "filled": 0, "bench_missing": 0, "costs": [], "used": []}
    for r in recs:
        if r.get("excluded"):
            continue
        L = r["ledgers"].get(ledger, {})
        fs = (L.get("fill") or {}).get("status")
        if fs == "UNFILLED":
            out["unfilled"] += 1
            continue
        hz = L.get("horizons", {}).get(h, {})
        st = hz.get("state")
        if st == "PENDING":
            out["pending"] += 1
        elif st == "OK":
            ex = hz.get("excess_cost_by_bench") or {}
            if all(b in ex for b in benches):
                for b in benches:
                    out["vals"][b].append(ex[b])
                out["used"].append(r)
                out["costs"].append((fs, hz.get("round_trip_cost_bps")))
                out["filled" if fs == "FILLED" else "fill_unknown"] += 1
            else:
                out["bench_missing"] += 1
        else:
            out["unknown"] += 1
    return out


def primary_lines(recs, cfg):
    pt = cfg["primary_test"]
    f = cfg["forward"]
    pv = primary_values(recs, cfg)
    n = len(pv["used"])
    L = ["## PRIMARY TEST (pre-registered %s, frozen in config.yaml, the only result that can mean anything)" % pt["registered_on"], "",
         "- Population: officer and director clusters as the cluster and filing rules define them. Ledger: Zac-can-act. Horizon: %d trading days (hold from the entry open to the close of day %d)." % (pt["horizon_trading_days"], pt["horizon_trading_days"]),
         "- Metric: mean excess return net of cost (the larger of %s bps and the measured half spread, each side) against SPY and against IWM. Pass condition: positive against BOTH." % f["cost_floor_bps"],
         "- Clusters in the figures: %d (FILLED %d, FILL_UNKNOWN %d). Not in the figures: UNFILLED %d, pending %d, unknown or missing price %d, a benchmark bar missing %d." % (
             n, pv["filled"], pv["fill_unknown"], pv["unfilled"], pv["pending"], pv["unknown"], pv["bench_missing"]), ""]
    for b in f["benchmarks"]:
        st = _stats(pv["vals"][b])
        L.append("- Excess vs %s: %s" % (b, _fmt(st, f["position_usd"])))
    L.append("")
    means = [(_stats(pv["vals"][b]) or {}).get("mean") for b in f["benchmarks"]]
    if n < f["min_counted_for_verdict"] or any(m is None for m in means):
        L.append("Forward leg: NOT ENOUGH CLUSTERS (%d of %d needed). Nothing here is evidence yet." % (n, f["min_counted_for_verdict"]))
    elif all(m > 0 for m in means):
        L.append("Forward leg: the pass condition is MET on this sample. That is necessary, not sufficient: it needs the point-in-time backfill too, and it is a request to Zac for a locked-rule change, never adopted automatically.")
    else:
        L.append("Forward leg: the pass condition is NOT met (mean excess is zero or negative against at least one benchmark).")
    L.append("")
    return L


def _median(v):
    return statistics.median(v) if v else None


def lookahead_records(recs):
    """K6, automated half 1: a scored entry whose open (09:30 ET on the entry date) is not after the signal instant. Returns a list of cluster ids."""
    import datetime as dt
    from zoneinfo import ZoneInfo
    et = ZoneInfo("America/New_York")
    bad = []
    for r in recs:
        sig = r.get("signal")
        if not isinstance(sig, dict) or not sig.get("instant_et"):
            continue
        t = dt.datetime.fromisoformat(sig["instant_et"])
        for L in r.get("ledgers", {}).values():
            ed = L.get("entry_date")
            if ed and dt.datetime.combine(dt.date.fromisoformat(ed), dt.time(9, 30), tzinfo=et) <= t:
                bad.append(r["cluster_id"])
                break
    return bad


def lookahead_clusters(cluster_records, chash):
    """K6, automated half 2: a counted cluster whose contributing filings were accepted after its signal instant. Returns cluster ids."""
    import datetime as dt
    bad = []
    for c in cluster_records:
        if c.get("config_hash") != chash or not c.get("counted") or not isinstance(c.get("signal"), dict):
            continue
        t = dt.datetime.fromisoformat(c["signal"]["instant_et"])
        contrib = set(c["signal"].get("contributing_accessions", []))
        if any(p["accession"] in contrib and dt.datetime.fromisoformat(p["accepted_et"]) > t for p in c["purchases"]):
            bad.append(c["cluster_id"])
    return sorted(set(bad))


def kill_lines(recs, cfg, extras):
    """RULING 10. Status of K1 to K7 from the config values. TRIGGERED / NOT TRIGGERED / NOT YET / NOT EVALUABLE, never a guess."""
    import datetime as dt
    kc, f = cfg["kill_criteria"], cfg["forward"]
    extras = extras or {}
    live = [r for r in recs if not r.get("excluded")]
    pv = primary_values(recs, cfg)
    n = len(pv["used"])
    zfill = [((r["ledgers"].get(cfg["primary_test"]["ledger"], {}).get("fill") or {}).get("status")) for r in live]
    rows = []
    # K1
    k = kc["K1"]
    if n < k["at_counted"]:
        rows.append(("K1", "no edge", "NOT YET", "%d of %d clusters in the primary figures" % (n, k["at_counted"])))
    else:
        means = [sum(v) / len(v) for v in pv["vals"].values()]
        meds = [_median(v) for v in pv["vals"].values()]
        mm, md = min(means), min(meds)
        hit = mm <= k["mean_at_or_below"] and md <= k["median_at_or_below"]
        rows.append(("K1", "no edge", "TRIGGERED" if hit else "NOT TRIGGERED", "binding-benchmark mean %+.2f%% (%s), median %+.2f%% (%s), n=%d" % (
            mm * 100, _usd(mm, f["position_usd"]), md * 100, _usd(md, f["position_usd"]), n)))
    # K2
    k = kc["K2"]
    q = [s for s in zfill if s in ("FILLED", "UNFILLED", "FILL_UNKNOWN")]
    uf, fu = q.count("UNFILLED"), q.count("FILL_UNKNOWN")
    if len(q) < k["at_qualifying"]:
        rows.append(("K2", "untradable", "NOT YET", "%d of %d qualifying clusters (UNFILLED %d, FILL_UNKNOWN %d)" % (len(q), k["at_qualifying"], uf, fu)))
    else:
        share, upper = uf / len(q), (uf + fu) / len(q)
        st = "TRIGGERED" if share > k["unfilled_share_over"] else "NOT TRIGGERED"
        note = "unfilled share %.0f%% measured, up to %.0f%% if the %d FILL_UNKNOWN were unfilled" % (share * 100, upper * 100, fu)
        if st == "NOT TRIGGERED" and upper > k["unfilled_share_over"]:
            st, note = "NOT EVALUABLE", note + " (FILL_UNKNOWN could change the answer: intraday first-trade data is needed)"
        rows.append(("K2", "untradable", st, note))
    # K3
    k = kc["K3"]
    filled = [c for fs, c in pv["costs"] if fs == "FILLED" and c is not None]
    if len(filled) < k["at_filled"]:
        why = "%d of %d FILLED clusters" % (len(filled), k["at_filled"])
        if pv["fill_unknown"] and not filled:
            why += "; %d are FILL_UNKNOWN (no intraday first-trade data), so this cannot be checked yet" % pv["fill_unknown"]
        rows.append(("K3", "too expensive", "NOT YET", why))
    else:
        med = _median([c / 1e4 for c in filled])
        rows.append(("K3", "too expensive", "TRIGGERED" if med > k["median_round_trip_cost_over"] else "NOT TRIGGERED", "median round-trip cost %.2f%% (%s on $%g)" % (med * 100, _usd(med, f["position_usd"]).replace("+", ""), f["position_usd"])))
    # K4
    k = kc["K4"]
    first = extras.get("first_counted_date") or (min((r.get("signal_filing_date") for r in live if r.get("signal_filing_date")), default=None))
    today = extras.get("today")
    if not first:
        rows.append(("K4", "too rare", "NOT YET", "no counted cluster yet, the six months have not started"))
    elif not today:
        rows.append(("K4", "too rare", "NOT EVALUABLE", "no run date supplied"))
    else:
        deadline = dt.date.fromisoformat(first) + dt.timedelta(days=round(30.4375 * k["months_after_first_counted_day"]))
        late = dt.date.fromisoformat(today) > deadline
        hit = late and len(live) < k["counted_under"]
        rows.append(("K4", "too rare", "TRIGGERED" if hit else "NOT TRIGGERED", "first counted day %s, deadline %s, counted %d of %d" % (first, deadline.isoformat(), len(live), k["counted_under"])))
    # K5
    rows.append(("K5", "backfill fails", "NOT EVALUABLE", "no backfill has been run (design stub only, docs/BACKTEST-DESIGN.md). No forward run is justified by a backfill yet"
                 if not kc["K5"]["backfill_run"] else "backfill result not wired into the scorecard"))
    # K6
    bad = lookahead_records(recs) + list(extras.get("lookahead_clusters", []))
    rows.append(("K6", "look-ahead found", "TRIGGERED" if bad else "NOT TRIGGERED",
                 ("%d violation(s): all counts void" % len(bad)) if bad else "automated checks clear (every scored entry is after its signal instant, every contributing filing was accepted by the signal time). qa-claims owns the real K6 finding"))
    # K7
    k = kc["K7"]
    rs = extras.get("config_resets")
    if rs is None:
        rows.append(("K7", "tuning", "NOT EVALUABLE", "config history not supplied"))
    else:
        rows.append(("K7", "tuning", "TRIGGERED" if (rs >= k["resets_at_or_over"] and len(live) < k["before_counted"]) else "NOT TRIGGERED", "%d config reset(s) so far, %d counted clusters" % (rs, len(live))))
    L = ["## KILL CRITERIA STATUS (from config.yaml, written before any data)", "", "| Id | Name | Status | Detail |", "|---|---|---|---|"]
    L += ["| %s | %s | %s | %s |" % r for r in rows]
    trig = [r[0] for r in rows if r[2] == "TRIGGERED"]
    L += ["", ("**FORWARD TEST ENDED by %s. trading-researcher logs it in strategies-tried.md as tried and failed, with the reason.**" % ", ".join(trig)) if trig
          else "No kill criterion is triggered. That is not a pass and promotes nothing.", ""]
    return L


def build(records, cfg, chash, counted_cluster_total, watch_total, generated, mode, source_file, extras=None):
    f = cfg["forward"]
    recs, old = latest_per_cluster(records, chash)
    n = len(recs)
    pb = f["pass_haircut_bps"]
    L = ["# WKT insider scanner scorecard", "", coverage(recs, cfg), ""] + header_lines(cfg) + [
         "Generated: %s. Mode: %s. Config hash: %s. Source: %s. Paper research only: this signal has NO sizing and NO trade authority." % (generated, mode, chash, source_file), "",
         "## Counts",
         "- COUNTED clusters scored under this config hash: %d (of which excluded at scoring and in no figure below: %d). Clusters seen but not counted (WATCH tier, 2 insiders): %d. Counted clusters found in the latest clusters file: %d." % (n, sum(1 for r in recs if r.get("excluded")), watch_total, counted_cluster_total),
         "- Forward-return lines from older config hashes, not counted here: %d." % old,
         "- Clusters with a signal at or before the config freeze (%s), recorded as PRE_FREEZE and never counted or scored: %d." % (cfg["freeze"]["counted_signals_from_et"], (extras or {}).get("pre_freeze", 0)), ""]
    if n < f["min_counted_for_verdict"]:
        L += ["**NO VERDICT. Fewer than %d counted clusters (%d). Everything below is plumbing output, not evidence.**" % (f["min_counted_for_verdict"], n), ""]
    L += primary_lines(recs, cfg)
    L += kill_lines(recs, cfg, extras)
    L += ["## Rules used",
          "- Entry: the first trade after the acceptance time of the filing that completed the cluster. With daily bars that is the open of the same day if accepted before the cutoff, else the open of the next trading day (labeled). If the acceptance time is missing, the open of the first trading day after the filing date (labeled). Zac-can-act ledger: %d trading day later (assumption). Never the insider's own price." % f["zac_extra_trading_days"],
          "- Hold h trading days (%s): entry open to the close of day entry + h - 1. Excess = stock net of cost minus the benchmark gross over the same two dates." % ", ".join(str(h) for h in f["horizons"]),
          "- Cost each side: the larger of %s bps and half the measured spread. Without a measured spread the floor is used and the cluster is tagged spread_unmeasured." % f["cost_floor_bps"],
          "- Data: Alpaca IEX daily bars, read-only, feed=iex. IEX volume is thin, so dollar-volume tags are an under-count.",
          "- Separate ledger and config: this scanner has its own folder, config file and hash. It writes nothing to the stock watcher and its flag never enters the watcher score, config, decisions or counts. A pass here is a request to Zac for a locked-rule change, never adopted automatically.", ""]
    L += ["## EXPLORATORY (cannot change a rule or promote anything; a rule from here must be re-tested on clusters accepted after it was proposed)", "",
          "Haircut ladder (bps each side, assumption): %s. Headline column uses %s bps. Excess here is against SPY only." % (", ".join(str(b) for b in f["haircut_bps"]), pb), ""]
    for ledger, title in (("zac", "Zac-can-act ledger, all horizons"), ("main", "Main ledger (first possible entry), all horizons")):
        L += ["### " + title, "", "| Horizon | Excess vs SPY at %s bps (all) | Excluding illiquid-tagged | At 5 bps (all) | Pending | Unknown |" % pb, "|---|---|---|---|---|---|"]
        for h in f["horizons"]:
            a, pend, unk = collect(recs, ledger, h, pb)
            b, _, _ = collect(recs, ledger, h, pb, drop_illiquid=True)
            c, _, _ = collect(recs, ledger, h, min(f["haircut_bps"]))
            L.append("| %d days | %s | %s | %s | %d | %d |" % (h, _fmt(a, f["position_usd"]), _fmt(b, f["position_usd"]), _fmt(c, f["position_usd"]), pend, unk))
        L.append("")
        hmid = f["horizons"][len(f["horizons"]) // 2]
        for label, keyf in (("insider type", lambda r: r["cluster_type"]), ("regime at entry", lambda r: r["regime"])):
            L += ["Split by %s, %d-day horizon, %s bps:" % (label, hmid, pb), ""]
            for k in sorted({keyf(r) for r in recs}):
                st, pend, unk = collect(recs, ledger, hmid, pb, only=lambda r, k=k: keyf(r) == k)
                L.append("- %s: %s (pending %d, unknown %d)%s" % (k, _fmt(st, f["position_usd"]), pend, unk, "  (n under 5: anecdote)" if st and st["n"] < 5 else ""))
            L.append("")
    tagc = {}
    for r in recs:
        for t in r["tags"]:
            tagc[t] = tagc.get(t, 0) + 1
    L += ["## Tags (kept in, never dropped silently)", ""]
    L += ["- %s: %d" % (t, c) for t, c in sorted(tagc.items())] or ["- none"]
    L += ["", "## Honest limits",
          "- Clusters cluster in time and share the same market days, so they are not independent samples.",
          "- Survivorship: a delisted or non-IEX ticker returns no bars and shows as MISSING. Results are labeled best case when more than %s%% are missing." % f["missing_best_case_over_pct"],
          "- Haircut ladder, liquidity floors and the cost floor are placeholders. Sponsor, fund and entity detection are name heuristics. Bid and ask are not available through the watcher client, so spreads are unmeasured.",
          "- Fewer than %d counted clusters is no verdict, and even more is evidence about this one rule set only, not advice." % f["min_counted_for_verdict"],
          "- Any config change resets these counts (new hash). One change per run.", ""]
    return "\n".join(L)
