# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 600)
        icon = QIcon()
        icon.addFile(u":/assets/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_container = QWidget(self.centralwidget)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMinimumSize(QSize(180, 0))
        self.menu_container.setMaximumSize(QSize(180, 16777215))
        self.menu_container.setStyleSheet(u"QWidget#menu_container{\n"
"background-color: rgb(32, 33, 35);\n"
"background-image:url(:/assets/assets/menu_bg.png);\n"
"background-repeat:no-repeat;\n"
"background-position:bottom;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.menu_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 20)
        self.btn_logo = QLabel(self.menu_container)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setMinimumSize(QSize(180, 58))
        self.btn_logo.setMaximumSize(QSize(180, 58))
        self.btn_logo.setStyleSheet(u"QLabel{\n"
"	border: none;\n"
"	margin: 10px 30px;\n"
"}")
        self.btn_logo.setPixmap(QPixmap(u":/assets/assets/logo.png"))
        self.btn_logo.setScaledContents(True)
        self.btn_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.btn_logo)

        self.menu_list = QWidget(self.menu_container)
        self.menu_list.setObjectName(u"menu_list")
        self.menu_list.setMinimumSize(QSize(0, 400))
        self.menu_list.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.menu_list)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.menu_text = QPushButton(self.menu_list)
        self.menu_text.setObjectName(u"menu_text")
        self.menu_text.setMinimumSize(QSize(0, 60))
        self.menu_text.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(11)
        self.menu_text.setFont(font)
        self.menu_text.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(43, 44, 47);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_text.setIcon(icon1)
        self.menu_text.setIconSize(QSize(20, 20))
        self.menu_text.setCheckable(True)
        self.menu_text.setChecked(True)
        self.menu_text.setAutoExclusive(True)
        self.menu_text.setFlat(True)

        self.verticalLayout_2.addWidget(self.menu_text)

        self.menu_code = QPushButton(self.menu_list)
        self.menu_code.setObjectName(u"menu_code")
        self.menu_code.setMinimumSize(QSize(0, 60))
        self.menu_code.setMaximumSize(QSize(16777215, 60))
        self.menu_code.setFont(font)
        self.menu_code.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(43, 44, 47);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/assets/assets/code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_code.setIcon(icon2)
        self.menu_code.setIconSize(QSize(20, 20))
        self.menu_code.setCheckable(True)
        self.menu_code.setChecked(False)
        self.menu_code.setAutoExclusive(True)
        self.menu_code.setFlat(True)

        self.verticalLayout_2.addWidget(self.menu_code)

        self.menu_image = QPushButton(self.menu_list)
        self.menu_image.setObjectName(u"menu_image")
        self.menu_image.setMinimumSize(QSize(0, 60))
        self.menu_image.setMaximumSize(QSize(16777215, 60))
        self.menu_image.setFont(font)
        self.menu_image.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(43, 44, 47);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/assets/assets/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_image.setIcon(icon3)
        self.menu_image.setIconSize(QSize(20, 20))
        self.menu_image.setCheckable(True)
        self.menu_image.setChecked(False)
        self.menu_image.setAutoExclusive(True)
        self.menu_image.setFlat(True)

        self.verticalLayout_2.addWidget(self.menu_image)

        self.verticalSpacer = QSpacerItem(20, 206, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.menu_list)

        self.widget_4 = QWidget(self.menu_container)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 50))
        self.widget_4.setMaximumSize(QSize(16777215, 50))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.btn_github = QPushButton(self.widget_4)
        self.btn_github.setObjectName(u"btn_github")
        self.btn_github.setMinimumSize(QSize(0, 40))
        self.btn_github.setMaximumSize(QSize(16777215, 40))
        self.btn_github.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/assets/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_github.setIcon(icon4)
        self.btn_github.setIconSize(QSize(20, 20))
        self.btn_github.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_github)

        self.btn_api = QPushButton(self.widget_4)
        self.btn_api.setObjectName(u"btn_api")
        self.btn_api.setMinimumSize(QSize(0, 40))
        self.btn_api.setMaximumSize(QSize(16777215, 40))
        self.btn_api.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets/assets/api.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_api.setIcon(icon5)
        self.btn_api.setIconSize(QSize(20, 20))
        self.btn_api.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_api)

        self.btn_about = QPushButton(self.widget_4)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 40))
        self.btn_about.setMaximumSize(QSize(16777215, 40))
        self.btn_about.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/assets/assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon6)
        self.btn_about.setIconSize(QSize(20, 20))
        self.btn_about.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_about)


        self.verticalLayout.addWidget(self.widget_4)

        self.version = QLabel(self.menu_container)
        self.version.setObjectName(u"version")
        self.version.setMinimumSize(QSize(0, 20))
        self.version.setMaximumSize(QSize(16777215, 20))
        self.version.setStyleSheet(u"color: rgba(255, 255, 255, 128);")
        self.version.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.version)


        self.horizontalLayout_4.addWidget(self.menu_container)

        self.main_container = QWidget(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"background-color: rgb(52, 53, 65);")
        self.verticalLayout_4 = QVBoxLayout(self.main_container)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.response_area = QWidget(self.main_container)
        self.response_area.setObjectName(u"response_area")
        self.response_area.setStyleSheet(u"background-color: rgb(52, 53, 65);")
        self.verticalLayout_6 = QVBoxLayout(self.response_area)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.response_area)

        self.prompt_container = QWidget(self.main_container)
        self.prompt_container.setObjectName(u"prompt_container")
        self.prompt_container.setMinimumSize(QSize(0, 90))
        self.prompt_container.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.prompt_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(143, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.prompt_area = QWidget(self.prompt_container)
        self.prompt_area.setObjectName(u"prompt_area")
        self.prompt_area.setMinimumSize(QSize(800, 0))
        self.prompt_area.setMaximumSize(QSize(1200, 16777215))
        self.prompt_area.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.prompt_area)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.prompt_area)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"QWidget{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(64, 65, 79);\n"
"	border: 1px solid rgb(64, 65, 79);\n"
"	border-radius:6px;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 6, 12, 6)
        self.prompt_input = QPlainTextEdit(self.widget)
        self.prompt_input.setObjectName(u"prompt_input")
        font1 = QFont()
        font1.setPointSize(10)
        self.prompt_input.setFont(font1)
        self.prompt_input.setStyleSheet(u"")
        self.prompt_input.setFrameShape(QFrame.NoFrame)
        self.prompt_input.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_3.addWidget(self.prompt_input)

        self.prompt_send = QPushButton(self.widget)
        self.prompt_send.setObjectName(u"prompt_send")
        self.prompt_send.setMinimumSize(QSize(32, 32))
        self.prompt_send.setMaximumSize(QSize(32, 32))
        self.prompt_send.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 26);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/assets/assets/send.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prompt_send.setIcon(icon7)
        self.prompt_send.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.prompt_send)


        self.verticalLayout_3.addWidget(self.widget)

        self.label = QLabel(self.prompt_area)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgba(255, 255, 255, 128);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.prompt_area)

        self.horizontalSpacer_2 = QSpacerItem(142, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.prompt_container)


        self.horizontalLayout_4.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PlanGPT", None))
        self.btn_logo.setText("")
        self.menu_text.setText(QCoreApplication.translate("MainWindow", u"  \u6587\u672c\u751f\u6210", None))
        self.menu_code.setText(QCoreApplication.translate("MainWindow", u"  \u4ee3\u7801\u751f\u6210", None))
        self.menu_image.setText(QCoreApplication.translate("MainWindow", u"  \u56fe\u7247\u751f\u6210", None))
#if QT_CONFIG(whatsthis)
        self.btn_github.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_github.setText("")
#if QT_CONFIG(whatsthis)
        self.btn_api.setWhatsThis(QCoreApplication.translate("MainWindow", u"API\u6587\u6863", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_api.setText("")
#if QT_CONFIG(whatsthis)
        self.btn_about.setWhatsThis(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_about.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"version: 0.1.8", None))
        self.prompt_input.setPlainText("")
        self.prompt_send.setText("")
#if QT_CONFIG(shortcut)
        self.prompt_send.setShortcut(QCoreApplication.translate("MainWindow", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Copyright \u00a9 2023 PlanPlus Inc. All Rights Reserved. For Research Use Only.", None))
    # retranslateUi

