#!/usr/bin/env python3
'''Concatenate 2 Strings'''


def cat_arrays(arr1,arr2):
    '''Add two Strings Together'''
    newList = []
    newList.extend(arr1)
    newList.extend(arr2)
    return newList


arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8]
cat_arrays(arr1, arr2)
