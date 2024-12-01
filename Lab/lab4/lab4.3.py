import sys
import random
from PySide6.QtCore import QTimer, QRect, QUrl
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtMultimedia import QSoundEffect

class Rabbit:
    def __init__(self):
        self.image = QPixmap("lab4/images/rabbit.png")
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_w, arena_h):
        self.x = random.randint(0, arena_w - self.w)
        self.y = random.randint(0, arena_h - self.h)

    def is_hit(self, mouse_x, mouse_y):
        if (mouse_x >= self.x - 40 and mouse_x <= self.x + 40 and mouse_y >= self.y - 40 and mouse_y <= self.y + 40):
            return True
        else:
            return False

class AnimationArea(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setMinimumSize(300, 300)
        self.arena_w = 300
        self.arena_h = 300
        self.rabbit = Rabbit()
        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(500)
        self.QSH = QSoundEffect()
        self.QSH.setSource(QUrl.fromLocalFile("lab4/sounds/rabbit_hit.wav"))
        self.QSM = QSoundEffect()
        self.QSM.setSource(QUrl.fromLocalFile("lab4/sounds/rabbit_missed.wav"))

    def mousePressEvent(self, e):
        if self.rabbit.is_hit(e.pos().x(), e.pos().y()):
            self.QSH.play()
            
            print("Hit!!!")
        else:
            self.QSM.play()
            print("Miss")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        self.rabbit.draw(p)
        p.end()

    def update_value(self):
        self.rabbit.random_pos(self.arena_w, self.arena_h)
        self.update()

class SimpleAnimationWindow(QWidget):
    def __init__(self):
        super().__init__(None)
        self.anim_area = AnimationArea()
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        self.setLayout(layout)
        self.setMinimumSize(330, 400)

def main():
    app = QApplication(sys.argv)
    w = SimpleAnimationWindow()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
