#!/usr/bin/env python3
'''Concatenate 2 Matrices'''


def cat_matrices2D(mat1, mat2, axis = 0):
    '''Function to concatenate 2 Matrices'''
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        result = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        result = [mat1[i] + mat2[i]for i in range(len(mat1))]
    else:
        return None
    return result


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis = 1)
mat4
mat5
mat1[0] = [9, 10]
mat1[1].append(5)
mat1
mat4
mat5
