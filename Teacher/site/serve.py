r"""Teacher course server. Standard library only.

- Serves site\build on a fixed port.
- Binds to ONE private LAN address only (10.x, 172.16-31.x, 192.168.x). Never 0.0.0.0.
  bind_address "auto" picks the private address of this PC. 127.0.0.1 is allowed for testing.
- POST /progress appends a quiz result to D:\WKP\Teacher\data\progress.json.
- POST /progress also accepts kind "practice" (learner marked a practice section done).
- GET /unlock-state returns only {unlock_enabled, completed lesson keys} for the learner's own
  browser (used to open the next lesson). It is NOT the viewer.
- GET /progress-view is the viewer for Zac. OFF unless config.json says true (default false).
  Her consent has not been asked yet. Leave it false until she says yes.
"""
import ipaddress
import json
import os
import socket
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "build")
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
PROGRESS = os.path.join(DATA, "progress.json")
PIDFILE = os.path.join(DATA, "server.pid")
LOCK = threading.Lock()
MAX_BODY = 2000


def load_config():
    cfg = {"port": 8800, "bind_address": "auto", "progress_viewer_enabled": False, "unlock_enabled": True}
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as f:
        cfg.update(json.load(f))
    cfg["port"] = int(cfg["port"])
    cfg["progress_viewer_enabled"] = cfg["progress_viewer_enabled"] is True
    cfg["unlock_enabled"] = cfg["unlock_enabled"] is not False  # default ON, only a literal false turns it off
    return cfg


def private_lan_addresses():
    found = []
    try:
        infos = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)
    except socket.gaierror:
        infos = []
    for info in infos:
        ip = info[4][0]
        a = ipaddress.ip_address(ip)
        # is_private includes 100.64/10? No: that range is CGNAT/Tailscale, excluded below.
        if a.is_private and not a.is_loopback and not a.is_link_local and a not in ipaddress.ip_network("100.64.0.0/10"):
            if ip not in found:
                found.append(ip)
    return found


def choose_bind(cfg):
    want = cfg["bind_address"]
    if want == "auto":
        addrs = private_lan_addresses()
        if not addrs:
            sys.exit("No private LAN address found. Connect to the home network, or set bind_address in config.json.")
        return addrs[0]
    a = ipaddress.ip_address(want)
    if a.is_unspecified:
        sys.exit("Refusing to bind to all addresses. Use a private LAN address.")
    if not (a.is_private or a.is_loopback):
        sys.exit("Refusing to bind to a non-private address: " + want)
    return want


def read_progress():
    if not os.path.exists(PROGRESS):
        return []
    with open(PROGRESS, encoding="utf-8") as f:
        return json.load(f)


def make_handler(cfg):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=BUILD, **kw)

        def _send(self, code, body, ctype="application/json"):
            data = body.encode("utf-8") if isinstance(body, str) else body
            self.send_response(code)
            self.send_header("Content-Type", ctype + "; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            path = self.path.split("?")[0]
            if path == "/progress-view":
                if not cfg["progress_viewer_enabled"]:
                    return self._send(404, "Not found", "text/plain")
                with LOCK:
                    return self._send(200, json.dumps(read_progress(), indent=2))
            if path == "/unlock-state":
                with LOCK:
                    rows = read_progress()
                done = sorted({r["lesson"] for r in rows if r.get("passed") is True})
                return self._send(200, json.dumps({"unlock_enabled": cfg["unlock_enabled"], "completed": done}))
            if path == "/progress":
                return self._send(405, "POST only", "text/plain")
            return super().do_GET()

        def do_POST(self):
            if self.path.split("?")[0] != "/progress":
                return self._send(404, "Not found", "text/plain")
            try:
                n = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                n = 0
            if n <= 0 or n > MAX_BODY:
                return self._send(400, '{"error":"bad size"}')
            try:
                d = json.loads(self.rfile.read(n).decode("utf-8"))
                lesson = d["lesson"]
                score, total, passed = d["score"], d["total"], d["passed"]
                kind = d.get("kind", "quiz")
                ok = (isinstance(lesson, str) and 0 < len(lesson) <= 60
                      and all(c.isalnum() or c in "-_/" for c in lesson)
                      and isinstance(score, int) and isinstance(total, int)
                      and not isinstance(score, bool) and not isinstance(total, bool)
                      and 0 <= score <= total <= 50 and isinstance(passed, bool)
                      and kind in ("quiz", "practice"))
            except Exception:
                ok = False
            if not ok:
                return self._send(400, '{"error":"bad data"}')
            # Store only lesson, score, pass/fail and time. Nothing else is kept.
            row = {"lesson": lesson, "kind": kind, "score": score, "total": total, "passed": passed,
                   "time": time.strftime("%Y-%m-%d %H:%M:%S")}
            with LOCK:
                os.makedirs(DATA, exist_ok=True)
                rows = read_progress()
                rows.append(row)
                tmp = PROGRESS + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    json.dump(rows, f, indent=2)
                os.replace(tmp, PROGRESS)
            return self._send(200, '{"saved":true}')

    return Handler


def main():
    cfg = load_config()
    if not os.path.isdir(BUILD):
        sys.exit("No build folder. Run start_teacher.bat (it builds the site first).")
    bind = choose_bind(cfg)
    os.makedirs(DATA, exist_ok=True)
    srv = ThreadingHTTPServer((bind, cfg["port"]), make_handler(cfg))
    with open(PIDFILE, "w") as f:
        f.write(str(os.getpid()))
    print("Teacher is running.")
    print("  Open on this PC or any device on the home network: http://%s:%d/" % (bind, cfg["port"]))
    print("  Progress viewer enabled: %s" % cfg["progress_viewer_enabled"])
    print("  Lesson unlocking enabled: %s" % cfg["unlock_enabled"])
    print("  To stop: close this window, or press Ctrl+C, or double-click stop_teacher.bat")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()
        try:
            os.remove(PIDFILE)
        except OSError:
            pass
        print("Teacher stopped.")


if __name__ == "__main__":
    main()
