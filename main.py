import sys
from PyQt5.QtWidgets import QApplication
from pyqtcode import CalculatorApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
