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


payout_table = (f'''Таблица выплат:
        {combinations[0]} х {payout_rates[0]}
        {combinations[1]}{(len(combinations[0]) - len(combinations[1])) * ' '} х {payout_rates[1]}
        {combinations[2]}{(len(combinations[0]) - len(combinations[2])) * ' '} x {payout_rates[2]}
        {combinations[3]}{(len(combinations[0]) - len(combinations[3])) * ' '} x {payout_rates[3]}
        {combinations[4]}{(len(combinations[0]) - len(combinations[4])) * ' '} x {payout_rates[4]}
        {combinations[5]}{(len(combinations[0]) - len(combinations[5])) * ' '} x {payout_rates[5]}
        {combinations[6]}{(len(combinations[0]) - len(combinations[6])) * ' '} x {payout_rates[6]}
        {combinations[7]}{(len(combinations[0]) - len(combinations[7])) * ' '} x {payout_rates[7]}
        {combinations[8]}{(len(combinations[0]) - len(combinations[8])) * ' '} x {payout_rates[8]}''')

print(f'''Добро пожаловать в игру "Видео покер". Задача игрока собрать как можно более сильную покерную комбинацию:
Чтобы выйграть необходимо собрать комбинацию от пары валетов или старше ("Jacks or better").
{payout_table}
Для замены карт используйте числа от 1 до 5 без пробелов, где число соответствует позиции карты слева направо.
Например:
Вам раздали A♣ K♥ T♣ T♥ 9♠
Чтобы заменить A♣ K♥ 9♠ необходимо ввести 125
Обратите внимание, что числа вводятся без пробелов, также порядок цифр не имеет значения:
125 дает тот же результат, что и 152, 215, 251, 521 и 512.
 ''')
print('У Вас', points, 'очков!')

while points > 0 and exit_request != 'y' and exit_request != 'у':
    to_change_flag = False  # сбрасываем флаг проверки корректности выбранных к замене карт
    print('Введите ставку:')
    bet = input()  # ставка игрока
    try:  # проверка ставки игрока на корректность данных
        bet = int(bet)
    except ValueError:
        print('Некорректная ставка. Введите действиетльное (целое) число ( > 0)')
        continue

    points -= bet
    cards = cards_deck.copy()  # загружаем карты в игровую колоду. Имитация возврата карт в колоду после раунда
    random.shuffle(cards)  # Тасуем карты

    player_cards = [cards.pop(0) for _ in range(5)]  # Выдаем 5 карт игроку, удаляя выданное из игровой колоды
    print(*player_cards)  # Показываем карты игроку

    print('Выберите карты для замены. Введите порядковые номера карт без пробелов для замены (от 1 до 5)')

    while to_change_flag is False:
        to_change = list(input())  # создание списка к замене
        count = 0
        for changed in to_change:
            if changed.isdigit() is False:
                continue
            else:
                if int(changed) > 5:
                    continue
                else:
                    count += 1
        if count == len(to_change):
            to_change_flag = True
        else:
            print('Для выбора карт используйте целые числа от 1 до 5\nВыберите карты для замены. ')
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
    if points == 0:  # Какой смысл предлагать продолжать Играть если все проебано :(
        break
    print('Если хотите продожить нажмите Enter. Для выхода введите "y"')
    exit_request = input()
if points == 0:
    print('Вы все проиграли, барин')
else:
    print(f'Поздравляем Ваш баланс {points} очков.\nСпасибо за игру')
   