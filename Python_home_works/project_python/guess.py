#Эта игра по угадыванию числа

import random

def get_guess():
    print("Как тебя зовут? \n")
    my_name = input()
    print(f"Привет {my_name}! Эта игра в угадай число. \nДавай сыграем!\n ")
    print("В этой игре очень простые правила: \nЯ загадываю целое число от 1 до 20,\nа ты должен угадать его за 6 попыток! \n")
    print(f"{my_name} Начнем!\n ")
    guesses_taken = 0
    ai_num = random.randint(1, 20)
    print(ai_num)

    while guesses_taken != 6:

        player_guess = input("Введи целое цисло от 1 до 20: \n")
        try:
            player_guess = int(player_guess)
            if player_guess not in range(1, 21):
                print("Только целые числа от 1 до 20! \n")
            else:
                print()
                if player_guess > ai_num:
                    guesses_taken += 1
                    print(f"Твое число {player_guess} слишком большое! \nПопробуй еще раз!\n ")
                elif player_guess < ai_num:
                    guesses_taken += 1
                    print(f"Твое число {player_guess} слишком маленькое! \nПопробуй еще раз!\n ")
                else:
                    guesses_taken += 1
                    print(f"Отлично {my_name} ты угадал! \nТы справился за {guesses_taken} попыток.\n ")
                    break
        except ValueError:
            print("Это не похоже на целое число! \nПопробуй еще раз! \n")
        if guesses_taken == 6:
            print(f"Увы {my_name} ты израсходовал все 6 попыток! \nЯ загадал чило {ai_num}")

get_guess()

    