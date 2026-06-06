"""
Visualize the residual landscape for the Burgers equation experiment.

This script reads `burgers_residual_grid.csv`, reshapes the residual values into
a two-dimensional parameter grid, and plots the surface

    (a, b) -> residual(a, b).

The resulting 3D surface helps identify low-residual valleys and candidate
approximation regimes in the parameter space.
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
# Convert tabular data into a surface grid
# ---------------------------------------------------------------------

# Rows correspond to a-values, columns correspond to b-values,
# and entries contain the residual value.
pivot = df.pivot(
    index="a",
    columns="b",
    values="residual"
)

# Create coordinate matrices for the 3D surface plot.
A, B = np.meshgrid(
    pivot.columns.values,
    pivot.index.values
)

Z = pivot.values


# ---------------------------------------------------------------------
# Plot residual landscape
# ---------------------------------------------------------------------

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(
    111,
    projection="3d"
)

ax.plot_surface(
    A,
    B,
    Z,
    cmap="viridis",
    linewidth=0,
    antialiased=True
)

ax.set_xlabel(r"$b$")
ax.set_ylabel(r"$a$")
ax.set_zlabel("Residual")

# Set a fixed view angle for reproducible figure appearance.
ax.view_init(30, 230)

plt.tight_layout()

plt.savefig(
    "burgers_residual_landscape.png",
    dpi=300
)

plt.show()
