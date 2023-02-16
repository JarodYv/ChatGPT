import sys
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    # main_window.setWindowFlags(Qt.CustomizeWindowHint)
    main_window.showMaximized()
    main_window.show()
    sys.exit(app.exec())
