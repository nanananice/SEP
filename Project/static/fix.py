import js
from pyscript import document
from abc import ABC, abstractmethod
from pyodide.http import pyfetch
import json
from js import window, document

userWidth = js.window.innerWidth
userHeight = js.window.innerHeight

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
        self.picked_destination = []
   
        self.picked_number = 1
        self.destinations = {}
        self.destination_counter = 1

    def gatherDestinationData(self):
        query_params = []
        for destination_id, destination in self.destinations.items():
            place = destination["place_input"].value
            date_from = destination["date_input_from"].value
            date_to = destination["date_input_to"].value
            if place and date_from and date_to:  
                params = f"place{destination_id}={place}&dateFrom{destination_id}={date_from}&dateTo{destination_id}={date_to}"
                query_params.append(params)
        query_string = "&".join(query_params)
        print(query_string)
        return query_string
    
    """def redirect_to_map(self, event):
        query_string = self.gatherDestinationData()
        base_url = '/map'
        if query_string:
            full_url = f"{base_url}?{query_string}"
        else:
            full_url = base_url
        js.window.location.href = full_url """

    async def redirect_to_map(self, event):
        query_string = self.gatherDestinationData()
        data = {"test":query_string}
        response = await pyfetch(url="http://127.0.0.1:8000/find_random_place",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps(data))
        if response.status == 200:
            data = await response.json() 
            if "Trip_detail" in data:
                trip = data["Trip_detail"]
                existing_trip = js.window.localStorage.getItem("Trip_detail")
                if existing_trip is not None:
                    js.window.localStorage.removeItem("Trip_detail")
                    
                
                js.window.localStorage.setItem("Trip_detail", json.dumps(trip))

                js.window.location.href = '/map'

    def redirect_to_login(self, event):
        js.window.location.href = '/login'


    def drawContent(self):
        self.content_container = document.createElement("div")
        self.content_container.style.width = "100%"
        self.content_container.style.maxWidth = "700px"
        self.content_container.style.margin = "10vh auto"
        self.content_container.style.padding = "20px"
        self.content_container.style.boxSizing = "border-box"

        self.topic = document.createElement("div")
        self.topic.style.textAlign = "center"
        self.topic.style.padding = "10px"
        self.topic.style.marginTop = "30px"
        self.topic.style.fontFamily = "Rubik, sans-serif"
        self.topic.style.fontSize = "32px"
        self.topic.innerText = "Plan The Trail"

        self.each_place = document.createElement("div")

        self.place = document.createElement("div")
        self.place.style.marginTop = "30px"
        self.place.style.fontFamily = "Rubik, sans-serif"
        self.place.style.fontSize = "18px"
        self.place.innerText = "Where do you want to gos?"

        self.place_input = document.createElement("input")                                      
        self.place_input.className = 'place-input'      
        self.place_input.setAttribute('type', 'text')
        self.place_input.style.width = "75%"
        self.place_input.style.borderRadius = "5px"
        self.place_input.style.padding = "10px"
        self.place_input.style.marginTop = "10px"
        self.place_input.style.border = "1px solid #ddd"
        
        self.element.appendChild(self.place_input)
        
        js.eval('initAutocomplete()')

        self.date_container = document.createElement("div")
        self.date_container.style.display = "flex"
        self.date_container.style.justifyContent = "space-between"
        self.date_container.style.marginTop = "10px"

        self.date_container.style.maxWidth = "50%"

        self.date_from_container = document.createElement("div")
        self.date_from_container.style.flex = "1"

        self.date_label_from = document.createElement("div")
        self.date_label_from.innerText = "From:"
        self.date_from_container.appendChild(self.date_label_from)

        self.date_input_from = document.createElement("input")
        self.date_input_from.type = "date"
        self.date_input_from.style.cursor = "pointer"
        self.date_input_from.style.borderRadius = "5px"
        self.date_input_from.style.padding = "10px"
        self.date_input_from.style.border = "1px solid #ddd"
        self.date_from_container.appendChild(self.date_input_from)

        self.date_to_container = document.createElement("div")
        self.date_to_container.style.flex = "1"

        self.date_label_to = document.createElement("div")
        self.date_label_to.innerText = "To:"
        self.date_to_container.appendChild(self.date_label_to)

        self.date_input_to = document.createElement("input")
        self.date_input_to.type = "date"
        self.date_input_to.style.cursor = "pointer"
        self.date_input_to.style.borderRadius = "5px"
        self.date_input_to.style.padding = "10px"
        self.date_input_to.style.border = "1px solid #ddd"
        self.date_to_container.appendChild(self.date_input_to)

        self.date_container.appendChild(self.date_from_container)
        self.date_container.appendChild(self.date_to_container)

        style = document.createElement('style')
        style.innerHTML = """
        .date-input:hover {
            background-color: #eee !important;
            border: 1px solid #aaa !important;
            color: #000 !important;
        }
        """
        document.head.appendChild(style)
        
        self.date_input_from.className = 'date-input'
        self.date_input_from.style.transition = 'background-color 0.3s ease'
        self.date_input_to.className = 'date-input'
        self.date_input_to.style.transition = 'background-color 0.3s ease'

        self.button_add = document.createElement("button")
        self.button_add.innerText = "+ Add Destination"
        self.button_add.style.width = "20%"
        self.button_add.style.borderRadius = "10px"
        self.button_add.style.padding = "10px"
        self.button_add.style.marginTop = "10px"
        self.button_add.style.color = "white"
        self.button_add.style.backgroundColor = "#ff7065"
        self.button_add.style.border = "1px solid #ff7065"
        self.button_add.style.cursor = "pointer"
        style = document.createElement('style')
        style.innerHTML = """
        .add-button:hover {
            background-color: #28a745 !important;
            border: 1px solid #28a745 !important;
        }
        """
        document.head.appendChild(style)

        self.button_add.className = 'add-button'
        self.button_add.style.transition = 'background-color 0.3s ease'

        self.content_container.appendChild(self.topic)
        self.content_container.appendChild(self.place)
        self.each_place.appendChild(self.place_input)
        self.each_place.appendChild(self.date_container)
        self.content_container.appendChild(self.each_place)
        self.button_add.onclick = self.addPlace
        self.content_container.appendChild(self.button_add)   
        self.element.appendChild(self.content_container)
        self.each_place.id = f"destination-{0}"
        self.destinations[0] = {
            "element": self.each_place,
            "place_input": self.place_input,
            "date_input_from": self.date_input_from,
            "date_input_to": self.date_input_to
        }                

    def createDestinationElement(self):
        destination_id = self.destination_counter
        each_place = document.createElement("div")
        each_place.id = f"destination-{destination_id}"
        each_place.style.display = "flex"
        each_place.style.flexDirection = "column"

        horizontalContainer = document.createElement("div")
        horizontalContainer.style.display = "flex"
        horizontalContainer.style.alignItems = "center"

        verticalLine = document.createElement("div")
        verticalLine.style.borderLeft = "3px dotted #aaa"
        verticalLine.style.height = "60px"
        verticalLine.style.marginLeft = "10px"
        verticalLine.style.marginRight = "10px"
        verticalLine.style.marginTop = "10px"
        verticalLine.style.position = "relative"

        horizontalContainer.appendChild(verticalLine)

        img = document.createElement("img")
        img.src = "/static/pic/bin_logo.png"
        img.style.width = "100%"

        next_label = document.createElement("div")
        next_label.style.paddingTop = "10px"
        next_label.innerText = "Going next to"
        self.remove_button = document.createElement("button")
        self.remove_button.style.cursor = "pointer"
        self.remove_button.style.border = "1px solid #ddd"
        self.remove_button.style.borderRadius = "15px"
        self.remove_button.appendChild(img)
        self.remove_button.style.width = "30px"
        self.remove_button.style.height = "30px"
        self.remove_button.style.marginTop = "10px"
        self.remove_button.style.marginLeft = "20px"
        self.remove_span = document.createElement("span")
        self.remove_span.style.border = "1px solid #ccc"
        self.remove_span.style.backgroundColor = "#ccc"
        self.remove_span.style.borderRadius = "15px"
        self.remove_span.style.color = "#000"
        self.remove_span.style.fontSize = "13px"
        self.remove_span.style.height = "25px"
        self.remove_span.style.lineHeight = "30px"
        self.remove_span.style.position = "absolute"
        self.remove_span.style.top = "-40px"
        self.remove_span.style.left = "50%"
        self.remove_span.style.transform = "translateX(-50%)"
        self.remove_span.style.whiteSpace = "nowrap"
        self.remove_span.style.textAlign = "center"
        self.remove_span.style.display = "none"
        self.remove_span.style.padding = "0 5px 5px"
        self.remove_span.innerText = "Remove This Place"
        self.remove_span.style.fontFamily = "Rubik, sans-serif"
        self.remove_span.style.fontSize = "12px"
        
        style = document.createElement('style')
        style.innerHTML = """
        .remove-button {
            position: relative;
        }

        .remove-button .span {
            display: none;
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%);
            whiteSpace: nowrap;
        }

        .remove-button:hover .span {
            display: block !important;
        }

        .remove-button:hover {
            background-color: #aaa !important;
            border: 1px solid #aaa !important;
        }

        span:after{
            content:'';
            position:absolute;
            bottom:-6px; 
            width:10px;
            height:10px;
            border-bottom:1px solid #ccc;
            border-right:1px solid #ccc;
            background:#ccc;
            left:50%;
            margin-left:-5px; /* Adjusted for centering */
            -moz-transform:rotate(45deg);
            -webkit-transform:rotate(45deg);
            transform:rotate(45deg);
        }

        .span {
            display: none;
            position: absolute;
            top: -40px; /* Adjust based on actual layout */
            left: 50%;
            transform: translateX(-50%);
            background-color: #fff; /* Or any other background */
            color: #000; /* Text color */
            padding: 5px; /* Adjust as needed */
            border: 1px solid #ccc; /* Border color */
            border-radius: 5px; /* Optional, for rounded corners */
            white-space: nowrap;
            z-index: 10; /* Ensure it's above other elements */
        }
        """
        document.head.appendChild(style)

        self.remove_button.className = 'remove-button'
        self.remove_button.style.transition = 'background-color 0.3s ease'

        self.remove_span.className = 'span'
        self.remove_button.appendChild(self.remove_span)

        self.remove_button.onclick = lambda event: self.removePlace(destination_id)
        horizontalContainer.appendChild(next_label)
        horizontalContainer.appendChild(self.remove_button)
        each_place.appendChild(horizontalContainer)

        place_input = document.createElement("input")
        place_input.className = 'place-input'  
        place_input.setAttribute('type', 'text')
        place_input.style.width = "75%"
        place_input.style.borderRadius = "5px"
        place_input.style.padding = "10px"
        place_input.style.marginTop = "10px"
        place_input.style.border = "1px solid #ddd"
        each_place.appendChild(place_input)

        date_container = document.createElement("div")
        date_container.style = self.date_container.style.cssText

        date_from_container = document.createElement("div")
        date_from_container.style = self.date_from_container.style.cssText
        date_input_from = document.createElement("input")
        date_input_from.type = "date"
        date_input_from.style = self.date_input_from.style.cssText
                
        date_label_from = document.createElement("div")
        date_label_from.innerText = "From:"
        date_from_container.appendChild(date_label_from)
        date_from_container.appendChild(date_input_from)
        
        date_to_container = document.createElement("div")
        date_to_container.style = self.date_to_container.style.cssText
        date_input_to = document.createElement("input")
        date_input_to.type = "date"
        date_input_to.style = self.date_input_to.style.cssText
        
        date_label_to = document.createElement("div")
        date_label_to.innerText = "To:"
        date_to_container.appendChild(date_label_to)
        date_to_container.appendChild(date_input_to)



        date_container.appendChild(date_from_container)
        date_container.appendChild(date_to_container)

        each_place.appendChild(date_container)

        self.destinations[destination_id] = {
            "element": each_place,
            "place_input": place_input,
            "date_input_from": date_input_from,
            "date_input_to": date_input_to
        }

        self.destination_counter += 1

        return each_place

    def addPlace(self, event):
        print("asdasdasd")
        new_destination = self.createDestinationElement()
        self.content_container.insertBefore(new_destination, self.button_add)
        js.eval('initAutocomplete()')

    def removePlace(self, destination_id):
        destination_element_id = f"destination-{destination_id}"
        if destination_id in self.destinations:
            destination_element = self.destinations[destination_id]['element']
            destination_element.parentNode.removeChild(destination_element)
            del self.destinations[destination_id]



    def drawPeoplenumber(self):
        self.people_container = document.createElement("div")
        self.people = document.createElement("div")
        self.people.style.marginTop = "30px"
        self.people.style.fontFamily = "Rubik, sans-serif"
        self.people.style.fontSize = "18px"
        self.people.innerText = "How many people are going?"
        self.people_box = document.createElement("div")
        self.people_box.style.display = "flex"
        self.people_box.style.alignItems = "center"
        self.people_box.style.justifyContent = "space-between"
        self.people_box.style.padding = "5px"
        self.people_box.style.border = "1px solid #ccc"
        self.people_box.style.borderRadius = "10px"
        self.people_box.style.marginTop = "10px"

        self.number_display = document.createElement("label")
        self.number_display.style.fontFamily = "Rubik, sans-serif"
        self.number_display.style.fontSize = "16px"
        self.number_display.innerText = "1"
        self.number_display.style.width = "30px"
        self.number_display.style.textAlign = "center"
        self.number_display.style.display = "inline-block"
        self.number_display.style.padding = "5px 10px"

        self.two_button = document.createElement("div")
        self.two_button.style.marginRight = "10px" 

        self.minus_button = document.createElement("button")
        self.minus_button.style.border = "1px solid #ddd"
        self.minus_button.style.borderRadius = "5px"
        self.minus_button.style.marginRight = "5px" 
        self.minus_button.style.color = "#ccc"
        self.minus_button.style.backgroundColor = "white"
        self.minus_button.innerText = "-"
        self.minus_button.style.width = "50px"
        self.minus_button.style.height = "30px"
        self.minus_button.style.cursor = "pointer"
        self.minus_button.onclick = self.decrease_number
        
        self.plus_button = document.createElement("button")
        self.plus_button.style.marginLeft = "5px" 
        self.plus_button.style.border = "1px solid #ddd"
        self.plus_button.style.borderRadius = "5px"
        self.plus_button.style.color = "#ccc"
        self.plus_button.style.backgroundColor = "white"
        self.plus_button.innerText = "+"
        self.plus_button.style.width = "50px"
        self.plus_button.style.height = "30px"
        self.plus_button.style.cursor = "pointer"
        self.plus_button.onclick = self.increase_number

        style = document.createElement('style')
        style.innerHTML = """
        .ppl-button:hover {
            background-color: #eee !important;
            border: 1px solid #aaa !important;
            color: #000 !important;
        }
        """
        document.head.appendChild(style)

        self.plus_button.className = 'ppl-button'
        self.plus_button.style.transition = 'background-color 0.3s ease'
        self.minus_button.className = 'ppl-button'
        self.minus_button.style.transition = 'background-color 0.3s ease'

        self.people_box.appendChild(self.number_display)
        self.two_button.appendChild(self.minus_button)
        self.two_button.appendChild(self.plus_button)
        self.people_box.appendChild(self.two_button)
        self.people_container.appendChild(self.people)
        self.people_container.appendChild(self.people_box)
        self.content_container.appendChild(self.people_container)
        
    def increase_number(self, event):
        self.picked_number += 1
        self.number_display.innerText = str(self.picked_number)
        
    def decrease_number(self, event):
        if self.picked_number > 1:
            self.picked_number -= 1
            self.number_display.innerText = str(self.picked_number)

    def drawPlantrail(self):
        self.button_map_div = document.createElement("div")
        self.button_map_div.style.marginTop = "20px"
        self.button_map_div.style.display = "flex"
        self.button_map_div.alignItems = "center"
        self.button_map = document.createElement("button")
        self.button_map.onclick = self.redirect_to_map
        self.button_map.innerText = "Plan the Trail"
        self.button_map.style.width = "20%"
        self.button_map.style.borderRadius = "10px"
        self.button_map.style.padding = "10px"
        self.button_map.style.marginTop = "5px"
        self.button_map.style.color = "white"
        self.button_map.style.backgroundColor = "black"
        self.button_map.style.border = "1px solid black"
        self.button_map.style.cursor = "pointer"
        self.button_map.style.margin = "auto"

        style = document.createElement('style')
        style.innerHTML = """
        .map-button:hover {
            background-color: #333 !important;
            border: 1px solid #333 !important;
        }
        """
        document.head.appendChild(style)

        self.button_map.className = 'map-button'
        self.button_map.style.transition = 'background-color 0.3s ease'

        self.button_map_div.appendChild(self.button_map)
        self.content_container.appendChild(self.button_map_div)

    def drawNavbar(self):
        self.nav_div = document.createElement("div")
        self.setResponsiveStyle(self.nav_div, {
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "space-between",
            "padding": "0 20px",
            "height": "10vh",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "right": "0",
            "backgroundColor": "white",
            "borderBottom": "1px solid #e7e7e7",
            "zIndex": "1000",
        })

        img = document.createElement("img")
        img.src = "/static/pic/Trailblazer_logo.png"
        img.style.height = "5vh" 

        self.trailblazer = document.createElement("div")
        self.trailblazer.style.fontFamily = "Rubik"
        self.trailblazer.style.fontSize = "2vh"  
        self.trailblazer.innerText = "Trailblazer"
        

        self.go_in = document.createElement("div")
        self.go_in.innertext = "Go lok map"
        self.go_in.style.fontFamily = "Rubik, sans-serif"
        self.go_in.style.fontSize = "1.5vh"
        self.go_in.style.padding = "1vh 2vh"
        self.go_in.style.borderRadius = "20px"
        self.go_in.style.backgroundColor = "black"
        self.go_in.style.color = "white"
        self.go_in.style.cursor = "pointer"
        self.go_in.style.marginLeft = "auto"
        self.go_in.onclick = self.go_in_wo_trip
        



        
        self.nav_div.appendChild(img)
        self.nav_div.appendChild(self.trailblazer)
        userData = js.window.localStorage.getItem("access_token")
        name = js.window.localStorage.getItem("user")
        if userData:
            self.profileContainer = document.createElement("div")
            self.profileContainer.innerText = name
            self.profileContainer.style.fontFamily = "Rubik, sans-serif"
            self.profileContainer.style.fontSize = "1.5vh"
            self.profileContainer.style.padding = "1vh 2vh"
            self.profileContainer.style.borderRadius = "20px"
            self.profileContainer.style.backgroundColor = "black"
            self.profileContainer.style.color = "white"
            self.profileContainer.style.cursor = "pointer"
            self.profileContainer.style.marginLeft = "auto"
            self.profileContainer.onclick = self.profile_page
            self.nav_div.appendChild(self.profileContainer)
            

        else:
            self.sign_in = document.createElement("div")
            self.sign_in.innerText = "Sign in"
            self.sign_in.style.fontFamily = "Rubik, sans-serif"
            self.sign_in.style.fontSize = "1.5vh"
            self.sign_in.style.padding = "1vh 2vh"
            self.sign_in.style.borderRadius = "20px"
            self.sign_in.style.backgroundColor = "black"
            self.sign_in.style.color = "white"
            self.sign_in.style.cursor = "pointer"
            self.sign_in.style.marginLeft = "auto"
            self.sign_in.onclick = self.redirect_to_login
            self.nav_div.appendChild(self.sign_in)
                    
      
        #self.nav_div.appendchild(self.go_in)
        
        self.element.appendChild(self.nav_div)
        self.applyGlobalStyles()

    def profile_page(self,event):
        js.window.location.href = '/profile'


    def go_in_wo_trip(self,event):
        existing_trip = js.window.localStorage.getItem("Trip_detail")
        if existing_trip is not None:
            js.window.localStorage.removeItem("Trip_detail")
        js.window.location.href = '/map'


    def logout(self,event):
        js.window.localStorage.removeItem('access_token')
        js.window.localStorage.removeItem('username')
        js.window.location.href = '/'


    def applyGlobalStyles(self):
        # Apply global responsive styles
        style = document.createElement('style')
        style.innerHTML = """
            @media screen and (max-width: 768px) {
                .nav-div, .trailblazer, .sign-in {
                    padding: 0 10px;
                    height: 8vh;
                    font-size: 3vh; /* Adjust nav items for smaller screens */
                }

                .content_container, .topic, .place_input, .date_input_from, .date_input_to, .button {
                    width: 90%;
                    font-size: 5vw; /* Use viewport width for dynamic scaling on smaller screens */
                }

                .button{
                    padding: 12px 15px;
                    font-size: 5vw;
                }
                .topic, .place, .people {
                    font-size: max(1.5vh, min(2vw, 3vh));
                }
            
                .place-input, .date-input, .button, .ppl-button, .map-button, .add-button, .remove-button {
                    font-size: max(1.5vh, min(2vw, 3vh));
                    padding: max(1vh, min(1.5vw, 2vh));
                }
            }

            @media screen and (max-width: 480px) {
                .content_container, .topic, .place_input, .date_input_from, .date_input_to, .button{
                    font-size: 6vw; /* Increase font size for better readability */
                }
            }
        """
        document.head.appendChild(style)


    def setResponsiveStyle(self, element, style_dict):
        for key, value in style_dict.items():
            setattr(element.style, key, value)

        style = document.createElement('style')
        style.innerHTML = """
            @media screen and (max-width: 768px) {
                .content_container, .topic, .place_input, .date_input_from, .date_input_to {
                    width: 90vw;
                    margin-top: 5vh;
                    font-size: 4vw; /* Adjust font size for smaller screens */
                }

                /* Adjust button sizes and padding for easier touch */
                .button {
                    padding: 15px 20px;
                }
            }
        """
        document.head.appendChild(style)
    

if __name__ == "__main__":
    start_page = Menu("container")
    start_page.drawNavbar()
    start_page.drawContent()

    start_page.drawPeoplenumber()
    start_page.drawPlantrail()