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
        title_div.innerText = "Reviews"
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
        button_div.innerText = "add review"

        button_div.onclick = self.new_review
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
        review_place = js.window.localStorage.getItem("review_place")
        print(review_place)
        response = await pyfetch(url="http://127.0.0.1:8000/get_review",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps({"place": review_place}))
        
        data = await response.json() 
        if "place" in data:
            place = data["place"]
        
        image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA8cTn1-RRcQ_T4-cf40vYi4sjFEADIdog1TqwvXO3kw&s"

      

        for review in place:
            photo_container = document.createElement("div")
            photo_container.setAttribute("style", """
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px;
            """)

            img = document.createElement("img")
            img.setAttribute("src", image_url)
            img.style.width = "300px"
            img.style.height = "200px"  
            img.style.marginBottom = "5px"

            review_context = document.createElement("div")
            review_context.innerText = review[0]["review"]
            review_context.setAttribute("style", "margin-top: 5px;")

            review_user = document.createElement("div")
            review_user.innerText = "By:" + review[1]["User"]
            review_user.setAttribute("style", "margin-top: 5px;")

            photo_container.appendChild(img)
            photo_container.appendChild(review_context)
            photo_container.appendChild(review_user)

            container.appendChild(photo_container)


        red_div.appendChild(container)
        content_div.appendChild(blue_div)
        content_div.appendChild(red_div)

        self.element.appendChild(content_div)

    def new_trip(self,event):
        js.window.location.href = '/'

    async def new_review(self,event):

    
    
        modal = document.getElementById("reviewModal")
        if not modal:
        # Create modal div
            modal = document.createElement("div")
            modal.id = "reviewModal"
            modal.style.display = "none"  # Initially hidden
            modal.style.position = "fixed"
            modal.style.left = "0"
            modal.style.top = "0"
            modal.style.width = "100%"
            modal.style.height = "100%"
            modal.style.zIndex = "1000"
            modal.style.backgroundColor = "rgba(0,0,0,0.4)"  # Semi-transparent background

            # Create the content container inside the modal
            modalContent = document.createElement("div")
            modalContent.style.position = "absolute"
            modalContent.style.top = "50%"
            modalContent.style.left = "50%"
            modalContent.style.transform = "translate(-50%, -50%)"
            modalContent.style.padding = "20px"
            modalContent.style.backgroundColor = "#fff"
            modalContent.style.borderRadius = "5px"
            modalContent.style.display = "flex"
            modalContent.style.flexDirection = "column"
            modalContent.style.alignItems = "center"

            # Create input field
            review_input = document.createElement("input")
            review_input.type = "text"
            review_input.placeholder = "Type your review here..."
            review_input.style.margin = "10px"
            review_input.style.padding = "5px"
            review_input.style.width = "80%"

            # Create submit button
            submit_button = document.createElement("button")
            submit_button.innerText = "Submit Review"
            submit_button.onclick = lambda event: self.submit_review(event, review_input, modal)
            submit_button.style.padding = "10px 20px"
            submit_button.style.backgroundColor = "#007bff"
            submit_button.style.color = "white"
            submit_button.style.border = "none"
            submit_button.style.borderRadius = "5px"
            submit_button.style.cursor = "pointer"
            submit_button.style.margin = "5px"

            confirm_button = document.createElement("button")
            confirm_button.innerText = "confirm Review"
            confirm_button.onclick = self.confirm
            confirm_button.style.padding = "10px 20px"
            confirm_button.style.backgroundColor = "#007bff"
            confirm_button.style.color = "white"
            confirm_button.style.border = "none"
            confirm_button.style.borderRadius = "5px"
            confirm_button.style.cursor = "pointer"
            confirm_button.style.margin = "5px"
            

            
            modalContent.appendChild(review_input)
            modalContent.appendChild(submit_button)
            modalContent.appendChild(confirm_button)
            

            
            modal.appendChild(modalContent)

            
            document.body.appendChild(modal)

    
        modal.style.display = "block"

    def submit_review(self, event, review_input, modal):
      
        review_value = review_input.value

        existing_review = js.window.localStorage.getItem("review")
       
        if existing_review is not None:

            js.window.localStorage.removeItem("review")

        js.window.localStorage.setItem("review", review_value)

        

        
        

    async def confirm(self,event):
        review_value = js.window.localStorage.getItem("review")
        name = js.window.localStorage.getItem("user")
        review_place = js.window.localStorage.getItem("review_place")
        print(review_value)
        respone = await pyfetch(url="http://127.0.0.1:8000/add_review",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps({"review":review_value,"name":name,"place":review_place}))
    

        
        js.window.location.href = "/review"

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
