
# pip install cryptography
from cryptography.fernet import Fernet

from firebase_admin import credentials
from firebase_admin import db

import os
import pyperclip
import firebase_admin

path = './'
RSA = 'Fernet'
file = 'cred.json'
dir = os.path.join(path, file)

cred = credentials.Certificate(dir)
url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL' : url}

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, path)

key = Fernet.generate_key()
fernet = Fernet(key)

print('\nKey (copied) : ', key.decode())
pyperclip.copy(key.decode())

def send_mess(user, send):
    import datetime
    dt = datetime.datetime.now()

    d = str(dt).split()[0]
    t = str(dt).split()[1].split('.')[0]

    encoded = send.encode()
    encMessage = fernet.encrypt(encoded)

    child = f"{RSA}/Message/{d}/{t}/{user}"
    db.reference(child).set(str(encMessage))

user = input('\nEnter your Name: ')
print('\nWrite your message ...\n')

while True:
    send = input('\n>>> ')
    send_mess(user, send)
