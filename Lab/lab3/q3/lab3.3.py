import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from program3_3 import Ui_Form

class TestUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(self.edit)
        self.ui.button_2.clicked.connect(self.edit)
        self.ui.button_3.clicked.connect(self.edit)
        self.ui.button_4.clicked.connect(self.edit)
        self.ui.button_5.clicked.connect(self.edit)
        self.ui.button_6.clicked.connect(self.edit)
        self.ui.button_7.clicked.connect(self.edit)
        self.ui.button_8.clicked.connect(self.edit)
        self.ui.button_9.clicked.connect(self.edit)
        self.ui.button_0.clicked.connect(self.edit)
        self.ui.button_mul.clicked.connect(self.edit)
        self.ui.button_hash.clicked.connect(self.edit)
        self.ui.button_del.clicked.connect(self.delete_last)
        self.ui.button_talk.clicked.connect(self.dial)

    def edit(self):
        add = self.sender().text()
        self.ui.label.setText(self.ui.label.text() + add) 
    
    def delete_last(self):
        self.ui.label.setText((self.ui.label.text())[:-1]) 

    def dial(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Dialing << " + self.ui.label.text() + " >>")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TestUI()
    w.show()
    sys.exit(app.exec())
