"""Generates the two charts in docs/images/: spin-up current and voltage budget.

Unlike the wiring diagrams these follow the viewer's light/dark preference.
"""

import os
from svg import FONT, esc

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "images")

STYLE = """<style>
  .bg { fill: #fcfcfb; stroke: #dcdbd6; }
  .ink { fill: #0b0b0b; } .ink2 { fill: #52514e; } .ink3 { fill: #7a7973; }
  .grid { stroke: #e6e5e0; } .axis { stroke: #9a9993; }
  .ref { stroke: #52514e; stroke-dasharray: 5 4; }
  .s1 { stroke: #2a78d6; } .f1 { fill: #2a78d6; } .a1 { fill: #2a78d6; opacity: .12; }
  .f2 { fill: #eb6834; } .conn { stroke: #9a9993; stroke-dasharray: 2 3; }
  @media (prefers-color-scheme: dark) {
    .bg { fill: #1a1a19; stroke: #3a3a37; }
    .ink { fill: #f0efec; } .ink2 { fill: #c3c2b7; } .ink3 { fill: #9a998f; }
    .grid { stroke: #2c2c2a; } .axis { stroke: #6b6a64; }
    .ref { stroke: #c3c2b7; }
    .s1 { stroke: #3987e5; } .f1 { fill: #3987e5; } .a1 { fill: #3987e5; opacity: .18; }
    .f2 { fill: #d95926; } .conn { stroke: #6b6a64; }
  }
</style>"""


def t(x, y, s, size=12.5, cls="ink", weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def doc(w, h, body, title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title>
<desc id="d">{esc(desc)}</desc>
{STYLE}
<rect class="bg" x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12"/>
{body}
</svg>
'''


def spinup():
    W, H = 960, 430
    L, R, T, B = 70, 820, 92, 370  # plot box
    tmax, amax = 20, 18

    def X(s):
        return L + (R - L) * s / tmax

    def Y(a):
        return B - (B - T) * a / amax

    b = [t(30, 36, "12 V current during spin-up: 8 drives on the RSP-200-12", 18, weight=700),
         t(30, 58, "Illustrative shape built from the per-drive figures (1.27 A peak, 0.40 A idle). "
                   "Measure your own drives with a clamp meter.", 12.5, "ink2")]
    for a in range(0, amax + 1, 3):
        b.append(f'<line class="grid" x1="{L}" y1="{Y(a)}" x2="{R}" y2="{Y(a)}"/>')
        b.append(t(L - 10, Y(a) + 4, f"{a}", 11.5, "ink2", anchor="end"))
    for s in range(0, tmax + 1, 2):
        b.append(t(X(s), B + 20, f"{s}", 11.5, "ink2", anchor="middle"))
    b.append(f'<line class="axis" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
    b.append(t((L + R) / 2, B + 44, "seconds after power-on", 12, "ink2", anchor="middle"))
    b.append(t(L - 52, T - 14, "amps", 12, "ink2"))

    # Reference lines, labelled at the right edge
    for amps, label, sub in [(16.7, "16.7 A", "RSP-200-12 rating"), (12.5, "12.5 A", "75 % target")]:
        b.append(f'<line class="ref" x1="{L}" y1="{Y(amps)}" x2="{R}" y2="{Y(amps)}" stroke-width="1.5"/>')
        b.append(t(R + 10, Y(amps) + 0, label, 12, "ink", 700))
        b.append(t(R + 10, Y(amps) + 15, sub, 11, "ink2"))

    pts = [(0, 0), (0.3, 0), (0.6, 10.16), (4.0, 10.0), (5.5, 9.2), (7.0, 6.8), (8.5, 4.6),
           (9.8, 3.55), (11, 3.25), (20, 3.2)]
    line = " ".join(f"{X(s):.1f},{Y(a):.1f}" for s, a in pts)
    area = f"{X(0)},{Y(0)} {line} {X(tmax)},{Y(0)}"
    b.append(f'<polygon class="a1" points="{area}"/>')
    b.append(f'<polyline class="s1" points="{line}" fill="none" stroke-width="2.5" stroke-linejoin="round"/>')

    # Annotations
    b.append(f'<circle class="f1" cx="{X(0.6)}" cy="{Y(10.16)}" r="4.5"/>')
    b.append(t(X(1.0), Y(10.16) - 22, "≈ 10.2 A peak", 12.5, "ink", 700))
    b.append(t(X(1.0), Y(10.16) - 8, "61 % of rating, 2.3 A below the 75 % target", 11.5, "ink2"))
    b.append(t(X(13), Y(3.2) - 12, "≈ 3.2 A idle (19 %)", 12.5, "ink", 700))
    b.append(t(X(13), Y(3.2) + 22, "5 V rail: steady ≈ 3.8 A throughout (17 % of the LRS-150F-5)", 11.5, "ink2"))
    b.append(t(X(6.6), Y(7.6), "platters reach speed", 11.5, "ink2"))
    return doc(W, H, "\n".join(b), "12 V current during spin-up",
               "Line chart: 12 V current jumps to about 10.2 A at power-on, holds for about 5 seconds, "
               "and settles to about 3.2 A idle by 10 seconds. The RSP-200-12 rating is 16.7 A and the 75 "
               "percent target is 12.5 A.")


def budget():
    W, H = 1120, 440
    panels = [
        ("+12 V rail at spin-up peak", 12.15, 11.85, 12.20, 0.05, [
            ("PSU → fuse block", 0.036), ("7.5 A fuse", 0.05), ("pigtail +12 V", 0.022),
            ("pigtail GND", 0.015), ("return to PSU", 0.036)]),
        ("+5 V rail", 5.15, 4.95, 5.20, 0.05, [
            ("PSU → WAGO", 0.013), ("5 A fuse", 0.05), ("holder + pigtail", 0.012),
            ("pigtail GND", 0.015), ("return to PSU", 0.013)]),
    ]
    b = [t(30, 36, "Voltage budget: from the trimmer to the drive", 18, weight=700),
         t(30, 58, "Calculated drops at peak load. Each axis is zoomed in: the whole budget is about 0.1–0.16 V, "
                   "while SATA allows ±5 % (±0.6 V on 12 V, ±0.25 V on 5 V).", 12.5, "ink2")]
    # legend
    b.append(f'<rect class="f1" x="30" y="76" width="14" height="14" rx="3"/>')
    b.append(t(52, 88, "voltage", 12, "ink2"))
    b.append(f'<rect class="f2" x="122" y="76" width="14" height="14" rx="3"/>')
    b.append(t(144, 88, "loss along the way", 12, "ink2"))

    pw, gap = 480, 50
    for p, (title, start, lo, hi, step, drops) in enumerate(panels):
        L = 80 + p * (pw + gap)
        R = L + pw - 30
        T, B = 140, 360

        def Y(v):
            return B - (B - T) * (v - lo) / (hi - lo)

        b.append(t(L, T - 18, title, 14, weight=700))
        v = lo
        while v <= hi + 1e-9:
            b.append(f'<line class="grid" x1="{L}" y1="{Y(v):.1f}" x2="{R}" y2="{Y(v):.1f}"/>')
            b.append(t(L - 8, Y(v) + 4, f"{v:.2f}", 11, "ink2", anchor="end"))
            v += step
        n = len(drops) + 2
        slot = (R - L) / n
        bw = slot - 14
        x = L + 7

        def bar(x, top, bottom, cls, label, value):
            y1, y2 = Y(top), Y(bottom)
            out = [f'<rect class="{cls}" x="{x:.1f}" y="{y1:.1f}" width="{bw:.1f}" height="{max(y2 - y1, 2):.1f}" rx="3"/>']
            out.append(t(x + bw / 2, y1 - 6, value, 11.5, "ink", 700, anchor="middle"))
            out.append(t(x + bw / 2, B + 16, label, 10.5, "ink2", anchor="end",
                         extra=f'transform="rotate(-35 {x + bw / 2:.1f} {B + 16})"'))
            return out

        b += bar(x, start, lo, "f1", "set (no load)", f"{start:.2f}")
        level = start
        for label, d in drops:
            b.append(f'<line class="conn" x1="{x + bw:.1f}" y1="{Y(level):.1f}" x2="{x + slot:.1f}" y2="{Y(level):.1f}"/>')
            x += slot
            b += bar(x, level, level - d, "f2", label, f"−{d * 1000:.0f} mV")
            level -= d
        b.append(f'<line class="conn" x1="{x + bw:.1f}" y1="{Y(level):.1f}" x2="{x + slot:.1f}" y2="{Y(level):.1f}"/>')
        x += slot
        b += bar(x, level, lo, "f1", "at the drive", f"≈ {level:.2f}")
        b.append(f'<line class="axis" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
    return doc(W, H, "\n".join(b), "Voltage budget",
               "Waterfall charts. 12 V: set to 12.15 V, losing 36, 50, 22, 15 and 36 millivolts to arrive at "
               "about 11.99 V. 5 V: set to 5.15 V, losing 13, 50, 12, 15 and 13 millivolts to arrive at about 5.05 V.")


for name, svg in [("spinup-current.svg", spinup()), ("voltage-budget.svg", budget())]:
    path = os.path.join(OUT, name)
    open(path, "w").write(svg)
    print("wrote", os.path.normpath(path))
