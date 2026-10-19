#!/usr/bin/env python3
"""Power budget calculator for the DIY JBOD power system.

Recomputes the load, PSU utilisation and per-header fuse currents for any
drive count, so the numbers in docs/ can be checked or redone for your own
drives. Standard library only.

Examples:
    python3 tools/jbod_power.py                    # 8-drive proof of concept
    python3 tools/jbod_power.py --drives 10
    python3 tools/jbod_power.py --drives 24 --psu12 RSP-500-12
    python3 tools/jbod_power.py --spinup-12v 2.0   # your drive's datasheet value
"""

import argparse
import math

# Rated continuous output of the supported supplies (datasheet values).
PSUS = {
    "RSP-200-12": {"volts": 12.0, "amps": 16.7},
    "RSP-500-12": {"volts": 12.0, "amps": 41.7},
    "LRS-150F-5": {"volts": 5.0, "amps": 22.0},
}

# Standard ATO/ATC blade fuse ratings in amps.
BLADE_FUSES = [1, 2, 3, 4, 5, 7.5, 10, 15, 20, 25, 30]

# A branch fuse should be at least this multiple of the branch's peak current.
FUSE_MARGIN = 1.25


def smallest_fuse(amps):
    for rating in BLADE_FUSES:
        if rating >= amps * FUSE_MARGIN:
            return rating
    return None


def max_drives(psu, amps_per_drive, derate):
    return math.floor(psu["amps"] * derate / amps_per_drive)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--drives", type=int, default=8, help="number of 3.5in drives (default 8)")
    p.add_argument("--spinup-12v", type=float, default=1.27, help="12 V spin-up current per drive, A (default 1.27)")
    p.add_argument("--idle-12v", type=float, default=0.40, help="12 V idle current per drive, A (default 0.40)")
    p.add_argument("--logic-5v", type=float, default=0.47, help="5 V current per drive, A (default 0.47)")
    p.add_argument("--bays", type=int, default=8, help="drive bays per backplane (default 8, Jonsbo N3)")
    p.add_argument("--headers", type=int, default=2, help="Molex power inputs per backplane (default 2)")
    p.add_argument("--psu12", choices=[k for k in PSUS if k.endswith("-12")], default="RSP-200-12")
    p.add_argument("--psu5", choices=["LRS-150F-5"], default="LRS-150F-5")
    p.add_argument("--derate", type=float, default=0.75, help="target max PSU load fraction (default 0.75)")
    a = p.parse_args()

    psu12, psu5 = PSUS[a.psu12], PSUS[a.psu5]
    n = a.drives

    peak12 = n * a.spinup_12v
    idle12 = n * a.idle_12v
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
    print(f"{n} drives on {backplanes} backplane(s), derating target {a.derate:.0%}\n")
    print(f"{'':26}{'Current':>10}{'Power':>10}{'PSU load':>10}  Status")
    rows = [
        (f"12 V spin-up ({a.psu12})", peak12, 12.0, psu12),
        (f"12 V idle", idle12, 12.0, psu12),
        (f"5 V ({a.psu5})", peak5, 5.0, psu5),
    ]
    for label, amps, volts, psu in rows:
        print(f"{label:26}{amps:>9.2f}A{amps * volts:>9.1f}W{load(amps, psu):>9.1f}%  {flag(amps, psu)}")
    print(f"{'Peak total':26}{'':>10}{peak12 * 12 + peak5 * 5:>9.1f}W")

    per_bp = min(n, a.bays)
    h12, h5 = per_bp * a.spinup_12v / a.headers, per_bp * a.logic_5v / a.headers
    print(f"\nPer Molex header ({per_bp} drives per backplane, load shared by {a.headers} headers):")
    print(f"  +12 V: {h12:.2f} A peak  -> smallest blade fuse {smallest_fuse(h12)} A")
    print(f"  +5 V:  {h5:.2f} A peak  -> smallest blade fuse {smallest_fuse(h5)} A")
    print(f"  (fuse >= {FUSE_MARGIN}x peak; must also stay below the ampacity of the branch wire)")

    print(f"\nMax drives at {a.derate:.0%} load, all spinning up at once:")
    print(f"  {a.psu12}: {max_drives(psu12, a.spinup_12v, a.derate)}   {a.psu5}: {max_drives(psu5, a.logic_5v, a.derate)}")


if __name__ == "__main__":
    main()
