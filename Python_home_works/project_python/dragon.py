#Эта игра про пещеры с драконами в одной из них сокровище, а в другой тебя съедят
#тебе нужно сделать правильный выбор и надеятся на удачу
import random
import time

dragon = random.randint(1, 2)

def introduction():
    print("\nВы находитесь в землях, заселенных драконами.\n")
    print("\nПеред собой вы видите две пещеры.\n")
    print("\nВ одной из них - дружелюбный дракон,\nкоторый готов поделиться с вами своими сокровищами.\n")
    print("\nВо второй - 'жадный и голодный дракон, который мигом вас съест.\n")
    print("\nВ какую пещеру вы войдете?  (нажмите клавишу 1 или 2)\n")


def player_select():
    while True:
        player_select = input()
        try:
            player_select = int(player_select)
            if player_select not in range(1, 3):
                print("\nПещер на вашем пути только две! Решите в какую вы войдете! И нажмите цифру 1 или 2!\n")
            else:
                print(player_select)
                break
        except ValueError:
            print("\nЭто не похоже на цифру! Попробуй еще раз!\n")
    
    return player_select

player = player_select()

def dragon_check():
    if dragon == 1 and player == 1:
        print("\nВы приближаетесь к пещере...\nЕе темнота заставляет вас дрожать от страха...\n", end = "")
        print("Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...\n...моментально вас съедает!\n")
    elif dragon == 2 and player == 2:
        print("\nВы приближаетесь к пещере...\nЕе ослепительное свечение успокаивает вас...\n", end = "")
        print("Большой дракон медленно выходит к вам на встречу! Смотря на вас приокрывает пасть...\n...и предлогает взять сокровище!\n")


def replay():
    print("\nПопытаете удачу еще раз? (да или нет)\n")
    pass

def dranon_lands():
    pass