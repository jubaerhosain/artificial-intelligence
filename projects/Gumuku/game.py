import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Gumuku:

    def __init__(self, board_size=10):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size), dtype=int)

        self.PLAYER_MARKER = 1
        self.AI_MARKER = -1
        self.EMPTY_MARKER = 0

        self.current_plyer = self.PLAYER_MARKER

    def __get_available_moves(self) -> [Point]:
        available_moves = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if (self.board[i][j] == self.EMPTY_MARKER):
                    available_moves.append(Point(i, j))
        return available_moves

    def __is_board_full(self) -> bool:
        return all(self.board[i][j] != self.EMPTY_MARKER for i in range(self.board_size) for j in range(self.board_size))

    def __minimax_alpha_beta_pruning(self, depth, alpha, beta):
        pass

    def make_move(self, pos, player) -> bool:
        if (self.board[pos.x][pos.y] != self.EMPTY_MARKER):
            return False
        self.board[pos.x, pos.y] = player
        return True

    def swap_current_player(self):
        self.current_plyer = self.AI_MARKER if self.current_plyer == self.PLAYER_MARKER else self.PLAYER_MARKER

    def is_won(self, player) -> bool:
        # Check rows
        for row in range(self.board_size):
            for col in range(self.board_size - 4):
                if all(self.board[row][col+i] == player for i in range(5)):
                    return True
        # Check columns
        for col in range(self.board_size):
            for row in range(self.board_size - 4):
                if all(self.board[row+i][col] == player for i in range(5)):
                    return True
        # Check diagonals
        for row in range(self.board_size - 4):
            for col in range(self.board_size - 4):
                if all(self.board[row+i][col+i] == player for i in range(5)):
                    return True
                if all(self.board[row+4-i][col+i] == player for i in range(5)):
                    return True
        return False

    def is_draw(self) -> bool:
        if self.is_won(self.PLAYER_MARKER):
            return False
        elif self.is_won(self.AI_MARKER):
            return False

        return self.__is_board_full()

    def is_game_over(self) -> bool:
        return self.__is_board_full() or self.is_won(self.PLAYER_MARKER) or self.is_won(self.AI_MARKER)

    def get_ai_move(self) -> Point:
        best_move = Point(-1, -1)
        best_score = np.inf
        for i in range(self.board_size):
            for j in range(self.board_size):
                current_move, current_score = 1, 1  # minimax()
                if (current_score > best_score):
                    best_move = current_move
        return best_move


if __name__ == "__main__":
    gumuku = Gumuku()
    current_player = gumuku.PLAYER_MARKER

    while not gumuku.is_game_over():
        if gumuku.current_plyer == gumuku.PLAYER_MARKER:
            print("player")
            gumuku.swap_current_player()
        else:
            print("ai")
            gumuku.swap_current_player()
