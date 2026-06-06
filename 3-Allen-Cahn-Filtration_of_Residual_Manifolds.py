"""
Visualize a filtration of Allen--Cahn residual manifolds.

This script constructs nested residual sublevel sets using three percentile-based
thresholds:

    M_tau1 subset M_tau2 subset M_tau3.

The filtration shows how low-residual approximation regions expand as the
threshold tau increases. This is useful for studying the geometric and
persistent-topological structure of approximation regimes.

Input
-----
allen_cahn_residual_grid.csv
    CSV file with columns: a, b, residual.

Output
------
allen_cahn_filtration.png
    Scatter plot of nested residual sublevel sets in the parameter plane.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the precomputed residual grid.
df = pd.read_csv("allen_cahn_residual_grid.csv")

# Percentile-based thresholds for the residual filtration.
tau1 = np.percentile(df["residual"], 2)
tau2 = np.percentile(df["residual"], 5)
tau3 = np.percentile(df["residual"], 10)

# Nested sublevel sets. Smaller thresholds represent stricter approximation regimes.
M1 = df[df["residual"] <= tau1]
M2 = df[df["residual"] <= tau2]
M3 = df[df["residual"] <= tau3]

plt.figure(figsize=(7, 6))

# Plot the largest sublevel set first so smaller, more accurate regimes remain visible.
plt.scatter(
    M3["a"],
    M3["b"],
    s=10,
    alpha=0.4,
    label=r"$M_{	au_3}$"
)

plt.scatter(
    M2["a"],
    M2["b"],
    s=20,
    label=r"$M_{	au_2}$"
)

plt.scatter(
    M1["a"],
    M1["b"],
    s=35,
    label=r"$M_{	au_1}$"
)

plt.xlabel(r"$a$")
plt.ylabel(r"$b$")
plt.legend()
plt.title("Filtration of Residual Manifolds")

plt.tight_layout()
plt.savefig(
    "allen_cahn_filtration.png",
    dpi=300
)

plt.show()
