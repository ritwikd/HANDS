from Objects.Cards import *

def high_card(n):
    """Returns an int representing the highest card"""
    return True, max(n)


def one_pair(n):
    """Returns an int representing the highest pair"""
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) == 0:
        return False, None
    else:
        return True, max(pairs)


def two_pair(n):
    """Returns a tuple of two ints representing the two highest pairs"""
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
    """Returns an int representing the highest three of a kind"""
    threes = []
    for k in n:
        if n[k] == 3:
            threes.append(k)
    if len(threes) == 0:
        return False, None
    else:
        return True, max(threes)


def straight(n):
    """Returns an int representing the highest card value 
    of the highest straight"""
    numbers = []
    sub_sequences = []
    straight = []
    for k in n:
        numbers.append(k)  # adds all the unique values of cards available
    numbers.sort(reverse=True)  # puts them highest to lowest
    for i in range(len(numbers) - 4):
        sub_sequences.append(numbers[i:i + 5])
    for s in sub_sequences:
        straight_found = True
        for i in range(4):
            if s[i] - s[i + 1] != 1:
                straight_found = False
        if straight_found == True:
            straight = s
    if len(straight) == 0:
        return False, None
    else:
        return True, straight[0]


def flush(s):
    for k in s:
        if s[k] >= 5:
            return True, k
    return False, None


def full_house(n):
    if (one_pair(n)[0] == True & three_of_a_kind(n)[0] == True):
        if (one_pair(n)[1] != three_of_a_kind(n)[1]):
            return True, (one_pair(n)[1], three_of_a_kind(n)[1])
    return False, None


def four_of_a_kind(n):
    for k in n:
        if n[k] == 4:
            return True, k
    return False, None


def straight_flush(hand, board):
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

    for i in range(len(numbers_in_hand) - 5):
        starting_num = numbers_in_hand[i]
        is_potential_straight = numbers_in_hand[i:i + 5] == list(range(starting_num, starting_num + 5))
        if is_potential_straight:
            potential_straights.append(numbers_in_hand[i:i+5])

    straight_flushes = []

    if len(potential_straights) > 0:
        all_cards_in_suit = {suit : False for suit in suits}
        for i in range(len(potential_straights)):
            straight = potential_straights[i]
            for suit in suits:
                straight_flush = [suit in num_to_suit_map[num] for num in straight] == [True, True, True, True, True]
                if straight_flush:
                    straight_flushes.append([suit, potential_straights[i]])

        if straight_flushes != []:
            highest_straight_flush = straight_flushes[-1]
            return True, (highest_straight_flush[0], highest_straight_flush[1][-1])
        else:
            return False, None
    else:
        return False, None


def royal_flush(hand, board):
    is_flush, info = straight_flush(hand, board)
    if is_flush:
        if info[1] == 14:
            return True, info[0]
        else:
            return False, None
    else:
        return False, None