# This may become a functioning version of chess

# Libraries

import numpy as np


# _______________________________________________________________
# Variables

T = 0

Board = np.full((8, 8), ' ') # Creates the 8 × 8 board

Last_Move = []
Move_List = []

W_Rook_a_Movecount = 0
W_Rook_h_Movecount = 0
B_Rook_a_Movecount = 0
B_Rook_h_Movecount = 0

W_King_Movecount = 0
B_King_Movecount = 0


# _______________________________________________________________
# Dictionaries

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


# _______________________________________________________________
# Functions

## Board_Reset

def Board_Reset():
    """Resets the board with pieces in their original positions and resets the turn ocelator"""

    # Resets turn ocelator
    global T
    T = 0
    
    global Move_List
    Move_List = []
    
    global Last_Move
    Last_Move = []

    # Places Pawns
    Board[1, : ] = 'p'
    Board[6, : ] = '♙'

    # Places Rooks
    Board[0, 0] = '♜'
    Board[0, 7] = '♜'

    Board[7, 0] = '♖'
    Board[7, 7] = '♖'

    # Places Knights
    Board[0, 1] = '♞'
    Board[0, 6] = '♞'

    Board[7, 1] = '♘'
    Board[7, 6] = '♘'

    # Places Bishops
    Board[0, 2] = '♝'
    Board[0, 5] = '♝'

    Board[7, 2] = '♗'
    Board[7, 5] = '♗'

    # Places Queens
    Board[0, 3] = '♛'

    Board[7, 3] = '♕'

    # Places Kings
    Board[0, 4] = '♚'

    Board[7, 4] = '♔'

    # Removes pieces in the center of the board
    Board[2 : 6, : ] = ' '

#### Move_Error

def Move_Error():
    """Gives the players their turn back and informs them that an illegal move has been made."""
    
    global T
    
    if T == 0:                  #
                                #
        T = 1                   #
                                #   Gives the players their turn back
    else:                       #
                                #
        T = 0                   #

    print("Illegal move. Try again.")


# _______________________________________________________________
## Move_Maker

def Move_Maker():
    """Move_Maker checks if the right piece is moved and if an own piece is going to be taken.
    If the function finds that a player made a move outside the previously stated parameters it raises
    an error an gives another chance to the player who made the error occur."""

    global T
    global Move_List
    global Last_Move
    global W_Rook_a_Movecount
    global W_Rook_h_Movecount
    global B_Rook_a_Movecount
    global B_Rook_h_Movecount
    global W_King_Movecount
    global B_King_Movecount
    
    
    # Checks if it is white's turn and the piece to be moved also is white
    if T == 1 and Piece_Old in W.values(): 
        
        # Checks if the new piece location is occupied by another white piece
        if Piece_New not in W.values():    
            
            # Removes piece from it's current location
            Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]] = ' '

            # Places piece at it's new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Piece_Old

            Last_Move = []
            Last_Move.append(Move_Current[1])
            Last_Move.append(Move_New[1])
            
            Move_List.append(Move)
            
            if Piece_Old == '♔':
                W_King_Movecount += 1
            
            
            elif Piece_Old == '♖' and Move_Current[0] == 'a':
                W_Rook_a_Movecount += 1
             
            
            elif Piece_Old == '♖' and Move_Current[0] == 'h':
                W_Rook_h_Movecount += 1
            
            
        else:

            T = 0 # Gives white another chance to make a move
            print("MoveError: Can not take own pieces. Try again.")

    # Checks if it is black's turn and the piece to be moved also is black
    elif T == 0 and Piece_Old in B.values():

        # Checks if the new piece location is occupied by another black piece
        if Piece_New not in B.values():    

            # Removes piece from current location
            Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]] = ' '

            # Adds piece in new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Piece_Old

            Last_Move = []
            Last_Move.append(Move_Current[1])
            Last_Move.append(Move_New[1])
            Move_List.append(Move_New)

            
            if Piece_Old == '♚':
                W_King_Movecount += 1
            
            
            elif Piece_Old == '♜' and Move_Current[0] == 'a':
                B_Rook_a_Movecount += 1
            
            
            elif Piece_Old == '♜' and Move_Current[0] == 'h':
                W_Rook_h_Movecount += 1
            
            
        else:

            T = 1 # Gives black another chance to make a move
            print("MoveError: Can not take own pieces. Try again.")

    else:

        Move_Error()
    
    print(Board)


# _______________________________________________________________
# Turn ocelator and input

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
Move = input("Current location,new location: ") # Takes player input for what move to make

Move = Move.split(',')  # Splits the input into a list with two elements

Move[0] = Move[0].lower() 
Move[1] = Move[1].lower()

Move_Current = ([*Move[0]]) # Makes a list of the current location of the selected piece
Move_New = ([*Move[1]]) # Makes a list of the new location of the selected piece

Piece_New = Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]]
Piece_Old = Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]]

dx = Index['x'][Move_New[0]] - Index['x'][Move_Current[0]]
dy = Index['y'][Move_New[1]] - Index['y'][Move_Current[1]]


# _______________________________________________________________
# Legal move detection

if Piece_Old == "♙" or Piece_Old == 'p':
    
    if (Move_New[1] == '8' and T == 1) or (Move_New[1] == '1' and T == 0):
        
        promote = input("Choose a piece to promote to.")
        promote.lower()

        
        if promote in ["rook", "knight", "bishop", "queen"]:

            Piece_Old = promote
            Move_Maker()
    
    
        else:
            
            Move_Error()
    
    
    elif Move_Current[1] == '5' and (dx == 1 or dx == -1) and dy == -1 and \
        (Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] - 1] == 'p' or \
         Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] + 1] == 'p') and \
         Index['y'][Last_Move[1]] - Index['y'][Last_Move[0]] == 2:
        
        Board[3, Index['x'][Move_New[0]]] = ' '
        Move_Maker()
        
        
    elif Move_Current[1] == '4' and (dx == 1 or dx == -1) and dy == 1 and \
        (Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] - 1] == '♙' or \
         Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] + 1] == '♙') and \
         Index['y'][Last_Move[1]] - Index['y'][Last_Move[0]] == -2:
        
        Board[4, Index['x'][Move_New[0]]] = ' '
        Move_Maker()
        
        
    elif Piece_New in B.values() and dy == -1 and (dx == 1 or dx == -1):
        
        Move_Maker()


    elif Piece_New in W.values() and dy == 1 and (dx == 1 or dx == -1): 
        
        Move_Maker()

    
    elif (Board[(Index['y'][Move_Current[1]] - 1), Index['x'][Move_Current[0]]] == ' ' and T == 1) or \
         (Board[(Index['y'][Move_Current[1]] + 1), Index['x'][Move_Current[0]]] == ' ' and T == 0):
        
        if (dy == 1 or dy == -1) and dx == 0:
            
            Move_Maker()


        elif (dy == 2 or dy == -2) and ((Move_Current[1] == '2' and T == 1 and \
              Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] == ' ') or \
             (Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] == ' ' and \
              Move_Current[1] == '7' and T == 0)) and dx == 0:
            
            Move_Maker()
            
            
        else:
            
            Move_Error()
        
    
    else:
        
        Move_Error()



elif (Piece_Old == '♖' or Piece_Old == '♜') and \
     (Move_New[1] == Move_Current[1] or Move_New[0] == Move_Current[0]):

    Move_Maker()



elif Piece_Old == '♗' or Piece_Old == '♝':
      
    if dy / dx == 1 or dy / dx == -1:

        Move_Maker()
      
    
    else:
        
        Move_Error()



elif Piece_Old == '♘' or Piece_Old == '♞':

    if ((dy ** 2) + (dx ** 2)) ** (1/2) - 5 ** (1/2) < 0.1 and \
       ((dy == 1 or dy == -1) or (dx == 1 or dx == -1)) and dx != dy:

        Move_Maker()
     
    
    else:
        
        Move_Error()



elif Piece_Old == '♕' or Piece_Old == '♛':
          
    if (Move_New[1] == Move_Current[1] or Move_New[0] == Move_Current[0]) or \
       (dy / dx == 1 or dy / dx == -1):
        
        Move_Maker()
      
    
    else:
        
        Move_Error()
        


elif Piece_Old == '♔' or Piece_Old == '♚':

    if ((dx == 1 or dx == -1) and dy == 0) or ((dy == 1 or dy == -1) and dx == 0) or \
       ((dx != 0 and (dy / dx == 1 or dy / dx == -1)) and (dx == 1 or dx == -1)):

        Move_Maker()
    
    
    elif dx == 2 and dy == 0 and W_Rook_h_Movecount == 0 and W_King_Movecount == 0 and \
         (Board[7, 5] == ' ' and Board[7,6] == ' '):
        
        Board[7, 7] = ' '
        Board[7, 5] = '♖'
        Move_Maker()
    
    
    elif dx == -2 and dy == 0 and W_Rook_a_Movecount == 0 and W_King_Movecount == 0 and \
         (Board[7, 1] == ' ' and Board[7, 2] == ' ' and Board[7, 3] == ' '):
        
        Board[7, 0] = ' '
        Board[7, 3] = '♖'
        Move_Maker()
        
        
    elif dx == 2 and dy == 0 and B_Rook_h_Movecount == 0 and B_King_Movecount == 0 and \
         (Board[0, 5] == ' ' and Board[0,6] == ' '):
        
        Board[0, 7] = ' '
        Board[0, 5] = '♜'
        Move_Maker()
        
        
    elif dx == -2 and dy == 0 and B_Rook_a_Movecount == 0 and B_King_Movecount == 0 and \
        (Board[0, 1] == ' ' and Board[0, 2] == ' ' and Board[0, 3] == ' '):
        
        Board[0, 0] = ' '
        Board[0, 3] = '♜'
        Move_Maker()
        

    else:
        
        Move_Error()



else:
    
    Move_Error()