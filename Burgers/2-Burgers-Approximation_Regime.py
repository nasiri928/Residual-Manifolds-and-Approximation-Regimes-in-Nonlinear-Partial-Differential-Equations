"""
Extract and visualize a low-residual approximation regime for Burgers' equation.

The approximation regime is defined as the sublevel set

    M_tau = {(a, b) : residual(a, b) <= tau},

where tau is chosen as the 5th percentile of all residual values.

This plot highlights the region of the parameter space where the trial functions
produce comparatively small Burgers residuals.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Load residual grid
# ---------------------------------------------------------------------

# The CSV file must be generated first by running `Burgers-Data.py`.
df = pd.read_csv("burgers_residual_grid.csv")


# ---------------------------------------------------------------------
# Define the approximation regime
# ---------------------------------------------------------------------

# Use the 5th percentile as a data-driven residual threshold.
tau = np.percentile(
    df["residual"],
    5
)

# Select all parameter pairs with residual below the threshold.
M = df[
    df["residual"] <= tau
]


# ---------------------------------------------------------------------
# Plot approximation regime
# ---------------------------------------------------------------------

plt.figure(figsize=(7, 6))

# Plot the full parameter grid in the background.
plt.scatter(
    df["a"],
    df["b"],
    c="lightgray",
    s=8,
    alpha=0.25
)

# Highlight the low-residual sublevel set M_tau.
plt.scatter(
    M["a"],
    M["b"],
    s=24
)

plt.xlabel(r"$a$")
plt.ylabel(r"$b$")

plt.title(
    rf"Burgers Approximation Regime $M_{{	au}}$, $	au={tau:.2e}$"
)

plt.tight_layout()

plt.savefig(
    "burgers_regime.png",
    dpi=300
)

plt.show()

print("points =", len(M))
print("tau =", tau)
