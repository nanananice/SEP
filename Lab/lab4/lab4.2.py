import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect

class Animation_area(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, None)
        self.parent = parent  # Reference to the parent widget
        self.frame_no = 0
        self.images = [QPixmap("lab4/images/frame-" + str(i + 1) + ".png") for i in range(20)]
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("lab4/sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        if self.parent.is_playing:  # Only update if playing
            self.frame_no += 1
            if self.frame_no >= 20:
                self.frame_no = 0
                self.QSE.play()
            self.update()

class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.is_playing = True
        self.button = QPushButton("Pause")
        self.anim_area = Animation_area(self)  # Pass self as parent
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setMinimumSize(330, 400)
        self.button.clicked.connect(self.change)

    def change(self):
        if self.button.text() == "Play":
            self.is_playing = True
            self.button.setText("Pause")
        else:
            self.is_playing = False
            self.button.setText("Play")
        self.anim_area.update_value()  # Reflect the change immediately

def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
