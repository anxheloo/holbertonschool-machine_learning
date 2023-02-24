#!/usr/bin/env python3
'''Transpose a matrix using numpy'''


import numpy as np

mat1 = np.array([1, 2, 3, 4, 5, 6])
mat2 = np.array([])
mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])

def np_transpose(matrix):
    '''Function to transpose matrix'''
    result = np.array(matrix)
    r = result.transpose()
    return r


np_transpose(mat1)
mat1
np_transpose(mat2)
mat2
np_transpose(mat3)
mat3
