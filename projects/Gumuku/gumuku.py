import numpy as np

class Gumuku:

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = np.zeros((board_size, board_size))
        self.player = 1

    def make_move(self, row, col):
        self.board[row, col] = self.player
        self.player = -self.player

    def is_terminal_state(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row, col] == 0:
                    return False
        return True

    def evaluate(self):
        if self.is_terminal_state():
            if self.board.sum() == self.player:
                return 1
            elif self.board.sum() == -self.player:
                return -1
            else:
                return 0
        else:
            return 0

    def minimax_alpha_beta_pruning(self, depth, alpha, beta):
        if self.is_terminal_state():
            return self.evaluate()

        best_move = None
        best_value = -np.inf if self.player == 1 else np.inf

        for row in range(self.board_size):
            for col in range(self.board_size):
                if self.board[row, col] == 0:
                    self.board[row, col] = self.player
                    value = self.minimax_alpha_beta_pruning(depth - 1, -beta, -alpha)
                    self.board[row, col] = 0

                    if self.player == 1:
                        if value > best_value:
                            best_value = value
                            best_move = (row, col)
                    elif self.player == -1:
                        if value < best_value:
                            best_value = value
                            best_move = (row, col)

                    alpha = max(alpha, best_value)
                    if alpha >= beta:
                        break

        return best_move, best_value

    def get_best_move(self, depth):
        _, best_move = self.minimax_alpha_beta_pruning(depth, -np.inf, np.inf)
        return best_move

def main():
    board_size = 15
    game = Gumuku(board_size)

    while not game.is_terminal_state():
        print(game.board)
        move = game.get_best_move(3)
        game.make_move(*move)

    print(game.board)
    print(game.evaluate())

if __name__ == "__main__":
    main()
