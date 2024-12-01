import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class simple_timer_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(time.strftime("%X"))
        vbox.addWidget(self.label)
        timer = QTimer(self)
        timer.timeout.connect(self.updateValue)
        timer.start(500)
        self.setLayout(vbox)
        self.show()

    def updateValue(self):
        self.label.setText(time.strftime("%X"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = simple_timer_window()
    sys.exit(app.exec())
