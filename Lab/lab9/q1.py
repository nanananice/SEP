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

if __name__ == "__main__":
    output = Total("container")
    output.drawWidget()