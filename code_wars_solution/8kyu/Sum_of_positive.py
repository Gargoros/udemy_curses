def positive_sum(arr):
    positive_num = [num if num > 0 else 0 for num in arr]
    return sum(positive_num)
