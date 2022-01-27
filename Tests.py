import unittest
import poker_functions


class CombinationsTest(unittest.TestCase):
    def test_straight(self):
        player_cards = [['A♣', '2♥', '3♣', '4♥', '5♠'], ['2♥', '3♣', '4♥', '5♠', '6♣'], ['7♥', '3♣', '4♥', '5♠', '6♣'],
                        ['7♥', '8♣', '4♥', '5♠', '6♣'], ['7♥', '8♣', '9♥', '5♠', '6♣'], ['7♥', '8♣', '9♥', 'T♠', '6♣'],
                        ['7♥', '8♣', '9♥', 'T♠', 'J♣'], ['Q♥', '8♣', '9♥', 'T♠', 'J♣'], ['Q♥', 'K♣', '9♥', 'T♠', 'J♣'],
                        ['Q♥', 'K♣', 'A♥', 'T♠', 'J♣']]
        for hand in player_cards:
            result = poker_functions.combination_check(hand)
            self.assertEqual(result, 'Straight')  # add assertion here

    def test_flush(self):
        player_card = ['8♣', '2♣', '3♣', '4♣', '5♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Flush')
        pass

    def test_pair(self):
        player_card = ['8♣', '8♣', '3♥', '4♣', '5♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Pair')

    def test_jack_or_better(self):
        player_card = ['J♥', 'J♣', '3♣', '4♣', '5♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Pair of Jacks of better')

    def test_two_pairs(self):
        player_card = ['J♥', 'J♣', '3♣', '3♥', '5♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Two pairs')

    def test_three_of_a_kind(self):
        player_card = ['J♥', 'J♣', 'J♠', '3♥', '5♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Three of a kind')

    def test_full_house(self):
        player_card = ['J♥', 'J♣', 'J♠', '3♥', '3♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Full House')

    def test_four_of_a_kind(self):
        player_card = ['J♥', 'J♣', 'J♠', 'J♦', '3♣']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Four of a kind')

    def test_straight_flush(self):
        player_card = ['Q♥', 'K♥', '9♥', 'T♥', 'J♥']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Straight Flush')

    def test_royal_flush(self):
        player_card = ['Q♥', 'K♥', 'A♥', 'T♥', 'J♥']
        result = poker_functions.combination_check(player_card)
        self.assertEqual(result, 'Royal Flush')


if __name__ == '__main__':
    unittest.main()
