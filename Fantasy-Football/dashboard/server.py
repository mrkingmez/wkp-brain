"""Serves the dashboard static page and the current state.json snapshot
on localhost. Never calls MFL, ESPN, or anything else -- it only reads
files poller.py already wrote. Refreshing the browser costs zero
external API calls, on purpose (see SUNDAY-DASHBOARD-BUILD.md Section 1:
"the browser must never trigger a data pull").
"""
import http.server
import socketserver
import subprocess
import sys
import time
from pathlib import Path

import config

STATIC_DIR = config.DASHBOARD_DIR / "static"


def _poller_pid_alive() -> int | None:
    """Returns the poller's PID if config.POLLER_PID_FILE names a process
    that's actually still running, else None. Checked via `tasklist`
    (Windows) rather than trusting the file's mere existence -- a
    crashed poller can leave a stale PID file behind."""
    if not config.POLLER_PID_FILE.exists():
        return None
    try:
        pid = int(config.POLLER_PID_FILE.read_text(encoding="utf-8").strip())
    except (ValueError, OSError):
        return None
    result = subprocess.run(
        ["tasklist", "/FI", f"PID eq {pid}"], capture_output=True, text=True, timeout=10
    )
    return pid if str(pid) in result.stdout else None


def _ensure_poller_running():
    pid = _poller_pid_alive()
    if pid:
        print(f"Poller already running (PID {pid}) -- not starting a second one.", flush=True)
        return

    print("No live poller found -- starting one now (separate process, own console window).", flush=True)
    subprocess.Popen(
        [sys.executable, str(config.DASHBOARD_DIR / "poller.py")],
        cwd=str(config.DASHBOARD_DIR),
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )
    # Give it a moment to write the PID file before reporting back --
    # confirms it actually started rather than just assuming Popen succeeded.
    for _ in range(20):
        time.sleep(0.5)
        if _poller_pid_alive():
            print(f"Poller confirmed running (PID {_poller_pid_alive()}).", flush=True)
            return
    print("WARNING: poller.py was launched but no PID file appeared after 10s -- check its console window.", flush=True)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        if self.path == "/state.json":
            self._serve_state()
            return
        super().do_GET()

    def _serve_state(self):
        if not config.STATE_PATH.exists():
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "state.json does not exist yet -- poller.py has not completed a cycle"}')
            return
        body = config.STATE_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass  # keep the console readable; poller.py already logs


def main():
    if not STATIC_DIR.exists():
        raise SystemExit(f"{STATIC_DIR} does not exist -- static assets missing.")
    _ensure_poller_running()
    with socketserver.TCPServer(("127.0.0.1", config.PORT), Handler) as httpd:
        print(f"Sunday Dashboard serving at http://localhost:{config.PORT} (Ctrl+C to stop)", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
