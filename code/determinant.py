"""
determinant.py

Provides utilities for computing determinants of discretized operators,
including Fredholm determinants det(I - K_s). Supports direct computation
via numpy.linalg.det and optional log-determinant stabilization.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np
from numpy.linalg import det, slogdet
from kernel import kernel_matrix

def fredholm_determinant(grid: np.ndarray, s: complex) -> complex:
    """
    Approximates the Fredholm determinant det(I - K_s).

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    complex
        Approximation of det(I - K_s).
    """
    K = kernel_matrix(grid, s)
    I = np.eye(len(grid), dtype=complex)
    return det(I - K)

def log_fredholm_determinant(grid: np.ndarray, s: complex) -> complex:
    """
    Computes the log of the Fredholm determinant using slogdet for stability.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    complex
        Logarithm of det(I - K_s).
    """
    K = kernel_matrix(grid, s)
    I = np.eye(len(grid), dtype=complex)
    sign, logdet = slogdet(I - K)
    return logdet + np.log(sign)

def normalized_determinant(grid: np.ndarray, s: complex) -> float:
    """
    Returns |det(I - K_s)| normalized by matrix size.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    float
        Normalized absolute determinant.
    """
    det_val = fredholm_determinant(grid, s)
    return np.abs(det_val) ** (1.0 / len(grid))

if __name__ == "__main__":
    # Example usage
    grid = np.linspace(0.1, 1.0, 10)
    s = 0.5 + 14j

    det_val = fredholm_determinant(grid, s)
    log_det_val = log_fredholm_determinant(grid, s)
    norm_det_val = normalized_determinant(grid, s)

    print("Fredholm determinant det(I - K_s):", det_val)
    print("Log Fredholm determinant:", log_det_val)
    print("Normalized determinant:", norm_det_val)
