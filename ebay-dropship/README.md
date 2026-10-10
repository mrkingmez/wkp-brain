# ebay-dropship

WKP eBay dropship venture (working name WKP Commerce). Read `CLAUDE.md` first.

- `decisions-queue.md`: items waiting on Zac
- `data/`: suppliers, candidates, listings, orders, ledger CSVs, fee table
- `research/`: trends.md, per-run reports, scheduled-task prompt
- `tools/`: `pricing.py` (pricing plus tests), `ebay_api.py` (eBay Sell/Buy API client, sandbox by default, `--dry-run` on writes)
- `reports/`, `logs/`: daily reports and API logs

Setup: `pip install -r tools/requirements.txt`. Set the EBAY_* variables from `tools/.env.example` in your environment (do not commit a .env).
Tests: `python tools/pricing.py --test`
