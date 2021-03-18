#Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

#Examples

#maximun([4,6,2,1,9,63,-134,566]) returns 566
#minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
#maximun([5]) returns 5
#minimun([42, 54, 65, 87, 0]) returns 0

def minimum(arr):
    min_arr = sorted(arr)
    return min_arr[0]

def maximum(arr):
    max_arr = sorted(arr)
    return max_arr[-1]
