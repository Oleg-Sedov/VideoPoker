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
    for i in suites:
        if i == suites[4]:
            combination = combinations[4]
        else:
            break
