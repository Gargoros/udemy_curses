#Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

#Return your answer as a number.

def sum_mix(arr):
    arr = [int(num) for num in arr]
    return sum(arr)

