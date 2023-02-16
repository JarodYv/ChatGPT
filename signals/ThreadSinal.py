from PySide6.QtCore import QObject, Signal


class ThreadSignal(QObject):
    result = Signal(dict)
