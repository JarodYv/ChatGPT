from PySide6.QtWidgets import QWidget
from widgets.q_item import Ui_q_item
import math


class QItem(QWidget):
    def __init__(self):
        super(QItem, self).__init__()
        self.ui = Ui_q_item()
        self.ui.setupUi(self)

    def set_content(self, text: str):
        self.ui.question.setText(text)
        lines = text.split("\n")
        width = float(self.ui.question.width())
        line_count = 0
        for line in lines:
            if line:
                line_width = self.ui.question.fontMetrics().horizontalAdvance(line)
                line_count += int(math.ceil(line_width / width))
            else:
                line_count += 1
        height = self.ui.question.fontMetrics().lineSpacing() + 1  # 字体每一行的高度
        h = line_count * height + 58
        if h < 72:
            h = 72
        self.setMaximumHeight(h)
        self.setMinimumHeight(h)
