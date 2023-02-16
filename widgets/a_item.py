# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'a_item.ui'
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
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_a_item(object):
    def setupUi(self, a_item):
        if not a_item.objectName():
            a_item.setObjectName(u"a_item")
        a_item.resize(810, 109)
        a_item.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(68, 70, 84);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(a_item)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(a_item)
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

        self.answer = QTextBrowser(self.widget)
        self.answer.setObjectName(u"answer")
        self.answer.setMinimumSize(QSize(700, 0))
        self.answer.setMaximumSize(QSize(1000, 16777215))
        self.answer.setFont(font)
        self.answer.setMouseTracking(False)
        self.answer.setAcceptDrops(False)
        self.answer.setStyleSheet(u"QTextBrowser{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.answer.setFrameShape(QFrame.NoFrame)
        self.answer.setFrameShadow(QFrame.Plain)
        self.answer.setAcceptRichText(True)

        self.horizontalLayout.addWidget(self.answer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(a_item)

        QMetaObject.connectSlotsByName(a_item)
    # setupUi

    def retranslateUi(self, a_item):
        a_item.setWindowTitle(QCoreApplication.translate("a_item", u"Form", None))
        self.label.setText("")
        self.time_cost.setText("")
        self.answer.setHtml(QCoreApplication.translate("a_item", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

