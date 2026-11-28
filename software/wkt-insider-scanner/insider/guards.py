"""Startup guards: SEC host allowlist, User-Agent by environment variable NAME, live-pull gate.
Error messages name variables and hosts that are public, never a value taken from the environment."""
import os
import urllib.parse

ALLOWED_HOSTS = frozenset({"www.sec.gov", "data.sec.gov"})   # in-code ceiling. Config can only narrow it.
HARD_MAX_RPS = 2.0


class GuardError(RuntimeError):
    pass


def effective_hosts(cfg):
    want = set(cfg["sec"]["allowed_hosts"])
    return frozenset(want & ALLOWED_HOSTS)


def assert_allowed_url(url, hosts=ALLOWED_HOSTS):
    p = urllib.parse.urlparse(url)
    if p.scheme != "https":
        raise GuardError("blocked: only https is allowed")
    if p.hostname not in hosts:
        raise GuardError("blocked: host not on the SEC allowlist: %s" % (p.hostname,))
    if p.username or p.password or (p.port not in (None, 443)):
        raise GuardError("blocked: credentials or a custom port in the URL")
    return url


def effective_rps(cfg):
    v = cfg["sec"]["max_requests_per_second"]
    if not isinstance(v, (int, float)) or isinstance(v, bool) or v <= 0:
        raise GuardError("sec.max_requests_per_second must be a positive number")
    return min(float(v), HARD_MAX_RPS)


def load_user_agent(cfg, environ=None):
    """Read the User-Agent from the environment by NAME. Refuses to run if unset or blank.
    SEC asks for 'Company Name contact@domain', so a value with no @ is refused too (the value is never shown)."""
    environ = os.environ if environ is None else environ
    name = cfg["sec"]["user_agent_env"]
    v = environ.get(name)
    if v is None or not v.strip():
        raise GuardError("environment variable %s is not set. The live pull refuses to run without it. "
                         "Zac supplies a company name and contact email there himself." % name)
    v = v.strip()
    if "@" not in v or any(ord(c) < 32 or ord(c) > 126 for c in v) or len(v) > 200:
        raise GuardError("environment variable %s does not look like 'Company name contact@email' (printable ASCII, with an email)." % name)
    return v


WATCHER_OUTPUT_NAMES = frozenset({"decisions.jsonl", "paper-trades.csv", "state.json"})   # the stock watcher output files: never written, never read for scoring


def assert_own_ledger(outdir, cfg):
    """RULING 8. The insider ledger folder must be its own: not inside the stock watcher folder and not holding the watcher output files."""
    o = os.path.normcase(os.path.realpath(outdir))
    w = os.path.normcase(os.path.realpath(cfg["forward"]["watcher_dir"]))
    if o == w or o.startswith(w + os.sep):
        raise GuardError("the insider ledger folder cannot be inside the stock watcher folder")
    for n in WATCHER_OUTPUT_NAMES:
        if os.path.isfile(os.path.join(outdir, n)):
            raise GuardError("this folder holds the stock watcher output (%s). The insider ledger needs its own folder." % n)
    return True


def live_gate(outdir):
    """The live pull needs the release file written by the trading-director after the terms brief and the User-Agent exist."""
    gate = os.path.join(outdir, "LIVE-OK.flag")
    if not os.path.isfile(gate):
        raise GuardError("live pull is locked until LIVE-OK.flag exists in the insider folder (trading-director writes it after the terms brief and the security pass)")
    stop = os.path.join(outdir, "SEC-STOP.flag")
    if os.path.isfile(stop):
        raise GuardError("a previous run was stopped by an SEC 403 or 429. Read SEC-STOP.flag, wait, then delete it by hand before running again.")
    return True
