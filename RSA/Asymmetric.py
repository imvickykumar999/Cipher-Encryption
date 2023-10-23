
import rsa

publicKey, privateKey = rsa.newkeys(512)
# print(publicKey, privateKey)

message = "hello geeks"
print("\nOriginal string: ", message)

encMessage = rsa.encrypt(message.encode(), publicKey)
print("\nEncrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("\nDecrypted string: ", decMessage)
