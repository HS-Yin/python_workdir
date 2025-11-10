import sys
from PySide6.QtWidgets import QApplication
from UI import XiangQiUI
from logic import XiangQi
def step_move(move):
    print(move)
    success = logic.step(move)
    if success:
        ui.set_board(logic.get_board())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logic = XiangQi()
    ui = XiangQiUI()
    ui.move_callback = step_move
    ui.set_board(logic.get_board())
    ui.show()
    sys.exit(app.exec())