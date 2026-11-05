# AeroTwin-X
**Physics-Based Aerospace Thermal-Fluid Digital Twin with Dynamic State Estimation and Predictive Fault Monitoring**

## Status
Individual project — preliminary mathematical model and executable simulation prototype. This repository is a starter proof of concept, not a validated engine digital twin.

## What is implemented
- Two lumped thermal control volumes: engine wall and well-mixed coolant.
- First-principles energy balances.
- Transient numerical integration using `scipy.integrate.solve_ivp`.
- Illustrative engine-load increase and coolant-flow reduction.
- Temperature-response plot and CSV output.
- Optional Streamlit dashboard with adjustable nominal heat input, coolant flow and heat-transfer coefficient.

## Governing equations
Let `Tw` be wall temperature and `Tc` be bulk coolant temperature.

`Cw dTw/dt = Qin - hA(Tw - Tc) - UA_amb(Tw - Tamb)`

`Cc dTc/dt = mdot cp,c(Tin - Tc) + hA(Tw - Tc)`

where `Cw = mw cp,w` and `Cc = mc cp,c`.

The coolant is treated as incompressible, perfectly mixed and single-phase. Wall and coolant properties are constant. The model neglects spatial gradients, combustion chemistry, radiation and compressible-flow effects. Parameters are illustrative and must not be interpreted as measured engine data.

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python run_demo.py
```
The plot and simulation data are saved in `outputs/`.

## Launch the dashboard
```bash
streamlit run app.py
```

## Planned development (November–December 2026)
1. Verify parameter ranges and perform sensitivity analysis.
2. Add sensor models and synthetic measurement noise.
3. Discretize the state-space model and assess observability.
4. Implement a Kalman Filter for state estimation.
5. Introduce coolant-flow degradation and sensor faults; evaluate residual-based detection.
6. Extend towards a distributed thermal-fluid model and, subject to suitable data, compare with CFD or experimental measurements.

## Important limitations
This is a simplified thermal-management demonstrator. It does not simulate a complete gas turbine or rocket engine, and it has not been validated against proprietary engine data or an experimental test rig. Any future validation claims will be made only after appropriate data and testing are available.
