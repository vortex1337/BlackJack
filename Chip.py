class Chip:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self, price):
        self.total += price
    def lose_bet(self, price):
        self.total -= price
