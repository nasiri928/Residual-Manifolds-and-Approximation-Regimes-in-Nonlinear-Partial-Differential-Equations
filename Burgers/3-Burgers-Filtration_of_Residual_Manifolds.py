"""
Visualize a filtration of residual manifolds for Burgers' equation.

This script builds three nested residual sublevel sets:

    M_tau1 subset M_tau2 subset M_tau3,

where tau1, tau2, and tau3 are selected from the 1st, 3rd, and 7th residual
percentiles, respectively.

The figure illustrates how low-residual parameter regions expand as the residual
threshold increases.
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
# Define filtration thresholds
# ---------------------------------------------------------------------

tau1 = np.percentile(df["residual"], 1)
tau2 = np.percentile(df["residual"], 3)
tau3 = np.percentile(df["residual"], 7)

# Nested sublevel sets of the residual function.
M1 = df[df["residual"] <= tau1]
M2 = df[df["residual"] <= tau2]
M3 = df[df["residual"] <= tau3]


# ---------------------------------------------------------------------
# Plot residual-manifold filtration
# ---------------------------------------------------------------------

plt.figure(figsize=(7, 6))

# Largest set is drawn first so smaller sets remain visible.
plt.scatter(
    M3["a"],
    M3["b"],
    s=10,
    alpha=0.35,
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

plt.title(
    "Burgers Filtration of Residual Manifolds"
)

plt.tight_layout()

plt.savefig(
    "burgers_filtration.png",
    dpi=300
)

plt.show()

print("tau1 =", tau1)
print("tau2 =", tau2)
print("tau3 =", tau3)
print("sizes:", len(M1), len(M2), len(M3))
