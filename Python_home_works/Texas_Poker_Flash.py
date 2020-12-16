# Идёт игра в семи-карточный техасский покер.
# На столе лежат пять карт и в руке две карты.
# Необходимо определить есть ли комбинация, называемая флеш (Flush).
# Комбинация флеш определяется наличием пяти карт одной масти (среди 
# всех карт: и тех, что лежат на столе и тех, что в руке)
# В вашем файле для решения есть две переменные: table_cards и hand_cards.
# В обе переменные записаны списки карт, в первой - пять карт на столе,
# во второй - две карты в руке.
# Вот примеры списков, которые будут записаны в эти переменные для проверки
# вашего решения:

# ['A_S', 'J_H','7_D', '8_D', '10_D'], ['J_D', '3_D']
# ['10_S', '7_S', '9_H','4_S', '3_S'], ['K_S', 'Q_S']
# ['3_S', '10_H', '10_D', '10_C', '10_S'], ['3_S', '4_D']

# Как видите, каждая карта записывается в определённом формате.
# Первым символом обозначается "номинал" карты.
# Возможные значения: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
# Второй символ - всегда подчеркивание.
# Третий символ - масть. Возможное значения: S(пики), H(черви), D(буби), C(трефы)

# Если присутствует комбинация флеш - вывесли на консоль "Flush!",
# в противном случае вывести "No Flush!"

#Вариант 1
table_cards = ['A_S', 'J_H','7_D', '8_D', '10_D']
hand_cards = ['J_D', '3_D']
game_round = table_cards + hand_cards

showdown = [suit[-1] for suit in game_round]
if showdown.count("S") >= 5 or showdown.count("H") >= 5:
    print("Flush!")
elif showdown.count("D") >= 5 or showdown.count("C") >= 5:
    print("Flush!")
else:
    print("No Flush!")


#Вариант 2 
flush = False
for suit in "SCHD":
    if showdown.count(suit) >= 5:
        flush = True
if flush:
    print("Flush!")
else:
    print("No Flush!")


#Вариант 3 
flush = any([showdown.count(suit) >= 5 for suit in "SHCD"])
if flush:
    print("Flush!")
else:
    print("No Flush!")

#Вариант 4
flush = [sum([card[-1] == suit for card in table_cards + hand_cards]) for suit in "SCHD"]
if flush:
    print("Flush!")
else:
    print("No Flush!")