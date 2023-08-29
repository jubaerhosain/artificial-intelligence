def is_won(board, player):
    size = len(board)
    
    # Check rows
    for row in range(size):
        for col in range(size - 4):
            if all(board[row][col+i] == player for i in range(5)):
                return True
    
    # Check columns
    for col in range(size):
        for row in range(size - 4):
            if all(board[row+i][col] == player for i in range(5)):
                return True
    
    # Check diagonals
    for row in range(size - 4):
        for col in range(size - 4):
            if all(board[row+i][col+i] == player for i in range(5)):
                return True
            if all(board[row+4-i][col+i] == player for i in range(5)):
                return True
    
    return False

# Example usage
game_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player = 1

if is_won(game_board, player):
    print("Player", player, "has won!")
else:
    print("Player", player, "has not won yet.")
