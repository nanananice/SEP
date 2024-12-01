# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 700)
        Form.setMinimumSize(QSize(400, 700))
        Form.setMaximumSize(QSize(400, 700))
        Form.setStyleSheet(u"QWidget::setFixedSize(400,800)\n"
"")
        self.home_app_2 = QLabel(Form)
        self.home_app_2.setObjectName(u"home_app_2")
        self.home_app_2.setGeometry(QRect(0, 0, 400, 800))
        self.home_app_2.setMinimumSize(QSize(400, 800))
        self.home_app_2.setMaximumSize(QSize(400, 800))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        self.home_app_2.setFont(font)
        self.home_app_2.setPixmap(QPixmap(u"pic/background.jpg"))
        self.exchanger_app = QPushButton(Form)
        self.exchanger_app.setObjectName(u"exchanger_app")
        self.exchanger_app.setGeometry(QRect(160, 40, 80, 80))
        self.exchanger_app.setMinimumSize(QSize(80, 80))
        self.exchanger_app.setMaximumSize(QSize(80, 80))
        self.exchanger_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"pic/currency_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exchanger_app.setIcon(icon)
        self.exchanger_app.setIconSize(QSize(80, 80))
        self.calculator_app = QPushButton(Form)
        self.calculator_app.setObjectName(u"calculator_app")
        self.calculator_app.setGeometry(QRect(40, 40, 80, 80))
        self.calculator_app.setMinimumSize(QSize(80, 80))
        self.calculator_app.setMaximumSize(QSize(80, 80))
        self.calculator_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"pic/calc_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calculator_app.setIcon(icon1)
        self.calculator_app.setIconSize(QSize(80, 80))
        self.contact_app = QPushButton(Form)
        self.contact_app.setObjectName(u"contact_app")
        self.contact_app.setGeometry(QRect(280, 40, 80, 80))
        self.contact_app.setMinimumSize(QSize(80, 80))
        self.contact_app.setMaximumSize(QSize(80, 80))
        self.contact_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"pic/contact_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.contact_app.setIcon(icon2)
        self.contact_app.setIconSize(QSize(90, 90))
        self.phone_app = QPushButton(Form)
        self.phone_app.setObjectName(u"phone_app")
        self.phone_app.setGeometry(QRect(40, 180, 80, 80))
        self.phone_app.setMinimumSize(QSize(80, 80))
        self.phone_app.setMaximumSize(QSize(80, 80))
        self.phone_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"pic/phone_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.phone_app.setIcon(icon3)
        self.phone_app.setIconSize(QSize(90, 90))
        self.game_app = QPushButton(Form)
        self.game_app.setObjectName(u"game_app")
        self.game_app.setGeometry(QRect(160, 180, 80, 80))
        self.game_app.setMinimumSize(QSize(80, 80))
        self.game_app.setMaximumSize(QSize(80, 80))
        self.game_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"pic/guess_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.game_app.setIcon(icon4)
        self.game_app.setIconSize(QSize(80, 80))
        self.calculator_label = QLabel(Form)
        self.calculator_label.setObjectName(u"calculator_label")
        self.calculator_label.setGeometry(QRect(40, 120, 80, 20))
        self.calculator_label.setMinimumSize(QSize(80, 20))
        self.calculator_label.setMaximumSize(QSize(80, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe Fluent Icons"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.calculator_label.setFont(font1)
        self.calculator_label.setLayoutDirection(Qt.LeftToRight)
        self.calculator_label.setScaledContents(True)
        self.calculator_label.setAlignment(Qt.AlignCenter)
        self.exchanger_label = QLabel(Form)
        self.exchanger_label.setObjectName(u"exchanger_label")
        self.exchanger_label.setGeometry(QRect(160, 120, 80, 20))
        self.exchanger_label.setMinimumSize(QSize(80, 20))
        self.exchanger_label.setMaximumSize(QSize(80, 20))
        self.exchanger_label.setFont(font)
        self.exchanger_label.setLayoutDirection(Qt.LeftToRight)
        self.exchanger_label.setScaledContents(True)
        self.exchanger_label.setAlignment(Qt.AlignCenter)
        self.contact_label = QLabel(Form)
        self.contact_label.setObjectName(u"contact_label")
        self.contact_label.setGeometry(QRect(280, 120, 80, 20))
        self.contact_label.setMinimumSize(QSize(80, 20))
        self.contact_label.setMaximumSize(QSize(80, 20))
        self.contact_label.setFont(font)
        self.contact_label.setLayoutDirection(Qt.LeftToRight)
        self.contact_label.setScaledContents(True)
        self.contact_label.setAlignment(Qt.AlignCenter)
        self.phone_label = QLabel(Form)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(40, 260, 80, 20))
        self.phone_label.setMinimumSize(QSize(80, 20))
        self.phone_label.setMaximumSize(QSize(80, 20))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.phone_label.setFont(font2)
        self.phone_label.setLayoutDirection(Qt.LeftToRight)
        self.phone_label.setScaledContents(True)
        self.phone_label.setAlignment(Qt.AlignCenter)
        self.guess_label = QLabel(Form)
        self.guess_label.setObjectName(u"guess_label")
        self.guess_label.setGeometry(QRect(160, 260, 80, 20))
        self.guess_label.setMinimumSize(QSize(80, 20))
        self.guess_label.setMaximumSize(QSize(80, 20))
        self.guess_label.setFont(font2)
        self.guess_label.setLayoutDirection(Qt.LeftToRight)
        self.guess_label.setScaledContents(True)
        self.guess_label.setAlignment(Qt.AlignCenter)
        self.home_app = QPushButton(Form)
        self.home_app.setObjectName(u"home_app")
        self.home_app.setGeometry(QRect(160, 610, 80, 80))
        self.home_app.setMinimumSize(QSize(80, 80))
        self.home_app.setMaximumSize(QSize(80, 80))
        self.home_app.setStyleSheet(u"QPushButton {\n"
"    border-radius: 1px;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"pic/home_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_app.setIcon(icon5)
        self.home_app.setIconSize(QSize(80, 80))
        self.home_background = QLabel(Form)
        self.home_background.setObjectName(u"home_background")
        self.home_background.setGeometry(QRect(0, 600, 400, 100))
        self.home_background.setMinimumSize(QSize(400, 100))
        self.home_background.setMaximumSize(QSize(400, 100))
        self.home_background.setStyleSheet(u"background-color: rgb(98, 98, 98);")
        self.home_app_2.raise_()
        self.home_background.raise_()
        self.exchanger_app.raise_()
        self.calculator_app.raise_()
        self.contact_app.raise_()
        self.phone_app.raise_()
        self.game_app.raise_()
        self.calculator_label.raise_()
        self.exchanger_label.raise_()
        self.contact_label.raise_()
        self.phone_label.raise_()
        self.guess_label.raise_()
        self.home_app.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_app_2.setText("")
        self.exchanger_app.setText("")
        self.calculator_app.setText("")
        self.contact_app.setText("")
        self.phone_app.setText("")
        self.game_app.setText("")
        self.calculator_label.setText(QCoreApplication.translate("Form", u"Calculator", None))
        self.exchanger_label.setText(QCoreApplication.translate("Form", u"Exchanger", None))
        self.contact_label.setText(QCoreApplication.translate("Form", u"Contacts", None))
        self.phone_label.setText(QCoreApplication.translate("Form", u"Phone", None))
        self.guess_label.setText(QCoreApplication.translate("Form", u"Guess it!", None))
        self.home_app.setText("")
        self.home_background.setText("")
    # retranslateUi

