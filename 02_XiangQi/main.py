import sys
from PySide6.QtWidgets import QApplication
from UI import XiangQiUI
from logic import XiangQi
def step_move(move):
    logic_return = logic.step(move)
    print(move)
    if logic_return:
        ui.set_board(logic.get_board())
    if logic_return == 2:
        ui.show_win("黑")
        logic.reset_board()
        ui.set_board(logic.get_board())
    elif logic_return == -2:
        ui.show_win("红")
        logic.reset_board()
        ui.set_board(logic.get_board())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    logic = XiangQi()
    ui = XiangQiUI()
    ui.move_callback = step_move
    ui.set_board(logic.get_board())
    ui.show()
    sys.exit(app.exec())