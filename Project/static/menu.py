import js
from pyscript import document
from abc import ABC, abstractmethod

userWidth = js.window.innerWidth
userHeight = js.window.innerHeight

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None
        self.content_container = document.createElement("div")

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
class Menu(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.destinations = {}
        self.destination_counter = 0

    def drawContent(self):
        self.content_container.style.width = str(userWidth/2.5) + "px"
        self.content_container.style.margin = "0 auto"
        self.content_container.style.marginTop = str(userHeight/10) + "px"
        self.content_container.style.border = "1px solid #000"
        self.content_container.style.padding = "20px"
        self.content_container.style.boxSizing = "border-box"

        self.each_place = document.createElement("div")

        self.place = document.createElement("div")
        self.place.style.marginTop = "30px"
        self.place.style.fontFamily = "Rubik, sans-serif"
        self.place.style.fontSize = "18px"
        self.place.innerText = "Where do you want to go?"

        self.place_input = document.createElement("input")
        self.place_input.style.width = "60%"
        self.place_input.style.borderRadius = "5px"
        self.place_input.style.padding = "10px"
        self.place_input.style.marginTop = "10px"
        self.place_input.style.border = "1px solid #ddd"

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
        self.date_input_to.style.borderRadius = "5px"
        self.date_input_to.style.padding = "10px"
        self.date_input_to.style.border = "1px solid #ddd"
        self.date_to_container.appendChild(self.date_input_to)

        self.date_container.appendChild(self.date_from_container)
        self.date_container.appendChild(self.date_to_container)

        self.button_add = document.createElement("button")
        self.button_add.innerText = "+ Add Destination"
        self.button_add.style.width = "20%"
        self.button_add.style.borderRadius = "5px"
        self.button_add.style.padding = "10px"
        self.button_add.style.marginTop = "5px"
        self.button_add.style.color = "white"
        self.button_add.style.backgroundColor = "#ff7065"
        self.button_add.style.border = "1px solid #ff4032"
        self.button_add.style.cursor = "pointer"

        self.plan_the_trail = document.createElement("div")
        self.plan_the_trail.style.textAlign = "center"
        self.plan_the_trail.style.padding = "10px"
        self.plan_the_trail.style.marginTop = "30px"
        self.plan_the_trail.style.fontFamily = "Rubik, sans-serif"
        self.plan_the_trail.style.fontSize = "32px"
        self.plan_the_trail.style.fontWeight = "bold"
        self.plan_the_trail.style.color = "white"
        self.plan_the_trail.style.backgroundColor = "black"
        self.plan_the_trail.innerText = "Plan The Trail"
        self.content_container.appendChild(self.plan_the_trail)

        self.content_container.appendChild(self.place)
        self.each_place.appendChild(self.place_input)
        self.each_place.appendChild(self.date_container)
        self.content_container.appendChild(self.each_place)
        self.button_add.onclick = self.addPlace
        self.content_container.appendChild(self.button_add)
        
        self.element.appendChild(self.content_container)

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
        img.src = "pic/bin_logo.png"
        img.style.width = "100%"

        next_label = document.createElement("div")
        next_label.style.paddingTop = "10px"
        next_label.innerText = "Going next to"
        remove_button = document.createElement("button")
        remove_button.style.cursor = "pointer"
        remove_button.style.border = "1px solid #ddd"
        remove_button.style.borderRadius = "15px"
        remove_button.appendChild(img)
        remove_button.style.width = "30px"
        remove_button.style.height = "30px"
        remove_button.style.marginTop = "10px"
        remove_button.style.marginLeft = "20px"
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
        """
        document.head.appendChild(style)

        self.remove_button.className = 'remove-button'
        self.remove_button.style.transition = 'background-color 0.3s ease'

        self.remove_span.className = 'span'
        remove_button.appendChild(self.remove_span)

        horizontalContainer.appendChild(next_label)
        horizontalContainer.appendChild(remove_button)
        each_place.appendChild(horizontalContainer)

        place_input = document.createElement("input")
        place_input.style = self.place_input.style.cssText
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

        self.destination_counter += 1

        return each_place

    def addPlace(self, event):
        new_destination = self.createDestinationElement()
        self.destinations[new_destination.id] = new_destination
        self.content_container.insertBefore(new_destination, self.button_add)

    def removePlace(self, destination_id):
        destination_element_id = f"destination-{destination_id}"
        if destination_element_id in self.destinations:
            destination_element = self.destinations[destination_element_id]
            destination_element.remove()
            del self.destinations[destination_element_id]
        
    def drawGenre(self):
        self.genre_container = document.createElement("div")

        self.genre = document.createElement("div")
        self.genre.style.marginTop = "30px"
        self.genre.style.fontFamily = "Rubik, sans-serif"
        self.genre.style.fontSize = "18px"
        self.genre.innerText = "Select the kind of activities you want to do"

        self.genre_box = document.createElement("div")
        self.genre_box.style.marginTop = "10px"
        self.genre_box.style.border = "1px solid #000"
        self.genre_box.style.width = "100%"
        self.genre_box.style.display = "flex"
        self.genre_box.style.flexWrap = "wrap"

        self.createGenrebox(self.genre_box, "Temple")
        self.createGenrebox(self.genre_box, "Kid Friendly")
        self.createGenrebox(self.genre_box, "Shopping")
        self.createGenrebox(self.genre_box, "Art & Cultural")
        self.createGenrebox(self.genre_box, "Amusement Parks")
        self.createGenrebox(self.genre_box, "WOWOWOWOWOWOW")
        self.createGenrebox(self.genre_box, "WKKWKWKWKWKW")
        self.createGenrebox(self.genre_box, "HEHEHEHEHEHEEHEHE")

        self.genre_container.appendChild(self.genre)
        self.genre_container.appendChild(self.genre_box)
        self.content_container.appendChild(self.genre_container)

    def createGenrebox(self,div,genre_name):
        self.this_genre = document.createElement("button")
        self.this_genre.style.cursor = "pointer"
        self.this_genre.style.margin = "5px"
        self.this_genre.style.padding = "5px"
        self.this_genre.style.backgroundColor = "white"
        self.this_genre.style.border = "1px solid #ddd"
        self.this_genre.style.borderRadius = "10px"
        self.this_genre_label = document.createElement("div")
        self.this_genre_label.innerText = genre_name
        self.this_genre_label.style.marginLeft = "5px"
        self.this_genre_label.style.marginRight = "5px"
        self.this_genre_label.style.fontFamily = "Rubik, sans-serif"
        self.this_genre_label.style.color = "#ddd"
        self.this_genre_label.style.fontSize = "16px"
        self.this_genre.appendChild(self.this_genre_label)
        div.appendChild(self.this_genre)

    def drawPeoplenumber(self):
        self.people_container = document.createElement("div")

        self.people = document.createElement("div")
        self.people.style.marginTop = "30px"
        self.people.style.fontFamily = "Rubik, sans-serif"
        self.people.style.fontSize = "18px"
        self.people.innerText = "How many people are going?"

        self.people_box = document.createElement("div")
        self.people_box.style.fontFamily = "Rubik, sans-serif"
        self.people_box.style.border = "1px solid #ddd"
        self.people_box.style.color = "#ddd"
        self.people_box.style.fontSize = "16px"

        self.people_container.appendChild(self.people)
        self.people_container.appendChild(self.people_box)
        self.content_container.appendChild(self.people_container)  
    
    def drawNavbar(self):
        self.nav_div = document.createElement("div")
        self.nav_div.style.display = "flex"
        self.nav_div.style.alignItems = "center"
        self.nav_div.style.justifyContent = "space-between"
        self.nav_div.style.padding = "0 20px"
        self.nav_div.style.boxSizing = "border-box"
        self.nav_div.style.height = str(userHeight/10) + "px"
        self.nav_div.style.position = "fixed"
        self.nav_div.style.top = "0"
        self.nav_div.style.left = "0"
        self.nav_div.style.right = "0"
        self.nav_div.style.backgroundColor = "white"
        self.nav_div.style.borderBottom = "1px solid #e7e7e7"
        self.nav_div.style.zIndex = "1000"

        img = document.createElement("img")
        img.src = "pic/Trailblazer_logo.png"
        img.style.height = str(userHeight/12) + "px"
        img.style.marginRight = "10px"

        self.trailblazer = document.createElement("div")
        self.trailblazer.style.fontFamily = "Rubik"
        self.trailblazer.style.fontSize = "24px"
        self.trailblazer.innerText = "Trailblazer"

        self.sign_in = document.createElement("div")
        self.sign_in.innerText = "Sign In"
        self.sign_in.style.fontFamily = "Rubik, sans-serif"
        self.sign_in.style.fontSize = "16px"
        self.sign_in.style.padding = "10px 20px"
        self.sign_in.style.borderRadius = "20px"
        self.sign_in.style.backgroundColor = "black"
        self.sign_in.style.color = "white"
        self.sign_in.style.cursor = "pointer"
        self.sign_in.style.marginLeft = "auto"

        self.nav_div.appendChild(img)
        self.nav_div.appendChild(self.trailblazer)
        self.nav_div.appendChild(self.sign_in)
        
        self.element.appendChild(self.nav_div)

if __name__ == "__main__":
    start_page = Menu("container")
    start_page.drawNavbar()
    start_page.drawContent()
    start_page.drawGenre()
    start_page.drawPeoplenumber()
