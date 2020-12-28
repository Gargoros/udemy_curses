# ДЗ: Мини-судоку
# Напишите функцию any_duplicates, которая принимает двумерный массив размера 3х3 (9 элементов).
# Двумерный массив заполнен числами от 1 до 9.

# Функция должна вернуть False, если в массиве все числа от 1 до 9 встречаются ровно один раз.
# В противном случае True.

#Примеры вызовов.

# any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]]) ➞ False
# any_duplicates([[8, 9, 2], [5, 6, 1], [3, 7, 4]]) ➞ False
# any_duplicates([[1, 1, 3], [6, 5, 4], [8, 7, 9]]) ➞ True # 1 дублируется
# any_duplicates([[1, 2, 3], [3, 4, 5], [9, 8, 7]]) ➞ True # 3 дублируется#



square = [[1, 2, 3], [3, 4, 5], [9, 8, 7]]

def any_duplicates(square):
    '''
    DOCSTRING: The function checks for duplicates in the array
    INPUT:     The input is a three-dimensional array
    OUTPUT:    Boolean values ​​are given for output
    '''
    all_num = {num for lst in square for num in lst}
    if len(all_num) != 9:
        return True
    else:
        return False



