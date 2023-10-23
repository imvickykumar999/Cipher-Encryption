import rsa

publicKey, privateKey = rsa.newkeys(512)
message = "hello geeks"
encMessage = rsa.encrypt(message.encode(), publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()
print("decrypted string: ", decMessage)

'''
python Asymmetric.py
original string:  hello geeks
encrypted string:  b'\x84ll\xe9\x95\x1a\x81\x04\x1e\xee\xf3\xb7\xf4\xd8\xcf\x05?D\xa3\xd9n\xd3\xb7\xf5\x84[\x1c\x8c\xd2\x16\xfda\xf5|\x9c\xab\x99\xac\xc3\x06\x8fd\xffl<\x1c\x9a\xd6\x12\xf4\xe6O>\xd3\xff\xd9?&\xbf\xad(Z4w'
decrypted string:  hello geeks
'''
