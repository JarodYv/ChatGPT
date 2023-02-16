# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'code_setting.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_code_setting(object):
    def setupUi(self, code_setting):
        if not code_setting.objectName():
            code_setting.setObjectName(u"code_setting")
        code_setting.resize(560, 631)
        code_setting.setMinimumSize(QSize(0, 0))
        code_setting.setMaximumSize(QSize(16777215, 16777215))
        code_setting.setStyleSheet(u"background-color: rgb(52, 53, 65);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(code_setting)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.widget = QWidget(code_setting)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(560, 0))
        self.widget.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 40))
        self.widget_3.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(24, 24))
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setPixmap(QPixmap(u":/assets/assets/model.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.model_help = QPushButton(self.widget_3)
        self.model_help.setObjectName(u"model_help")
        self.model_help.setMinimumSize(QSize(24, 24))
        self.model_help.setMaximumSize(QSize(24, 24))
        self.model_help.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets/assets/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.model_help.setIcon(icon)
        self.model_help.setIconSize(QSize(18, 18))
        self.model_help.setFlat(True)

        self.horizontalLayout_2.addWidget(self.model_help)

        self.horizontalSpacer_3 = QSpacerItem(521, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_16 = QWidget(self.widget_2)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout = QHBoxLayout(self.widget_16)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.code_davinci = QPushButton(self.widget_16)
        self.code_davinci.setObjectName(u"code_davinci")
        self.code_davinci.setMinimumSize(QSize(160, 60))
        self.code_davinci.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(62, 63, 75);\n"
"	background-color: rgb(62, 63, 75);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 1px solid rgb(32, 33, 35);\n"
"	background-color: rgb(32, 33, 35);\n"
"}")
        self.code_davinci.setCheckable(True)
        self.code_davinci.setChecked(True)
        self.code_davinci.setAutoExclusive(True)
        self.code_davinci.setFlat(True)

        self.horizontalLayout.addWidget(self.code_davinci)

        self.code_cushman = QPushButton(self.widget_16)
        self.code_cushman.setObjectName(u"code_cushman")
        self.code_cushman.setMinimumSize(QSize(160, 60))
        self.code_cushman.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(62, 63, 75);\n"
"	background-color: rgb(62, 63, 75);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 1px solid rgb(32, 33, 35);\n"
"	background-color: rgb(32, 33, 35);\n"
"}")
        self.code_cushman.setCheckable(True)
        self.code_cushman.setChecked(False)
        self.code_cushman.setAutoExclusive(True)
        self.code_cushman.setFlat(True)

        self.horizontalLayout.addWidget(self.code_cushman)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addWidget(self.widget_16)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_13 = QWidget(self.widget)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_5 = QVBoxLayout(self.widget_13)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 40))
        self.widget_14.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(24, 24))
        self.label_10.setMaximumSize(QSize(24, 24))
        self.label_10.setPixmap(QPixmap(u":/assets/assets/token.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.txt_max_token = QLineEdit(self.widget_14)
        self.txt_max_token.setObjectName(u"txt_max_token")
        self.txt_max_token.setStyleSheet(u"padding: 0 6px;")
        self.txt_max_token.setFrame(True)

        self.horizontalLayout_10.addWidget(self.txt_max_token)

        self.token_help = QPushButton(self.widget_14)
        self.token_help.setObjectName(u"token_help")
        self.token_help.setMinimumSize(QSize(24, 24))
        self.token_help.setMaximumSize(QSize(24, 24))
        self.token_help.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        self.token_help.setIcon(icon)
        self.token_help.setIconSize(QSize(18, 18))
        self.token_help.setFlat(True)

        self.horizontalLayout_10.addWidget(self.token_help)


        self.verticalLayout_5.addWidget(self.widget_14)


        self.verticalLayout_6.addWidget(self.widget_13)

        self.widget_15 = QWidget(self.widget)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout = QGridLayout(self.widget_15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.widget_4 = QWidget(self.widget_15)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 40))
        self.widget_5.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(24, 24))
        self.label_4.setMaximumSize(QSize(24, 24))
        self.label_4.setPixmap(QPixmap(u":/assets/assets/temperature.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.temperature_help = QPushButton(self.widget_5)
        self.temperature_help.setObjectName(u"temperature_help")
        self.temperature_help.setMinimumSize(QSize(24, 24))
        self.temperature_help.setMaximumSize(QSize(24, 24))
        self.temperature_help.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        self.temperature_help.setIcon(icon)
        self.temperature_help.setIconSize(QSize(18, 18))
        self.temperature_help.setFlat(True)

        self.horizontalLayout_3.addWidget(self.temperature_help)

        self.horizontalSpacer_4 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget_5)

        self.temperature = QLabel(self.widget_4)
        self.temperature.setObjectName(u"temperature")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.temperature.setFont(font2)
        self.temperature.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.temperature)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setPointSize(8)
        self.label_12.setFont(font3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_12)

        self.temperature_slider = QSlider(self.widget_6)
        self.temperature_slider.setObjectName(u"temperature_slider")
        self.temperature_slider.setStyleSheet(u"QSlider{\n"
"	margin-left: 50px;\n"
"}")
        self.temperature_slider.setMaximum(10)
        self.temperature_slider.setSingleStep(1)
        self.temperature_slider.setPageStep(1)
        self.temperature_slider.setValue(0)
        self.temperature_slider.setOrientation(Qt.Horizontal)
        self.temperature_slider.setTickPosition(QSlider.TicksAbove)

        self.horizontalLayout_4.addWidget(self.temperature_slider)

        self.label_13 = QLabel(self.widget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_13)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.gridLayout.addWidget(self.widget_4, 0, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_15)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 40))
        self.widget_8.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(24, 24))
        self.label_6.setMaximumSize(QSize(24, 24))
        self.label_6.setPixmap(QPixmap(u":/assets/assets/frequency.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.frequency_help = QPushButton(self.widget_8)
        self.frequency_help.setObjectName(u"frequency_help")
        self.frequency_help.setMinimumSize(QSize(24, 24))
        self.frequency_help.setMaximumSize(QSize(24, 24))
        self.frequency_help.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        self.frequency_help.setIcon(icon)
        self.frequency_help.setIconSize(QSize(18, 18))
        self.frequency_help.setFlat(True)

        self.horizontalLayout_5.addWidget(self.frequency_help)

        self.horizontalSpacer_7 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.frequency_penalty = QLabel(self.widget_7)
        self.frequency_penalty.setObjectName(u"frequency_penalty")
        self.frequency_penalty.setFont(font2)
        self.frequency_penalty.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.frequency_penalty)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.label_14 = QLabel(self.widget_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.frequency_slider = QSlider(self.widget_9)
        self.frequency_slider.setObjectName(u"frequency_slider")
        self.frequency_slider.setStyleSheet(u"QSlider{\n"
"	margin-left: 50px;\n"
"}")
        self.frequency_slider.setMinimum(-20)
        self.frequency_slider.setMaximum(20)
        self.frequency_slider.setSingleStep(1)
        self.frequency_slider.setPageStep(1)
        self.frequency_slider.setValue(0)
        self.frequency_slider.setTracking(True)
        self.frequency_slider.setOrientation(Qt.Horizontal)
        self.frequency_slider.setInvertedAppearance(False)
        self.frequency_slider.setInvertedControls(False)
        self.frequency_slider.setTickPosition(QSlider.TicksAbove)
        self.frequency_slider.setTickInterval(0)

        self.horizontalLayout_6.addWidget(self.frequency_slider)

        self.label_15 = QLabel(self.widget_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_15)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addWidget(self.widget_9)


        self.gridLayout.addWidget(self.widget_7, 0, 1, 1, 1)

        self.widget_10 = QWidget(self.widget_15)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_4 = QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 40))
        self.widget_11.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(24, 24))
        self.label_8.setMaximumSize(QSize(24, 24))
        self.label_8.setPixmap(QPixmap(u":/assets/assets/presence.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.presence_help = QPushButton(self.widget_11)
        self.presence_help.setObjectName(u"presence_help")
        self.presence_help.setMinimumSize(QSize(24, 24))
        self.presence_help.setMaximumSize(QSize(24, 24))
        self.presence_help.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        self.presence_help.setIcon(icon)
        self.presence_help.setIconSize(QSize(18, 18))
        self.presence_help.setFlat(True)

        self.horizontalLayout_8.addWidget(self.presence_help)

        self.horizontalSpacer_12 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout_4.addWidget(self.widget_11)

        self.presence_penalty = QLabel(self.widget_10)
        self.presence_penalty.setObjectName(u"presence_penalty")
        self.presence_penalty.setFont(font2)
        self.presence_penalty.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.presence_penalty)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.presence_slider = QSlider(self.widget_12)
        self.presence_slider.setObjectName(u"presence_slider")
        self.presence_slider.setStyleSheet(u"QSlider{\n"
"	margin-left: 50px;\n"
"}")
        self.presence_slider.setMinimum(-20)
        self.presence_slider.setMaximum(20)
        self.presence_slider.setSingleStep(1)
        self.presence_slider.setPageStep(1)
        self.presence_slider.setValue(0)
        self.presence_slider.setTracking(True)
        self.presence_slider.setOrientation(Qt.Horizontal)
        self.presence_slider.setInvertedAppearance(False)
        self.presence_slider.setInvertedControls(False)
        self.presence_slider.setTickPosition(QSlider.TicksAbove)
        self.presence_slider.setTickInterval(0)

        self.horizontalLayout_9.addWidget(self.presence_slider)

        self.label_17 = QLabel(self.widget_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.verticalLayout_4.addWidget(self.widget_12)


        self.gridLayout.addWidget(self.widget_10, 0, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_15)

        self.verticalSpacer_2 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.retranslateUi(code_setting)

        QMetaObject.connectSlotsByName(code_setting)
    # setupUi

    def retranslateUi(self, code_setting):
        code_setting.setWindowTitle(QCoreApplication.translate("code_setting", u"Form", None))
        self.label.setText(QCoreApplication.translate("code_setting", u"\u4ee3\u7801\u751f\u6210", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("code_setting", u"\u6a21\u578b\u9009\u62e9", None))
        self.model_help.setText("")
        self.code_davinci.setText(QCoreApplication.translate("code_setting", u"code-davinci-002", None))
        self.code_cushman.setText(QCoreApplication.translate("code_setting", u"code-cushman-001", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("code_setting", u"\u6700\u5927token\u6570\uff1a", None))
        self.txt_max_token.setText(QCoreApplication.translate("code_setting", u"16", None))
        self.token_help.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("code_setting", u"\u91c7\u6837\u6e29\u5ea6", None))
        self.temperature_help.setText("")
        self.temperature.setText(QCoreApplication.translate("code_setting", u"0", None))
        self.label_12.setText(QCoreApplication.translate("code_setting", u"\u66f4\u7a33\u5b9a", None))
        self.label_13.setText(QCoreApplication.translate("code_setting", u"\u66f4\u521b\u610f", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("code_setting", u"\u9891\u7387\u60e9\u7f5a", None))
        self.frequency_help.setText("")
        self.frequency_penalty.setText(QCoreApplication.translate("code_setting", u"0", None))
        self.label_14.setText(QCoreApplication.translate("code_setting", u"\u66f4\u91cd\u590d", None))
        self.label_15.setText(QCoreApplication.translate("code_setting", u"\u66f4\u4e30\u5bcc", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("code_setting", u"\u5b58\u5728\u60e9\u7f5a", None))
        self.presence_help.setText("")
        self.presence_penalty.setText(QCoreApplication.translate("code_setting", u"0", None))
        self.label_16.setText(QCoreApplication.translate("code_setting", u"\u66f4\u805a\u7126", None))
        self.label_17.setText(QCoreApplication.translate("code_setting", u"\u66f4\u53d1\u6563", None))
    # retranslateUi

