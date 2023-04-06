# This may become a functioning version of chess

import numpy as np

### Variables

T = 0

### Board with peices placed

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

# Nested dictionaries containing the peices and their visualisations
Pieces = {
    'Black' : {
        "Pawn" : "b", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" 
    }, 
    'White' : {
        "Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" 
    }
}

# Placing Pawns
Board[1, : ] = Pieces['Black']['Pawn']
Board[6, : ] = Pieces['White']['Pawn']

# Placing Rooks
Board[0, 0] = Pieces['Black']['Rook']
Board[0, 7] = Pieces['Black']['Rook']

Board[7, 0] = Pieces['White']['Rook']
Board[7, 7] = Pieces['White']['Rook']

# Placing Knights
Board[0, 1] = Pieces['Black']['Knight']
Board[0, 6] = Pieces['Black']['Knight']

Board[7, 1] = Pieces['White']['Knight']
Board[7, 6] = Pieces['White']['Knight']

# Placing Bishops
Board[0, 2] = Pieces['Black']['Bishop']
Board[0, 5] = Pieces['Black']['Bishop']

Board[7, 2] = Pieces['White']['Bishop']
Board[7, 5] = Pieces['White']['Bishop']

# Placing Queens
Board[0, 3] = Pieces['Black']['Queen']

Board[7, 3] = Pieces['White']['Queen']

# Placing Kings
Board[0, 4] = Pieces['Black']['King']

Board[7, 4] = Pieces['White']['King']


print(Board)

### Turn ocelator

for i in range(10):
    if T % 2 == 0:
        Turn = 'White'

    else:
        Turn = 'Black'
    
    T += 1
    print(Turn)

### Piece moves

print('Choose a piece and where to move it.')
Move = [input('piece, move')]
print(Move)