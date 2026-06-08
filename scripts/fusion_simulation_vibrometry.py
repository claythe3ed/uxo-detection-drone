#!/usr/bin/env python3
"""
v5.2 – Winter vs Summer comparison (January vs July 2024)
Uses dynamic thermal contrast for both months.
Prints side-by-side comparison table.
"""
import json
import numpy as np
from scipy.ndimage import maximum_filter
from collections import Counter

GRID_SIZE = 100; CELL_SIZE = 0.1; ALTITUDE = 1.0; SOIL_CLAY = 0.29

targets = [
    {"name":"PMA-1","mag":0.002,"d":0.10,"th":0.4,"vib":1,"gpr":0.2},
    {"name":"PMA-2","mag":0.003,"d":0.10,"th":0.5,"vib":1,"gpr":0.25},
    {"name":"PMA-3","mag":0.001,"d":0.10,"th":0.4,"vib":1,"gpr":0.2},
    {"name":"TMA-3","mag":2.5,"d":0.15,"th":0.6,"vib":0,"gpr":0.95},
    {"name":"TMA-4","mag":0.01,"d":0.15,"th":0.5,"vib":1,"gpr":0.3},
    {"name":"TMA-5","mag":1.8,"d":0.15,"th":0.6,"vib":0,"gpr":0.9},
    {"name":"M75 grenade","mag":0.08,"d":0.05,"th":0.2,"vib":1,"gpr":0.4},
    {"name":"60mm mortar HE","mag":0.45,"d":0.30,"th":0.3,"vib":0,"gpr":0.75},
    {"name":"82mm mortar HE","mag":1.2,"d":0.40,"th":0.3,"vib":0,"gpr":0.85},
    {"name":"120mm mortar HE","mag":3.5,"d":0.50,"th":0.4,"vib":0,"gpr":0.9},
    {"name":"PROM-1","mag":0.15,"d":0.10,"th":0.5,"vib":1,"gpr":0.35},
    {"name":"TMRP-6","mag":2.8,"d":0.15,"th":0.6,"vib":0,"gpr":0.95}
]

def load_weather(filepath):
    with open(filepath) as f:
        w = json.load(f)
    times = w["hourly"]["time"]
    soil = np.array(w["hourly"]["soil_temperature_0_to_7cm"])
    hourly = [[] for _ in range(24)]
    for t_str, temp in zip(times, soil):
        hourly[int(t_str[11:13])].append(temp)
    avg_cycle = np.array([np.mean(h) if h else 0 for h in hourly])
    # compute max slope
    max_s = 0.0
    for h in range(24):
        slope = (avg_cycle[h] - avg_cycle[(h-2)%24]) / 2.0
        if abs(slope) > max_s: max_s = abs(slope)
    return avg_cycle, max(max_s, 1.0)

jan_cycle, jan_max_slope = load_weather("data/weather/bosnia_weather_jan2024.json")
jul_cycle, jul_max_slope = load_weather("data/weather/bosnia_weather_july2024.json")

print("=== SOIL TEMPERATURE COMPARISON ===")
print(f"Month     | 06:00 | 12:00 | 15:00 | 21:00 | Max slope")
print(f"January   | {jan_cycle[6]:5.1f} | {jan_cycle[12]:5.1f} | {jan_cycle[15]:5.1f} | {jan_cycle[21]:5.1f} | {jan_max_slope:.2f}°C/h")
print(f"July      | {jul_cycle[6]:5.1f} | {jul_cycle[12]:5.1f} | {jul_cycle[15]:5.1f} | {jul_cycle[21]:5.1f} | {jul_max_slope:.2f}°C/h")

def dipole_B(m, x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    with np.errstate(divide='ignore', invalid='ignore'):
        Bz = 100 * m * (2*z**2 - x**2 - y**2) / (r**5)
    Bz[r < 0.01] = 0.0
    return np.abs(Bz)

def thermal_anomaly_dynamic(base_dT, depth, survey_hour, avg_cycle, max_slope):
    t_now = avg_cycle[survey_hour]
    t_prev = avg_cycle[(survey_hour-2)%24]
    slope = (t_now - t_prev) / 2.0
    rate_factor = min(1.0, abs(slope) / max_slope)
    depth_att = max(0.0, 1.0 - depth/0.5)
    return base_dT * rate_factor * depth_att

def run_survey(avg_cycle, max_slope, survey_hour, label):
    np.random.seed(42)
    chosen = np.random.choice(targets, 12, replace=False)
    positions = []
    for t in chosen:
        ix = np.random.randint(5, GRID_SIZE-5)
        iy = np.random.randint(5, GRID_SIZE-5)
        positions.append((ix, iy, t))

    gt = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)
    for (ix, iy, _) in positions: gt[iy, ix] = True

    x = np.arange(GRID_SIZE)*CELL_SIZE; y = np.arange(GRID_SIZE)*CELL_SIZE
    X, Y = np.meshgrid(x, y)

    mag_map = np.zeros_like(X); thermal_map = np.zeros_like(X)
    vibro_map = np.zeros_like(X); gpr_map = np.zeros_like(X); hsi_map = np.zeros_like(X)

    for ix, iy, t in positions:
        xc, yc = ix*CELL_SIZE, iy*CELL_SIZE
        dx, dy = X - xc, Y - yc
        Bz = dipole_B(t["mag"], dx, dy, ALTITUDE + t["d"])
        mag_map[np.sqrt(dx**2+dy**2) <= 1.0] += Bz[np.sqrt(dx**2+dy**2) <= 1.0]
        dT = thermal_anomaly_dynamic(t["th"], t["d"], survey_hour, avg_cycle, max_slope)
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                ny, nx = iy+di, ix+dj
                if 0<=ny<GRID_SIZE and 0<=nx<GRID_SIZE:
                    thermal_map[ny, nx] += dT*0.25
        if t.get("vib",1):
            amp = 0.85*np.exp(-t["d"]/0.12) if t["d"]<=0.3 else 0
            amp *= max(0.1, 1.0 - SOIL_CLAY/0.5)
            vibro_map += amp * np.exp(-((X-xc)**2 + (Y-yc)**2)/(2*0.15**2))
        if t.get("gpr",0)>0 and t["d"]<=0.3:
            sig = t["gpr"] * np.exp(-SOIL_CLAY/0.2) * np.exp(-t["d"]/0.15)
            gpr_map += sig * np.exp(-((X-xc)**2 + (Y-yc)**2)/(2*0.12**2))
        if t["d"] <= 0.05:
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    ny, nx = iy+di, ix+dj
                    if 0<=ny<GRID_SIZE and 0<=nx<GRID_SIZE:
                        hsi_map[ny, nx] = max(hsi_map[ny, nx], 0.6)

    np.random.seed(1234)
    mag_map += np.random.normal(0, 1.0, mag_map.shape)
    thermal_map += np.random.normal(0, 0.2, thermal_map.shape)
    vibro_map += np.random.normal(0, 0.1, vibro_map.shape)
    gpr_map += np.random.normal(0, 0.08, gpr_map.shape)
    hsi_map += np.random.normal(0, 0.05, hsi_map.shape)

    def detect_peaks(data, threshold_abs, min_distance=3):
        footprint = np.ones((min_distance, min_distance))
        local_max = (data == maximum_filter(data, footprint=footprint))
        peaks = local_max & (data > threshold_abs)
        ys, xs = np.where(peaks)
        return list(zip(xs, ys))

    peaks_mag   = detect_peaks(mag_map,   10.0)
    peaks_therm = detect_peaks(thermal_map, 0.6)
    peaks_vibro = detect_peaks(vibro_map,   0.25)
    peaks_gpr   = detect_peaks(gpr_map,     0.20)
    peaks_hsi   = detect_peaks(hsi_map,     0.4)

    def vote_window_5(px, py):
        cells = [(px, py)]
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = px+dx, py+dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                cells.append((nx, ny))
        return cells

    vote_counter = Counter()
    for px, py in peaks_therm + peaks_vibro + peaks_gpr:
        for cx, cy in vote_window_5(px, py):
            vote_counter[(cx, cy)] += 1

    detected_cells = set()
    for px, py in peaks_mag: detected_cells.add((px, py))
    for px, py in peaks_hsi: detected_cells.add((px, py))
    for cell, w in vote_counter.items():
        if w >= 2: detected_cells.add(cell)

    detected = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)
    for cx, cy in detected_cells: detected[cy, cx] = True

    detected_gt = np.zeros_like(gt, dtype=bool)
    for cx, cy in detected_cells:
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                ny, nx = cy+di, cx+dj
                if 0<=ny<GRID_SIZE and 0<=nx<GRID_SIZE:
                    detected_gt[ny, nx] = True

    tp = sum(1 for ix, iy, _ in positions if np.any(detected_gt[iy-1:iy+2, ix-1:ix+2]))
    fp = len(detected_cells) - tp
    fn = len(positions) - tp
    recall = tp/len(positions) if positions else 0
    precision = tp/len(detected_cells) if detected_cells else 0

    return {
        "time": label,
        "soil_temp": avg_cycle[survey_hour],
        "slope": (avg_cycle[survey_hour] - avg_cycle[(survey_hour-2)%24]) / 2.0,
        "therm_peaks": len(peaks_therm),
        "detections": len(detected_cells),
        "tp": tp, "fp": fp, "fn": fn,
        "recall": recall, "precision": precision
    }

time_slots = [("DAWN",6), ("NOON",12), ("AFTERNOON",15), ("NIGHT",21)]

print("\n==================== JANUARY RESULTS ====================")
for label, hour in time_slots:
    res = run_survey(jan_cycle, jan_max_slope, hour, label)
    print(f"{label:12s} | slope={res['slope']:+.2f}°C/h | ThermPeaks={res['therm_peaks']} | Det={res['detections']} | TP={res['tp']} FP={res['fp']} FN={res['fn']} | Recall={res['recall']:.1%} Precision={res['precision']:.1%}")

print("\n==================== JULY RESULTS ====================")
for label, hour in time_slots:
    res = run_survey(jul_cycle, jul_max_slope, hour, label)
    print(f"{label:12s} | slope={res['slope']:+.2f}°C/h | ThermPeaks={res['therm_peaks']} | Det={res['detections']} | TP={res['tp']} FP={res['fp']} FN={res['fn']} | Recall={res['recall']:.1%} Precision={res['precision']:.1%}")

print("\n======= BEST TIME RECOMMENDATION =======")
# Find best precision for July
best = max([run_survey(jul_cycle, jul_max_slope, h, l) for l,h in time_slots], key=lambda x: x['precision'])
print(f"Optimal survey time: {best['time']} (July, {best['soil_temp']:.1f}°C, slope={best['slope']:+.2f}°C/h)")
print(f"  Recall={best['recall']:.1%}, Precision={best['precision']:.1%}, Detections={best['detections']}")
