import sys 
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QRectF

class XiangQiBoard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(100, 100, 450, 500)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = XiangQiBoard()
    board.show()
    sys.exit(app.exec())