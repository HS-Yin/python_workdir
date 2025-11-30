from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

from XiangQiBoard import XiangQiBoard
from XiangQiLog import XiangQiLog

class MainWindow(QMainWindow):
    def __init__(self, logic, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("中国象棋")
        self.logic = logic
        self.board = XiangQiBoard()
        self.log = XiangQiLog()
        self.board.move_callback = self.step_move  # 注册回调
        # 布局
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.log)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.board, stretch=4)
        main_layout.addLayout(right_layout, stretch=2)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # 初始化棋盘
        self.board.set_board(self.logic.get_board())

    #走棋判断
    def step_move(self, move):
        result = self.logic.step(move)
        if result == 0:
            return
        self.board.set_board(self.logic.get_board())
        if result == 2:
            self.log.add_log("黑方获胜！")
            self.restart_game()
        elif result == -2:
            self.log.add_log("红方获胜！")
            self.restart_game()
    
    # 重新开始
    def restart_game(self):
        self.logic.reset_board()
        self.board.set_board(self.logic.get_board())
    