from ZODB import FileStorage, DB
import transaction
from persistent import Persistent
import random
import requests
from ZEO import ClientStorage
storage = ClientStorage.ClientStorage(('127.0.0.1', 8100))

db = DB(storage)
connection = db.open()
root = connection.root()
api_key = "AIzaSyCgqyG_lZyJ28gnl-5EKzQDUwF4gKeMFDQ"


def get_db():
    storage = ClientStorage.ClientStorage(('127.0.0.1', 8100))

    db = DB(storage)
    connection = db.open()
    root = connection.root()
    return root

def close_db():
    db.close()





class Attraction(Persistent):

    def __init__(self, name):
        self.name = name
        self.review = []
        self.detail = ""
    

    def add_detail(self):
        pass

    def add_review(self,review):
        self.review.append(review)
        self._p_changed = True


class Temple(Attraction):

    def __init__(self, name):
        super().__init__(name)
        

class Entertain(Attraction):

    def __init__(self, name):
        super().__init__(name)
        

class Museum(Attraction):

    def __init__(self, name):
       
     
        super().__init__(name)


class Restuarnt(Attraction):

    def __init__(self, name):
        super().__init__(name)


class Hotel(Attraction):

    def __init__(self, name):
        super().__init__(name)


class Nature(Attraction):
    
    def __init__(self, name):
        super().__init__(name)


class kid_friendly(Attraction):

    def __init__(self, name):
        super().__init__(name)

class Place(Attraction):
    def __init__(self, name):
        super().__init__(name)


class User(Persistent):

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.point = 0
        self.quests = []
        self.trips = []

    def get_point(self):
        return self.point
    
    def add_point(self,point):
        self.point+=point

    def add_trip(self,trip):
        self.trips.append(trip)
        self._p_changed = True
   
     


transaction.commit()
connection.close()
db.close()