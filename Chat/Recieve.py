
# pip install cryptography
from cryptography.fernet import Fernet

def get(encMessage):
    decMessage = fernet.decrypt(encMessage)
    decoded = decMessage.decode()
    return decoded

key = input('\nEnetr Key: ') # decryption
fernet = Fernet(key)

while True:
    encrypted = input('>>> ')
    decrypted = get(encrypted)
    print('\n', decrypted)
