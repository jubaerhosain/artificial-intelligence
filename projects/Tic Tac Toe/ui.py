import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class TicTacToe(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                self.buttons.append(button)
                self.grid.addWidget(button, i, j)

        self.setLayout(self.grid)

        self.current_player = "X"
        self.winner = None

        for button in self.buttons:
            button.clicked.connect(lambda checked, b=button: self.on_button_clicked(b))


    def on_button_clicked(self, button):
        self.current_player = "O" if self.current_player == "X" else "X"
        button.setText(self.current_player)

        # Check for a winner.
        for row in range(3):
            if button.text() == self.buttons[row * 3].text() == self.buttons[row * 3 + 1].text() == self.buttons[row * 3 + 2].text():
                self.winner = self.current_player
                break

        for col in range(3):
            if button.text() == self.buttons[col].text() == self.buttons[col + 3].text() == self.buttons[col + 6].text():
                self.winner = self.current_player
                break

        if button.text() == self.buttons[0].text() == self.buttons[4].text() == self.buttons[8].text():
            self.winner = self.current_player

        if button.text() == self.buttons[2].text() == self.buttons[4].text() == self.buttons[6].text():
            self.winner = self.current_player

        if self.winner is not None:
            self.disable_buttons()
            print(f"{self.winner} wins!")

        elif all(button.text() != "" for button in self.buttons):
            print("Tie game!")
            self.disable_buttons()

    def disable_buttons(self):
        for button in self.buttons:
            button.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tic_tac_toe = TicTacToe()
    tic_tac_toe.show()
    sys.exit(app.exec_())
