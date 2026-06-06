"""
Generate the residual grid for a two-parameter trial family of the Allen--Cahn equation.

This script evaluates a simple analytic trial function

    u(x, t; a, b) = a sin(x) sin(t) + b cos(2x) cos(t)

on randomly sampled points in the space-time domain [0, pi] x [0, pi]. For each
pair of parameters (a, b), it computes the mean squared residual of the
Allen--Cahn equation

    u_t - eps^2 u_xx + (u^3 - u) = 0.

The resulting residual landscape is saved as a CSV file and can be used by the
visualization scripts in this folder.

Output
------
allen_cahn_residual_grid.csv
    A CSV file with columns: a, b, residual.
"""

import numpy as np
import pandas as pd


# Diffusion/interface-width parameter in the Allen--Cahn equation.
eps = 0.01

# Parameter grid for the two-dimensional trial-function family.
# Each point (a, b) defines one candidate approximation u(x, t; a, b).
a_values = np.linspace(-0.1, 0.1, 100)
b_values = np.linspace(-0.1, 0.1, 100)

# Number of random space-time evaluation points used to estimate the residual.
n_points = 500

# Random collocation points in the domain [0, pi] x [0, pi].
x = np.random.uniform(0, np.pi, n_points)
t = np.random.uniform(0, np.pi, n_points)

results = []

for a in a_values:
    for b in b_values:
        # Trial function.
        u = (
            a * np.sin(x) * np.sin(t)
            + b * np.cos(2 * x) * np.cos(t)
        )

        # Time derivative u_t.
        ut = (
            a * np.sin(x) * np.cos(t)
            - b * np.cos(2 * x) * np.sin(t)
        )

        # Second spatial derivative u_xx.
        uxx = (
            -a * np.sin(x) * np.sin(t)
            - 4 * b * np.cos(2 * x) * np.cos(t)
        )

        # Allen--Cahn residual: u_t - eps^2 u_xx + (u^3 - u).
        residual = (
            ut
            - eps**2 * uxx
            + (u**3 - u)
        )

        # Mean squared residual over the sampled collocation points.
        mse = np.mean(residual**2)

        results.append([a, b, mse])

# Store the residual values as a structured table.
df = pd.DataFrame(
    results,
    columns=["a", "b", "residual"]
)

# This file is the input for the residual-landscape and topology scripts.
df.to_csv("allen_cahn_residual_grid.csv", index=False)

print(df.head())
print()
print("Minimum residual:")
print(df["residual"].min())
