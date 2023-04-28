# This may become a functioning version of chess

import numpy as np

### Variables

T = 0
print(T)

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
    global T
    
    # Resets turn ocelator
    T = 0

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
    Board[2 : 6, : ] = ' '
    
    
Board_Reset()
print(T)
print(Board)

### Piece moves

Index = {
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
        T = 1

    else:
        Turn = "Black's turn"
        T = 0
    
    print(Turn, '\n' 'Choose a piece and where to move it.')
    
    
    Move = input('Piece,current location,new location: ')
    Move = Move.split(',')
    Move_Old = ([*Move[1]])
    Move_New = ([*Move[2]])
    
    
    if T == 1 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in W.values():    
       
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in W.values():    
            
            if Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] == Pieces['White'][Move[0]]:
                # Removes piece from current location
                Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

                # Adds piece in new location
                Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['White'][Move[0]]
            
            else:
                T = 0
                raise Exeption('PieceError: Can not replace piece with another. Try again.')   
        else:
            T = 0
            raise Exception('MoveError: Can not take own pieces. Try again.')
   

    elif T == 0 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in B.values():
        
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in B.values():    
            
            if Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] == Pieces['White'][Move[0]]:
                # Removes piece from current location
                Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

                # Adds piece in new location
                Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['White'][Move[0]]
            
            else:
                T = 1
                raise Exeption('PieceError: Can not replace piece with another. Try again.')
        else:
            T = 1
            raise Exception('MoveError: Can not take own pieces. Try again.')
    else:
        if T == 0:
            T = 1
        else:
            T = 0
        raise Exception("MoveError: Can not move opponent's pieces. Try again.")

print(Board)

Board_Reset()