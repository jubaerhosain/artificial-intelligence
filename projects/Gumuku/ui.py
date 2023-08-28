import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class Gomoku(QWidget):

    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.buttons = []
        for i in range(10):
            for j in range(10):
                button = QPushButton()
                button.setFixedSize(100, 100)
                self.buttons.append(button)
                self.grid.addWidget(button, i, j)

        self.setLayout(self.grid)

        self.current_player = "X"

        for button in self.buttons:
            button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self, button):
        button.setText(self.current_player)
        self.current_player = "O" if self.current_player == "X" else "X"

        # Check for a winner.
        for row in range(10):
            for col in range(10):
                if button.text() == self.buttons[row * 10 + col].text() == self.buttons[row * 10 + col + 1].text() == self.buttons[row * 10 + col + 2].text() == self.buttons[row * 10 + col + 3].text() == self.buttons[row * 10 + col + 4].text():
                    self.winner = self.current_player
                    break

                if button.text() == self.buttons[row + col].text() == self.buttons[row + col + 10].text() == self.buttons[row + col + 20].text() == self.buttons[row + col + 30].text() == self.buttons[row + col + 40].text():
                    self.winner = self.current_player
                    break

                if button.text() == self.buttons[row].text() == self.buttons[row + 1].text() == self.buttons[row + 2].text() == self.buttons[row + 3].text() == self.buttons[row + 4].text():
                    self.winner = self.current_player
                    break

                if button.text() == self.buttons[col].text() == self.buttons[col + 10].text() == self.buttons[col + 20].text() == self.buttons[col + 30].text() == self.buttons[col + 40].text():
                    self.winner = self.current_player
                    break

                if button.text() == self.buttons[row // 10 * 10 + col].text() == self.buttons[row // 10 * 10 + col + 1].text() == self.buttons[row // 10 * 10 + col + 2].text() == self.buttons[row // 10 * 10 + col + 3].text() == self.buttons[row // 10 * 10 + col + 4].text():
                    self.winner = self.current_player
                    break

                if button.text() == self.buttons[row + 10 * (col // 10)].text() == self.buttons[row + 10 * (col // 10) + 1].text() == self.buttons[row + 10 * (col // 10) + 2].text() == self.buttons[row + 10 * (col // 10) + 3].text() == self.buttons[row + 10 * (col // 10) + 4].text():
                    self.winner = self.current_player
                    break

        if self.winner is not None:
            self.disable_buttons()
            print(f"{self.winner} wins!")

        elif all(button.text() != "" for button in self.buttons):
            print("Tie game!")
            self.disable_buttons()

    def disable_buttons(self):
        for button in self.buttons:
            button.setDisabled(True)
