# Запросить у пользователя ввод числа.
# Построить цикл от 0 до введённого числа (включительно)
# и для чётных чисел вывести то, что они чётные,
# а для нечётных, что они нечётные. Пример вывода:

#0 is EVEN
#1 is ODD
#2 is EVEN

#и так далее...

user_input = int(input("Please enter an integer "))
for num in range(user_input + 1):
    if num % 2 == 0:
        print(f"{num} is EVEN number")
    else:
        print(f"{num} is ODD number")
