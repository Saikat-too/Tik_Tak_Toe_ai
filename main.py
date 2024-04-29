# It is needed to copy the board from move to move
from copy import deepcopy 

#  Function to check the if the board is full or not 

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    
    return True

# Function to check if  a player has won 

def has_won(board , player):
    #Check rows 
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    #Check Columns 
    for col in range(3):
        if all(board[row][col] ==player for row in range(3)):
            return True
    
    #Check Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True 
    
    return False 


# For evaluating the board state 
def evaluate_board(board , player , opponent):
    if has_won(board , player):
        return 1
    elif has_won(board , opponent):
        return -1
    elif is_board_full(board):
        return 0 

# Function to check Possible moves 

def possible_moves(board):
    moves = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append(i , j )
    
    return moves

# Function to implement ucs algorithm to for tic tac toe 

def ucs(board , player , opponent):
    
    # Base case if the game is over return the score 
    return evaluae 