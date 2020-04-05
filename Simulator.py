# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:16:42 2020

@author: Lagerstrom
"""

import random,json

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
    straight_check, y = straight(n)
    if straight_check == True:
        if verbose: print("Straight ending in " + face_string[y] + "!")
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
        if verbose: print(
            "***** STRAIGHT FLUSH ****: Straight flush of suit " + y[0] + " ending in " + face_string[y[1]])
    royal_flush_check, y = royal_flush(hand, board)
    if royal_flush_check == True:
        print("***** ROYAL FLUSH ****: Straight flush of suit " + y + ".")
    if verbose: print(
        "----------------------------------------------------------------------------------------------------------")

    return (hand,high_check, pair_check, two_pair_check, three_check, straight_check, flush_check,
            full_house_check, four_check, straight_flush_check, royal_flush_check)


checks = {'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0, 'straight': 0,
          'flush': 0, 'full_house': 0, 'four': 0, 'straight_flush': 0, 'royal_flush': 0}

num_deals = 1000000

hand_probabilities = {}

for i in range(num_deals):

    hand, a, b, c, d, e, f, g, h, i, j = play_game(verbose=False)
    hand_id = faces[hand[0][0]] + hand[0][1] + '|' + faces[hand[1][0]] + hand[1][1]
    if hand_id not in hand_probabilities:
        hand_probabilities[hand_id] = {'total' : 0, 'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0, 'straight': 0,
          'flush': 0, 'full_house': 0, 'four': 0, 'straight_flush': 0, 'royal_flush': 0}

    hand_probabilities[hand_id]['total'] += 1

    if j:
        hand_probabilities[hand_id]['royal_flush'] += 1
    elif i:
        hand_probabilities[hand_id]['straight_flush'] += 1
    elif h:
        hand_probabilities[hand_id]['four'] += 1
    elif g:
        hand_probabilities[hand_id]['full_house'] += 1
    elif f:
        hand_probabilities[hand_id]['flush'] += 1
    elif e:
        hand_probabilities[hand_id]['straight'] += 1
    elif d:
        hand_probabilities[hand_id]['three'] += 1
    elif c:
        hand_probabilities[hand_id]['two_pair'] += 1
    elif b:
        hand_probabilities[hand_id]['pair'] += 1
    elif a:
        hand_probabilities[hand_id]['high'] += 1

for hand in hand_probabilities:
    for outcome in hand_probabilities[hand]:
        if outcome != 'total':
            hand_probabilities[hand][outcome] = round(hand_probabilities[hand][outcome]/float(hand_probabilities[hand]['total']), 3)

for hand in hand_probabilities:
    print(hand, hand_probabilities[hand])

with open('card-probabilities.json', 'w') as file_handler:
    json.dump(hand_probabilities, file_handler)