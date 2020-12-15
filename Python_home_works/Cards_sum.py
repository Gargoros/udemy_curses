#Дан список карт. Например такой:
#current_hand = [2, 3, 4, 10, "Q", 5]
#В общем и целом, список может содержать следующие значения:
#[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"].
#У каждой карты есть свой "вес":
#2, 3, 4, 5, 6 - весят +1
#7, 8, 9 - весят 0
#10, "J", "Q", "K", "A" - весят -1
#Задача: имея список карт (current_hand), посчитать их
#общий "вес".
#Примечание: это уже задача посложнее. Для красивого решения
#подумайте как вам может помочь здесь словарь.

current_hand = [2, 3, 4, 10, "Q", 5]

card_deck = {2:1, 3:1, 4:1, 5:1, 6:1, 7:0, 8:0, 9:0, 10:-1, "J":-1, "Q":-1, "K":-1, "A": -1}
cards_sum = []
weight_card = []
for card in current_hand:
    if card in card_deck:
        weight_card.append(card_deck.get(card))
        cards_sum = sum(weight_card)

print(cards_sum)

card_sum = sum([card_deck[card] for card in current_hand])
print(card_sum)
        