
# pip install cryptography
from cryptography.fernet import Fernet

key = bytes(input('\nEnetr Key: '), "utf-8")
fernet = Fernet(key)

def get(encMessage):
    decMessage = fernet.decrypt(encMessage)
    decoded = decMessage.decode()
    return str(decoded)

while True:
    line = input('\n>>> ')
    encrypted = bytes(line[2:-1], "utf-8")

    decrypted = get(encrypted)
    print('\n', decrypted)
