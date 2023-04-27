# This may become a functioning version of chess

import numpy as np

### Variables

T = 0

### Board with peices placed

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

# Dictionaries containing the peices and their visualisations

Pieces = {
    'Black' : {
        "Pawn" : "p", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛"     
    },
    'White' : {
        "Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" 
    }
}

def Board_Reset():
    """resets the board with pieces in their original positions and resets the turn ocelator"""
    
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

    # Removing peices in the center of the board
    Board[2 : 5, : ] = ' '
    
    # Resets turn ocelator
    T = 0
    
Board_Reset()

print(Board)

### Piece moves

Board_index = {
    'x' : {
        'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7
    },
    'y' : {
        '1' : 7, '2' : 6, '3' : 5, '4' : 4, '5' : 3, '6' : 2, '7' : 1, '8' : 0
    }
}

W = Pieces['White']
B = Pieces['Black']

for i in range(1): # Will be turned into a while loop in the future
    if T == 0:
        Turn = "White's turn"
        Turncol = 'White'
        T = 1

    else:
        Turn = "Black's turn"
        Turncol = 'Black'
        T = 0
    
    print(Turn, '\n' 'Choose a piece and where to move it.')
    
    
    Move = input('piece,current location,new location: ')
    Move = Move.split(',')
    Move_Old = ([*Move[1]])
    Move_New = ([*Move[2]])
    
    print(Board[Board_index['y'][Move_New[1]], Board_index['x'][Move_New[0]]])
    
    if ((T == 0) and (Board[Board_index['y'][Move_Old[0]], Board_index['x'][Move_Old[1]]] in W.values())):
            print('success')
    
    # Removes piece from current location
    Board[Board_index['y'][Move_Old[1]], Board_index['x'][Move_Old[0]]] = ' '

    # Adds piece in new location
    Board[Board_index['y'][Move_New[1]], Board_index['x'][Move_New[0]]] = Pieces[TurnCol][Move[0]]

    print(Board)

Board_Reset()