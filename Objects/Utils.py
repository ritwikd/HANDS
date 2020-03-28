num_lookup = {
    'J' : 'Jack',
    'Q' : 'Queen',
    'K' : 'King',
    'A' : 'Ace'
}

suit_lookup = {
    'C' : 'Clubs',
    'D' : 'Diamonds',
    'H' : 'Hearts',
    'S' : 'Spades'
}

def card_to_verbose(card):
    verbose = ''
    num = card[0]
    suit = card[1]
    if num in list(num_lookup.keys()):
        verbose += num_lookup[num]
    else:
        verbose += num
    verbose += ' of ' + suit_lookup[suit]

    return verbose

def card_list_to_verbose(card_list):
    return list(map(card_to_verbose, card_list))

