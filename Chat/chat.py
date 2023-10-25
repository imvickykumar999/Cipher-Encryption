
from firebase_admin import db
from firebase_admin import credentials
import os

path = './'
RSA = 'Fernet'
file = 'cred.json'
dir = os.path.join(path, file)

cred = credentials.Certificate(dir)
url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL' : url}

import firebase_admin
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, path)

def send_mess(user, send):
    import datetime

    dt = datetime.datetime.now()
    # # Hosting Server Time Difference
    # dt += datetime.timedelta(
    #     days = 0, 
    #     hours = 0, 
    #     minutes = 0
    # )

    d = str(dt).split()[0]
    t = str(dt).split()[1].split('.')[0]

    child = f"{RSA}/Message/{d}/{t}/{user}"
    db.reference(child).set(send)

def get_mess():
    child = f"{RSA}/Message"
    ref = db.reference(child).get()
    return ref
