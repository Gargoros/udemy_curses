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
ai_hand      = random.choice(game_items)
game_raund   = 1
print("\nLet's play rock, paper, scissors\n")
print(game_items)
print(ai_hand)

while True:
    player_hand = str(input("Enter a short name for the figure "))
    if player_hand == "R" or player_hand == "S" or player_hand == "P":
        print(f"Player chose is {player_hand} and ai chose is {ai_hand} ")
        break
    elif player_hand == "replay":
        break
    else:
        print("It doesn't look like a short name for the figure") 
          
while game_raund != 0 :
    if player_hand == "R" and ai_hand == "S" or player_hand == "S" and ai_hand == "P" or player_hand == "P" and ai_hand == "R":
        game_raund -= 1
        print("PLAYER WIN")
    elif ai_hand == "R" and player_hand == "S" or ai_hand == "S" and player_hand == "P" or ai_hand == "P" and player_hand == "R":
        game_raund -= 1
        print("AI WIN")
    else:
        print("DRAW")
        break
print("GAME OVER")



    
        
