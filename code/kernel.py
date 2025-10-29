"""
kernel.py

Defines the convolution-type kernel K_s(x, y) used in the integral operator
associated with the functional equation. Includes utilities for discretization
and symmetry testing.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np

def kernel(x: float, y: float, s: complex) -> complex:
    """
    Convolution-type kernel function K_s(x, y).

    Parameters
    ----------
    x : float
        First variable.
    y : float
        Second variable.
    s : complex
        Spectral parameter.

    Returns
    -------
    complex
        Value of the kernel K_s(x, y).
    """
    # Example kernel: Gaussian decay with multiplicative s-dependence
    return np.exp(-np.pi * (x - y)**2) * (1 + (x * y)**(s - 1))

def kernel_matrix(grid: np.ndarray, s: complex) -> np.ndarray:
    """
    Constructs the discretized kernel matrix K_s over a given grid.

    Parameters
    ----------
    grid : np.ndarray
        1D array of evaluation points.
    s : complex
        Spectral parameter.

    Returns
    -------
    np.ndarray
        2D kernel matrix.
    """
    n = len(grid)
    K = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            K[i, j] = kernel(grid[i], grid[j], s)
    return K

def is_symmetric(K: np.ndarray, tol: float = 1e-12) -> bool:
    """
    Checks whether the kernel matrix is Hermitian (symmetric).

    Parameters
    ----------
    K : np.ndarray
        Kernel matrix.
    tol : float
        Tolerance for symmetry check.

    Returns
    -------
    bool
        True if symmetric within tolerance.
    """
    return np.allclose(K, K.T.conj(), atol=tol)

if __name__ == "__main__":
    # Example usage
    grid = np.linspace(0.1, 1.0, 5)
    s = 0.5 + 14j
    K = kernel_matrix(grid, s)
    print("Kernel matrix:\n", K)
    print("Is symmetric?", is_symmetric(K))
