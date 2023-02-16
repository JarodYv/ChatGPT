from PySide6.QtWidgets import QWidget

from widgets.ImageQListWidgetItem import ImageQListWidgetItem
from widgets.img_item import Ui_img_item
from dialogs.PreviewDialog import PreviewDialog


class ImgItem(QWidget):
    def __init__(self, pics: list, time_cost: int = 0):
        super(ImgItem, self).__init__()
        self.ui = Ui_img_item()
        self.ui.setupUi(self)
        self.ui.listWidget.itemClicked.connect(self.show_pic)
        if time_cost:
            self.ui.time_cost.setText(f"{time_cost}s")
        for p in pics:
            url = p["url"]
            img_item = ImageQListWidgetItem(url)
            self.ui.listWidget.addItem(img_item)
            self.ui.listWidget.setItemWidget(img_item, img_item.widget)
            img_item.download_image()

    def show_pic(self, item):
        img = item.photo
        PreviewDialog(img).exec()
