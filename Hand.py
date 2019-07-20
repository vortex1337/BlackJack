import variables
values = variables.values
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        if card[1] == 'A' and self.value + values[card[1]] > 21 and self.value + 1 <= 21:
            self.value +=1
        else:
            self.value += values[card[1]]
