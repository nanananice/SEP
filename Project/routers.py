from fastapi import APIRouter
from fastapi import FastAPI, Form, HTTPException, Depends,  status
from starlette.responses import RedirectResponse
from fastapi.responses import FileResponse, HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer
import transaction
from db import get_db, User, Place
from BTrees.OOBTree import BTree
import jwt
import datetime
import logging
from ZODB import FileStorage, DB
from persistent import Persistent
import googlemaps
from pathlib import Path
import js
import requests

logger = logging.getLogger("uvicorn")
SECRET_KEY = "YouStoleMyHeart"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
token_login = ""

router = APIRouter()

templates = Jinja2Templates(directory="templates")




gmaps = googlemaps.Client(key='AIzaSyCgqyG_lZyJ28gnl-5EKzQDUwF4gKeMFDQ')
api_key = 'AIzaSyCgqyG_lZyJ28gnl-5EKzQDUwF4gKeMFDQ'


class User_datas(BaseModel):
    username: str
    password: str

class FindPlace(BaseModel):
    citiCenter : str
    radius : int
    _type : str
    count : int

class Test(BaseModel):
    test : str

class User_trip(BaseModel):
    user : str
    trip : str

class User(BaseModel):
    name : str

class Location(BaseModel):
    place : str

class Review_data(BaseModel):
    place : str

class Review_User(BaseModel):
    review : str
    name : str
    place : str


def get_city_image_url(city_name, api_key):
    find_place_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={city_name}&inputtype=textquery&fields=photos&key={api_key}"
    response = requests.get(find_place_url)
    data = response.json()
    
    if 'candidates' in data and data['candidates']:
        first_candidate = data['candidates'][0]
        
        if 'photos' in first_candidate:
            photo_reference = first_candidate['photos'][0]['photo_reference']
            
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
            return photo_url
    
    return None 



def create_trip(data, gmaps, api_key):
    travel_plan = []

    num_destinations = sum(1 for key in data if key.startswith('place'))

    for i in range(num_destinations):
        location = data[f'place{i}']
        words = location.split()
        country = words[-1]
        date_from = data[f'dateFrom{i}']
        date_to = data[f'dateTo{i}']
        date_from_obj = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        date_to_obj = datetime.datetime.strptime(date_to, '%Y-%m-%d')
        num_days = (date_to_obj - date_from_obj).days + 1
        attractions_per_day = 3
        city_image_url = get_city_image_url(country, api_key)

        hotels_result = gmaps.places(query='hotels in ' + location)
        if hotels_result['results']:
            hotel = hotels_result['results'][0] 
            hotel_details = gmaps.place(place_id=hotel['place_id'], fields=['name', 'formatted_address', 'photo', 'geometry'])

            if 'photos' in hotel_details['result']:
                photo_reference = hotel_details['result']['photos'][0]['photo_reference']
                hotel_photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
            else:
                hotel_photo_url = "No image available"

            if 'geometry' in hotel_details['result']:
                lat = hotel_details['result']['geometry']['location']['lat']
                lng = hotel_details['result']['geometry']['location']['lng']
            else:
                lat, lng = None, None

            hotel_info = {
                "info": f"{hotel_details['result']['name']} - {hotel_details['result'].get('formatted_address', 'No address available')}",
                "image": hotel_photo_url,
                "lat": lat,
                "lng": lng
            }
            
        else:
            hotel_info = {
                "info": "No hotel found",
                "image": "No image available",
                "lat": "No lat available",
                "lng": "No lng available"
            }

        places_result = gmaps.places(query='tourist attractions in ' + location)

        for day in range(num_days):
            current_date = date_from_obj + datetime.timedelta(days=day)
            day_plan = {"trip_day": current_date.strftime('%A, %d %B'), "trip_infos": [hotel_info],"city_image": city_image_url} 
            
            for j in range(attractions_per_day):
                index = day * attractions_per_day + j
                if index < len(places_result['results']):
                    place = places_result['results'][index]
                    place_details = gmaps.place(place_id=place['place_id'], fields=['name', 'formatted_address', 'photo', 'geometry'])

                    if 'photos' in place_details['result']:
                        photo_reference = place_details['result']['photos'][0]['photo_reference']
                        photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
                    else:
                        photo_url = "No image available"

                    if 'geometry' in place_details['result']:
                        lat = place_details['result']['geometry']['location']['lat']
                        lng = place_details['result']['geometry']['location']['lng']
                    else:
                        lat, lng = None, None

                    info = {
                        "info": f"{place_details['result']['name']} - {place_details['result'].get('formatted_address', 'No address available')}",
                        "image": photo_url,
                        "lat": lat,
                        "lng": lng
                    }

                    day_plan["trip_infos"].append(info)
            travel_plan.append(day_plan)

    return travel_plan

def get_trip():
    return js.window.localStorage.getItem("Trip_detail")

def clear_storage():

    print("Clear success")




@router.post("/search_location")
async def search_trip(data: Location):
    gmaps = googlemaps.Client(key=api_key)
    location_result = gmaps.places(query=data.place)
    
    if location_result['results']:
        location = location_result['results'][0]
        location_details = gmaps.place(place_id=location['place_id'], fields=['name', 'formatted_address', 'photo', 'geometry'])
        
        # Initialize default values
        location_photo_url = "No image available"
        lat, lng = None, None
        
        # Check if photos are available and get the URL
        if 'photos' in location_details['result']:
            photo_reference = location_details['result']['photos'][0]['photo_reference']
            location_photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}"
        
        # Check if geometry details are available
        if 'geometry' in location_details['result']:
            lat = location_details['result']['geometry']['location']['lat']
            lng = location_details['result']['geometry']['location']['lng']
        
        # Compile the location info
        location_info = {
            "info": f"{location_details['result']['name']} - {location_details['result'].get('formatted_address', 'No address available')}",
            "image": location_photo_url,
            "lat": lat,
            "lng": lng
        }
        
        return {"Location_detail":location_info}
    else:
        return {"Location_detail":"No results found for the specified location."}

@router.post("/find_random_place")
async def find_random_place(data: Test,request: Request):
    data.test = dict([param.split('=') for param in data.test.split('&')])
    trip = create_trip(data.test,gmaps,api_key)
    #print(data.test)
    #print(trip)
    return {"Trip_detail":trip}

@router.post("/insert_trip")
async def insert_trip(data: User_trip):
    user_dict = get_user(data.user)
    trip_list = data.trip
    #print(user_dict.trips)
    user_dict.add_trip(trip_list)

    
    transaction.commit()

@router.post("/get_user_profile")
async def get_user_profile(data : User):

    username = data.name
    root = get_db()
    if 'users' not in root:
        raise HTTPException(status_code=404, detail="No users found")

    users = root['users']


    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user = users[username]
    trips = user.trips

    return {"trips": trips}



def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            return None 
        return username
    except jwt.PyJWTError:
        return None

def get_user(username):
    root = get_db()
    if 'users' not in root:
        raise HTTPException(status_code=404, detail="No users found")

    users = root['users']


    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user = users[username]
    print(user)
    return user



@router.get("/")
async def get_root(response_class=RedirectResponse,status_code=302):
    global token_login 
    token = token_login
    #print("token")
    if not token:
        print("a")
        return FileResponse('index.html')

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        if username is None:
            raise HTTPException(status_code=400, detail="Invalid token")
        logger.info(f"Username from token: {username}")
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=400, detail="Invalid token")
    print("b")
    return FileResponse('index.html')

def get_place(name):
    root = get_db()
    if 'places' not in root:
        root['places'] = BTree()
        transaction.commit()
    
    places = root['places']
    
    if name not in places:
        new_place = Place(name)
        places[name] = new_place
        transaction.commit()
        
    return places[name]

@router.post("/get_review")
async def get_review(data: Review_data):

    place_reference = get_place(data.place)
    print(place_reference.review)
    return {"place": place_reference.review}



@router.post("/add_review")
async def add_review(data: Review_User):
    place_reference = get_place(data.place)
    reviewlist = [ {"review": data.review},{"User":data.name}]
    place_reference.add_review(reviewlist)
    
    transaction.commit()
    print(place_reference.review)
    return {"message": "Review added successfully"}
   
    


#curently not use
@router.post("/")
async def post_root(data: Test,request: Request):
    data.test = data.test[1:]
    data.test = dict([param.split('=') for param in data.test[1:].split('&')])

    return data.test

@router.get("/map")
async def another_page():

    return FileResponse('trip.html')


@router.get("/login")
def get_login():
    return FileResponse('login.html')


@router.get("/profile")
def get_login():
    return FileResponse('profile.html')

@router.get("/register")
def get_register():
    return FileResponse('register.html')

@router.get("/review")
def get_review():
    return FileResponse('review.html')

@router.post("/register")
async def add_data(data: User_datas, response: Response):
    root = get_db()
    
    if 'users' not in root:
        root['users'] = BTree()
        transaction.commit()
   
    users = root['users']
    
   
    users[data.username] = User(data.username, data.password)
    transaction.commit()

    return RedirectResponse(url='/login', status_code=303)


@router.post("/login")
async def login(data: User_datas, response: Response,request: Request):
    global token_login 
    root = get_db()
    user = root['users'].get(data.username)
    if not user or user.password != data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = datetime.timedelta(minutes=30)
    access_token = jwt.encode(
        {"username": user.username, "exp": datetime.datetime.utcnow() + access_token_expires},
        SECRET_KEY, algorithm=ALGORITHM
    )
    
    return {"access_token": access_token,"user":get_current_user(access_token),"user_object":get_user(get_current_user(access_token))}

