#Эта игра про пещеры с драконами в одной из них сокровище, а в другой тебя съедят
#тебе нужно сделать правильный выбор и надеятся на удачу
import random
import time

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
    print("\nВ какую пещеру вы войдете?  (нажмите клавишу 1 или 2)\n")
    time.sleep(2)

    while True:
        player_select = input()
        try:
            player_select = int(player_select)
            if player_select not in range(1, 3):
                print("\nПещер на вашем пути только две! Решите в какую вы войдете! И нажмите цифру 1 или 2!\n")
            else:
                break
        except ValueError:
            print("\nЭто не похоже на цифру! Попробуй еще раз!\n")
    return player_select

player_cave = cave()
friendly_dragon = random.randint(1, 2)

def cave_check():
    if player_cave == friendly_dragon:
        print("\nВы приближаетесь к пещере...\nЕе темнота заставляет вас дрожать от страха...\n", end = "")
        time.sleep(2)
        print("Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...\n...моментально вас съедает!\n")
        time.sleep(2)
    else:
        print("\nВы приближаетесь к пещере...\nЕе ослепительное свечение успокаивает вас...\n", end = "")
        time.sleep(2)
        print("Большой дракон медленно выходит к вам на встречу! Смотря на вас приокрывает пасть...\n...и предлогает взять сокровище!\n")
        time.sleep(2)

def replay():
    print("\nПопытаете удачу еще раз? (да или нет)\n")
    while True:
        player = input()
        try:
            player = str(player)
            if player.lower() != "да" or player.lower() != "нет":
                print("\nЭто не похоже на ответ!\nВы должны ввести либо 'да', либо 'нет'!\n")
            else:
                print(player)
                break
        except ValueError:
            print("\nЭто не то, что нужно ввести!\nПопробуй снова!\n")
    return player

def dragon_lands():
    introduction()
    cave()
    cave_check()
    replay()
    pass

