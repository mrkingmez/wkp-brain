"""Read-only Alpaca client. GET only, path whitelist, feed forced to iex, X-Request-ID kept per call.
Headers hold the keys and are never logged, printed or returned."""
import json
import urllib.error
import urllib.parse
import urllib.request

from .guards import assert_paper_url

PAPER_HOST = "paper-api.alpaca.markets"
DATA_HOST = "data.alpaca.markets"
ALLOWED = {
    PAPER_HOST: {"/v2/account", "/v2/positions", "/v2/clock"},
    DATA_HOST: {"/v2/stocks/bars", "/v2/stocks/bars/latest"},
}


class ClientError(RuntimeError):
    pass


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None  # never follow a redirect: it would forward the key headers to another host


_OPENER = urllib.request.build_opener(_NoRedirect)


def _default_transport(url, headers):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        r = _OPENER.open(req, timeout=20)
        return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


class Result:
    def __init__(self, status, request_id, data, error=None, url_path=""):
        self.status, self.request_id, self.data, self.error, self.path = status, request_id, data, error, url_path

    @property
    def ok(self):
        return self.status == 200 and self.error is None


class AlpacaReadOnly:
    def __init__(self, key_id, secret, base_url, transport=None):
        self.base = assert_paper_url(base_url)
        self._headers = {"APCA-API-KEY-ID": key_id, "APCA-API-SECRET-KEY": secret, "accept": "application/json"}
        self._transport = transport or _default_transport
        self.shapes = {}   # timeframe -> key names of the bars response (names only, no values)

    def __repr__(self):
        return "AlpacaReadOnly(paper, keys hidden)"   # never show headers (tester F9)

    def get(self, url):
        p = urllib.parse.urlparse(url)
        if p.scheme != "https" or p.hostname not in ALLOWED or p.path not in ALLOWED[p.hostname]:
            raise ClientError("blocked: not a whitelisted read-only endpoint: %s%s" % (p.hostname, p.path))
        q = urllib.parse.parse_qs(p.query)
        if p.hostname == DATA_HOST and q.get("feed") != ["iex"]:
            raise ClientError("blocked: market data must use feed=iex")
        try:
            status, hdrs, body = self._transport(url, self._headers)
        except Exception as e:  # network failure: report the type only, never the message
            return Result(0, None, None, "network error: " + type(e).__name__, p.path)
        hl = {k.lower(): v for k, v in hdrs.items()}
        rid = hl.get("x-request-id")
        try:
            data = json.loads(body.decode("utf-8")) if body else None
        except ValueError:
            return Result(status, rid, None, "bad json", p.path)
        err = None if status == 200 else "http %s" % status
        return Result(status, rid, data, err, p.path)

    def account(self):
        return self.get(self.base + "/v2/account")

    def positions(self):
        return self.get(self.base + "/v2/positions")

    def clock(self):
        return self.get(self.base + "/v2/clock")

    def bars(self, symbols, start_iso, timeframe="1Hour"):
        """All pages. Returns (dict symbol -> list of raw bars, list of request ids, error or None)."""
        out, rids, token = {s: [] for s in symbols}, [], None
        for _ in range(20):
            qs = {"symbols": ",".join(symbols), "timeframe": timeframe, "start": start_iso,
                  "limit": "10000", "feed": "iex", "adjustment": "raw"}
            if token:
                qs["page_token"] = token
            r = self.get("https://%s/v2/stocks/bars?%s" % (DATA_HOST, urllib.parse.urlencode(qs)))
            if r.request_id:
                rids.append(r.request_id)
            if not r.ok or not isinstance(r.data, dict):
                return None, rids, r.error or "bad response"
            got = r.data.get("bars")
            if got is not None and not isinstance(got, dict):
                return None, rids, "bad bars shape"
            for s, rows in (got or {}).items():
                if s in out:
                    out[s].extend(rows or [])
            if timeframe not in self.shapes:
                first = next((rows[0] for rows in (got or {}).values() if rows and isinstance(rows[0], dict)), None)
                self.shapes[timeframe] = {"top_level_keys": sorted(r.data.keys()),
                                          "bars_container": type(got).__name__, "bar_keys": sorted(first.keys()) if first else None,
                                          "symbols_returned": len(got or {})}
            token = r.data.get("next_page_token")
            if not token:
                return out, rids, None
        return None, rids, "too many pages"
