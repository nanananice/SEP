import js
from pyscript import document
from abc import ABC, abstractclassmethod

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
class Menu(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def drawWidget(self):
        # Add a div to hold the map
        self.map_div = document.createElement("div")
        self.map_div.id = "map"
        self.map_div.style.height = "400px"
        self.element.appendChild(self.map_div)
        # Load the Google Maps
        self.load_google_maps()

    def load_google_maps(self):
        # Assuming you have defined a function in JS to initialize the map
        js_code = """
        function initMap(lat, lng) {
            var map = new google.maps.Map(document.getElementById('map'), {
                center: {lat: lat, lng: lng},
                zoom: 8
            });
        }
        """
        js.eval(js_code)
        # Get current location and initialize the map
        def success(position):
            lat = position.coords.latitude
            lng = position.coords.longitude
            js.initMap(lat, lng)
        
        def error():
            js.alert("Unable to retrieve your location")
        
        if js.navigator.geolocation:
            js.navigator.geolocation.getCurrentPosition(success, error)
        else:
            js.alert("Geolocation is not supported by this browser.")


if __name__ == "__main__":
    output = Menu("container")
    output.drawWidget()