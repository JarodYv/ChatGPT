from PySide6.QtWidgets import QWidget

from dialogs.HelpDialog import HelpDialog
from pages.code_setting import Ui_code_setting
from Parameters import CodeParameter

MODELS = ["code-davinci-002", "code-cushman-001"]


class CodeSettingPage(QWidget):
    def __init__(self):
        super(CodeSettingPage, self).__init__()
        self.ui = Ui_code_setting()
        self.ui.setupUi(self)
        model = CodeParameter["model"]
        if model == "code-davinci-002":
            self.ui.code_davinci.setChecked(True)
        elif model == "code-cushman-001":
            self.ui.code_cushman.setChecked(True)

        self.ui.txt_max_token.setText(str(CodeParameter["max_tokens"]))
        self.ui.temperature_slider.setValue(CodeParameter["temperature"] * 10)
        self.ui.temperature.setText(str(CodeParameter["temperature"]))
        self.ui.frequency_slider.setValue(CodeParameter["frequency_penalty"] * 10)
        self.ui.frequency_penalty.setText(str(CodeParameter["frequency_penalty"]))
        self.ui.presence_slider.setValue(CodeParameter["presence_penalty"] * 10)
        self.ui.presence_penalty.setText(str(CodeParameter["presence_penalty"]))

        self.ui.code_davinci.clicked.connect(lambda: self.set_model(MODELS[0]))
        self.ui.code_cushman.clicked.connect(lambda: self.set_model(MODELS[1]))

        self.ui.txt_max_token.textChanged.connect(lambda v: self.set_max_token(v))
        self.ui.temperature_slider.valueChanged.connect(lambda v: self.set_temperature(v))
        self.ui.frequency_slider.valueChanged.connect(lambda v: self.set_frequency_penalty(v))
        self.ui.presence_slider.valueChanged.connect(lambda v: self.set_presence_penalty(v))

        self.ui.model_help.clicked.connect(lambda: HelpDialog("模型", "assets/docs/code_model.md").exec())
        self.ui.token_help.clicked.connect(lambda: HelpDialog("最大token数", "assets/docs/max_token.md").exec())
        self.ui.temperature_help.clicked.connect(lambda: HelpDialog("采样温度", "assets/docs/temperature.md").exec())
        self.ui.frequency_help.clicked.connect(lambda: HelpDialog("频率惩罚", "assets/docs/frequency_penalty.md").exec())
        self.ui.presence_help.clicked.connect(lambda: HelpDialog("存在惩罚", "assets/docs/presence_penalty.md").exec())

    def set_model(self, model: str):
        CodeParameter["model"] = model

    def set_temperature(self, t: int):
        CodeParameter["temperature"] = t / 10.0
        self.ui.temperature.setText(str(CodeParameter["temperature"]))

    def set_frequency_penalty(self, t: int):
        CodeParameter["frequency_penalty"] = t / 10.0
        self.ui.frequency_penalty.setText(str(CodeParameter["frequency_penalty"]))

    def set_presence_penalty(self, t: int):
        CodeParameter["presence_penalty"] = t / 10.0
        self.ui.presence_penalty.setText(str(CodeParameter["presence_penalty"]))

    def set_max_token(self, t: str):
        t = t.strip()
        CodeParameter["max_tokens"] = int(t)
