# Safety

> [!CAUTION]
> This is an **untested proof of concept**. The author has not built it, powered it on or tested it under load. The sizing comes from calculations and manufacturer datasheets, which can be wrong or incomplete.

## The hazards

- **Mains voltage (230 VAC) can kill.** The inlet, the AC lever-nut splits and the AC terminals of both power supplies carry mains voltage whenever the cord is plugged in. That includes the times the rocker switch is off: the switch breaks L and N, but the wiring up to the switch stays live.
- **Stored charge.** Switch-mode supplies hold charge in their input capacitors for a while after you unplug them. Wait at least 1 minute after unplugging, and check that the DC-OK LEDs are off, before you touch any terminal.
- **Fire.** A short on the DC side can deliver far more than 100 A. The branch fuses are there to stop that, so never bypass them or fit a larger fuse than the docs specify.
- **Exposed terminals.** Mean Well supplies have open screw terminals, so use the terminal covers and keep the build away from metal desks, tools and liquids.

## Rules for building it

1. **Unplug the mains cord before you touch anything.** Do not rely on the rocker switch.
2. **Earth everything metal.** Each supply's PE (earth) terminal and any metal enclosure or mounting plate must connect to the inlet's earth pin. Do the continuity test in the [commissioning checklist](docs/05-commissioning-checklist.md) before the first power-on.
3. **Crimp properly.** Use ferrules on stranded wire in lever nuts and screw terminals, and ring or fork terminals on studs. A loose strand on the AC side is a shock hazard, and a poor DC crimp heats up.
4. **No drives at first power-on.** Measure and trim the voltages with nothing connected, then add drives.
5. **Use test drives for the first spin-up**, not drives with data you care about.
6. **Follow your local electrical code** (in Switzerland NIN / SEV; elsewhere VDE, NEC, etc.). If you are not qualified to do mains wiring, have a licensed electrician do the AC side or inspect it before you plug it in.

## Disclaimer of liability

THIS REPOSITORY AND ALL ASSOCIATED DOCUMENTATION ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OPERATIONAL SAFETY, OR NON-INFRINGEMENT.

IN NO EVENT SHALL THE AUTHORS, MAINTAINERS, OR CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES, LOSS OF DATA, DESTRUCTION OF HARDWARE, PROPERTY DAMAGE, FIRE DAMAGE, PERSONAL INJURY, ELECTROCUTION, OR DEATH, WHETHER IN AN ACTION OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, ARISING OUT OF OR IN CONNECTION WITH THE ACCESS, USE, REPLICATION, MODIFICATION, OR IMPLEMENTATION OF THIS MATERIAL.

If you build, adapt or energize any circuit described here, **you do so entirely at your own risk** and you are solely responsible for complying with applicable electrical codes and standards.
