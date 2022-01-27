# This is the try up of skills
# ♠︎ ♣︎ ♥︎ ♦︎
import poker_functions
import random

combinations = ('Pair of Jacks of better', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full House',
                'Four of a kind', 'Straight Flush', 'Royal Flush')
payout_rates = (2, 4, 7, 14, 28, 50, 340, 3500, 25000)  # множители выйгрыша

points = 1000
combination = ''
exit_request = ''


#  перенести функцию к функциям
def count_win():  # расчитываем выйгрыш
    if combination not in combinations:
        win = 0
    else:
        win = bet * payout_rates[combinations.index(combination)]
    return win


def payout_table():
    for i, _ in enumerate(combinations):
        print(f'{combinations[i].ljust(len(combinations[0]))} x {payout_rates[i]}')


print(f'''Добро пожаловать в игру "Видео покер". Задача игрока собрать как можно более сильную покерную комбинацию:
Чтобы выйграть необходимо собрать комбинацию от пары валетов или старше ("Jacks or better").
Таблица выплат:''')
payout_table()
print('''Для замены карт используйте числа от 1 до 5 без пробелов, где число соответствует позиции карты слева направо.
Например:
Вам раздали A♣ K♥ T♣ T♥ 9♠
Чтобы заменить A♣ K♥ 9♠ необходимо ввести 125
Обратите внимание, что числа вводятся без пробелов, также порядок цифр не имеет значения:
125 дает тот же результат, что и 152, 215, 251, 521 и 512.
 ''')
print('У Вас', points, 'очков!')

while points > 0 and exit_request != 'y' and exit_request != 'у':
    print('Введите ставку:')
    bet = input()
    try:  # проверка ставки игрока на корректность данных
        bet = int(bet)
        if bet > points:
            raise ValueError
    except ValueError:
        print(f'Некорректная ставка. Введите действиетльное (целое) число ( > 0), не превышающее'
              f'доступное количество очков - {points}''')
        continue

    points -= bet
    card_deck = list(poker_functions.cards_deck_generate())
    random.shuffle(card_deck)  # Тасуем карты

    player_cards = [card_deck.pop(0) for _ in range(5)]  # Выдаем 5 карт игроку, удаляя выданное из игровой колоды
    print(*player_cards)  # Показываем карты игроку
    player_cards_prev = player_cards.copy()  # сохраняем первоначальные карты

    print('Выберите карты для замены. Введите порядковые номера карт без пробелов для замены (от 1 до 5)'
          'Номера карт не должны повторяться')
    to_change_flag = False
    while to_change_flag is False:  # проверяем корректность данных для замены карт
        to_change = list(set(input()))  # удаление случайных повторно дважды выбранных карт ("113" -> "13")
        count = 0
        for changed in to_change:
            if changed.isdigit() is False:
                break
            else:
                if int(changed) > 5:
                    break
                else:
                    count += 1
        if count == len(to_change):
            to_change_flag = True

        else:
            print('Для выбора карт используйте целые числа от 1 до 5. Номера карт не должны повторяться!'
                  '\nВыберите карты для замены.')
    to_change = [int(to_change[i]) for i in range(len(to_change))]

    for i in to_change:  # замена выбранных карт
        player_cards[i - 1] = card_deck.pop(1)

    combination = poker_functions.combination_check(player_cards)

    print(f'Ваша комбинация {combination}!')
    print('Начальные карты\n', ' '.join(player_cards_prev))
    print('Ваши текущие карты\n', ' '.join(player_cards).upper())
    points += count_win()
    if combination in combinations:
        print(f'Чистый выйгрыш {count_win() - bet} очков!')
    else:
        print('К сожалению, Вы проиграли.')
    print(f'У Вас {points} очков!')
    if points == 0:  # Какой смысл предлагать продолжать играть если все проиграно :(
        break
    print('Если хотите продожить нажмите Enter. Для выхода введите "y"')
    exit_request = input()
if points == 0:
    print('Вы все проиграли, барин')
else:
    print(f'Поздравляем Ваш баланс {points} очков.\nСпасибо за игру')
   