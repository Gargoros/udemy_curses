# Написать игру в "камень-ножницы-бумага" против компьютера.

# Запустить игру в бесконечном цикле. 
# Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага). 
# Сгенерировать случайный выбор компьютера. 
# Вывести выбор компьютера.
# Определить победителя, выведя соответствующую информацию. 
# Спросить пользователя - хочет ли он повторить игру. 
# Если хочет - повторить, не хочет - выйти из цикла.

import random

game_fig   = ["R", "S", "P"]
ai_fig     = random.choice(game_fig)
game_raund = 1
print("\nLet's play rock, paper, scissors\n")
print(game_fig)
print(ai_fig)

while True:
    player_fig = str(input("Enter a short name for the figure "))
    if player_fig == "R" or player_fig == "S" or player_fig == "P":
        print(f"Player chose is {player_fig} and ai chose is {ai_fig} ")
        break
    elif player_fig == "replay":
        break
    else:
        print("It doesn't look like a short name for the figure") 
          
while game_raund != 0 :
    if player_fig == "R" and ai_fig == "S" or player_fig == "S" and ai_fig == "P" or player_fig == "P" and ai_fig == "R":
        game_raund -= 1
        print("PLAYER WIN")
    elif ai_fig == "R" and player_fig == "S" or ai_fig == "S" and player_fig == "P" or ai_fig == "P" and player_fig == "R":
        game_raund -= 1
        print("AI WIN")
    elif player_fig == ai_fig:
        print("DRAW")
        break
print("GAME OVER")

    
        
