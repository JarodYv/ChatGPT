from PySide6 import QtGui, QtCore
from PySide6.QtCore import QThread
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QApplication
import Parameters
from dialogs.AboutDialog import AboutDialog
from main_window import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from pages.TextSetting import TextSettingPage
from pages.CodeSetting import CodeSettingPage
from pages.ImageSetting import ImageSettingPage
from pages.ChatList import ChatListPage
import openai

from signals.ThreadSinal import ThreadSignal

openai.api_key = "YOUR_API_KEY"


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.func = 0
        self.current_page = None
        self.chat_list = None
        self.ui.btn_github.clicked.connect(
            lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://www.planyun.com')))
        self.ui.btn_api.clicked.connect(
            lambda: QtGui.QDesktopServices.openUrl(QtCore.QUrl('https://platform.openai.com/examples')))
        self.ui.btn_about.clicked.connect(lambda: AboutDialog().exec())
        self.ui.menu_text.clicked.connect(lambda: self.goto_page(0))
        self.ui.menu_code.clicked.connect(lambda: self.goto_page(1))
        self.ui.menu_image.clicked.connect(lambda: self.goto_page(2))
        self.ui.prompt_send.clicked.connect(self.send)
        self.ui.prompt_input.textChanged.connect(self.on_text_changed)
        shortcut = QShortcut(QKeySequence("Ctrl+S"), self.ui.prompt_input)
        shortcut.activated.connect(self.send)
        self.ui.prompt_input.installEventFilter(self)
        self.on_text_changed()
        self.goto_page(0)

    def remove_current_page(self):
        if self.current_page:
            layout = self.ui.response_area.layout()
            layout.removeWidget(self.current_page)
            self.current_page.deleteLater()
            self.current_page = None

    def goto_page(self, index: int = 0):
        self.remove_current_page()
        if index == 1:
            self.current_page = CodeSettingPage()
        elif index == 2:
            self.current_page = ImageSettingPage()
        else:
            self.current_page = TextSettingPage()
        layout = self.ui.response_area.layout()
        layout.addWidget(self.current_page)
        self.func = index
        self.chat_list = None

    def send(self):
        prompt = self.ui.prompt_input.toPlainText().strip()
        if prompt:
            if self.chat_list is None:
                self.chat_list = ChatListPage()
            if self.current_page != self.chat_list:
                self.remove_current_page()
                self.current_page = self.chat_list
                layout = self.ui.response_area.layout()
                layout.addWidget(self.current_page)
            self.chat_list.append_q(prompt)
            self.chat_list.append_a("")
            thread = MainWindow.RequestThread(self, prompt, self.func)
            thread.started.connect(lambda: self.start_timer())
            thread.signal.result.connect(self.show_answer)
            thread.finished.connect(lambda: self.remove_timer())
            thread.start()
        self.ui.prompt_input.setPlainText("")

    def on_text_changed(self):
        line_count = self.ui.prompt_input.document().lineCount()
        if line_count == 0:
            line_count = 1
        height = self.ui.prompt_input.fontMetrics().lineSpacing() + 2  # 字体每一行的高度
        # self.ui.prompt_input.setMinimumHeight(row_count * height)
        h = line_count * height + 76
        self.ui.prompt_container.setMaximumHeight(h)
        self.ui.prompt_container.setMinimumHeight(h)

    def show_answer(self, response: dict):
        if self.func == 2:
            data = response.get("data", None)
            if data:
                self.chat_list.show_pic(data)
                return
        choices = response["choices"][0]
        text = choices.get("text", "")
        self.chat_list.update_a(text.strip())

    def start_timer(self):
        self.ui.prompt_input.setDisabled(True)
        self.ui.prompt_send.setDisabled(True)

    def remove_timer(self):
        self.ui.prompt_input.setEnabled(True)
        self.ui.prompt_send.setEnabled(True)

    def resizeEvent(self, event):
        event.accept()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.KeyPress and obj is self.ui.prompt_input:
            if event.key() == QtCore.Qt.Key.Key_Return and self.ui.prompt_input.hasFocus():
                modifiers = QApplication.keyboardModifiers()
                if not modifiers:
                    self.send()
                    return True
        return super().eventFilter(obj, event)

    class RequestThread(QThread):
        def __init__(self, parent, prompt, func):
            super().__init__(parent)
            self.prompt = prompt
            self.func = func
            self.signal = ThreadSignal()

        def run(self):
            try:
                if self.func == 0:
                    # print(Parameters.TextParameter)
                    response = openai.Completion.create(prompt=self.prompt,
                                                        **Parameters.TextParameter
                                                        )
                elif self.func == 1:
                    # print(Parameters.CodeParameter)
                    response = openai.Completion.create(prompt=self.prompt,
                                                        **Parameters.CodeParameter
                                                        )
                else:
                    # print(Parameters.ImageParameter)
                    response = openai.Image.create(prompt=self.prompt,
                                                   **Parameters.ImageParameter
                                                   )
                self.signal.result.emit(response)
            except Exception as e:
                self.signal.result.emit({"choices": [{"text": f"接口报错: {e}"}]})
