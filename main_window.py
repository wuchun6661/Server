# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(840, 525)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Edit_id = QLineEdit(Form)
        self.Edit_id.setObjectName(u"Edit_id")
        font1 = QFont()
        font1.setPointSize(18)
        self.Edit_id.setFont(font1)
        self.Edit_id.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")

        self.horizontalLayout_2.addWidget(self.Edit_id)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Edit_out = QTextBrowser(Form)
        self.Edit_out.setObjectName(u"Edit_out")
        self.Edit_out.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        self.Edit_out.setFont(font2)
        self.Edit_out.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.Edit_out.setMouseTracking(True)
        self.Edit_out.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.verticalLayout.addWidget(self.Edit_out)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.Edit_in = QLineEdit(Form)
        self.Edit_in.setObjectName(u"Edit_in")
        self.Edit_in.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Edit_in.sizePolicy().hasHeightForWidth())
        self.Edit_in.setSizePolicy(sizePolicy1)
        self.Edit_in.setBaseSize(QSize(0, 1))
        self.Edit_in.setFont(font)
        self.Edit_in.setLayoutDirection(Qt.LeftToRight)
        self.Edit_in.setStyleSheet(u"color: rgb(255, 85, 255);")
        self.Edit_in.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout.addWidget(self.Edit_in)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_clear = QPushButton(Form)
        self.button_clear.setObjectName(u"button_clear")
        font4 = QFont()
        font4.setPointSize(25)
        font4.setKerning(True)
        self.button_clear.setFont(font4)

        self.horizontalLayout.addWidget(self.button_clear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.button_send = QPushButton(Form)
        self.button_send.setObjectName(u"button_send")
        font5 = QFont()
        font5.setPointSize(25)
        self.button_send.setFont(font5)

        self.horizontalLayout.addWidget(self.button_send)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 5)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 13)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.setStretch(0, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.setStretch(0, 1)
        self.Edit_id.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e3b\u754c\u9762", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u60a8\u7684\u6635\u79f0\uff1a", None))
        self.Edit_id.setText(QCoreApplication.translate("Form", u"\u94c1\u61a8\u61a8", None))
        self.Edit_out.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Edit_out.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u8bf7\u5728\u4e0b\u65b9\uff0c\u8f93\u5165\u60a8\u8981\u53d1\u9001\u7684\u6d88\u606f\uff1a", None))
        self.Edit_in.setInputMask("")
        self.Edit_in.setText("")
        self.Edit_in.setPlaceholderText("")
        self.button_clear.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a\u5386\u53f2\u8bb0\u5f55", None))
        self.button_send.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
    # retranslateUi

