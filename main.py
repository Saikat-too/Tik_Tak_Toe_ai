# It is needed to copy the board from move to move
from copy import deepcopy 

# Utility function to check the if the board is full or not 

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    
    return True

