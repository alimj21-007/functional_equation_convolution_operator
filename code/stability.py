"""
stability.py

Provides tools for testing numerical stability of discretized operators
and Fredholm determinants. Includes condition number analysis, sensitivity
tests, and grid refinement comparisons.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np
from numpy.linalg import cond, norm
from kernel import kernel_matrix
from determinant import fredholm_determinant

def condition_number(grid: np.ndarray, s: complex) -> float:
    """
    Computes the condition number of the kernel matrix K_s.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.

    Returns
    -------
    float
        Condition number of K_s.
    """
    K = kernel_matrix(grid, s)
    return cond(K)

def sensitivity_test(grid: np.ndarray, s: complex, epsilon: float = 1e-8) -> float:
    """
    Tests sensitivity of the Fredholm determinant to small perturbations.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.
    epsilon : float
        Perturbation magnitude.

    Returns
    -------
    float
        Relative change in determinant under perturbation.
    """
    det_val = fredholm_determinant(grid, s)

    # Add small random perturbation to kernel
    K = kernel_matrix(grid, s)
    perturbation = epsilon * np.random.randn(*K.shape)
    perturbed_det = np.linalg.det(np.eye(len(grid)) - (K + perturbation))

    return np.abs((perturbed_det - det_val) / det_val)

def grid_refinement_stability(a: float, b: float, s: complex, n_values: list) -> dict:
    """
    Compares determinant values across different grid refinements.

    Parameters
    ----------
    a : float
        Left endpoint of interval.
    b : float
        Right endpoint of interval.
    s : complex
        Spectral parameter.
    n_values : list
        List of grid sizes.

    Returns
    -------
    dict
        Mapping from grid size to determinant value.
    """
    results = {}
    for n in n_values:
        grid = np.linspace(a, b, n)
        results[n] = fredholm_determinant(grid, s)
    return results

if __name__ == "__main__":
    # Example usage
    a, b = 0.1, 1.0
    s = 0.5 + 14j
    grid = np.linspace(a, b, 20)

    cond_num = condition_number(grid, s)
    sens = sensitivity_test(grid, s)
    refinement = grid_refinement_stability(a, b, s, [10, 20, 40, 80])

    print("Condition number of K_s:", cond_num)
    print("Relative sensitivity of determinant:", sens)
    print("Grid refinement results:", refinement)
