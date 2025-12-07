import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QPainter, QColor, QPen, QFont, QRadialGradient, QBrush
from PySide6.QtCore import Qt, QRectF, QPointF

class XiangQiBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 450, 500)
        self.rows = 10
        self.cols = 9
        self.selected_piece = None
        self._player = 1
        self._board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self._pre_move = []
        self.piece_map = {
                            0: "",
                            1: "车",
                            2: "马",
                            3: "相",
                            4: "士",
                            5: "帅",
                            6: "炮",
                            7: "兵",
                            -1: "车",
                            -2: "马",
                            -3: "象",
                            -4: "士",
                            -5: "将",
                            -6: "炮",
                            -7: "卒"
                        }
    def set_pre_move(self, pre_move=[], selected_piece = None):
        self._pre_move = pre_move
        self.selected_piece = selected_piece
        self.update()
    def set_board(self, board, player):
        self._board = board
        self._player = player
        self._pre_move = None
        self.selected_piece = None
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        w = self.width()
        h = self.height()

        cols = 9
        rows = 10
        margin = min(w,h) * 0.15
        board_w = w - 2 * margin
        board_h = h - 2 * margin
        cell_w = board_w / (cols - 1)
        cell_h = board_h / (rows - 1)

        painter.fillRect(self.rect(),QColor(245, 222, 179))

        pen = QPen(QColor(60, 40, 20))
        pen.setWidth(2)
        painter.setPen(pen)
        outer = QRectF(0.5*margin, 0.5*margin, board_w + 1.0*margin , board_h + 1.0*margin)
        painter.drawRect(outer)
        
        for i in range(cols):
            x = margin + i * cell_w
            top_y = margin
            bottom_y = margin + (rows - 1) * cell_h
            mid_y1 = margin + 4 * cell_h
            mid_y2 = margin + 5 * cell_h
            painter.drawLine(x, top_y, x, mid_y1)
            painter.drawLine(x, mid_y2, x, bottom_y)
        
        for i in range(rows):
            y = margin + i * cell_h
            left_x = margin
            right_x = margin + (cols - 1) * cell_w
            painter.drawLine(left_x, y, right_x, y)
        
        left_palace = margin + 3 * cell_w
        right_palace = margin + 5 * cell_w
        top_palace_y1 = margin + 0 * cell_h
        top_palace_y2 = margin + 2 * cell_h      
        painter.drawLine(left_palace, top_palace_y1, right_palace, top_palace_y2)
        painter.drawLine(right_palace, top_palace_y1, left_palace, top_palace_y2)

        bottom_palace_y1 = margin + 7 * cell_h
        bottom_palace_y2 = margin + 9 * cell_h
        painter.drawLine(left_palace, bottom_palace_y1, right_palace, bottom_palace_y2)
        painter.drawLine(right_palace, bottom_palace_y1, left_palace, bottom_palace_y2)

        # === 楚河汉界 ===
        font = QFont("KaiTi", int(cell_h * 0.5))
        painter.setFont(font)
        painter.setPen(QColor(80, 30, 20))

        text_y = margin + 4 * cell_h + cell_h * 0.1
        painter.drawText(
            QRectF(margin, text_y, (cols - 1) * cell_w, cell_h),
            Qt.AlignCenter,
            "楚河        汉界"
        )
        # === 炮位点 ===
        mark_pen = QPen(QColor(60, 40, 20))
        mark_pen.setWidth(2)
        painter.setPen(mark_pen)

        def draw_mark(x, y, r):
            painter.drawLine(x-r, y-r, x-r/2, y-r/2)
            painter.drawLine(x+r, y-r, x+r/2, y-r/2)
            painter.drawLine(x-r, y+r, x-r/2, y+r/2)
            painter.drawLine(x+r, y+r, x+r/2, y+r/2)

        cannon_positions = [
            (2, 1), (2, 7),    # 上方炮位
            (7, 1), (7, 7)     # 下方炮位
        ]

        for i, j in cannon_positions:
            hx = margin + j * cell_w
            hy = margin + (9 - i) * cell_h
            draw_mark(hx, hy, min(cell_w, cell_h)*0.18)

        # === 兵/卒 初始点 标记 ===
        soldier_positions = [
            (3, 0), (3, 2), (3, 4), (3, 6), (3, 8),  # 红兵
            (6, 0), (6, 2), (6, 4), (6, 6), (6, 8),  # 黑卒
        ]

        for i, j in soldier_positions:
            hx = margin + j * cell_w
            hy = margin + (9 - i) * cell_h
            draw_mark(hx, hy, min(cell_w, cell_h)*0.18)

        # === 棋子和合理走位 ===
        for i, j in ((i, j) for i in range(self.rows) for j in range(self.cols)):
            piece = self._board[i][j]
            if piece:
                cx = margin + j * cell_w
                cy = margin + (9-i) * cell_h
                radius = min(cell_w,cell_h)*0.8
                if self.selected_piece == (i, j):
                    radius *= 1.2
                wood_color = QColor(205, 133, 63)  # 木色
                painter.setBrush(wood_color)
                pen = QPen(QColor(139, 69, 19))
                pen.setWidth(2)
                painter.setPen(pen)
                painter.drawEllipse(cx-radius/2, cy-radius/2, radius, radius)
                if piece > 0:
                    painter.setPen(QColor(255, 0, 0))  # 红棋
                else:
                    painter.setPen(Qt.black)
                font = QFont("SimHei")
                font.setPointSize(int(radius * 0.5))
                font.setBold(True)
                painter.setFont(font)
                painter.drawText(cx-radius/2, cy-radius/2, radius, radius, Qt.AlignCenter, str(self.piece_map[piece]))
            if isinstance(self._pre_move, list) and [i, j] in self._pre_move:
                hx = margin + j * cell_w
                hy = margin + (9 - i) * cell_h
                radius = min(cell_w, cell_h) * 0.2  # 小圆半径

                painter.setPen(Qt.NoPen)
                painter.setBrush(QColor(255, 165, 0, 220)) 
                painter.drawEllipse(hx - radius, hy - radius, radius*2, radius*2)

        painter.end()
    def mousePressEvent(self, event):
        if self._board is None:
            return 
        w, h = self.width(), self.height()
        margin = min(w,h) * 0.15
        cell_w = (w - 2 * margin) / (self.cols - 1)
        cell_h = (h - 2 * margin) / (self.rows - 1)
        x = event.position().x()
        y = event.position().y()
        col = round((x - margin) / cell_w)
        row = self.rows-1-round((y - margin) / cell_h)
        if row<0 or row>=self.rows or col<0 or col>=self.cols:
            return
        clicked_piece = self._board[row][col]
        if self.selected_piece is None:
            if clicked_piece  != 0:
                self.selected_piece = (row, col)
                if self.pre_move_callback:
                    self.pre_move_callback((row, col))
        else:
            pos_x, pos_y = self.selected_piece
            if (pos_x, pos_y) == (row, col):
                self.selected_piece = None
                self._pre_move = None
                self.update()
                return
            if clicked_piece != 0 and (clicked_piece * self._player > 0):
                self.selected_piece = (row, col)
                if self.pre_move_callback:
                    self.pre_move_callback((row, col))
                self.update()
                return
            mov_x, mov_y = row, col
            if self.move_callback:
                self.move_callback((pos_x, pos_y, mov_x, mov_y))
            self.selected_piece = None
            self._pre_move = None
            self.update()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = XiangQiBoard()
    board.show()
    sys.exit(app.exec())