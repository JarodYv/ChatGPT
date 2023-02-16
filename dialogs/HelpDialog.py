from PySide6.QtWidgets import QDialog

from dialogs.help_dlg import Ui_help_dlg
from file_utils import resource_path


class HelpDialog(QDialog):
    def __init__(self, title: str, doc: str):
        super().__init__()
        self.ui_dialog = Ui_help_dlg()
        self.ui_dialog.setupUi(self)
        self.setWindowTitle(title)
        with open(resource_path(doc), encoding='utf-8') as f:
            content = f.read()
            self.ui_dialog.textBrowser.setMarkdown(content)
