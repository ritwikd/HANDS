class Game():
    def __init__(self, deck):
        self.deck = deck
        self.table = []
        self.discarded = []

    def deal_hand(self):
        hand = [self.deck.draw(), self.deck.draw()]
        return hand

    def deal_flop(self):
        self.discarded = [self.deck.discard()]
        self.table = [self.deck.draw(), self.deck.draw(), self.deck.draw()]

    def deal_turn(self):
        self.discarded.append(self.deck.discard())
        self.table.append(self.deck.draw())

    def deal_river(self):
        self.discarded.append(self.deck.discard())
        self.table.append(self.deck.draw())

    #def check_hand(self, hand):