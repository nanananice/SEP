# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_exchanger.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 700)
        Form.setMinimumSize(QSize(400, 700))
        Form.setMaximumSize(QSize(400, 700))
        self.home_background = QLabel(Form)
        self.home_background.setObjectName(u"home_background")
        self.home_background.setGeometry(QRect(0, 600, 400, 100))
        self.home_background.setMinimumSize(QSize(400, 100))
        self.home_background.setMaximumSize(QSize(400, 100))
        self.home_background.setStyleSheet(u"background-color: rgb(98, 98, 98);")
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
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 110, 300, 150))
        self.widget.setStyleSheet(u"background-color: rgb(54, 222, 68);\n"
"border-radius: 20px;")
        self.from_currency_input = QLineEdit(self.widget)
        self.from_currency_input.setObjectName(u"from_currency_input")
        self.from_currency_input.setGeometry(QRect(40, 70, 160, 60))
        self.from_currency_input.setMinimumSize(QSize(160, 60))
        self.from_currency_input.setMaximumSize(QSize(160, 60))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(14)
        self.from_currency_input.setFont(font)
        self.from_currency_input.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"border-radius: 20px;")
        self.from_currency_combo = QComboBox(self.widget)
        self.from_currency_combo.setObjectName(u"from_currency_combo")
        self.from_currency_combo.setGeometry(QRect(210, 20, 70, 20))
        self.from_currency_combo.setMinimumSize(QSize(70, 20))
        self.from_currency_combo.setMaximumSize(QSize(70, 20))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(8)
        self.from_currency_combo.setFont(font1)
        self.from_currency_combo.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"")
        self.from_currency_name = QLabel(self.widget)
        self.from_currency_name.setObjectName(u"from_currency_name")
        self.from_currency_name.setGeometry(QRect(40, 20, 100, 20))
        self.from_currency_name.setMinimumSize(QSize(100, 20))
        self.from_currency_name.setMaximumSize(QSize(100, 20))
        self.from_currency_name.setFont(font1)
        self.from_currency_name.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"")
        self.from_currency_symbol = QLabel(self.widget)
        self.from_currency_symbol.setObjectName(u"from_currency_symbol")
        self.from_currency_symbol.setGeometry(QRect(0, 80, 40, 40))
        self.from_currency_symbol.setMinimumSize(QSize(40, 40))
        self.from_currency_symbol.setMaximumSize(QSize(40, 40))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        self.from_currency_symbol.setFont(font2)
        self.from_currency_symbol.setStyleSheet(u"background-color: rgb(54, 222, 68);\n"
"")
        self.from_currency_symbol.setAlignment(Qt.AlignCenter)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(50, 270, 300, 150))
        self.widget_2.setStyleSheet(u"background-color: rgb(54, 222, 68);\n"
"border-radius: 20px;")
        self.to_currency_combo = QComboBox(self.widget_2)
        self.to_currency_combo.setObjectName(u"to_currency_combo")
        self.to_currency_combo.setGeometry(QRect(210, 110, 70, 20))
        self.to_currency_combo.setMinimumSize(QSize(70, 20))
        self.to_currency_combo.setMaximumSize(QSize(70, 20))
        self.to_currency_combo.setFont(font1)
        self.to_currency_combo.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"")
        self.to_currency_name = QLabel(self.widget_2)
        self.to_currency_name.setObjectName(u"to_currency_name")
        self.to_currency_name.setGeometry(QRect(40, 110, 100, 20))
        self.to_currency_name.setMinimumSize(QSize(100, 20))
        self.to_currency_name.setMaximumSize(QSize(100, 20))
        self.to_currency_name.setFont(font1)
        self.to_currency_name.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"")
        self.to_currency_total = QLabel(self.widget_2)
        self.to_currency_total.setObjectName(u"to_currency_total")
        self.to_currency_total.setGeometry(QRect(40, 20, 160, 60))
        self.to_currency_total.setMinimumSize(QSize(160, 60))
        self.to_currency_total.setMaximumSize(QSize(160, 60))
        self.to_currency_total.setFont(font)
        self.to_currency_total.setStyleSheet(u"background-color: rgb(54, 202, 68);\n"
"")
        self.to_currency_symbol = QLabel(self.widget_2)
        self.to_currency_symbol.setObjectName(u"to_currency_symbol")
        self.to_currency_symbol.setGeometry(QRect(0, 30, 40, 40))
        self.to_currency_symbol.setMinimumSize(QSize(40, 40))
        self.to_currency_symbol.setMaximumSize(QSize(40, 40))
        self.to_currency_symbol.setFont(font2)
        self.to_currency_symbol.setStyleSheet(u"background-color: rgb(54, 222, 68);\n"
"")
        self.to_currency_symbol.setAlignment(Qt.AlignCenter)
        self.home_background_2 = QLabel(Form)
        self.home_background_2.setObjectName(u"home_background_2")
        self.home_background_2.setGeometry(QRect(0, 0, 400, 600))
        self.home_background_2.setMinimumSize(QSize(400, 600))
        self.home_background_2.setMaximumSize(QSize(400, 600))
        self.home_background_2.setStyleSheet(u"\n"
"background-color: rgb(62, 166, 46);")
        self.currency_label = QLabel(Form)
        self.currency_label.setObjectName(u"currency_label")
        self.currency_label.setGeometry(QRect(70, 30, 260, 50))
        self.currency_label.setMinimumSize(QSize(260, 50))
        self.currency_label.setMaximumSize(QSize(260, 50))
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(22)
        self.currency_label.setFont(font3)
        self.currency_label.setLayoutDirection(Qt.LeftToRight)
        self.currency_label.setScaledContents(True)
        self.currency_label.setAlignment(Qt.AlignCenter)
        self.from_currency_name_2 = QLabel(Form)
        self.from_currency_name_2.setObjectName(u"from_currency_name_2")
        self.from_currency_name_2.setGeometry(QRect(250, 220, 90, 90))
        self.from_currency_name_2.setMinimumSize(QSize(90, 90))
        self.from_currency_name_2.setMaximumSize(QSize(90, 90))
        self.from_currency_name_2.setFont(font1)
        self.from_currency_name_2.setStyleSheet(u"\n"
"background-color: rgb(62, 166, 46);\n"
"border-radius: 40px;")
        self.confirm = QPushButton(Form)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setGeometry(QRect(260, 230, 70, 70))
        self.confirm.setMinimumSize(QSize(70, 70))
        self.confirm.setMaximumSize(QSize(70, 70))
        self.confirm.setStyleSheet(u"background-color: rgb(54, 175, 68);\n"
"border-radius: 30px;")
        icon1 = QIcon()
        icon1.addFile(u"pic/updown_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confirm.setIcon(icon1)
        self.confirm.setIconSize(QSize(40, 40))
        self.home_background_2.raise_()
        self.home_background.raise_()
        self.home_app.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.currency_label.raise_()
        self.from_currency_name_2.raise_()
        self.confirm.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_background.setText("")
        self.home_app.setText("")
        self.from_currency_name.setText("")
        self.from_currency_symbol.setText("")
        self.to_currency_name.setText("")
        self.to_currency_total.setText("")
        self.to_currency_symbol.setText("")
        self.home_background_2.setText("")
        self.currency_label.setText(QCoreApplication.translate("Form", u"Money Exchanger", None))
        self.from_currency_name_2.setText("")
        self.confirm.setText("")
    # retranslateUi

