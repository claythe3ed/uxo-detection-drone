#!/usr/bin/env python3
"""
Advanced thermal simulation using Fourier heat equation (unsteady).
Computes thermal contrast ΔT at surface due to a buried object.
Version 2: uses physically distinct thermal properties for buried object (e.g., plastic/wood mine).
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Soil thermal properties (from previous simulation, Bosnia clay)
ALPHA_SOIL = 1.08e-7          # m²/s thermal diffusivity (clay-rich)
K_SOIL = 0.75                 # W/(m·K) thermal conductivity
# Object properties (plastic/wood mine, very low diffusivity)
ALPHA_OBJECT = 0.15e-7        # m²/s (plastic/wood ~ 0.1-0.2e-7)
K_OBJECT = 0.25               # W/(m·K)

# Simulation domain
DEPTH_MAX = 1.0               # m
DX = 0.01                     # m spatial step
DT = 60.0                     # seconds time step (1 minute)
TIME_STEPS = 24 * 60          # 24 hours in minutes

# Surface boundary condition (sinusoidal daily temperature)
T_MEAN = 20.0                 # °C average temperature
T_AMP = 10.0                  # °C amplitude
PERIOD = 24 * 3600            # seconds

# Buried object properties
OBJECT_TOP = 0.35             # m depth (top of object)
OBJECT_BOTTOM = 0.45          # m depth (thickness 0.1 m)

# Discretization
Nz = int(DEPTH_MAX / DX) + 1
z = np.linspace(0, DEPTH_MAX, Nz)   # vertical grid (0 at surface)

# Initialize temperature profile (linear gradient from surface to deep)
T_init = T_MEAN + (T_AMP / 2.0)   # initial temperature at t=0 (noon approx)
T_deep = T_MEAN                    # deep temperature constant
T = np.full(Nz, T_deep)
# Set initial surface temperature
T[0] = T_init

# Precompute thermal diffusivity array (layer-dependent)
alpha = np.full(Nz, ALPHA_SOIL)
for i in range(Nz):
    depth = z[i]
    if OBJECT_TOP <= depth <= OBJECT_BOTTOM:
        alpha[i] = ALPHA_OBJECT

# Helper: solve heat equation via explicit FTCS
def solve_heat_equation(T, alpha, dt, dx, n_steps, surface_temp_func):
    """Time-marching solution."""
    T_history = []
    for step in range(n_steps):
        t = step * dt
        # Update surface boundary condition
        T[0] = surface_temp_func(t)
        # Deep boundary condition (constant temperature)
        T[-1] = T_deep
        
        # Compute new temperature using FTCS
        T_new = T.copy()
        for i in range(1, Nz-1):
            d2T = (T[i+1] - 2*T[i] + T[i-1]) / (dx*dx)
            T_new[i] = T[i] + alpha[i] * d2T * dt
        T = T_new
        
        # Store temperature at surface and at object depth (every hour)
        if step % 60 == 0:   # every hour
            T_history.append((t/3600.0, T[0], T[int(OBJECT_TOP/DX)]))
    return T, T_history

def surface_temperature(t_seconds):
    """Sinusoidal daily temperature."""
    return T_MEAN + T_AMP * np.sin(2 * np.pi * t_seconds / PERIOD)

# Run simulation with object
print("Running advanced thermal simulation (with distinct object properties)...")
T_final, history = solve_heat_equation(T, alpha, DT, DX, TIME_STEPS, surface_temperature)

# Compute background (no object) simulation
print("Computing background (no object) simulation...")
T_bg = np.full(Nz, T_deep)
T_bg[0] = T_init
alpha_bg = np.full(Nz, ALPHA_SOIL)
T_bg_final, history_bg = solve_heat_equation(T_bg, alpha_bg, DT, DX, TIME_STEPS, surface_temperature)

# Extract surface temperatures from both simulations
times_h = [h[0] for h in history]
T_surface_obj = [h[1] for h in history]
T_surface_bg = [h[1] for h in history_bg]
delta_T = [T_surface_obj[i] - T_surface_bg[i] for i in range(len(times_h))]

# Find maximum contrast
max_delta = max(delta_T, key=abs)
max_time = times_h[delta_T.index(max_delta)]
print("\n=== Thermal Simulation Results (V2) ===")
print(f"Maximum thermal contrast ΔT = {max_delta:.4f} °C at t = {max_time:.1f} hours")
print(f"Soil thermal diffusivity α_soil = {ALPHA_SOIL:.2e} m²/s")
print(f"Object thermal diffusivity α_obj = {ALPHA_OBJECT:.2e} m²/s")
print(f"Object depth: {OBJECT_TOP} - {OBJECT_BOTTOM} m")

# Save results to CSV
output_csv = os.path.expanduser("~/drone_remote_sensing_postwar/simulation_data/thermal_contrast_v2.csv")
with open(output_csv, 'w') as f:
    f.write("time_hours,T_surface_with_object_C,T_surface_background_C,delta_T_C\n")
    for i in range(len(times_h)):
        f.write(f"{times_h[i]},{T_surface_obj[i]},{T_surface_bg[i]},{delta_T[i]}\n")
print(f"Results saved to {output_csv}")

# Plot if matplotlib available
try:
    plt.figure()
    plt.plot(times_h, delta_T, 'r-')
    plt.xlabel('Time (hours)')
    plt.ylabel('Thermal contrast ΔT (°C)')
    plt.title('Surface thermal contrast due to buried plastic/wood object')
    plt.grid(True)
    plot_path = os.path.expanduser("~/drone_remote_sensing_postwar/simulation_data/thermal_contrast_v2.png")
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
except Exception as e:
    print("Plotting skipped (no display or matplotlib issue).")

print("\nSimulation completed.")
