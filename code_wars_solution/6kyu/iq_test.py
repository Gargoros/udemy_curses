

def iq_test(numbers):
    all_numbs = [int(num) for num in numbers.split(" ")]
    even_list = [num for num in all_numbs if num % 2 == 0]
    odd_list  = [num for num in all_numbs if num % 2 != 0]
    if len(even_list) > len(odd_list):
        return all_numbs.index(odd_list[0]) + 1
    else:
        return all_numbs.index(even_list[0]) + 1

\
    