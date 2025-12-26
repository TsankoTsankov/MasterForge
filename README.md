# 🏭 MasterForge: The Machine Shop Cheatsheet
MasterForge is a modular web dashboard designed for the modern machine shop floor. It replaces physical charts, dirty calculators, and "back-of-the-napkin" math with precise, interactive digital tools.

![Version](https://img.shields.io/badge/version-0.1.0--alpha-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/status-🚧_Under_Construction-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
> **System Status:** 🟢 Online | **Latest Module:** Tap & Drill Chart

---

## Current Capabilities
The application currently hosts the following modules:

- ⚪ Bolt Circle Generator: Calculates X/Y coordinates for bolt patterns and visualizes hole locations relative to the part center.
- ⬡ Hexagon Calculator: Converts "Across Flats" (wrench size) to "Across Points" (vertex coordinates) for CNC profiling.
- 🔩 Tap & Drill Chart: Interactive lookup for Metric (ISO) and Imperial (UNC/UNF) threads, distinguishing between Cut Taps and Form Taps.

## 🗺️ Roadmap (TODO)
The goal is to build a complete suite of manufacturing utilities.

📐 Geometry & Math

- [ ] Right Triangle Solver: Calculate unknown sides/angles for chamfers and taper checks.

- [ ] Countersink Depth Calculator: Determine Z-depth based on hole diameter and tool angle (90°/82°/60°).

- [ ] Sine Bar Stack Calc: Calculate gauge block stack height for precision setups.

🔍 Inspection & Quality
- [ ] GD&T Decoder: Interactive guide for symbols (True Position, Parallelism) with inspection methods.

- [ ] Hardness Converter: Instant conversion between HRC, HRB, Brinell, and Tensile Strength.

- [ ] Surface Finish Comparator: Visual and numerical reference for Ra/Rz/RMS.

🔩 Planning & Material
- [ ] Stock Weight Calculator: Estimate weight and cost for Round/Rectangular stock (Steel, Alum, Brass).

- [ ] Unit Converter: Shop-specific conversions (Nm ↔ Ft-Lbs, Bar ↔ PSI).

⚡ Advanced
- [ ] Feeds & Speeds Engine: Connect to external Material Catalog (Google Sheets/Database) for live cutting data.

- [ ] Cutter Comp Visualizer: Graphical guide for G41/G42 selection (Climb vs. Conventional).

# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.