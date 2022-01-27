"""This file determines combinations a player has."""

import itertools


def cards_deck_generate():
    card_deck = ('A♠', 'A♣', 'A♥', 'A♦', 'K♠', 'K♣', 'K♥', 'K♦', 'Q♠', 'Q♣', 'Q♥', 'Q♦', 'J♠', 'J♣', 'J♥', 'J♦',
                 'T♠', 'T♣', 'T♥', 'T♦', '9♠', '9♣', '9♥', '9♦', '8♠', '8♣', '8♥', '8♦', '7♠', '7♣', '7♥', '7♦',
                 '6♠', '6♣', '6♥', '6♦', '5♠', '5♣', '5♥', '5♦', '4♠', '4♣', '4♥', '4♦', '3♠', '3♣', '3♥', '3♦',
                 '2♠', '2♣', '2♥', '2♦')
    return card_deck

def combination_check(player_cards):
    ranks_dict = {'A': 14, 'a': 1, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    combinations = ('Pair of Jacks of better', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full House',
                    'Four of a kind', 'Straight Flush', 'Royal Flush')

    ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])
    suites = [suite[1] for suite in player_cards]

    counter_flush = 0
    for suite in suites:  # проверка есть ли флэш
        if suite == suites[4]:
            counter_flush += 1

    counter_straight = 0
    for index in range(4):  # проверка есть ли стрит
        if ranks[index] == ranks[index + 1] - 1:
            counter_straight += 1

    if {2, 3, 4, 5}.issubset(ranks):  # проверка на "нижний" стрит
        counter_straight = 0
        for card in player_cards:
            if 'A' in card:
                del player_cards[player_cards.index(card)]
                card = card.lower()
                player_cards.append(card)
        ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])
        for index in range(4):
            if ranks[index] == ranks[index + 1] - 1:
                counter_straight += 1

    counter = 0
    used_cards = []
    for index in range(4):  # сравниваем ранг первых 4 карт со следующей картой 1с2, 2с3 ...
        if ranks[index] == ranks[index + 1]:
            counter += 1  # считаем кол-во совпадений, совпадаение одно - одна пара. два-2 пары/cет. три-каре/фулл
            used_cards.append(index)  # записываем индексы карты которая совпадает со следующей
        # если совпадают последовательные индексы, то это сет либо карэ (в зависимости от счетчика совпадений)
        # если разность индексов > 1, то это две пары либо фуллхаус (в той же зависимости)

    if counter == 0:
        comb = 'High card'
    if counter == 1:
        if ranks[used_cards[0]] >= 11:
            comb = combinations[0]
        else:
            comb = 'Pair'
    if counter == 2 and used_cards[1] - used_cards[0] != 1:
        comb = combinations[1]
    elif counter == 2 and used_cards[1] - used_cards[0] == 1:
        comb = combinations[2]
    if counter_straight == 4:
        comb = combinations[3]
    if counter_flush == 5:
        comb = combinations[4]
    if counter == 3 and (used_cards[2] - used_cards[1] != 1 or used_cards[1] - used_cards[0] != 1):
        comb = combinations[5]
    elif counter == 3:
        comb = combinations[6]
    if counter_flush == 5 and counter_straight == 4:
        comb = combinations[7]
        if max(ranks) == 14:
            comb = combinations[8]
    return comb

