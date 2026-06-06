"""
Estimate the number of connected components in Burgers approximation regimes.

For a sequence of residual thresholds tau, this script constructs the sublevel
set

    M_tau = {(a, b) : residual(a, b) <= tau}

and estimates its connected components using DBSCAN clustering.

The resulting curve provides a simple stability diagnostic: persistent component
counts across thresholds suggest stable geometric structure in the approximation
regime.
"""

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Load residual grid
# ---------------------------------------------------------------------

# The CSV file must be generated first by running `Burgers-Data.py`.
df = pd.read_csv("burgers_residual_grid.csv")


# ---------------------------------------------------------------------
# Threshold sweep
# ---------------------------------------------------------------------

# Evaluate thresholds from the 1st to the 30th residual percentile.
taus = np.percentile(
    df["residual"],
    np.arange(1, 31)
)

components = []

for tau in taus:

    # Residual sublevel set at the current threshold.
    M = df[
        df["residual"] <= tau
    ]

    # Very small sets are not reliable for clustering.
    if len(M) < 5:
        components.append(0)
        continue

    # Use only the parameter coordinates for connectivity estimation.
    X = M[["a", "b"]].values

    # DBSCAN approximates connected components in the parameter plane.
    # The eps value should be interpreted relative to the grid spacing.
    labels = DBSCAN(
        eps=0.02,
        min_samples=5
    ).fit_predict(X)

    # Count all non-noise clusters.
    ncomp = len(
        set(labels)
        -
        {-1}
    )

    components.append(ncomp)


# ---------------------------------------------------------------------
# Plot stability curve
# ---------------------------------------------------------------------

plt.figure(figsize=(7, 5))

plt.plot(
    taus,
    components,
    marker="o"
)

plt.xlabel(r"$	au$")
plt.ylabel("Connected Components")

plt.title(
    "Burgers Stability of Approximation Regimes"
)

plt.tight_layout()

plt.savefig(
    "burgers_stability.png",
    dpi=300
)

plt.show()

for tau, comp in zip(taus, components):
    print(f"tau={tau:.3e}, components={comp}")
