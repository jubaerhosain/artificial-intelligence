class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Gumuku:

    def __init__(self, board_size=10, win_row=5):
        self.board_size = board_size
        self.win_row = win_row
        self.board = [[0 for i in range(board_size)]
                      for j in range(board_size)]

        self.inf = int(1e9)

        self.PLAYER_MARKER = 1
        self.AI_MARKER = 2
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

    def print_board(self):
        print()
        for row in self.board:
            print(row)
        print()

    def make_move(self, pos, player) -> bool:
        if (self.board[pos.x][pos.y] != self.EMPTY_MARKER):
            return False
        self.board[pos.x, pos.y] = player
        return True

    def swap_current_player(self):
        self.current_plyer = self.AI_MARKER if self.current_plyer == self.PLAYER_MARKER else self.PLAYER_MARKER

    def is_won(self, player) -> bool:
        boundary = self.win_row - 1
        # Check rows
        for row in range(self.board_size):
            for col in range(self.board_size - boundary):
                if all(self.board[row][col+i] == player for i in range(self.win_row)):
                    return True
        # Check columns
        for col in range(self.board_size):
            for row in range(self.board_size - boundary):
                if all(self.board[row+i][col] == player for i in range(self.win_row)):
                    return True
        # Check diagonals
        for row in range(self.board_size - boundary):
            for col in range(self.board_size - boundary):
                if all(self.board[row+i][col+i] == player for i in range(self.win_row)):
                    return True
                if all(self.board[row+boundary-i][col+i] == player for i in range(self.win_row)):
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

    def __minimax_alpha_beta_pruning(self, marker, depth, alpha, beta):
        best_move = Point(-1, -1)
        best_score = -self.inf if marker == self.AI_MARKER else self.inf

        if self.is_won(self.AI_MARKER):
            return best_move, self.inf
        elif self.is_won(self.PLAYER_MARKER):
            return best_move, -self.inf
        elif self.__is_board_full():
            return best_move, 0
        
        if (depth >= 4):
            # print(depth)
            return best_move, 0

        for current_move in self.__get_available_moves():
            self.board[current_move.x][current_move.y] = marker
            if marker == self.AI_MARKER:
                _, current_score = self.__minimax_alpha_beta_pruning(
                    self.PLAYER_MARKER, depth+1, alpha, beta)
                if current_score > best_score:
                    best_score = current_score
                    best_move = current_move
                    self.board[current_move.x][current_move.y] = self.EMPTY_MARKER
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
            else:
                _, current_score = self.__minimax_alpha_beta_pruning(
                    self.AI_MARKER, depth+1, alpha, beta)
                if current_score < best_score:
                    best_score = current_score
                    best_move = current_move
                    self.board[current_move.x][current_move.y] = self.EMPTY_MARKER
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
            self.board[current_move.x][current_move.y] = self.EMPTY_MARKER

        return best_move, best_score

    def get_ai_move(self) -> Point:
        best_move, _ = self.__minimax_alpha_beta_pruning(
            self.AI_MARKER, 0, -self.inf, self.inf)
        return best_move


if __name__ == "__main__":
    gumuku = Gumuku(10, 5)
    current_player = gumuku.PLAYER_MARKER

    gumuku.print_board()

    while not gumuku.is_game_over():
        if gumuku.current_plyer == gumuku.PLAYER_MARKER:
            i, j = tuple(map(int, input("Enter two integers: ").split()))
            gumuku.board[i][j] = gumuku.PLAYER_MARKER
            gumuku.swap_current_player()
        else:
            print("AI is moving...")
            ai_move = gumuku.get_ai_move()
            gumuku.board[ai_move.x][ai_move.y] = gumuku.AI_MARKER
            gumuku.swap_current_player()
        gumuku.print_board()
