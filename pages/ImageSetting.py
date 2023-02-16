from PySide6.QtWidgets import QWidget
from pages.image_setting import Ui_img_setting
from Parameters import ImageParameter

SIZES = ["1024x1024", "512x512", "256x256"]


class ImageSettingPage(QWidget):
    def __init__(self):
        super(ImageSettingPage, self).__init__()
        self.ui = Ui_img_setting()
        self.ui.setupUi(self)
        size = ImageParameter["size"]
        if size == "1024x1024":
            self.ui.size_1024.setChecked(True)
        elif size == "512x512":
            self.ui.size_512.setChecked(True)
        elif size == "256x256":
            self.ui.size_256.setChecked(True)

        self.ui.img_num.setText(str(ImageParameter["n"]))

        self.ui.size_1024.clicked.connect(lambda: self.set_size(SIZES[0]))
        self.ui.size_512.clicked.connect(lambda: self.set_size(SIZES[1]))
        self.ui.size_256.clicked.connect(lambda: self.set_size(SIZES[2]))

        self.ui.img_num.textChanged.connect(lambda v: self.set_img_num(v))

    def set_size(self, s: str):
        ImageParameter["size"] = s

    def set_img_num(self, n: str):
        n = n.strip()
        ImageParameter["n"] = int(n)
