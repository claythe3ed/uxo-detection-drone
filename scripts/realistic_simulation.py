#!/usr/bin/env python3
"""
Realistic simulation: fly over a grid, compute magnetic anomaly and thermal contrast.
Detects a simulated buried target (landmine surrogate).
"""

import json
import math
import os
import numpy as np   # requires 'pkg install python-numpy' or 'pip install numpy'

# Load parameters from Blueprints.am design (simplified)
MAGNETOMETER_SENSITIVITY_uT_per_LSB = 0.013   # 13 nT/LSB
DETECTION_THRESHOLD_LSB = 38                 # approx 0.5 uT / 0.013 uT_per_LSB = 38 LSB
THERMAL_CAMERA_NETD_mK = 50                  # mK (from FLIR Lepton 3.5)
THERMAL_CONTRAST_THRESHOLD_mK = 30           # minimum detectable contrast

# Target properties (simulated landmine)
TARGET_MAGNETIC_MOMENT_Am2 = 12.0            # stronger than earlier example
TARGET_DEPTH_m = 0.35                        # 35 cm deep
TARGET_POSITION_X = 5.0                      # center of grid
TARGET_POSITION_Y = 5.0
TARGET_THERMAL_CONTRAST_mK = 45.0            # peak contrast at surface

# Simulation grid
GRID_SIZE_m = 10.0
STEP_m = 0.5                                 # resolution (drone samples every 0.5 m)
FLIGHT_ALTITUDE_m = 1.0

def magnetic_anomaly(x, y, target_x, target_y, depth, moment, altitude):
    """Returns B (uT) at drone position (x,y,altitude) from target at (target_x,target_y,-depth)"""
    dx = x - target_x
    dy = y - target_y
    r_horiz = math.sqrt(dx*dx + dy*dy)
    r = math.sqrt(r_horiz*r_horiz + (altitude + depth)**2)
    B = (1e-7 * moment) / (r**3)   # Tesla
    return B * 1e6   # uT

def thermal_contrast(x, y, target_x, target_y, depth, peak_contrast_mK, decay_constant=1.5):
    """Simplified Gaussian-like thermal contrast (mK) decaying with horizontal distance"""
    dx = x - target_x
    dy = y - target_y
    dist = math.sqrt(dx*dx + dy*dy)
    sigma = depth * decay_constant   # spread parameter
    contrast = peak_contrast_mK * math.exp(-0.5 * (dist/sigma)**2)
    return contrast

def main():
    print("=== Realistic Simulation of UXO Detection Drone ===")
    print(f"Grid: {GRID_SIZE_m}x{GRID_SIZE_m} m, step {STEP_m} m")
    print(f"Flight altitude: {FLIGHT_ALTITUDE_m} m")
    print(f"Target buried at depth {TARGET_DEPTH_m} m, moment {TARGET_MAGNETIC_MOMENT_Am2} A·m²")
    print(f"Magnetometer sensitivity: {MAGNETOMETER_SENSITIVITY_uT_per_LSB} uT/LSB")
    print(f"Thermal camera NETD: {THERMAL_CAMERA_NETD_mK} mK")
    print("")

    # Prepare grid points
    x_vals = np.arange(0, GRID_SIZE_m + STEP_m/2, STEP_m)
    y_vals = np.arange(0, GRID_SIZE_m + STEP_m/2, STEP_m)
    detected_mag = False
    detected_thermal = False
    max_B = 0.0
    max_contrast = 0.0

    # We'll store results for later plotting (optional)
    results = []

    for x in x_vals:
        for y in y_vals:
            B = magnetic_anomaly(x, y, TARGET_POSITION_X, TARGET_POSITION_Y, TARGET_DEPTH_m, TARGET_MAGNETIC_MOMENT_Am2, FLIGHT_ALTITUDE_m)
            contrast = thermal_contrast(x, y, TARGET_POSITION_X, TARGET_POSITION_Y, TARGET_DEPTH_m, TARGET_THERMAL_CONTRAST_mK)
            mag_detect = (B / MAGNETOMETER_SENSITIVITY_uT_per_LSB) >= DETECTION_THRESHOLD_LSB
            thermal_detect = contrast >= THERMAL_CONTRAST_THRESHOLD_mK
            if mag_detect:
                detected_mag = True
            if thermal_detect:
                detected_thermal = True
            if B > max_B:
                max_B = B
            if contrast > max_contrast:
                max_contrast = contrast
            results.append((x, y, B, contrast))

    print("--- Detection Results ---")
    print(f"Maximum magnetic field anomaly: {max_B:.3f} µT")
    print(f"Maximum thermal contrast: {max_contrast:.1f} mK")
    print(f"Magnetometer detection achieved: {'YES' if detected_mag else 'NO'}")
    print(f"Thermal camera detection achieved: {'YES' if detected_thermal else 'NO'}")
    print("")

    if detected_mag and detected_thermal:
        print("✅ Both sensors would detect the target. Fusion is possible.")
    elif detected_mag:
        print("⚠️ Only magnetometer detects. Thermal contrast too weak (consider different burial depth/time of day).")
    elif detected_thermal:
        print("⚠️ Only thermal camera detects. Target may be non-metallic or deep.")
    else:
        print("❌ Neither sensor detects. Target may be too deep or sensor sensitivity insufficient.")

    # Optionally save results as CSV
    import csv
    csv_path = os.path.expanduser("~/drone_remote_sensing_postwar/simulation_data/simulation_results.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x (m)", "y (m)", "B (uT)", "Thermal contrast (mK)"])
        writer.writerows(results)
    print(f"\nDetailed results saved to {csv_path}")

if __name__ == "__main__":
    main()
