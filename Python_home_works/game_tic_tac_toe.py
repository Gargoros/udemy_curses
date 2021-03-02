# Создаем игровое поле 3 * 3
def game_field():
    figure = [num for num in range(1, 10)]
    line1 = f" {figure[0]} | {figure[1]} | {figure[2]} "
    line2 = "-" * len(line1)
    line3 = f" {figure[3]} | {figure[4]} | {figure[5]} "
    line4 = f" {figure[6]} | {figure[7]} | {figure[8]} "
    print("Draw game field\n")
    print(f"{line1}\n{line2}\n{line3}\n{line2}\n{line4}\n")
    return figure


#Выйгрышные комбинации
figure = game_field()
win_conditions = [[figure[0], figure[1], figure[2]], [figure[3], figure[4], figure[5]], [figure[6], figure[7], figure[8]],
                  [figure[0], figure[3], figure[6]], [figure[1], figure[4], figure[7]], [figure[2], figure[5], figure[8]],
                  [figure[0], figure[4], figure[8]], [figure[2], figure[4], figure[6]]]

#Ввод игроков
def player_choice():
    turn = "X"
    raund = 0

    while raund < 9:
        player = input(f"Enter the num of '{turn}' cell:  ")
        try:
            player = int(player)
            if player not in range(1, 10):
                print("Out of range 1 to 9! Try again!")
            else:
                print(player)
                figure[player - 1] = turn
                raund +=1
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(figure)
        except ValueError:
            print("Incorrect input! Try again!")
    return player

#