import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from phone_map import Ui_Form as phone_map_ui

class PhoneMain(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = phone_map_ui()
        self.setWindowTitle("Simple Map Gui")
        self.ui.setupUi(self)
        self.layout = QVBoxLayout(self)
        self.location_from_pos = [0, 0]
        self.location_to_pos = [0, 0]
        self.ui.add_location_from.clicked.connect(self.addLocationFrom)
        self.ui.add_location_to.clicked.connect(self.addLocationTo)
        self.ui.switch_button.clicked.connect(self.switch)
        self.ui.nav_button.clicked.connect(self.draw)
        self.ui.back_button.clicked.connect(self.reset)

    def mousePressEvent(self, event):
        x = event.position().x()
        y = event.position().y()

        if 0 <= x <= 400 and 100 <= y <= 600:
            if self.setting_location_from_pos:
                self.location_from_pos = [x, y]
                print(f"Location from set to {self.location_from_pos}")
            elif self.setting_location_to_pos:
                self.location_to_pos = [x, y]
                print(f"Location to set to {self.location_to_pos}")

            self.setting_location_from_pos = False
            self.setting_location_to_pos = False
            self.set_value()

    def addLocationFrom(self):
        self.setting_location_from_pos = True
        self.setting_location_to_pos = False

    def addLocationTo(self):
        self.setting_location_from_pos = False
        self.setting_location_to_pos = True
    
    def switch(self):
        temp = self.location_to_pos
        self.location_to_pos = self.location_from_pos
        self.location_from_pos = temp
        self.set_value()

    def draw(self):
        self.anim_area = Animation_pin(self.location_to_pos, self.location_from_pos)
        self.layout.addWidget(self.anim_area)
    
    def set_value(self):
        self.ui.location_from.setText(f"X: {self.location_from_pos[0]} Y: {self.location_from_pos[1]}")
        self.ui.location_to.setText(f"X: {self.location_to_pos[0]} Y: {self.location_to_pos[1]}") 

    def reset(self):
        self.location_from_pos = [0, 0]
        self.location_to_pos = [0, 0]
        self.set_value()

class Animation_pin(QWidget):
    def __init__(self, location_to_pos, location_from_pos):
        QWidget.__init__(self, None)
        self.frame_no = 0
        self.images = [QPixmap("pin" + str(i + 1) + ".png") for i in range(10)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateAnimation)
        self.timer.start(100)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("bounce.wav"))
        self.location_to_pos = location_to_pos
        self.location_from_pos = location_from_pos

    def updateAnimation(self):
        self.frame_no = (self.frame_no + 1) % 10
        if self.frame_no == 1:
            self.QSE.play()
        self.update() 


    def paintEvent(self, e):
        p = QPainter(self)

        p.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        p.drawLine(self.location_from_pos[0], self.location_from_pos[1], self.location_to_pos[0], self.location_to_pos[1])

        p.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        p.drawEllipse(QPoint(self.location_from_pos[0], self.location_from_pos[1]), 5, 5)

        pin_size = QSize(100, 80)
        p.drawPixmap(QRect(self.location_to_pos[0] - 50, self.location_to_pos[1] - 63, pin_size.width(), pin_size.height()), self.images[self.frame_no])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = PhoneMain()
    w.show()
    sys.exit(app.exec())
