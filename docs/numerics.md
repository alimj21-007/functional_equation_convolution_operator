# Numerical Experiments and Computational Setup

This document outlines the numerical framework used in Paper 2 to compute and analyze the Fredholm determinant \(\Xi(s) = \det(I - K_s)\) and its relation to the Riemann zeta function \(\zeta(s)\).

## 1. Discretization Strategy

We discretize the integral operator \(K_s\) on a uniform grid:
- **Domain:** \([0.1, 1.0]\)
- **Grid size:** typically 40–100 points
- **Quadrature:** midpoint rule (uniform weights), with optional trapezoidal correction

The kernel matrix \(K_s[i,j] = K_s(x_i, x_j)\) is constructed using the function:
\[
K_s(x, y) = \exp(-s(x - y)^2)
\]
or other variants depending on the experiment.

## 2. Spectral Parameter Handling

We evaluate \(s = \sigma + it\) along the critical line:
- **Fixed real part:** \(\sigma = 0.5\)
- **Imaginary part:** \(t \in [0, 20]\), sampled at 100–200 points

This allows us to probe the behavior of \(\Xi(s)\) in direct comparison with \(\zeta(s)\) on the critical line.

## 3. Fredholm Determinant Computation

We compute \(\Xi(s) = \det(I - K_s)\) using:
- **Direct determinant:** via `numpy.linalg.det`
- **Log-determinant (optional):** via `numpy.linalg.slogdet` for numerical stability
- **Normalization:** \(|\Xi(s)|^{1/n}\) for grid-size invariance

All computations are performed in complex arithmetic with double precision.

## 4. Spectral Radius and Eigenvalue Analysis

We compute the eigenvalues \(\lambda_i\) of \(K_s\) using `numpy.linalg.eigvals`, and extract:
- **Spectral radius:** \(\rho(K_s) = \max |\lambda_i|\)
- **Dominant eigenvalue:** \(\max \Re(\lambda_i)\)

These quantities are plotted against \(t\) to assess operator growth and spectral behavior.

## 5. Symmetry Tests and Functional Equation

To test the symmetry \(\Xi(s) = \Xi(1 - s)\), we compute:
- \(|\Xi(0.5 + it)|\) and \(|\Xi(0.5 - it)|\)
- Absolute difference: \(|\Xi(0.5 + it)| - |\Xi(0.5 - it)|\)

These are visualized to assess how well the numerical determinant respects the functional equation.

## 6. Output Formats and Reproducibility

All outputs are saved in the following formats:
- **PDF plots:** for visual comparison (e.g., `determinate_vs_zeta.pdf`, `spectral_radius_plot.pdf`)
- **CSV tables:** for numerical inspection and external analysis
- **Markdown summaries:** for documentation and publication

Scripts are modular and documented. All figures are reproducible with a single execution of the main script.

---

**Note:** All numerical experiments are designed to be portable, with support for Persian-language documentation and mobile-friendly outputs for outreach.
