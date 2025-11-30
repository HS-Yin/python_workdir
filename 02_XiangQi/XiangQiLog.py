# log_widget.py
from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt

class XiangQiLog(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)       # 日志框只读，不允许手动编辑
        self.setAcceptRichText(False)  # 文本纯文本显示
        self.setAlignment(Qt.AlignTop) # 文本顶部对齐

    def add_log(self, text):
        """向日志框添加一条新日志"""
        self.append(text)
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())  # 自动滚动到底部