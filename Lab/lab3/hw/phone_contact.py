# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_contact.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

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
        self.home_background_3 = QLabel(Form)
        self.home_background_3.setObjectName(u"home_background_3")
        self.home_background_3.setGeometry(QRect(0, 0, 400, 600))
        self.home_background_3.setMinimumSize(QSize(400, 600))
        self.home_background_3.setMaximumSize(QSize(400, 600))
        self.home_background_3.setStyleSheet(u"\n"
"background-color: rgb(161, 161, 161);")
        self.head_label = QLabel(Form)
        self.head_label.setObjectName(u"head_label")
        self.head_label.setGeometry(QRect(10, 30, 300, 50))
        self.head_label.setMinimumSize(QSize(300, 50))
        self.head_label.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(22)
        self.head_label.setFont(font)
        self.head_label.setLayoutDirection(Qt.LeftToRight)
        self.head_label.setScaledContents(True)
        self.head_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 90, 380, 400))
        self.scrollArea.setMinimumSize(QSize(380, 400))
        self.scrollArea.setMaximumSize(QSize(380, 400))
        self.scrollArea.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 398))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.add_contact = QPushButton(Form)
        self.add_contact.setObjectName(u"add_contact")
        self.add_contact.setGeometry(QRect(10, 500, 100, 90))
        self.add_contact.setMinimumSize(QSize(100, 90))
        self.add_contact.setMaximumSize(QSize(100, 90))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(8)
        self.add_contact.setFont(font1)
        self.name = QLineEdit(Form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(179, 510, 200, 30))
        self.name.setMinimumSize(QSize(200, 30))
        self.name.setMaximumSize(QSize(200, 30))
        self.phone = QLineEdit(Form)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(180, 550, 200, 30))
        self.phone.setMinimumSize(QSize(200, 30))
        self.phone.setMaximumSize(QSize(200, 30))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 510, 50, 30))
        self.label.setMinimumSize(QSize(50, 30))
        self.label.setMaximumSize(QSize(50, 30))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 550, 50, 30))
        self.label_2.setMinimumSize(QSize(50, 30))
        self.label_2.setMaximumSize(QSize(50, 30))
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_background.setText("")
        self.home_app.setText("")
        self.home_background_3.setText("")
        self.head_label.setText(QCoreApplication.translate("Form", u"My Contacts", None))
        self.add_contact.setText(QCoreApplication.translate("Form", u"Add to contacts", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Phone", None))
    # retranslateUi

