import js
from pyscript import document
from abc import ABC, abstractmethod
from pyodide.http import pyfetch
import json
from js import window, document
import datetime

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
    
class Profile(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id) 

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
        


        img.onclick = self.go_index
        self.trailblazer.onclick = self.go_index
        
        self.nav_div.appendChild(img)
        self.nav_div.appendChild(self.trailblazer)
   
        self.sign_out = document.createElement("div")
        self.sign_out.innerText = "Sign out"
        self.sign_out.style.fontFamily = "Rubik, sans-serif"
        self.sign_out.style.fontSize = "1.5vh"
        self.sign_out.style.padding = "1vh 2vh"
        self.sign_out.style.borderRadius = "20px"
        self.sign_out.style.backgroundColor = "black"
        self.sign_out.style.color = "white"
        self.sign_out.style.cursor = "pointer"
        self.sign_out.style.marginLeft = "auto"
        self.sign_out.onclick = self.log_out
        self.nav_div.appendChild(self.sign_out)
        self.nav_div.onclick = self.drawcontent
        
                    
      
        #self.nav_div.appendchild(self.go_in)
        
        self.element.appendChild(self.nav_div)

    async def drawcontent(self,event):
        content_div = document.createElement("div")

    # Set the style for the content div with inline CSS
        content_div.setAttribute("style", """
        height: 100vh; /* 100% of the viewport height */
        width: 50%; /* 50% of its parent's width */
        position: absolute; /* Use absolute positioning */
        left: 50%; /* Positioned halfway across its parent */
        transform: translateX(-50%); /* This centers the div horizontally */
       /* Example background color */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start; /* Align children to the start of the flex container */
        padding-top: 20px; /* Add some space from the top */
       Adding a black border to create a visible frame */
    """)

   
        blue_div = document.createElement("div")

        blue_div.setAttribute("style", """
        width: 100%; /* Full width */
        height: 20%; /* 20% of the viewport height */
     
        display: flex; /* Use flex to align children */
        justify-content: space-between; /* Space out title and button */
        align-items: center; /* Align items vertically */
        padding: 200px 0 0 0; /* Increased padding on the top */
        """)

    
   

    
        red_div = document.createElement("div")
        red_div.setAttribute("style", """
    width: 100%; /* Full width */
    height: 80%; /* Remaining height */
    
    display: flex;
    flex-wrap: wrap; /* Allow items to wrap to the next line */
    justify-content: space-around; /* Distribute space around items */
    align-items: flex-start; /* Align items to the start */
    padding: 10px; /* Add padding inside the red div */
    """)


        title_div = document.createElement("div")
        title_div.innerText = "Your Trips"
        title_div.setAttribute("style", """
        font-family: Rubik, sans-serif;
        font-size: 24px;
        flex-grow: 1; /* Allows the title to grow */
                               
        margin-right: 10px; /* Provides a margin to the right of the title */
/* Visible border for debugging */""")
    

        button_div = document.createElement("div")
        button_div.setAttribute("style", """
        font-family: Rubik, sans-serif;
        font-size: 16px;
        padding: 10px 15px;
        border-radius: 20px;
        background-color: #28a745;
        color: white;
        cursor: pointer;
        flex-grow: 0; /* Prevent the button from growing */
        /* Visible border for debugging */
        """)
        button_div.innerText = "+ New trip"

        button_div.onclick = self.new_trip
        blue_div.appendChild(title_div)
        blue_div.appendChild(button_div)


      

        container = document.createElement("div")  
        container.style.padding = "0 10px"   
        container.setAttribute("style", """
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center the items */
                               gap: 20px; /*
        padding: 0 31px; /* Horizontal padding */
        """)
        username = js.window.localStorage.getItem("user")
        response = await pyfetch(url="http://127.0.0.1:8000/get_user_profile",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps({"name": username}))
        
        data = await response.json() 
        if "trips" in data:
            data_list = data['trips']
            
            count = 0
        
        for trips in data_list:
            trip = json.loads(trips)
            
            count += 1
            
            start_date_str = trip[0]["trip_day"]
            end_date_str = trip[-1]["trip_day"]

            
            year = "2024"
            start_date = datetime.datetime.strptime(f"{start_date_str} {year}", "%A, %d %B %Y")
            end_date = datetime.datetime.strptime(f"{end_date_str} {year}", "%A, %d %B %Y")
            

            duration_days = (end_date - start_date).days + 1  
            
            
            country_name = trip[0]["trip_infos"][0]["info"].split(",")[-1].strip().split(" ")[-1]


            image_url = trip[0]["trip_infos"][0]["image"]

            photo_container = document.createElement("div")
            photo_container.setAttribute("style", """
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px;
            """)
            
            photo_container.setAttribute('id', count)
            photo_container.onclick = self.go_trip
            img = document.createElement("img")
            img.setAttribute("src", image_url)
            img.style.width = "300px"
            img.style.height = "200px"  
            img.style.marginBottom = "5px"


            city_name = document.createElement("div")
            city_name.innerText = country_name
            city_name.setAttribute("style", "margin-top: 5px;")

            
            start_date = document.createElement("div")
            start_date.innerText = start_date_str
            start_date.setAttribute("style", "margin-top: 5px;")

    
            duration = document.createElement("div")
            duration.innerText = duration_days
            duration.setAttribute("style", "margin-top: 5px;")

            photo_container.appendChild(img)
            photo_container.appendChild(city_name)
            photo_container.appendChild(start_date)
            photo_container.appendChild(duration)

  
            container.appendChild(photo_container)

        red_div.appendChild(container)
        content_div.appendChild(blue_div)
        content_div.appendChild(red_div)

        self.element.appendChild(content_div)

    def new_trip(self,event):
        js.window.location.href = '/'

    async def go_trip(self,event):
        username = js.window.localStorage.getItem("user")
        button = event.target.closest('div')
        trip_id = int(button.getAttribute('id'))
        response = await pyfetch(url="http://127.0.0.1:8000/get_user_profile",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps({"name": username}))
        
        data = await response.json() 
        if "trips" in data:
            data_list = data['trips']
        
        
       
        js.window.localStorage.removeItem("Trip_detail")
        js.window.localStorage.setItem("Trip_detail", data_list[trip_id-1]) 
        js.window.location.href = '/map'
        
       
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

    def log_out(self,event):
        js.window.localStorage.removeItem('access_token')
        js.window.localStorage.removeItem('username')
        js.window.localStorage.removeItem('userobject')
        
        js.window.location.href = '/'

    def go_index(self,event):
        js.window.location.href = '/'

if __name__ == "__main__":
    start_page = Profile("container")
    start_page.drawNavbar()
