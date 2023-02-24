#!/usr/bin/env python3
'''Concatenate numpy'''
import numpy as np


def np_cat(mat1,mat2, axis = 0):
    '''done done done'''
    a = np.array(mat1)
    b = np.array(mat2)
    c = np.concatenate((a, b), axis)
    return c 

