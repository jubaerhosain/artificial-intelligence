import numpy as np

AI_MARKER = 'O'
PLAYER_MARKER = 'X'
EMPTY_SPACE = '-'
START_DEPTH = 0


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


board = np.array([[EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
                  [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE],
                  [EMPTY_SPACE, EMPTY_SPACE, EMPTY_SPACE]])


def print_board(board):
    print()
    for row in range(3):
        print(board[row][0], "|", board[row][1], "|", board[row][2])
        if row < 2:
            print("--+---+--")
    print()


def is_won(player):
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


def is_valid_pos(row, col):
    return row >= 0 and row <= 3 and col >= 0 and col <= 3


def is_valid_move(row, col):
    return board[row][col] == EMPTY_SPACE


def make_move(row, col, marker):
    board[row][col] = marker


def get_valid_moves():
    valid_moves = []
    for i in range(3):
        for j in range(3):
            if is_valid_move(i, j):
                valid_moves.append(Point(i, j))
    return valid_moves


def minimax(depth, is_maximizing):
    if is_won(AI_MARKER):
        return 1
    if is_won(PLAYER_MARKER):
        return -1
    if np.all(board != EMPTY_SPACE):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for move in get_valid_moves():
            make_move(move.x, move.y, AI_MARKER)
            score = minimax(depth + 1, False)
            make_move(move.x, move.y, EMPTY_SPACE)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for move in get_valid_moves():
            make_move(move.x, move.y, PLAYER_MARKER)
            score = minimax(depth + 1, True)
            make_move(move.x, move.y, EMPTY_SPACE)
            best_score = min(score, best_score)
        return best_score


def get_best_move():
    best_score = -np.inf
    best_move = None
    for move in get_valid_moves():
        make_move(move.x, move.y, AI_MARKER)
        score = minimax(START_DEPTH, False)
        make_move(move.x, move.y, EMPTY_SPACE)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def game_over():
    return np.all(board != EMPTY_SPACE) or is_won(AI_MARKER) or is_won(PLAYER_MARKER)

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are X and the computer is O.")
    print("To make a move, enter a number from 1 to 9 corresponding to the position on the board.")
    print("Here is the initial board:")
    print_board(board)

    while True:
        row = int(input("row: "))
        col = int(input("col: "))
        while not is_valid_pos(row, col) or not is_valid_move(row, col):
            print("Invalid move. Please try again.")
            player_move = int(input("Enter your move: "))

        make_move(row, col, PLAYER_MARKER)
        print_board(board)

        if is_won(PLAYER_MARKER):
            print("Congratulations! You won!")
            break
        if np.all(board != EMPTY_SPACE):
            print("It's a tie!")
            break

        print("The computer is making its move...")
        ai_move = get_best_move()
        make_move(ai_move.x, ai_move.y, AI_MARKER)
        print_board(board)

        if is_won(AI_MARKER):
            print("The computer won!")
            break
        if np.all(board != EMPTY_SPACE):
            print("It's a tie!")
            break


# play_game()
