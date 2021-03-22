#Эта игра про пещеры с драконами в одной из них сокровище, а в другой тебя съедят
#тебе нужно сделать правильный выбор и надеятся на удачу
import random
import time

friendly_dragon = random.randint(1, 2)

def introduction():
    print("\nВы находитесь в землях, заселенных драконами.\n")
    time.sleep(2)
    print("\nПеред собой вы видите две пещеры.\n")
    time.sleep(2)
    print("\nВ одной из них - дружелюбный дракон,\nкоторый готов поделиться с вами своими сокровищами.\n")
    time.sleep(2)
    print("\nВо второй - 'жадный и голодный дракон, который мигом вас съест.\n")
    time.sleep(2)


def cave():
    while True:
        time.sleep(2)
        player_select = input("\nВ какую пещеру вы войдете?  (нажмите клавишу 1 или 2)\n")
        try:
            player_select = int(player_select)
            if player_select not in range(1, 3):
                print("\nПещер на вашем пути только две! Решите в какую вы войдете! И нажмите цифру 1 или 2!\n")
            else:
                break
        except ValueError:
            print("\nЭто не похоже на цифру! Попробуй еще раз!\n")
    return player_select

def cave_check():
    player_cave = cave()
    if player_cave == friendly_dragon:
        print("\nВы приближаетесь к пещере...\nЕе темнота заставляет вас дрожать от страха...\n", end = "")
        time.sleep(2)
        print("Большой дракон медленно выходит к вам на встречу! \nСмотря на вас приокрывает пасть...\n...и предлогает взять сокровище!\n")
        time.sleep(2)
    else:
        print("\nВы приближаетесь к пещере...\nЕе ослепительное свечение успокаивает вас...\n", end = "")
        time.sleep(2)
        print("Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...\n...моментально вас съедает!\n")
        time.sleep(2)
        

def replay():
    print("\nПопытаете удачу еще раз? (да или нет)\n")
    while True:
        player = input().lower()
        player = str(player)
        if player != "да" and player != "нет":
            print("\nЭто не похоже на ответ!\nВы должны ввести либо 'да', либо 'нет'!\n")
        else:
            print()
            break
    return player

def dragon_lands():
    introduction()
    cave_check()
    if replay() == "да":
        dragon_lands()
    else:
        print("\nКоней игры\n")
dragon_lands()    

