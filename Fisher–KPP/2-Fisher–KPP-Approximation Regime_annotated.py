"""
Extract and visualize a low-residual approximation regime for Fisher--KPP.

The approximation regime is defined as

    M_tau = {(c, a) : residual(c, a) <= tau},

where tau is chosen as the 5th percentile of all residual values. This produces
a parameter-space subset containing the best low-residual trial functions.

Input
-----
fisher_kpp_equilibrium_residual_grid.csv
    CSV file with columns: c, a, residual.

Output
------
fisher_kpp_equilibrium_regimes.png
    Scatter plot showing the full parameter grid and the selected low-residual
    approximation regime.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the precomputed residual grid.
df = pd.read_csv("fisher_kpp_equilibrium_residual_grid.csv")


# Select a residual threshold using the 5th percentile.
tau = np.percentile(df["residual"], 5)


# Keep only parameter pairs whose residual is below the threshold.
M = df[df["residual"] <= tau]


# Plot all parameters in gray and highlight the approximation regime.
plt.figure(figsize=(8, 6))

plt.scatter(df["c"], df["a"], c="lightgray", s=8, alpha=0.25)
plt.scatter(M["c"], M["a"], s=20)

plt.xlabel(r"$c$")
plt.ylabel(r"$a$")
plt.title(rf"Fisher--KPP Approximation Regimes, $	au={tau:.2e}$")

plt.tight_layout()
plt.savefig("fisher_kpp_equilibrium_regimes.png", dpi=300)
plt.show()


# Print threshold information for reproducibility and reporting.
print("points =", len(M))
print("tau =", tau)
