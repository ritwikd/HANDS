import random

from Objects.Utils import *

# Aces high!
faces = {2: '2 ', 3: '3 ', 4: '4 ', 5: '5 ',
         6: '6 ', 7: '7 ', 8: '8 ', 9: '9 ', 10: '10',
         11: 'J ', 12: 'Q ', 13: 'K ', 14: 'A '}

face_string = {2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
               6: 'Six', 7: "Seven", 8: 'Eight', 9: 'Nine', 10: 'Ten',
               11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

suits = ['♠', '♦', '♥', '♣']

suit_letter_to_string_map = {
    'S': '♠',
    'D': '♦',
    'H': '♥',
    'C': '♣'
}

suit_string = ['Spades', 'Diamonds', 'Hearts', 'Clubs']


def init_deck():
    deck = []
    for f in faces:
        for s in suits:
            deck.append((f, s))
    random.shuffle(deck)
    return deck


def remove_card(deck, card):
    card_index = deck.index(card)
    del deck[card_index]
    return deck


def deal_hand(deck):
    hand = [deck.pop(), deck.pop()]
    return deck, hand


def deal_board(deck):
    board = []
    deal_flop(deck, board)
    deal_turn(deck, board)
    deal_river(deck, board)
    return deck, board


def deal_flop(deck, board):
    deck.pop()
    for i in range(3):
        board.append(deck.pop())
    return deck, board


def deal_turn(deck, board):
    deck.pop()
    board.append(deck.pop())
    return deck, board


def deal_river(deck, board):
    deck.pop()
    board.append(deck.pop())
    return deck, board


def get_numbers(hand, board):
    """
    Returns a dictionary where the keys are the numerical values (Jack = 11)
    and the entries are the count of each value in the hand and board
    """
    numbers = {}
    for card in hand + board:
        if card[0] in numbers:
            numbers[card[0]] += 1
        else:
            numbers[card[0]] = 1
    return numbers


def get_suits(hand, board):
    """
    Returns a dictionary where the keys are the suits
    and the entries are the count of each suit in the hand and board
    """
    suits = {}
    for card in hand + board:
        if card[1] in suits:
            suits[card[1]] += 1
        else:
            suits[card[1]] = 1
    return suits
