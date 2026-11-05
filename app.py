import streamlit as st
import matplotlib.pyplot as plt
from src.model import simulate, Parameters

st.set_page_config(page_title="AeroTwin-X Demo", layout="wide")
st.title("AeroTwin-X | Aerospace Thermal-Fluid Digital Twin")
st.caption("Preliminary lumped-parameter simulation prototype — illustrative parameters, not validated engine data.")

col1, col2, col3 = st.columns(3)
with col1:
    heat = st.slider("Engine heat input (W)", 4000, 14000, 8000, 500)
with col2:
    flow = st.slider("Coolant mass flow (kg/s)", 0.05, 0.30, 0.15, 0.01)
with col3:
    h = st.slider("Heat-transfer coefficient (W/m²K)", 500, 3000, 1500, 100)

p = Parameters(h=float(h))
# Reuse the physical model with a user-selected nominal heat input and flow by
# temporarily defining a constant-input simulation for the dashboard.
import numpy as np
from scipy.integrate import solve_ivp

Cw = p.wall_mass*p.wall_cp
Cc = p.coolant_mass*p.coolant_cp
H = p.h*p.area
L = p.ambient_UA
def rhs(t, x):
    Tw, Tc = x
    qwc = H*(Tw-Tc)
    qloss = L*(Tw-p.ambient_temp)
    return [(heat-qwc-qloss)/Cw,
            (flow*p.coolant_cp*(p.inlet_temp-Tc)+qwc)/Cc]
t = np.linspace(0, 1200, 601)
sol = solve_ivp(rhs, (0,1200), [p.initial_wall_temp,p.initial_coolant_temp], t_eval=t)
st.subheader("Predicted thermal response")
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(t/60, sol.y[0], label="Engine wall")
ax.plot(t/60, sol.y[1], label="Coolant")
ax.set_xlabel("Time (min)")
ax.set_ylabel("Temperature (K)")
ax.grid(alpha=.25)
ax.legend()
st.pyplot(fig)
a,b = st.columns(2)
a.metric("Final wall temperature", f"{sol.y[0,-1]:.2f} K")
b.metric("Final coolant temperature", f"{sol.y[1,-1]:.2f} K")
st.info("Next development stages: transient operating profiles, synthetic sensor noise, observability analysis, Kalman filtering and fault detection.")
