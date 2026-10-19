#!/usr/bin/env python3
"""Consistency checks for the docs. Run: python3 tools/check_repo.py

- every relative Markdown link and #anchor resolves
- the key figures quoted in the docs match tools/jbod_power.py
- the SVG diagrams are up to date with their generator scripts
Standard library only. Exits non-zero on any failure.
"""

import glob
import os
import re
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from jbod_power import DRIVE, PSUS, max_drives, peak_12v, smallest_fuse, voltage_drop, AWG18_MM2, FUSE_DROP  # noqa: E402

errors = []


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def slug(heading):
    h = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return h.replace(" ", "-")


def check_links():
    files = [os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)]
    anchors = {f: {slug(h) for h in re.findall(r"^#+\s+(.*)$", read(f), re.M)} for f in files}
    for f in files:
        for link in re.findall(r"\]\(([^)\s]+)\)", read(f)):
            if re.match(r"[a-z]+:", link):
                continue
            path, _, frag = link.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
            if not os.path.exists(os.path.join(ROOT, target)):
                errors.append(f"{f}: broken link {link}")
            elif frag and target.endswith(".md") and frag not in anchors.get(target, set()):
                errors.append(f"{f}: missing anchor {link}")


def expect(path, text):
    if text not in read(path):
        errors.append(f"{path}: expected to find {text!r}")


def check_figures():
    rsp200, rsp500, lrs = (PSUS[k]["amps"] for k in ("RSP-200-12", "RSP-500-12", "LRS-150F-5"))
    peak = 8 * DRIVE["spinup_12v"]
    idle = 8 * DRIVE["idle_12v"]
    five = 8 * DRIVE["logic_5v"]
    calc = "docs/03-electrical-calculations.md"
    expect(calc, f"**{peak:.2f} A**")
    expect(calc, f"**{100 * peak / rsp200:.1f} %**")
    expect(calc, f"**{idle:.1f} A**")
    expect(calc, f"**{five:.2f} A**")
    expect(calc, f"**{100 * five / lrs:.1f} %**")
    expect(calc, f"**{peak / 2:.2f} A**")
    expect(calc, f"**{five / 2:.2f} A**")
    expect(calc, f"**{smallest_fuse(peak / 2):g} A** ATO/ATC")
    expect(calc, f"at most **{max_drives(rsp200, 0.75, DRIVE['spinup_12v'])} drives**")
    expect(calc, f"handles **{max_drives(lrs, 0.75, DRIVE['logic_5v'])} drives**")
    expect("README.md", f"{100 * peak / rsp200:.0f} % load at spin-up")
    expect("README.md", f"{max_drives(rsp500, 0.75, DRIVE['spinup_12v'])} drives per RSP-500-12")

    scale = "docs/06-scaling-up.md"
    expect(scale, f"| RSP-200-12 (16.7 A) | **{max_drives(rsp200, 0.75, DRIVE['spinup_12v'])}** | "
                  f"~{max_drives(rsp200, 0.75, DRIVE['spinup_12v'], DRIVE['idle_12v'], 8)} |")
    expect(scale, f"| RSP-500-12 (41.7 A) | **{max_drives(rsp500, 0.75, DRIVE['spinup_12v'])}** | "
                  f"~{max_drives(rsp500, 0.75, DRIVE['spinup_12v'], DRIVE['idle_12v'], 8)} |")
    stag = peak_12v(30, DRIVE["spinup_12v"], DRIVE["idle_12v"], 8)
    expect(scale, f"≈ {stag:.0f} A, which is {100 * stag / rsp500:.0f} %")
    p24 = 24 * DRIVE["spinup_12v"]
    expect(scale, f"{p24:.1f} A peak ({100 * p24 / rsp500:.0f} %)")

    # Voltage budget: wire and fuse drops from trimmer to drive.
    gnd = (peak + five) / 4
    drop12 = (2 * voltage_drop(peak, 0.5, 2.5) + FUSE_DROP + voltage_drop(peak / 2, 0.2, AWG18_MM2)
              + voltage_drop(gnd, 0.2, AWG18_MM2))
    drop5 = (2 * voltage_drop(five, 0.5, 2.5) + FUSE_DROP + voltage_drop(five / 2, 0.3, AWG18_MM2)
             + voltage_drop(gnd, 0.2, AWG18_MM2))
    expect(calc, f"12.15 − {drop12:.2f} = {12.15 - drop12:.2f} V")
    expect(calc, f"5.15 − {drop5:.2f} = {5.15 - drop5:.2f} V")


def check_diagrams():
    before = {p: read(p) for p in (os.path.relpath(x, ROOT) for x in glob.glob(os.path.join(ROOT, "docs/images/*.svg")))}
    subprocess.run([sys.executable, os.path.join(ROOT, "tools/diagrams/build_all.py")],
                   check=True, stdout=subprocess.DEVNULL)
    for path, old in before.items():
        if read(path) != old:
            errors.append(f"{path}: out of date. Run python3 tools/diagrams/build_all.py and commit the result")


check_links()
check_figures()
check_diagrams()
for e in errors:
    print("FAIL", e)
print(f"{len(errors)} problem(s) found" if errors else "All checks passed")
sys.exit(1 if errors else 0)
