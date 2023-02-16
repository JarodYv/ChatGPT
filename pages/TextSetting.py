from PySide6.QtWidgets import QWidget, QListWidget

from dialogs.HelpDialog import HelpDialog
from pages.text_setting import Ui_text_setting
from Parameters import TextParameter

MODELS = ["text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001"]


class TextSettingPage(QWidget):
    def __init__(self):
        super(TextSettingPage, self).__init__()
        self.ui = Ui_text_setting()
        self.ui.setupUi(self)
        model = TextParameter["model"]
        if model == "text-davinci-003":
            self.ui.txt_davinci.setChecked(True)
        elif model == "text-curie-001":
            self.ui.txt_curie.setChecked(True)
        elif model == "text-babbage-001":
            self.ui.txt_babbage.setChecked(True)
        elif model == "text-ada-001":
            self.ui.txt_ada.setChecked(True)

        self.ui.txt_max_token.setText(str(TextParameter["max_tokens"]))
        self.ui.temperature_slider.setValue(TextParameter["temperature"] * 10)
        self.ui.temperature.setText(str(TextParameter["temperature"]))
        self.ui.frequency_slider.setValue(TextParameter["frequency_penalty"] * 10)
        self.ui.frequency_penalty.setText(str(TextParameter["frequency_penalty"]))
        self.ui.presence_slider.setValue(TextParameter["presence_penalty"] * 10)
        self.ui.presence_penalty.setText(str(TextParameter["presence_penalty"]))

        self.ui.txt_davinci.clicked.connect(lambda: self.set_model(MODELS[0]))
        self.ui.txt_curie.clicked.connect(lambda: self.set_model(MODELS[1]))
        self.ui.txt_babbage.clicked.connect(lambda: self.set_model(MODELS[2]))
        self.ui.txt_ada.clicked.connect(lambda: self.set_model(MODELS[3]))
        self.ui.model_help.clicked.connect(lambda: HelpDialog("模型", "assets/docs/text_model.md").exec())
        self.ui.token_help.clicked.connect(lambda: HelpDialog("最大token数", "assets/docs/max_token.md").exec())
        self.ui.temperature_help.clicked.connect(lambda: HelpDialog("采样温度", "assets/docs/temperature.md").exec())
        self.ui.frequency_help.clicked.connect(lambda: HelpDialog("频率惩罚", "assets/docs/frequency_penalty.md").exec())
        self.ui.presence_help.clicked.connect(lambda: HelpDialog("存在惩罚", "assets/docs/presence_penalty.md").exec())

        self.ui.txt_max_token.textChanged.connect(lambda v: self.set_max_token(v))
        self.ui.temperature_slider.valueChanged.connect(lambda v: self.set_temperature(v))
        self.ui.frequency_slider.valueChanged.connect(lambda v: self.set_frequency_penalty(v))
        self.ui.presence_slider.valueChanged.connect(lambda v: self.set_presence_penalty(v))

    def set_model(self, model: str):
        TextParameter["model"] = model

    def set_temperature(self, t: int):
        TextParameter["temperature"] = t / 10.0
        self.ui.temperature.setText(str(TextParameter["temperature"]))

    def set_frequency_penalty(self, t: int):
        TextParameter["frequency_penalty"] = t / 10.0
        self.ui.frequency_penalty.setText(str(TextParameter["frequency_penalty"]))

    def set_presence_penalty(self, t: int):
        TextParameter["presence_penalty"] = t / 10.0
        self.ui.presence_penalty.setText(str(TextParameter["presence_penalty"]))

    def set_max_token(self, t: str):
        t = t.strip()
        TextParameter["max_tokens"] = int(t)
