from PySide6.QtCore import QObject, Signal


class ImageDownloadSignal(QObject):
    result = Signal(bytes)
