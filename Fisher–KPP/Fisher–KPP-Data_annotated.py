"""
Generate the residual grid for a two-parameter Fisher--KPP trial family.

This script evaluates a simple parametric ansatz for the Fisher--KPP equation

    u_t = D u_xx + r u(1 - u),

or equivalently the residual form

    R(u) = u_t - D u_xx - r u(1 - u).

The trial function is

    u(x,t) = c + a sin(x) sin(t),

where c is a baseline equilibrium-like level and a is an oscillatory amplitude.
For each pair (c, a), the mean squared residual is computed over randomly sampled
space-time points. The resulting residual landscape is saved as a CSV file and is
used by the visualization and topological-analysis scripts in this folder.

Output
------
fisher_kpp_equilibrium_residual_grid.csv
    Columns: c, a, residual.
"""

import numpy as np
import pandas as pd


# -----------------------------------------------------------------------------
# Fisher--KPP equation parameters
# -----------------------------------------------------------------------------
# D is the diffusion coefficient and r is the logistic growth rate.
D = 0.1
r = 1.0


# -----------------------------------------------------------------------------
# Parameter grid for the trial family
# -----------------------------------------------------------------------------
# c controls the baseline level of the solution candidate.
# a controls the amplitude of the oscillatory perturbation.
c_values = np.linspace(-0.2, 1.2, 160)
a_values = np.linspace(-0.2, 0.2, 120)


# -----------------------------------------------------------------------------
# Random space-time sample points
# -----------------------------------------------------------------------------
# A fixed random seed makes the experiment reproducible for GitHub users.
n_points = 700
np.random.seed(42)

x = np.random.uniform(0, np.pi, n_points)
t = np.random.uniform(0, np.pi, n_points)


# -----------------------------------------------------------------------------
# Residual evaluation over the full parameter grid
# -----------------------------------------------------------------------------
results = []

for c in c_values:
    for a in a_values:

        # Trial function: equilibrium baseline plus oscillatory perturbation.
        u = c + a * np.sin(x) * np.sin(t)

        # Analytical derivatives of the trial function.
        ut = a * np.sin(x) * np.cos(t)
        uxx = -a * np.sin(x) * np.sin(t)

        # Fisher--KPP residual: R = u_t - D u_xx - r u(1-u).
        residual = ut - D * uxx - r * u * (1 - u)

        # Mean squared residual over the sampled space-time points.
        mse = np.mean(residual**2)

        results.append([c, a, mse])


# -----------------------------------------------------------------------------
# Save residual grid for downstream scripts
# -----------------------------------------------------------------------------
df = pd.DataFrame(results, columns=["c", "a", "residual"])
df.to_csv("fisher_kpp_equilibrium_residual_grid.csv", index=False)


# Print a short numerical summary for quick verification.
print("Minimum residual:", df["residual"].min())
print(df["residual"].quantile([0.01, 0.02, 0.05, 0.10]))
