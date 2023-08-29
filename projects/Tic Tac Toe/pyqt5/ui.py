import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QVBoxLayout
import play


class TicTacToe(QMainWindow):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.position = [i, j]
                button.setFixedSize(100, 100)
                self.buttons[i][j] = button
                self.grid.addWidget(button, i, j)

        self.central_widget = QWidget()
        self.central_layout = QHBoxLayout()

        self.player_label = QLabel("Current Player: X")
        self.status_label = QLabel("")

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.player_label)
        self.right_layout.addWidget(self.status_label)

        self.central_layout.addLayout(self.grid)
        self.central_layout.addLayout(self.right_layout)
        self.central_widget.setLayout(self.central_layout)

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Tic Tac Toe")

        # self.setLayout(self.grid)

        self.current_player = play.PLAYER_MARKER
        self.winner = None

        for row in self.buttons:
            for button in row:
                button.clicked.connect(
                    lambda checked, b=button: self.on_button_clicked(b))

    def on_button_clicked(self, button):

        if self.current_player == play.AI_MARKER or button.text() != "":
            return

        button.setText(self.current_player)
        play.make_move(button.position[0], button.position[1], play.PLAYER_MARKER)
        
        if(play.is_won(play.PLAYER_MARKER)):
            print("YOU WINS")
            exit()
        
        if play.game_over():
            print("game is drawn")
            exit()

        self.current_player = play.AI_MARKER
        self.player_label.setText("Current Player: " + self.current_player)
        
        ai_move  = play.get_best_move()
        play.make_move(ai_move.x, ai_move.y, play.AI_MARKER)
        
        self.buttons[ai_move.x][ai_move.y].setText(play.AI_MARKER)
        self.current_player = play.PLAYER_MARKER
        self.player_label.setText("Current Player: " + self.current_player)
        
        if(play.is_won(play.AI_MARKER)):
            print("AI WINS")
            exit()
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    tic_tac_toe = TicTacToe()
    tic_tac_toe.show()
    sys.exit(app.exec_())
