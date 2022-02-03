import pyrebase
from gps import gps 

config = {
    "apiKey": "AIzaSyDuetJQ9NvrHkfZD6JpHP-T60zycMpMoPc",
    "authDomain": "raspberry-67ba1.firebaseapp.com",
    "databaseURL": "https://raspberry-67ba1-default-rtdb.firebaseio.com",
    "projectId": "raspberry-67ba1",
    "storageBucket": "raspberry-67ba1.appspot.com",
    "messagingSenderId": "183370367782",
    "appId": "1:183370367782:web:e8c08b2290eea52bb0b7e7"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

gp = gps()
print(gp)
db.child().update({"varia":gp})
