# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:16:42 2020

@author: Lagerstrom, Dutta
"""

# Deck creation, manipulation, and drawing
from Objects.Cards import init_deck, remove_card, deal_flop
from Objects.Cards import deal_turn, deal_river, deal_hand

# Card list analysis
from Objects.Cards import get_numbers, get_suits

# Win condition checking
from Objects.Conditions import high_card, one_pair, two_pair, three_of_a_kind
from Objects.Conditions import four_of_a_kind, full_house, flush, straight
from Objects.Conditions import royal_flush, straight_flush


def best_hand(hand, board):
    """Get best hand and win condition from given hand board."""
    stats = ()

    n = get_numbers(hand, board)
    s = get_suits(hand, board)
    high_check, high_result = high_card(n)
    pair_check, pair_result = one_pair(n)
    two_pair_check, two_pair_result = two_pair(n)
    three_check, three_result = three_of_a_kind(n)
    straight_check, straight_result = straight(n)
    flush_check, flush_result = flush(s)
    full_house_check, full_house_result = full_house(n)
    four_check, four_result = four_of_a_kind(n)
    straight_flush_check, straight_flush_result = straight_flush(
        hand, board)
    royal_flush_check, royal_flush_result = royal_flush(hand, board)

    if royal_flush_check:
        stats = ('royal_flush', royal_flush_result)
    elif straight_flush_check:
        stats = ('straight_flush', straight_flush_result)
    elif four_check:
        stats = ('four', four_result)
    elif full_house_check:
        stats = ('full_house', full_house_result)
    elif flush_check:
        stats = ('flush', flush_result)
    elif straight_check:
        stats = ('straight', straight_result)
    elif three_check:
        stats = ('three', three_result)
    elif two_pair_check:
        stats = ('two_pair', two_pair_result)
    elif pair_check:
        stats = ('pair', pair_result)
    elif high_check:
        stats = ('high', high_result)

    return stats


def simulate_hand_probability(hand, runs, initial_board=None):
    """Get probabilities of each condition being your best condition
        with the given hand and board, including simulating a flop,
        turn, or river as required."""
    to_test = {
        'flop': False,
        'turn': False,
        'river': False,
    }
    if not initial_board:
        initial_board = []
        to_test = {
            'flop': True,
            'turn': True,
            'river': True,
        }
    elif len(initial_board) == 3:
        to_test['turn'] = True
        to_test['river'] = True
    elif len(initial_board) == 4:
        to_test['river'] = True

    stats = {
        'flop': {'total': 0, 'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0,
                 'straight': 0, 'flush': 0, 'full_house': 0, 'four': 0,
                 'straight_flush': 0, 'royal_flush': 0},
        'turn': {'total': 0, 'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0,
                 'straight': 0, 'flush': 0, 'full_house': 0, 'four': 0,
                 'straight_flush': 0, 'royal_flush': 0},
        'river': {'total': 0, 'high': 0, 'pair': 0, 'two_pair': 0, 'three': 0,
                  'straight': 0, 'flush': 0, 'full_house': 0, 'four': 0,
                  'straight_flush': 0, 'royal_flush': 0}
    }

    for i in range(runs):
        sim_deck = init_deck()
        sim_board = initial_board.copy()
        for card in hand + sim_board:
            sim_deck = remove_card(sim_deck, card)

        if to_test['flop']:
            # Flop Test
            sim_deck, sim_board = deal_flop(sim_deck, sim_board)
            n = get_numbers(hand, sim_board)
            s = get_suits(hand, sim_board)

            stats['flop']['total'] += 1

            high_check, high_result = high_card(n)
            pair_check, pair_result = one_pair(n)
            two_pair_check, two_pair_result = two_pair(n)
            three_check, three_result = three_of_a_kind(n)
            straight_check, straight_result = straight(n)
            flush_check, flush_result = flush(s)
            full_house_check, full_house_result = full_house(n)
            four_check, four_result = four_of_a_kind(n)
            straight_flush_check, straight_flush_result = straight_flush(
                hand, sim_board)
            royal_flush_check, royal_flush_result = royal_flush(hand, sim_board)

            if royal_flush_check:
                stats['flop']['royal_flush'] += 1
            elif straight_flush_check:
                stats['flop']['straight_flush'] += 1
            elif four_check:
                stats['flop']['four'] += 1
            elif full_house_check:
                stats['flop']['full_house'] += 1
            elif flush_check:
                stats['flop']['flush'] += 1
            elif straight_check:
                stats['flop']['straight'] += 1
            elif three_check:
                stats['flop']['three'] += 1
            elif two_pair_check:
                stats['flop']['two_pair'] += 1
            elif pair_check:
                stats['flop']['pair'] += 1
            elif high_check:
                stats['flop']['high'] += 1

        if to_test['turn']:
            # Turn Test
            sim_deck, sim_board = deal_turn(sim_deck, sim_board)
            n = get_numbers(hand, sim_board)
            s = get_suits(hand, sim_board)

            stats['turn']['total'] += 1

            high_check, high_result = high_card(n)
            pair_check, pair_result = one_pair(n)
            two_pair_check, two_pair_result = two_pair(n)
            three_check, three_result = three_of_a_kind(n)
            straight_check, straight_result = straight(n)
            flush_check, flush_result = flush(s)
            full_house_check, full_house_result = full_house(n)
            four_check, four_result = four_of_a_kind(n)
            straight_flush_check, straight_flush_result = straight_flush(
                hand, sim_board)
            royal_flush_check, royal_flush_result = royal_flush(hand, sim_board)

            if royal_flush_check:
                stats['turn']['royal_flush'] += 1
            elif straight_flush_check:
                stats['turn']['straight_flush'] += 1
            elif four_check:
                stats['turn']['four'] += 1
            elif full_house_check:
                stats['turn']['full_house'] += 1
            elif flush_check:
                stats['turn']['flush'] += 1
            elif straight_check:
                stats['turn']['straight'] += 1
            elif three_check:
                stats['turn']['three'] += 1
            elif two_pair_check:
                stats['turn']['two_pair'] += 1
            elif pair_check:
                stats['turn']['pair'] += 1
            elif high_check:
                stats['turn']['high'] += 1

        if to_test['river']:
            # River Test
            sim_deck, sim_board = deal_river(sim_deck, sim_board)
            n = get_numbers(hand, sim_board)
            s = get_suits(hand, sim_board)

            stats['river']['total'] += 1

            high_check, high_result = high_card(n)
            pair_check, pair_result = one_pair(n)
            two_pair_check, two_pair_result = two_pair(n)
            three_check, three_result = three_of_a_kind(n)
            straight_check, straight_result = straight(n)
            flush_check, flush_result = flush(s)
            full_house_check, full_house_result = full_house(n)
            four_check, four_result = four_of_a_kind(n)
            straight_flush_check, straight_flush_result = straight_flush(
                hand, sim_board)
            royal_flush_check, royal_flush_result = royal_flush(hand, sim_board)

            if royal_flush_check:
                stats['river']['royal_flush'] += 1
            elif straight_flush_check:
                stats['river']['straight_flush'] += 1
            elif four_check:
                stats['river']['four'] += 1
            elif full_house_check:
                stats['river']['full_house'] += 1
            elif flush_check:
                stats['river']['flush'] += 1
            elif straight_check:
                stats['river']['straight'] += 1
            elif three_check:
                stats['river']['three'] += 1
            elif two_pair_check:
                stats['river']['two_pair'] += 1
            elif pair_check:
                stats['river']['pair'] += 1
            elif high_check:
                stats['river']['high'] += 1

    for step in stats:
        if to_test[step]:
            for outcome in stats[step]:
                if outcome != 'total':
                    stats[step][outcome] = stats[step][outcome] / \
                                           float(stats[step]['total'])

    return stats
