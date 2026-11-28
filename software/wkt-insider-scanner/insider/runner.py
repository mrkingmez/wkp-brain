"""Orchestration: filings -> clusters.jsonl and skips.jsonl; clusters -> forward-returns.jsonl; scorecard.
Every output line carries config hash, tool version, run id, mode. No secret is ever in scope here."""
import datetime as dt
import os
import sys

from . import VERSION, cluster, form4, forward, guards, logio, scorecard


def _meta(run, **extra):
    d = {"run_id": run["run_id"], "config_hash": run["config_hash"], "tool_version": VERSION, "mode": run["mode"]}
    d.update(extra)
    return d


def new_run(cfg_hash, mode, now):
    return {"run_id": now.strftime("%Y%m%dT%H%M%SZ") + "-" + mode, "config_hash": cfg_hash, "mode": mode, "started_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ")}


def parse_all(xml_items, skips):
    """xml_items: list of (xml_text, meta). Parse failures go to the skip list with a reason code."""
    out = []
    for xml, meta in xml_items:
        try:
            out.append(form4.parse_form4(xml, meta))
        except form4.Form4Error as e:
            skips.append({"accession": meta.get("accession"), "reason": "parse_failed:" + e.code, "filing_date": meta.get("filing_date"),
                          "source_url": meta.get("source_url")})
    return out


def apply_freeze(clusters, cfg):
    """RULING 11. A COUNTED cluster whose signal instant is not after the freeze time becomes PRE_FREEZE: recorded, never counted, never scored."""
    from zoneinfo import ZoneInfo
    et = ZoneInfo("America/New_York")
    fz = dt.datetime.fromisoformat(str(cfg["freeze"]["counted_signals_from_et"]))
    fz = fz if fz.tzinfo else fz.replace(tzinfo=et)
    for c in clusters:
        if c["status"] == "COUNTED" and c.get("signal"):
            if dt.datetime.fromisoformat(c["signal"]["instant_et"]) <= fz:
                c["status"], c["counted"] = "PRE_FREEZE", False
                c["flags"] = list(c["flags"]) + ["pre_freeze(signal at or before %s)" % cfg["freeze"]["counted_signals_from_et"]]
    return clusters


def cluster_run(filings, pre_skips, cfg, outdir, run, source_urls, fetch_time_utc):
    """Writes clusters.jsonl and skips.jsonl (append). Returns (clusters, skips)."""
    guards.assert_own_ledger(outdir, cfg)
    kept, s1 = cluster.supersede(filings)
    purchases, s2 = cluster.to_purchases(kept, cfg)
    clusters = apply_freeze(cluster.find_clusters(purchases, cfg), cfg)
    skips = list(pre_skips) + s1 + s2
    ts = run["started_utc"]
    lines = []
    for c in clusters:
        lines.append(dict(c, **_meta(run, run_started_utc=ts, fetch_time_utc=fetch_time_utc, run_source_urls=sorted(source_urls))))
    logio.append_jsonl(os.path.join(outdir, "clusters.jsonl"), lines)
    logio.append_jsonl(os.path.join(outdir, "skips.jsonl"), [dict(s, **_meta(run, run_started_utc=ts)) for s in skips])
    return clusters, skips


def score_run(clusters, bars_for, regime_for, cfg, outdir, run, quote_for=None):
    """bars_for(symbol) -> daily rows or None. regime_for(entry_date_iso_or_None, ticker) -> tag. Only COUNTED clusters are scored."""
    guards.assert_own_ledger(outdir, cfg)
    spy = bars_for(cfg["forward"]["benchmark"])
    if not spy:
        raise RuntimeError("no benchmark bars (%s): cannot score. Nothing written." % cfg["forward"]["benchmark"])
    bench = {}
    for b in cfg["forward"]["benchmarks"]:
        bench[b] = bars_for(b)
        if not bench[b]:
            raise RuntimeError("no benchmark bars (%s): the primary pass needs both SPY and IWM, cannot score. Nothing written." % b)
    recs = []
    for c in clusters:
        if not c["counted"]:
            continue
        stock = bars_for(c["issuer"]["ticker"]) if c["issuer"]["ticker"] else None
        sig = c.get("signal") or c.get("signal_filing_date") or c["last_filing_date"]
        i0, _ = forward.entry_index(spy, sig, cfg)
        reg_date = spy[i0]["d"].isoformat() if i0 is not None else None
        tag = regime_for(reg_date, c["issuer"]["ticker"]) if reg_date else "UNKNOWN"
        qf = (lambda d, t=c["issuer"]["ticker"]: quote_for(t, d)) if quote_for and c["issuer"]["ticker"] else None
        r = forward.score_cluster(c, stock, spy, tag, cfg, qf, bench)
        recs.append(dict(r, **_meta(run, scored_utc=run["started_utc"], bars_last_date=spy[-1]["d"].isoformat())))
    logio.append_jsonl(os.path.join(outdir, "forward-returns.jsonl"), recs)
    return recs


def write_scorecard(outdir, cfg, chash, generated, mode, clusters_file_records=None):
    guards.assert_own_ledger(outdir, cfg)
    recs = logio.read_jsonl(os.path.join(outdir, "forward-returns.jsonl"))
    cl = clusters_file_records if clusters_file_records is not None else logio.read_jsonl(os.path.join(outdir, "clusters.jsonl"))
    cur = {c["cluster_id"]: c for c in cl if c.get("config_hash") == chash}
    counted = sum(1 for c in cur.values() if c.get("counted"))
    watch = sum(1 for c in cur.values() if c.get("status") == "WATCH")
    pre = sum(1 for c in cur.values() if c.get("status") == "PRE_FREEZE")
    hist = logio.read_jsonl(os.path.join(outdir, "config-history.jsonl"))
    extras = {"today": generated[:10] if generated[:4].isdigit() else None,
              "config_resets": (sum(1 for h in hist if h.get("previous_hash")) if hist else None),
              "lookahead_clusters": scorecard.lookahead_clusters(cl, chash), "pre_freeze": pre}
    text = scorecard.build(recs, cfg, chash, counted, watch, generated, mode, "forward-returns.jsonl", extras)
    path = os.path.join(outdir, "insider-scorecard.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


# ---- regime link: the watcher's own regime module, read only, imported by path
def load_watcher(cfg):
    wdir = cfg["forward"]["watcher_dir"]
    if not os.path.isdir(os.path.join(wdir, "wkt")):
        return None
    if wdir not in sys.path:
        sys.path.insert(0, wdir)
    try:
        from wkt import regime as wreg   # noqa: E402
        from wkt.config import load_config as wload   # noqa: E402
    except Exception:
        return None
    return {"regime": wreg, "cfg": wload(os.path.join(wdir, "config.yaml"))}


def make_regime_for(watcher, daily_parsed_by_symbol, watcher_cfg_override=None):
    """Returns regime_for(entry_date_iso, ticker). The tag is the watcher's, computed from bars strictly before the entry date.
    Missing watcher module or bars = UNKNOWN (never a guess)."""
    if not watcher:
        return lambda d, t: "UNKNOWN"
    wcfg = watcher_cfg_override or watcher["cfg"]

    def regime_for(entry_iso, ticker):
        try:
            res = watcher["regime"].compute(daily_parsed_by_symbol, wcfg, dt.date.fromisoformat(entry_iso))
            return res["tag"]
        except Exception:
            return "UNKNOWN"
    return regime_for
