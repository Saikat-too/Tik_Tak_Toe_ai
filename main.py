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
    if has_won(board , player):
        return 1
    elif has_won(board , opponent):
        return -1
    elif is_board_full(board):
        return 0 
    # Get all the possible moves
    moves = possible_moves(board)
    
    # Initialize the best score and move 
    best_score = float('-inf')
    best_move = None
    
    #Iterate over all possible moves 
    
    for move in moves:
        new_board = deepcopy(board)
        new_board[move[0]][move[1]] == player
        
        #Recursively Evaluate the value 
        score = -ucs(new_board , player , opponent)
        
        #Update the best score and move 
        if score > best_score:
            best_score = score 
            best_move = move
        
    # IF no move is available return 0     
    if best_move is None:
        return 0 
    
    else:
        board[best_move[0]][best_move[1]] == player 
        return best_score 
    


# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()
    
# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    opponent = 'O'

    while True:
        print_board(board)

        # Human player's turn
        if player == 'X':
            move = input("Enter your move (row col): ").split()
            row, col = int(move[0]), int(move[1])

            if board[row][col] != ' ':
                print("Invalid move, try again!")
                continue

            board[row][col] = player

        # AI player's turn
        else:
            score = ucs(board, opponent, player)
            if score == 0:
                print("It's a tie!")
                break
            elif score == -1:
                print("You win!")
                break
            else:
                print("AI's move:")

        # Switch players
        player, opponent = opponent, player

    print_board(board)

# Play the game
play_game()