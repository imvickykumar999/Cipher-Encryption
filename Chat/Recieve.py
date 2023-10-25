
# https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/Fernet/Message.json

# pip install cryptography
from cryptography.fernet import Fernet

key = input('\nEnter Key: ')
key = bytes(key, "utf-8")
fernet = Fernet(key)

def get(encMessage):
    decMessage = fernet.decrypt(encMessage)
    decoded = decMessage.decode()
    return str(decoded)

while True:
    line = input('\n>>> ')[2:-1]
    encrypted = bytes(line, "utf-8")

    decrypted = get(encrypted)
    print('\n', decrypted)
