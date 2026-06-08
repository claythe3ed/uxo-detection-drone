Contributing to UXO Detection Drone

Thank you for considering a contribution. This document explains how to set up the project, run the simulations, and submit your work.

Code of Conduct
This project serves a single purpose: protecting civilians from the remnants of war. Every contribution, discussion, and decision must align with that mission. Be direct, be constructive, and respect the time of others. We do not tolerate grandstanding, bikeshedding, or hostility disguised as honesty.

Setting Up
Clone the repository to your local machine. The project is developed and tested on Python 3.10 and above. Install the required packages by running the following command from the repository root:

pip install numpy matplotlib scipy

All simulation scripts are located in the `scripts/` directory. The data they require is in `data/` and the target library is in `target_library/`.

Running the Simulations
Before making changes, run the existing simulations to establish a baseline. The core simulation scripts are:

- `scripts/simulation_with_target_library.py` – Magnetic dipole model for all ten original targets.
- `scripts/advanced_thermal_simulation_v2.py` – One-dimensional Crank-Nicolson thermal model using Bosnia weather data.
- `scripts/realistic_simulation.py` – Flight grid simulation combining magnetic and thermal detection.
- `scripts/fusion_simulation_vibrometry.py` – The latest multi-sensor fusion simulation using peak detection and spatial voting. This is the script you will most likely work with.

To run the fusion simulation and verify everything is working, execute the following command from the repository root:

python3 scripts/fusion_simulation_vibrometry.py

The script will print performance metrics to the terminal and save a result image as `fusion_simulation_result.png`. If the script runs without errors and generates a valid image, your environment is set up correctly.

Where to Help
We track all work as GitHub Issues. Look for issues tagged `good first issue` if you are new to the project. The current priorities are:

- Improving the two-dimensional and three-dimensional thermal model.
- Adding new target types to `target_library/targets.json`.
- Enhancing the sensor noise models with published empirical data.
- Building a ROS 2 workspace for real-time sensor fusion, starting from the architecture described in `research/MASTER_RESEARCH_REPORT.md`.

Before starting work on a significant change, open an issue to discuss your approach. This prevents wasted effort on a path that may not align with the project's direction.

Submitting Changes
Create a fork of the repository and make your changes on a new branch. Name the branch descriptively, using the convention `feature/short-description` or `fix/short-description`. When your work is ready, open a pull request against the `main` branch of this repository. The pull request description must clearly state what problem the change solves and how it was tested. If you modified a simulation script, include before-and-after performance metrics.

Your pull request will be reviewed against the following criteria. The change must align with the humanitarian mission. It must be documented sufficiently for the next person to understand. It must not break existing functionality, and any new simulation code must be verified against published data or analytical solutions.

Communication
Use GitHub Issues for bug reports, feature requests, and technical discussions. Be specific. A good issue includes the exact command you ran, the full error message, and the version of Python and libraries you are using. A poor issue says "the simulation does not work." We will ask for details before we can help.

License
By contributing, you agree that your work will be distributed under the same dual license as the rest of the project: MIT and Apache 2.0.

This project was built by a single maker on a phone. It grows because others decide to leave their own trace. We are glad you are here.
