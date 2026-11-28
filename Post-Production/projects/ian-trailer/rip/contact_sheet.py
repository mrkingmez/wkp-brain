"""contact_sheet.py FRAMES_DIR OUT_PREFIX first last [cols] -> OUT_PREFIX.png, tiles 640x360 with frame numbers and times."""
import sys, cv2, numpy as np
d, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 4
idx = list(range(a, b + 1))
rows = (len(idx) + cols - 1) // cols
sheet = np.zeros((rows * 360, cols * 640, 3), np.uint8)
for k, i in enumerate(idx):
    im = cv2.resize(cv2.imread(f"{d}/f{i:03d}.png"), (640, 360), interpolation=cv2.INTER_AREA)
    cv2.putText(im, f"f{i} {i/24:.2f}s", (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    r, c = divmod(k, cols)
    sheet[r * 360:(r + 1) * 360, c * 640:(c + 1) * 640] = im
cv2.imwrite(out, sheet)
