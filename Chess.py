# This may become a functioning version of chess

import numpy as np

## Pieces

black = {"Pawn" : "b", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }
white = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }

## Board

Board = np.full((8, 8), ' ')

# Placing pawns
Board[1, : ] = black['Pawn']
Board[6, : ] = white['Pawn']

# Placing Rooks
Board[0, 0] = black['Rook']


print(Board)
