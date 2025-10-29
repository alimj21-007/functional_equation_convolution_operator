"""
functional_eq.py

Defines the functional equation Xi(s) = det(I - K_s) built from the
convolution-type operator. Provides utilities for evaluation, symmetry
testing, and plotting along vertical lines in the critical strip.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from operator import fredholm_determinant

def xi_function(s: complex, grid: np.ndarray) -> complex:
    """
    Functional equation defined as Xi(s) = det(I - K_s).

    Parameters
    ----------
    s : complex
        Spectral parameter.
    grid : np.ndarray
        Discretization grid.

    Returns
    -------
    complex
        Value of Xi(s).
    """
    return fredholm_determinant(grid, s)

def xi_on_line(sigma: float, t_values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    """
    Evaluates Xi(s) along a vertical line Re(s) = sigma.

    Parameters
    ----------
    sigma : float
        Real part of s.
    t_values : np.ndarray
        Array of imaginary parts.
    grid : np.ndarray
        Discretization grid.

    Returns
    -------
    np.ndarray
        Array of Xi(sigma + i t).
    """
    values = []
    for t in t_values:
        s = sigma + 1j * t
        values.append(xi_function(s, grid))
    return np.array(values)

def plot_xi_line(sigma: float, t_values: np.ndarray, grid: np.ndarray):
    """
    Plots |Xi(s)| along a vertical line Re(s) = sigma.

    Parameters
    ----------
    sigma : float
        Real part of s.
    t_values : np.ndarray
        Array of imaginary parts.
    grid : np.ndarray
        Discretization grid.
    """
    values = xi_on_line(sigma, t_values, grid)
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, np.abs(values), label=f"|Xi({sigma} + it)|")
    plt.xlabel("t (Imag part)")
    plt.ylabel("|Xi(s)|")
    plt.title(f"Functional Equation along Re(s) = {sigma}")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage
    grid = np.linspace(0.1, 1.0, 20)
    sigma = 0.5
    t_values = np.linspace(0, 20, 100)

    plot_xi_line(sigma, t_values, grid)
