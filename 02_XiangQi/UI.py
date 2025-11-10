import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QRectF

class XiangQiUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 450, 500)
        self.rows = 10
        self.cols = 9
        self.selected_piece = None
        self._board = [[None for _ in range(self.cols)] for _ in range(self.rows)]
    
    def set_board(self, board_state):
        self._board = board_state
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

        # painter.fillRect(self.rect(),QColor(245, 222, 179))
        painter.fillRect(self.rect(),QColor(255, 255, 255))

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
        
        for i in range(self.rows):
            for j in range(self.cols):
                piece = self._board[i][j]
                if piece:
                    cx = margin + j * cell_w
                    cy = margin + i * cell_h
                    radius = min(cell_w,cell_h)*0.4
                    painter.setBrush(Qt.black if piece > 0 else Qt.red)
                    painter.drawEllipse(cx-radius/2, cy-radius/2, radius, radius)
                    painter.setPen(Qt.white)
                    painter.drawText(cx-radius/2, cy-radius/2, radius, radius, Qt.AlignCenter, str(abs(piece)))
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
        row = round((y - margin) / cell_h)
        if row<0 or row>=self.rows or col<0 or col>=self.cols:
            return
        if self.selected_piece is None:
            print("first_press",row, col, self._board[row][col])
            if self._board[row][col] is not None:
                self.selected_piece = (row, col)  
        else:
            pos_x, pos_y = self.selected_piece
            mov_x, mov_y = row, col
            if self.move_callback:
                self.move_callback((pos_x, pos_y, mov_x, mov_y))
            self.selected_piece = None
        self.update()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = XiangQiUI()
    board.show()
    sys.exit(app.exec())