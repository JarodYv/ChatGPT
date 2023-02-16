# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)
import resource_rc

class Ui_help_dlg(object):
    def setupUi(self, help_dlg):
        if not help_dlg.objectName():
            help_dlg.setObjectName(u"help_dlg")
        help_dlg.resize(535, 438)
        icon = QIcon()
        icon.addFile(u":/assets/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        help_dlg.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(help_dlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(help_dlg)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(help_dlg)

        QMetaObject.connectSlotsByName(help_dlg)
    # setupUi

    def retranslateUi(self, help_dlg):
        help_dlg.setWindowTitle(QCoreApplication.translate("help_dlg", u"Dialog", None))
    # retranslateUi

