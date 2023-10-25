
# pip install cryptography
from cryptography.fernet import Fernet
import requests

key = input('\nEnter Key: ')
key = bytes(key, "utf-8")
fernet = Fernet(key)

def get(encMessage):
    decMessage = fernet.decrypt(encMessage)
    decoded = decMessage.decode()
    return str(decoded)

headers = {'Accept': 'application/json'}
URL = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/Fernet/Message.json'

r = requests.get(URL, headers=headers).json()
print()

for i in r:
    for j in r[i]:
        for k in r[i][j]:

            line = r[i][j][k][2:-1]
            e = bytes(line, "utf-8")

            try:
                l = get(e)

                print(f'''
                    
Date    : {i}
Time    : {j}
User    : {k}
Message : {l}

    ''')
            except:
                pass
