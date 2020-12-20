# Написать игру в "камень-ножницы-бумага" против компьютера.

# Запустить игру в бесконечном цикле. 
# Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага). 
# Сгенерировать случайный выбор компьютера. 
# Вывести выбор компьютера.
# Определить победителя, выведя соответствующую информацию. 
# Спросить пользователя - хочет ли он повторить игру. 
# Если хочет - повторить, не хочет - выйти из цикла.

import random

game_items   = ["R", "S", "P"]
game_raund   = True
print("\nLet's play rock, paper, scissors\n")
print(game_items)

while game_raund:
    ai_hand = random.choice(game_items)
    print(ai_hand)
    player_hand = str(input("Enter a short name for the figure "))
    if player_hand == "R" or player_hand == "S" or player_hand == "P":
        print(f"Player chose is {player_hand} and ai chose is {ai_hand} ")
        if player_hand == "R" and ai_hand == "S" or player_hand == "S" and ai_hand == "P" or player_hand == "P" and ai_hand == "R":
            print("PLAYER WIN")
            game_raund = False
        elif ai_hand == "R" and player_hand == "S" or ai_hand == "S" and player_hand == "P" or ai_hand == "P" and player_hand == "R":
            print("AI WIN")
            game_raund = False
        else:
            print("DRAW")
        while game_raund == False:
            print("Do you want to play again\n")
            player_hand = str(input("Enter 'yes' to replay or 'no' to quit "))
            if player_hand == "yes":
                print("Let's play again!")
                game_raund  = True
            elif player_hand == "no":
                print("Good luck")
                break
            else:
                print("It doesn't seem like an answer!!!")
    else:
        print("It doesn't look like a short name for the figure")
print("GAME OVER")