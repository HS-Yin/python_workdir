from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt

from XiangQiBoard import XiangQiBoard
from XiangQiLog import XiangQiLog
import datetime

def timestamp():
    return datetime.datetime.now().strftime("[%H:%M:%S] ")

class MainWindow(QMainWindow):
    def __init__(self, logic, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("中国象棋")
        self.logic = logic
        self.board = XiangQiBoard()
        self.log = XiangQiLog()
        self.board.move_callback = self.step_move  # 回调移动功能
        self.board.pre_move_callback = self.pre_move # 回调预移动功能
        self.game_over = False # 新增：游戏是否结束
        # 布局
        self.restart_button = QPushButton("重新开始")
        self.surrender_button = QPushButton("认输") 
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.restart_button)
        right_layout.addWidget(self.surrender_button)
        right_layout.addWidget(self.log)
        right_layout.addStretch() # 让按钮固定在上方，日志占剩余空间

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.board, stretch=4)
        main_layout.addLayout(right_layout, stretch=2)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        self.restart_button.clicked.connect(self.restart_game)
        self.surrender_button.clicked.connect(self.surrender_game)
        # 初始化棋盘
        self.board.set_board(self.logic.get_board(), 1)
    def pre_move(self, position):
        if self.game_over: return # 游戏结束，禁止移动
        board = self.logic.get_board()
        player = self.logic.get_player()
        pre_move = self.logic.pre_step(position)
        piece = board[position[0],position[1]]
        if piece*player > 0:
            self.board.set_pre_move(pre_move, position)
        else:
            self.board.set_pre_move(pre_move)
    #走棋判断
    def step_move(self, move):
        if self.game_over: return # 游戏结束，禁止移动
        result = self.logic.step(move)
        board = self.logic.get_board()
        player = self.logic.get_player()
        if result == 1:
            self.board.set_board(board, player)
            next_player = "红方" if player == 1 else "黑方"
            self.log.add_log(timestamp()+f"轮到{next_player}走棋")
        elif result == 2:
            self.board.set_board(board, player)
            self.log.add_log(timestamp()+"黑方获胜！")
            self.game_over = True # 解锁棋盘
        elif result == -2:
            self.board.set_board(board, player)
            self.log.add_log(timestamp()+"红方获胜！")
            self.game_over = True # 解锁棋盘
        elif type(result) == str:
            self.log.add_log(timestamp()+result)
        else:
            return
    
    # 重新开始
    def restart_game(self):
        self.logic.reset_board()
        self.board.set_board(self.logic.get_board(), 1)
        self.game_over = False # 解锁棋盘
        self.log.add_log(timestamp()+"轮到红方走棋")
    
    def surrender_game(self):
        if self.game_over:
            return
        if self.logic.get_player() == 1:
            self.log.add_log(timestamp() + "红方认输，黑方获胜！")
        else:
            self.log.add_log(timestamp() + "黑方认输，红方获胜！")
        self.game_over = True
    