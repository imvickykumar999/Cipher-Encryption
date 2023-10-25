
# pip install cryptography
from cryptography.fernet import Fernet

key = bytes(input('\nEnetr Key: '), "utf-8")
fernet = Fernet(key)

def get(encMessage):
    decMessage = fernet.decrypt(encMessage)
    decoded = decMessage.decode()
    return str(decoded)

while True:
    encrypted = bytes(input('\n>>> '), "utf-8")
    decrypted = get(encrypted)
    print('\n', decrypted)
