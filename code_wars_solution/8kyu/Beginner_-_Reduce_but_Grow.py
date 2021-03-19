# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    multy = 1
    for num in arr:
        multy *= num
    return multy

    
import math

def grow1(arr):
    return math.prod(arr)