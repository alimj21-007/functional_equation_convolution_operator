"""
plots.py

Provides visualization utilities for spectral analysis and functional
equation experiments. Includes plotting of eigenvalues, determinant
magnitude, and Xi(s) along vertical lines.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from operator import eigenvalues
from determinant import fredholm_determinant
from functional_eq import xi_on_line

def plot_eigenvalues(grid: np.ndarray, s: complex):
    """
    Plots eigenvalues of the discretized operator K_s in the complex plane.

    Parameters
    ----------
    grid : np.ndarray
        Discretization grid.
    s : complex
        Spectral parameter.
    """
    vals = eigenvalues(grid, s)
    plt.figure(figsize=(6, 6))
    plt.scatter(np.real(vals), np.imag(vals), c="blue", marker="o")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.xlabel("Re(λ)")
    plt.ylabel("Im(λ)")
    plt.title(f"Eigenvalues of K_s at s={s}")
    plt.grid(True)
    plt.show()

def plot_determinant_vs_t(sigma: float, t_values: np.ndarray, grid: np.ndarray):
    """
    Plots |det(I - K_s)| along a vertical line Re(s) = sigma.

    Parameters
    ----------
    sigma : float
        Real part of s.
    t_values : np.ndarray
        Array of imaginary parts.
    grid : np.ndarray
        Discretization grid.
    """
    det_vals = [np.abs(fredholm_determinant(grid, sigma + 1j*t)) for t in t_values]
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, det_vals, label=f"|det(I - K_s)|, Re(s)={sigma}")
    plt.xlabel("t (Imag part)")
    plt.ylabel("|det(I - K_s)|")
    plt.title("Fredholm determinant along vertical line")
    plt.legend()
    plt.grid(True)
    plt.show()

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

    plot_eigenvalues(grid, sigma + 14j)
    plot_determinant_vs_t(sigma, t_values, grid)
    plot_xi_line(sigma, t_values, grid)
