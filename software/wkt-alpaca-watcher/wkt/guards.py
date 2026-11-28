"""Startup guards: paper URL assert, key loading by env var NAME only, counted-period gate."""
import os

PAPER_URL = "https://paper-api.alpaca.markets"
KEY_VARS = ("APCA_API_KEY_ID", "APCA_API_SECRET_KEY", "APCA_API_BASE_URL")


class GuardError(RuntimeError):
    pass


def assert_paper_url(url):
    """Exactly the paper URL, nothing else. No live code path exists."""
    if url != PAPER_URL:
        raise GuardError("refusing to start: base URL is not exactly the paper URL")
    return url


def load_env():
    """Return (key_id, secret, base_url). Error messages name variables, never values."""
    missing = [n for n in KEY_VARS if not os.environ.get(n)]
    if missing:
        raise GuardError("missing environment variables: " + ", ".join(missing))
    base = assert_paper_url(os.environ["APCA_API_BASE_URL"])
    return os.environ["APCA_API_KEY_ID"], os.environ["APCA_API_SECRET_KEY"], base


def counted_gate(outdir, flag_present):
    """Counted watch-week scans need the explicit counted flag AND a release file
    written by the trading-director after the security pass and qa-director check."""
    gate = os.path.join(outdir, "GO-COUNTED.flag")
    if not flag_present:
        raise GuardError("counted mode needs --counted")
    if not os.path.isfile(gate):
        raise GuardError("counted scans are locked until GO-COUNTED.flag exists in the watch-week folder")
    return True
