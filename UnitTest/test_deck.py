import unittest
import deck


class MyTestCase(unittest.TestCase):
    my_deck = deck.Deck()

    def test_something(self):
        result = len(self.my_deck.all_cards)
        self.assertEqual(result, 52)


if __name__ == '__main__':
    unittest.main()
