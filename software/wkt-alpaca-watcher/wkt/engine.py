"""Scan engine and local paper books. Our own simulated trades only. Nothing here talks to a broker:
bars come in as data, results go to files.

Two simulated ledgers run side by side on the same signals:
  main : fills at the first 1-hour bar open at or after the signal bar close and at or after the 10:00 ET fill hour (the plumbing test)
  zac  : "Zac can act" ledger. Zac works 8 to 5 and enters by hand, so a signal can only fill at the open of the
         NEXT trading session. Go-live is judged on this ledger, not on main."""
import datetime as dt
from zoneinfo import ZoneInfo

from . import regime as regime_mod, risk, scoring
from .config import config_hash
from .logio import Out
from .stats import bdays_between, net_at

ET = ZoneInfo("America/New_York")
HOUR = dt.timedelta(hours=1)
PREFIX = {"main": "T", "zac": "Z"}


def parse_bars(rows):
    out = []
    for r in rows or []:
        try:
            t = dt.datetime.fromisoformat(str(r["t"]).replace("Z", "+00:00"))
            if t.tzinfo is None:
                raise ValueError("naive time")
            out.append({"t": t.astimezone(dt.timezone.utc), "o": r.get("o"), "h": r.get("h"),
                        "l": r.get("l"), "c": r.get("c"), "v": r.get("v")})
        except (KeyError, ValueError, TypeError, AttributeError):
            out.append({"t": dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc), "o": None, "h": None, "l": None, "c": None, "v": None})
    out.sort(key=lambda b: b["t"])
    return out


def filter_session(bars, cfg):
    """Drop pre-market and after-hours hourly bars. Alpaca's IEX hourly bars start at 08:00 ET and run to 16:00 ET
    (seen in the 2026-11-26 smoke run), so without this the scores, ATR, stops and exits would use thin extended-hours bars.
    Keeps bars whose START hour (ET) is inside the configured range. Returns (kept, dropped_count)."""
    sb = cfg["session_bars"]
    if not sb["regular_hours_only"]:
        return list(bars), 0
    keep = [b for b in bars if sb["first_bar_start_hour_et"] <= b["t"].astimezone(ET).hour <= sb["last_bar_start_hour_et"]]
    return keep, len(bars) - len(keep)


def iso(t):
    return t.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fromiso(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def new_book(equity):
    return {"cash": float(equity), "starting_equity": float(equity), "positions": {}, "pending": {},
            "day": {"date": None, "start_equity": None, "killed": False},
            "week": {"start": None, "start_equity": None, "blocked": False},
            "next_trade": 0, "closed_stats": [], "day_trades": [], "last_kill_date": None, "last_equity": None}


def new_state(cfg):
    eq = float(cfg["paper_book"]["starting_equity"])
    st = new_book(eq)
    st.update({"marks": {}, "evaluated": {}, "episodes": {}, "next_decision": 0, "regime": None,
               "config_hash": None, "ended": False, "journal": None, "zac": new_book(eq)})
    return st


class Watcher:
    def __init__(self, cfg, outdir, mode):
        self.cfg, self.mode = cfg, mode
        self.chash = config_hash(cfg)
        self.out = Out(outdir, mode)
        default = new_state(cfg)
        st = self.out.load_state(default)
        for k, v in default.items():
            st.setdefault(k, v)
        for k, v in default["zac"].items():
            st["zac"].setdefault(k, v)
        self.st = st
        self.recovered = self.out.recover(st)
        if st.get("config_hash") != self.chash:
            self.out.append_history({"recorded_at_utc": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                                     "hash": self.chash, "previous": st.get("config_hash"), "mode": mode,
                                     "note": "first start" if st.get("config_hash") is None else "CONFIG CHANGED: counts restart under the new hash"})
            st["config_hash"] = self.chash
        if st.get("ended") and st.get("ended_hash") != self.chash:
            st["ended"] = False      # the end rule belongs to one frozen config: a new hash is a new experiment
        self._daily_try = None
        self.info = {}

    # ---------- helpers
    def books(self):
        out = [("main", self.st)]
        if self.cfg["zac_ledger"]["enabled"]:
            out.append(("zac", self.st["zac"]))
        return out

    def equity(self, bk=None):
        bk = self.st if bk is None else bk
        marks = self.st["marks"]
        return bk["cash"] + sum(p["shares"] * marks.get(s, p["entry_fill"]) for s, p in sorted(bk["positions"].items()))

    def _log(self, now, common, symbol, action, reason, **extra):
        rec = dict(common, ts_utc=iso(now), symbol=symbol, action=action, reason=reason)
        rec.update(extra)
        return self.out.decision(self.st, rec)

    def _hc(self):
        return float(self.cfg["paper_book"]["haircut_bps_each_side"])

    def needs_daily(self, now, today_date):
        """True when today's regime is not computed yet and we have not asked in the last 10 minutes."""
        r = self.st.get("regime")
        if r and r.get("date") == today_date.isoformat():
            return False
        return self._daily_try is None or (now - self._daily_try) >= dt.timedelta(minutes=10)

    def _regime(self, now, today_date, daily):
        r = self.st.get("regime")
        if r and r.get("date") == today_date.isoformat():
            return r, False
        if daily is None:
            return {"tag": "UNKNOWN", "detail": {"why": "no daily data this scan"}, "date": None}, False
        res = regime_mod.compute(daily, self.cfg, today_date)
        self.st["regime"] = {"date": today_date.isoformat(), "tag": res["tag"], "detail": res["detail"]}
        return self.st["regime"], True

    def _common(self, now, request_ids, clock_open, reg):
        return {"scan_id": iso(now), "feed": self.cfg["feed"], "request_ids": list(request_ids or []),
                "clock_open": bool(clock_open), "config_hash": self.chash, "regime": reg["tag"],
                "spy_mark": self.st["marks"].get(self.cfg["market_gauge"])}

    # ---------- main scan
    def scan(self, now, bars, request_ids, error=None, clock_open=True, daily=None):
        """now: aware UTC datetime. bars: dict symbol -> parsed bars (or None if the data call failed).
        daily: dict symbol -> parsed daily bars (only passed when the regime still needs computing today)."""
        cfg, st = self.cfg, self.st
        et = now.astimezone(ET)
        wd, today_date = et.strftime("%a"), et.date()
        today = today_date.isoformat()
        symbols = cfg["symbols"]
        summary = {"decisions": 0, "trades_opened": 0, "trades_closed": 0, "zac_trades_opened": 0, "zac_trades_closed": 0}
        reg, new_reg = self._regime(now, today_date, daily)
        common = self._common(now, request_ids, clock_open, reg)

        if bars is None:
            for s in symbols:
                self._log(now, common, s, "SKIP", "FAIL: UNKNOWN data call failed (%s)" % error, fresh=False, counted=False)
            self.out.save_state(st)
            return summary

        # 1. marks, day and week start (baseline is the last equity of the prior scan, so overnight gaps count), kill switch
        for sym, sb in bars.items():
            if sb and scoring.bars_valid(sb[-1:]) is None:
                st["marks"][sym] = sb[-1]["c"]
        common["spy_mark"] = st["marks"].get(cfg["market_gauge"])
        if new_reg:
            self._log(now, common, "*", "REGIME", "regime %s" % reg["tag"], fresh=False, regime_detail=reg["detail"])
        monday = (today_date - dt.timedelta(days=today_date.weekday())).isoformat()
        for name, bk in self.books():
            eq = self.equity(bk)
            if bk["day"]["date"] != today:
                bk["day"] = {"date": today, "start_equity": bk.get("last_equity") or eq, "killed": False}
            if bk["week"]["start"] != monday:
                bk["week"] = {"start": monday, "start_equity": bk.get("last_equity") or eq, "blocked": False}
            if not bk["day"]["killed"] and risk.kill_switch_tripped(bk["day"]["start_equity"], eq, cfg):
                bk["day"]["killed"] = True
                bk["last_kill_date"] = today
                self._log(now, common, "*", "KILL", "daily kill switch tripped: equity %.2f vs day start %.2f, no new trades today" % (eq, bk["day"]["start_equity"]), fresh=False, ledger=name)
            if not bk["week"]["blocked"] and risk.weekly_limit_hit(bk["week"]["start_equity"], eq, cfg):
                bk["week"]["blocked"] = True
                self._log(now, common, "*", "WEEK_LIMIT", "weekly loss limit hit: equity %.2f vs week start %.2f, no new trades until next Monday" % (eq, bk["week"]["start_equity"]), fresh=False, ledger=name)

        # 2. fills (blocked while killed) and exits on our own paper books. Open positions keep their own stops.
        for name, bk in self.books():
            for sym in sorted(bk["pending"]):
                if bk["day"]["killed"] or bk["week"]["blocked"]:
                    why = "daily kill switch tripped" if bk["day"]["killed"] else "weekly loss limit hit"
                    self._log(now, common, sym, "CANCEL", why + ", signal cancelled before fill", fresh=False, ledger=name, decision_ref=bk["pending"][sym]["decision_id"])
                    del bk["pending"][sym]
                elif self._expired(now, common, name, bk, sym, now.astimezone(ET).date()):
                    pass
                elif bars.get(sym):
                    self._try_fill(now, common, name, bk, sym, bars[sym], summary)
            for sym in sorted(bk["positions"]):
                if bars.get(sym):
                    self._check_exit(now, common, name, bk, sym, bars[sym], summary)
                else:
                    self._log(now, common, sym, "HOLD_UNKNOWN", "FAIL: UNKNOWN no data to check stop, target or time stop", fresh=False, ledger=name)

        # 3. evaluation, one line per symbol per scan. Signals come from the main book's view; the zac book mirrors them.
        closed = {s: [b for b in (bars.get(s) or []) if b["t"] + HOUR <= now] for s in symbols}
        mood = scoring.market_mood(closed[cfg["market_gauge"]], cfg, now)
        slots = cfg["rules"]["max_open_positions"] - len(st["positions"]) - len(st["pending"])
        count_min = cfg["counting"]["min_score"]
        eligible, lines = [], []
        for sym in symbols:
            cb = closed[sym]
            base = {"fresh": True, "bar_t": iso(cb[-1]["t"]) if cb else None, "counted": False}
            if sym in st["positions"] or sym in st["pending"]:
                lines.append((sym, "SKIP", "already holding or signal pending", dict(base, fresh=False))); continue
            why = scoring.hard_filters(cb, cfg, now)
            if why:
                lines.append((sym, "SKIP", why, dict(base, fresh=False))); continue
            if st["evaluated"].get(sym) == iso(cb[-1]["t"]):
                lines.append((sym, "SKIP", "bar already evaluated, nothing new", dict(base, fresh=False))); continue
            if st["day"]["killed"] or st["week"]["blocked"]:
                lines.append((sym, "SKIP", "kill switch or weekly limit active, no new trades", dict(base, fresh=False))); continue
            if slots <= 0:
                lines.append((sym, "SKIP", "max open positions reached", dict(base, fresh=False))); continue
            cand, note = scoring.evaluate(cb, mood, cfg)
            st["evaluated"][sym] = iso(cb[-1]["t"])
            if cand is None:
                st["episodes"][sym] = None
                lines.append((sym, "SKIP", note, base)); continue
            # a decision counts at score 70 or higher, once per setup (same setup on consecutive bars is the same episode)
            counted = cand["score"] >= count_min and st["episodes"].get(sym) != cand["setup"]
            st["episodes"][sym] = cand["setup"] if cand["score"] >= count_min else None
            extra = dict(base, setup=cand["setup"], score=cand["score"], parts=cand["parts"], counted=counted)
            block = risk.gate_reason(cand["score"], wd, cfg)
            if block:
                lines.append((sym, "WATCH", block, extra)); continue
            eligible.append((cand["score"], sym, cand, extra))
        eligible.sort(key=lambda x: (-x[0], x[1]))
        for rank, (score, sym, cand, extra) in enumerate(eligible):
            if rank < slots:
                lines.append((sym, "TRADE", "signal queued, main fills at next bar open, zac ledger at next session open",
                              dict(extra, planned_risk_pct=risk.risk_pct_for(score, cfg))))
            else:
                lines.append((sym, "WATCH", "max open positions reached, lower rank this scan", extra))
        order = {s: i for i, s in enumerate(symbols)}
        for sym, action, reason, extra in sorted(lines, key=lambda x: order[x[0]]):
            did = self._log(now, common, sym, action, reason, **extra)
            summary["decisions"] += 1
            if action == "TRADE":
                c = next(e[2] for e in eligible if e[1] == sym)
                sig = {"decision_id": did, "signal_bar_t": iso(c["bar_t"]), "entry_ref": c["entry"], "atr": c["atr"],
                       "score": c["score"], "setup": c["setup"], "parts": c["parts"], "regime": reg["tag"], "config_hash": self.chash}
                st["pending"][sym] = dict(sig)
                self._mirror_to_zac(now, common, sym, sig, did)
        for name, bk in self.books():
            bk["last_equity"] = self.equity(bk)
        self.out.save_state(st)
        return summary

    def _mirror_to_zac(self, now, common, sym, sig, did):
        if not self.cfg["zac_ledger"]["enabled"]:
            return
        zb = self.st["zac"]
        mx = self.cfg["rules"]["max_open_positions"]
        why = None
        if sym in zb["positions"] or sym in zb["pending"]:
            why = "zac ledger already holds or is waiting on this symbol"
        elif len(zb["positions"]) + len(zb["pending"]) >= mx:
            why = "zac ledger at max open positions"
        elif zb["day"]["killed"] or zb["week"]["blocked"]:
            why = "zac ledger kill switch or weekly limit active"
        if why:
            self._log(now, common, sym, "LEDGER_SKIP", why, fresh=False, ledger="zac", decision_ref=did)
        else:
            zb["pending"][sym] = dict(sig)

    # ---------- paper fills
    def _expired(self, now, common, name, bk, sym, ref_date):
        """Change 6 (tester pass 3 F2): a Zac-ledger signal that waited more than zac_ledger.max_pending_sessions weekdays
        (signal ET date to ref_date, holidays not modeled) is cancelled, never filled at a stale price. True when cancelled."""
        if name != "zac":
            return False
        sig = bk["pending"][sym]
        sig_date = fromiso(sig["signal_bar_t"]).astimezone(ET).date()
        limit = self.cfg["zac_ledger"]["max_pending_sessions"]
        waited = bdays_between(sig_date, ref_date)
        if waited <= limit:
            return False
        self._log(now, common, sym, "CANCEL", "signal expired: %d weekdays since the signal date %s, limit %d, no fill" % (waited, sig_date.isoformat(), limit),
                  fresh=False, ledger=name, decision_ref=sig["decision_id"])
        del bk["pending"][sym]
        return True

    def _open_entry_dates(self, now, common, name, bk, today_date):
        """ET dates (ISO) of the entries still open, for the PDT guard. Change 7 (tester pass 3 F3): a missing or unreadable
        entry_bar_t is logged as UNKNOWN (FAIL) and fails safe: that entry counts as opened today, so it can only make the guard stricter."""
        out = []
        for sym in sorted(bk["positions"]):
            p = bk["positions"][sym]
            try:
                out.append(fromiso(p["entry_bar_t"]).astimezone(ET).date().isoformat())
            except (KeyError, ValueError, TypeError, AttributeError):
                out.append(today_date.isoformat())
                self._log(now, common, sym, "HOLD_UNKNOWN", "FAIL: UNKNOWN entry_bar_t missing or unreadable on the open position, counted as opened today for the PDT guard",
                          fresh=False, ledger=name)
        return out

    def _try_fill(self, now, common, name, bk, sym, sb, summary):
        cfg, st = self.cfg, self.st
        sig = bk["pending"][sym]
        sig_t = fromiso(sig["signal_bar_t"])
        due = sig_t + HOUR
        if name == "zac":
            sig_date = sig_t.astimezone(ET).date()
            fh = cfg["fills"]["session_open_fill_hour_et"]
            # next session, first bar starting at or after the fill hour (10:00 bar open, not the 09:00 bar with pre-open prints)
            ok = lambda b: b["t"] >= due and b["t"].astimezone(ET).date() > sig_date and b["t"].astimezone(ET).hour >= fh
        else:
            # change 5: main entry also fills at the first bar open at or after the fill hour (the 09:00 bar holds pre-open prints)
            fh = cfg["fills"]["session_open_fill_hour_et"]
            ok = lambda b: b["t"] >= due and b["t"].astimezone(ET).hour >= fh
        nxt = next((b for b in sb if ok(b) and scoring.bars_valid([b]) is None), None)
        if nxt is None:
            return
        if self._expired(now, common, name, bk, sym, nxt["t"].astimezone(ET).date()):
            return
        pb, R = cfg["paper_book"], cfg["rules"]
        today_date = now.astimezone(ET).date()
        # S4 fix: entries still open that were opened on this ET date count as potential day trades (they could be exited today)
        # Change 8 (tester pass 3 F1): the guard dates the entry by its FILL BAR (ET), not by the scan time, so a backfill after an outage still counts same-day fills
        fill_date = nxt["t"].astimezone(ET).date()
        open_today = self._open_entry_dates(now, common, name, bk, fill_date)
        blocked = risk.pdt_block(bk["day_trades"], fill_date, cfg, open_entry_dates=open_today)
        if blocked:
            self._log(now, common, sym, "CANCEL", blocked, fresh=False, ledger=name, decision_ref=sig["decision_id"])
            del bk["pending"][sym]; return
        raw = nxt["o"]
        gap_limit = pb["max_gap_atr"] if name == "main" else cfg["zac_ledger"].get("max_gap_atr")
        gap_atr = abs(raw - sig["entry_ref"]) / sig["atr"] if sig["atr"] else None
        if gap_limit is not None and abs(raw - sig["entry_ref"]) > gap_limit * sig["atr"]:
            self._log(now, common, sym, "CANCEL", "next bar opened %.2f vs signal close %.2f, gap over %s ATR" % (raw, sig["entry_ref"], gap_limit), fresh=False, ledger=name, decision_ref=sig["decision_id"])
            del bk["pending"][sym]; return
        hc = self._hc()
        fill = raw * (1 + hc / 1e4)
        eq_now = self.equity(bk)
        views = cfg["scorecard"]["haircut_views_bps"]
        zb = st["zac"]
        nets = [s["net"][str(cfg["sizing"]["step_up"]["expectancy_haircut_bps"])] for s in zb["closed_stats"] if s["hash"] == self.chash]
        su_pct, su_why = risk.step_up_check(cfg, sig["score"], sig.get("regime", "UNKNOWN"), len(bk["positions"]), nets, bk["last_kill_date"], today_date)
        shares, det = risk.size_shares(eq_now, bk["cash"], fill, sig["atr"], sig["score"], cfg, risk_pct=su_pct)
        det["step_up"] = su_why
        fee_bps = float(pb["fee_bps_each_side"])
        while shares > 0 and shares * fill * (1 + fee_bps / 1e4) > bk["cash"]:
            shares -= 1
        if shares < 1:
            self._log(now, common, sym, "CANCEL", "size under 1 share (%s)" % det.get("binding", det.get("why")), fresh=False, ledger=name, decision_ref=sig["decision_id"])
            del bk["pending"][sym]; return
        fee = shares * fill * fee_bps / 1e4
        stop = fill - R["atr_stop_multiple"] * sig["atr"]
        target = fill + R["reward_multiple"] * (fill - stop)
        bk["next_trade"] += 1
        tid = "%s%04d" % (PREFIX[name], bk["next_trade"])
        bk["cash"] -= shares * fill + fee
        bk["positions"][sym] = {"trade_id": tid, "shares": shares, "entry_raw": raw, "entry_fill": fill, "entry_fee": fee, "stop": stop,
                                "target": target, "atr": sig["atr"], "risk_usd": shares * (fill - stop), "score": sig["score"],
                                "setup": sig["setup"], "entry_bar_t": iso(nxt["t"]), "decision_id": sig["decision_id"],
                                "regime": sig.get("regime", "UNKNOWN"), "parts": sig.get("parts", {}), "config_hash": sig.get("config_hash", self.chash)}
        del bk["pending"][sym]
        did = self._log(now, common, sym, "FILL", "paper fill (%s ledger), size bound by %s" % (name, det["binding"]), fresh=False, trade_id=tid,
                        ledger=name, decision_ref=sig["decision_id"], shares=shares, size=det, equity=round(eq_now, 2), notional=round(shares * fill, 2),
                        gap_atr=None if gap_atr is None else round(gap_atr, 3))
        import json as _json
        self.out.trade({"trade_id": tid, "event": "OPEN", "ts_utc": iso(now), "symbol": sym, "side": "BUY", "shares": shares, "price_raw": raw,
                        "price_filled": round(fill, 6), "haircut_bps": hc, "fee_usd": round(fee, 6), "reason": "signal " + sig["decision_id"],
                        "setup": sig["setup"], "score": sig["score"], "stop": round(stop, 6), "target": round(target, 6),
                        "risk_usd": round(shares * (fill - stop), 2), "decision_id": did, "bar_t": iso(nxt["t"]),
                        "ledger": name, "regime": sig.get("regime", "UNKNOWN"), "config_hash": sig.get("config_hash", self.chash),
                        "parts": _json.dumps(sig.get("parts", {}), sort_keys=True), "day_trade": ""})
        summary["trades_opened" if name == "main" else "zac_trades_opened"] += 1

    def _check_exit(self, now, common, name, bk, sym, sb, summary):
        cfg = self.cfg
        pos, R = bk["positions"][sym], cfg["rules"]
        entry_t = fromiso(pos["entry_bar_t"])
        dates = set()
        fh = cfg["fills"]["session_open_fill_hour_et"]
        for b in sb:
            if b["t"] < entry_t or scoring.bars_valid([b]) is not None:
                continue
            bd = b["t"].astimezone(ET).date()
            dates.add(bd)
            elapsed = len(dates) - 1
            # time stop: exit at the open of the first bar starting at or after the fill hour on the time-stop session (stops and targets stay live on earlier bars)
            if elapsed >= R["time_stop_sessions"] and b["t"].astimezone(ET).hour >= fh:
                return self._close(now, common, name, bk, sym, pos, b["o"], "time_stop", b, summary)
            if b["l"] <= pos["stop"]:
                return self._close(now, common, name, bk, sym, pos, min(pos["stop"], b["o"]), "stop", b, summary)
            if b["h"] >= pos["target"]:
                return self._close(now, common, name, bk, sym, pos, pos["target"], "target", b, summary)

    def _close(self, now, common, name, bk, sym, pos, raw, reason, bar, summary):
        import json as _json
        cfg, st, pb = self.cfg, self.st, self.cfg["paper_book"]
        hc = self._hc()
        fill = raw * (1 - hc / 1e4)
        fee = pos["shares"] * fill * (float(pb["fee_bps_each_side"]) + float(pb["sell_reg_fee_bps"])) / 1e4
        gross = (raw - pos["entry_raw"]) * pos["shares"]
        net = (fill - pos["entry_fill"]) * pos["shares"] - pos["entry_fee"] - fee
        r = net / pos["risk_usd"] if pos["risk_usd"] else None
        bk["cash"] += pos["shares"] * fill - fee
        del bk["positions"][sym]
        exit_date = bar["t"].astimezone(ET).date()
        day_trade = fromiso(pos["entry_bar_t"]).astimezone(ET).date() == exit_date
        if day_trade:
            bk["day_trades"].append(exit_date.isoformat())
        views = cfg["scorecard"]["haircut_views_bps"]
        bk["closed_stats"].append({"trade_id": pos["trade_id"], "hash": pos.get("config_hash", self.chash), "day_trade": day_trade,
                                   "net": {str(b): round(net_at(pos["entry_raw"], raw, pos["shares"], b, float(pb["fee_bps_each_side"]), float(pb["sell_reg_fee_bps"])), 4) for b in views}})
        did = self._log(now, common, sym, "EXIT", "%s: raw %.4f, bar %s" % (reason, raw, iso(bar["t"])), fresh=False, trade_id=pos["trade_id"],
                        ledger=name, pnl_net=round(net, 2), decision_ref=pos["decision_id"], day_trade=day_trade)
        self.out.trade({"trade_id": pos["trade_id"], "event": "CLOSE", "ts_utc": iso(now), "symbol": sym, "side": "SELL", "shares": pos["shares"],
                        "price_raw": raw, "price_filled": round(fill, 6), "haircut_bps": hc, "fee_usd": round(fee, 6), "reason": reason,
                        "setup": pos["setup"], "score": pos["score"], "stop": round(pos["stop"], 6), "target": round(pos["target"], 6),
                        "risk_usd": round(pos["risk_usd"], 2), "pnl_gross": round(gross, 2), "pnl_net": round(net, 2),
                        "r_net": None if r is None else round(r, 3), "decision_id": did, "bar_t": iso(bar["t"]),
                        "ledger": name, "regime": pos.get("regime", "UNKNOWN"), "config_hash": pos.get("config_hash", self.chash),
                        "parts": _json.dumps(pos.get("parts", {}), sort_keys=True), "day_trade": "True" if day_trade else "False"})
        summary["trades_closed" if name == "main" else "zac_trades_closed"] += 1

    # ---------- fixed end rule
    def close_out(self, now, reason="end_rule"):
        """End rule: cancel waiting signals and close every open paper position at the last mark (the final close).
        The last mark is the latest bar close seen by the last scan, within about a minute of the close, NOT the official closing print.
        A position with no mark is left open and logged as UNKNOWN (never guessed)."""
        st = self.st
        reg = st.get("regime") or {"tag": "UNKNOWN"}
        common = self._common(now, [], False, reg)
        summary = {"trades_closed": 0, "zac_trades_closed": 0}
        n = 0
        for name, bk in self.books():
            for sym in sorted(bk["pending"]):
                self._log(now, common, sym, "CANCEL", "end rule reached, waiting signal cancelled", fresh=False, ledger=name, decision_ref=bk["pending"][sym]["decision_id"])
                del bk["pending"][sym]
            for sym in sorted(bk["positions"]):
                mark = st["marks"].get(sym)
                pos = bk["positions"][sym]
                if mark is None or scoring.bars_valid([{"o": mark, "h": mark, "l": mark, "c": mark, "v": 0}]):
                    self._log(now, common, sym, "HOLD_UNKNOWN", "FAIL: UNKNOWN no closing mark at the end rule, left open", fresh=False, ledger=name)
                    continue
                self._close(now, common, name, bk, sym, pos, mark, reason, {"t": now}, summary)
                n += 1
            bk["last_equity"] = self.equity(bk)
        st["ended"] = True
        st["ended_hash"] = self.chash
        self.out.save_state(st)
        return n
