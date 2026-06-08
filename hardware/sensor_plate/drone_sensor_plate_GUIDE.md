## Tools
- 3D printer (PLA capable)
- M3 hex key
- Wire strippers
- Soldering iron with fine tip
- Multimeter
- Heat gun (for heat shrink)
- Precision knife / Deburring tool
- Small Phillips screwdriver

## Assumptions
- Basic 3D printing knowledge
- Basic soldering experience
- Familiarity with companion computer development environments (e.g., Linux, Python, C++)
- Access to common electronics consumables (solder, wires, heat shrink, zip ties)

## 1. Fabrication
### 1.1 3D print the Main Sensor Plate (PLA, 20% infill, 0.2mm layer)
*(not yet generated)*

### 1.2 3D print all component mounts and housings (PLA, 20-30% infill, 0.2mm layer)
*(not yet generated)*

### 1.3 Clean, deburr, and inspect all 3D printed parts for defects
*(not yet generated)*

### 1.4 Test fit M3 screws and nuts into all mounting holes on printed parts
*(not yet generated)*

## 2. Wiring
### 2.1 Prepare and tin all necessary power and data wires for electrical connections
*(not yet generated)*

### 2.2 Solder VIN/VOUT power lines to the 5V Step-Down Power Supply module
*(not yet generated)*

### 2.3 Solder power (5V) and UART data lines from the main MCU to the GPS/RTK Module
*(not yet generated)*

### 2.4 Solder power (5V) and I2C data lines from the main MCU to the Fluxgate Magnetometer
*(not yet generated)*

### 2.5 Connect the FLIR Lepton Thermal Camera to its Breakout Board, then solder power (5V) and connect USB data line to main MCU
*(not yet generated)*

### 2.6 Solder power (5V) and GPIO control lines from the main MCU to the Laser Line Module
*(not yet generated)*

### 2.7 Solder power (5V) and connect CSI/I2C data lines from the main MCU to the Global Shutter Camera
*(not yet generated)*

### 2.8 Solder power (5V) and PWM audio input lines from the main MCU to the Audio Amplifier, then solder speaker output to Mini Acoustic Speaker
*(not yet generated)*

### 2.9 Solder power (5V) and connect USB data line from the main MCU to the SFCW GPR NanoVNA
*(not yet generated)*

### 2.10 Perform continuity checks on all soldered power and data lines
*(not yet generated)*

## 3. Bring-up
### 3.1 Verify 5V output from power_supply_module using a multimeter
*(not yet generated)*

### 3.2 Power on main_mcu and confirm boot-up and basic functionality
*(not yet generated)*

### 3.3 Connect GPS/RTK Module to main_mcu and verify UART communication and GPS lock
*(not yet generated)*

### 3.4 Connect Fluxgate Magnetometer to main_mcu and verify I2C communication and sensor readings
*(not yet generated)*

### 3.5 Connect Thermal Camera (via breakout) to main_mcu and verify USB camera detection
*(not yet generated)*

### 3.6 Connect Global Shutter Camera to main_mcu and verify CSI camera detection and image capture
*(not yet generated)*

### 3.7 Test Laser Line Module activation via main_mcu GPIO control
*(not yet generated)*

### 3.8 Test Acoustic Speaker output by sending audio from main_mcu through Audio Amplifier
*(not yet generated)*

### 3.9 Connect NanoVNA GPR to main_mcu and verify USB communication and basic operation
*(not yet generated)*

## 4. Assembly
### 4.1 Mount vibration isolators to the Main Sensor Plate using M3 screws and nuts
*(not yet generated)*

### 4.2 Secure main_mcu into the Raspberry Pi 4 Housing, then mount housing to the Main Sensor Plate
*(not yet generated)*

### 4.3 Mount the power_supply_module into its mount, then attach to the Main Sensor Plate
*(not yet generated)*

### 4.4 Mount GPS/RTK Module into its mount, then attach to the Main Sensor Plate
*(not yet generated)*

### 4.5 Mount Fluxgate Magnetometer into its boom mount, then attach to the Main Sensor Plate
*(not yet generated)*

### 4.6 Mount Thermal Camera into its mount and its breakout into its mount, then attach both to Main Sensor Plate
*(not yet generated)*

### 4.7 Mount Laser Line Module into its mount, then attach to the Main Sensor Plate
*(not yet generated)*

### 4.8 Mount Global Shutter Camera into its mount, then attach to the Main Sensor Plate
*(not yet generated)*

### 4.9 Mount Acoustic Speaker into its mount and Audio Amplifier into its mount, then attach both to Main Sensor Plate
*(not yet generated)*

### 4.10 Mount NanoVNA GPR into its housing, then attach housing to Main Sensor Plate along with Vivaldi antenna mounts
*(not yet generated)*

### 4.11 Route all electrical cables, ensuring proper strain relief and avoiding mutual EMI
*(not yet generated)*

### 4.12 Perform final system test of all integrated components
*(not yet generated)*
