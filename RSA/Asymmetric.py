
# pip install rsa
import rsa

publicKey, privateKey = rsa.newkeys(512)
# print(publicKey, privateKey)

message = "hello geeks"
print("\nOriginal string: ", message)

encoded = message.encode()
encMessage = rsa.encrypt(encoded, publicKey)
print("\nEncrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey)
decoded = decMessage.decode()
print("\nDecrypted string: ", decoded)
