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

class AnimationPin(AbstractWidget):
    def __init__(self, element_id, x=0, y=0):
        super().__init__(element_id)
        self.x = x
        self.y = y
        self.counter = 1
        self.now = True
        
    def on_setInterval(self):
        if self.now == True:
            self.counter += 1

        if self.counter > 10:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/pin"+str(self.counter)+".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "50px"
        self.image.style.height = "50px"
        self.image.src = "./images/pin1.png"
        self.image.style.position = "absolute"
        self.image.style.left = f"{self.x}px"
        self.image.style.top = f"{self.y}px"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        self.jump_sound = js.Audio.new("./sounds/pin_bounce.wav")
        self.element.appendChild(self.button)

class MainScreen(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.label_start_status = False
        self.label_end_status = False
        self.startx = 0
        self.starty = 0
        self.endx = 0
        self.endy = 0

    def drawWidget(self):
        self.maindiv = document.createElement("div")

        self.button_start = document.createElement("button")
        self.button_start.innerText = "Add Start"
        self.button_start.style.width = "100px"

        self.button_start.onclick = self.edit_start
        self.maindiv.onclick = lambda event: self.handle_click(event)
        self.maindiv.appendChild(self.button_start)

        self.label_start = document.createElement("input")  
        self.label_start.setAttribute("type", "text")
        self.label_start.style.width = "400px"
        self.maindiv.appendChild(self.label_start)

        self.button_go = document.createElement("button")
        self.button_go.innerText = "Go"
        self.button_go.style.width = "100px"
        self.button_go.onclick = self.drawline
        self.maindiv.appendChild(self.button_go)

        self.button_end = document.createElement("button")
        self.button_end.innerText = "Add End"
        self.button_end.style.width = "100px"
        self.button_end.onclick = self.edit_end
        self.maindiv.appendChild(self.button_end)

        self.label_end = document.createElement("input")
        self.label_end.setAttribute("type", "text")
        self.label_end.style.width = "400px"
        self.maindiv.appendChild(self.label_end)

        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "800px"
        self.image.src = "./images/map.png"
        self.image.style.position = "relative"
        self.image.style.zIndex = "0"  

        self.canvas = document.createElement("canvas")
        self.canvas.style.position = "absolute"
        self.canvas.width = 600  
        self.canvas.height = 800
        self.context = self.canvas.getContext("2d")
        self.canvas.style.left = "0px"  
        self.canvas.style.top = "0px"  
        self.canvas.style.pointerEvents = "none"  
        self.canvas.style.zIndex = "1"  

        self.maindiv.appendChild(self.image)
        self.maindiv.appendChild(self.canvas)

        self.element.appendChild(self.maindiv)

    def handle_click(self, event):
        x = event.clientX
        y = event.clientY

        if self.label_start_status == True:
            self.label_start.value = f"Clicked at position X: {x}, Y: {y}"
            self.startx = x
            self.starty = y
            self.label_start_status = False
        elif self.label_end_status == True:
            self.label_end.value = f"Clicked at position X: {x}, Y: {y}"
            self.endx = x
            self.endy = y
            self.label_end_status = False

    def edit_start(self,event):
        self.label_start_status = True
        event.stopPropagation()  

    def edit_end(self,event):
        self.label_end_status = True
        event.stopPropagation()  

    def drawline(self, event):
        self.context.clearRect(0, 0, self.canvas.width, self.canvas.height)

        startx = int(self.startx)
        starty = int(self.starty)
        endx = int(self.endx)
        endy = int(self.endy)

        self.context.beginPath()
        self.context.moveTo(startx, starty)  
        self.context.lineTo(endx, endy)  
        self.context.strokeStyle = "red" 
        self.context.lineWidth = 1 
        self.context.stroke() 

        pin = AnimationPin("container", self.endx-25, self.endy-40)
        pin.drawWidget()

if __name__ == "__main__":
    output = MainScreen("container")
    output.drawWidget()