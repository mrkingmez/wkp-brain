"""Offline demo data. FICTIONAL issuers, people, prices and bars (seeded random numbers). No network, no keys.
Also holds the Form 4 XML builder the tests use."""
import datetime as dt
import math
import random
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")


def owner_xml(cik, name, director=False, officer=False, ten=False, other=False, title="", relationship=True):
    rel = ""
    if relationship:
        rel = ("<reportingOwnerRelationship><isDirector>%d</isDirector><isOfficer>%d</isOfficer><isTenPercentOwner>%d</isTenPercentOwner>"
               "<isOther>%d</isOther>%s</reportingOwnerRelationship>") % (director, officer, ten, other, ("<officerTitle>%s</officerTitle>" % title) if title else "")
    return "<reportingOwner><reportingOwnerId><rptOwnerCik>%s</rptOwnerCik><rptOwnerName>%s</rptOwnerName></reportingOwnerId>%s</reportingOwner>" % (cik, name, rel)


def txn_xml(date, code="P", shares=1000, price=10.0, post=5000, ad="A", fn=()):
    refs = "".join('<footnoteId id="%s"/>' % i for i in fn)
    pr = "<transactionPricePerShare><value>%s</value>%s</transactionPricePerShare>" % (price, refs) if price is not None else ""
    return ("<nonDerivativeTransaction><securityTitle><value>Common Stock</value></securityTitle><transactionDate><value>%s</value></transactionDate>"
            "<transactionCoding><transactionFormType>4</transactionFormType><transactionCode>%s</transactionCode></transactionCoding>"
            "<transactionAmounts><transactionShares><value>%s</value></transactionShares>%s"
            "<transactionAcquiredDisposedCode><value>%s</value></transactionAcquiredDisposedCode></transactionAmounts>"
            "<postTransactionAmounts><sharesOwnedFollowingTransaction><value>%s</value></sharesOwnedFollowingTransaction></postTransactionAmounts>"
            "<ownershipNature><directOrIndirectOwnership><value>D</value></directOrIndirectOwnership></ownershipNature></nonDerivativeTransaction>") % (date, code, shares, pr, ad, post)


def form4_xml(issuer_cik, issuer_name, ticker, owners, txns, doc="4", period="2026-10-01", a10b5=None, deriv=0, footnotes=None):
    fnx = ("<footnotes>%s</footnotes>" % "".join('<footnote id="%s">%s</footnote>' % (k, v) for k, v in footnotes.items())) if footnotes else ""
    d = "<derivativeTable>%s</derivativeTable>" % ("<derivativeTransaction><securityTitle><value>Option</value></securityTitle></derivativeTransaction>" * deriv) if deriv else ""
    a = "<aff10b5One>%s</aff10b5One>" % a10b5 if a10b5 is not None else ""
    return ('<?xml version="1.0"?><ownershipDocument><schemaVersion>X0508</schemaVersion><documentType>%s</documentType><periodOfReport>%s</periodOfReport>%s'
            "<issuer><issuerCik>%s</issuerCik><issuerName>%s</issuerName><issuerTradingSymbol>%s</issuerTradingSymbol></issuer>%s"
            "<nonDerivativeTable>%s</nonDerivativeTable>%s%s</ownershipDocument>") % (doc, period, a, issuer_cik, issuer_name, ticker, "".join(owners), "".join(txns), d, fnx)


def demo_filings():
    """List of (xml, meta). Every name here is invented."""
    F = []

    def add(xml, acc, fdate, doc="4"):
        F.append((xml, {"accession": acc, "filing_date": fdate, "accepted_utc": fdate + "T17:30:00", "form_type": doc,
                        "source_url": "demo://fictional/" + acc}))
    # ZEPH Robotics: three distinct people, CEO among them, inside the window -> COUNTED (officers and directors, CEO involved)
    z = ("0009000001", "Zephyr Demo Robotics Inc", "ZEPH")
    add(form4_xml(*z, [owner_xml("1000001", "Alder Quinn", officer=True, title="Chief Executive Officer")], [txn_xml("2026-10-08", shares=5000, price=12.5, post=45000)]), "0009990001-26-000001", "2026-10-12")
    add(form4_xml(*z, [owner_xml("1000002", "Birch Tamsin", director=True)], [txn_xml("2026-10-09", shares=2000, price=12.6, post=22000)]), "0009990001-26-000002", "2026-10-13")
    add(form4_xml(*z, [owner_xml("1000003", "Cedar Wynn", officer=True, title="Chief Financial Officer")], [txn_xml("2026-10-14", shares=1500, price=12.9, post=9000), txn_xml("2026-10-14", code="S", shares=100, price=12.9, post=8900, ad="D")], a10b5=0), "0009990001-26-000003", "2026-10-15")
    # same person twice, plus one other: only 2 distinct -> WATCH
    q = ("0009000002", "Quillon Demo Foods Inc", "QUIL")
    add(form4_xml(*q, [owner_xml("1000010", "Dune Arlo", director=True)], [txn_xml("2026-10-20", price=8.0, shares=3000, post=30000)]), "0009990002-26-000001", "2026-10-21")
    add(form4_xml(*q, [owner_xml("1000010", "Dune Arlo", director=True)], [txn_xml("2026-10-22", price=8.1, shares=3000, post=33000)]), "0009990002-26-000002", "2026-10-23")
    add(form4_xml(*q, [owner_xml("1000011", "Ember Sol", officer=True, title="VP Sales")], [txn_xml("2026-10-23", price=8.2, shares=900, post=7000)]), "0009990002-26-000003", "2026-10-26")
    # three insiders but one filing has no relationship flags -> FAIL_UNKNOWN_TYPE
    b = ("0009000003", "Braxton Demo Metals Corp", "BRAX")
    add(form4_xml(*b, [owner_xml("1000020", "Flint Ora", officer=True, title="Chief Operating Officer")], [txn_xml("2026-10-27", price=20.0, shares=800, post=6000)]), "0009990003-26-000001", "2026-10-28")
    add(form4_xml(*b, [owner_xml("1000021", "Gale Pim", director=True)], [txn_xml("2026-10-28", price=20.1, shares=700, post=5000)]), "0009990003-26-000002", "2026-10-29")
    add(form4_xml(*b, [owner_xml("1000022", "Heath Rue", relationship=False)], [txn_xml("2026-10-28", price=20.1, shares=650, post=4000)]), "0009990003-26-000003", "2026-10-30")
    # closed-end fund with entity owners -> COUNTED but sponsor_or_fund flagged
    fu = ("0009000004", "Demo Income Fund", "DMIF")
    add(form4_xml(*fu, [owner_xml("1000030", "Harbor Demo Capital LLC", ten=True), owner_xml("1000031", "Iris Vale", director=True)], [txn_xml("2026-11-02", price=12.0, shares=100000, post=100100)]), "0009990004-26-000001", "2026-11-04")
    add(form4_xml(*fu, [owner_xml("1000032", "Jade Moor", director=True)], [txn_xml("2026-11-03", price=12.1, shares=500, post=5500)]), "0009990004-26-000002", "2026-11-05")
    # three insiders spread over 25 days -> no cluster (window edge)
    m = ("0009000005", "Monteverde Demo Energy Inc", "MONT")
    for i, (d, fd) in enumerate((("2026-09-01", "2026-09-03"), ("2026-09-14", "2026-09-15"), ("2026-09-27", "2026-09-29")), 1):
        add(form4_xml(*m, [owner_xml("10000%d0" % (40 + i), "Mont Person %d" % i, director=True)], [txn_xml(d, price=30.0, shares=400, post=4400)]), "0009990005-26-00000%d" % i, fd)
    # amendment: original ASH cluster had 3, a 4/A removes one buyer's P (changed to S) so only 2 remain
    a = ("0009000006", "Ashgrove Demo Bio Inc", "ASHG")
    add(form4_xml(*a, [owner_xml("1000050", "Kit Lane", officer=True, title="CEO")], [txn_xml("2026-10-05", price=5.0, shares=2000, post=12000)]), "0009990006-26-000001", "2026-10-07")
    add(form4_xml(*a, [owner_xml("1000051", "Lark Dell", director=True)], [txn_xml("2026-10-06", price=5.0, shares=2000, post=12000)]), "0009990006-26-000002", "2026-10-07")
    add(form4_xml(*a, [owner_xml("1000052", "Moss Rey", director=True)], [txn_xml("2026-10-06", price=5.0, shares=2000, post=12000)]), "0009990006-26-000003", "2026-10-08")
    add(form4_xml(*a, [owner_xml("1000052", "Moss Rey", director=True)], [txn_xml("2026-10-06", code="S", price=5.0, shares=2000, post=10000, ad="D")], doc="4/A"), "0009990006-26-000004", "2026-10-20", doc="4/A")
    # dead ticker: counted cluster with no bars
    g = ("0009000007", "Ghostline Demo Corp", "GHST")
    for i, (cik, d) in enumerate((("1000060", "2026-10-12"), ("1000061", "2026-10-13"), ("1000062", "2026-10-13")), 1):
        add(form4_xml(*g, [owner_xml(cik, "Ghost Person %d" % i, director=True)], [txn_xml(d, price=3.0, shares=5000, post=30000)]), "0009990007-26-00000%d" % i, "2026-10-15")
    # very recent cluster: forward returns still pending
    r = ("0009000008", "Recenta Demo Systems Inc", "RECN")
    for i, (cik, d, fd) in enumerate((("1000070", "2026-11-18", "2026-11-19"), ("1000071", "2026-11-19", "2026-11-20"), ("1000072", "2026-11-20", "2026-11-24")), 1):
        add(form4_xml(*r, [owner_xml(cik, "Recent Person %d" % i, officer=True, title="Director of Ops")], [txn_xml(d, price=40.0, shares=300, post=3300)]), "0009990008-26-00000%d" % i, fd)
    # ruling cases (all fictional): an offering-style same-day same-price group, a 10 percent owner who does not count, a late filing, a new listing
    o = ("0009000011", "Offerco Demo Holdings Inc", "OFFR")
    for i, cik in enumerate(("1000090", "1000091", "1000092"), 1):
        add(form4_xml(*o, [owner_xml(cik, "Offer Person %d" % i, director=True)], [txn_xml("2026-10-14", price=15.0, shares=2000, post=2000, fn=("F1",))],
                      footnotes={"F1": "Shares acquired in the initial public offering."}), "0009990011-26-00000%d" % i, "2026-10-15")
    t = ("0009000012", "Tenco Demo Inc", "TENC")
    add(form4_xml(*t, [owner_xml("1000100", "Ten Person One", director=True)], [txn_xml("2026-10-14", price=9.0, shares=500, post=5500)]), "0009990012-26-000001", "2026-10-15")
    add(form4_xml(*t, [owner_xml("1000101", "Ten Person Two", officer=True, title="Controller")], [txn_xml("2026-10-15", price=9.1, shares=500, post=4500)]), "0009990012-26-000002", "2026-10-16")
    add(form4_xml(*t, [owner_xml("1000102", "Ten Person Three", ten=True)], [txn_xml("2026-10-15", price=9.1, shares=90000, post=900000)]), "0009990012-26-000003", "2026-10-16")
    la = ("0009000013", "Latenco Demo Inc", "LATE")
    add(form4_xml(*la, [owner_xml("1000110", "Late Person One", director=True)], [txn_xml("2026-10-01", price=7.0, shares=400, post=4400)]), "0009990013-26-000001", "2026-10-02")
    add(form4_xml(*la, [owner_xml("1000111", "Late Person Two", director=True)], [txn_xml("2026-10-02", price=7.1, shares=400, post=4400)]), "0009990013-26-000002", "2026-10-05")
    add(form4_xml(*la, [owner_xml("1000112", "Late Person Three", director=True)], [txn_xml("2026-10-02", price=7.1, shares=400, post=4400)]), "0009990013-26-000003", "2026-10-26")
    n = ("0009000014", "Newlist Demo Corp", "NEWC")
    for i, (cik, d, fd) in enumerate((("1000120", "2026-10-27", "2026-10-28"), ("1000121", "2026-10-28", "2026-10-29"), ("1000122", "2026-10-29", "2026-10-30")), 1):
        add(form4_xml(*n, [owner_xml(cik, "New Person %d" % i, director=True)], [txn_xml(d, price=21.0, shares=700, post=700 + 100 * i)]), "0009990014-26-00000%d" % i, fd)
    # junk rows: a sale only filing, and a derivative only filing
    add(form4_xml("0009000009", "Sellco Demo Inc", "SELL", [owner_xml("1000080", "Seller One", officer=True, title="CEO")], [txn_xml("2026-10-10", code="S", ad="D")]), "0009990009-26-000001", "2026-10-12")
    add(form4_xml("0009000010", "Optco Demo Inc", "OPTN", [owner_xml("1000081", "Option Holder", director=True)], [], deriv=2), "0009990010-26-000001", "2026-10-12")
    return F


def make_daily(seed, start_price, start, end, drift=0.0003, vol=0.012, volume=2_000_000):
    rng = random.Random(seed)
    bars, price, d = [], start_price, start
    while d <= end:
        if d.weekday() < 5:
            o = price
            c = o * math.exp(drift + rng.gauss(0, vol))
            h = max(o, c) * (1 + abs(rng.gauss(0, 0.004)))
            l = min(o, c) * (1 - abs(rng.gauss(0, 0.004)))
            t = dt.datetime(d.year, d.month, d.day, 0, 0, tzinfo=ET).astimezone(dt.timezone.utc)
            bars.append({"t": t, "o": o, "h": h, "l": l, "c": c, "v": int(volume * (0.6 + rng.random()))})
            price = c
        d += dt.timedelta(days=1)
    return bars


DEMO_TICKERS = ["ZEPH", "QUIL", "BRAX", "DMIF", "MONT", "ASHG", "RECN", "OFFR", "TENC", "LATE"]   # GHST is deliberately absent: dead ticker, no bars
BREADTH = ["DEMA", "DEMB", "DEMC", "DEMD", "DEME", "DEMF", "DEMG", "DEMH", "DEMI", "DEMJ", "DEMK"]


def demo_bars(benchmark="SPY"):
    start, end = dt.date(2025, 6, 2), dt.date(2026, 11, 25)
    out = {benchmark: make_daily(1, 450.0, start, end), "IWM": make_daily(2, 210.0, start, end, drift=0.0002, vol=0.016)}
    for i, s in enumerate(DEMO_TICKERS + BREADTH):
        out[s] = make_daily(100 + i, 10 + 3 * i, start, end, drift=0.0004 if i % 2 else 0.0001)
    out["NEWC"] = make_daily(190, 21.0, dt.date(2026, 9, 1), end)       # first bar 2026-09-01: about 40 trading days old at its signal, a new listing
    return out
