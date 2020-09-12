import card


class Hand:
    def __init__(self):
        self.cards = []  # empty list of cards
        self.values = 0  # start with zero value
        self.aces = 0    # keep track of aces

    def add_card(self, new_card):
        self.cards.append(new_card)
        self.values += card.values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1



