#На вход подаются два списка чисел длины N.
#Задача: взять из первого списка все нечётные числа,
#из второго все четные и объединить их в новом списке 
#с названием joined_list.
#Примечание: можно сделать двумя циклами for, можно одним,
#можно с помощью list comprehensions.


n1 = int(input()) +1
n2 = int(input()) +1
first_lst = list(range(n1))
second_lst = list(range(n2))
joined_list = []

for num_odd in first_lst:
    if num_odd % 2 != 0:
        joined_list.append(num_odd)
for num_even in second_lst:
    if num_even % 2 == 0:
        joined_list.append(num_even)
print(joined_list)


odd_list = [odd for odd in first_lst if odd % 2 != 0]
even_list = [even for even in second_lst if even % 2 == 0]
joined_list = odd_list + even_list
print(joined_list)