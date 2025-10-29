"""
discretize.py

Provides utilities for discretizing the domain of integral operators.
Includes uniform and adaptive grids, as well as quadrature weights
for numerical integration.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np

def uniform_grid(a: float, b: float, n: int) -> np.ndarray:
    """
    Creates a uniform discretization grid.

    Parameters
    ----------
    a : float
        Left endpoint of interval.
    b : float
        Right endpoint of interval.
    n : int
        Number of grid points.

    Returns
    -------
    np.ndarray
        Uniform grid points in [a, b].
    """
    return np.linspace(a, b, n)

def chebyshev_grid(a: float, b: float, n: int) -> np.ndarray:
    """
    Creates a Chebyshev-distributed grid (denser near endpoints).

    Parameters
    ----------
    a : float
        Left endpoint of interval.
    b : float
        Right endpoint of interval.
    n : int
        Number of grid points.

    Returns
    -------
    np.ndarray
        Chebyshev grid points in [a, b].
    """
    k = np.arange(1, n + 1)
    x = np.cos((2 * k - 1) / (2 * n) * np.pi)  # Chebyshev nodes in [-1,1]
    return 0.5 * (a + b) + 0.5 * (b - a) * x

def trapezoidal_weights(a: float, b: float, n: int) -> np.ndarray:
    """
    Computes trapezoidal rule weights for integration.

    Parameters
    ----------
    a : float
        Left endpoint of interval.
    b : float
        Right endpoint of interval.
    n : int
        Number of grid points.

    Returns
    -------
    np.ndarray
        Weights for trapezoidal integration.
    """
    h = (b - a) / (n - 1)
    w = np.ones(n) * h
    w[0] *= 0.5
    w[-1] *= 0.5
    return w

def integrate(f, grid: np.ndarray, weights: np.ndarray) -> float:
    """
    Approximates integral of f over grid using given weights.

    Parameters
    ----------
    f : callable
        Function to integrate.
    grid : np.ndarray
        Grid points.
    weights : np.ndarray
        Quadrature weights.

    Returns
    -------
    float
        Approximation of integral.
    """
    values = f(grid)
    return np.sum(values * weights)

if __name__ == "__main__":
    # Example usage
    a, b, n = 0.0, 1.0, 10
    grid = uniform_grid(a, b, n)
    weights = trapezoidal_weights(a, b, n)

    f = lambda x: np.exp(-x**2)
    approx = integrate(f, grid, weights)

    print("Grid:", grid)
    print("Trapezoidal weights:", weights)
    print("Approx integral of exp(-x^2) over [0,1]:", approx)
