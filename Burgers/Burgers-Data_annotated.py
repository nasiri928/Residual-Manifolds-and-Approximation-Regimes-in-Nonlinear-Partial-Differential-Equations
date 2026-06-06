"""
Generate a residual grid for a two-parameter trial family applied to Burgers' equation.

This script evaluates the mean squared residual of the viscous Burgers equation

    u_t + u u_x - nu u_xx = 0

for a simple two-parameter trigonometric trial function

    u(x, t; a, b) =
        a sin(pi x) sin(pi t) + b cos(pi x) cos(pi t).

The output is a CSV file, `burgers_residual_grid.csv`, containing one row for
each pair (a, b) in the parameter grid and the corresponding residual value.

This file is intended to support the residual-manifold and approximation-regime
experiments used in the RDSF framework.
"""

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------
# Model and sampling parameters
# ---------------------------------------------------------------------

# Viscosity coefficient in the Burgers equation.
nu = 0.1

# Parameter grid for the trial function coefficients.
# Each point (a, b) defines one candidate function u(x, t; a, b).
a_values = np.linspace(-0.2, 0.2, 140)
b_values = np.linspace(-0.2, 0.2, 140)

# Number of random space-time points used to estimate the residual.
n_points = 700

# Fixing the random seed makes the experiment reproducible.
np.random.seed(42)

# Random evaluation points in the space-time domain [0, 1] x [0, 1].
x = np.random.uniform(0, 1, n_points)
t = np.random.uniform(0, 1, n_points)


# ---------------------------------------------------------------------
# Residual evaluation over the parameter grid
# ---------------------------------------------------------------------

results = []

for a in a_values:
    for b in b_values:

        # Trial function u(x, t; a, b).
        u = (
            a * np.sin(np.pi * x) * np.sin(np.pi * t)
            +
            b * np.cos(np.pi * x) * np.cos(np.pi * t)
        )

        # First derivative with respect to x.
        ux = (
            a * np.pi * np.cos(np.pi * x) * np.sin(np.pi * t)
            -
            b * np.pi * np.sin(np.pi * x) * np.cos(np.pi * t)
        )

        # First derivative with respect to t.
        ut = (
            a * np.pi * np.sin(np.pi * x) * np.cos(np.pi * t)
            -
            b * np.pi * np.cos(np.pi * x) * np.sin(np.pi * t)
        )

        # Second derivative with respect to x.
        uxx = (
            -a * np.pi**2 * np.sin(np.pi * x) * np.sin(np.pi * t)
            -
            b * np.pi**2 * np.cos(np.pi * x) * np.cos(np.pi * t)
        )

        # Pointwise Burgers residual:
        #     R = u_t + u u_x - nu u_xx.
        residual = (
            ut
            +
            u * ux
            -
            nu * uxx
        )

        # Mean squared residual over the sampled space-time points.
        mse = np.mean(residual**2)

        results.append([a, b, mse])


# ---------------------------------------------------------------------
# Save results
# ---------------------------------------------------------------------

df = pd.DataFrame(
    results,
    columns=["a", "b", "residual"]
)

df.to_csv(
    "burgers_residual_grid.csv",
    index=False
)

print("Minimum residual:", df["residual"].min())
print("Residual percentiles:")
print(
    df["residual"].quantile(
        [0.01, 0.02, 0.05, 0.10, 0.20]
    )
)
