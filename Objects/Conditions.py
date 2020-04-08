# -*- coding: utf-8 -*-
from Objects.Cards import *


def high_card(n):
    """Return number representing highest card"""
    return True, max(n)


def one_pair(n):
    """Return if pair exists and card number of highest pair if so."""
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) == 0:
        return False, None
    else:
        return True, max(pairs)


def two_pair(n):
    """Returns if two pair exists and highest two pairs if so."""
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) < 2:
        return False, None
    else:
        pairs.sort()
        return True, (pairs.pop(), pairs.pop())


def three_of_a_kind(n):
    """Return if three-of-a-kind exists and card number of highest triplet if so."""
    threes = []
    for k in n:
        if n[k] == 3:
            threes.append(k)
    if len(threes) == 0:
        return False, None
    else:
        return True, max(threes)


def straight(n):
    """Return if a straight exists and card number of the last card in the highest straight if so."""
    numbers = []
    sub_sequences = []
    best_straight = []
    for k in n:
        numbers.append(k)  # Get all unique card numbers
    numbers.sort(reverse=True)  # Sort in descending order
    for i in range(len(numbers) - 4):
        sub_sequences.append(numbers[i:i + 5])
    for s in sub_sequences:
        straight_found = True
        for i in range(4):
            if s[i] - s[i + 1] != 1:
                straight_found = False
        if straight_found:
            best_straight = s
    if len(best_straight) == 0:
        return False, None
    else:
        return True, best_straight


def flush(s):
    """Return if a flush exists and suit of the flush if so."""
    for k in s:
        if s[k] >= 5:
            return True, k
    return False, None


def full_house(n):
    """Return if a full house exists and card numbers of the highest pair and highest triplet if so."""
    if one_pair(n)[0] and three_of_a_kind(n)[0]:
        if one_pair(n)[1] != three_of_a_kind(n)[1]:
            return True, (one_pair(n)[1], three_of_a_kind(n)[1])
    return False, None


def four_of_a_kind(n):
    """Return if a four-of-a-kind exists and card number of the highest four-of-a-kind if so."""
    for k in n:
        if n[k] == 4:
            return True, k
    return False, None


def straight_flush(hand, board):
    """Return if a straight flush exists and number and suit of the last card in the highest straight flush if so."""
    combined = hand + board

    num_to_suit_map = {}
    for card in combined:
        if card[0] not in num_to_suit_map:
            num_to_suit_map[card[0]] = [card[1]]
        else:
            num_to_suit_map[card[0]].append(card[1])

    numbers_in_hand = sorted(list(set(list(num_to_suit_map.keys()))))
    if len(numbers_in_hand) < 5:
        return False, None

    potential_straights = []

    for i in range(len(numbers_in_hand) - 4):
        starting_num = numbers_in_hand[i]
        is_potential_straight = numbers_in_hand[i:i + 5] == list(range(starting_num, starting_num + 5))
        if is_potential_straight:
            potential_straights.append(numbers_in_hand[i:i + 5])

    straight_flushes = []

    if len(potential_straights) > 0:
        for i in range(len(potential_straights)):
            best_straight = potential_straights[i]
            for suit in suits:
                best_straight_flush = [suit in num_to_suit_map[num] for num in best_straight] == [True, True, True, True, True]
                if best_straight_flush:
                    straight_flushes.append([suit, potential_straights[i]])

        if straight_flushes:
            highest_straight_flush = straight_flushes[-1]
            return True, highest_straight_flush
        else:
            return False, None
    else:
        return False, None


def royal_flush(hand, board):
    """Return if a royal flush exists and return card number (always 14) and suit of the royal flush if so."""
    is_straight_flush, s_f = straight_flush(hand, board)
    if is_straight_flush:
        if s_f[1][-1] == 14:
            return True, s_f
        else:
            return False, None
    else:
        return False, None
