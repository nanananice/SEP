import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class convert(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label1 = QLabel(self)
        self.label1.setText("CONVERTING MACHINE:")
        vbox.addWidget(self.label1)
        self.label2 = QLabel(self)
        self.label2.setText("INPUT AMOUNT:")
        vbox.addWidget(self.label2)
        self.entry = QLineEdit(self)
        vbox.addWidget(self.entry)
        usd = QPushButton("USD", self)
        usd.clicked.connect(self.to_USD)
        vbox.addWidget(usd)
        thb = QPushButton("THB", self)
        thb.clicked.connect(self.to_THB)
        vbox.addWidget(thb)
        self.setLayout(vbox)
        self.show()

    def to_USD(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        amount = self.entry.text()       
        total = float(amount) / 30
        label = QLabel(self)
        label.setText(f"{amount} THB = {round(total,4)} USD")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def to_THB(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        amount = self.entry.text()       
        total = float(amount) * 30
        label = QLabel(self)
        label.setText(f"{amount} USD = {round(total,4)} THB")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = convert()
    sys.exit(app.exec())