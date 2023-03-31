#!/usr/bin/env python3
"""1-Correlation"""


import numpy as np


def correlation(C):
    """
    Calculates a correlation matrix
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if (len(C.shape) != 2) or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    # here's how you can calculate the square root of the diagonal matrix
    D = np.sqrt(np.diag(C))
    outer_matrix = np.outer(D, D)
    correlation = C / outer_matrix
    return correlation
