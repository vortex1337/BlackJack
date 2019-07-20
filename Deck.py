import random
import variables
suits = variables.suits
ranks = variables.ranks
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit,rank))
    def __str__(self):
        return str(self.deck)
    def shuffle(self):
        return random.shuffle(self.deck)
    def deal(self):
        choice = random.choice(self.deck)
        self.deck.remove(choice)
        return choice
