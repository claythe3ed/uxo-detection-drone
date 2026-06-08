MASTER RESEARCH REPORT: UXO Detection Drone – Advanced Sensor Fusion R&D

Project: UXO Detection Drone (open-source)
Mission: Humanitarian demining – low-cost, sub-2 kg payload, sub-$2,000 BOM
Stage: Conceptual design and feasibility assessment for new sensor modalities
Author: Internal R&D Swarm (Orchestrator + 5 specialist agents)
Date: 2026-06-08

1. EXECUTIVE SUMMARY

The existing fluxgate-magnetometer + passive-thermal-camera drone already detects ferrous mines and shallow thermal anomalies. To reliably find non-metallic AP mines and deep-buried UXO, we evaluated seven candidate physics modalities under the strict constraints of a solo-maker, open-source, low-cost UAV. After balanced analysis by Researcher, Analyst, Skeptic, and Guardian agents, two sensors emerge as immediately integratable: Laser Speckle Vibrometry (acoustic-seismic) and a low-cost Stepped-Frequency Continuous-Wave (SFCW) Ground Penetrating Radar using a NanoVNA. Laser vibrometry adds plastic-mine detection, costs < $150 and weighs < 250 g; the SFCW GPR costs ~ $350 and gives depth profiling but requires further antenna engineering. A sensor-fusion architecture based on probabilistic grid mapping (Bayesian update) will combine these with the existing two sensors. The recommended first prototype is the laser vibrometry sensor, because it can be built in days, directly addresses the current system's biggest blind spot, and stays true to the "Building is a trace" philosophy.

2. INDIVIDUAL SENSOR PROFILE CARDS

Each card follows a uniform format: Principle, COTS components, SWaP-C, Simplified Detection Model, Performance vs. 10-object target library, Feasibility Verdict, Skeptic's Corner, and Guardian Notes.

2.1 Ground Penetrating Radar (GPR)

Principle
A broadband electromagnetic pulse (0.5-3 GHz) is transmitted into the soil; dielectric contrasts at mine bodies cause reflections. Metal and plastic mines both have a dielectric constant different from surrounding soil.

COTS Components
- NanoVNA-V2 Plus4 (SFCW vector network analyser, 50 kHz-4.4 GHz, 65x65 mm, $200)
- Two wideband Vivaldi antennas (DIY etched on FR4, ~$30 for materials)
- 3D-printed antenna holder and RPi interface (USB)
- Software: open-source "OpenGPR" processing chain (Python)

SWaP-C Estimate
- Size: 150x100x80 mm (with antennas)
- Weight: 350 g
- Power: 5 W (USB)
- Cost: $350 (total, including antennas)

Simplified Detection Model
- Measure S11 (reflection coefficient) over 0.5-3 GHz.
- Subtract mean background (empty-soil reference).
- A mine produces a reflection peak above a threshold when the antenna passes over it.
- Depth d ≈ (c · Δt) / (2√εr) with εr ~ 4-10 for dry soil. Maximum penetration ~30 cm in dry sand, ~15 cm in moist loam.

Performance vs. Target Library
- Steel AT mines (TM-62M, M15): strong reflection, detected at 30 cm.
- Plastic AP mines (PMN-2, VS-50): detectable at 10-20 cm in dry soil; very weak in wet clay.
- Steel fragments (grenade, mortar): good.

Feasibility Verdict: CONDITIONAL PASS
Works in dry-to-medium soils; fails in saturated clay. Requires careful antenna design and real-time processing. Within payload budget and open-source ecosystem.

Skeptic's Corner
- Soil moisture kills penetration; radar becomes blind after rain.
- Rugged terrain causes antenna lift-off variations, creating false alarms.
- Small plastic mines (VS-50, 0.1 A·m²) have tiny dielectric contrast → may be invisible.
- NanoVNA sweep time (seconds per trace) limits forward speed; only suitable for slow-hovering survey.

Guardian Notes
All components are consumer electronics, no ITAR restrictions. Research papers are public (e.g., MDPI Remote Sensing "Low-Cost SFCW GPR Using NanoVNA"). Used purely for demining.

2.2 Hyperspectral Imaging (HSI)

Principle
Hundreds of narrow spectral bands (VIS-NIR) sense chemical signatures of disturbed soil or explosive residues. Airborne push-broom scanning builds a spatial-spectral data cube.

COTS Components
- Hamamatsu C12880MA micro-spectrometer (340-850 nm, 15 nm res., $150, 5 g)
- Collimating lens, slit, compact scanning mechanism (rely on drone forward motion)
- RPi for capture and processing

SWaP-C Estimate
- Size: 60x40x30 mm
- Weight: 80 g (incl. optics)
- Power: 1 W
- Cost: $200

Simplified Detection Model
- Compute vegetation index (NDVI) or soil disturbance index (e.g., 680 nm/800 nm ratio).
- A freshly buried mine disturbs topsoil and stresses plants → anomaly in index map.
- Only effective for surface or very shallow (< 5 cm) objects.

Performance vs. Target Library
- Surface-laid or very shallow mines may create a spectral anomaly for a few weeks.
- No penetration, so buried mines (>5 cm) are invisible.

Feasibility Verdict: CONDITIONAL (low priority)
Excellent SWaP-C and low cost, but depth capability is near zero. Useful as a secondary cue for surface clearance, not for primary detection.

Skeptic's Corner
- Spectral signatures fade with rain and vegetation regrowth.
- Sun-angle changes and shadows produce false positives.
- Flight-induced motion blur reduces spatial resolution.

Guardian Notes
Completely civilian technology; spectral indices are public domain.

2.3 Acoustic/Seismic Vibrometry – Laser Speckle Contrast

Principle
An acoustic source excites the ground (e.g., 100-300 Hz). A buried mine creates a mechanical compliance contrast, causing a local increase in surface vibration amplitude. A laser illuminates the soil, and a high-frame-rate camera captures the speckle pattern; the temporal variance of speckle intensity maps vibration.

COTS Components
- 650 nm, 5 mW laser diode with line-generator lens ($10)
- Global-shutter camera (Arducam OV9281, 1 MP, 120 fps, $35)
- 3-inch 5 W miniature speaker + D-class amplifier ($20)
- 3D-printed gimbal for isolation
- Processing on RPi (OpenCV + FFT)

SWaP-C Estimate
- Size: 120x80x100 mm
- Weight: 210 g
- Power: 6 W (peak)
- Cost: $100

Simplified Detection Model
- Acquire image stream at ≥100 fps.
- For each pixel time-series, compute power at the excitation frequency → vibration amplitude map.
- A mine-sized amplitude anomaly above threshold flags a target.
- Excitation frequencies chosen to match mine-soil resonant modes (often 150-200 Hz).

Performance vs. Target Library
- Plastic mines: PMN-2, VS-50 → reported detection at 15-20 cm in dry sandy soil (literature).
- Steel AT mines → also detectable but already covered by magnetometer.
- Depth limited by soil stiffness; wet or clay soil reduces contrast.

Feasibility Verdict: CONDITIONAL PASS (strongly recommended)
Ultra-low cost and weight, directly addresses the plastic-mine gap. Requires robust vibration isolation and algorithmic rejection of drone self-noise.

Skeptic's Corner
- Drone rotor noise may saturate the sensor; acoustic excitation may need to be loud enough to overcome background, but then speaker weight grows.
- Ground coupling of an airborne speaker is inefficient; a ground-based shaker is better but adds operational complexity.
- Laser speckle signals are highly sensitive to platform motion; active stabilisation or post-processing image registration is essential.

Guardian Notes
Technology published in open literature (SPIE "Laser Speckle Vibrometry for Landmine Detection"). No military-only components.

2.4 Electrical Impedance/Capacitance Tomography (EIT/ECT)

Principle
A ring of electrodes contacts the soil; current injection measures impedance. Anomalies in conductivity/permittivity reveal buried objects.

Feasibility Verdict: FAIL (for UAV)
Requires physical electrode contact with the ground. Not possible from a flying drone. Could be implemented on a ground robot, but out of scope for this airborne platform.

2.5 Active Thermography

Principle
A heat source (e.g., high-power NIR LEDs or microwave) warms the soil surface; thermal camera observes the cooling curve. Mines alter thermal effusivity, producing a transient signature.

COTS Components
- 10x Luminus SST-10-IR 850 nm LEDs + heatsink (400 g, ~20 W optical)
- LED driver board
- Existing Lepton thermal camera

SWaP-C Estimate
- Weight: 450 g
- Power: 25 W (electrical)
- Cost: $150

Feasibility Verdict: FAIL (for this platform)
Payload power budget is already tight; the heater drains battery and adds significant weight. Penetration depth < 5 cm. The passive thermal camera already exploits diurnal solar heating – active heating does not justify the SWaP-C burden.

2.6 Nuclear Quadrupole Resonance (NQR) / Neutron-Based (TNA/FNA)

Principle
NQR detects ¹⁴N nuclei in explosives by radio-frequency excitation and resonance. Neutron methods induce gamma emission from nitrogen or hydrogen.

Feasibility Verdict: FAIL
Equipment weighs tens of kilograms, requires kilowatts of power and cryogenic cooling (NQR) or a radioactive source (neutron). Completely impractical for any small UAV. Excluded from further consideration.

2.7 Electronic Nose (E-nose)

Principle
Array of chemiresistive or polymer sensors responds to explosive vapour (TNT, RDX). Buried mines emit extremely low vapour concentrations.

COTS Components
- Bosch BME688 (VOC, but insensitive to TNT) – inadequate.
- FLIR Fido X3 ($15k) – far above budget.
- No low-cost explosive-specific sensor exists.

Feasibility Verdict: FAIL
Detection limits in air are ppm-ppb, while mine vapour signature in open air is orders of magnitude lower. Airborne sampling from altitude does not work. Not suitable for drone integration.

3. SENSOR FUSION BLUEPRINT

3.1 Selected Sensor Suite (Primary)
1. Fluxgate Magnetometer – ferrous object detection
2. Passive Thermal Camera (FLIR Lepton) – shallow mine thermal contrast
3. Laser Speckle Vibrometry – plastic mine detection via acoustic-seismic signature

Rationale: The vibrometer fills the critical gap of non-metallic mines. The three sensors together provide complementary physics: magnetic permeability, thermal effusivity, and mechanical impedance.

3.2 Fusion Architecture (Text Diagram)

                   +-----------+
                   |   GPS+RTK | (u-blox ZED-F9P)
                   +-----+-----+
                         | time + position
        +----------------+----------------+
        |                |                |
 [Mag Sensor]    [Thermal Cam]    [Vibrometer]
 (SPI)           (SPI)            (CSI/USB)
        |                |                |
   Mag Driver       Thermal Driver    Vibro Driver
        |                |                |
   Mag Anomaly Map  Thermal Contrast   Vibration Amplitude
   (2D grid)        Map (2D grid)      Map (2D grid)
        |                |                |
        +----------------+----------------+
                         |
                     Time Alignment
                    (ROS message_filters)
                         |
                Georeferenced Grid (0.1 m cells)
                         |
         Bayesian Occupancy Update (log-odds)
              P(mine|Mag) × P(mine|Therm) × P(mine|Vibro)
                         |
                Fused Probability Map
                         |
                  Threshold → Alarm

3.3 Software Implementation
- Framework: ROS 2 (or ROS 1) on Raspberry Pi 4
- Nodes:
  - mag_node, thermal_node, vibro_node – publish sensor_msgs/PointCloud2 or custom grid
  - fusion_node – subscribes, performs Bayesian update using grid_map package, publishes nav_msgs/OccupancyGrid
- Time Sync: All sensor messages stamped with GPS time; NTP from ZED-F9P PPS.
- State Estimation: robot_localization EKF fusing IMU, GPS, visual odometry (optional)
- Simplified Detection Models (per sensor) embedded in nodes:
  - Magnetometer: analytic signal amplitude > 3σ of background → P=0.9 for ferrous, 0.01 for plastic
  - Thermal: temperature anomaly (ΔT > 0.5 °C) after diurnal compensation → P=0.7 for shallow mines
  - Vibrometer: vibration amplitude anomaly > threshold → P=0.8 for mines in dry soil, 0.3 in wet
  These probabilities are placeholders to be tuned in field tests.

4. PRIORITIZED ACTION PLAN

Priority 1 (Immediate): Laser Speckle Vibrometry Prototype
- Lowest cost ($100) and weight (210 g)
- Directly addresses plastic AP mine blind spot
- Leverages existing Raspberry Pi and camera skills
- Can be tested on a static test bed before flight
- Source components from AliExpress/eBay; use open-source Python vibrometry code; design 3D-printed speaker mount

Priority 2 (Parallel): SFCW GPR Payload Development
- Adds depth profiling and metal/plastic discrimination
- Moderate cost ($350), weight (350 g)
- NanoVNA-based approach well-documented in open literature
- Buy NanoVNA-V2, etch Vivaldi antennas; adapt OpenGPR processing; ground-test on surrogate mine lane

Priority 3 (Following): Software Fusion Integration
- Combine mag + thermal + vibrometry maps in ROS
- Implement Bayesian grid and field-validate with inert mines
- Work in parallel with hardware testing; use recorded datasets to tune probabilities

Priority 4 (Long-term): Hyperspectral Push-broom
- Low SWaP-C but limited to surface anomalies; useful as supplementary cue for recently laid mines
- Keep as optional payload; integrate only when core suite is stable

Cancelled: EIT/ECT, Active Thermography, NQR/Neutron, E-nose
Not feasible on this UAV platform for reasons documented in profile cards

Why start with vibrometry?
It is the spirit of the project: a single maker, using a smartphone, built the first drone. The vibrometry sensor follows the same philosophy—simple components, clever physics, and immediate testability. By building the physical sensor first, we produce a trace. The commentary (this report) follows.

End of Master Research Report.
All research notes, profile cards, and pseudo-code stubs are to be committed to the research/ directory of the UXO Detection Drone repository. MIT/Apache 2.0 license applies.
