
# https://stackoverflow.com/a/65598901/11493297
import rsa

publicKey, privateKey = rsa.newkeys(2048) 
# print(publicKey, privateKey)

publicKeyPkcs1PEM = publicKey.save_pkcs1().decode('utf8') 
# print(publicKeyPkcs1PEM)

privateKeyPkcs1PEM = privateKey.save_pkcs1().decode('utf8') 
# print(privateKeyPkcs1PEM)

with open('publicKeyPkcs1PEM.txt', 'w') as f: f.write(publicKeyPkcs1PEM)
with open('privateKeyPkcs1PEM.txt', 'w') as f: f.write(privateKeyPkcs1PEM)

publicKeyReloaded = rsa.PublicKey.load_pkcs1(publicKeyPkcs1PEM.encode('utf8')) 
privateKeyReloaded = rsa.PrivateKey.load_pkcs1(privateKeyPkcs1PEM.encode('utf8')) 

plaintext = "hello world"
print("\nPlaintext : ", plaintext)

encoded = plaintext.encode('utf8')
ciphertext = rsa.encrypt(encoded, publicKeyReloaded)
print("\nCiphertext: ", ciphertext)

decryptedMessage = rsa.decrypt(ciphertext, privateKeyReloaded)
decoded = decryptedMessage.decode()
print("\nDecrypted message: ", decoded)
