"""Generates docs/images/wiring-diagram.svg: every wire of the 8-drive build in its real colour."""

import os
from svg import (Wiring, circle, document, legend, rect, text, MUTED, INK, PART_EDGE)

FUSE_7A5 = "#8b5a2b"  # ATO colour code: 7.5 A brown
FUSE_5A = "#d2b48c"   # ATO colour code: 5 A tan
FUSE_1A = "#2b2b2b"   # ATO colour code: 1 A black

w = Wiring()
parts = []
labels = []


def terminal(x, y, label, side):
    """Screw terminal dot with a label inside the part."""
    parts.append(circle(x, y, 5, fill="#d9d9d3"))
    dx, anchor = (12, "start") if side == "left" else (-12, "end")
    labels.append(text(x + dx, y + 4.5, label, 12, 600, anchor=anchor))


# --- Mains inlet -----------------------------------------------------------
parts.append(f'<line x1="22" y1="375" x2="60" y2="375" stroke="#3c3c3a" stroke-width="9" stroke-linecap="round"/>')
labels.append(text(22, 470, "Typ 12 → C13 cord", 12, fill=MUTED))
labels.append(text(22, 486, "to wall outlet", 12, fill=MUTED))
parts.append(rect(60, 300, 110, 150))
labels += [text(115, 322, "Schurter DD11", 12.5, 700, anchor="middle"),
           text(115, 438, "switch + 2 × 6.3 A T", 11, fill=MUTED, anchor="middle")]
for y, lab in [(335, "L"), (375, "N"), (415, "PE")]:
    terminal(170, y, lab, "right")

# --- AC lever nuts ---------------------------------------------------------
labels.append(text(240, 312, "WAGO 221", 11.5, 600, fill=MUTED, anchor="middle"))
labels.append(text(115, 286, "1.5 mm² leads, 4.8 mm tabs", 11, fill=MUTED, anchor="middle"))
for y in (335, 375, 415):
    parts.append(rect(220, y - 12, 40, 24, fill="#f6a623", stroke="#9a6206", rx=4))

w.add("L", (170, 335), (220, 335))
w.add("N", (170, 375), (220, 375))
w.add("PE", (170, 415), (220, 415))
w.add("L", (260, 335), (290, 335), (290, 140), (360, 140))
w.add("L", (260, 335), (290, 335), (290, 530), (360, 530))
w.add("N", (260, 375), (310, 375), (310, 180), (360, 180))
w.add("N", (260, 375), (310, 375), (310, 570), (360, 570))
w.add("PE", (260, 415), (330, 415), (330, 220), (360, 220))
w.add("PE", (260, 415), (330, 415), (330, 610), (360, 610))

# --- Power supplies --------------------------------------------------------
def psu(y, name, rating, trim, ac, dc):
    parts.append(rect(360, y, 210, 170, rx=8))
    labels.append(text(465, y + 26, name, 15, 700, anchor="middle"))
    labels.append(text(465, y + 46, rating, 12.5, fill=MUTED, anchor="middle"))
    labels.append(text(465, y + 150, trim, 12, 600, anchor="middle"))
    for yy, lab in ac:
        terminal(360, yy, lab, "left")
    for yy, lab in dc:
        terminal(570, yy, lab, "right")


psu(90, "RSP-200-12", "12 V · 16.7 A", "V.ADJ → 12.15 V",
    [(140, "L"), (180, "N"), (220, "FG")], [(140, "V+"), (210, "V−")])
psu(480, "LRS-150F-5", "5 V · 22 A", "V.ADJ → 5.15 V",
    [(530, "L"), (570, "N"), (610, "FG")], [(510, "V−"), (570, "V+")])

# --- Fuse block ------------------------------------------------------------
parts.append(rect(680, 50, 230, 250, rx=8))
labels.append(text(795, 74, "Blue Sea 5026", 14, 700, anchor="middle"))
parts.append(rect(700, 86, 12, 146, fill="#c8a24a", stroke="#7a5f1c", rx=2))  # + bus
parts.append(rect(700, 262, 205, 12, fill="#8f8f8a", stroke="#4d4d4a", rx=2))  # − bus
labels.append(text(724, 254, "negative bus", 11, fill=MUTED))
for n, y in enumerate((100, 130, 160, 190, 220), start=1):
    parts.append(f'<line x1="712" y1="{y}" x2="736" y2="{y}" stroke="{PART_EDGE}" stroke-width="2"/>')
    if n <= 3:
        colour, rating = (FUSE_7A5, "7.5 A") if n <= 2 else (FUSE_1A, "1 A")
        parts.append(rect(736, y - 8, 40, 16, fill=colour, stroke="#1d1d1c", rx=3))
        labels.append(text(756, y + 4, rating, 10.5, 700, fill="#ffffff", anchor="middle"))
        parts.append(f'<line x1="776" y1="{y}" x2="794" y2="{y}" stroke="{PART_EDGE}" stroke-width="2"/>')
    else:
        parts.append(rect(736, y - 8, 40, 16, fill="none", stroke="#a9a9a3", rx=3,
                          extra='stroke-dasharray="3 3"'))
    parts.append(circle(800, y, 5))
    labels.append(text(724, y - 4, str(n), 9.5, 600, fill=MUTED, anchor="middle"))
labels.append(text(812, 194, "4–12", 11, fill=MUTED))
labels.append(text(812, 208, "unused", 11, fill=MUTED))
parts.append(circle(712, 140, 8, fill="#e0c46e", stroke="#7a5f1c"))  # + stud
labels.append(text(694, 166, "+ stud", 11, 600, fill=MUTED, anchor="end"))
parts.append(circle(712, 268, 9, fill="#bdbdb7", stroke="#4d4d4a"))  # − stud
labels.append(text(712, 316, "− stud", 11, 600, fill=MUTED, anchor="middle"))
for x in (760, 785, 810, 835, 855, 880, 900):
    parts.append(circle(x, 268, 4.5, fill="#d9d9d3", stroke="#4d4d4a"))

w.add("12V", (570, 140), (704, 140))
w.add("GND", (570, 210), (625, 210), (625, 263), (703, 263))
w.add("GND", (570, 510), (645, 510), (645, 273), (703, 273))

# --- 5 V split and inline fuses --------------------------------------------
parts.append(rect(790, 558, 40, 24, fill="#f6a623", stroke="#9a6206", rx=4))
labels.append(text(810, 598, "WAGO", 11, 600, fill=MUTED, anchor="middle"))
for y in (540, 600):
    parts.append(rect(870, y - 9, 60, 18, fill="#3a3a38", stroke="#1d1d1c", rx=9))
    parts.append(rect(887, y - 6, 26, 12, fill=FUSE_5A, stroke="#7d6542", rx=2))
    labels.append(text(900, y + 3.5, "5 A", 9, 700, fill="#3b2a12", anchor="middle"))
labels.append(text(900, 525, "inline fuse holders", 11, fill=MUTED, anchor="middle"))

w.add("5V", (570, 570), (790, 570))
w.add("5V", (830, 565), (850, 565), (850, 540), (870, 540))
w.add("5V", (830, 575), (850, 575), (850, 600), (870, 600))

# --- Molex pigtails and backplane ------------------------------------------
def molex(y, name):
    parts.append(rect(1000, y, 42, 92, fill="#f4f1e6", stroke="#8c8672", rx=4))
    labels.append(text(1021, y - 8, name, 13, 700, anchor="middle"))
    for n in range(4):
        py = y + 15 + 20 * n
        parts.append(rect(1004, py - 6, 12, 12, fill="#e7e2cf", stroke="#8c8672", rx=2))
        labels.append(text(1030, py + 4, str(n + 1), 10.5, 600, fill=MUTED, anchor="middle"))


molex(315, "A1")
molex(435, "A2")
labels.append(text(1021, 548, "Molex pigtails", 11, fill=MUTED, anchor="middle"))
labels.append(text(1021, 562, "(18 AWG)", 11, fill=MUTED, anchor="middle"))
parts.append(rect(1052, 290, 70, 250, fill="#2f6b3a", stroke="#1b3f22", rx=6))
labels.append(text(1087, 415, "Jonsbo N3 backplane · 8 bays", 13, 700, fill="#ffffff",
                   anchor="middle", extra='transform="rotate(-90 1087 415)"'))

# A1: pins at 330 / 350 / 370 / 390, A2: 450 / 470 / 490 / 510
w.add("12V", (806, 100), (960, 100), (960, 330), (1004, 330))
w.add("12V", (806, 130), (930, 130), (930, 450), (1004, 450))
w.add("GND", (880, 274), (880, 350), (1004, 350))
w.add("GND", (855, 274), (855, 370), (1004, 370))
w.add("GND", (810, 274), (810, 470), (1004, 470))
w.add("GND", (785, 274), (785, 490), (1004, 490))
w.add("5V", (930, 540), (975, 540), (975, 390), (1004, 390))
w.add("5V", (930, 600), (985, 600), (985, 510), (1004, 510))

# --- Fans (fuse 3, 1 A) -----------------------------------------------------
parts.append(rect(1000, 140, 160, 110, rx=8))
labels.append(text(1080, 166, "Drive fans", 13, 700, anchor="middle"))
labels.append(text(1080, 184, "2 × 120 mm, 12 V", 11, fill=MUTED, anchor="middle"))
labels.append(text(1080, 200, "≤ 0.3 A each", 11, fill=MUTED, anchor="middle"))
w.add("12V", (806, 160), (1000, 160))
w.add("GND", (900, 262), (900, 236), (1000, 236))

# --- 0 V to PE bond ----------------------------------------------------------
w.add("PE", (240, 427), (240, 450), (835, 450), (835, 274))
labels.append(text(470, 443, "0 V – PE bond (2.5 mm²)", 11.5, 600, anchor="middle"))

# --- Server ----------------------------------------------------------------
parts.append(rect(960, 680, 200, 64, rx=8))
labels.append(text(1060, 707, "Host server", 14, 700, anchor="middle"))
labels.append(text(1060, 726, "bare-metal chassis screw", 11.5, fill=MUTED, anchor="middle"))
parts.append(f'<line x1="1087" y1="540" x2="1087" y2="680" stroke="{MUTED}" stroke-width="2" stroke-dasharray="5 4"/>')
labels.append(text(1095, 615, "SATA data", 11.5, fill=MUTED))
w.add("GND", (760, 274), (760, 712), (960, 712))
labels.append(text(770, 704, "ground bond", 11.5, 600, fill=INK))

# --- Wire tags ---------------------------------------------------------------
labels += [
    text(636, 133, "+12 V", 11.5, 600, anchor="middle"),
    text(596, 203, "0 V", 11.5, 600, anchor="middle"),
    text(605, 503, "0 V", 11.5, 600, anchor="middle"),
    text(680, 563, "+5 V", 11.5, 600, anchor="middle"),
]

# --- Title and legend ------------------------------------------------------
header = [
    text(30, 34, "Wiring diagram: 8-drive build", 20, 700),
    text(30, 56, "All wire 2.5 mm² H07V-K except the inlet leads (1.5 mm²),", 12.5, fill=MUTED),
    text(30, 74, "the Molex pigtails (18 AWG) and the fan leads.", 12.5, fill=MUTED),
    text(30, 760, "Everything left of the Molex pigtails sits inside the earthed enclosure.", 12.5, 600, fill=INK),
    text(30, 92, "A hop means two wires cross without connecting.", 12.5, fill=MUTED),
]
key = legend(30, 790, [("L", "Live (L): brown"), ("N", "Neutral (N): blue"),
                       ("PE", "Earth (PE): green-yellow"), ("data", "SATA data cable"),
                       ("12V", "+12 V: yellow"), ("5V", "+5 V: red"),
                       ("GND", "0 V / ground: black")], cols=4, col_w=190)

body = "\n".join(header + parts + [w.render()] + labels + [key])
svg = document(1190, 850, body, "Wiring diagram: 8-drive build",
               "Colour-coded wiring from the Schurter mains inlet through WAGO splits to the "
               "RSP-200-12 and LRS-150F-5, then through the Blue Sea 5026 fuse block (7.5 A) and "
               "inline 5 A fuses to Molex pigtails A1 and A2 on the Jonsbo N3 backplane. A 1 A fuse feeds the "
               "drive fans. The negative bus is bonded to PE and to the host server's chassis.")

out = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "images", "wiring-diagram.svg")
with open(out, "w") as f:
    f.write(svg)
print("wrote", os.path.normpath(out))
