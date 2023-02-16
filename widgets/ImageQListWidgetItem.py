import requests
from PySide6.QtCore import QSize, QThread
from PySide6.QtGui import QPixmap, QMovie, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem, QLabel, QVBoxLayout
from signals.ImageDownloadSignal import ImageDownloadSignal


class ImageQListWidgetItem(QListWidgetItem):
    def __init__(self, img_path):
        super().__init__()

        self.img_path = img_path
        self.photo = None
        # 自定义item中的widget 用来显示自定义的内容
        self.widget = QWidget()
        # 用来显示avatar(图像)
        self.avatarLabel = QLabel()
        # 设置大小
        self.scale_size = QSize(150, 150)
        self.avatarLabel.setMinimumSize(self.scale_size)
        self.avatarLabel.setMaximumSize(self.scale_size)
        self.avatarLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avatarLabel.setStyleSheet("""
                    QWidget{
                        background-color:#FFFFFF;
                    }
                """)
        # 显示占位图片
        # self.avatarLabel.setPixmap(QPixmap(u":/assets/assets/image.png"))
        self.movie = QMovie(u":/assets/assets/loading.gif")
        self.avatarLabel.setMovie(self.movie)
        # 设置布局用来对nameLabel和avatarLabel进行布局
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.avatarLabel)
        self.vbox.addStretch(1)
        # 设置widget的布局
        self.widget.setLayout(self.vbox)
        # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        self.setSizeHint(self.widget.sizeHint())

    def download_image(self):
        thread = ImageQListWidgetItem.DownloadThread(self.widget, self.img_path)
        thread.started.connect(lambda: self.start_movie())
        thread.signal.result.connect(self.show_image)
        thread.finished.connect(lambda: self.remove_movie())
        thread.start()

    def start_movie(self):
        self.movie.start()

    def remove_movie(self):
        self.movie.stop()

    def show_image(self, content):
        self.photo = QPixmap()
        self.photo.loadFromData(content)
        self.avatarLabel.setPixmap(self.photo.scaled(self.scale_size))
        # 图像自适应窗口大小
        self.avatarLabel.setScaledContents(True)

    def image_path(self):
        return self.img_path

    class DownloadThread(QThread):
        def __init__(self, parent, url):
            super().__init__(parent)
            self.url = url
            self.signal = ImageDownloadSignal()

        def run(self):
            req = requests.get(self.url)
            self.signal.result.emit(req.content)
