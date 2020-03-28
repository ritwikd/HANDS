from Objects import Poker, Cards
from Objects.Utils import *

playing_deck = Cards.Deck()

game = Poker.Game(playing_deck)

hand = game.deal_hand()

print("Hand:\t\t", ', '.join(card_list_to_verbose(hand)))

game.deal_flop()

game.deal_turn()

game.deal_river()

print("Table:\t\t", ', '.join(card_list_to_verbose(game.table)))

combined = card_list_to_verbose(hand) + card_list_to_verbose(game.table)

print("Combined:\t", ', '.join(combined))

print("\n\n")

game.check_hand(hand)