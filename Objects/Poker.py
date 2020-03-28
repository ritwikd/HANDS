from Objects.Utils import *
from Objects import Conditions

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

    def check_hand(self, hand):
        total_hand = hand + self.table
        total_hand_numbers = get_numbers(total_hand)
        total_hand_suits = get_suits(total_hand)

        number_frequencies = get_number_frequencies(total_hand_numbers)
        suit_frequencies = get_suit_frequencies(total_hand_suits)

        filtered_numbers = list(filter(lambda f: number_frequencies[f] > 1, list(set(total_hand_numbers))))
        filtered_number_frequencies = [(num, number_frequencies[num]) for num in filtered_numbers]

        filtered_suits = list(filter(lambda f: suit_frequencies[f] > 4, list(set(total_hand_suits))))
        filtered_suit_frequencies = [(suit, suit_frequencies[suit]) for suit in filtered_suits]

        win_conditions = {
            'High Card' : Conditions.high_card(total_hand_numbers, filtered_number_frequencies, filtered_suit_frequencies),
            'Pair' : Conditions.pair(filtered_number_frequencies, filtered_suit_frequencies),
            'Two Pair' : Conditions.two_pair(filtered_number_frequencies, filtered_suit_frequencies),
            'Three of a Kind' : Conditions.three_of_a_kind(filtered_number_frequencies, filtered_suit_frequencies),
            'Straight' : Conditions.straight(total_hand_numbers),
            'Full House' : Conditions.full_house(filtered_number_frequencies, filtered_suit_frequencies),
            'Flush' : Conditions.flush(filtered_suit_frequencies)
        }

        for w in win_conditions:
            output_str = w + ": "
            conditions_holds = win_conditions[w]
            if conditions_holds[1]:
                if type(conditions_holds[0]) == list or type(conditions_holds[0]) == tuple:
                    output_str += ', '.join(conditions_holds[0])
                else:
                    output_str += conditions_holds[0]
                print(output_str)
