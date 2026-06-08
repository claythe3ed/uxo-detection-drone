## Tools
- 3D printer (PETG capable)
- Soldering iron with fine tip
- Wire strippers
- Multimeter
- M2.5 hex key
- M3 hex key
- Small Phillips screwdriver (optional, for general electronics)
- Hot air gun or specific tip for heat-set inserts (optional, but recommended)

## Assumptions
- Basic 3D printing experience and printer calibration knowledge.
- Basic soldering experience for small components and power connections.
- Familiarity with Raspberry Pi OS setup and basic command line operations.
- Access to a 5V USB power source for initial Raspberry Pi testing.
- General understanding of electrical safety and polarity.

## 1. Fabrication
### 1.1 3D print all mechanical components according to specified materials and infills.
*(not yet generated)*

### 1.2 Deburr and clean all 3D printed parts.
*(not yet generated)*

### 1.3 Insert M3 heat set inserts into the main chassis and electronics enclosure base.
*(not yet generated)*

### 1.4 Test fit the NanoVNA and Raspberry Pi into their integrated mounts on the enclosure base.
*(not yet generated)*

## 2. Wiring
### 2.1 Solder input and output wires to the DC-DC Step-down module.
*(not yet generated)*

### 2.2 Solder power input wires from the DC-DC Step-down to both LDO regulators (VIN+ to VIN, VIN- to GND).
*(not yet generated)*

### 2.3 Solder output wires from the Raspberry Pi LDO regulator to the Raspberry Pi's 5V power input.
*(not yet generated)*

### 2.4 Solder output wires from the NanoVNA LDO regulator to the NanoVNA's 5V power input.
*(not yet generated)*

### 2.5 Connect the Raspberry Pi to the NanoVNA via a USB3.0 to USB-C cable.
*(not yet generated)*

### 2.6 Connect SMA Coaxial Cable (Port 1) to NanoVNA Port 1 and the Transmit Antenna.
*(not yet generated)*

### 2.7 Connect SMA Coaxial Cable (Port 2) to NanoVNA Port 2 and the Receive Antenna.
*(not yet generated)*

## 3. Bring-up
### 3.1 Verify LDO output voltages (5V) with a multimeter before connecting to sensitive electronics.
*(not yet generated)*

### 3.2 Apply input power to the DC-DC step-down and confirm correct voltage outputs.
*(not yet generated)*

### 3.3 Power up the Raspberry Pi and install the necessary operating system and GPR software.
*(not yet generated)*

### 3.4 Power up the NanoVNA and confirm it functions independently.
*(not yet generated)*

### 3.5 Connect the Raspberry Pi to the NanoVNA and verify communication/device recognition.
*(not yet generated)*

### 3.6 Perform initial GPR system test without antennas connected to confirm software integration.
*(not yet generated)*

## 4. Assembly
### 4.1 Mount the Raspberry Pi controller into its integrated mount on the electronics enclosure base using M2.5 screws.
*(not yet generated)*

### 4.2 Mount the NanoVNA GPR module into its integrated mount on the electronics enclosure base using M2.5 screws.
*(not yet generated)*

### 4.3 Mount the DC-DC Step-down module onto the power module mount using appropriate M2.5 screws.
*(not yet generated)*

### 4.4 Mount the power module mount onto the electronics enclosure base.
*(not yet generated)*

### 4.5 Secure the SMA Coaxial Cable mounts to the electronics enclosure base.
*(not yet generated)*

### 4.6 Attach the Transmit and Receive Vivaldi Antennas to their respective left and right antenna mounts.
*(not yet generated)*

### 4.7 Mount the left and right antenna mounts to the main chassis using M3 screws and nuts.
*(not yet generated)*

### 4.8 Secure the electronics enclosure base (with all internal components) to the main chassis using M3 screws into the heat set inserts.
*(not yet generated)*

### 4.9 Attach the drone quick-release adapter to the main chassis using M3 screws and nuts.
*(not yet generated)*

### 4.10 Close the electronics enclosure by securing the electronics enclosure lid to the base with M3 screws.
*(not yet generated)*

### 4.11 Perform a final system power-up and functional check with antennas attached.
*(not yet generated)*
