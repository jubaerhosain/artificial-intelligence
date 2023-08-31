import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtWidgets import QGridLayout, QDesktopWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from gumuku import Gumuku, Point


class GumukuBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board_width = 800
        self.board_height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gumuku Board")
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.createGrid())
        main_layout.addWidget(self.createRightPanel())
        main_widget.setLayout(main_layout)
        # Calculate the center position after setting the central widget
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.board_width) // 2
        y = (screen_geometry.height() - self.board_height) // 2
        self.setGeometry(x, y, self.board_width, self.board_height)
        # Set the fixed size of the main window
        self.setFixedSize(self.board_width, self.board_height)

    def createGrid(self):
        grid_widget = QWidget()
        grid_layout = QGridLayout()
        grid_layout.setVerticalSpacing(5)
        grid_layout.setHorizontalSpacing(5)
        grid_layout.setAlignment(Qt.AlignCenter)
        self.buttons = []
        for row in range(10):
            row_buttons = []
            for col in range(10):
                button = QPushButton()
                button.setFixedSize(40, 40)
                button.position = Point(row, col)
                button.clicked.connect(self.buttonClicked)
                # Set the button style sheet to make it circular
                button.setStyleSheet(
                    "QPushButton { border-radius: 20px; background-color: grey; }")
                row_buttons.append(button)
                grid_layout.addWidget(button, row, col)
            self.buttons.append(row_buttons)
        grid_widget.setLayout(grid_layout)
        return grid_widget

    def createRightPanel(self):
        right_widget = QWidget()
        # Create buttons
        new_game_button = QPushButton("New Game")
        reset_game_button = QPushButton("Reset Game")
        self.current_player_label = QPushButton("Current Player: You")
        # Set button sizes and style
        button_height = 40
        button_width = 200
        new_game_button.setFixedSize(button_width, button_height)
        reset_game_button.setFixedSize(button_width, button_height)
        self.current_player_label.setFixedSize(button_width, button_height)
        new_game_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; font-size: 18px; text-align: center; }"
            "QPushButton:hover { background-color: #45a049; }"
        )
        reset_game_button.setStyleSheet(
            "QPushButton { background-color: #f44336; color: white; font-size: 18px; text-align: center; }"
            "QPushButton:hover { background-color: #d32f2f; }"
        )
        self.current_player_label.setStyleSheet(
            "QPushButton { background-color: #2196F3; color: white; font-size: 18px; text-align: center; }"
        )
        # Connect buttons to slots
        new_game_button.clicked.connect(self.newGame)
        reset_game_button.clicked.connect(self.resetGame)
        # Create layout
        right_layout = QVBoxLayout()
        right_layout.addWidget(new_game_button)
        right_layout.addWidget(reset_game_button)
        right_layout.addWidget(self.current_player_label)
        # Set vertical spacing between buttons
        right_layout.setSpacing(10)
        # Center-align the buttons
        right_layout.setAlignment(Qt.AlignHCenter)
        right_widget.setLayout(right_layout)
        return right_widget

    def buttonClicked(self):
        sender = self.sender()
        # Change button color on click
        current_color = sender.palette().button().color()
        new_color = QColor(
            Qt.red) if current_color == Qt.green else QColor(Qt.green)
        sender.setStyleSheet(
            f"border-radius: 20px; background-color: {new_color.name()};")
        
        print(sender.position.x, sender.position.y)

    def newGame(self):
        # Reset button colors and current player label
        for row in range(10):
            for col in range(10):
                self.buttons[row][col].setStyleSheet(
                    "QPushButton { border-radius: 20px; background-color: grey; }")
        self.current_player_label.setText("Current Player: You")

    def resetGame(self):
        # Reset button colors, current player label, and remove AI moves (if any)
        for row in range(10):
            for col in range(10):
                self.buttons[row][col].setStyleSheet(
                    "QPushButton { border-radius: 20px; background-color: grey; }")
        self.current_player_label.setText("Current Player: You")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GumukuBoard()
    window.show()
    sys.exit(app.exec_())
