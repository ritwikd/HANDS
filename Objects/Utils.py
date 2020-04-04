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