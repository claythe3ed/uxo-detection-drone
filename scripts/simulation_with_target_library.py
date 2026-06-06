#!/usr/bin/env python3
"""
Simulate drone flight over multiple target types from the target library.
Computes magnetic anomaly and thermal contrast for each target.
"""

import json
import math
import os
import csv

# Sensor parameters (from Blueprints.am design)
MAG_SENSITIVITY_uT_per_LSB = 0.013
DETECTION_THRESHOLD_LSB = 38   # 0.5 uT / 0.013 uT/LSB
THERMAL_NETD_mK = 50.0
THERMAL_THRESHOLD_mK = 30.0

# Flight parameters
ALTITUDE_m = 1.0
GRID_SIZE_m = 10.0
STEP_m = 0.5
TARGET_POS_X = 5.0
TARGET_POS_Y = 5.0
BURIAL_DEPTH_m = 0.3   # constant for all targets for simplicity

def magnetic_anomaly(x, y, target_x, target_y, depth, moment, altitude):
    dx = x - target_x
    dy = y - target_y
    r_horiz = math.hypot(dx, dy)
    r = math.hypot(r_horiz, altitude + depth)
    B_T = (1e-7 * moment) / (r**3)
    return B_T * 1e6   # uT

def thermal_contrast(x, y, target_x, target_y, depth, peak_contrast_mK, decay_constant=1.5):
    dx = x - target_x
    dy = y - target_y
    dist = math.hypot(dx, dy)
    sigma = depth * decay_constant
    contrast = peak_contrast_mK * math.exp(-0.5 * (dist/sigma)**2)
    return contrast

def load_targets(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data['targets']

def simulate_for_target(target, depth_m=0.3, altitude_m=1.0):
    moment = target.get('magnetic_moment_Am2', 0.0)
    # Estimate peak thermal contrast based on material (crude)
    if 'steel' in target['case_material'].lower():
        peak_contrast_mK = 80.0
    elif 'plastic' in target['case_material'].lower():
        peak_contrast_mK = 30.0
    else:
        peak_contrast_mK = 50.0
    # Compute max B at zero offset
    B_max = magnetic_anomaly(TARGET_POS_X, TARGET_POS_Y, TARGET_POS_X, TARGET_POS_Y, depth_m, moment, altitude_m)
    B_lsb = B_max / MAG_SENSITIVITY_uT_per_LSB
    mag_detect = B_lsb >= DETECTION_THRESHOLD_LSB
    # Thermal: compute contrast directly above target
    contrast = thermal_contrast(TARGET_POS_X, TARGET_POS_Y, TARGET_POS_X, TARGET_POS_Y, depth_m, peak_contrast_mK)
    thermal_detect = contrast >= THERMAL_THRESHOLD_mK
    return {
        'id': target['id'],
        'name': target['name'],
        'magnetic_moment_Am2': moment,
        'B_max_uT': B_max,
        'B_lsb': B_lsb,
        'mag_detect': mag_detect,
        'thermal_contrast_mK': contrast,
        'thermal_detect': thermal_detect,
        'peak_contrast_mK': peak_contrast_mK
    }

def main():
    targets_path = os.path.expanduser("~/drone_remote_sensing_postwar/target_library/targets.json")
    targets = load_targets(targets_path)
    results = []
    print("=== Target Library Simulation ===")
    print(f"Flight altitude: {ALTITUDE_m} m, burial depth: {BURIAL_DEPTH_m} m")
    print(f"Magnetometer threshold: {DETECTION_THRESHOLD_LSB} LSB ({DETECTION_THRESHOLD_LSB * MAG_SENSITIVITY_uT_per_LSB:.3f} uT)")
    print(f"Thermal camera threshold: {THERMAL_THRESHOLD_mK} mK\n")
    for t in targets:
        res = simulate_for_target(t, BURIAL_DEPTH_m, ALTITUDE_m)
        results.append(res)
        print(f"{res['name']} (ID: {res['id']})")
        print(f"  Magnetic moment: {res['magnetic_moment_Am2']:.1f} A·m² -> B_max = {res['B_max_uT']:.3f} uT ({res['B_lsb']:.0f} LSB) -> Detect: {'YES' if res['mag_detect'] else 'NO'}")
        print(f"  Thermal contrast: {res['thermal_contrast_mK']:.1f} mK -> Detect: {'YES' if res['thermal_detect'] else 'NO'}")
        print()
    # Save results to CSV
    csv_path = os.path.expanduser("~/drone_remote_sensing_postwar/simulation_data/target_simulation_results.csv")
    with open(csv_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id","name","magnetic_moment_Am2","B_max_uT","B_lsb","mag_detect","thermal_contrast_mK","thermal_detect","peak_contrast_mK"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results saved to {csv_path}")

if __name__ == "__main__":
    main()
