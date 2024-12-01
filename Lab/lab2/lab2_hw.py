import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class convert(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.conversion_rates = {
            'THB': [30, '฿', 'Thai Baht'],
            'USD': [1, '$', 'US Dollar'],
            'CNY': [7, 'CN¥', 'Chinese Yuan'],
            'JPY': [140, 'JP¥', 'Japanese Yen'],
            'KRW': [1300, '₩', 'South Korean Won'],
            'EUR': [0.9, '€', 'Euro'],
            'CHF': [0.9, 'CHF', 'Swiss Franc'],
            'HKD': [8, 'HK$', 'Hong Kong Dollar'],
            'SGD': [1.3, 'S$', 'Singapore Dollar'],
            'MYR': [4.7, 'RM', 'Malaysian Ringgit'],
            'IDR': [15490, 'Rp', 'Indonesian Rupiah'],
            'BND': [1.3, 'B$', 'Brunei Dollar'],
            'INR': [83, '₹', 'Indian Rupee']
        }
        vbox = QVBoxLayout()
        self.label1 = QLabel(self)
        self.label1.setText("CONVERT:")
        vbox.addWidget(self.label1)
        self.currency1 = QComboBox()
        for x in self.conversion_rates:
            self.currency1.addItem(x)
        vbox.addWidget(self.currency1)
        self.label2 = QLabel(self)
        self.label2.setText("TO:")
        vbox.addWidget(self.label2)
        self.currency2 = QComboBox()
        for x in self.conversion_rates:
            self.currency2.addItem(x)
        vbox.addWidget(self.currency2)
        self.label3 = QLabel(self)
        self.label3.setText("INPUT AMOUNT:")
        vbox.addWidget(self.label3)
        self.entry = QLineEdit(self)
        vbox.addWidget(self.entry)
        conv = QPushButton("EXCHANGE!", self)
        conv.clicked.connect(self.convert_currency)
        vbox.addWidget(conv)
        self.setLayout(vbox)
        self.show()

    def convert_currency(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        from_currency = self.currency1.currentText()
        to_currency = self.currency2.currentText()
        amount = self.entry.text()       
        if str(amount) == '':
            QMessageBox.warning(self, "ERROR!", "Input amount")
        total = float(amount) * float(self.conversion_rates[to_currency][0]) / float(self.conversion_rates[from_currency][0])
        label = QLabel(self)
        label.setText(f"{self.conversion_rates[from_currency][1]} {amount} ({self.conversion_rates[from_currency][2]}) = {self.conversion_rates[to_currency][1]} {round(total,4)} ({self.conversion_rates[to_currency][2]})")
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