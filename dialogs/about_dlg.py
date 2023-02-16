# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/assets/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(AboutDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(64, 64))
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/assets/assets/planyun.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.label_3 = QLabel(AboutDialog)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #BBBBBB;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(AboutDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:#666666;\n"
"margin-top: 20px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(AboutDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #BBBBBB;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"Dialog", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("AboutDialog", u"version: 0.1.8", None))
        self.label_4.setText(QCoreApplication.translate("AboutDialog", u"\u8c31\u84dd\u4e91ChatGPT\u57fa\u4e8eOpenAI GPT-3\u63a5\u53e3\u5f00\u53d1\uff0c\n"
"\u7528\u4e8e\u63a2\u7d22\u548c\u5b9e\u9a8cChatGPT\u7684\u529f\u80fd\u548c\u5728\u4e1a\u52a1\u5e94\u7528\u4e0a\u7684\u6f5c\u529b\u3002", None))
        self.label_2.setText(QCoreApplication.translate("AboutDialog", u"Copyright \u00a9 2023 PlanPlus Inc. All Rights Reserved", None))
    # retranslateUi

