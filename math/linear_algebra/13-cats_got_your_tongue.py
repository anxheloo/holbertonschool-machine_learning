#!/usr/bin/env python3
'''Concatenate numpy'''
import numpy as np


def np_cat(mat1,mat2, axis = 0):
    '''done done done'''
    a = np.array(mat1)
    b = np.array(mat2)
    if axis == 0:
        c = np.concatenate((a, b), axis=0)
    else:
        c = np.concatenate((a, b), axis=1)
    return c 

