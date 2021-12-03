"""This file determines combinations a player has."""

import itertools

ranks_dict = {'A': 14, 'a': 1, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
reversed_ranks_dict = {14: 'A', 1: 'a', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9', 8: '8',
                       7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2'}
combinations = ('Pair of Jacks of better', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full House',
                'Four of a kind', 'Straight Flush', 'Royal Flush')


def cards_deck_generate():
    card_deck = ('A♠', 'A♣', 'A♥', 'A♦', 'K♠', 'K♣', 'K♥', 'K♦', 'Q♠', 'Q♣', 'Q♥', 'Q♦', 'J♠', 'J♣', 'J♥', 'J♦',
                 'T♠', 'T♣', 'T♥', 'T♦', '9♠', '9♣', '9♥', '9♦', '8♠', '8♣', '8♥', '8♦', '7♠', '7♣', '7♥', '7♦',
                 '6♠', '6♣', '6♥', '6♦', '5♠', '5♣', '5♥', '5♦', '4♠', '4♣', '4♥', '4♦', '3♠', '3♣', '3♥', '3♦',
                 '2♠', '2♣', '2♥', '2♦')
    return card_deck


def straight_flush_check(player_cards):
    """The function determines if a player got flush, straight or straight flush. Requires player card_deck as argument.
    Works for 5 carded poker hands."""

    comb = ''
    ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])
    suites = [suite[1] for suite in player_cards]
    counter_flush = 0
    for suite in suites:  # проверка есть ли флэш
        if suite == suites[4]:
            counter_flush += 1
    
    counter_straight = 0
    for rank in range(4):  # проверка есть ли стрит
        if ranks[rank + 1] - 1 == ranks[rank]:
            counter_straight += 1
    if counter_straight != 4:  # проверка на "нижний" стрит
        counter_straight = 0
        ranks_dict['A'] = 1  # установка "веса" туза за единицу
        ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])
        for rank in range(4):
            if ranks[rank + 1] - 1 == ranks[rank]:
                counter_straight += 1
        ranks_dict['A'] = 14  # после рассчетов и проверки на низший стрит возвращаем "вес" туза

    if counter_flush == 5 and counter_straight == 4:
        comb = combinations[7]
        if max(ranks) == 14:
            comb = combinations[8]
    elif counter_flush == 5:
        comb = combinations[4]
    elif counter_straight == 4:
        comb = combinations[3]

    return comb


def pairs_3ofkind_4ofkind_fullhouse_check(player_cards):
    """The function determines if a player got pair, two pairs, 3 of a kind, 4 of a kind, full house or just high card
        Requires player card_deck as argument. Works for 5 carded poker hands."""

    comb = ''
    ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])
    counter = 0
    used_cards = []
    for rank in range(4):  # сравниваем ранг первых 4 карт со следующей картой 1с2, 2с3 ...
        if ranks[rank] == ranks[rank + 1]:
            counter += 1  # считаем кол-во совпадений, совпадаение одно - одна пара. два-2 пары/cет. три-каре/фулл
            used_cards.append(rank)  # записываем индексы карты которая совпадает со следующей
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
    if counter == 3 and (used_cards[2] - used_cards[1] != 1 or used_cards[1] - used_cards[0] != 1):
        comb = combinations[5]
    elif counter == 3:
        comb = combinations[6]
    return comb


def hand_determiner(h_cards, c_cards):
    """Receives pocket card of a player and common card_deck as arguments. Finds all possible variations of hands with
    this card_deck."""

    combs = []
    cards = h_cards + c_cards
    for c in itertools.combinations(cards, 5):
        combs.append(list(c))
    # return combs
    pass
