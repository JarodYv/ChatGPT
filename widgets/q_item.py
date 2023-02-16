# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'q_item.ui'
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

class Ui_q_item(object):
    def setupUi(self, q_item):
        if not q_item.objectName():
            q_item.setObjectName(u"q_item")
        q_item.resize(800, 72)
        q_item.setMinimumSize(QSize(0, 0))
        q_item.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(52, 53, 65);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(q_item)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(q_item)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
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
"	border: 1px solid rgb(52,53,65);\n"
"	border-radius: 4px;\n"
"}")
        self.label.setPixmap(QPixmap(u":/assets/assets/jarod.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.widget_2)

        self.question = QTextBrowser(self.widget)
        self.question.setObjectName(u"question")
        self.question.setMinimumSize(QSize(700, 0))
        self.question.setMaximumSize(QSize(1000, 16777215))
        self.question.setAcceptDrops(False)
        self.question.setStyleSheet(u"QTextBrowser{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.question.setFrameShape(QFrame.NoFrame)
        self.question.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.question)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(q_item)

        QMetaObject.connectSlotsByName(q_item)
    # setupUi

    def retranslateUi(self, q_item):
        q_item.setWindowTitle(QCoreApplication.translate("q_item", u"Form", None))
        self.label.setText("")
    # retranslateUi

