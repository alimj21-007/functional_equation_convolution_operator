"""
utils.py

General utility functions for logging, timing, normalization, and
data management across the spectral analysis project.

Author: Seyed Ali Mozhgani
Date: 2025-10-29
License: MIT
"""

import time
import numpy as np
import logging

# -----------------------------
# Logging utilities
# -----------------------------

def setup_logger(name: str = "project", level: int = logging.INFO) -> logging.Logger:
    """
    Sets up a logger with a given name and level.

    Parameters
    ----------
    name : str
        Logger name.
    level : int
        Logging level (e.g., logging.INFO, logging.DEBUG).

    Returns
    -------
    logging.Logger
        Configured logger.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

# -----------------------------
# Timing utilities
# -----------------------------

class Timer:
    """
    Context manager for timing code execution.
    Usage:
        with Timer("Computation"):
            # code block
    """
    def __init__(self, name: str = "Block"):
        self.name = name
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"[TIMER] {self.name} took {elapsed:.4f} seconds")

# -----------------------------
# Numerical utilities
# -----------------------------

def normalize_vector(vec: np.ndarray) -> np.ndarray:
    """
    Normalizes a vector to unit L2 norm.

    Parameters
    ----------
    vec : np.ndarray
        Input vector.

    Returns
    -------
    np.ndarray
        Normalized vector.
    """
    norm_val = np.linalg.norm(vec)
    if norm_val == 0:
        return vec
    return vec / norm_val

def relative_error(approx: float, exact: float) -> float:
    """
    Computes relative error between approximation and exact value.

    Parameters
    ----------
    approx : float
        Approximate value.
    exact : float
        Exact value.

    Returns
    -------
    float
        Relative error.
    """
    return np.abs((approx - exact) / exact) if exact != 0 else np.inf

# -----------------------------
# Data I/O utilities
# -----------------------------

def save_array(filename: str, arr: np.ndarray):
    """
    Saves a numpy array to disk.

    Parameters
    ----------
    filename : str
        Path to file.
    arr : np.ndarray
        Array to save.
    """
    np.save(filename, arr)

def load_array(filename: str) -> np.ndarray:
    """
    Loads a numpy array from disk.

    Parameters
    ----------
    filename : str
        Path to file.

    Returns
    -------
    np.ndarray
        Loaded array.
    """
    return np.load(filename, allow_pickle=True)

# -----------------------------
# Example usage
# -----------------------------

if __name__ == "__main__":
    logger = setup_logger("demo", logging.DEBUG)
    logger.info("Logger initialized")

    with Timer("Vector normalization"):
        v = np.array([3, 4])
        v_norm = normalize_vector(v)
        logger.debug(f"Normalized vector: {v_norm}")

    arr = np.linspace(0, 1, 5)
    save_array("test.npy", arr)
    loaded = load_array("test.npy")
    logger.info(f"Loaded array: {loaded}")
