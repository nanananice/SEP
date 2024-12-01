# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_calculator.ui'
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
        self.widget.setGeometry(QRect(10, 139, 380, 450))
        self.widget.setStyleSheet(u"")
        self.button_1 = QPushButton(self.widget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setGeometry(QRect(0, 270, 95, 90))
        self.button_1.setMinimumSize(QSize(95, 90))
        self.button_1.setMaximumSize(QSize(95, 90))
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
        self.button_2.setGeometry(QRect(95, 270, 95, 90))
        self.button_2.setMinimumSize(QSize(95, 90))
        self.button_2.setMaximumSize(QSize(95, 90))
        self.button_2.setFont(font1)
        self.button_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_3 = QPushButton(self.widget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setGeometry(QRect(190, 270, 95, 90))
        self.button_3.setMinimumSize(QSize(95, 90))
        self.button_3.setMaximumSize(QSize(95, 90))
        self.button_3.setFont(font1)
        self.button_3.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_4 = QPushButton(self.widget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setGeometry(QRect(0, 180, 95, 90))
        self.button_4.setMinimumSize(QSize(95, 90))
        self.button_4.setMaximumSize(QSize(95, 90))
        self.button_4.setFont(font1)
        self.button_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_5 = QPushButton(self.widget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setGeometry(QRect(95, 180, 95, 90))
        self.button_5.setMinimumSize(QSize(95, 90))
        self.button_5.setMaximumSize(QSize(95, 90))
        self.button_5.setFont(font1)
        self.button_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_6 = QPushButton(self.widget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setGeometry(QRect(190, 180, 95, 90))
        self.button_6.setMinimumSize(QSize(95, 90))
        self.button_6.setMaximumSize(QSize(95, 90))
        self.button_6.setFont(font1)
        self.button_6.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_7 = QPushButton(self.widget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setGeometry(QRect(0, 90, 95, 90))
        self.button_7.setMinimumSize(QSize(95, 90))
        self.button_7.setMaximumSize(QSize(95, 90))
        self.button_7.setFont(font1)
        self.button_7.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_8 = QPushButton(self.widget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setGeometry(QRect(95, 90, 95, 90))
        self.button_8.setMinimumSize(QSize(95, 90))
        self.button_8.setMaximumSize(QSize(95, 90))
        self.button_8.setFont(font1)
        self.button_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;\n"
"")
        self.button_9 = QPushButton(self.widget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setGeometry(QRect(190, 90, 95, 90))
        self.button_9.setMinimumSize(QSize(95, 90))
        self.button_9.setMaximumSize(QSize(95, 90))
        self.button_9.setFont(font1)
        self.button_9.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_multiply = QPushButton(self.widget)
        self.button_multiply.setObjectName(u"button_multiply")
        self.button_multiply.setGeometry(QRect(285, 90, 95, 90))
        self.button_multiply.setMinimumSize(QSize(95, 90))
        self.button_multiply.setMaximumSize(QSize(95, 90))
        self.button_multiply.setFont(font1)
        self.button_multiply.setStyleSheet(u"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 30px;")
        self.button_plus = QPushButton(self.widget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setGeometry(QRect(285, 270, 95, 90))
        self.button_plus.setMinimumSize(QSize(95, 90))
        self.button_plus.setMaximumSize(QSize(95, 90))
        self.button_plus.setFont(font1)
        self.button_plus.setStyleSheet(u"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 30px;")
        self.button_decimal = QPushButton(self.widget)
        self.button_decimal.setObjectName(u"button_decimal")
        self.button_decimal.setGeometry(QRect(190, 360, 95, 90))
        self.button_decimal.setMinimumSize(QSize(95, 90))
        self.button_decimal.setMaximumSize(QSize(95, 90))
        self.button_decimal.setFont(font1)
        self.button_decimal.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;")
        self.button_0 = QPushButton(self.widget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setGeometry(QRect(0, 360, 190, 90))
        self.button_0.setMinimumSize(QSize(190, 90))
        self.button_0.setMaximumSize(QSize(190, 90))
        self.button_0.setFont(font1)
        self.button_0.setStyleSheet(u"color: white;\n"
"background-color: rgb(59, 59, 59);\n"
"border-radius: 30px;\n"
"")
        self.button_minus = QPushButton(self.widget)
        self.button_minus.setObjectName(u"button_minus")
        self.button_minus.setGeometry(QRect(285, 180, 95, 90))
        self.button_minus.setMinimumSize(QSize(95, 90))
        self.button_minus.setMaximumSize(QSize(95, 90))
        self.button_minus.setFont(font1)
        self.button_minus.setStyleSheet(u"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 30px;")
        self.button_divide = QPushButton(self.widget)
        self.button_divide.setObjectName(u"button_divide")
        self.button_divide.setGeometry(QRect(285, 0, 95, 90))
        self.button_divide.setMinimumSize(QSize(95, 90))
        self.button_divide.setMaximumSize(QSize(95, 90))
        self.button_divide.setFont(font1)
        self.button_divide.setStyleSheet(u"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 30px;")
        self.button_clear = QPushButton(self.widget)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setGeometry(QRect(0, 0, 95, 90))
        self.button_clear.setMinimumSize(QSize(95, 90))
        self.button_clear.setMaximumSize(QSize(95, 90))
        self.button_clear.setFont(font1)
        self.button_clear.setStyleSheet(u"color: white;\n"
"background-color: rgb(135, 135, 135);\n"
"border-radius: 30px;")
        self.button_plusminus = QPushButton(self.widget)
        self.button_plusminus.setObjectName(u"button_plusminus")
        self.button_plusminus.setGeometry(QRect(190, 0, 95, 90))
        self.button_plusminus.setMinimumSize(QSize(95, 90))
        self.button_plusminus.setMaximumSize(QSize(95, 90))
        self.button_plusminus.setFont(font1)
        self.button_plusminus.setStyleSheet(u"color: white;\n"
"background-color: rgb(135, 135, 135);\n"
"border-radius: 30px;")
        self.button_equal = QPushButton(self.widget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(285, 360, 95, 90))
        self.button_equal.setMinimumSize(QSize(95, 90))
        self.button_equal.setMaximumSize(QSize(95, 90))
        self.button_equal.setFont(font1)
        self.button_equal.setStyleSheet(u"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"border-radius: 30px;")
        self.button_delete = QPushButton(self.widget)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setGeometry(QRect(95, 0, 95, 90))
        self.button_delete.setMinimumSize(QSize(95, 90))
        self.button_delete.setMaximumSize(QSize(95, 90))
        self.button_delete.setFont(font1)
        self.button_delete.setStyleSheet(u"color: white;\n"
"background-color: rgb(135, 135, 135);\n"
"border-radius: 30px;")
        self.number = QLabel(Form)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(10, 10, 380, 121))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(24)
        font2.setBold(False)
        self.number.setFont(font2)
        self.number.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"}")
        self.number.setFrameShape(QFrame.Panel)
        self.number.setFrameShadow(QFrame.Plain)
        self.number.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
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
        self.home_background_2.raise_()
        self.home_background.raise_()
        self.widget.raise_()
        self.number.raise_()
        self.home_app.raise_()

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
        self.button_multiply.setText(QCoreApplication.translate("Form", u"*", None))
        self.button_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.button_decimal.setText(QCoreApplication.translate("Form", u".", None))
        self.button_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.button_divide.setText(QCoreApplication.translate("Form", u"/", None))
        self.button_clear.setText(QCoreApplication.translate("Form", u"c", None))
        self.button_plusminus.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.button_equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.button_delete.setText(QCoreApplication.translate("Form", u"<", None))
        self.number.setText("")
        self.home_app.setText("")
        self.home_background.setText("")
        self.home_background_2.setText("")
    # retranslateUi

