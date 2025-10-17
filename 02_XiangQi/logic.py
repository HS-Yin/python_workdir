import numpy as np

class XiangQi:
    def __init__(self):
        self.board = np.zeros((10, 9), dtype=int)
        self.reset_board()
        self.current_player = 1  # 1 for Red, -1 for Black
        self.game_over = False
        self.winner = None
        self.move_history = []
        