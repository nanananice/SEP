from js import window, document
import js
from pyodide.http import pyfetch
import json
class RegisForm:
    def __init__(self, container_id):
        self.container = document.getElementById(container_id)
        self.create_form()
        self.add_event_listeners()

    def create_form(self):
        self.container.style.display = "flex"
        self.container.style.justifyContent = "center"
        self.container.style.alignItems = "center"
        self.container.style.height = "100vh"
        self.container.style.margin = "0"

        self.form_container = document.createElement('div')
        self.form_container.style.width = "300px"
        self.form_container.style.padding = "20px"
        self.form_container.style.borderRadius = "20px"
        self.form_container.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.5)"
        self.form_container.style.display = "flex"
        self.form_container.style.flexDirection = "column"
        self.form_container.style.alignItems = "center"
        self.form_container.style.justifyContent = "center"
        self.container.appendChild(self.form_container)

        img = document.createElement("img")
        img.src = "/static/pic/Trailblazer_logo.png"
        img.style.height = "10vh"
        self.form_container.appendChild(img)

        self.text = document.createElement('label')
        self.text.style.fontFamily = "Rubik, sans-serif"
        self.text.style.fontSize = "24px"
        self.text.style.fontWeight = "bold"
        self.text.textContent = 'Register for your Account'
        self.text.style.marginBottom = "5vh"
        self.form_container.appendChild(self.text)

        self.username_label = document.createElement('label')
        self.username_label.style.fontFamily = "Rubik, sans-serif"
        self.username_label.style.fontSize = "18px"
        self.username_label.style.fontWeight = "bold"
        self.username_label.setAttribute('for', 'username')
        self.username_label.textContent = 'Username:'
        self.form_container.appendChild(self.username_label)

        self.username_input = document.createElement('input')
        self.username_input.style.fontFamily = "Rubik, sans-serif"
        self.username_input.style.fontSize = "14px"
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

        self.confirm_password_label = document.createElement('label')
        self.confirm_password_label.setAttribute('for', 'conrifm_password')
        self.confirm_password_label.textContent = 'confirm Password:'
        self.form_container.appendChild(self.confirm_password_label)


        self.confirm_password_input = document.createElement('input')
        self.confirm_password_input.type = 'password'
        self.confirm_password_input.id = 'confirm_password'
        self.confirm_password_input.name = 'confirm_password'
        self.form_container.appendChild(self.confirm_password_input)

        self.submit_input = document.createElement('input')
        self.submit_input.type = 'submit'
        self.submit_input.value = 'register'
        self.submit_input.onclick = self.on_submit
        self.form_container.appendChild(self.submit_input)

        self.login_text = document.createElement('label')
        self.login_text.textContent = "Already has Account? Login"
        self.login_text.onclick = self.on_login_click
        self.form_container.appendChild(self.login_text)

    

    def add_event_listeners(self):

        self.submit_input.addEventListener('mouseover', self.on_mouse_over)
        self.submit_input.addEventListener('mouseleave', self.on_mouse_leave)


    async def on_submit(self, event):
        event.preventDefault()
        data = {"username":self.username_input.value, "password":self.password_input.value}
        response = await pyfetch(url="http://127.0.0.1:8000/register",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps(data))
        if response.status == 200:
            window.location.href = "/login"

    def on_mouse_over(self, event):
        event.target.style.backgroundColor = '#0056b3'

    def on_mouse_leave(self, event):
        event.target.style.backgroundColor = '#007bff'

    def on_login_click(self, event):

        js.document.location.href = '/login'

RegisForm('register-form-container')