Field Validation Protocol: UXO Detection Drone

Objective
To empirically verify the detection performance of the integrated dual-sensor (fluxgate magnetometer and thermal camera) and the laser vibrometry payload against the simulated results, using inert landmine surrogates in a controlled outdoor environment.

Test Site Requirements
A flat area of at least 20 meters by 20 meters, with soil composition similar to the simulation baseline (sandy loam, 29% clay, 36% sand). The site must be cleared of all metallic debris prior to setup. Vegetation, if any, should be short and uniform to minimize thermal occlusion.

Target Preparation
Procure or fabricate inert surrogates for the following five objects from the Balkan target library: PMA-1 (plastic AP), TMA-3 (metal AT), PROM-1 (metal bounding), 82mm mortar (metal), and PMA-3 (plastic AP). Bury them at precise depths of 0.05 m, 0.10 m, 0.15 m, and 0.20 m, distributed across a predefined 5-meter by 5-meter grid.

Environmental Data Collection
Simultaneously with the drone survey, record local weather data: air temperature, soil temperature at 0.1 m depth, and soil moisture content at 0.1 m depth. Log these measurements every 60 seconds using a ground-based weather station synchronized with the drone's GPS time.

Drone Survey Procedure
Conduct three autonomous surveys following an identical lawnmower pattern at 1 meter altitude and 1 m/s ground speed.
The first survey will be conducted at 14:00 local time to capture the peak positive thermal contrast for plastic mines.
The second survey will be conducted at 03:00 local time to capture the peak negative thermal contrast for metal objects.
The third survey will be conducted at the same times, but with the laser vibrometry payload active, using acoustic excitation between 150 Hz and 200 Hz.

Data Logging
All sensor data must be timestamped with GPS time and geotagged. The magnetometer data (in nanotesla), thermal images (in radiometric format), and vibrometry amplitude maps will be logged to separate ROS bag files, along with the drone's position, attitude, and velocity estimates.

Post-Processing and Analysis
Run the fusion simulation script (fusion_simulation_vibrometry.py) in "validation mode" using the recorded environmental data and drone flight path. This will produce a predicted detection probability map. Compare this map against the known ground truth positions using the same metrics as the simulation (recall, precision, and false positives per hectare). A successful validation is defined as achieving a recall of at least 60% and a precision of at least 25%, which accounts for the expected degradation from simulation to a real-world environment.

Safety and Permissions
Obtain all necessary permissions from local authorities for outdoor drone operations and the handling of inert explosive surrogates. The test area must be secured and all personnel must maintain a safe distance during flight operations.
