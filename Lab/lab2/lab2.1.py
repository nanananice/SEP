import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton)

def say_hello():
    print('Hello World!')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    w.setWindowTitle('Simple')
    btn = QPushButton('Say hello!', w) 
    btn.clicked.connect(say_hello)
    w.show()

    sys.exit(app.exec())