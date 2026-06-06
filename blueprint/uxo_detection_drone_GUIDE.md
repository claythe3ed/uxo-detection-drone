## Tools
- Soldering iron with fine tip
- Solder
- Wire strippers
- Wire cutters
- Precision pliers
- Digital Multimeter
- M3 hex key
- M2 screwdriver
- Small Phillips head screwdriver
- Tweezers
- Hot glue gun
- 3D printer (PETG, PLA, TPU capable)
- Hobby knife/Deburring tool

## Assumptions
- Basic soldering experience
- Familiarity with drone flight controller software (e.g., ArduPilot, PX4) setup and flashing
- Experience with programming microcontrollers (e.g., Arduino IDE for Payload MCU)
- Understanding of LiPo battery safety and handling
- Access to a computer with necessary drivers and software for component configuration
- Knowledge of basic serial communication protocols (UART, I2C, RS485)

## 1. Fabrication
### 1.1 3D print all custom mounts and mechanisms using specified materials and settings
*(not yet generated)*

### 1.2 Deburr and clean all 3D printed parts, ensuring smooth surfaces and proper fit
*(not yet generated)*

### 1.3 Inspect main frame components for manufacturing defects and ensure hole alignment
*(not yet generated)*

### 1.4 Pre-assemble mechanical joints and test fit to verify clearances
*(not yet generated)*

## 2. Wiring
### 2.1 Solder XT60 connector to Main LiPo Battery (if not pre-attached) and to Power Distribution Board
*(not yet generated)*

### 2.2 Solder motor phase wires from each ESC to its corresponding motor
*(not yet generated)*

### 2.3 Solder power input wires from Power Distribution Board to each ESC
*(not yet generated)*

### 2.4 Connect power output (5V, 12V) from Power Distribution Board to Flight Controller, Payload MCU, GNSS Module, Telemetry Radio, Magnetometers, and Laser Altimeter
*(not yet generated)*

### 2.5 Connect PWM signal wires from Flight Controller to each ESC
*(not yet generated)*

### 2.6 Wire all UART/I2C/RS485 data connections between Flight Controller, Payload MCU, GNSS Module, Telemetry Radio, Magnetometers, and Laser Altimeter
*(not yet generated)*

### 2.7 Perform continuity checks on all power and data lines to prevent shorts
*(not yet generated)*

## 3. Bring-up
### 3.1 Connect Flight Controller to computer, flash drone firmware, and perform initial configuration
*(not yet generated)*

### 3.2 Connect Payload MCU to computer, upload custom sensor acquisition and processing code
*(not yet generated)*

### 3.3 Power on the system (without propellers), verify 5V and 12V power rails with multimeter
*(not yet generated)*

### 3.4 Verify GNSS module is recognized by Flight Controller and receiving satellite data
*(not yet generated)*

### 3.5 Test Telemetry Radio communication between drone and ground station
*(not yet generated)*

### 3.6 Verify data acquisition from magnetometers and laser altimeter via Payload MCU serial console
*(not yet generated)*

### 3.7 Calibrate ESCs and perform individual motor spin tests using flight controller software (without propellers)
*(not yet generated)*

## 4. Assembly
### 4.1 Assemble the main frame by attaching arms to the bottom plate and then securing the top plate with standoffs and screws
*(not yet generated)*

### 4.2 Mount ESCs into their respective 3D printed mounts and attach mounts to the main frame bottom plate
*(not yet generated)*

### 4.3 Mount motors to the frame arms and attach propellers, ensuring correct rotation direction and tight fit
*(not yet generated)*

### 4.4 Mount the Flight Controller and Payload MCU to their 3D printed mounts and secure them to the main frame bottom plate using nylon standoffs/screws
*(not yet generated)*

### 4.5 Mount the Boom Retraction Mechanism to the bottom plate and attach the Collapsible Sensor Boom, then mount magnetometers and laser altimeter to boom mounts
*(not yet generated)*

### 4.6 Assemble the GNSS mast and mount the GNSS module to its top mount, then attach the mast to the main frame top plate
*(not yet generated)*

### 4.7 Mount the Telemetry Radio into its 3D printed mount and secure it to the main frame bottom plate
*(not yet generated)*

### 4.8 Route all cables neatly, use cable ties for strain relief, and secure the Main LiPo Battery with the battery strap
*(not yet generated)*
