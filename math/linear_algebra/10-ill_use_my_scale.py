#!/usr/bin/env python3
'''Function to calculate the shape of matrix'''


def np_shape(matrix):
    '''Function to calculate the shape of matrix'''
    tuple = np.array(matrix)
    return tuple.shape


mat1 = [1, 2, 3, 4, 5, 6]
mat2 = []
mat3 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]
np_shape(mat1)
np_shape(mat2)
np_shape(mat3)
