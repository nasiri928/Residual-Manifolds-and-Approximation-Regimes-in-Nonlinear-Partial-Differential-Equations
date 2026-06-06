# Residual Manifolds and Approximation Regimes in Nonlinear Partial Differential Equations

This repository contains the source code, datasets, and visualization scripts accompanying the manuscript:

**Residual Manifolds and Approximation Regimes in Nonlinear Partial Differential Equations**

## Overview

This repository presents a computational framework for studying nonlinear partial differential equations (PDEs) through the concepts of **Residual Manifolds** and **Approximation Regimes**.

The central idea is to explore parameterized trial-function spaces by evaluating PDE residuals over large parameter grids. The resulting residual landscapes reveal geometric and topological structures associated with high-quality approximate solutions.

Three representative nonlinear PDEs are investigated:

* Allen–Cahn Equation
* Burgers' Equation
* Fisher–KPP Equation

For each equation, the repository provides scripts for residual computation, approximation regime extraction, manifold filtration, and topological stability analysis.

---

## Repository Structure

```text
allen_cahn/
    Allen-Cahn-Data.py
    1-Allen-Cahn-Residual Landscape.py
    2-Allen-Cahn-Approximation Regime.py
    3-Allen-Cahn-Filtration of Residual Manifolds.py
    4-Allen-Cahn-Connected Components vs Threshold.py

Burgers/
    Burgers-Data.py
    1-Burgers-Residual Landscape.py
    2-Burgers-Approximation Regime.py
    3-Burgers-Filtration of Residual Manifolds.py
    4-Burgers-Connected Components vs Threshold.py

Fisher–KPP/
    Fisher–KPP-Data.py
    1-Fisher–KPP-Residual Landscape.py
    2-Fisher–KPP-Approximation Regime.py
    3-Fisher–KPP-Filtration of Residual Manifolds.py
    4-Fisher–KPP-Connected Components vs Threshold.py
```

---

## Methodology

For each PDE, the workflow consists of four stages:

1. **Residual Dataset Generation**

   * Construction of parameterized trial functions.
   * Numerical evaluation of PDE residuals.
   * Creation of residual datasets over parameter grids.

2. **Residual Landscape Analysis**

   * Visualization of residual values as surfaces over parameter space.
   * Identification of low-residual regions.

3. **Approximation Regimes**

   * Extraction of regions satisfying

[
M_{\tau}={\theta:R(\theta)\leq\tau}.
]

* Characterization of high-quality approximate solutions.

4. **Topological Analysis**

   * Filtration of approximation regimes.
   * Connected-component analysis using DBSCAN.
   * Investigation of regime stability under varying residual thresholds.

---

## Generated Figures

The scripts reproduce the figures presented in the manuscript, including:

* Residual landscapes
* Approximation regimes
* Filtration of residual manifolds
* Connected-components-versus-threshold diagrams

These visualizations provide geometric evidence for the organization of approximate solution spaces in nonlinear PDEs.

---

## Requirements

Required Python packages:

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## Authors

### Mohammad Nasiri

Independent Researcher

Ph.D. in Mathematics

Department of Mathematics

Iran University of Science and Technology (IUST)

Tehran, Iran

### Mehdi Nadjafikhah

Professor of Mathematics

Department of Mathematics

Iran University of Science and Technology (IUST)

Tehran, Iran

---

## Affiliation

Department of Mathematics

Iran University of Science and Technology (IUST)

Tehran, Iran

---

## Citation

If you use this repository in your research, please cite:

Nasiri, M., & Nadjafikhah, M.

*Residual Manifolds and Approximation Regimes in Nonlinear Partial Differential Equations.*

---

## License

This repository is provided for academic and research purposes. Please cite the corresponding article when using the code, figures, or ideas contained in this repository.
