import js
from pyscript import document
from abc import ABC, abstractmethod
from datetime import datetime
import json
from pyodide.http import pyfetch

userWidth = js.window.innerWidth
userHeight = js.window.innerHeight

api_key = 'AIzaSyCgqyG_lZyJ28gnl-5EKzQDUwF4gKeMFDQ'

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
class Trip(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)

    def defineElement(self):
        self.element.style.width = "100%"
        self.element.style.height = f"{userHeight}px"
        self.element.style.overflow = "hidden"
        self.element.style.margin = "0"
        self.element.style.padding = "0"
        self.element.style.display = "flex"
        self.element.style.boxSizing = "border-box"
        
    def get_query_params(self):
        query_params = js.window.location.search
        # parse the query params to dictionary
        # remove the '?' from the query params
        query_params = query_params[1:]
        query_params = dict([param.split('=') for param in query_params[1:].split('&')])
        #print(query_params)
        return query_params
    
    def add_custom_css(self):
        css_content = """
            /* Hide scrollbar for Chrome, Safari and Opera */
            .trip-div::-webkit-scrollbar {
                display: none; /* for Chrome, Safari, and Opera */
            }

            /* Hide scrollbar for IE, Edge, and Firefox */
            .trip-div {
                -ms-overflow-style: none;  /* IE and Edge */
                scrollbar-width: none;  /* Firefox */
            }

            /* Add your custom CSS here if needed */
        """
        style_element = document.createElement("style")
        style_element.innerHTML = css_content
        document.head.appendChild(style_element)

    async def add_this_place(self, event):

        button = event.target.closest('button')
        trip_id = int(button.getAttribute('data-trip-id'))
        element = f"inputPlace{trip_id}"
        input_element = document.getElementById(element)
        place_name = input_element.value
        data = {"place":place_name}
        response = await pyfetch(url="http://127.0.0.1:8000/search_location",
                            method = "POST",
                            headers = {"Content-Type": "application/json"},
                            body=json.dumps(data))
        if response.status == 200:
            location_data = await response.json() 
            if "Location_detail" in location_data:
                location = location_data["Location_detail"]
                print(location)
            data_str = js.window.localStorage.getItem("Trip_detail")
            trip_data = json.loads(data_str) if data_str else []
            if 0 <= trip_id < len(trip_data):
                trip_data[trip_id]["trip_infos"].append(location)
                
                updated_data_str = json.dumps(trip_data)
                js.window.localStorage.setItem("Trip_detail", updated_data_str)
                js.window.location.reload()
            else:
                print("Invalid trip_id")
        else:
            print(f"Failed to fetch location details, status code: {response.status}")

    def remove_place(self, event):
        data_str = js.window.localStorage.getItem("Trip_detail")
        data = json.loads(data_str) if data_str else []
        button = event.target.closest('button')
        trip_id = int(button.getAttribute('data-trip-id'))
        place_id = int(button.getAttribute('data-place-id'))
        if trip_id < len(data):

            if place_id < len(data[trip_id]['trip_infos']):
                del data[trip_id]['trip_infos'][place_id]
            else:
                print("Place ID out of bounds for the specified trip.")
        else:
            print("Trip ID out of bounds for the data provided.")
        print(data)
        js.window.localStorage.removeItem('Trip_detail')
        data_str = json.dumps(data)
        js.window.localStorage.setItem('Trip_detail', data_str)
        js.window.location.reload()

    def trip_on_left(self,details: list[dict[str:str]]):
        #print(details)
        self.tripdiv = document.createElement("div")
        self.tripdiv.className = "trip-div"
        self.tripdiv.style.flex = "1"
        self.tripdiv.style.overflowY = "auto"
        self.tripdiv.style.maxHeight = f"{userHeight}px"
        self.tripdiv.style.overflowX = "hidden"

        self.place_pic = document.createElement("div")
        self.place_pic.style.width = "100%"
        self.place_pic.style.height = "300px"
        banner = details[0]
        img = document.createElement("img")
        img.setAttribute("src", banner['city_image'])
        img.style.width = "100%"
        img.style.height = "100%"
        img.style.objectFit = "contain"
        img.style.borderRadius = "10px"
        self.tripdiv.appendChild(self.place_pic)
        self.place_pic.appendChild(img)

        self.pic_text = document.createElement("div")

        self.word_div = document.createElement("div")
        self.word_div.style.position = "absolute"
        self.word_div.style.top = "0"
        self.word_div.style.left = "0"
        self.word_div.style.padding = "10px"


        self.place_text = document.createElement("div")
        address = details[0]['trip_infos'][0]['info']
        words = address.split()
        last_word = words[-1]
        self.place_text.innerText = last_word
        self.place_text.style.color = "#4e4e4e"
        self.place_text.style.backgroundColor = "#e7e7e7"
        self.place_text.style.border = "1px solid #4e4e4e"
        self.place_text.style.padding = "0 5px 0 5px"
        self.place_text.style.borderRadius = "15px"
        self.place_text.style.display = "inline"
        self.place_text.style.fontSize = "34px"
        self.place_text.style.fontWeight = "bold"
        self.place_text.style.fontFamily = "Rubik, sans-serif"

        self.date_text = document.createElement("div")

        date_obj1 = datetime.strptime(details[0]['trip_day'], "%A, %d %B")
        formatted_date1 = date_obj1.strftime("%d %b")

        self.date_text.innerText = formatted_date1
        if len(details) > 1:
            date_obj2 = datetime.strptime(details[-1]['trip_day'], "%A, %d %B")
            formatted_date2 = date_obj2.strftime("%d %b")
            self.date_text.innerText += " ➞ " + formatted_date2

        self.date_text.style.color = "#4e4e4e"
        self.date_text.style.backgroundColor = "#e7e7e7"
        self.date_text.style.border = "1px solid #4e4e4e"
        self.date_text.style.padding = "0 5px 2px 5px"
        self.date_text.style.borderRadius = "15px"
        self.date_text.style.marginTop = "10px"
        self.date_text.style.fontSize = "24px"
        self.date_text.style.fontWeight = "bold"
        self.date_text.style.fontFamily = "Rubik, sans-serif"

        self.word_div.appendChild(self.place_text)
        self.word_div.appendChild(self.date_text)
        self.pic_text.appendChild(self.word_div)

        self.place_pic.appendChild(self.pic_text)

        self.all_trip = document.createElement("div")
        for index, detail in enumerate(details):
            self.each_date_trip(detail['trip_day'], self.all_trip, detail['trip_infos'], index)
        self.tripdiv.appendChild(self.all_trip)

        self.save_place = document.createElement("button")
        self.save_place.innerText = "Save the Trip"
        self.save_place.style.borderRadius = "10px"
        self.save_place.style.padding = "10px"
        self.save_place.style.margin = "auto auto 40px auto"
        self.save_place.style.display = "flex"
        self.save_place.style.color = "white"
        self.save_place.style.backgroundColor = "#ff7065"
        self.save_place.style.border = "1px solid #ff7065"
        self.save_place.style.cursor = "pointer"
        self.save_place.onclick = self.do_save

        style = document.createElement('style')
        style.innerHTML = """
        .save-place:hover {
            background-color: #28a745 !important;
            border: 1px solid #28a745 !important;
        }
        """
        document.head.appendChild(style)

        self.save_place.className = 'save-place'
        self.save_place.style.transition = 'background-color 0.3s ease'
        #self.button_add.onclick = add more place

        self.all_trip.appendChild(self.save_place)

        self.element.appendChild(self.tripdiv)

    async def do_save(self,event):
        existing_trip = js.window.localStorage.getItem("Trip_detail")
        existing_user = js.window.localStorage.getItem("user")
 
        await pyfetch(url="http://127.0.0.1:8000/insert_trip",
                                    method = "POST",
                                    headers = {"Content-Type": "application/json"},
                                    body=json.dumps({"user": existing_user,"trip":existing_trip}))

    def each_date_trip(self, day, parent,trip_info: list[dict[str:str]], id):     
        self.thisday = document.createElement("div")
        self.thisday.style.width = "75%"
        self.thisday.style.margin = "25px auto"
        self.thisday.style.border = "none"
        self.thisday.style.display = "flex"
        self.thisday.style.flexDirection = "column"
        self.thisday.style.alignItems = "flex-start"
        self.thisday.style.padding = "10px"
        self.thisday.style.backgroundColor = "#f7f7f7"
        self.thisday.style.borderRadius = "15px"
        self.thisday.style.boxShadow = "1px 1px 5px 2px rgba(0,0,0,0.5)"
        self.thisday.setAttribute("class", "date-trip")
        self.thisday.setAttribute("data-day", day)
        self.thisday.onclick = self.toggle_info 

        self.textinside = document.createElement("div")      

        self.headtext = document.createElement("div")
        self.headtext.style.border = "none"
        self.headtext.style.margin = "40px 5px"
        self.headtext.style.fontFamily = "Rubik, sans-serif"
        self.headtext.style.fontSize = "24px"
        self.headtext.innerText = f"> {day}"

        self.thisday_info = document.createElement("div")
        self.thisday_info.setAttribute("class", "thisday_info")
        self.thisday_info.style.display = 'none'
        self.thisday_info.style.width = "100%"
        self.thisday_info.style.marginTop = "30px"


        # self.each_thisday_info("1", self.thisday_info)
        # self.each_thisday_info("2", self.thisday_info)
        for index, trip in enumerate(trip_info):
            self.each_thisday_info(trip['info'], trip['image'], self.thisday_info, id, index)

        
        self.add_place = document.createElement("button")
        self.add_place.innerText = "Add This"
        self.add_place.style.borderRadius = "10px"
        self.add_place.style.padding = "10px"
        self.add_place.style.margin = "10px"
        self.add_place.style.color = "white"
        self.add_place.style.backgroundColor = "#ff7065"
        self.add_place.style.border = "1px solid #ff7065"
        self.add_place.style.cursor = "pointer"
        style = document.createElement('style')
        style.innerHTML = """
        .button-add:hover {
            background-color: #28a745 !important;
            border: 1px solid #28a745 !important;
        }
        """
        document.head.appendChild(style)

        self.add_place.className = 'button-add'
        self.add_place.style.transition = 'background-color 0.3s ease'
        self.add_place.setAttribute('data-trip-id', int(id))
        self.add_place.onclick = self.add_this_place


        self.input_place = document.createElement("input")
        self.input_place.id = f"inputPlace{id}"
        self.input_place.style.width = "60%"
        self.input_place.style.borderRadius = "5px"
        self.input_place.style.padding = "10px"
        self.input_place.style.marginTop = "10px"
        self.input_place.style.border = "1px solid #ddd"
        self.thisday_info.appendChild(self.input_place)

        self.thisday_info.appendChild(self.add_place)

        self.textinside.appendChild(self.headtext)
        self.thisday.appendChild(self.textinside)
        self.thisday.appendChild(self.thisday_info)
        parent.appendChild(self.thisday)
    



    def each_thisday_info(self, place_text, place_image, parent, trip_index, place_id):
        fixed_height = "100px"

        self.thisplace_all = document.createElement("div")
        self.thisplace_all.style.display = "flex"
        self.thisplace_all.style.alignItems = "flex-start"
        self.thisplace_all.style.justifyContent = "space-between" 
        self.thisplace_all.style.marginBottom = "10px"
        self.thisplace_all.style.maxWidth = "100%"

        self.thisplace_pic = document.createElement("div")
        self.thisplace_pic.style.margin = "10px"
        self.thisplace_pic.style.flex = "0 0 auto"
        self.thisplace_pic.style.width = "150px"
        self.thisplace_pic.style.height = fixed_height

        img = document.createElement("img")
        img.setAttribute("src", place_image)
        img.style.width = "100%"
        img.style.height = "100%"
        img.style.objectFit = "cover"
        img.style.borderRadius = "10px"
        self.thisplace_pic.appendChild(img)

        self.place_info = document.createElement("div")
        self.place_info.style.margin = "auto"
        self.place_info.style.flex = "1"
        self.place_info.style.minHeight = "50px"
        self.place_info.style.overflowY = "auto"
        self.place_info.style.padding = "10px"
        self.place_info.style.fontFamily = "Rubik, sans-serif"
        self.place_info.style.fontSize = "14px"
        self.place_info.innerText = place_text

        img = document.createElement("img")
        img.src = "/static/pic/bin_logo.png"
        img.style.maxWidth = "100%"
        img.style.maxHeight = "100%"
        
        self.remove_button = document.createElement("button")
        if place_id != 0:
            
            self.remove_button.style.cursor = "pointer"
            self.remove_button.style.border = "1px solid #ddd"
            self.remove_button.style.borderRadius = "15px"
            self.remove_button.appendChild(img)
            self.remove_button.style.width = "30px"
            self.remove_button.style.height = "30px"
            self.remove_button.style.margin = "auto 10px auto 10px"
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
            self.remove_span.style.fontSize = "10px"
            
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

            self.remove_button.setAttribute('data-place-id', int(place_id))
            self.remove_button.setAttribute('data-trip-id', int(trip_index))

            self.remove_span.className = 'span'
            self.remove_button.appendChild(self.remove_span)
            self.remove_button.onclick = self.remove_place

        self.thisplace_all.appendChild(self.thisplace_pic)
        self.thisplace_all.appendChild(self.place_info)
        self.thisplace_all.appendChild(self.remove_button)
        parent.appendChild(self.thisplace_all)


    def toggle_info(self, event):

        if event.target.tagName.lower() == 'button' or event.target.tagName.lower() == 'input':
            return

        info_div = event.target.closest('.date-trip').querySelector('.thisday_info')

        if info_div.style.display == 'none':
            info_div.style.display = 'block'
        else:
            info_div.style.display = 'none'


    def map_on_right(self):
        self.mapdiv = document.createElement("div")
        self.mapdiv.setAttribute("id", "googleMap")
        self.mapdiv.style.flex = "1"
        self.mapdiv.style.overflowY = "hidden"
        self.mapdiv.style.height = f"{userHeight}px"
        self.element.appendChild(self.mapdiv)


        js_code = """
        var map; 
        var data = window.localStorage.getItem("Trip_detail")
        const travelPlan = JSON.parse(data);
        function initMap() {
            var styles = [
                {
                    featureType: "poi",
                    stylers: [{ visibility: "off" }] 
                },
                {
                    featureType: "transit",
                    elementType: "labels",
                    stylers: [{ visibility: "off" }] 
                }
            ];
            var firstHotel = travelPlan[0].trip_infos[0];
            var centerLat = firstHotel.lat;
            var centerLng = firstHotel.lng

            map = new google.maps.Map(document.getElementById('googleMap'), {
                center: new google.maps.LatLng(centerLat, centerLng),
                zoom: 10,
                styles: styles
            });      
            addMarkers(travelPlan);   
        }

function addMarkers(travelPlan) {
    if (Array.isArray(travelPlan)) {
        travelPlan.forEach((day, dayIndex) => {
            day.trip_infos.forEach((info, index) => {
                var markerIcon = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png';
                if (index === 0) {
                    markerIcon = 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png';
                }
                var placeName = info.info.split(' - ')[0];
                const marker = new google.maps.Marker({
                    position: {lat: info.lat, lng: info.lng},
                    map: map,
                    icon: markerIcon,
                    title: info.info
                });

                const buttonId = `button-${dayIndex}-${index}`; // Unique ID for each button
                
                const infowindowContent = `<div>
                                              <h3>${day.trip_day}</h3>
                                              <p>${info.info}</p>
                                              <p>${placeName}</p>
                                              <img src="${info.image}" style="width: 100%; max-width: 250px;" alt="Image">
                                              <button id="${buttonId}">See Reviews</button>
                                           </div>`;

                const infowindow = new google.maps.InfoWindow({
                    content: infowindowContent
                });

                marker.addListener('click', () => {
                    infowindow.open(map, marker);
                    infowindow.addListener('domready', () => {
                        document.getElementById(buttonId).addEventListener('click', () => redirectUser(placeName));
                    });
                });
            });
        });
    } else {
        console.error('travelPlan is not an array:', travelPlan);
    }
}

// Redirect function
function redirectUser(placeName) {
    
    if (localStorage.getItem("review_place") !== null) {
    
        localStorage.removeItem("review_place");
        localStorage.setItem("review_place", placeName);
    } else {
       
        localStorage.setItem("review_place", placeName);
    }
 
    window.location.href = `/review`;
}
        initMap();
        """
        js.eval(js_code)


if __name__ == "__main__":
    trip_page = Trip("container")
    trip_page.add_custom_css()
    trip_page.defineElement()
    existing_trip = js.window.localStorage.getItem("Trip_detail")
    if existing_trip is not None:
        #print(existing_trip)
        existing_trip = json.loads(existing_trip)
        trip_page.trip_on_left(existing_trip)
    
    trip_page.map_on_right()
