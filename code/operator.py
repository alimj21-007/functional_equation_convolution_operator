"""
operator.py

Defines integral operators built from the convolution-type kernel K_s(x, y).
Includes utilities for applying the operator to vectors, computing eigenvalues,
and approximating Fredholm determinants.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np
from numpy.linalg import eigvals, det
from kernel import kernel_matrix

def apply_operator(vec: np.ndarray, grid: np.ndarray, s: complex) -> np.ndarray:
    """
    Applies the discretized operator K_s to a vector.

    Parameters
    ----------
    vec : np.ndarray
        Input vector (function values on grid).
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    np.ndarray
        Result of applying operator.
    """
    K = kernel_matrix(grid, s)
    return K @ vec

def eigenvalues(grid: np.ndarray, s: complex) -> np.ndarray:
    """
    Computes eigenvalues of the discretized operator K_s.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    np.ndarray
        Eigenvalues of K_s.
    """
    K = kernel_matrix(grid, s)
    return eigvals(K)

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

if __name__ == "__main__":
    # Example usage
    grid = np.linspace(0.1, 1.0, 10)
    s = 0.5 + 14j

    vec = np.ones(len(grid))
    applied = apply_operator(vec, grid, s)
    vals = eigenvalues(grid, s)
    det_val = fredholm_determinant(grid, s)

    print("Applied operator result:", applied)
    print("Eigenvalues:", vals)
    print("Fredholm determinant det(I - K_s):", det_val)
