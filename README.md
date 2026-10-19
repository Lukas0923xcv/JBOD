# DIY JBOD Power System

Power a shelf of 3.5" SATA hard drives (a JBOD) from two industrial **Mean Well** power supplies instead of a consumer ATX PSU, with a fuse on every branch and a ground shared with the host server.

> [!CAUTION]
> **Untested design. It has not been built or powered on yet.** It also involves **230 VAC mains wiring, which can kill you** and can start fires. Read [SAFETY.md](SAFETY.md) before you build anything. If you are not qualified to work on mains wiring, have an electrician do or inspect that part.

[![Colour-coded wiring diagram of the 8-drive build](docs/images/wiring-diagram.svg)](docs/images/wiring-diagram.svg)

| | |
|---|---|
| **Status** | Design complete, not yet built. See [Project status](#project-status). |
| **First build** | 8 drives on one Jonsbo N3 backplane: old test drives first, then WD Ultrastar DC HC530 14 TB |
| **12 V supply** | Mean Well RSP-200-12 (16.7 A): 61 % load at spin-up, 64 % with the fans |
| **5 V supply** | Mean Well LRS-150F-5 (22 A): 17 % load |
| **Branch fuses** | 7.5 A on each +12 V lead, 5 A on each +5 V lead, 1 A for the drive fans |
| **Enclosure** | Everything carrying mains sits in a closed, earthed metal enclosure. The JBOD's 0 V is bonded to earth and to the server chassis |
| **Parts cost** | ~CHF 400 including enclosure and fans (~CHF 450 with a clamp meter), bought in Switzerland |
| **Scales to** | 24 drives per RSP-500-12 with all drives spinning up at once, more with staggered spin-up |

## Where to start

Read the documents in this order:

1. **[Design overview](docs/01-design-overview.md)**: how the system fits together and why it uses Mean Well supplies. Includes the wiring diagram.
2. **[Bill of materials](docs/02-bill-of-materials.md)**: what to buy and from which shop, with prices.
3. **[Electrical calculations](docs/03-electrical-calculations.md)**: load, fuse and wire sizing. Read this if you want to change anything.
4. **[Assembly guide](docs/04-assembly-guide.md)**: step-by-step wiring.
5. **[Commissioning checklist](docs/05-commissioning-checklist.md)**: the checks to do before and at first power-on. Print it.
6. **[Test log](docs/test-log.md)**: write down what you measure. This is how the design gets verified.
7. **[Scaling up](docs/06-scaling-up.md)**: going past 8 drives with the RSP-500-12.

[`docs/reference/original-calculation-sheet.md`](docs/reference/original-calculation-sheet.md) is the original worksheet the design came from. It is kept for history and has known errors. The other documents take precedence.

## Recalculate for your own drives

The figures in these documents are for the **WD Ultrastar DC HC530 14 TB**: **1.27 A at 12 V spin-up, 0.40 A at 12 V idle and 0.47 A at 5 V per drive**. For any other drive, check its datasheet. The label only shows running current, not the spin-up peak. If its numbers differ, or you want a different drive count, run the calculator (Python 3, no dependencies):

```sh
python3 tools/jbod_power.py                               # the 8-drive build
python3 tools/jbod_power.py --drives 10 --spinup-12v 1.8  # your own numbers
python3 tools/jbod_power.py --drives 24 --psu12 RSP-500-12
python3 tools/jbod_power.py --drives 30 --psu12 RSP-500-12 --stagger 8   # staggered spin-up
python3 tools/jbod_power.py --extra-12v 0.6                               # include the fans
python3 tools/jbod_power.py --help
```

It prints the load on each supply, flags anything above the 75 % derating target, and suggests a branch fuse rating for each Molex header. It warns when no fuse can protect the 18 AWG pigtails.

## Project status

- [x] Load, fuse and wire calculations
- [x] Bill of materials with Swiss suppliers
- [x] Assembly and commissioning procedure
- [ ] Parts ordered
- [ ] Built into the enclosure
- [ ] Safety test of the AC side by an electrician
- [ ] Bench build without drives (voltages trimmed, backplane checked)
- [ ] 8-drive spin-up test with measurements recorded in the [test log](docs/test-log.md)
- [ ] Long-run thermal test (24 h under load)

## Still to verify

These facts come from secondary sources or memory, not from the manufacturer's datasheet, or depend on your own parts. Check them before you rely on them:

- **Mean Well:** the RSP-200-12 and RSP-500-12 voltage-adjust range (sources say 10–13.2 V; the 12.15 V target is inside it either way), the terminal screw size of all three supplies, and the RSP-500-12's overload behaviour.
- **Schurter DD11.0121.1111:** rated current (distributors list 7 A or 10 A; both are above the 6.3 A fuse) and the panel cutout. The 6051.2015 cord length (2.5 m or 5 m).
- **InLine 33445 Y-cable:** that it really is 18 AWG. Check the print on the insulation.
- **Blue Sea 5026:** the footprint (≈ 100 × 150 mm is an estimate) and that the negative bus has at least 7 free branch screws (4 pigtail grounds, server bond, 0 V–PE bond, fans).
- **Jonsbo N3 backplane:** whether A1 and A2 share copper planes and whether it makes 3.3 V. Commissioning steps B and D2 measure both.
- **Electrician's test limits** in commissioning step B2 are typical values; the electrician applies the standard's actual limits.
- **Voltage tolerance:** the docs use ±5 % on both rails, the strictest common figure. Your drive's datasheet may allow more on 12 V.

## Repository layout

```
README.md                 This file
SAFETY.md                 Hazards, precautions and the liability disclaimer
CHANGELOG.md              What changed in the docs, including corrections
LICENSE                   MIT, plus a hardware safety disclaimer
docs/                     The guides, numbered in reading order
docs/reference/           The original design worksheet (historical)
docs/images/              Diagrams (SVG), generated by tools/diagrams/
tools/jbod_power.py       Power budget calculator
tools/check_repo.py       Checks links, figures and diagrams (run before committing)
tools/diagrams/           Python scripts that draw the SVG diagrams
```

To change a diagram, edit its script in `tools/diagrams/` and run `python3 tools/diagrams/build_all.py`. Don't edit the SVGs by hand.

## License

MIT, with an additional hardware safety disclaimer. See [LICENSE](LICENSE).
