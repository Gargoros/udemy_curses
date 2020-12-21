# Реализуйте одну классическую и достаточно простую игру: "угадай число"
# Компьютер загадывает число от 1 до 50 и даёт 6 попыток пользователю,
# чтобы тот смог угадать загаданное число.
# Когда пользователь вводит число, компьютер проверяет угадано ли число
# и если не угадано, то сообщает пользователю меньше ли или больше загаданое число.
# Если пользователь угадал - сообщает о том, что число отгадано.
# Подсказка:
# для "загадывания" числа используйте модуль random: импортируйте его и для генерации
# (загадывания) числа вызовите метод random.randint(1, 50).

import random

ai_num = random.randint(1, 50)
print(ai_num)
game_raund = 6
print("Guess a number from 1 to 50 ")
print("Try to guess a number ")

while game_raund > 0:
    player_num = int(input("\n Enter the hidden number "))
    if player_num > ai_num:
        print("The hidden number is too less")
        game_raund -= 1
    elif player_num < ai_num:
        print("The hidden number is too high")
        game_raund -= 1
    else:
        print(f"\nYou win!")
        break
    if game_raund == 0 and player_num != ai_num:
        print(f"Your tries is over! The hidden number is {ai_num}")
        break
print("Game Over")
