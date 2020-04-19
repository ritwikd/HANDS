"""
All conditions take n, s, or card and baord.
n is get numbers, a dictionary of numbers to counts in the deck and board
s is set suits, a dictionary with the count of the suits

Returns a tuple for which the first element is T or F, the rest are points of interest.
"""


def high_card(n):
    return (True, max(n))


def one_pair(n):
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) > 0:
        return (True, max(pairs))
    return (False, None)


def two_pair(n):
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) >= 2:
        pairs.sort()
        return (True, pairs.pop(), pairs.pop())
    return (False, None)


def three_of_a_kind(n):
    threes = []
    for k in n:
        if n[k] == 3:
            threes.append(k)
    if len(threes) > 0:
        return (True, max(threes))
    return (False, None)
        
    
def straight(hand, board):
    suits = {}
    numbers = [] 
    for card in hand + board:
        if card[1] not in suits:
            suits[card[1]] = [card[0]]
        else:
            suits[card[1]].append(card[0])
        if card[0] not in numbers:
            numbers.append(card[0])
    numbers.sort(reverse = True)
    windows = []
    for r in range(len(numbers) - 4):
        window = []
        for f in range(5):
            window.append(numbers[r + f])
        windows.append(window)  
    straights = []        
    for w in windows:
        potential = True
        for i in range(4):
            if w[i] - w[i + 1] != 1:
                potential = False
        if potential == True:
            straights.append(w)  
    flush = False
    flush_suit = ''
    if len(straights) > 0:
        for s in suits:
            for v in straights:
                if v[0] in suits[s] and v[1] in suits[s] and v[2] in suits[s] and v[3] in suits[s] and v[4] in suits[s]:
                    flush = True
                    flush_suit = s
        return (True, straights[0][0], flush, flush_suit)
    return (False, None)

        
def flush(s):
    for k in s:
        if s[k] >= 5:
            return (True, k)
    return (False, None)


def full_house(n):
    if one_pair(n)[0] & three_of_a_kind(n)[0]:
        if one_pair(n)[1] != three_of_a_kind(n)[1]:
            return (True, one_pair(n)[1], three_of_a_kind(n)[1])
    return (False, None)


def four_of_a_kind(n):
    for k in n:
        if n[k] == 4:
            return (True, k)
    return (False, None)


def straight_flush(hand, board):
    y = straight(hand, board)
    if y[0] and y[1] != 14 and y[2]:
        return (True, y[1], y[3])
    return (False, None)


def royal_flush(hand, board):
    y = straight(hand, board)
    if y[0] and y[1] == 14 and y[2]:
        return (True, y[1], y[3])
    return (False, None)
     