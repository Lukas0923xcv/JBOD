#!/usr/bin/env python3
"""Power budget calculator for the DIY JBOD power system.

Recomputes the load, PSU utilisation and per-header fuse currents for any
drive count, so the numbers in docs/ can be checked or redone for your own
drives. Standard library only. tools/diagrams/charts.py imports the
constants below, so the charts always match this calculator.

Examples:
    python3 tools/jbod_power.py                    # 8-drive proof of concept
    python3 tools/jbod_power.py --drives 10
    python3 tools/jbod_power.py --drives 24 --psu12 RSP-500-12
    python3 tools/jbod_power.py --spinup-12v 2.0   # your drive's datasheet value
    python3 tools/jbod_power.py --drives 30 --psu12 RSP-500-12 --stagger 8
"""

import argparse
import math

# Rated continuous output of the supported supplies (datasheet values).
PSUS = {
    "RSP-200-12": {"volts": 12.0, "amps": 16.7},
    "RSP-500-12": {"volts": 12.0, "amps": 41.7},
    "LRS-150F-5": {"volts": 5.0, "amps": 22.0},
}

# WD Ultrastar DC HC530 14 TB SATA, "Start up Peak DC" and idle figures.
DRIVE = {"spinup_12v": 1.27, "idle_12v": 0.40, "logic_5v": 0.47}

# Standard ATO/ATC blade fuse ratings in amps.
BLADE_FUSES = [1, 2, 3, 4, 5, 7.5, 10, 15, 20, 25, 30]

# A branch fuse should be at least this multiple of the branch's peak current.
FUSE_MARGIN = 1.25

# Largest fuse that still protects an 18 AWG (0.82 mm²) Molex pigtail.
MAX_FUSE_18AWG = 10

# The design fits 5 A on +5 V, above the 3 A minimum, for hot-plug inrush.
FUSE_5V_CHOSEN = 5

# Wire resistance and the assumed drop across one blade fuse and holder.
RHO_CU = 0.0175   # ohm mm²/m
AWG18_MM2 = 0.82
FUSE_DROP = 0.05  # V


def smallest_fuse(amps):
    for rating in BLADE_FUSES:
        if rating >= amps * FUSE_MARGIN:
            return rating
    return None


def voltage_drop(amps, length_m, area_mm2):
    return amps * RHO_CU * length_m / area_mm2


def peak_12v(n, spinup, idle, stagger):
    """12 V peak for n drives when at most `stagger` spin up together."""
    group = n if stagger is None else min(stagger, n)
    return spinup * group + idle * (n - group)


def max_drives(psu_amps, derate, spinup, idle=0.0, stagger=None, extra=0.0):
    budget = psu_amps * derate - extra
    if budget < 0:
        return 0
    if stagger is None:
        return math.floor(budget / spinup + 1e-9)
    if spinup * stagger > budget:
        return math.floor(budget / spinup + 1e-9)
    if idle == 0:
        return None  # unlimited by the 12 V rail
    return stagger + math.floor((budget - spinup * stagger) / idle + 1e-9)


def fuse_text(amps):
    fuse = smallest_fuse(amps)
    if fuse is None or fuse > MAX_FUSE_18AWG:
        return (f"NO SAFE FUSE: needs >= {amps * FUSE_MARGIN:.1f} A, but 18 AWG pigtails "
                f"allow at most {MAX_FUSE_18AWG} A. Use fewer drives per backplane, "
                f"staggered spin-up or thicker wire")
    return f"smallest blade fuse {fuse:g} A"


def positive_float(s):
    v = float(s)
    if v <= 0:
        raise argparse.ArgumentTypeError("must be greater than 0")
    return v


def non_negative_float(s):
    v = float(s)
    if v < 0:
        raise argparse.ArgumentTypeError("must be 0 or more")
    return v


def positive_int(s):
    v = int(s)
    if v < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return v


def fraction(s):
    v = float(s)
    if not 0 < v <= 1:
        raise argparse.ArgumentTypeError("must be between 0 and 1, e.g. 0.75")
    return v


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--drives", type=positive_int, default=8, help="number of 3.5in drives (default 8)")
    p.add_argument("--spinup-12v", type=positive_float, default=DRIVE["spinup_12v"],
                   help=f"12 V spin-up current per drive, A (default {DRIVE['spinup_12v']})")
    p.add_argument("--idle-12v", type=non_negative_float, default=DRIVE["idle_12v"],
                   help=f"12 V idle current per drive, A (default {DRIVE['idle_12v']})")
    p.add_argument("--logic-5v", type=positive_float, default=DRIVE["logic_5v"],
                   help=f"5 V current per drive, A (default {DRIVE['logic_5v']})")
    p.add_argument("--extra-12v", type=non_negative_float, default=0.0,
                   help="other 12 V load on its own fuse, e.g. fans, A (default 0)")
    p.add_argument("--stagger", type=positive_int, default=None,
                   help="drives that spin up together with staggered spin-up (default: all at once)")
    p.add_argument("--bays", type=positive_int, default=8, help="drive bays per backplane (default 8, Jonsbo N3)")
    p.add_argument("--headers", type=positive_int, default=2, help="Molex power inputs per backplane (default 2)")
    p.add_argument("--psu12", choices=[k for k in PSUS if k.endswith("-12")], default="RSP-200-12")
    p.add_argument("--psu5", choices=["LRS-150F-5"], default="LRS-150F-5")
    p.add_argument("--derate", type=fraction, default=0.75, help="target max PSU load fraction (default 0.75)")
    a = p.parse_args()

    psu12, psu5 = PSUS[a.psu12], PSUS[a.psu5]
    n = a.drives

    peak12 = peak_12v(n, a.spinup_12v, a.idle_12v, a.stagger) + a.extra_12v
    idle12 = n * a.idle_12v + a.extra_12v
    peak5 = n * a.logic_5v

    def load(amps, psu):
        return 100 * amps / psu["amps"]

    def flag(amps, psu):
        pct = load(amps, psu)
        if pct > 100:
            return "OVERLOAD"
        if pct > a.derate * 100:
            return f"above {a.derate:.0%} target"
        return "ok"

    backplanes = math.ceil(n / a.bays)
    spin = "all at once" if a.stagger is None or a.stagger >= n else f"in groups of {a.stagger}"
    print(f"{n} drives on {backplanes} backplane(s), spinning up {spin}, derating target {a.derate:.0%}")
    if a.extra_12v:
        print(f"Includes {a.extra_12v:.2f} A of other 12 V load (fans etc.)")
    print(f"\n{'':26}{'Current':>10}{'Power':>10}{'PSU load':>10}  Status")
    rows = [
        (f"12 V spin-up ({a.psu12})", peak12, 12.0, psu12),
        ("12 V idle", idle12, 12.0, psu12),
        (f"5 V ({a.psu5})", peak5, 5.0, psu5),
    ]
    for label, amps, volts, psu in rows:
        print(f"{label:26}{amps:>9.2f}A{amps * volts:>9.1f}W{load(amps, psu):>9.1f}%  {flag(amps, psu)}")
    print(f"{'Peak total':26}{'':>10}{peak12 * 12 + peak5 * 5:>9.1f}W")

    per_bp = min(n, a.bays)
    spinning = per_bp if a.stagger is None else min(a.stagger, per_bp)
    bp12 = spinning * a.spinup_12v + (per_bp - spinning) * a.idle_12v
    h12, h5 = bp12 / a.headers, per_bp * a.logic_5v / a.headers
    print(f"\nPer Molex header ({per_bp} drives per backplane, load shared by {a.headers} headers):")
    print(f"  +12 V: {h12:.2f} A peak  -> {fuse_text(h12)}")
    print(f"  +5 V:  {h5:.2f} A peak  -> {fuse_text(h5)}")
    print(f"  (fuse >= {FUSE_MARGIN}x peak and <= {MAX_FUSE_18AWG} A for 18 AWG pigtails. The docs fit "
          f"{FUSE_5V_CHOSEN} A on +5 V to allow for hot-plug inrush.)")
    if a.headers > 1:
        alone = bp12 / (a.headers - 1)
        fuse = smallest_fuse(h12)
        if fuse and fuse <= MAX_FUSE_18AWG and alone > fuse:
            print(f"  If one +12 V fuse blows and the headers share copper planes, the others carry "
                  f"{alone:.2f} A ({100 * alone / fuse:.0f} % of {fuse:g} A) at the next spin-up.")

    label = "all spinning up at once" if a.stagger is None else f"spinning up in groups of {a.stagger}"
    m12 = max_drives(psu12["amps"], a.derate, a.spinup_12v, a.idle_12v, a.stagger, a.extra_12v)
    m5 = max_drives(psu5["amps"], a.derate, a.logic_5v)
    print(f"\nMax drives at {a.derate:.0%} load, {label}:")
    print(f"  {a.psu12}: {'no 12 V limit' if m12 is None else m12}   {a.psu5}: {m5}")


if __name__ == "__main__":
    main()
