from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QListWidgetItem
from pages.chat_list import Ui_chat_list
from widgets.ImgItem import ImgItem
from widgets.QItem import QItem
from widgets.AItem import AItem


class ChatListPage(QWidget):
    def __init__(self):
        super(ChatListPage, self).__init__()
        self.ui = Ui_chat_list()
        self.ui.setupUi(self)

    def append_q(self, question: str):
        widget = QItem()
        widget.set_content(question)
        item = QListWidgetItem(self.ui.listWidget)
        item.setSizeHint(QSize(widget.width(), widget.height()))
        # hint_size = widget.sizeHint()
        # print(hint_size.height(), widget.height())
        # lines = question.count("\n") + 1
        # height = lines * 18 + 36
        # if height <= widget.height():
        #     item.setSizeHint(QSize(widget.width(), widget.height()))
        # elif height <= hint_size.height():
        #     item.setSizeHint(hint_size)
        # else:
            # if hint_size.height() > height:
            # item.setSizeHint(QSize(widget.width(), height))
            # else:
            #     item.setSizeHint(QSize(widget.width(), height))
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, widget)

    def append_a(self, answer: str, t: int = 0):
        widget = AItem()
        widget.set_content(answer)
        widget.set_time_cost(t)
        item = QListWidgetItem(self.ui.listWidget)
        item.setSizeHint(QSize(widget.width(), widget.height()))
        hint_size = widget.sizeHint()
        height = widget.height()
        # # print(hint_size.height(), widget.height())
        # lines = answer.count("\n") + 1
        # height = lines * 18 + 36
        # if height <= hint_size.height():
        #     item.setSizeHint(hint_size)
        # else:
        #   item.setSizeHint(QSize(widget.width(), widget.height()))
        # elif height <= hint_size.height():
        #     item.setSizeHint(hint_size)
        # else:
        #     # if hint_size.height() < height:
        #     item.setSizeHint(QSize(widget.width(), height))
        #     # else:
        #     #     item.setSizeHint(QSize(widget.width(), height))
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, widget)
        self.ui.listWidget.scrollToBottom()
        if not answer:
            widget.start_timer()

    def delete_last_item(self) -> int:
        n = self.ui.listWidget.count()
        item = self.ui.listWidget.item(n - 1)
        widget = self.ui.listWidget.itemWidget(item)
        widget.stop_timer()
        t = widget.get_time_cost()
        item = self.ui.listWidget.takeItem(n - 1)
        del item
        return t

    def update_a(self, answer: str):
        t = self.delete_last_item()
        self.append_a(answer, t)

    def show_pic(self, pics: list):
        t = self.delete_last_item()
        widget = ImgItem(pics, t)
        hint_size = widget.sizeHint()
        item = QListWidgetItem(self.ui.listWidget)
        item.setSizeHint(hint_size)
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, widget)
        self.ui.listWidget.scrollToBottom()

