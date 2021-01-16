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


#Переменные
player_1_name = str(input("Player 1, enter your name, or your name will be Player 1 "))
player_2_name = str(input("Player 2, enter your name, or your name will be Player 2 "))


def sticks_in_game():
    stick = input("Enter the number of sticks in the game ")
    while True:
        if stick.isdigit():
            print(f"{stick} sticks in the game ")
            return int(stick)
        else:
            print("10 sticks in the game ")
            return 10

sticks = sticks_in_game()

# Приветсвие
def greeting(name1, name2):
    '''
    DOCSTRING: checks user input and if an empty entry is found, replaces it.
    INPUT:     two inputs from users, with names.
    OUTPUT:    get the input value and print a greeting to the console for users.
    '''
    while True:
        if not name1 or not name2:
            name1 = "Player_1"
            name2 = "Player_2"
            print(f"Hello {name1} and {name2}. Let's play a very old and simple game!")
            return name1, name2
        else:
            print(f"Hello {name1} and {name2}. Let's play a very old and simple game!")
            return name1, name2
        
players_names = greeting(player_1_name, player_2_name)
# Правила игры
def game_rules():
    print('''\n\n    In the game "Sticks" 
    you will need to demonstrate your ability to calculate moves in advance. 
    There are twenty wooden sticks on the playing field in front of you. 
    The players, in turn, will take one, two or three sticks 
    (how much to take is up to the player). 
    The one who took the last stick loses, 
    so the goal of the game is to leave this stick to the opponent. 
    Player 1 traditionally has the first move.\n\n''')

#Палочки играков

def select_sticks(player_select, stick, player_name):
    '''
    DOCSTRING: subtracts from a given occurrence, where parameters are given by users.
    INPUT: values ​​to subtract, the name of the user who is executing the request and the number from which will be subtracted
    OUTPUT: subtraction result
    '''
    global sticks
    if player_select in range(1, 4):
        print(f"{player_name} removes {player_select} sticks from the game")
        sticks -= player_select
        print(f"{sticks} sticks left in the game \n")
        return sticks
    else:
        print("Incorrect input, please try again")

#Ход игры


def board_game_sticks():
    '''
    DOCSTRING: implements the game and calls functions to understand the rules and the course of the game
    INPUT: NONE
    OUTPUT: NONE
    '''
    greeting(player_1_name, player_2_name)
    sticks
    game_rules()
    while sticks != 0:
        pl1_select = int(input(f"{players_names[0]} Enter the number of sticks to remove, according to the rules of the game "))
        if select_sticks(pl1_select, sticks, player_1_name) < 4:
            print(f"{players_names[0]} win")
            break
        pl2_select = int(input(f"{players_names[1]} Enter the number of sticks to remove, according to the rules of the game "))
        if select_sticks(pl2_select, sticks, player_2_name) < 4:
            print(f"{players_names[1]} win")
            break

board_game_sticks()
