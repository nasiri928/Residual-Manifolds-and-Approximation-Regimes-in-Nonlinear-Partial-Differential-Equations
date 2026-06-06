"""
Visualize a filtration of Fisher--KPP residual manifolds.

This script constructs nested low-residual subsets of the parameter plane using
three percentile-based thresholds:

    M_tau1 subset M_tau2 subset M_tau3.

These sets show how the approximation regime grows as the residual threshold is
relaxed. This is useful for interpreting the geometric and topological structure
of near-solution parameter regions.

Input
-----
fisher_kpp_equilibrium_residual_grid.csv
    CSV file with columns: c, a, residual.

Output
------
fisher_kpp_equilibrium_filtration.png
    Scatter plot of nested residual manifolds in the (c, a) parameter plane.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the residual grid.
df = pd.read_csv("fisher_kpp_equilibrium_residual_grid.csv")


# Define three increasing thresholds from low residual percentiles.
tau1 = np.percentile(df["residual"], 1)
tau2 = np.percentile(df["residual"], 3)
tau3 = np.percentile(df["residual"], 7)


# Extract nested residual manifolds.
M1 = df[df["residual"] <= tau1]
M2 = df[df["residual"] <= tau2]
M3 = df[df["residual"] <= tau3]


# Plot the filtration from the largest set to the smallest set.
plt.figure(figsize=(8, 6))

plt.scatter(M3["c"], M3["a"], s=10, alpha=0.35, label=r"$M_{	au_3}$")
plt.scatter(M2["c"], M2["a"], s=20, label=r"$M_{	au_2}$")
plt.scatter(M1["c"], M1["a"], s=35, label=r"$M_{	au_1}$")

plt.xlabel(r"$c$")
plt.ylabel(r"$a$")
plt.legend()
plt.title("Fisher--KPP Filtration of Residual Manifolds")

plt.tight_layout()
plt.savefig("fisher_kpp_equilibrium_filtration.png", dpi=300)
plt.show()
