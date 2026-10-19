"""Tiny helpers shared by the diagram generators (standard library only)."""

FONT = "system-ui,-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"

# Surface and ink for the always-light diagram card. Wire colours need a known
# light background to read correctly, so these diagrams do not switch to dark.
CARD = "#fbfbf9"
CARD_EDGE = "#d4d4cf"
PART = "#efefea"
PART_EDGE = "#7d7d78"
INK = "#1b1b1a"
MUTED = "#5c5c58"

# Wire colours: (core, outline). Outlines keep yellow and green legible on white.
WIRES = {
    "L": ("#8b4513", "#4f260a"),
    "N": ("#1f6fd1", "#0d3a73"),
    "PE": ("#2e9e3e", "#17561f"),
    "12V": ("#f2c200", "#7a6200"),
    "5V": ("#d62828", "#6e0f0f"),
    "GND": ("#2b2b2b", "#000000"),
}
PE_STRIPE = "#f5d400"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, size=13, weight=400, fill=INK, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def rect(x, y, w, h, fill=PART, stroke=PART_EDGE, rx=6, sw=1.5, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def circle(x, y, r, fill="#c9c9c3", stroke=PART_EDGE, sw=1.5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def document(w, h, body, title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title>
<desc id="d">{esc(desc)}</desc>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{CARD}" stroke="{CARD_EDGE}"/>
{body}
</svg>
'''


class Wiring:
    """Orthogonal wires that hop over each other where they cross."""

    HOP = 6

    def __init__(self):
        self.wires = []  # (kind, points)

    def add(self, kind, *points):
        self.wires.append((kind, points))

    def _verticals(self, skip):
        for i, (_, pts) in enumerate(self.wires):
            if i == skip:
                continue
            for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
                if x1 == x2:
                    yield x1, min(y1, y2), max(y1, y2)

    def _path(self, i, pts):
        d = [f"M{pts[0][0]},{pts[0][1]}"]
        for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
            if y1 == y2:
                lo, hi = min(x1, x2), max(x1, x2)
                xs = sorted({vx for vx, a, b in self._verticals(i)
                             if lo + self.HOP < vx < hi - self.HOP and a < y1 < b},
                            reverse=x2 < x1)
                sign = 1 if x2 > x1 else -1
                for vx in xs:
                    d.append(f"L{vx - sign * self.HOP},{y1}")
                    sweep = 1 if sign > 0 else 0
                    d.append(f"A{self.HOP},{self.HOP} 0 0 {sweep} {vx + sign * self.HOP},{y1}")
            d.append(f"L{x2},{y2}")
        return " ".join(d)

    def render(self):
        out = []
        for i, (kind, pts) in enumerate(self.wires):
            core, edge = WIRES[kind]
            d = self._path(i, pts)
            common = 'fill="none" stroke-linejoin="round" stroke-linecap="round"'
            out.append(f'<path d="{d}" {common} stroke="{edge}" stroke-width="6"/>')
            out.append(f'<path d="{d}" {common} stroke="{core}" stroke-width="3.6"/>')
            if kind == "PE":
                out.append(f'<path d="{d}" fill="none" stroke-linejoin="round" stroke="{PE_STRIPE}" '
                           f'stroke-width="3.6" stroke-dasharray="7 7"/>')
        return "\n".join(out)


def legend(x, y, items, cols=4, col_w=170):
    """items: list of (kind or 'data', label)."""
    out = []
    for n, (kind, label) in enumerate(items):
        cx = x + (n % cols) * col_w
        cy = y + (n // cols) * 24
        if kind == "data":
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 28}" y2="{cy}" stroke="{MUTED}" '
                       f'stroke-width="2" stroke-dasharray="5 4"/>')
        else:
            core, edge = WIRES[kind]
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 28}" y2="{cy}" stroke="{edge}" stroke-width="6" stroke-linecap="round"/>')
            out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 28}" y2="{cy}" stroke="{core}" stroke-width="3.6" stroke-linecap="round"/>')
            if kind == "PE":
                out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 28}" y2="{cy}" stroke="{PE_STRIPE}" stroke-width="3.6" stroke-dasharray="7 7"/>')
        out.append(text(cx + 38, cy + 4.5, label, 12.5))
    return "\n".join(out)
