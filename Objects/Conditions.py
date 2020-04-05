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
    
    
def straight(hand, board):
    """Returns an int representing the highest card value 
    of the highest straight"""
    suits = {}
    numbers = []
    sequences = []
    straights = []
    flush = False
    
    for card in hand + board:
        if card[1] not in suits:
            suits[card[1]] = [card[0]]
        else:
            suits[card[1]].append(card[0])
            
    print(suits)
            
    for s in suits:
        for i in suits[s]:
            if i not in numbers:
                numbers.append(i) 
                
    numbers.sort(reverse = True)
    
    for i in range(len(numbers) - 4):
        seq = []
        for j in range(5):
            seq.append(numbers[i + j])
        sequences.append(seq)
        
    for z in sequences:
        potential_straight = True
        for i in range(4):
            if z[i] - z[i + 1] != 1:
                potential_straight = False
        if potential_straight:
            straights.append(z)
            
    if len(straights) == 0:
        return False, (None, None)
    
    for s in suits:
        for v in straights:
            if v[0] in suits[s] and v[1] in suits[s] and v[2] in suits[s] and v[3] in suits[s] and v[4] in suits[s]:
                flush = True
                
    return True, (straights[0][0], flush)

        
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
    x, y = straight(hand, board)
    if y[1] == True:
        return True, y[0]
    else:
        return False, None


#def royal_flush(hand, board):
#    is_flush, info = straight_flush(hand, board)
#    if is_flush:
#        if info[1] == 14:
#            return True, info[0]
#        else:
#            return False, None
#    else:
#        return False, None