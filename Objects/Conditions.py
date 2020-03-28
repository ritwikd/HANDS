from Objects.Utils import *

def high_card(thn, n, s):
    to_numeric = {
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }

    to_card = {
        10 : 'T',
        11 : 'J',
        12 : 'Q',
        13 : 'K',
        14 : 'A'
    }

    numeric = []
    for c in thn:
        if c in to_numeric:
            numeric.append(to_numeric[c])
        else:
            numeric.append(int(c))
    r_mc = max(numeric)
    mc = None

    if r_mc in to_card:
        mc = to_card[r_mc]
    else:
        mc = str(r_mc)

    if len(n) == 0 and len(s) == 0:
        return (mc, True)
    else:
        return (None, False)

def pair(n, s):
    if len(n) == 1 and len(s) == 0:
        if n[0][1] == 2:
            return (n[0][0], True)
        else:
            return (None, False)
    else:
        return (None, False)

def two_pair(n, s):
    if len(n) == 2 and len(s) == 0:
        if n[0][1] == 2 and n[1][1] == 2:
            return ((n[0][0], n[1][0]), True)
        else:
            return (None, False)
    else:
        return (None, False)

def three_of_a_kind(n ,s):
    if len(n) == 1 and len(s) == 0:
        if n[0][1] == 3:
            return (n[0][0], True)
        else:
            return (None, False)
    else:
        return (None, False)

def straight(hand_numbers):
    to_numeric = {
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }

    to_card = {
        10 : 'T',
        11 : 'J',
        12 : 'Q',
        13 : 'K',
        14 : 'A'
    }

    no_copies = list(set(hand_numbers))
    if len(no_copies) < 5:
        return (None, False)
    numeric = []
    for n in no_copies:
        if n in to_numeric:
            numeric.append(to_numeric[n])
        else:
            numeric.append(int(n))

    potential_straights = []

    for card_range in ranges(numeric):
        if card_range[1] - card_range[0] >= 4:
            potential_straights.append(card_range)

    if len(potential_straights) == 0:
        return (None, False)

    best_straight = potential_straights[-1]
    ending_card = best_straight[-1]

    raw_straight_cards = reversed(list(range(ending_card, ending_card - 5, -1)))

    straight_cards = []
    for number in raw_straight_cards:
        if number in to_card:
            straight_cards.append(to_card[number])
        else:
            straight_cards.append(str(number))

    return (straight_cards, True)

def full_house(n, s):
    if len(n) == 2 and len(s) == 0:
        if n[0][1] == 2 and n[1][1] == 3 or n[0][1] == 3 and n[1][1] == 2:
            return ((n[0][0], n[1][0]), True)
        else:
            return (None, False)
    else:
        return (None, False)

def flush(s):
    if len(s) == 1:
        if s[0][1] >= 5:
            return (s[0][0], True)
        else:
            return (None, False)
    else:
        return (None, False)