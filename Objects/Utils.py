from Objects.Cards import *


def show_hand(hand):
    print('Your hand:      ' +
          card_to_string(hand[0]) + '   ' +
          card_to_string(hand[1]))


def show_board(board):
    print("On the table:   " +
          card_to_string(board[0]) + '   ' +
          card_to_string(board[1]) + '   ' +
          card_to_string(board[2]) + '   ' +
          card_to_string(board[3]) + '   ' +
          card_to_string(board[4]))


def card_to_id(card):
    return faces[card[0]] + card[1]


def card_to_string(card):
    return "[" + faces[card[0]] + " of  " + card[1] + "]"
