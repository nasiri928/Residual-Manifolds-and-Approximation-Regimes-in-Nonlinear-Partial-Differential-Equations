"""
Extract and visualize a low-residual approximation regime for the Allen--Cahn equation.

The approximation regime is defined as the sublevel set

    M_tau = {(a, b) : residual(a, b) <= tau},

where tau is chosen as the 5th percentile of all residual values. This highlights
the subset of the parameter plane where the trial functions produce relatively
small Allen--Cahn residuals.

Input
-----
allen_cahn_residual_grid.csv
    CSV file with columns: a, b, residual.

Output
------
allen_cahn_regime.png
    Scatter plot showing the full parameter grid and the selected low-residual regime.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load residual values over the two-parameter grid.
df = pd.read_csv("allen_cahn_residual_grid.csv")

# Select a residual threshold using the lower 5% of the residual distribution.
tau = np.percentile(
    df["residual"],
    5
)

# Approximation regime: all parameter values with residual below the threshold.
M = df[
    df["residual"] <= tau
]

plt.figure(figsize=(7, 6))

# Plot the full parameter grid as a light background.
plt.scatter(
    df["a"],
    df["b"],
    c="lightgray",
    s=10,
    alpha=0.4
)

# Overlay the low-residual approximation regime.
plt.scatter(
    M["a"],
    M["b"],
    s=30
)

plt.xlabel(r"$a$")
plt.ylabel(r"$b$")
plt.title(
    rf"Approximation Regime $M_{{	au}}$, $	au={tau:.2e}$"
)

plt.tight_layout()
plt.savefig(
    "allen_cahn_regime.png",
    dpi=300
)

plt.show()

print("points =", len(M))
print("tau =", tau)
