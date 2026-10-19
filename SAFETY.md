# Safety

> [!CAUTION]
> This is an **untested proof of concept**. The author has not built it, powered it on or tested it under load. The sizing comes from calculations and manufacturer datasheets, which can be wrong or incomplete.

## The hazards

- **Mains voltage (230 VAC) can kill.** The inlet, the AC lever-nut splits and the AC terminals of both power supplies carry mains voltage whenever the cord is plugged in. That includes the times the rocker switch is off: the switch breaks L and N, but the wiring up to the switch stays live.
- **Stored charge.** Switch-mode supplies hold charge in their input capacitors for a while after you unplug them. Wait at least 1 minute after unplugging, and check that the DC-OK LEDs are off, before you touch any terminal.
- **Fire.** A short on the DC side is limited mainly by the supplies themselves. The RSP-200-12 delivers about 17.5–22.5 A (105–135 % of its rating) and then switches off and retries ("hiccup" mode); the LRS-150F-5 about 24–31 A. A poor crimp or an undersized wire carrying that for minutes still gets hot enough to start a fire. Never bypass a fuse or fit a larger one than the docs specify.
- **Exposed terminals.** The inlet tabs, the AC lever nuts and the supplies' screw terminals all carry 230 VAC. That is why the whole build goes in an earthed enclosure. When the lid is open for trimming, the AC terminals must be covered.

## Rules for building it

1. **Unplug the mains cord before you touch anything.** Do not rely on the rocker switch.
2. **Enclose it.** Everything from the mains inlet to the fuse block goes inside a closed enclosure, with the inlet fitted in its wall. Never run it as an open board.
3. **Earth everything metal.** Each supply's PE (earth) terminal, the metal enclosure and the JBOD's 0 V (negative bus) connect to the inlet's earth pin. Do the continuity test in the [commissioning checklist](docs/05-commissioning-checklist.md) before the first power-on.
4. **Crimp properly.** Use ferrules on stranded wire in lever nuts and screw terminals, and ring or fork terminals on studs. A loose strand on the AC side is a shock hazard, and a poor DC crimp heats up.
5. **Have the AC side tested before the first plug-in.** An electrician checks the earth resistance, insulation resistance and leakage current (in Switzerland a safety test to SNR 462638, elsewhere e.g. EN 50678 / VDE 0701-0702). A hobby multimeter can't do this test properly.
6. **First power-on from an RCD-protected socket** (FI-Schutzschalter, 30 mA).
7. **Trim with an insulated tool.** The V.ADJ trimmers sit on the same terminal strip as the AC terminals. Use a plastic trimming tool, keep the AC terminals covered, and keep your other hand away.
8. **No drives at first power-on.** Measure and trim the voltages with nothing connected, then add drives.
9. **Use test drives for the first spin-up**, not drives with data you care about.
10. **Follow the rules that apply where you live.** In Switzerland the installation rules (NIV / NIN) cover fixed building wiring, and a mains device you build yourself counts as a product (NEV). Elsewhere it is VDE, NEC, etc. If you are not qualified to do mains wiring, have an electrician do the AC side or inspect it before you plug it in.

## Disclaimer of liability

THIS REPOSITORY AND ALL ASSOCIATED DOCUMENTATION ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OPERATIONAL SAFETY, OR NON-INFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS, MAINTAINERS, OR CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES, LOSS OF DATA, DESTRUCTION OF HARDWARE, PROPERTY DAMAGE, FIRE DAMAGE, PERSONAL INJURY, ELECTROCUTION, OR DEATH, WHETHER IN AN ACTION OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, ARISING OUT OF OR IN CONNECTION WITH THE ACCESS, USE, REPLICATION, MODIFICATION, OR IMPLEMENTATION OF THIS MATERIAL.

If you build, adapt or energize any circuit described here, **you do so entirely at your own risk** and you are solely responsible for complying with applicable electrical codes and standards.
