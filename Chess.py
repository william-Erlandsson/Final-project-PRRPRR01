# This may become a functioning version of chess

import numpy as np

# Board

Index_letter = ["a", "b", "c", "d", "e", "f", "g", "h"]

Board = np.zeros((8, 9))

for i in range(9):
    Board[i - 1, 0] = i

Index_letter = np.array((' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'))

print(Board, '\n', Index_letter)


