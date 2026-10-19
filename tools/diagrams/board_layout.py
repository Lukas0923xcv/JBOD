"""Generates docs/images/board-layout.svg: suggested placement on the mounting board, to scale."""

import os
from svg import MUTED, INK, document, rect, text

S = 2.0          # px per mm
OX, OY = 70, 110  # board origin in px
BW, BH = 420, 300  # board size in mm


def mm(x, y):
    return OX + x * S, OY + y * S


def part(x, y, w, h, title, sub, fill, term_side=None, term_label=""):
    px, py = mm(x, y)
    out = [rect(px, py, w * S, h * S, fill=fill, stroke="#5f5f5a", rx=5)]
    out.append(text(px + w * S / 2, py + h * S / 2 - 4, title, 14, 700, anchor="middle"))
    out.append(text(px + w * S / 2, py + h * S / 2 + 14, sub, 11.5, fill=MUTED, anchor="middle"))
    if term_side == "right":
        out.append(rect(px + w * S - 14, py + 8, 10, h * S - 16, fill="#3d3d3a", stroke="none", rx=2))
        out.append(text(px + w * S - 20, py + h * S - 10, term_label, 10.5, fill=MUTED, anchor="end"))
    return out


body = [
    text(30, 36, "Board layout (top view, to scale)", 20, 700),
    text(30, 58, "Suggested placement on a 420 × 300 mm insulating board, mounted inside the earthed enclosure. "
                 "Footprints are approximate: check your parts before drilling.", 12.5, fill=MUTED),
    text(30, 76, "Keep ≥ 20 mm around each supply for airflow (dashed outline). Terminal strips face the DC side to keep runs short.",
         12.5, fill=MUTED),
]

bx, by = mm(0, 0)
body.append(rect(bx, by, BW * S, BH * S, fill="#e9dcc3", stroke="#9b8660", rx=8, sw=2))

# Clearance halos around the supplies
for x, y, w, h in [(70, 25, 215, 115), (70, 170, 159, 97)]:
    hx, hy = mm(x - 20, y - 20)
    body.append(rect(hx, hy, (w + 40) * S, (h + 40) * S, fill="none", stroke="#3f7cc0", rx=10,
                     sw=1.5, extra='stroke-dasharray="6 5"'))

body += part(70, 25, 215, 115, "RSP-200-12", "215 × 115 mm", "#efefea", "right", "terminals")
body += part(70, 170, 159, 97, "LRS-150F-5", "159 × 97 mm", "#efefea", "right", "terminals")
body += part(305, 25, 100, 150, "Blue Sea 5026", "≈ 100 × 150 mm", "#e4e4de")
body += part(10, 40, 40, 60, "Inlet", "in wall", "#d9d9d3")
for i in range(3):
    px, py = mm(18, 125 + i * 16)
    body.append(rect(px, py, 24 * S, 10 * S, fill="#f6a623", stroke="#9a6206", rx=3))
body.append(text(mm(30, 185)[0], mm(30, 185)[1], "AC WAGOs", 11, 600, fill=MUTED, anchor="middle"))
px, py = mm(270, 215)
body.append(rect(px, py, 24 * S, 10 * S, fill="#f6a623", stroke="#9a6206", rx=3))
for i in range(2):
    qx, qy = mm(315, 205 + i * 22)
    body.append(rect(qx, qy, 60 * S, 12 * S, fill="#3a3a38", stroke="#1d1d1c", rx=10))
body.append(text(mm(330, 265)[0], mm(330, 265)[1], "+5 V split and inline fuses", 11, 600, fill=MUTED, anchor="middle"))

# Pigtails leave the board edge towards the backplane
ex, ey = mm(BW, 100)
body.append(f'<path d="M{ex},{ey} l40,0" stroke="#5f5f5a" stroke-width="3" marker-end="url(#arr)"/>')
body.append(text(ex + 46, ey - 8, "pigtails A1, A2", 11.5, 600))
body.append(text(ex + 46, ey + 8, "through a grommet", 11.5, fill=MUTED))
ex2, ey2 = mm(BW, 150)
body.append(f'<path d="M{ex2},{ey2} l40,0" stroke="#5f5f5a" stroke-width="3" marker-end="url(#arr)"/>')
body.append(text(ex2 + 46, ey2 + 4, "ground bond to server", 11.5, 600))
cx, cy = mm(0, 70)
body.append(f'<path d="M{cx - 40},{cy} l38,0" stroke="#3c3c3a" stroke-width="7" stroke-linecap="round"/>')
body.append(text(cx - 44, cy - 26, "mains", 11.5, 600))
body.append(text(cx - 44, cy - 12, "cord", 11.5, 600))

# Dimension lines
x1, y1 = mm(0, BH)
x2, _ = mm(BW, BH)
body.append(f'<path d="M{x1},{y1 + 22} L{x2},{y1 + 22}" stroke="{INK}" stroke-width="1.2" marker-start="url(#dim)" marker-end="url(#dim)"/>')
body.append(text((x1 + x2) / 2, y1 + 40, "420 mm", 12.5, 600, anchor="middle"))
x3, y3 = mm(BW, 0)
body.append(f'<path d="M{x3 + 215},{y3} L{x3 + 215},{y1}" stroke="{INK}" stroke-width="1.2" marker-start="url(#dim)" marker-end="url(#dim)"/>')
body.append(text(x3 + 205, (y3 + y1) / 2, "300 mm", 12.5, 600, anchor="middle", extra=f'transform="rotate(-90 {x3 + 205} {(y3 + y1) / 2})"'))

defs = '''<defs>
<marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#5f5f5a"/></marker>
<marker id="dim" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#1b1b1a"/></marker>
</defs>'''

svg = document(1180, 790, defs + "\n".join(body), "Board layout, top view",
               "To-scale placement on a 420 by 300 mm board: RSP-200-12 top left, LRS-150F-5 below it, "
               "Blue Sea 5026 fuse block on the right, inlet and AC lever nuts on the left edge, "
               "+5 V split and inline fuses bottom right, with 20 mm airflow clearance around each supply.")
out = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "images", "board-layout.svg")
open(out, "w").write(svg)
print("wrote", os.path.normpath(out))
