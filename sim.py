from Objects import Poker, Cards
from Objects.Utils import *

playing_deck = Cards.Deck()

game = Poker.Game(playing_deck)

hand = game.deal_hand()

print(card_list_to_verbose(hand))

game.deal_flop()

print(card_list_to_verbose(game.table))

game.deal_turn()

print(card_list_to_verbose(game.table))

game.deal_river()

print(card_list_to_verbose(game.table))