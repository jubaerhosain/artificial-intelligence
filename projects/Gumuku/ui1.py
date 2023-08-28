import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton


class Gomoku(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gumuku AI")

        self.grid = QGridLayout()
        self.buttons = []
        for i in range(10):
            for j in range(10):
                button = QPushButton()
                button.setFixedSize(50, 50)
                self.buttons.append(button)
                self.grid.addWidget(button, i, j)

        self.right_section = QGridLayout()
        self.current_user_move_label = QLabel()
        self.new_game_button = QPushButton("New Game")
        self.reset_button = QPushButton("Reset")
        self.right_section.addWidget(self.current_user_move_label, 0, 0)
        self.right_section.addWidget(self.new_game_button, 0, 1)
        self.right_section.addWidget(self.reset_button, 0, 2)

        self.setLayout(QGridLayout())
        self.layout().addLayout(self.grid, 0, 0)
        self.layout().addLayout(self.right_section, 1, 0)

        self.current_user_move_label.setText("Current User Move: X")
        self.new_game_button.clicked.connect(self.on_new_game_clicked)
        self.reset_button.clicked.connect(self.on_reset_clicked)

    def on_new_game_clicked(self):
        for button in self.buttons:
            button.setText("")
        self.current_user_move_label.setText("Current User Move: X")

    def on_reset_clicked(self):
        for button in self.buttons:
            button.setText("")
        self.current_user_move_label.setText("Current User Move:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gomoku()
    window.show()
    sys.exit(app.exec_())
