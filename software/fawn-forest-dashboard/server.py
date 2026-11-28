"""Fawn Forest Investments dashboard server.

localhost only (127.0.0.1), GET only, read-only. It serves three fixed static
files and one JSON endpoint built from files on disk. No order buttons, no
write routes, no keys, no outbound network calls.

Usage:  python -I server.py [--port 8790] [--source auto|live|demo]
"""
from __future__ import annotations

import argparse
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ffdata

HERE = Path(__file__).resolve().parent
STATIC = HERE / "static"
HOST = "127.0.0.1"
DEFAULT_PORT = 8790
ALLOWED_HOSTS = {"127.0.0.1", "localhost"}

# fixed allowlist: URL path -> (file, content type). Nothing else is ever opened.
FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/themes.css": ("themes.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "application/javascript; charset=utf-8"),
}
SECURITY_HEADERS = {
    "Cache-Control": "no-store",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Content-Security-Policy": "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self'; frame-ancestors 'none'",
}

SERVER_SOURCE = "auto"


class Handler(BaseHTTPRequestHandler):
    server_version = "FFDash"
    sys_version = ""

    def _send(self, code, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in SECURITY_HEADERS.items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def _host_ok(self) -> bool:
        raw = (self.headers.get("Host") or "")
        try:
            host = urlsplit("//" + raw).hostname
            urlsplit("//" + raw).port
        except ValueError:
            return False
        return host in ALLOWED_HOSTS

    def do_GET(self):
        if not self._host_ok():
            return self._send(403, b"forbidden host", "text/plain")
        parts = urlsplit(self.path)
        path = parts.path
        if path == "/api/state":
            q = parse_qs(parts.query)
            src = (q.get("source", [SERVER_SOURCE])[0] or "auto")
            if src not in ("auto", "live", "demo"):
                return self._send(400, b"bad source", "text/plain")
            try:
                data = ffdata.build_state(src)
                json.dumps(ffdata.clean(data), allow_nan=False, default=str)
            except Exception as exc:  # never crash the page, say what failed
                data = {"available": False, "message": "NOT AVAILABLE: data layer error: " + type(exc).__name__,
                        "paper_only": True, "department": "FAWN FOREST INVESTMENTS"}
            body = json.dumps(ffdata.clean(data), allow_nan=False, default=str).encode("utf-8")
            return self._send(200, body, "application/json; charset=utf-8")
        if path == "/api/health":
            return self._send(200, b'{"ok": true, "read_only": true}', "application/json")
        entry = FILES.get(path)
        if entry is None:
            return self._send(404, b"not found", "text/plain")
        fp = STATIC / entry[0]
        try:
            return self._send(200, fp.read_bytes(), entry[1])
        except OSError:
            return self._send(404, b"missing static file", "text/plain")

    def _reject(self):
        self._send(405, b"read-only dashboard: GET only", "text/plain")

    do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = _reject

    def log_message(self, fmt, *args):
        pass  # keep the console quiet; nothing is logged to disk


def main(argv=None):
    global SERVER_SOURCE
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=DEFAULT_PORT)
    ap.add_argument("--source", choices=["auto", "live", "demo"], default="auto")
    args = ap.parse_args(argv)
    SERVER_SOURCE = args.source
    try:
        httpd = ThreadingHTTPServer((HOST, args.port), Handler)
    except OSError as exc:
        print("Could not start on port %d (%s). Is the dashboard already running? Try --port %d." % (args.port, exc, args.port + 1))
        return 1
    print("FAWN FOREST INVESTMENTS dashboard (paper only, read-only)")
    print("Open in your browser:  http://localhost:%d" % args.port)
    print("Leave this window open. Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
