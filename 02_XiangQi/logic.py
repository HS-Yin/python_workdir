import numpy as np

class XiangQi:
    def __init__(self):
        self.board = np.zeros((10, 9), dtype=int)
        self.reset_board()
        self.current_player = 1  # 1 for Red, -1 for Black
        self.game_over = False
        self.winner = None
        self.move_history = []
        
    def reset_board(self):
        self.board = np.zeros((10, 9), dtype=int)
        # Initialize the pieces on the board
        self.board[0, :] = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Red pieces
        self.board[9, :] = [-1, -2, -3, -4, -5, -6, -7, -8, -9]  # Black pieces
        self.board[2, 1::2] = 10  # Red pawns
        self.board[7, 1::2] = -10  # Black pawns
        self.board[0, 3] = self.board[0, 5] = 11  # Red cannons
        self.board[9, 3] = self.board[9, 5] = -11  # Black cannons
        self.board[0, 1] = self.board[0, 7] = 12  # Red horses
        self.board[9, 1] = self.board[9, 7] = -12  # Black horses