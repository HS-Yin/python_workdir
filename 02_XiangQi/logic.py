import numpy as np

class XiangQi:
    def __init__(self):
        self.board = np.zeros((10, 9), dtype=int)
        self.reset_board()
        self.current_player = 1  # 1 for Red, -1 for Black
        self.game_over = False
        self.winner = None
        self.move_history = [] 
        print(self.board) 
    def reset_board(self):
        # Initialize the board with starting positions
        self.board[0] = ['1', '2', '3', '4', '5', '4', '3', '2', '1']
        self.board[1] = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.board[2] = ['0', '6', '0', '0', '0', '0', '0', '6', '0']
        self.board[3] = ['7', '0', '7', '0', '7', '0', '7', '0', '7']
        self.board[4] = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.board[5] = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.board[6] = ['-7', '0', '-7', '0', '-7', '0', '-7', '0', '-7']
        self.board[7] = ['0', '-6', '0', '0', '0', '0', '0', '-6', '0']
        self.board[8] = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
        self.board[9] = ['-1', '-2', '-3', '-4', '-5', '-4', '-3', '-2', '-1']
    def step(self,move):
        move_true = False
        move_from, move_to = move
        piece = self.board[move_from]
        if piece == '0':
            print("error0")
            return
        if piece == '1' or piece == '-1':
            diff = [b - a for a, b in zip(move_from, move_to)]
            zero_count = [sum(1 for d in diff if d == 0)]
            if zero_count != 1:
                print("error1")
                return
            else:
                pass
        if move_true:
            self.board[move_to] = piece
            self.board[move_from] = '0'

if __name__ == "__main__":
    game = XiangQi()
    while game.game_over == False:
        input = input(" ")
        if input.lower() == 'exit':
            break
        game.step(eval(input))
        print(game.board)
