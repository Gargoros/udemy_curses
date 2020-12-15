#Вы получили ввод данных от пользователя
#Постройте цикл от 0 до введенного числа (включительно) и посчитать
#сумму всех чисел, делимых без остатка на 3 или 5.
#Выведите на консоль это число.
#Примечание: задача решается как прямым for, так и с помощью list comprehension
#(просуммировать числа "профильтрованного" списка можно, передав список в функцию sum(arg_list)). 

limit = int(input("Please enter an integer "))
arg_list = []
for num in range(limit + 1):
    if num % 3 == 0:
        arg_list.append(num)
    elif num % 5 == 0:
        arg_list.append(num)
    
print(sum(arg_list))


arg_list = [num for num in range(limit + 1) if num % 3 == 0 or num % 5 == 0]
print(sum(arg_list))
