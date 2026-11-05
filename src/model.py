"""AeroTwin-X: lumped two-node aerospace thermal-fluid demonstrator."""
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp

@dataclass
class Parameters:
    wall_mass: float = 12.0          # kg
    wall_cp: float = 500.0           # J/(kg K)
    coolant_mass: float = 1.5        # kg in control volume
    coolant_cp: float = 4180.0       # J/(kg K)
    h: float = 1500.0                # W/(m^2 K), illustrative
    area: float = 0.12               # m^2
    ambient_UA: float = 5.0          # W/K, effective external loss
    ambient_temp: float = 298.15     # K
    inlet_temp: float = 300.15       # K
    initial_wall_temp: float = 310.15 # K
    initial_coolant_temp: float = 300.15 # K

def simulate(p=Parameters(), duration=1200.0, points=1201):
    """Simulate wall/coolant temperatures with load and flow disturbances."""
    Cw = p.wall_mass * p.wall_cp
    Cc = p.coolant_mass * p.coolant_cp
    H = p.h * p.area
    t_eval = np.linspace(0.0, duration, points)

    def inputs(t):
        # Illustrative operating schedule: load increase, then coolant-flow reduction.
        q_in = 8000.0 if t < 400.0 else 10000.0  # W
        mdot = 0.15 if t < 750.0 else 0.10     # kg/s
        return q_in, mdot

    def rhs(t, x):
        Tw, Tc = x
        q_in, mdot = inputs(t)
        q_wall_coolant = H * (Tw - Tc)
        q_loss = p.ambient_UA * (Tw - p.ambient_temp)
        dTw = (q_in - q_wall_coolant - q_loss) / Cw
        dTc = (mdot * p.coolant_cp * (p.inlet_temp - Tc)
               + q_wall_coolant) / Cc
        return [dTw, dTc]

    sol = solve_ivp(rhs, (0.0, duration),
                    [p.initial_wall_temp, p.initial_coolant_temp],
                    t_eval=t_eval, method="RK45", rtol=1e-7, atol=1e-8)
    if not sol.success:
        raise RuntimeError(sol.message)
    q = np.array([inputs(t)[0] for t in sol.t])
    mdot = np.array([inputs(t)[1] for t in sol.t])
    return {
        "time_s": sol.t,
        "wall_temp_K": sol.y[0],
        "coolant_temp_K": sol.y[1],
        "heat_input_W": q,
        "coolant_flow_kg_s": mdot,
    }
