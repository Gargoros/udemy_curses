import random
number_1 = random.randint(1, 10)
number_2 = random.randint(1, 10)
print("Сколько будет: " + str(number_1) + " + " + str(number_2) + " ? ")
answer = input()
if answer == number_1 + number_2:
    print("Верно!")
else:
    print("Нет! Правильный ответ - " + str(number_1 + number_2))

number_1 = random.randint(1, 10)
number_2 = random.randint(1, 10)
print("Сколько будет: " + str(number_1) + " + " + str(number_2) + " ? ")
answer = input()
if int(answer) == number_1 + number_2:
    print("Верно!")
else:
    print("Нет! Правильный ответ - " + str(number_1 + number_2))