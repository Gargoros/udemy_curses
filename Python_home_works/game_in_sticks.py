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


# Переменные для ввода имен двух игроков
player_1_name = str(input("Player 1, enter your name, or your name will be Player 1 "))
player_2_name = str(input("Player 2, enter your name, or your name will be Player 2 "))

# Приветсвие: Функция выполняет проверку ввода двух игроков,
# присваивает им имена и выводит на консоль приветсвие игроков
def greeting(name1, name2):
    
    while True:
        if not name1 or not name2:
            name1 = "Player_1"
            name2 = "Player_2"
            print(f"\nHello {name1} and {name2}. Let's play a very old and simple game!")
            return name1, name2
        else:
            print(f"\nHello {name1} and {name2}. Let's play a very old and simple game!")
            return name1, name2
        
players_names = greeting(player_1_name, player_2_name)

# Правила игры
# Функция выводит на консоль правила игры
def game_rules():
    print('''\n\n    In the game "Sticks" 
    you will need to demonstrate your ability to calculate moves in advance. 
    There are twenty wooden sticks on the playing field in front of you. 
    The players, in turn, will take one, two or three sticks 
    (how much to take is up to the player). 
    The one who took the last stick loses, 
    so the goal of the game is to leave this stick to the opponent. 
    Player 1 traditionally has the first move.\n\n''')

# Функция выполняет проверку количества палочек в игре,
# по умолчанию возврощает 10 палочек, результат записывается в новую переменную
def sticks_in_game():
    stick = input("\nEnter the number of sticks in the game ")
    while True:
        if stick.isdigit():
            print(f"\n{stick} sticks in the game \n")
            return int(stick)
        else:
            print("\n10 sticks in the game \n")
            return 10

sticks = sticks_in_game()

# Палочки играков
# Функция выполняет проверку ввода игрока и изменяет количество палочек в игре, перезаписывая переменную
def select_sticks(player_name):
    
    global sticks
    while True:
        print(f"\n{sticks} sticks left in the game \n")
        player_select = input(f"{player_name} Enter the number of sticks to remove, according to the rules of the game ")
        if player_select.isdigit() == True:
            player_select = int(player_select)
            if player_select in range(1, 4):
                print(f"{player_name} removes {player_select} sticks from the game")
                sticks -= player_select
                return sticks
            else:
                print("In one game raund, you can remove from 1 to 3 sticks ")
        else:
            print("You must enter the 'int' number of sticks")

# Проверка победы игрока
# Функция выполняет проверку условия победы одного из двух игроков и выводит на консоль имя победителя

def win(name1, name2):
    while sticks > 0:
        if select_sticks(name1) < 4:
            print(f"{name1} win")
            break
        elif select_sticks(name2) < 4:
            print(f"{name2} win")
            break

#Ход игры

def board_game_sticks():
    
    players_names
    game_rules()
    sticks
    win(players_names[0], players_names[1])
    


board_game_sticks()
