from js import window, document
import js
from pyodide.http import pyfetch
import json

class LoginForm:
    def __init__(self, container_id):
        self.container = document.getElementById(container_id)
        self.create_form()
        self.apply_styles()
        self.add_event_listeners()

    def create_form(self):
        self.form_container = document.createElement('div')
        self.form_container.className = 'login-container'
        self.container.appendChild(self.form_container)

        self.username_label = document.createElement('label')
        self.username_label.setAttribute('for', 'username')
        self.username_label.textContent = 'Username:'
        self.form_container.appendChild(self.username_label)

        self.username_input = document.createElement('input')
        self.username_input.type = 'text'
        self.username_input.id = 'username'
        self.username_input.name = 'username'
        self.form_container.appendChild(self.username_input)

        self.password_label = document.createElement('label')
        self.password_label.setAttribute('for', 'password')
        self.password_label.textContent = 'Password:'
        self.form_container.appendChild(self.password_label)

        self.password_input = document.createElement('input')
        self.password_input.type = 'password'
        self.password_input.id = 'password'
        self.password_input.name = 'password'
        self.form_container.appendChild(self.password_input)

        self.submit_input = document.createElement('input')
        self.submit_input.type = 'submit'
        self.submit_input.value = 'Login'
        self.submit_input.onclick = self.on_submit
        self.form_container.appendChild(self.submit_input)

        self.registext = document.createElement('label')
        self.registext.textContent = "No Account? register now"
     
        self.form_container.appendChild(self.registext)

    def apply_styles(self):
        # Styles applied directly in HTML
        pass

    def add_event_listeners(self):

        self.submit_input.addEventListener('mouseover', self.on_mouse_over)
        self.submit_input.addEventListener('mouseleave', self.on_mouse_leave)
        self.registext.onclick = self.on_register_click
        

    async def on_submit(self, event):
            event.preventDefault()

            data = {"username":self.username_input.value, "password":self.password_input.value}
            
            response = await pyfetch(url="http://127.0.0.1:8000/login",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps(data))
            if response.status == 200:
                data = await response.json()
                if "access_token" in data:
                    access_token = data["access_token"]
                    username = data["user"]
                    user = data["user_object"]
                    
                
                    js.window.localStorage.setItem("access_token", access_token)
                    js.window.localStorage.setItem("user", username)
                    js.window.localStorage.setItem("user_object", user)
                    
                    
                    js.window.location.href = "/"
                
                

                    
                    


    def on_mouse_over(self, event):
        event.target.style.backgroundColor = '#0056b3'

    def on_mouse_leave(self, event):
        event.target.style.backgroundColor = '#007bff'

    def on_register_click(self, event):
        
        js.window.location.href ='/register'

LoginForm('login-form-container')