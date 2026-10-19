# DIY High-Density JBOD Power System

> [!CAUTION]
> ## ⚠️ UNTESTED EXPERIMENTAL DESIGN & STRICT LIMITATION OF LIABILITY
>
> **1. STATUS: THEORETICAL / UNTESTED PROOF OF CONCEPT (POC)**  
> The schematics, wiring instructions, Bill of Materials, calculations, and architectural designs in this repository represent a **theoretical and currently UNTESTED proof of concept**. The author has **NOT yet built, powered on, physically stress-tested, or lab-verified this build**. Sizing is derived strictly from calculations and manufacturer datasheets that may contain omissions or unmodeled real-world failure dynamics.
>
> **2. LETHAL MAINS VOLTAGE (230 VAC) & FIRE HAZARDS**  
> This project involves working directly with **mains electricity (100–240 VAC / 230 VAC)** and high-current direct-current (DC) power supplies. Mains voltage is **LETHAL** and presents severe risks of **fatal electrocution, arc flash, explosive component failure, and property-destroying fires**.
>
> **3. NO WARRANTY & ABSOLUTE LIMITATION OF LIABILITY ("AS IS")**  
> THIS REPOSITORY AND ALL ASSOCIATED DOCUMENTATION ARE PROVIDED **"AS IS", WITHOUT WARRANTY OF ANY KIND**, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OPERATIONAL SAFETY, OR NON-INFRINGEMENT.  
> **IN NO EVENT SHALL THE AUTHORS, MAINTAINERS, OR CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES, LOSS OF DATA, DESTRUCTION OF HARDWARE, PROPERTY DAMAGE, FIRE DAMAGE, PERSONAL INJURY, ELECTROCUTION, OR DEATH**, WHETHER IN AN ACTION OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY, OR OTHERWISE, ARISING OUT OF OR IN CONNECTION WITH THE ACCESS, USE, REPLICATION, MODIFICATION, OR IMPLEMENTATION OF THIS MATERIAL.
>
> **4. USER ASSUMES 100% OF ALL RISKS**  
> If you choose to replicate, adapt, construct, or energize any circuit described herein, **YOU DO SO AT YOUR OWN RISK**. You are solely responsible for compliance with all applicable local, regional, and national electrical codes and standards (e.g., SEV / NIN, VDE, NEC, CE, UL). Never work on energized circuits, and always have mains-voltage installations inspected by a licensed, certified electrician before applying power.

---

A well-documented, reproducible hardware guide for powering large arrays of 3.5" SATA hard drives (JBOD) using industrial **Mean Well switch-mode power supplies** instead of consumer ATX power supplies.

Designed for high reliability, clean voltage regulation, individual branch fuse protection, and common-ground reference with host servers.

---

## 📖 Navigation & Documentation

This repository is organized into self-contained, human-readable modules:

* 🛒 **[Procurement & Sourcing Guide](docs/procurement_guide.md)**  
  Complete Bill of Materials (BOM), verified part numbers, pricing (CHF / EUR delivered to Bern, Switzerland), and consolidated distributor order lists (Mouser, Galaxus/Digitec, Distrelec, Conrad).
* ⚡ **[Electrical Calculations & Fusing](docs/electrical_calculations.md)**  
  Spin-up load calculations, continuous ampacity, fuse sizing (ATO/ATC blade fuses), wire cross-sections, and ground-loop prevention.
* 🛠️ **[Wiring & Assembly Guide](docs/wiring_and_assembly.md)**  
  Step-by-step bench assembly instructions, WAGO 221 AC mains split, voltage trimming (12.15 V / 5.15 V), and pre-flight commissioning checklist.
* 📊 **[Original Calculation Sheet & Schematic (PDF)](docs/power_calculation_sheet.pdf)**  
  The source engineering spreadsheet and wiring layout used for sizing.
* ⚖️ **[License & Legal Disclaimer](LICENSE)**  
  MIT License with strict limitation of liability and hardware safety terms.

---

## 🎯 Project Overview & Scope

### 1. Proof of Concept (Current Target)
* **Drive Count:** 8x 3.5" SATA HDDs (using sacrificial 80–500 GB test drives).
* **Backplane:** 1x Jonsbo N3 8-bay backplane (dual 4-pin Molex power inputs, 8x SATA data).
* **12 V Spindle Power:** **Mean Well LRS-200-12** (12 V / 17 A, 204 W).
* **5 V Logic Power:** **Mean Well LRS-150F-5** (5 V / 22 A, 110 W).
* **Branch Fusing:** Blue Sea Systems 5026 ST Blade Fuse Block (7.5 A fuses on 12 V, 5 A fuses on 5 V).
* **Pigtails:** Factory-crimped 18 AWG Molex Y-cables cut into pigtails (no specialized pin crimpers needed).
* **Host Grounding:** $6.0\text{ mm}^2$ dedicated bonding wire between central DC negative and host server chassis.

### 2. Scale-Up Target (Future Expansion)
* **Drive Count:** 40 to 60 drives split across two isolated power loops.
* **12 V Supplies:** 2x Mean Well PSP-600-12 (active current sharing & remote ON/OFF) or 2x LRS-600-12.
* **Busbars:** Blue Sea Systems 2301 solid copper busbars (150 A rated).
* **Inrush Mitigation:** Finder 80.11 ON-delay relay to stagger 12 V power activation 2 seconds after the 5 V rail.

---

## 🔌 System Architecture & Wiring Diagram

```mermaid
flowchart TD
    subgraph Mains ["Mains Side (230 VAC / 50 Hz)"]
        Wall["Swiss Typ 13 Wall Outlet"] --> Cable["Schurter V-Lock Swiss Cable (3G1.0)"]
        Cable --> C14["Schurter DD11 Switched/Fused C14 Inlet"]
        C14 --> W_L["WAGO 221 (Live - L)"]
        C14 --> W_N["WAGO 221 (Neutral - N)"]
        C14 --> W_PE["WAGO 221 (Earth - PE)"]
    end

    subgraph Supplies ["Industrial Power Supplies"]
        W_L -->|L| PSU12["Mean Well LRS-200-12<br>(12V / 17A, 204W)<br><i>Trimmed to 12.15V</i>"]
        W_N -->|N| PSU12
        W_PE -->|PE| PSU12

        W_L -->|L| PSU5["Mean Well LRS-150F-5<br>(5V / 22A, 110W)<br><i>Trimmed to 5.15V</i>"]
        W_N -->|N| PSU5
        W_PE -->|PE| PSU5
    end

    subgraph Distribution ["DC Distribution & Fusing"]
        PSU12 -->|+12V (2.5mm²)| FuseBlock["Blue Sea 5026 Fuse Block<br>Positive Stud (M5)"]
        PSU12 -->|V- (6mm²)| NegBus["Blue Sea 5026<br>Negative Ground Bus"]
        PSU5 -->|V- (6mm²)| NegBus

        PSU5 -->|+5V (2.5mm²)| W_5V["WAGO 221 (+5V Split)"]

        FuseBlock -->|Fuse 1 (7.5A)| M1_12["Molex A1 (Pin 1: +12V)"]
        FuseBlock -->|Fuse 2 (7.5A)| M2_12["Molex A2 (Pin 1: +12V)"]

        W_5V -->|Inline Fuse 5A| M1_5["Molex A1 (Pin 4: +5V)"]
        W_5V -->|Inline Fuse 5A| M2_5["Molex A2 (Pin 4: +5V)"]

        NegBus -->|GND (18 AWG)| M1_GND["Molex A1 (Pins 2 & 3: GND)"]
        NegBus -->|GND (18 AWG)| M2_GND["Molex A2 (Pins 2 & 3: GND)"]
    end

    subgraph Host ["Server / Ground Reference"]
        NegBus ===|"6.0 mm² Server-GND Wire"| HostChassis["Host Server Chassis / Motherboard Ground"]
    end

    subgraph Backplane ["Drives & Backplane"]
        M1_12 --> BP["Jonsbo N3 Backplane (8 Bays)"]
        M2_12 --> BP
        M1_5 --> BP
        M2_5 --> BP
        M1_GND --> BP
        M2_GND --> BP
        BP --> HDDs["8x 3.5\" SATA HDDs"]
    end
```

---

## ⚡ Key Engineering Takeaways

1. **Why Not Consumer ATX PSUs?**  
   ATX power supplies require dummy load resistors on the 3.3 V/5 V rails to prevent group-regulated 12 V collapse, have clumsy multi-rail cable harnesses, and shut down unpredictably under asynchronous drive spin-up transients. Industrial Mean Well supplies offer rock-solid individual voltage adjustment trimmers, predictable overcurrent protection, and continuous industrial ratings.
2. **Backplane Power Plane Behavior:**  
   On backplanes like the Jonsbo N3, both Molex headers share continuous internal 12 V and 5 V PCB planes. Feeding both headers from the **same** power supply pair is safe and distributes current across multiple pins. *Never connect two different power supplies to the two Molex ports on a single backplane without ORing isolation.*
3. **Common Ground is Mandatory:**  
   SATA data links are single-ended signals referenced to ground. If the JBOD DC negative and host server ground differ in potential, data corruption or blown PHY chips will occur. The dedicated $6.0\text{ mm}^2$ bonding wire ties both grounds together securely.
4. **Trimming for IR Drop:**  
   Tuning the 5 V rail to **5.15 V** and the 12 V rail to **12.15 V** at the power supply terminals guarantees that hard drives receive exactly 5.00 V and 12.00 V under full load at the end of the wire harness.
