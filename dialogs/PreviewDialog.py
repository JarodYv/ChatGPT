from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QFileDialog
from Parameters import ImageParameter
from dialogs.preview_dlg import Ui_preview_dlg


class PreviewDialog(QDialog):
    def __init__(self, img: QPixmap):
        super().__init__()
        self.img = img
        self.ui_dialog = Ui_preview_dlg()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(u"图片预览")
        size = ImageParameter["size"]
        if size == "1024x1024":
            qsize = QSize(720, 720)
        elif size == "512x512":
            qsize = QSize(512, 512)
        else:
            qsize = QSize(256, 256)
        self.ui_dialog.preview.setScaledContents(True)
        self.ui_dialog.preview.setMaximumSize(qsize)
        self.ui_dialog.preview.setMinimumSize(qsize)
        self.ui_dialog.preview.setPixmap(self.img)
        self.ui_dialog.download_btn.clicked.connect(self.save_img)

    def save_img(self):
        saveFile, exp = QFileDialog.getSaveFileName(self, u"保存图片", '', '图片文件 (*.png *.jpg)')
        if not saveFile:
            return
        self.img.save(saveFile)
