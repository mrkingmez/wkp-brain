"""Scout on the PC: the state machine plus a stand-in screen, no hardware.

    python scout_sim.py                 open the window
    python scout_sim.py --headless      print what Scout would show for every mock scenario, then exit

Edit any file in mock_data\\ while the window is open and Scout re-reads it within a second.
Buttons: pick a scenario, force evening (to see the recap), reset Scout's memory (to replay event reactions).
"""
import datetime as dt
import json
import sys
from pathlib import Path

import scout_state as ss
import sprites

HERE = Path(__file__).parent
MOCK = HERE / "mock_data"
PX = 18                     # screen pixels per sprite pixel
W, H = 18 * PX, 14 * PX


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def headless():
    for f in sorted(MOCK.glob("*.json")):
        mem = {}
        for label, hour in (("day", 10), ("evening", 20)):
            now = dt.datetime.combine(dt.date.today(), dt.time(hour, 0))
            view, mem = ss.step(load(f), mem, now)
            print(f"{f.stem:<22} {label:<8} {view['mood']:<9} overlays={view['overlays']} load={view['load']}")
            print(f"{'':<31}line: {view['line']}")
            print(f"{'':<31}why:  {'; '.join(view['reasons'])}")


def gui():
    import tkinter as tk

    root = tk.Tk()
    root.title("Scout - PC sim")
    root.configure(bg="#1d1f24")
    files = sorted(MOCK.glob("*.json"))
    choice = tk.StringVar(value=files[0].name)
    evening = tk.BooleanVar(value=False)
    st = dict(mem={}, mtime=0, data=None, view=None, tick=0, file=None)

    bar = tk.Frame(root, bg="#1d1f24")
    bar.pack(fill="x", padx=10, pady=6)
    tk.OptionMenu(bar, choice, *[f.name for f in files]).pack(side="left")
    tk.Checkbutton(bar, text="Evening", variable=evening, bg="#1d1f24", fg="white", selectcolor="#333").pack(side="left", padx=8)
    tk.Button(bar, text="Reset memory", command=lambda: st.update(mem={}, mtime=0)).pack(side="left")

    cv = tk.Canvas(root, width=W + 40, height=H + 80, bg="#101114", highlightthickness=0)
    cv.pack(padx=10)
    mood_lbl = tk.Label(root, font=("Segoe UI", 14, "bold"), bg="#1d1f24", fg="white")
    mood_lbl.pack()
    line_lbl = tk.Label(root, font=("Segoe UI", 12), bg="#1d1f24", fg="#ffe9a8", wraplength=380)
    line_lbl.pack(pady=4)
    why_lbl = tk.Label(root, font=("Consolas", 9), bg="#1d1f24", fg="#9aa3ad", justify="left", wraplength=380)
    why_lbl.pack(pady=(0, 10))

    def refresh_state():
        f = MOCK / choice.get()
        m = f.stat().st_mtime
        if f != st["file"] or m != st["mtime"]:
            try:
                st["data"] = load(f)
            except (ValueError, OSError) as e:          # half-saved edit: keep the last good data
                why_lbl.config(text=f"could not read {f.name}: {e}")
                return
            st.update(file=f, mtime=m)
        now = dt.datetime.now()
        if evening.get():
            now = now.replace(hour=20)
        st["view"], st["mem"] = ss.step(st["data"], st["mem"], now, st["tick"])
        v = st["view"]
        mood_lbl.config(text=v["mood"] + ("  +  " + " + ".join(v["overlays"]) if v["overlays"] else ""))
        line_lbl.config(text=f"“{v['line']}”")
        c = v["counts"]
        why_lbl.config(text="why: " + "; ".join(v["reasons"]) + f"\nload {v['load']} | overdue {c['overdue']} | "
                       f"blocked {c['blocked']} | calendar today {c['calendar_today']} | decisions {c['decisions']}")

    def draw():
        v = st["view"]
        cv.delete("all")
        if not v:
            return
        frames = sprites.FRAMES[v["mood"]]
        grid = frames[(st["tick"] // 3) % len(frames)]
        special = "SPECIAL" in v["overlays"]
        bounce = 0
        if v["mood"] == "THRIVING":
            bounce = -PX // 2 if (st["tick"] // 3) % 2 else 0
        if special:
            bounce = -PX if (st["tick"] // 2) % 2 else 0
        ox, oy = 20, 60 + bounce
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                if ch != ".":
                    cv.create_rectangle(ox + x * PX, oy + y * PX, ox + (x + 1) * PX, oy + (y + 1) * PX,
                                        fill=sprites.COLORS[ch], outline="")
        if special:     # confetti, offset by tick so it twinkles
            cols = ["#ff5d73", "#ffd23f", "#3bceac", "#6c8cff"]
            for i in range(14):
                x = (i * 53 + st["tick"] * 7) % (W + 20)
                y = (i * 37 + st["tick"] * 11) % 60
                cv.create_rectangle(x, y, x + 8, y + 8, fill=cols[i % 4], outline="")
        if "REACTION" in v["overlays"]:
            cv.create_oval(W - 40, 4, W + 30, 54, fill="#ffd23f", outline="")
            cv.create_text(W - 5, 29, text="!", font=("Segoe UI", 26, "bold"), fill="#101114")
        if "RECAP" in v["overlays"]:
            cv.create_text(40, 30, text="★", font=("Segoe UI", 28), fill="#ffd23f")

    def loop():
        st["tick"] += 1
        if st["tick"] % 4 == 1:
            refresh_state()
        draw()
        root.after(250, loop)

    loop()
    root.mainloop()


if __name__ == "__main__":
    headless() if "--headless" in sys.argv else gui()
