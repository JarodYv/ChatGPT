# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_item.ui'
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
    QListView, QListWidget, QListWidgetItem, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_img_item(object):
    def setupUi(self, img_item):
        if not img_item.objectName():
            img_item.setObjectName(u"img_item")
        img_item.resize(810, 109)
        img_item.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(68, 70, 84);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(img_item)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(img_item)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(54, 0))
        self.widget_2.setMaximumSize(QSize(54, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.widget_2.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(32, 32))
        self.label.setMaximumSize(QSize(32, 32))
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	background-color: rgb(16, 163, 127);\n"
"	padding: 4px;\n"
"	border: 1px solid rgb(16, 163, 127);\n"
"	border-radius: 4px;\n"
"}")
        self.label.setPixmap(QPixmap(u":/assets/assets/openai_avatar.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.time_cost = QLabel(self.widget_2)
        self.time_cost.setObjectName(u"time_cost")
        font1 = QFont()
        font1.setPointSize(8)
        self.time_cost.setFont(font1)
        self.time_cost.setStyleSheet(u"color: rgba(255, 255, 255, 128);\n"
"margin: 4px 0;")
        self.time_cost.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.time_cost)

        self.verticalSpacer = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_2)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(700, 0))
        self.listWidget.setMaximumSize(QSize(1000, 16777215))
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setViewMode(QListView.IconMode)

        self.horizontalLayout.addWidget(self.listWidget)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(img_item)

        QMetaObject.connectSlotsByName(img_item)
    # setupUi

    def retranslateUi(self, img_item):
        img_item.setWindowTitle(QCoreApplication.translate("img_item", u"Form", None))
        self.label.setText("")
        self.time_cost.setText("")
    # retranslateUi

