import unittest
import card


class MyTestCase(unittest.TestCase):
    testcard = card.Card("Club", "Ace")

    def test_suit(self):
        suit = "Club"
        rank = "Ace"
        self.assertEqual(self.testcard.suit, suit)

    def test_rank(self):
        value = 11
        result = self.testcard.value
        self.assertEqual(result, value)


if __name__ == '__main__':
    unittest.main()
