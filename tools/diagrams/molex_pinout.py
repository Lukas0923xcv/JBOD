"""Generates docs/images/molex-pinout.svg: what each pigtail wire is and where it lands."""

import os
from svg import WIRES, MUTED, INK, document, rect, text

rows = [
    (1, "12V", "Yellow", "+12 V", "Fuse block branch screw (A1 → pos. 1, A2 → pos. 2)", "7.5 A blade fuse"),
    (2, "GND", "Black", "Ground", "Negative bus branch screw", "not fused"),
    (3, "GND", "Black", "Ground", "Negative bus branch screw", "not fused"),
    (4, "5V", "Red", "+5 V", "Inline fuse holder → +5 V WAGO split", "5 A inline fuse"),
]

parts = [
    text(30, 36, "Molex pigtail: pin-out and termination", 20, 700),
    text(30, 58, "Same for A1 and A2. Check the colours against the moulded pin numbers before you crimp.", 12.5, fill=MUTED),
]

# Connector body (seen from the wire side), chamfered corners on top edge.
x0, y0, w, h, c = 60, 96, 240, 74, 14
parts.append(f'<path d="M{x0 + c},{y0} L{x0 + w - c},{y0} L{x0 + w},{y0 + c} L{x0 + w},{y0 + h} '
             f'L{x0},{y0 + h} L{x0},{y0 + c} Z" fill="#f4f1e6" stroke="#8c8672" stroke-width="2"/>')
parts.append(text(x0 + w / 2, y0 - 10, "female 4-pin Molex (plugs into the backplane)", 11.5, fill=MUTED, anchor="middle"))
pin_x = [x0 + 36 + i * 56 for i in range(4)]
for (pin, kind, *_), px in zip(rows, pin_x):
    parts.append(f'<circle cx="{px}" cy="{y0 + 30}" r="12" fill="#e7e2cf" stroke="#8c8672" stroke-width="1.5"/>')
    parts.append(text(px, y0 + 35, str(pin), 13, 700, anchor="middle"))
    core, edge = WIRES[kind]
    parts.append(f'<line x1="{px}" y1="{y0 + h}" x2="{px}" y2="{y0 + h + 40}" stroke="{edge}" stroke-width="8" stroke-linecap="round"/>')
    parts.append(f'<line x1="{px}" y1="{y0 + h}" x2="{px}" y2="{y0 + h + 40}" stroke="{core}" stroke-width="5" stroke-linecap="round"/>')
parts.append(text(x0 + w / 2, y0 + 62, "chamfered corners: keying only", 10.5, fill=MUTED, anchor="middle"))

# Table
tx, ty = 360, 92
cols = [(tx, "Pin"), (tx + 44, "Wire"), (tx + 130, "Carries"), (tx + 210, "Lands on"), (tx + 560, "Protection")]
for x, head in cols:
    parts.append(text(x, ty, head, 12, 700, fill=MUTED))
for i, (pin, kind, colour, carries, lands, prot) in enumerate(rows):
    y = ty + 30 + i * 30
    if i % 2 == 0:
        parts.append(rect(tx - 10, y - 19, 700, 28, fill="#f1f1ec", stroke="none", rx=4))
    core, edge = WIRES[kind]
    parts.append(f'<line x1="{tx + 44}" y1="{y - 4}" x2="{tx + 64}" y2="{y - 4}" stroke="{edge}" stroke-width="7" stroke-linecap="round"/>')
    parts.append(f'<line x1="{tx + 44}" y1="{y - 4}" x2="{tx + 64}" y2="{y - 4}" stroke="{core}" stroke-width="4.5" stroke-linecap="round"/>')
    parts += [text(tx + 8, y, str(pin), 13, 700, anchor="middle"),
              text(tx + 74, y, colour, 12.5),
              text(tx + 130, y, carries, 12.5, 600),
              text(tx + 210, y, lands, 12.5),
              text(tx + 560, y, prot, 12.5, fill=MUTED)]

svg = document(1080, 230, "\n".join(parts), "Molex pigtail pin-out",
               "Pin 1 yellow +12 V to the fuse block through a 7.5 A fuse; pins 2 and 3 black ground "
               "to the negative bus; pin 4 red +5 V through a 5 A inline fuse.")
out = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "images", "molex-pinout.svg")
open(out, "w").write(svg)
print("wrote", os.path.normpath(out))
