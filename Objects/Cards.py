import random

class Deck():
    def __init__(self):
        self.cards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', 'TC', 'TD', 'TH', 'TS', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS', 'KC', 'KD', 'KH', 'KS', 'AC', 'AD', 'AH', 'AS']

    def shuffle(self):
        random.shuffle(self.cards)

    def discard(self):
        discard_index = random.randrange(len(self.cards))
        card = self.cards[discard_index]
        del(self.cards[discard_index])
        return card

    def draw(self):
        draw_index = random.randrange(len(self.cards))
        card = self.cards[draw_index]
        del(self.cards[draw_index])
        return card

