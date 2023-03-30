#!/usr/bin/env python3
"""afd"""


import numpy as np
import matplotlib.pyplot as plt

def convolve_grayscale_same(images, kernel):
    """adfsads"""
    m, height, width = images.shape
    kh, kw = kernel.shape
    if (kh % 2) == 1 and (kw % 2) == 1:
        ph = (kh - 1) // 2
        pw = kw // 2
    images = np.pad(images, ((0,0), (ph,ph),(pw,pw)), 'constant', constant_values=0)
    convoluted = np.zeros((m, height, width))
    for h in range(height):
        for w in range(width):
            output = np.sum(images[:, h: h+kh, w: w+kw ] * kernel, axis = 1).sum(axis=1)
            convoluted[:, h, w] = output
    return convoluted
