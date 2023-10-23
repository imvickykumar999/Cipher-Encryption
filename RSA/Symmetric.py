
from cryptography.fernet import Fernet

message = "hello geeks"
print("\nOriginal string : ", message)

key = Fernet.generate_key()
# key = b'n59X6L2iEqgjYx4JHXXeQ_O9w7JDarlJMzIxRNPp80g='

# print('\nKey : ', key)
fernet = Fernet(key)

encoded = message.encode()
encMessage = fernet.encrypt(encoded)

print("\nEncrypted string : ", encMessage)
decMessage = fernet.decrypt(encMessage)

decoded = decMessage.decode()
print("\nDecrypted string : ", decoded)
