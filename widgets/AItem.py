from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget
from widgets.a_item import Ui_a_item
import math


class AItem(QWidget):
    def __init__(self):
        super(AItem, self).__init__()
        self.ui = Ui_a_item()
        self.ui.setupUi(self)
        self.timer = None
        self.count = 0

    # def update_height(self):
    #     line_count = self.ui.answer.document().lineCount()
    #     if line_count == 0:
    #         line_count = 1
    #     height = self.ui.answer.fontMetrics().lineSpacing() + 2  # 字体每一行的高度
    #     h = line_count * height + 58
    #     print(line_count, height, h)
    #     if h < 100:
    #         h = 100
    #     self.setMaximumHeight(h)
    #     self.setMinimumHeight(h)

    def set_content(self, text: str):
        self.ui.answer.setText(text)
        lines = text.split("\n")
        width = float(self.ui.answer.width())
        line_count = 0
        for line in lines:
            if line:
                line_width = self.ui.answer.fontMetrics().horizontalAdvance(line)
                line_count += int(math.ceil(line_width / width))
            else:
                line_count += 1
        height = self.ui.answer.fontMetrics().lineSpacing() + 1  # 字体每一行的高度
        h = line_count * height + 58
        if h < 100:
            h = 100
        self.setMaximumHeight(h)
        self.setMinimumHeight(h)

    def set_time_cost(self, time_cost: int):
        if time_cost:
            self.ui.time_cost.setText(f"{time_cost}s")

    def add_image(self, html: str):
        self.ui.answer.setHtml(html)

    def start_timer(self):
        self.count = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_tock)
        self.timer.start(500)

    def stop_timer(self):
        self.timer.stop()

    def tick_tock(self):
        self.count += 1
        if self.count % 2 == 1:
            self.ui.answer.setText(u"▉")
        else:
            self.ui.answer.setText(u"")

    def get_time_cost(self) -> int:
        return self.count // 2
