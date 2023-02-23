#!/usr/bin/env python3
'''Flip me over'''


def matrix_transpose(x):
    '''ca bone lale'''
    res = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
    return res


mat1 = [[1, 2], [3, 4]]
matrix_transpose(mat1)
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
matrix_transpose(mat2)
