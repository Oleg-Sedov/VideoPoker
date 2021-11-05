# This is the try up of skills
# ♠︎ ♣︎ ♥︎ ♦︎

import random

# Создаем колоду карт
cards_deck = ['A♠', 'A♣', 'A♥', 'A♦', 'K♠', 'K♣', 'K♥', 'K♦', 'Q♠', 'Q♣', 'Q♥', 'Q♦', 'J♠', 'J♣', 'J♥', 'J♦',
              'T♠', 'T♣', 'T♥', 'T♦', '9♠', '9♣', '9♥', '9♦', '8♠', '8♣', '8♥', '8♦', '7♠', '7♣', '7♥', '7♦',
              '6♠', '6♣', '6♥', '6♦', '5♠', '5♣', '5♥', '5♦', '4♠', '4♣', '4♥', '4♦', '3♠', '3♣', '3♥', '3♦',
              '2♠', '2♣', '2♥', '2♦']
combinations = ['Pair of Jacks of better', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full House',
                'Four of a kind', 'Straight Flush', 'Royal Flush']
payout_rates = [2, 4, 7, 14, 28, 50, 340, 3500, 25000]  # множители выйгрыша
# Словари ранга карт (карта:ранг, ранг:карта)
ranks_dict = {'A': 14, 'a': 1, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
              '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
reversed_ranks_dict = {14: 'A', 1: 'a', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9', 8: '8',
                       7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2'}
points = 1000
bet = 0
combination = ''
exit_request = ''


def flush_check():  # функция проверки на флэш
    global combination
    for suite in suites:
        if suite == suites[0]:
            combination = combinations[4]
        else:
            break


def straight_check():
    global combination
    combination_2 = ''
    counter = 0
    for rank in range(4):
        if ranks[rank + 1] - 1 == ranks[rank]:  # check in visualizer
            counter += 1
    if counter == 4:
        combination_2 = combinations[3]
    if combination == combinations[4] and combination_2 == combinations[3]:
        combination = combinations[7]
        if max(ranks) == 14:
            combination = combinations[8]


def pairs_3ofkind_4ofkind_fullhouse_check():  # проверка пары/две пары, сет, каре, фуллхаус
    global combination
    counter = 0
    used_cards = []
    for rank in range(4):  # сравниваем ранг первых 4 карт со следующей картой 1с2, 2с3 ...
        if ranks[rank] == ranks[rank + 1]:
            counter += 1  # считаем кол-во совпадений, совпадаение одно - одна пара. два-2 пары/ сет. три - каре/фулл
            used_cards.append(rank)  # записываем индексы карты которая совпадает со следующей
    # если совпадают последовательные индексы, то это сет либо карэ (в зависимости от счетчика совпадений)
    # если разность индексов > 1, то это две пары либо фуллхаус (в той же зависимости)
    if counter == 0:
        combination = 'High card'
    if counter == 1:
        if ranks[used_cards[0]] >= 11:
            combination = combinations[0]
        else:
            combination = 'Pair'
    if counter == 2 and used_cards[1] - used_cards[0] != 1:
        combination = combinations[1]
    elif counter == 2 and used_cards[1] - used_cards[0] == 1:
        combination = combinations[2]
    if counter == 3 and (used_cards[2] - used_cards[1] != 1 or used_cards[1] - used_cards[0] != 1):
        combination = combinations[5]
    elif counter == 3:
        combination = combinations[6]


def count_win():  # расчитываем выйгрыш
    global combination, bet, payout_rates
    if combination not in combinations:
        win = 0
    else:
        win = bet * payout_rates[combinations.index(combination)]
    return win


while points > 0 and exit_request != 'y' and exit_request != 'у':
    print('У Вас', points, 'очков!')
    print('Введите ставку:')
    bet = int(input())
    points -= bet
    cards = cards_deck.copy()  # загружаем карты в игровую колоду. Имитация возврата карт в колоду после раунда
    random.shuffle(cards)  # Тасуем карты

    player_cards = [cards.pop(0) for _ in range(5)]  # Выдаем 5 карт игроку, удаляя выданное из игровой колоды
    print(*player_cards)  # Показываем карты игроку
    print('Выберите карты для замены. Введите порядковые номера карт для замены (от 1 до 5)')
    to_change = list(input())  # создание списка к замене
    to_change = [int(to_change[i]) for i in range(len(to_change))]

    for i in to_change:  # замена выбранных карт
        player_cards[i - 1] = cards.pop(1)
    suites = [i[1] for i in player_cards]  # получаем масти карт
    nominal = [i[0] for i in player_cards]  # получаем номиналы карт (как видит игрок)
    ranks = sorted([ranks_dict.get(i[0]) for i in player_cards])  # ранг карт + сортировка для проверки стрита

    flush_check()
    straight_check()
    pairs_3ofkind_4ofkind_fullhouse_check()

    print(f'У Вас {combination}!')
    print(*player_cards)
    points += count_win()
    if combination in combinations:
        print(f'Вы выйграли {count_win() - bet} очков!')
    else:
        print('К сожалению, Вы проиграли.')
    print(f'У Вас {points} очков!')
    print('Если хотите продожить нажмите Enter. Для выхода введите "y"')
    exit_request = input()

print(f'Поздравляем Ваш баланс {points} очков. \nСпасибо за игру')
