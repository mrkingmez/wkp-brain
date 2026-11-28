"""Read-only SEC HTTP client. GET only, https only, host allowlist, rate limit (hard ceiling 2 per second), local cache,
retry with backoff, STOP on 403 or 429. The User-Agent is held in memory only: never printed, logged, cached or written.
Redirects are followed by hand and only to allowlisted https hosts."""
import datetime as dt
import gzip
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib

from . import guards


class SecStop(RuntimeError):
    """403 or 429: the run stops at once. Nothing retries."""


class FetchError(RuntimeError):
    pass


class NotFound(FetchError):
    pass


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_OPENER = urllib.request.build_opener(_NoRedirect)


def default_transport(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        r = _OPENER.open(req, timeout=timeout)
        return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def no_network_transport(url, headers):
    raise AssertionError("network call attempted in a no-network mode")


class Fetched:
    def __init__(self, url, body, fetched_utc, from_cache):
        self.url, self.body, self.fetched_utc, self.from_cache = url, body, fetched_utc, from_cache


def _unzip_capped(body, cap):
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)
    out = d.decompress(body, cap + 1)
    if len(out) > cap:
        raise FetchError("response too large after decompression")
    return out


class SecClient:
    def __init__(self, cfg, user_agent, cache_dir, transport=None, sleep=time.sleep, clock=time.monotonic, now=None, on_stop=None):
        self.cfg = cfg
        self._ua = user_agent
        self.hosts = guards.effective_hosts(cfg)
        self.min_gap = 1.0 / guards.effective_rps(cfg)
        self.cache_dir = cache_dir
        self.transport = transport or (lambda u, h: default_transport(u, h, cfg["sec"]["timeout_seconds"]))
        self._sleep, self._clock = sleep, clock
        self._now = now or (lambda: dt.datetime.now(dt.timezone.utc))
        self._last = None
        self.on_stop = on_stop
        self.requests_made = 0
        self.cache_hits = 0
        self.stopped = False
        os.makedirs(cache_dir, exist_ok=True)

    def __repr__(self):
        return "SecClient(hosts=%s, user_agent hidden)" % sorted(self.hosts)

    def _paths(self, url):
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()
        d = os.path.join(self.cache_dir, h[:2])
        return d, os.path.join(d, h + ".bin"), os.path.join(d, h + ".json")

    def fetch(self, url, use_cache=True):
        if self.stopped:
            raise SecStop("client already stopped by an earlier 403 or 429")
        guards.assert_allowed_url(url, self.hosts)
        d, body_p, meta_p = self._paths(url)
        if use_cache and os.path.exists(body_p) and os.path.exists(meta_p):
            try:
                with open(meta_p, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                with open(body_p, "rb") as f:
                    body = f.read()
                self.cache_hits += 1
                return Fetched(url, body, meta.get("fetched_utc"), True)
            except (OSError, ValueError):
                pass   # damaged cache entry: fall through and fetch again
        s = self.cfg["sec"]
        cur, hops, attempt = url, 0, 0
        while True:
            if self._last is not None:
                wait = self.min_gap - (self._clock() - self._last)
                if wait > 0:
                    self._sleep(wait)
            self._last = self._clock()
            self.requests_made += 1
            headers = {"User-Agent": self._ua, "Accept-Encoding": "gzip", "Accept": "*/*"}
            try:
                status, hdrs, body = self.transport(cur, headers)
            except AssertionError:
                raise
            except Exception as e:   # network failure: the type only, never the message
                status, hdrs, body = 0, {}, b""
                err = type(e).__name__
            else:
                err = None
            hl = {k.lower(): v for k, v in (hdrs or {}).items()}
            if status in (403, 429):
                self.stopped = True
                if self.on_stop:
                    self.on_stop(status, urllib.parse.urlparse(cur).hostname)
                raise SecStop("SEC answered %s: run stopped, no retry" % status)
            if status in (301, 302, 303, 307, 308):
                loc = hl.get("location")
                hops += 1
                if not loc or hops > 2:
                    raise FetchError("too many redirects or no location")
                cur = guards.assert_allowed_url(urllib.parse.urljoin(cur, loc), self.hosts)
                continue
            if status == 404:
                raise NotFound("404 for an allowlisted URL")
            if status == 200:
                cap = s["max_response_bytes"]
                if len(body) > cap:
                    raise FetchError("response too large")
                if hl.get("content-encoding", "").lower() == "gzip":
                    body = _unzip_capped(body, cap)
                fetched = self._now().strftime("%Y-%m-%dT%H:%M:%SZ")
                os.makedirs(d, exist_ok=True)
                tmp = body_p + ".tmp"
                with open(tmp, "wb") as f:
                    f.write(body)
                os.replace(tmp, body_p)
                with open(meta_p, "w", encoding="utf-8") as f:
                    json.dump({"url": url, "fetched_utc": fetched, "bytes": len(body)}, f)
                return Fetched(url, body, fetched, False)
            attempt += 1
            if attempt > s["retries"]:
                raise FetchError("gave up after %d attempts (%s)" % (attempt, err or "http %s" % status))
            self._sleep(s["backoff_seconds"] * (2 ** (attempt - 1)))
