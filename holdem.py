# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:16:42 2020
@author: Lagerstrom
"""


from Objects.Cards import *
from Objects.Conditions import *


def play_game(verbose=True):
    print("------------------------------------------------------------------")
    
    deck = init_deck()
    deck, hand = deal_hand(deck)
    deck, board = deal_board(deck)
    
    n = get_numbers(hand, board)
    s = get_suits(hand, board)
    
    if verbose: 
        show_board(board)
        show_hand(hand)
        print("\n")
    
    return(high_card(n), one_pair(n), two_pair(n), three_of_a_kind(n),
           straight(hand, board), flush(s), full_house(n), 
           four_of_a_kind(n),  straight_flush(hand, board), royal_flush(hand, board))

checks = {'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0, 'straight': 0,
          'flush': 0, 'full_house': 0, 'four': 0, 'straight_flush': 0, 'royal_flush': 0}

num_deals = 1000

for i in range(num_deals):
    
    a, b, c, d, e, f, g, h, i, j = play_game()

    if a[0] == True:
        checks['high'] += 1
        print(face_string[a[1]] + " High")
        
    if b[0] == True:
        checks['pair'] += 1 
        print("Pair of " + face_string[b[1]] + "s")
        
    if c[0] == True:
        checks['two_pair'] += 1
        print("Two pair! " + face_string[c[1]] + "s and " + face_string[c[2]] + "s")
        
    if d[0] == True:
        checks['three'] += 1
        print("Three " + face_string[d[1]] + "s!")
        
    if e[0] == True:
        checks['straight'] += 1
        print("Straight ending in " + face_string[e[1]] + "!")
        
    if f[0] == True:
        checks['flush'] += 1
        print("Flush! Five " + f[1] + "!")
        
    if g[0] == True:
        checks['full_house'] += 1
        print("Full house: Two " + face_string[g[1]] + "s and three " + face_string[g[2]] + "s!")
        
    if h[0] == True:
        checks['four'] += 1
        print("* FOUR OF A KIND: Four " + face_string[h[1]] + "s! *")
        
    if i[0] == True:
        checks['straight_flush'] += 1
        print("** STRAIGHT FLUSH **: Straight flush of suit " + i[2] + " ending in " + face_string[i[1]])
        
    if j[0] == True:
        checks['royal_flush'] += 1
        print("*** ROYAL FLUSH ***: Straight flush of suit " + j[2] + " ending in  " + face_string[j[1]] + ".")
        
print("Below is the count of each hand that could have been played in " + str(num_deals) + " deals")   
print(checks)
