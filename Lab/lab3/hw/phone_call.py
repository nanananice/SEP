# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_call.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 700)
        Form.setMinimumSize(QSize(400, 700))
        Form.setMaximumSize(QSize(400, 700))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(20)
        font.setBold(True)
        Form.setFont(font)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 380, 490))
        self.button_1 = QPushButton(self.widget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(0, 0, 120, 90))
        self.button_1.setMinimumSize(QSize(120, 90))
        self.button_1.setMaximumSize(QSize(120, 90))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(20)
        font1.setBold(False)
        self.button_1.setFont(font1)
        self.button_1.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_2 = QPushButton(self.widget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setGeometry(QRect(130, 0, 120, 90))
        self.button_2.setMinimumSize(QSize(120, 90))
        self.button_2.setMaximumSize(QSize(120, 90))
        self.button_2.setFont(font1)
        self.button_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_3 = QPushButton(self.widget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(260, 0, 120, 90))
        self.button_3.setMinimumSize(QSize(120, 90))
        self.button_3.setMaximumSize(QSize(120, 90))
        self.button_3.setFont(font1)
        self.button_3.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_4 = QPushButton(self.widget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(0, 100, 120, 90))
        self.button_4.setMinimumSize(QSize(120, 90))
        self.button_4.setMaximumSize(QSize(120, 90))
        self.button_4.setFont(font1)
        self.button_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_5 = QPushButton(self.widget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(130, 100, 120, 90))
        self.button_5.setMinimumSize(QSize(120, 90))
        self.button_5.setMaximumSize(QSize(120, 90))
        self.button_5.setFont(font1)
        self.button_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_6 = QPushButton(self.widget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setGeometry(QRect(260, 100, 120, 90))
        self.button_6.setMinimumSize(QSize(120, 90))
        self.button_6.setMaximumSize(QSize(120, 90))
        self.button_6.setFont(font1)
        self.button_6.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_7 = QPushButton(self.widget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setGeometry(QRect(0, 200, 120, 90))
        self.button_7.setMinimumSize(QSize(120, 90))
        self.button_7.setMaximumSize(QSize(120, 90))
        self.button_7.setFont(font1)
        self.button_7.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_8 = QPushButton(self.widget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setGeometry(QRect(130, 200, 120, 90))
        self.button_8.setMinimumSize(QSize(120, 90))
        self.button_8.setMaximumSize(QSize(120, 90))
        self.button_8.setFont(font1)
        self.button_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;\n"
"")
        self.button_9 = QPushButton(self.widget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setGeometry(QRect(260, 200, 120, 90))
        self.button_9.setMinimumSize(QSize(120, 90))
        self.button_9.setMaximumSize(QSize(120, 90))
        self.button_9.setFont(font1)
        self.button_9.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_mul = QPushButton(self.widget)
        self.button_mul.setObjectName(u"button_mul")
        self.button_mul.setGeometry(QRect(0, 300, 120, 90))
        self.button_mul.setMinimumSize(QSize(120, 90))
        self.button_mul.setMaximumSize(QSize(120, 90))
        self.button_mul.setFont(font1)
        self.button_mul.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_0 = QPushButton(self.widget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setGeometry(QRect(130, 300, 120, 90))
        self.button_0.setMinimumSize(QSize(120, 90))
        self.button_0.setMaximumSize(QSize(120, 90))
        self.button_0.setFont(font1)
        self.button_0.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_hash = QPushButton(self.widget)
        self.button_hash.setObjectName(u"button_hash")
        self.button_hash.setGeometry(QRect(260, 300, 120, 90))
        self.button_hash.setMinimumSize(QSize(120, 90))
        self.button_hash.setMaximumSize(QSize(120, 90))
        self.button_hash.setFont(font1)
        self.button_hash.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_talk = QPushButton(self.widget)
        self.button_talk.setObjectName(u"button_talk")
        self.button_talk.setGeometry(QRect(0, 400, 180, 90))
        self.button_talk.setMinimumSize(QSize(180, 90))
        self.button_talk.setMaximumSize(QSize(180, 90))
        self.button_talk.setFont(font1)
        self.button_talk.setStyleSheet(u"color: white;\n"
"background-color: rgb(6, 217, 55);\n"
"border-radius: 30px;")
        self.button_del = QPushButton(self.widget)
        self.button_del.setObjectName(u"button_del")
        self.button_del.setGeometry(QRect(200, 400, 180, 90))
        self.button_del.setMinimumSize(QSize(180, 90))
        self.button_del.setMaximumSize(QSize(180, 90))
        self.button_del.setFont(font1)
        self.button_del.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.home_app = QPushButton(Form)
        self.home_app.setObjectName(u"home_app")
        self.home_app.setGeometry(QRect(160, 610, 80, 80))
        self.home_app.setMinimumSize(QSize(80, 80))
        self.home_app.setMaximumSize(QSize(80, 80))
        self.home_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"pic/home_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_app.setIcon(icon)
        self.home_app.setIconSize(QSize(80, 80))
        self.home_background = QLabel(Form)
        self.home_background.setObjectName(u"home_background")
        self.home_background.setGeometry(QRect(0, 600, 400, 100))
        self.home_background.setMinimumSize(QSize(400, 100))
        self.home_background.setMaximumSize(QSize(400, 100))
        self.home_background.setStyleSheet(u"background-color: rgb(98, 98, 98);")
        self.home_background_2 = QLabel(Form)
        self.home_background_2.setObjectName(u"home_background_2")
        self.home_background_2.setGeometry(QRect(0, 0, 400, 600))
        self.home_background_2.setMinimumSize(QSize(400, 600))
        self.home_background_2.setMaximumSize(QSize(400, 600))
        self.home_background_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.phone_number = QLabel(Form)
        self.phone_number.setObjectName(u"phone_number")
        self.phone_number.setGeometry(QRect(10, 10, 380, 81))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.phone_number.setFont(font2)
        self.phone_number.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")
        self.phone_number.setFrameShape(QFrame.Panel)
        self.phone_number.setFrameShadow(QFrame.Plain)
        self.phone_number.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.home_background_2.raise_()
        self.home_background.raise_()
        self.widget.raise_()
        self.home_app.raise_()
        self.phone_number.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.button_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.button_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.button_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.button_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.button_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button_hash.setText(QCoreApplication.translate("Form", u"#", None))
        self.button_talk.setText(QCoreApplication.translate("Form", u"Talk", None))
        self.button_del.setText(QCoreApplication.translate("Form", u"<", None))
        self.home_app.setText("")
        self.home_background.setText("")
        self.home_background_2.setText("")
        self.phone_number.setText("")
    # retranslateUi

