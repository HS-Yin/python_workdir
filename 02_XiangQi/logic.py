import numpy as np
class XiangQi:
    def __init__(self):
        self.board = np.zeros((10, 9), dtype=int)
        self.reset_board()
        self.current_player = 1  # 1 for Red, -1 for Black
        self.game_over = False
        self.winner = None
    def reset_board(self):
        # Initialize the board with starting positions
        self.current_player = 1
        self.board[0] = [1, 2, 3, 4, 5, 4, 3, 2, 1]
        self.board[1] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[2] = [0, 6, 0, 0, 0, 0, 0, 6, 0]
        self.board[3] = [7, 0, 7, 0, 7, 0, 7, 0, 7]
        self.board[4] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[5] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[6] = [-7, 0, -7, 0, -7, 0, -7, 0, -7]
        self.board[7] = [0, -6, 0, 0, 0, 0, 0, -6, 0]
        self.board[8] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.board[9] = [-1, -2, -3, -4, -5, -4, -3, -2, -1]
    def step(self, move):
        
        pos_x, pos_y, mov_x, mov_y = move
        pos_x, pos_y, mov_x, mov_y = int(pos_x), int(pos_y), int(mov_x), int(mov_y)
      
        piece = self.board[pos_x, pos_y]
        target = self.board[mov_x, mov_y]
        # Check if move is within bounds
        if all (0 <= x <=9 for x in (pos_x, pos_y, mov_x, mov_y)) == False:
            return "提示: 超出范围"
        # check basic move rules
        if piece == 0:
            return 0
        if int(piece) * int(target) > 0:
            return "提示: 无效走棋"
        if (self.current_player == 1 and piece < 0) or (self.current_player == -1 and piece > 0):
            return "提示：不是你的回合"
        # Check piece-specific move rules
        if piece == 1 or piece == -1:
            if pos_x == mov_x and pos_y != mov_y:
                indy = 1 if mov_y > pos_y else -1
                for y in range(pos_y + indy, mov_y, indy):
                    if self.board[pos_x, y] != 0:
                        return "提示: 车走棋错误"
            elif pos_y == mov_y and pos_x != mov_x:
                indx = 1 if mov_x > pos_x else -1
                for x in range(pos_x + indx, mov_x, indx):
                    if self.board[x, pos_y] != 0:
                        return "提示: 车走棋错误"
            else:
                return "提示: 车走棋错误"
        elif piece == 2 or piece == -2:
            if abs(pos_x - mov_x) == 2 and abs(pos_y - mov_y) == 1:
                if self.board[(pos_x + mov_x) // 2, pos_y] != 0:
                    return "提示: 马走棋错误"
            elif abs(pos_x - mov_x) == 1 and abs(pos_y - mov_y) == 2:
                if self.board[pos_x, (pos_y + mov_y) // 2] != 0:
                    return "提示: 马走棋错误"
            else:
                return "提示: 马走棋错误"
                return
        elif piece == 3 or piece == -3:
            if abs(pos_x - mov_x) == 2 and abs(pos_y - mov_y) == 2:
                if self.board[(pos_x + mov_x) // 2, (pos_y + mov_y) // 2] != 0:
                    return "提示: 相/象走棋错误"
            else:
                return "提示: 相/象走棋错误"
        elif piece == 4 or piece == -4:
            if abs(pos_x - mov_x) == 1 and abs(pos_y - mov_y) == 1:
                if mov_y not in [4,5,6]:
                    return "提示: 士走棋错误"
                if mov_x not in [0,1,2] and self.current_player == 1:
                    return "提示: 士走棋错误"
                if mov_x not in [7,8,9] and self.current_player == -1:
                   return "提示: 士走棋错误"
            else:
                return "提示: 士走棋错误"
        elif piece == 5 or piece == -5:
            if (abs(pos_x - mov_x) == 1 and pos_y == mov_y) or (pos_x == mov_x and abs(pos_y - mov_y) == 1):
                if mov_y not in [4,5,6]:
                    return "提示: 帅/将走棋错误"
                if mov_x not in [0,1,2] and self.current_player == 1:
                    return "提示: 帅/将走棋错误"
                if mov_x not in [7,8,9] and self.current_player == -1:
                    return "提示: 帅/将走棋错误"
            else:
                return "提示: 帅/将走棋错误"
        elif piece == 6 or piece == -6:
            mid_num = 0
            if pos_x == mov_x and pos_y != mov_y:
                indy = 1 if mov_y > pos_y else -1
                for y in range(pos_y + indy, mov_y, indy):
                    if self.board[pos_x, y] != 0:
                        mid_num = mid_num + 1
            elif pos_y == mov_y and pos_x != mov_x:
                indx = 1 if mov_x > pos_x else -1
                for x in range(pos_x + indx, mov_x, indx):
                    if self.board[x, pos_y] != 0:
                        mid_num = mid_num + 1
            else:
                return "提示: 炮走棋错误"
            if not (mid_num == 1 and target != 0) and not (mid_num == 0 and target == 0):
                return "提示: 炮走棋错误"
        elif piece == 7 or piece == -7:
            if pos_y == mov_y and abs(pos_x - mov_x) == 1:
                indx = 1 if mov_x > pos_x else -1
                if indx * self.current_player < 0:
                    return "提示: 兵/卒走棋错误"
            elif abs(pos_y - mov_y) == 1 and pos_x == mov_x:
                if (self.current_player == 1 and pos_x < 5) or (self.current_player == -1 and pos_x > 4):
                    return "提示: 兵/卒走棋错误"
        else:
            return "提示: 走棋错误"
        # Execute the move
        self.board[mov_x, mov_y] = piece 
        self.board[pos_x, pos_y] = 0
        self.current_player *= -1
        # final win
        if target == 5:
            return 2
        elif target == -5:
            return -2
        else:
            return 1 
    def get_board(self):
        return self.board.copy()        
if __name__ == "__main__":
    game = XiangQi()
    while game.game_over == False:
        usr_input = input(" ")
        if usr_input.lower() == 'exit':
            break
        game.step(usr_input)
        print(game.board)
