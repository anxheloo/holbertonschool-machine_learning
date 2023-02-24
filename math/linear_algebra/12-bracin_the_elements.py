#!/usr/bin/env python3

import numpy as np

mat1 = np.array([[11, 22, 33], [44, 55, 66]])
mat2 = np.array([[1, 2, 3], [4, 5, 6]])

def add(mat1,mat2):
    a = np.array(mat1)
    b = np.array(mat2)
    
    result = np.add(a,b)
    return result


def sub(mat1,mat2):
    a = np.array(mat1)
    b = np.array(mat2)
    
    result = np.subtract(a,b)
    return result


def mul(mat1,mat2):
    a = np.array(mat1)
    b = np.array(mat2)

    result = np.multiply(a,b)
    return result


def div(mat1,mat2):
    a = np.array(mat1)
    b = np.array(mat2)
    
    result = np.divide(a,b)
    return result


print(add(mat1,mat2))
print(sub(mat1,mat2))
print(mul(mat1,mat2))
print(div(mat1,mat2))
