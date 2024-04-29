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
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True 
    
    return False 


# For evaluating the board state 
def evaluate_board(board , player , opponent ):
    if has_won(board , player):
        return 1
    elif has_won(board , opponent):
        return -1
    elif is_board_full(board):
        return 0 
    
# Function to check Possible moves 

def get_possible_moves(board):
    moves = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i , j ))
    
    return moves

# Function to implement ucs algorithm to for tic tac toe 

# Function to implement UCS for Tic Tac Toe (iterative)
def ucs(board, player, opponent , depth):
    
    # Initialize a queue with the initial board state
    queue = [(board, None, 0)]  # (board, move, score)
    best_score = float('-inf')
    best_move = None

    while queue:
        current_board, current_move, current_score = queue.pop(0)

        # Check if the game is over
        if has_won(current_board, player):
            best_score = 1
            break
        elif has_won(current_board, opponent):
            best_score = -1
            break
        elif is_board_full(current_board):
            best_score = 0
            break
        elif depth == 4:
            return best_move , best_score 
    
        depth+=1
        # Get all possible moves
        moves = get_possible_moves(current_board)

        # Explore each move
        for move in moves:
            new_board = deepcopy(current_board)
            new_board[move[0]][move[1]] = opponent  # Make the move for the opponent

            # Evaluate the opponent's best response
            opponent_best_score = -ucs(new_board, opponent, player)

            # Update the best score and move
            if opponent_best_score > best_score:
                best_score = opponent_best_score
                best_move = move

            # Add the new board state to the queue
            queue.append((new_board, move, opponent_best_score))

    return best_move, best_score

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'

    while True:
        print_board(board)

        # Human player's turn
        move = input("Enter your move (row col): ").split()
        row, col = int(move[0]), int(move[1])

        if board[row][col] != ' ':
            print("Invalid move, try again!")
            continue

        board[row][col] = human_player

        # AI player's turn
        depth = 0
        best_move, score = ucs(board, ai_player, human_player , depth)
        if score == 0:
            print("It's a tie!")
            break
        elif score == -1:
            print("You win!")
            break
        else:
            if best_move is not None:
                board[best_move[0]][best_move[1]] = ai_player
                print("AI's move:")
            else:
                print("No move available for AI.")

    print_board(board)

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()
    

           
      

    print_board(board)

# Play the game
play_game()