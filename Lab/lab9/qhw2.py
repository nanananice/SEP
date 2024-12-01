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

class Total(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def tobaht(self, event):
        text = self.input_text.value
        js.alert(str(int(text)/30) + " dollar")

    def tousd(self, event):
        text = self.input_text.value
        js.alert(str(int(text)*30) + " baht")


    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "To BAHT"
        self.button.onclick = self.tobaht
        self.element.appendChild(self.button)

        self.button2 = document.createElement("button")
        self.button2.innerText = "To USD"
        self.button2.onclick = self.tousd
        self.element.appendChild(self.button2)


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
        self.newwidget = document.createElement("div")
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.newwidget.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.button = document.createElement("button")
        self.button.innerText = "pause"
        self.button.style.width = "600px"
        self.button.onclick = self.on_click
        self.newwidget.appendChild(self.button)
        self.element.appendChild(self.newwidget)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        super().__init__(element_id)

    def randomcolor(self, event):
        color = random.randrange(0, 2**24)  
        hex_color = hex(color)
        std_color = "#" + hex_color[2:]
        self.newwidget.style.backgroundColor = std_color
        
    def drawWidget(self):
        super().drawWidget()
        self.button1= document.createElement("button")
        self.button1.innerText = "color"
        self.button1.style.width = "600px"
        self.button1.onclick = self.randomcolor
        self.newwidget.appendChild(self.button1)
        self.element.appendChild(self.newwidget)


class addable_ui(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def add_widgetq1(self, event):
        widget_no = Total("container")
        widget_no.drawWidget()
        
    def add_widgetq2(self, event):
        widget_no = AnimationWidget("container")
        widget_no.drawWidget()
    
    def add_widgetq3(self, event):
        widget_no = ColorfulAnimationWidget("container")
        widget_no.drawWidget()

    def drawWidget(self):
        self.buttonq1 = document.createElement("button")
        self.buttonq1.style.width = "600px"
        self.buttonq1.innerText = "Add Q1"
        self.buttonq1.onclick = self.add_widgetq1
        self.element.appendChild(self.buttonq1)

        self.buttonq2 = document.createElement("button")
        self.buttonq2.style.width = "600px"
        self.buttonq2.innerText = "Add Q2"
        self.buttonq2.onclick = self.add_widgetq2
        self.element.appendChild(self.buttonq2)

        self.buttonq3 = document.createElement("button")
        self.buttonq3.style.width = "600px"
        self.buttonq3.innerText = "Add Q3"
        self.buttonq3.onclick = self.add_widgetq3
        self.element.appendChild(self.buttonq3)

if __name__ == "__main__":
    output = addable_ui("container")
    output.drawWidget()