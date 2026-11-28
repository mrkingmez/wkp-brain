"""Output files: decisions.jsonl, paper-trades.csv, state.json. Append-only logs, atomic state save.
Nothing here ever receives a key or secret: only request ids, prices, counts and reasons.

Crash safety (fix for tester F4): decision lines and trade rows are buffered during a scan. save_state() then
  1. writes state.json WITH the buffered records inside it (a journal), atomically,
  2. appends the records to the log files,
  3. writes state.json again with the journal cleared.
If the program dies anywhere in between, the next start finds the journal and appends only the records that are
not already in the files. Ids therefore never repeat and no line is lost."""
import csv
import json
import os

TRADE_COLUMNS = ["trade_id", "event", "ts_utc", "symbol", "side", "shares", "price_raw", "price_filled",
                 "haircut_bps", "fee_usd", "reason", "setup", "score", "stop", "target", "risk_usd",
                 "pnl_gross", "pnl_net", "r_net", "decision_id", "bar_t", "mode",
                 "ledger", "regime", "config_hash", "parts", "day_trade"]


class StateError(RuntimeError):
    pass


class Out:
    def __init__(self, outdir, mode):
        self.dir, self.mode = outdir, mode
        os.makedirs(outdir, exist_ok=True)
        self.decisions = os.path.join(outdir, "decisions.jsonl")
        self.trades = os.path.join(outdir, "paper-trades.csv")
        self.state_path = os.path.join(outdir, "state.json")
        self.history = os.path.join(outdir, "config-history.jsonl")
        self.buf_dec, self.buf_tr = [], []

    # ---------- state
    def load_state(self, default):
        if not os.path.exists(self.state_path):
            return default
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                st = json.load(f)
        except (ValueError, OSError) as e:   # JSONDecodeError and UnicodeDecodeError are ValueError
            raise StateError("state.json is unreadable (%s). Not starting: fix or move the file, nothing was changed." % type(e).__name__)
        if not isinstance(st, dict) or "cash" not in st or "positions" not in st or "pending" not in st:
            raise StateError("state.json does not look like a watcher state file. Not starting, nothing was changed.")
        return st

    def _write_state(self, st):
        tmp = self.state_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f, indent=1, sort_keys=True, default=str)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, self.state_path)

    def recover(self, st):
        """Replay a journal left by a crash. Appends only records not already in the files. Returns how many were replayed."""
        j = st.get("journal")
        if not j or not (j.get("decisions") or j.get("trades")):
            st["journal"] = None
            return 0
        have_d = self._decision_ids()
        have_t = self._trade_keys()
        d = [r for r in j.get("decisions", []) if r["decision_id"] not in have_d]
        t = [r for r in j.get("trades", []) if (r["trade_id"], r["event"]) not in have_t]
        self._flush(d, t)
        st["journal"] = None
        self._write_state(st)
        return len(d) + len(t)

    def save_state(self, st):
        """Commit the scan: journal, append, clear. Also the only place state.json is written."""
        if self.buf_dec or self.buf_tr:
            st["journal"] = {"decisions": self.buf_dec, "trades": self.buf_tr}
            self._write_state(st)                       # step 1: state plus journal are durable
            self._flush(self.buf_dec, self.buf_tr)      # step 2: append to the logs
            self.buf_dec, self.buf_tr = [], []
        st["journal"] = None
        self._write_state(st)                           # step 3: journal cleared

    # ---------- buffered records
    def decision(self, st, rec):
        st["next_decision"] += 1
        did = "D%06d" % st["next_decision"]
        self.buf_dec.append(dict(rec, decision_id=did, mode=self.mode))
        return did

    def trade(self, row):
        self.buf_tr.append(dict(row, mode=self.mode))

    # ---------- file writes
    def _flush(self, decs, trs):
        if decs:
            lead = ""
            if os.path.exists(self.decisions) and os.path.getsize(self.decisions) > 0:
                with open(self.decisions, "rb") as f:
                    f.seek(-1, os.SEEK_END)
                    if f.read(1) != b"\n":
                        lead = "\n"           # a torn last line from a crash: start a fresh line
            with open(self.decisions, "a", encoding="utf-8") as f:
                f.write(lead + "".join(json.dumps(r, sort_keys=True, default=str) + "\n" for r in decs))
                f.flush()
                os.fsync(f.fileno())
        if trs:
            new = not os.path.exists(self.trades)
            with open(self.trades, "a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=TRADE_COLUMNS, extrasaction="ignore")
                if new:
                    w.writeheader()
                for r in trs:
                    w.writerow(r)
                f.flush()
                os.fsync(f.fileno())

    def _decision_ids(self):
        ids = set()
        if os.path.exists(self.decisions):
            with open(self.decisions, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    try:
                        ids.add(json.loads(line)["decision_id"])
                    except (ValueError, KeyError, TypeError):
                        continue            # torn or damaged line: not counted as present
        return ids

    def _trade_keys(self):
        keys = set()
        if os.path.exists(self.trades):
            with open(self.trades, "r", encoding="utf-8", errors="replace", newline="") as f:
                for r in csv.DictReader(f):
                    keys.add((r.get("trade_id"), r.get("event")))
        return keys

    def append_history(self, rec):
        with open(self.history, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, sort_keys=True) + "\n")
