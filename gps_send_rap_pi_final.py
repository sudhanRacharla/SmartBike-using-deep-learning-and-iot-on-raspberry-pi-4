import pyrebase
#import serial
#import pynmea2

firebaseConfig={
    "apiKey": "AIzaSyBeA82Bj2gv-D6hL_XjdjGIFwIvXjflBXc",
    "authDomain": "vehicle-gps-39c3b.firebaseapp.com",
    "databaseURL": "https://vehicle-gps-39c3b-default-rtdb.firebaseio.com",
    "projectId": "vehicle-gps-39c3b",
    "storageBucket": "vehicle-gps-39c3b.appspot.com",
    "messagingSenderId": "80477120597",
    "appId": "1:80477120597:web:0b0949f4d81aeb769eccdc"
    }

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

while True:
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data[0:6] == '$GPRMC':
                newmsg=pynmea2.parse(n_data)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
                print(gps)
                data = {"LAT": lat, "LNG": lng}
                db.update(data)
                print("Data sent")
