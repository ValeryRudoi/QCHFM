# QCHFM CODE
Quantum-Coherent Hybrid Flow Modeling

## 🧪 QCHFM 2D Simulation Prototype

This script demonstrates a simplified 2D version of QCHFM (Quantum-Coherent Hybrid Flow Modeling) for exploring how uncertainty affects fluid flow simulation.

### 🔧 Features:
- 2D velocity field (`u`) over a fixed grid
- Quantum-inspired stochastic noise using a Wiener process
- Confidence map computed from local uncertainty
- Animated side-by-side visualization of flow + confidence

### ▶️ To Run:
```bash
pip install numpy matplotlib
python qchfm_simulation.py
```

### 📈 Output:
- Velocity field (red/blue: intensity & direction)
- Confidence map (yellow/green: trust level in prediction)
- Live animation of how both evolve over time

This serves as the core of the QCHFM framework, expandable to real-world scenarios like Mars canyons, plasma edge flows, or turbulence-aware aircraft routing.

Created by Valery Rudoi, 2025.
