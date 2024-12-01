# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'phone_map.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 700)
        Form.setMinimumSize(QSize(400, 700))
        Form.setMaximumSize(QSize(400, 700))
        Form.setStyleSheet(u"QWidget::setFixedSize(400,800)\n"
"")
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
        icon.addFile(u"home_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_app.setIcon(icon)
        self.home_app.setIconSize(QSize(80, 80))
        self.home_background = QLabel(Form)
        self.home_background.setObjectName(u"home_background")
        self.home_background.setGeometry(QRect(0, 600, 400, 100))
        self.home_background.setMinimumSize(QSize(400, 100))
        self.home_background.setMaximumSize(QSize(400, 100))
        self.home_background.setStyleSheet(u"background-color: rgb(98, 98, 98);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-210, 100, 611, 501))
        self.label.setPixmap(QPixmap(u"map_vector.jpg"))
        self.home_background_2 = QLabel(Form)
        self.home_background_2.setObjectName(u"home_background_2")
        self.home_background_2.setGeometry(QRect(0, 0, 400, 100))
        self.home_background_2.setMinimumSize(QSize(400, 100))
        self.home_background_2.setMaximumSize(QSize(400, 100))
        self.home_background_2.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.nav_button = QPushButton(Form)
        self.nav_button.setObjectName(u"nav_button")
        self.nav_button.setGeometry(QRect(350, 60, 40, 30))
        self.nav_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.location_from = QLineEdit(Form)
        self.location_from.setObjectName(u"location_from")
        self.location_from.setGeometry(QRect(90, 10, 250, 30))
        self.location_from.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.location_to = QLineEdit(Form)
        self.location_to.setObjectName(u"location_to")
        self.location_to.setGeometry(QRect(90, 60, 250, 30))
        self.location_to.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.switch_button = QPushButton(Form)
        self.switch_button.setObjectName(u"switch_button")
        self.switch_button.setGeometry(QRect(350, 10, 40, 30))
        self.switch_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"updown_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.switch_button.setIcon(icon1)
        self.add_location_from = QPushButton(Form)
        self.add_location_from.setObjectName(u"add_location_from")
        self.add_location_from.setGeometry(QRect(50, 10, 30, 30))
        self.add_location_from.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px\n"
"")
        self.add_location_to = QPushButton(Form)
        self.add_location_to.setObjectName(u"add_location_to")
        self.add_location_to.setGeometry(QRect(50, 60, 30, 30))
        self.add_location_to.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px\n"
"")
        self.back_button = QPushButton(Form)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(10, 10, 30, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px\n"
"")
        self.home_background.raise_()
        self.home_app.raise_()
        self.label.raise_()
        self.home_background_2.raise_()
        self.nav_button.raise_()
        self.location_from.raise_()
        self.location_to.raise_()
        self.switch_button.raise_()
        self.add_location_from.raise_()
        self.add_location_to.raise_()
        self.back_button.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.home_app.setText("")
        self.home_background.setText("")
        self.label.setText("")
        self.home_background_2.setText("")
        self.nav_button.setText(QCoreApplication.translate("Form", u"Go", None))
        self.switch_button.setText("")
        self.add_location_from.setText(QCoreApplication.translate("Form", u"Add", None))
        self.add_location_to.setText(QCoreApplication.translate("Form", u"Add", None))
        self.back_button.setText(QCoreApplication.translate("Form", u"<", None))
    # retranslateUi

