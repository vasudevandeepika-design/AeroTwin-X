from pathlib import Path
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.model import simulate, Parameters

ROOT = Path(__file__).resolve().parent
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

result = simulate(Parameters())
df = pd.DataFrame(result)
df["time_min"] = df["time_s"] / 60.0
df.to_csv(out / "baseline_simulation.csv", index=False)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(df["time_min"], df["wall_temp_K"], label="Engine wall temperature")
ax.plot(df["time_min"], df["coolant_temp_K"], label="Coolant bulk temperature")
ax.axvline(400/60, color="grey", linestyle="--", alpha=.7, label="Engine load increase")
ax.axvline(750/60, color="black", linestyle=":", alpha=.7, label="Coolant-flow reduction")
ax.set_xlabel("Time (min)")
ax.set_ylabel("Temperature (K)")
ax.set_title("AeroTwin-X | Two-node thermal-fluid transient simulation")
ax.grid(True, alpha=.25)
ax.legend()
fig.tight_layout()
fig.savefig(out / "temperature_response.png", dpi=180)
print("Simulation complete.")
print(f"Final wall temperature: {df.wall_temp_K.iloc[-1]:.2f} K")
print(f"Final coolant temperature: {df.coolant_temp_K.iloc[-1]:.2f} K")
print(f"Saved: {out / 'temperature_response.png'}")
