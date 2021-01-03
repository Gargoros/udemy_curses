# Домашнее задание: игра в палочки
# А теперь первое серьёзное домашнее задание. Вы попробуете разработать игру.

# Предлагаю древнюю китайскую игру в палочки.
# Играют два игрока.
# Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек. 
# Играют до тех пор пока не закончатся палочки. 
# Тот кто взял последним - тот проиграл.

# Реализуйте игру таким образом, 
# чтобы могли играть два человека. 
# Изначально есть 10 палочек. 
# На каждом ходу выводите на консоль текущее количество оставшихся палочек 
# и просите ввести количество палочек, 
# которое хочет взять игрок (который делает ход). 
# Не забывайте менять очерёдность игроков и сокращать кол-во палочек. 
# В конце надо вывести кто победил - первый или второй игрок.

# Нюансы реализации могут отличаться. 
# Кто-то может захотет запросить имена у игроков. 
# Кто-то может захотеть реализовать не с 10-ю палочками, 
# а с тем количеством, которое введёт пользователь 
# (может он хочет играть с 20-ю палочками?).

def board_game_sticks(*args):
    pass

# Приветсвие
def greeting(name1 = "Player 1", name2 = "Player 2"):
    name_1 = str(input("Player 1, enter your name, or your name will be Player 1 "))
    name_2 = str(input("Player 2, enter your name, or your name will be Player 2 "))

    while True:
        if not name_1.split() and name_2.split():
            print(f"Hello players {name_1} and {name_2}. Let's play a very old and simple game!")
        else:
            print(f"Hello players {name1} and {name2}. Let's play a very old and simple game!")
            break

# Правила игры
def game_rules():
    print('''    In the game "Sticks" 
    you will need to demonstrate your ability to calculate moves in advance. 
    There are twenty wooden sticks on the playing field in front of you. 
    The players, in turn, will take one, two or three sticks 
    (how much to take is up to the player). 
    The one who took the last stick loses, 
    so the goal of the game is to leave this stick to the opponent. 
    Player 1 traditionally has the first move.''')

#Ход игры
