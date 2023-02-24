#!/usr/bin/env python3
'''Math Operations'''


def np_elementwise(mat1, mat2):
    '''Math operations function numpy'''
    result = np.add(mat1, mat2), np.subtract(mat1, mat2), np.multiply(mat1, mat2), np.divide(mat1, mat2)
    return result
