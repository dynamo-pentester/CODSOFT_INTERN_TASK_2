from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import QFile, QTextStream
import sys

class CalculatorApp(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 500)
        self.initUI()

        # Load the CSS file
        css_file = QFile("theme.css")
        if css_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(css_file)
            style = stream.readAll()
            self.setStyleSheet(style)
            css_file.close()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.layout.addWidget(self.display)

        # Create a 4x4 grid for the calculator buttons
        button_grid = QGridLayout()
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
            '00', '.', '%', '**'
        ]
        self.buttons_dict = {}
        row, col = 0, 0
        for button_text in self.buttons:
            button = QPushButton(button_text)
            self.buttons_dict[button_text] = button
            button.clicked.connect(self.on_button_click)
            button_grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

            # Customize the button style
            button.setStyleSheet("background-color: #E0E0E0; color: #000000; font-size: 18px; padding: 10px;")

        self.layout.addLayout(button_grid)
        self.setLayout(self.layout)

    def on_button_click(self):
        button = self.sender()
        button_text = button.text()
        if button_text == 'C':
            self.display.clear()
        elif button_text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            current_text = self.display.text()
            new_text = current_text + button_text
            self.display.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
