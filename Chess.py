# This is a functioning version of chess

# Libraries

import numpy as np
import time



# _______________________________________________________________
# Variables

# A variable used to determine which players turn it is
T = 0

B_Time = 'not important'        #
W_Time = 'not important'        #    Are only there to make the unlimited time mode playable


W_Rook_a_Movecount = 0          #
W_Rook_h_Movecount = 0          #
B_Rook_a_Movecount = 0          #
B_Rook_h_Movecount = 0          #    Variables used for checking if castle is an availible move
                                #
W_King_Movecount = 0            #
B_King_Movecount = 0            #



# _______________________________________________________________
# Lists and dictionaries

# Numpy two dimensional array used as the playing board
Board = np.full((8, 8), ' ')


# Lists containing the peices visualisations
B = ["p", "♜", "♞", "♝", "♚", "♛"]     
    
W = ["♙", "♖", "♘", "♗", "♔", "♕"]


# A list that is iterated after every move and determines if en passant is availible
Last_Move = []


# A nested dictionary to translate the inputted koordinates to indexes in the array "Board"
Index = {
    'x' : {
        "a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
    },
    'y' : {
        "1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0
    }
}



# _______________________________________________________________
# Functions

## Board_Reset

def Board_Reset():
    """Resets the board with pieces in their original positions and also resets the turn ocelator"""

    global T
    

    T = 0 # Resets variable to their default state in preparation of a new game

    
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



# _______________________________________________________________
## Move_Error

def Move_Error():
    """Gives the player their turn back and informs them that an illegal move has been made."""
    
    global Move_Made
    global T
    
    # A variable used to determine if a move that was tried is illegal. This is used for detecting game over.
    Move_Made = 0
    
    
    if T == 0:                  #
                                #
        T = 1                   #
                                #    Gives the players their turn back
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
    global Time_Stop
    global Last_Move
    global Move_Made
    global W_Rook_a_Movecount
    global W_Rook_h_Movecount
    global B_Rook_a_Movecount
    global B_Rook_h_Movecount
    global W_King_Movecount
    global B_King_Movecount
    
    
    # Checks if it is white's turn and the piece to be moved also is white
    if T == 1 and Piece_Old in W: 
        
        # Checks if the new piece location is occupied by another white piece
        if Piece_New not in W:    
            
            # Removes piece from it's current location
            Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]] = ' '

            # Places piece at it's new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Piece_Old
            
            
            # Clears last move and appends the new move as the last move for the next turn
            Last_Move = []
            Last_Move.append(Move_Current[1])
            Last_Move.append(Move_New[1])
            
            # Changes Move_Made to let the game detect if the king has been legally captured
            Move_Made = 1
            
            
            # Checks if white's king was moved and updates a viariable used for legal detection of castle
            if Piece_Old == '♔':
                W_King_Movecount += 1
            
            # Checks if white's rook on a1 was moved and changes viariable used for legal detection of castle
            elif Piece_Old == '♖' and Move_Current[0] == 'a':
                W_Rook_a_Movecount += 1
             
            # Checks if white's rook on h1 was moved and changes viariable used for legal detection of castle
            elif Piece_Old == '♖' and Move_Current[0] == 'h':
                W_Rook_h_Movecount += 1
            
            
        else:

            Move_Error()

    # Checks if it is black's turn and the piece to be moved also is black
    elif T == 0 and Piece_Old in B:

        # Checks if the new piece location is occupied by another black piece
        if Piece_New not in B:    

            # Removes piece from current location
            Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]] = ' '

            # Adds piece in new location
            Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] = Piece_Old
            
            
            # Clears last move and appends the new move as the last move for the next turn
            Last_Move = []
            Last_Move.append(Move_Current[1])
            Last_Move.append(Move_New[1])
            
            # Changes Move_Made to let the game detect if the king has been legally captured
            Move_Made = 1

            
            # Checks if black's king was moved and updates a viariable used for legal detection of castle
            if Piece_Old == '♚':
                W_King_Movecount += 1
            
            # Checks if black's rook on a8 was moved and changes viariable used for legal detection of castle
            elif Piece_Old == '♜' and Move_Current[0] == 'a':
                B_Rook_a_Movecount += 1
            
            # Checks if black's rook on h8 was moved and changes viariable used for legal detection of castle
            elif Piece_Old == '♜' and Move_Current[0] == 'h':
                W_Rook_h_Movecount += 1
            
            
        else:

            Move_Error()

    else:

        Move_Error()
    
    Time_Stop = round(time.time(), 1) # Takes a time stamp for when a move has been made

    print(Board)



# _______________________________________________________________
## Piece_Jump

def Piece_Jump():
    """Piece_Jump detects if a player tries jumping over another piece with either a rook, bishop or queen"""
    
    if dx >= 2 and dy == 0:
        
        try:
            for i in range(dx - 1):
            
                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] + (i + 1)] != ' ':
                
                    Move_Error()
                    break
            
        except:
            Move_Maker()
            
        
    elif dx <= -2 and dy == 0:
        
        try:
            for i in range(-dx - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] - (i + 1)] != ' ':

                    Move_Error()
                    break

        except:
            Move_Maker()
            
            
    elif dx == 0 and dy <= -2:
        
        try:
            for i in range(-dy - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] - (i + 1), Index['x'][Move_Current[0]]] != ' ':

                    Move_Error()
                    break
        
        except:
            Move_Maker()
        
            
    elif dx == 0 and dy >= -2:
        
        try:
            for i in range(dy - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] + (i + 1), Index['x'][Move_Current[0]]] != ' ':

                    Move_Error()
                    break
        
        except:
            Move_Maker()
            
            
    elif dx / dy == -1 and dx >= 2:
        
        try:
            for i in range(dx - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] - (i + 1), Index['x'][Move_Current[0]] + (i + 1)] != ' ':

                    Move_Error()
                    break
        
        except:
            Move_Maker()
            
            
    elif dx / dy == -1 and dx <= -2:
        
        try:
            for i in range(-dx - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] + (i + 1), Index['x'][Move_Current[0]] - (i + 1)] != ' ':

                    Move_Error()
                    break

        except:
            Move_Maker()
            
            
    elif dx / dy == 1 and dx >= 2:
        
        try:
            for i in range(dx - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] + (i + 1), Index['x'][Move_Current[0]] + (i + 1)] != ' ':

                    Move_Error()
                    break
            
        except:
            Move_Maker()
            
            
    elif dx / dy == 1 and dx <= -2:
        
        try:
            for i in range(-dx - 1):

                # Checks if any of the spaces between Move_New and Move_Current are not empty
                if Board[Index['y'][Move_Current[1]] - (i + 1), Index['x'][Move_Current[0]] - (i + 1)] != ' ':

                    Move_Error()
                    break
            
        except:
            Move_Maker()
            
            
    else:
        
        Move_Error()



# _______________________________________________________________
# Input and move check

# Asks player if they would like to play
Play = input("Would you like to play?  yes/no ")
Play.lower()

if Play == "yes":
    
    # Gives the player the standard options for timer settings but also gives the format for creating your
    # own timer settings 
    print("What game mode would you like to play?", '\n', "Your choises are:", '\n', "1-min", '\n', "1-1", \
          '\n', "2-1", '\n', "3-min", '\n', "3-2", '\n', "5-min", '\n', "10-min", '\n', "15-10", '\n', \
          "30-min", '\n', "unlimited", '\n', "or something else in the same format: (x-y)")
    
    Last_Move = [] # Clears Last_Move in preparation for a new game
    
try:                                                    #
    Mode = input().split('-')                           #
                                                        #    Tries to iterate over the input 
    B_Time = int(Mode[0]) * 60                          #
    W_Time = int(Mode[0]) * 60                          #
    
    
except:                                                 #
    if Mode[0] != "unlimited":                          #    Prevents game from starting if iteration failed
        print("incorrect format for mode inputted.")    #    and The selected mode is not unlimited
        Play = "no"                                     #


    
# _______________________________________________________________
# Game loop  

while Play == "yes": # The while-loop that contains the game
    
    if Last_Move == []:                 #
                                        #
        Piece_New = 'Game start'        #    Resets the board if it is the first turn of the game
                                        #
        Board_Reset()                   #
        print(Board)                    #

        
        Time_Count = 0                  #
        Time_Stop = 'new game'          #    Resets the timer variables for the first turn of the game
        Time_Start = 'new game'         #
        
        
        
# _______________________________________________________________
# Game over messages
    
    if (Piece_New == '♚' and Move_Made == 1) or (B_Time <= 0 and Mode[0] != "unlimited"):

        print("White Wins. Black's king was captured")    #
        Play = "no"                                       #    Gives win message and breaks the while-loop
      
    
    elif (Piece_New == '♔' and Move_Made == 1) or (W_Time <= 0 and Mode[0] != "unlimited"):
        
        print("Black Wins. White's king was captured")    #
        Play = "no"                                       #    Gives win message and breaks the while-loop
        

        
# _______________________________________________________________
# Turn ocelator and Time calculator

    if T == 0:

        Turn = "White's turn"
        T = 1 # Ocelates turn
        
        
        # Checks if a timer is needed 
        if Mode[0] != "unlimited":
            
            try:
                B_Time = B_Time - (Time_Stop - Time_Start) # Calculates time used during a move
            
            except:
                Time_Count = 1 # A variable used on the first turn for black     
                print(Mode[0], ':', "00") # Prints the timer in its starting state for the game-mode

                
            if W_Time <= 0:
                print("Black wins. White ran out of time")
                Play = "no"
            
            
            try:
                W_Time += int(Mode[1]) # Adds a designated amount of time as stated in the Mode input

                print(int(W_Time // 60), ':', round(((W_Time / 60) - (W_Time // 60)) * 60, 1)) # prints timer
            
            except:
                print(int(W_Time // 60), ':', round(((W_Time / 60) - (W_Time // 60)) * 60, 1)) # prints timer
        
        
    else:
 
        Turn = "Black's turn"
        T = 0 # Ocelates turn
        
        W_Time = W_Time - (Time_Stop - Time_Start) # Calculates time used during a move

        
        # Checks if a timer is needed
        if Mode[0] != "unlimited":
            
            if Time_Count == 1:
            
                Time_Count = 0
                print(Mode[0], ':', "00") # Prints the timer in its starting state for the game-mode
            
            
            elif B_Time <= 0:
                print("White wins. Black ran out of time")
                Play = "no"
            
            
            try:
                B_Time += int(Mode[1]) # Adds a designated amount of time as stated in the Mode input

                print(int(B_Time // 60), ':', round(((B_Time / 60) - (B_Time // 60)) * 60, 1)) # Prints timer

            except:
                print(int(B_Time // 60), ':', round(((B_Time / 60) - (B_Time // 60)) * 60, 1)) # Prints timer

        
        
# _______________________________________________________________
# Input
    
    Time_Start = round(time.time(), 1) # Takes a time stamp for when a move starts

    # Takes player input for what move to make
    print(Turn, '\n' "Choose a piece and where to move it.")
    Move = input("Current location,new location (Do not use spaces): ") 
    
    
    # Prevents Pieces from being moved outside the board and raising an error
    if Move_New[0] not in Index['x'].keys() or Move_New[1] not in Index['y'].keys():
            
            Move_Error()
    
    
    try:
        Move = Move.split(',')  # Splits the input into a list with two elements

        Move[0] = Move[0].lower()        #
        Move[1] = Move[1].lower()        #    Makes the inputted move into lowercase

        Move_Current = ([*Move[0]]) # Makes a list of the current location of the selected piece
        Move_New = ([*Move[1]]) # Makes a list of the new location of the selected piece

        # Makes the piece in the new location and the current location into variables
        Piece_New = Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]]
        Piece_Old = Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]]]

        # Variables made from the difference in the i and j values of the Board array
        dx = Index['x'][Move_New[0]] - Index['x'][Move_Current[0]]
        dy = Index['y'][Move_New[1]] - Index['y'][Move_Current[1]]
        
        
    except:
        Move_Error()



# _______________________________________________________________
# Legal Move Detection

    # Checks if the piece to be moved is a pawn
    if Piece_Old == "♙" or Piece_Old == 'p':

        # Checks if the pawn is on its promotion rank
        if (Move_New[1] == '8' and T == 1) or (Move_New[1] == '1' and T == 0):

            # Asks the player which piece to promote to
            promote = input("Choose a piece to promote to.")
            promote.lower()


            # Checks if the chosen promotion piece is allowed
            if promote in ["rook", "knight", "bishop", "queen"]:

                # Promotes the pawn
                Piece_Old = promote
                Move_Maker()


            else:

                Move_Error()


        # Checks if all rules for white doing en passant are fullfilled
        elif Move_Current[1] == '5' and (dx == 1 or dx == -1) and dy == -1 and \
            (Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] - 1] == 'p' or \
             Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] + 1] == 'p') and \
             Index['y'][Last_Move[1]] - Index['y'][Last_Move[0]] == 2:

            Board[3, Index['x'][Move_New[0]]] = ' '         #
            Move_Maker()                                    #    Performs the en passant move
                                                            
        # Checks if all rules for black doing en passant are fullfilled
        elif Move_Current[1] == '4' and (dx == 1 or dx == -1) and dy == 1 and \
            (Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] - 1] == '♙' or \
             Board[Index['y'][Move_Current[1]], Index['x'][Move_Current[0]] + 1] == '♙') and \
             Index['y'][Last_Move[1]] - Index['y'][Last_Move[0]] == -2:

            Board[4, Index['x'][Move_New[0]]] = ' '         #
            Move_Maker()                                    #    Performs the en passant move


        # if-statement for white pawn captures
        elif Piece_New in B and dy == -1 and (dx == 1 or dx == -1): 

            Move_Maker()


        # if-statement for black pawn captures
        elif Piece_New in W and dy == 1 and (dx == 1 or dx == -1): 

            Move_Maker()

        # Checks if the space ahead of the pawn is empty
        elif (Board[(Index['y'][Move_Current[1]] - 1), Index['x'][Move_Current[0]]] == ' ' and T == 1) or \
             (Board[(Index['y'][Move_Current[1]] + 1), Index['x'][Move_Current[0]]] == ' ' and T == 0):

            # Checks if the pawn is to be moved one square forward
            if (dy == 1 or dy == -1) and dx == 0:

                Move_Maker()


            # Checks if the pawn is to be moved 2 spaces and if the second space ahead of the pawn is empty
            elif (dy == 2 or dy == -2) and ((Move_Current[1] == '2' and T == 1 and \
                  Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] == ' ') or \
                 (Board[Index['y'][Move_New[1]], Index['x'][Move_New[0]]] == ' ' and \
                  Move_Current[1] == '7' and T == 0)) and dx == 0:

                Move_Maker()


            else:

                Move_Error()


        else:

            Move_Error()



    # Checks if the piece to be moved is a rook and it is only being moved in a cardinal direction
    elif (Piece_Old == '♖' or Piece_Old == '♜') and \
         (dx == 0  or dy == 0):

        Piece_Jump()        


        
    # Checks if the piece to be moved is a bishop and it is only being moved directly diagonal
    elif (Piece_Old == '♗' or Piece_Old == '♝') and \
         (dx == dy or dx == -dy):

        Piece_Jump()


    
    # Checks if the piece to be moved is a queen
    elif Piece_Old == '♕' or Piece_Old == '♛':

        Piece_Jump()



    # Checks if the piece to be moved is a king
    elif Piece_Old == '♔' or Piece_Old == '♚':

        # Checks if the king is being moved only one square
        if ((dx == 1 or dx == -1) and dy == 0) or ((dy == 1 or dy == -1) and dx == 0) or \
           ((dx != 0 and (dy / dx == 1 or dy / dx == -1)) and (dx == 1 or dx == -1)):

            Move_Maker()

            
        # Checks if the white king can castle with the rook on h1
        elif dx == 2 and dy == 0 and W_Rook_h_Movecount == 0 and W_King_Movecount == 0 and \
             (Board[7, 5] == ' ' and Board[7,6] == ' '):

            Board[7, 7] = ' '           #
            Board[7, 5] = '♖'           #    Performs the castle with the h1 rook
            Move_Maker()                #


        # Checks if the white king can castle with the rook on a1
        elif dx == -2 and dy == 0 and W_Rook_a_Movecount == 0 and W_King_Movecount == 0 and \
             (Board[7, 1] == ' ' and Board[7, 2] == ' ' and Board[7, 3] == ' '):

            Board[7, 0] = ' '           #
            Board[7, 3] = '♖'           #    Performs the castle with the a1 rook
            Move_Maker()                #


        # Checks if the black king can castle with the rook on h8
        elif dx == 2 and dy == 0 and B_Rook_h_Movecount == 0 and B_King_Movecount == 0 and \
             (Board[0, 5] == ' ' and Board[0,6] == ' '):

            Board[0, 7] = ' '           #
            Board[0, 5] = '♜'           #    Performs the castle with the h8 rook
            Move_Maker()                #


        # Checks if the black king can castle with the rook on a8
        elif dx == -2 and dy == 0 and B_Rook_a_Movecount == 0 and B_King_Movecount == 0 and \
            (Board[0, 1] == ' ' and Board[0, 2] == ' ' and Board[0, 3] == ' '):

            Board[0, 0] = ' '           #
            Board[0, 3] = '♜'           #    Performs the castle with the a8 rook
            Move_Maker()                #


        else:

            Move_Error()


    # Checks if the piece to be moved is a knght
    elif Piece_Old == '♘' or Piece_Old == '♞':

        # Checks if the knight is making its unique legal move
        if ((dy ** 2) + (dx ** 2)) ** (1/2) - 5 ** (1/2) < 0.1 and \
           ((dy == 1 or dy == -1) or (dx == 1 or dx == -1)) and dx != dy:

            Move_Maker()


        else: 
            
            Move_Error()


    else:

        Move_Error()