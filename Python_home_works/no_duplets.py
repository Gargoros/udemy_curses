# ДЗ: Без дуплетов!
# Играем в кости. Правила следующие:
# 1. Кидаем пару костей.
# 2. Складываем количество выпавших чисел и прибавляем к общему кол-ву очков
# 3. Повторяем пункты 1 и 2 трижды.
# 4. Если выпадает дуплет (на обоих костях одно и то же число), 
# то кол-во очков обнуляется и последующие броски не считаются.

# Задание:
# Напишите функцию calc_dice_scores принимающую список кортежей и,
# возвращающую общее кол-во очков.
# Примеры вызовов и ожидаемый результат.

# calc_dice_scores ([(1, 2), (3, 4), (5, 6)]) ➞ 21 
# calc_dice_scores ([(1, 1), (5, 6), (6, 4)]) ➞ 0 
# calc_dice_scores ([(4, 5), (4, 5), (4, 5)]) ➞ 27
# Всегда передаются три кортежа по два элемента в каждом.

lst = [(1, 2), (3, 4), (5, 6)]

def calc_dice_scores(lst):
    '''
    DOCSTRING: The function calculates game points
    INPUT:     Takes a list of tuples with game points at the input 
    OUTPUT:    Displays the total amount of points if the game conditions are not violated
    '''
    score = [dice[0] + dice[1] for dice in lst if dice[0] != dice[1]]
    if len(score) == 3:
        return sum(score)
    else:
        return 0


def calc_dice_scores_udemy(lst):
    return sum([a +b for a, b in lst]) if not any([a == b for a, b in lst]) else 0

calc_dice_scores_udemy(lst)