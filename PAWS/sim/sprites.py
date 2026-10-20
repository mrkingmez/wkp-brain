"""Scout placeholder pixel art, 18 x 14 grid. Stand-in until the real character art (8 states, 3 frames) exists.

Grids are plain strings so the same data can be packed into firmware later.
  .  empty   B  fur   D  dark (ears, eye, nose, paws)   W  muzzle/belly   T  tongue
"""

THRIVING_A = [  # sitting up, ears up, tail high, tongue out
    "............D..D..",
    "...........DD.DD..",
    "...........BBBBB..",
    ".B........BBBBDBB.",
    "..B.......BBBBBWWD",
    "...B.......BBBWWT.",
    "....BBBBBBBBBB....",
    "...BBBBBBBBBWBB...",
    "...BBBBBBBBBWBB...",
    "...BBBBBBBBBWBB...",
    "....BBBBBBBBBB....",
    "....BB..BB..BB....",
    "....BB..BB..BB....",
    "....DD..DD..DD....",
]
THRIVING_B = [  # tail swung low: the wag
    "............D..D..",
    "...........DD.DD..",
    "...........BBBBB..",
    "..........BBBBDBB.",
    "..........BBBBBWWD",
    "...........BBBWWT.",
    ".BBBBBBBBBBBBB....",
    "...BBBBBBBBBWBB...",
    "...BBBBBBBBBWBB...",
    "...BBBBBBBBBWBB...",
    "....BBBBBBBBBB....",
    "....BB..BB..BB....",
    "....BB..BB..BB....",
    "....DD..DD..DD....",
]
BURIED_A = [  # lying down, ears flat, eyes open: alert, watching
    "..................",
    "..................",
    "..................",
    "..................",
    "..................",
    "..................",
    "............BBBB..",
    "...........DBBDBB.",
    "...........DBBBBWD",
    "..BBBBBBBBBBBBBW..",
    ".BBBBBBBBBBBBBB...",
    "BBBBBBBBBBBBBBBB..",
    "..DD......DDDD....",
    "..................",
]
BURIED_B = [r.replace("DBBDBB", "DBBBBB") if i == 7 else r for i, r in enumerate(BURIED_A)]  # slow blink

FRAMES = {"THRIVING": [THRIVING_A, THRIVING_B], "BURIED": [BURIED_A, BURIED_A, BURIED_A, BURIED_B]}
COLORS = {"B": "#b5793f", "D": "#3a2414", "W": "#f2e3c6", "T": "#e8798a"}

for _name, _frames in FRAMES.items():
    for _f in _frames:
        assert len(_f) == 14 and all(len(r) == 18 for r in _f), f"bad sprite grid in {_name}"
