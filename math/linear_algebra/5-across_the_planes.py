#!/usr/bin/env python3
'''Add two Matrices'''


def add_matrices2D(mat1, mat2):
    '''Add two Matrices Function'''
    result = []
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    for i in range(len(mat1)):
        a = []
        for j in range(len(mat1[0])):
            a.append(mat1[i][j] + mat2[i][j])
        result.append(a)
    return result


mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
add_matrices2D(mat1, mat2)
add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]])
