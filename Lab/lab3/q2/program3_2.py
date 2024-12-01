# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program3_2.ui'
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
        Form.resize(400, 300)
        self.num_label = QLabel(Form)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(40, 50, 131, 201))
        font = QFont()
        font.setFamilies([u"Segoe Script"])
        font.setPointSize(36)
        font.setBold(True)
        self.num_label.setFont(font)
        self.num_label.setLayoutDirection(Qt.LeftToRight)
        self.num_label.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(210, 20, 171, 261))
        self.dec_button = QPushButton(self.widget)
        self.dec_button.setObjectName(u"dec_button")
        self.dec_button.setGeometry(QRect(10, 160, 151, 91))
        self.dec_button.setFont(font)
        self.inc_button = QPushButton(self.widget)
        self.inc_button.setObjectName(u"inc_button")
        self.inc_button.setGeometry(QRect(10, 10, 151, 91))
        self.inc_button.setFont(font)
        self.reset = QPushButton(self.widget)
        self.reset.setObjectName(u"reset")
        self.reset.setGeometry(QRect(10, 100, 151, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe Script"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.reset.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.num_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.dec_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.inc_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.reset.setText(QCoreApplication.translate("Form", u"RESET", None))
    # retranslateUi

