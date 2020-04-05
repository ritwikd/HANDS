# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:16:42 2020
@author: Lagerstrom
"""

import random

from Objects.Cards import *
from Objects.Conditions import *
from Objects.Utils import *


def play_game(verbose=True):
    deck = init_deck()
    deck, hand = deal_hand(deck)
    if verbose: show_hand(hand)
    deck, board = deal_board(deck)
    if verbose: show_board(board)
    n = get_numbers(hand, board)
    s = get_suits(hand, board)
    if verbose: print("\n")

    high_check, y = high_card(n)
    if high_check == True:
        if verbose: print(face_string[y], "High")
    pair_check, y = one_pair(n)
    if pair_check == True:
        if verbose: print("Pair of " + face_string[y] + "s")
    two_pair_check, y = two_pair(n)
    if two_pair_check == True:
        if verbose: print("Two pair! " + face_string[y[0]] + "s and " + face_string[y[1]] + "s")
    three_check, y = three_of_a_kind(n)
    if three_check == True:
        if verbose: print("Three " + face_string[y] + "s!")
    straight_check, y = straight(hand, board)
    if straight_check == True:
        if verbose: print("Straight ending in " + face_string[y[0]] + "!")
    flush_check, y = flush(s)
    if flush_check == True:
        if verbose: print("Flush! Five " + y + "!")
    full_house_check, y = full_house(n)
    if full_house_check == True:
        if verbose: print("Full house: Two " + face_string[y[0]] + "s and three " + face_string[y[1]] + "s!")
    four_check, y = four_of_a_kind(n)
    if four_check == True:
        if verbose: print("**** FOUR OF A KIND: Four " + face_string[y] + "s ! ****")
    straight_flush_check, y = straight_flush(hand, board)
    if straight_flush_check == True:
        if verbose: print("***** STRAIGHT FLUSH ****: Straight flush ending in " + face_string[y])
#    royal_flush_check, y = royal_flush(hand, board)
#    if royal_flush_check == True:
#        print("***** ROYAL FLUSH ****: Straight flush of suit " + y + ".")
    if verbose: print(
        "----------------------------------------------------------------------------------------------------------")
        
    return(high_check, pair_check, two_pair_check, three_check,  straight_check, flush_check,
           full_house_check, four_check,  straight_flush_check)

checks = {'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0, 'straight': 0,
          'flush': 0, 'full_house': 0, 'four': 0, 'straight_flush' : 0}

num_deals = 10000

for i in range(num_deals):
    
    a, b, c, d, e, f, g, h, i = play_game(verbose=True)

    if h == True:
        checks['four'] += 1
    if a == True:
        checks['high'] += 1
    if b == True:
        checks['pair'] += 1 
    if c == True:
        checks['two_pair'] += 1
    if d == True:
        checks['three'] += 1
    if e == True:
        checks['straight'] += 1
    if f == True:
        checks['flush'] += 1
    if g == True:
        checks['full_house'] += 1
    if h == True:
        checks['four'] += 1
    if i == True:
        checks['straight_flush'] += 1
#    if j == True:
#        checks['royal_flush'] += 1
        
print("Below is the count of each hand that could have been played in " + str(num_deals) + " deals")   
print(checks)