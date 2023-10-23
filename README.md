# `Cipher Encryption`

    Encryption and Digital Signatures using Python

## `Asymmetric Key Encryption`

```python
>>> python Asymmetric.py

original string:  hello geeks
encrypted string:  b'\x84ll\xe9\x95\x1a...4\xe6O>\xd3\xff\xd9?&\xbf\xad(Z4w'
decrypted string:  hello geeks
```

------------

## `Symmetric Key Encryption`

```python
>>> python Symmetric.py

Original string :  hello geeks

Key :  b'r2K6w_U21JC1NjEpYIRPvkSGUBanjDI-vKJRYtYCgk0='

Encrypted string :  b'gAAAAABlNniRctNbR9B-XI_uwhQNP8JY__qWeBqBP0C7MWmq2BedHE_miM46z1kqy2mnhqPmNVK4g5uhLEDN_RUPgeUyk-9-cg=='

Decrypted string :  hello geeks
```

<br>

> The fernet.encrypt() function in Python generates a unique string every time because it uses a random IV (initialization vector) for each encryption operation. 

<br>

```python
>>> from cryptography.fernet import Fernet
>>> key = b'n59X6L2iEqgjYx4JHXXeQ_O9w7JDarlJMzIxRNPp80g='
>>> fernet = Fernet(key)

>>> en = b'gAAAAABlNm46j4ighABDBj9MlbCVTQkmnd7khz_V69JHQibhL8MKKDbjE2iJbGJF3ZnrQM20lMSFWilloy7jc7pzrUr5GEbjXQ=='
>>> fernet.decrypt(en).decode()
'hello geeks'

>>> en = b'gAAAAABlNm_oPf7FMEWokFN4Tnqgq-_nLBqlnNSSpz9bABbjYPULshPGIBG1ZmgAsgUsFBQdEjyFJvZJJwx_PTMGbZ-U66iuOA=='
>>> fernet.decrypt(en).decode()
'hello geeks'

>>> en = b'gAAAAABlNnFgqsSXUNH5MjLTMRe3Pyk3uClXugyEIAvEa2EjjOW3DZ_Itb8J1Sw-xSQ2ys_N3nhn17x_0zjzLRhYyUWZGq3Gfw=='
>>> fernet.decrypt(en).decode()
'hello geeks'
```

<br>

- The IV is a random value that is used to encrypt the data, and it is not reused for subsequent encryption operations. 

- This ensures that even if the same plaintext is encrypted multiple times, the resulting ciphertext will be different.

- The fernet.encrypt() function uses the Advanced Encryption Standard (AES) algorithm in CBC mode with PKCS7 padding. 

- AES is a symmetric encryption algorithm, which means that the same key is used to encrypt and decrypt the data. 

- This makes it ideal for situations where the key must be shared between two or more parties.

- The fernet.encrypt() function is a secure way to encrypt data in Python. 

- It is used by many popular Python libraries, such as Django and Flask.
