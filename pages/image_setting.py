# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_img_setting(object):
    def setupUi(self, img_setting):
        if not img_setting.objectName():
            img_setting.setObjectName(u"img_setting")
        img_setting.resize(758, 631)
        img_setting.setMinimumSize(QSize(0, 0))
        img_setting.setMaximumSize(QSize(16777215, 16777215))
        img_setting.setStyleSheet(u"background-color: rgb(52, 53, 65);\n"
"	color: rgb(255, 255, 255);\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(img_setting)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widget = QWidget(img_setting)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(560, 0))
        self.widget.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"margin: 20px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

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
        self.label_2.setPixmap(QPixmap(u":/assets/assets/image.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(521, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.size_1024 = QPushButton(self.widget_4)
        self.size_1024.setObjectName(u"size_1024")
        self.size_1024.setMinimumSize(QSize(120, 60))
        self.size_1024.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(62, 63, 75);\n"
"	background-color: rgb(62, 63, 75);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 1px solid rgb(32, 33, 35);\n"
"	background-color: rgb(32, 33, 35);\n"
"}")
        self.size_1024.setCheckable(True)
        self.size_1024.setChecked(True)
        self.size_1024.setAutoExclusive(True)
        self.size_1024.setFlat(True)

        self.horizontalLayout.addWidget(self.size_1024)

        self.size_512 = QPushButton(self.widget_4)
        self.size_512.setObjectName(u"size_512")
        self.size_512.setMinimumSize(QSize(120, 60))
        self.size_512.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(62, 63, 75);\n"
"	background-color: rgb(62, 63, 75);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 1px solid rgb(32, 33, 35);\n"
"	background-color: rgb(32, 33, 35);\n"
"}")
        self.size_512.setCheckable(True)
        self.size_512.setChecked(False)
        self.size_512.setAutoExclusive(True)
        self.size_512.setFlat(True)

        self.horizontalLayout.addWidget(self.size_512)

        self.size_256 = QPushButton(self.widget_4)
        self.size_256.setObjectName(u"size_256")
        self.size_256.setMinimumSize(QSize(120, 60))
        self.size_256.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid rgb(62, 63, 75);\n"
"	background-color: rgb(62, 63, 75);\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	border: 1px solid rgb(32, 33, 35);\n"
"	background-color: rgb(32, 33, 35);\n"
"}")
        self.size_256.setCheckable(True)
        self.size_256.setAutoExclusive(True)
        self.size_256.setFlat(True)

        self.horizontalLayout.addWidget(self.size_256)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget_4)


        self.verticalLayout_2.addWidget(self.widget_2)

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

        self.img_num = QLineEdit(self.widget_14)
        self.img_num.setObjectName(u"img_num")
        self.img_num.setStyleSheet(u"padding: 0 6px;")
        self.img_num.setFrame(True)

        self.horizontalLayout_10.addWidget(self.img_num)


        self.verticalLayout_5.addWidget(self.widget_14)


        self.verticalLayout_2.addWidget(self.widget_13)

        self.verticalSpacer_2 = QSpacerItem(20, 248, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.retranslateUi(img_setting)

        QMetaObject.connectSlotsByName(img_setting)
    # setupUi

    def retranslateUi(self, img_setting):
        img_setting.setWindowTitle(QCoreApplication.translate("img_setting", u"Form", None))
        self.label.setText(QCoreApplication.translate("img_setting", u"\u56fe\u7247\u751f\u6210", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("img_setting", u"\u56fe\u7247\u5c3a\u5bf8", None))
        self.size_1024.setText(QCoreApplication.translate("img_setting", u"1024x1024", None))
        self.size_512.setText(QCoreApplication.translate("img_setting", u"512x512", None))
        self.size_256.setText(QCoreApplication.translate("img_setting", u"256x256", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("img_setting", u"\u751f\u6210\u56fe\u7247\u6570\u91cf\uff1a", None))
        self.img_num.setText(QCoreApplication.translate("img_setting", u"1", None))
    # retranslateUi

