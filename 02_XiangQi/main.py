import sys
from PySide6.QtWidgets import QApplication
from logic import XiangQi
from UI import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    logic = XiangQi()

    window = MainWindow(logic)
    window.show()

    sys.exit(app.exec())