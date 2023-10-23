# `Cipher Encryption`

    Encryption and Digital Signatures using Python

## `Asymmetric Key Encryption`

```python
>>> python Asymmetric.py

PublicKey(7538027940834762299477012974681369470157088352079307534503734208990957157514995150109710544147686089899315399491723268770703983898021641639130349545463343, 65537) 
PrivateKey(7538027940834762299477012974681369470157088352079307534503734208990957157514995150109710544147686089899315399491723268770703983898021641639130349545463343, 65537, 1704932910676315387722168596727069283857035272332752118405615944884156398152540715416529946634956290096876648599758143936974562791927808996952099713217025, 5405229185937478753088862673417195807428878302634952893870388486916057243952904449, 1394580633222006956650843540030034504070210921256495543022793151541077807)

Original string:  hello geeks

Encrypted string:  b'\n\xd9y\xdcH\xefL\xe2\xd1\xa3=\x98\xf3\xb7\xf4>Pl\x11\xabeL@\xe2\xd1\x87\xeb\xb4\xc5\xa7R\xa7\xb8\x85\x8f\x18\x1e\xf0^\xddFPn\x97;k\xdd\xa2\x87\x92\xf9\xc2R\xd4=\xbc\nH\xac\xa5M\x9a\x0c\x88'

Decrypted string:  hello geeks
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
