import card
import random


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                self.all_cards.append(card.Card(suit, rank))

    def card_shuffle(self):
        return random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

