num_lookup = {
    'T' : '10',
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

def get_numbers(card_list):
    return [card[0] for card in card_list]

def get_suits(card_list):
    return [card[1] for card in card_list]

def get_number_frequencies(numbers):
    return {i: numbers.count(i) for i in set(numbers)}

def get_suit_frequencies(suits):
    return {i: suits.count(i) for i in set(suits)}

def ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))