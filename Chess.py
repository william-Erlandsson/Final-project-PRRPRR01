# This may become a functioning version of chess

### Libraries

import numpy as np

### Variables

T = 0

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

Last_Move = []

### Dictionaries

# Dictionaries containing the peices and their visualisations on the board
Pieces = {
    'Black' : {
        "pawn" : "p", "rook" : "♜", "knight" : "♞", "bishop" : "♝", "king" : "♚", "queen" : "♛"     
    },
    'White' : {
        "pawn" : "♙", "rook" : "♖", "knight" : "♘", "bishop" : "♗", "king" : "♔", "queen" : "♕" 
    }
}


# A nested dictionary to translate the inputted koordinates to indexes in the array "Board"
Index = {
    'x' : {
        "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
    },
    'y' : {
        "1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0
    }
}

W = Pieces['White'] # Isolates the dictionary with the white pieces
B = Pieces['Black'] # Isolates the dictionary with the black pieces

### Functions

#### Board_Reset

def Board_Reset():
    """Resets the board with pieces in their original positions and resets the turn ocelator"""

    # Resets turn ocelator
    global T
    T = 0

    global Last_Move
    Last_Move = []

    # Places Pawns
    Board[1, : ] = Pieces['Black']['pawn']
    Board[6, : ] = Pieces['White']['pawn']

    # Places Rooks
    Board[0, 0] = Pieces['Black']['rook']
    Board[0, 7] = Pieces['Black']['rook']

    Board[7, 0] = Pieces['White']['rook']
    Board[7, 7] = Pieces['White']['rook']

    # Places Knights
    Board[0, 1] = Pieces['Black']['knight']
    Board[0, 6] = Pieces['Black']['knight']

    Board[7, 1] = Pieces['White']['knight']
    Board[7, 6] = Pieces['White']['knight']

    # Places Bishops
    Board[0, 2] = Pieces['Black']['bishop']
    Board[0, 5] = Pieces['Black']['bishop']

    Board[7, 2] = Pieces['White']['bishop']
    Board[7, 5] = Pieces['White']['bishop']

    # Places Queens
    Board[0, 3] = Pieces['Black']['queen']

    Board[7, 3] = Pieces['White']['queen']

    # Places Kings
    Board[0, 4] = Pieces['Black']['king']

    Board[7, 4] = Pieces['White']['king']

    # Removes pieces in the center of the board
    Board[2 : 6, : ] = ' '

#### Move_Maker

def Move_Maker():
    """Move_Maker checks if the right piece is moved and if an own piece is going to be taken.
    If the function finds that a player made a move outside the previously stated parameters it raises
    an error an gives another chance to the player who made the error occur."""

    global T
    global Last_Move

    # Checks if it is white's turn and the piece to be moved also is white
    if T == 1 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in W.values(): 

        # Checks if the new piece location is occupied by another white piece
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in W.values():    

            # Removes piece from it's current location
            Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

            # Places piece at it's new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['White'][Move[0]]

        else:

            T = 0 # Gives white another chance to make a move
            print("MoveError: Can not take own pieces. Try again.")

    # Checks if it is black's turn and the piece to be moved also is black
    elif T == 0 and Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] in B.values():

        # Checks if the new piece location is occupied by another black piece
        if Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] not in B.values():    

            # Removes piece from current location
            Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]] = ' '

            # Adds piece in new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Pieces['Black'][Move[0]]

            Last_Move.append(Move[0])
            Last_Move.append(Move_Old)
            Last_Move.append(Move_New)

        else:

            T = 1 # Gives black another chance to make a move
            print("MoveError: Can not take own pieces. Try again.")

    else:

        if T == 0:                  #
                                    #
            T = 1                   #
                                    #   Gives the players their turn back
        else:                       #
                                    #
            T = 0                   #

        print("MoveError: Can only move own pieces. Try again.")
    print(Board)

### Turn ocelator and input

if T == 0:                          #
                                    #
    Turn = "White's turn"           #
    T = 1                           #
                                    #   Turn ocelator
else:                               #
                                    #
    Turn = "Black's turn"           #
    T = 0                           #


print(Turn, '\n' "Choose a piece and where to move it.")
Move = input("Piece,current location,new location: ") # Takes player input for what move to make

Move = Move.split(',')  # Splits the input into a list with three elements

Move[0] = Move[0].lower()
Move[1] = Move[1].lower() 
Move[2] = Move[2].lower()

Move_Old = ([*Move[1]]) # Makes a list of the current location of the selected piece
Move_New = ([*Move[2]]) # Makes a list of the new location of the selected piece

Piece_New = Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]]
Piece_Old = Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]]]

dx = Index['x'][Move_New[0]] - Index['x'][Move_Old[0]]
dy = Index['y'][Move_New[1]] - Index['y'][Move_Old[1]]

### Legal move detection

#### Detecting the legal moves for each piece with the exception of special moves (i.e castle, pawn promotion and en pasant).

if (Piece_Old == "♙" or Piece_Old == 'p') and Move[0] == "pawn":
    
    if Piece_New in B.values() and dy == -1 and (dx == 1 or dx == -1):
        
        print('test')
        if Move_New[1] == '8':

            promote = input("Choose a piece to promote to.")
            promote.lower()

            if promote in ["rook, knight, bishop, queen"]:

                Move[0] = promote

                Move_Maker()

        Move_Maker()
  

    elif Piece_New in W.values() and dy == 1 and (dx == 1 or dx == -1):
        
        print('test')
        if Move_New[1] == '1':

            promote = input("Choose a piece to promote to.")
            promote.lower()

            if promote in ["rook, knight, bishop, queen"]:

                Move[0] = promote

                Move_Maker()

        Move_Maker()

    
    elif (Board[(Index['y'][Move_Old[1]] - 1), Index['x'][Move_Old[0]]] == ' ' and T == 1) or \
       (Board[(Index['y'][Move_Old[1]] + 1), Index['x'][Move_Old[0]]] == ' ' and T == 0):
        
        if (dy == 1 or dy == -1) and Move_New[0] == Move_Old[0]:
            print('test')
            if Move_New[1] == 8:

                promote = input("Choose a piece to promote to.")
                promote.lower()

                if promote in ["rook, knight, bishop, queen"]:

                    Move[0] = promote

                    Move_Maker()
            
            Move_Maker()


            


        elif (dy == 2 or dy == -2) and ((Move_Old[1] == '2' and T == 1) or (Move_Old[1] == '7' and T == 0)):

            print('s')
            Move_Maker()


    """elif Index['y'][Move_Old[1]] == 3 and Last_Move[]
         Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]] + 1] in B.values() or \ 
         Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]] - 1] in B.values() or \
         \
         Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]] + 1] in W.values() or \ 
         Board[Index['y'][Move_Old[1]], Index['x'][Move_Old[0]] - 1] in W.values():
"""
    

elif ((Piece_Old == '♖' or Piece_Old == '♜') and Move[0] == "rook") or \
     ((Piece_Old == '♕' or Piece_Old == '♛') and Move[0] == "queen"):

    if Move_New[1] == Move_Old[1] or Move_New[0] == Move_Old[0]:

            Move_Maker()


elif ((Piece_Old == '♗' or Piece_Old == '♝') and Move[0] == "bishop") or \
     ((Piece_Old == '♕' or Piece_Old == '♛') and Move[0] == "queen"):
    
    if (dy / dx == 1) or (dy / dx == -1):

        Move_Maker()


elif (Piece_Old == '♘' or Piece_Old == '♞') and Move[0] == "knight":
    
    if ((dy ** 2) + (dx ** 2)) ** (1/2) == 5 ** (1/2) and \
       ((dy == 1 or dy == -1) or (dx == 1 or dx == -1)) and dx != dy:
        
        Move_Maker()
        
        
elif (Piece_Old == '' or Piece_Old == '') and Move[0] == "king":
    
    if ((dx == 1 or dx == -1) and dy == 0) or ((dy == 1 or dy == -1) and dx == 0) or \
       ((dy / dx == 1 or dy / dx == -1) and (dx == 1 or dx == -1)):
        
        Move_Maker()


else:

    if T == 0:              #
                            #
        T = 1               #
                            # Gives player their turn back
    else:                   #
                            #
        T = 0               #

    print("Illegal move, try again.")
