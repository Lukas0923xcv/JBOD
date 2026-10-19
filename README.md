# DIY JBOD Power System

Power a shelf of 3.5" SATA hard drives (a JBOD) from two industrial **Mean Well** power supplies instead of a consumer ATX PSU, with a fuse on every branch and a ground shared with the host server.

> [!CAUTION]
> **Untested design. It has not been built or powered on yet.** It also involves **230 VAC mains wiring, which can kill you** and can start fires. Read [SAFETY.md](SAFETY.md) before you build anything. If you are not qualified to work on mains wiring, have an electrician do or inspect that part.

| | |
|---|---|
| **Status** | Design complete, not yet built. See [Project status](#project-status). |
| **First build** | 8 drives on one Jonsbo N3 backplane |
| **12 V supply** | Mean Well RSP-200-12 (16.7 A): 61 % load at spin-up |
| **5 V supply** | Mean Well LRS-150F-5 (22 A): 17 % load |
| **Branch fuses** | 7.5 A on each +12 V lead, 5 A on each +5 V lead |
| **Parts cost** | ~CHF 250 (~CHF 300 with a clamp meter), bought in Switzerland |
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

The figures in these documents assume **1.27 A at 12 V spin-up, 0.40 A at 12 V idle and 0.47 A at 5 V per drive**. Check your drive's datasheet. If its numbers differ, or you want a different drive count, run the calculator (Python 3, no dependencies):

```sh
python3 tools/jbod_power.py                               # the 8-drive build
python3 tools/jbod_power.py --drives 10 --spinup-12v 1.8  # your own numbers
python3 tools/jbod_power.py --drives 24 --psu12 RSP-500-12
python3 tools/jbod_power.py --help
```

It prints the load on each supply, flags anything above the 75 % derating target, and suggests a branch fuse rating for each Molex header.

## Project status

- [x] Load, fuse and wire calculations
- [x] Bill of materials with Swiss suppliers
- [x] Assembly and commissioning procedure
- [ ] Parts ordered
- [ ] Bench build without drives (voltages trimmed)
- [ ] 8-drive spin-up test with measurements recorded in the [test log](docs/test-log.md)
- [ ] Long-run thermal test (24 h under load)

## Repository layout

```
README.md                 This file
SAFETY.md                 Hazards, precautions and the liability disclaimer
CHANGELOG.md              What changed in the docs, including corrections
LICENSE                   MIT, plus a hardware safety disclaimer
docs/                     The guides, numbered in reading order
docs/reference/           The original design worksheet (historical)
tools/jbod_power.py       Power budget calculator
```

## License

MIT, with an additional hardware safety disclaimer. See [LICENSE](LICENSE).
