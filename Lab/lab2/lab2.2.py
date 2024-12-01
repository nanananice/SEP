import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class simple_spin_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)

        plus = QPushButton("+", self)
        plus.clicked.connect(self.updateNumber)
        vbox.addWidget(plus)

        minus = QPushButton("-", self)
        minus.clicked.connect(self.updateNumber)
        vbox.addWidget(minus)

        zero = QPushButton("0", self)
        zero.clicked.connect(self.updateNumber)
        vbox.addWidget(zero)
        self.setLayout(vbox)
        self.show()

    def updateNumber(self):
        text = self.sender().text()
        if text == "+":
            self.num += 1
        elif text == "-":
            self.num -= 1
        elif text == "0":
            self.num = 0   
        self.label.setText(str(self.num))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = simple_spin_window()
    sys.exit(app.exec())
