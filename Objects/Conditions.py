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
    return True, max(pairs)


def two_pair(n):
    """Returns a tuple of two ints representing the two highest pairs"""
    pairs = []
    for k in n:
        if n[k] == 2:
            pairs.append(k)
    if len(pairs) < 2:
        return False, None
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
    
    
def straight(hand, board):
    """Returns an int representing the highest card value 
    of the highest straight and a boolean about whether it's also a flush"""
    suits = {}
    numbers = []
    sequences = []
    straights = []
    flush = False
    
    # Populates suits (a dictionary) where the keys are the four suits and the
    # values are lists of card values in that suit
    for card in hand + board:
        if card[1] not in suits:
            suits[card[1]] = [card[0]]
        else:
            suits[card[1]].append(card[0])
    
    # Populates numbers, a list of all the unique card values in the hand    
    for s in suits:
        for i in suits[s]:
            if i not in numbers:
                numbers.append(i) 
                
    # Sorts the list of unique numbers highest to lowest
    numbers.sort(reverse = True)
    
    # Populates sequences, a list of five-value sequences
    for i in range(len(numbers) - 4):
        seq = []
        for j in range(5):
            seq.append(numbers[i + j])
        sequences.append(seq)
        
    # Checks whether each sequence is a straight, and if it is, adds it to straights
    for z in sequences:
        potential_straight = True
        for i in range(4):
            if z[i] - z[i + 1] != 1:
                potential_straight = False
        if potential_straight:
            straights.append(z)
    
    # If no straights have been found, quit
    if len(straights) == 0:
        return False, (None, False)
    
    # Checks whether each straight can be made from all cards of the same suit
    # If so, then we have a straight flush
    for s in suits:
        for v in straights:
            if v[0] in suits[s] and v[1] in suits[s] and v[2] in suits[s] and v[3] in suits[s] and v[4] in suits[s]:
                flush = True
                
    # Straights[0][0] is the straight ending in the highest card
    # If it's Ace and flush == true, then it's a royal flush
    return True, (straights[0][0], flush)

        
def flush(s):
    for k in s:
        if s[k] >= 5:
            return True, k
    return False, None


def full_house(n):
    if one_pair(n)[0] & three_of_a_kind(n)[0]:
        if one_pair(n)[1] != three_of_a_kind(n)[1]:
            return True, (one_pair(n)[1], three_of_a_kind(n)[1])
    return False, None


def four_of_a_kind(n):
    for k in n:
        if n[k] == 4:
            return True, k
    return False, None


def straight_flush(hand, board):
    is_straight, y = straight(hand, board)
    if is_straight and y[0] != 14 and y[1] == True:
        return True, y[0]
    return False, None


def royal_flush(hand, board):
    is_straight, y = straight(hand, board)
    if is_straight and y[0] == 14 and y[1] == True:
        return True, y[0]
    return False, None
     
