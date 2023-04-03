# This may become a functioning version of chess

import numpy as np

### Board with peices placed

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

# Dictionaries containing the peices and their visualisations
black = {"Pawn" : "b", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" } 
white = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }

# Placing Pawns
Board[1, : ] = black['Pawn']
Board[6, : ] = white['Pawn']

# Placing Rooks
Board[0, 0] = black['Rook']
Board[0, 7] = black['Rook']

Board[7, 0] = white['Rook']
Board[7, 7] = white['Rook']

# Placing Knights
Board[0, 1] = black['Knight']
Board[0, 6] = black['Knight']

Board[7, 1] = white['Knight']
Board[7, 6] = white['Knight']

# Placing Bishops
Board[0, 2] = black['Bishop']
Board[0, 5] = black['Bishop']

Board[7, 2] = white['Bishop']
Board[7, 5] = white['Bishop']

# Placing Queens
Board[0, 3] = black['Queen']

Board[7, 3] = white['Queen']

# Placing Kings
Board[0, 4] = black['King']

Board[7, 4] = white['King']


print(Board)