#!/usr/bin/env python3
'''Add 2 arrays'''


def add_arrays(arr1, arr2):
    '''Function'''
    result = []
    if len(arr1) != len(arr2):
        return None
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
add_arrays(arr1, arr2)
add_arrays(arr1, [1, 2, 3])
