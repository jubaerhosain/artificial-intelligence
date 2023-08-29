import numpy as np

AI_MARKER = 'O'
PLAYER_MARKER = 'X'
EMPTY_SPACE = '-'
START_DEPTH = 0

board = np.array([[EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
                  [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
                  [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE]])


def is_won(board, player):
    for row in range(3):
        if np.all(board[row] == player):
            return True

    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    if np.all(np.diag(board) == player):
        return True

    if np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False


def print_board(board):
    print()
    for row in range(3):
        print(board[row][0], "|", board[row][1], "|", board[row][2])
        if row < 2:
            print("--+---+--")
    print()


def is_valid_pos(n):
    return (n >= 1 and n <= 9)


def is_valid_move(board, n):
    row = (n - 1) // 3
    col = (n - 1) % 3
    return board[row][col] == EMPTY_SPACE


def make_move(board, n, marker):
    row = (n - 1) // 3
    col = (n - 1) % 3
    board[row][col] = marker


def get_valid_moves(board):
    valid_moves = []
    for n in range(1, 10):
        if is_valid_move(board, n):
            valid_moves.append(n)
    return valid_moves


def minimax(board, depth, is_maximizing):
    if is_won(board, AI_MARKER):
        return 1
    if is_won(board, PLAYER_MARKER):
        return -1
    if np.all(board != EMPTY_SPACE):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for move in get_valid_moves(board):
            make_move(board, move, AI_MARKER)
            score = minimax(board, depth + 1, False)
            make_move(board, move, EMPTY_SPACE)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for move in get_valid_moves(board):
            make_move(board, move, PLAYER_MARKER)
            score = minimax(board, depth + 1, True)
            make_move(board, move, EMPTY_SPACE)
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    best_score = -np.inf
    best_move = None
    for move in get_valid_moves(board):
        make_move(board, move, AI_MARKER)
        score = minimax(board, START_DEPTH, False)
        make_move(board, move, EMPTY_SPACE)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X and the computer is O.")
    print("To make a move, enter a number from 1 to 9 corresponding to the position on the board.")
    print("Here is the initial board:")
    print_board(board)

    while True:
        player_move = int(input("Enter your move: "))
        while not is_valid_pos(player_move) or not is_valid_move(board, player_move):
            print("Invalid move. Please try again.")
            player_move = int(input("Enter your move: "))

        make_move(board, player_move, PLAYER_MARKER)
        print_board(board)

        if is_won(board, PLAYER_MARKER):
            print("Congratulations! You won!")
            break
        if np.all(board != EMPTY_SPACE):
            print("It's a tie!")
            break

        print("The computer is making its move...")
        ai_move = get_best_move(board)
        make_move(board, ai_move, AI_MARKER)
        print_board(board)

        if is_won(board, AI_MARKER):
            print("The computer won!")
            break
        if np.all(board != EMPTY_SPACE):
            print("It's a tie!")
            break


play_game()
