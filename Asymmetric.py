import rsa

# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(512)

# this is the string that we will be encrypting
message = "hello geeks"

# rsa.encrypt method is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption 
# with encode method
encMessage = rsa.encrypt(message.encode(), 
						publicKey)

print("original string: ", message)
print("encrypted string: ", encMessage)

# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption
decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)


'''
python Asymmetric.py
original string:  hello geeks
encrypted string:  b'\x84ll\xe9\x95\x1a\x81\x04\x1e\xee\xf3\xb7\xf4\xd8\xcf\x05?D\xa3\xd9n\xd3\xb7\xf5\x84[\x1c\x8c\xd2\x16\xfda\xf5|\x9c\xab\x99\xac\xc3\x06\x8fd\xffl<\x1c\x9a\xd6\x12\xf4\xe6O>\xd3\xff\xd9?&\xbf\xad(Z4w'
decrypted string:  hello geeks
'''
