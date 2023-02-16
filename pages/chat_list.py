# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_list.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QListView,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_chat_list(object):
    def setupUi(self, chat_list):
        if not chat_list.objectName():
            chat_list.setObjectName(u"chat_list")
        chat_list.resize(498, 396)
        chat_list.setStyleSheet(u"background-color: rgb(52, 53, 65);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QVBoxLayout(chat_list)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.listWidget = QListWidget(chat_list)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget{\n"
"	border: none;\n"
"}\n"
"\n"
"QListWidget::item{\n"
"	margin: 0;\n"
"	padding: 0;\n"
"	border: none;\n"
"	outline: 0;\n"
"}")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Plain)
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.listWidget.setViewMode(QListView.ListMode)

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(chat_list)

        QMetaObject.connectSlotsByName(chat_list)
    # setupUi

    def retranslateUi(self, chat_list):
        chat_list.setWindowTitle(QCoreApplication.translate("chat_list", u"Form", None))
    # retranslateUi

