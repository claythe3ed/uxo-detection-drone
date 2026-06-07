Future Work Plan

This document outlines the immediate next steps required to advance this project from simulation to field deployment. Each task is tied to an existing component in the repository and can be undertaken independently.

Thermal simulation upgrade. The current thermal model is one-dimensional and assumes a homogeneous soil background with no vegetation, rocks, or moisture dynamics. The next iteration will extend the Fourier heat conduction solver to two dimensions, incorporating a spatially varying soil moisture field and surface obstructions. The starting point is the script scripts/advanced_thermal_simulation_v2.py. The expected deliverable is a new script, thermal_simulation_2d.py, placed alongside the existing ones, together with updated simulation results in data/simulation_results.

Magnetometer interference characterization. The drone's onboard electronics generate magnetic noise that has been partially mitigated by a retractable boom but never fully modeled. The next step is to design and execute a benchtop measurement procedure that maps the magnetic field signature of each motor and power line at varying distances. The resulting data will be stored in a new file, data/magnetic_noise/motor_interference_profile.json, and integrated into the simulation pipeline by modifying scripts/realistic_simulation.py to accept a noise profile parameter.

Field validation preparation. No simulation can replace an outdoor test with a buried target. The immediate objective is to produce a detailed validation protocol that specifies the required equipment, the test grid layout, the target types and depths, the sensor settings, the data logging format, and the safety procedures. This protocol will be written as docs/FIELD_VALIDATION_PROTOCOL.md. Once reviewed, the document will serve as the basis for funding applications and collaboration proposals.

Target library expansion. The current library contains ten objects common in Bosnia, Ukraine, and Afghanistan. Additional entries are needed for cluster munition submunitions, wooden-bodied mines, and improvised explosive devices with minimal metal content. Each new entry must include the object's magnetic moment and thermal diffusivity, following the schema in target_library/targets.json.

Repository infrastructure. To lower the barrier for new contributors, the repository will be enhanced with a CONTRIBUTING.md file explaining how to set up the Python environment, run the simulations, and submit improvements. A GitHub Actions workflow will be added to automatically execute the simulation scripts and verify that output files are generated correctly on every pull request.

These tasks are open to anyone willing to contribute. Each can be tracked as a GitHub issue once the repository is active.
