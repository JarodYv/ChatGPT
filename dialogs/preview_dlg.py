# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_preview_dlg(object):
    def setupUi(self, preview_dlg):
        if not preview_dlg.objectName():
            preview_dlg.setObjectName(u"preview_dlg")
        preview_dlg.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/assets/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        preview_dlg.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(preview_dlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.preview = QLabel(preview_dlg)
        self.preview.setObjectName(u"preview")

        self.verticalLayout.addWidget(self.preview)

        self.download_btn = QPushButton(preview_dlg)
        self.download_btn.setObjectName(u"download_btn")
        font = QFont()
        font.setPointSize(10)
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet(u"color: rgb(112, 112, 112);")
        icon1 = QIcon()
        icon1.addFile(u":/assets/assets/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.download_btn.setIcon(icon1)
        self.download_btn.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.download_btn)


        self.retranslateUi(preview_dlg)

        QMetaObject.connectSlotsByName(preview_dlg)
    # setupUi

    def retranslateUi(self, preview_dlg):
        preview_dlg.setWindowTitle(QCoreApplication.translate("preview_dlg", u"\u56fe\u7247\u6d4f\u89c8", None))
        self.preview.setText("")
        self.download_btn.setText(QCoreApplication.translate("preview_dlg", u"\u4e0b\u8f7d\u56fe\u7247", None))
    # retranslateUi

