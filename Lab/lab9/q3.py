import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime
import random

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None
    
    @property
    def element(self):
        """Return Dom"""
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
    @abstractmethod
    def drawWidget(self):
        pass
    
class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.now = True

    def on_click(self, event):
        if self.button.innerText == "pause":
            self.now = False
            self.button.innerText = "play"
        else:
            self.now = True
            self.button.innerText = "pause"

    def on_setInterval(self):
        if self.now == True:
            self.counter += 1

        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/frame-"+str(self.counter)+".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
    
    def randomcolor(self, event):
        color = random.randrange(0, 2**24)  
        hex_color = hex(color)
        std_color = "#" + hex_color[2:]
        self.element.style.backgroundColor = std_color

    def drawWidget(self):
        super().drawWidget()
        self.button1= document.createElement("button")
        self.button1.innerText = "color"
        self.button1.style.width = "600px"
        self.button1.onclick = self.randomcolor
        self.element.appendChild(self.button1)





if __name__ == "__main__":
    output = ColorfulAnimationWidget("container")
    output.drawWidget()