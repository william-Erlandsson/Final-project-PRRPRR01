# This may become a functioning version of chess

import numpy as np

### Variables

T = 0

### Board with peices placed

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

# Dictionaries containing the peices and their visualisations on the board
Pieces = {
    'Black' : {
        "pawn" : "p", "rook" : "♜", "knight" : "♞", "bishop" : "♝", "king" : "♚", "queen" : "♛"     
    },
    'White' : {
        "pawn" : "♙", "rook" : "♖", "knight" : "♘", "bishop" : "♗", "King" : "♔", "Queen" : "♕" 
    }
}


def Board_Reset():
    """resets the board with pieces in their original positions and resets the turn ocelator"""
    
    # Resets turn ocelator
    global T
    T = 0

    # Places Pawns
    Board[1, : ] = Pieces['Black']['Pawn']
    Board[6, : ] = Pieces['White']['Pawn']

    # Places Rooks
    Board[0, 0] = Pieces['Black']['Rook']
    Board[0, 7] = Pieces['Black']['Rook']

    Board[7, 0] = Pieces['White']['Rook']
    Board[7, 7] = Pieces['White']['Rook']

    # Places Knights
    Board[0, 1] = Pieces['Black']['Knight']
    Board[0, 6] = Pieces['Black']['Knight']

    Board[7, 1] = Pieces['White']['Knight']
    Board[7, 6] = Pieces['White']['Knight']

    # Places Bishops
    Board[0, 2] = Pieces['Black']['Bishop']
    Board[0, 5] = Pieces['Black']['Bishop']

    Board[7, 2] = Pieces['White']['Bishop']
    Board[7, 5] = Pieces['White']['Bishop']

    # Places Queens
    Board[0, 3] = Pieces['Black']['Queen']

    Board[7, 3] = Pieces['White']['Queen']

    # Places Kings
    Board[0, 4] = Pieces['Black']['King']

    Board[7, 4] = Pieces['White']['King']

    # Remoes pieces in the center of the board
    Board[2 : 6, : ] = ' '
    
    
Board_Reset()

print(Board) # Prints the board

### Piece moves

# A nested dictionary to translate the inputted koordinates to indexes in the array "Board"
Index = {
    'x' : {
        'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7
    },
    'y' : {
        '1' : 7, '2' : 6, '3' : 5, '4' : 4, '5' : 3, '6' : 2, '7' : 1, '8' : 0
    }
}

W = Pieces['White'] # Isolates the dictionary with the white pieces
B = Pieces['Black'] # Isolates the dictionary with the black pieces


for i in range(10): # Will be turned into a while loop in the future
    
    if T == 0:                          #
                                        #
        Turn = "White's turn"           #
        T = 1                           #
                                        #   Turn ocelator
    else:                               #
                                        #
        Turn = "Black's turn"           #
        T = 0                           #
    
    print(Turn, '\n' 'Choose a piece and where to move it.')
    Move = input('Piece,current location,new location: ') # Takes player input for what move to make
    
    Move = Move.split(',')  # Splits the input into a list with three elements
    
    Move_Old = ([*Move[1]]) # Makes a list of the current location of the selected piece
    Move_New = ([*Move[2]]) # Makes a list of the new location of the selected piece
    
    
    # Checks if it is white's turn and the piece to be moved also is white
    if T == 1 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in W.values(): 
        
        # Checks if the new piece location is occupied by another white piece
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in W.values():    
            
            # Checks if the piece to be moved is the same as the piece stated in the move input
            if Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] == Pieces['White'][Move[0]]:
                
                # Removes piece from it's current location
                Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

                # Places piece at it's new location
                Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['White'][Move[0]]
            
            else:
                
                T = 0 # Gives white another chance to make a move
                raise Exeption('PieceError: Can not replace piece with another. Try again.')   
        
        else:
            
            T = 0 # Gives white another chance to make a move
            raise Exception('MoveError: Can not take own pieces. Try again.')
   
    # Checks if it is black's turn and the piece to be moved also is black
    elif T == 0 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in B.values():
        
        # Checks if the new piece location is occupied by another white piece
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in B.values():    
            
            # Checks if the piece to be moved is the same as the piece stated in the move input
            if Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] == Pieces['White'][Move[0]]:
                
                # Removes piece from current location
                Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

                # Adds piece in new location
                Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['White'][Move[0]]
            
            else:
                
                T = 1 # Gives black another chance to make a move
                raise Exeption('PieceError: Can not replace piece with another. Try again.')
        
        else:
            
            T = 1 # Gives black another chance to make a move
            raise Exception('MoveError: Can not take own pieces. Try again.')
    
    else:
        
        if T == 0:            #
                              #
            T = 1             #
                              #   Gives the players their turn back
        else:                 #
                              #
            T = 0             #
        
        raise Exception("MoveError: Can only move own pieces. Try again.")


print(Board) # Prints the board 

### Legal move detection

#### Detecting the legal moves for each piece with the exception of special moves (i.e castle, pawn promotion and en pasant).
