
# pip install cryptography
from cryptography.fernet import Fernet
import os

'''
>>> adb devices
>>> adb tcpip 5555
>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
>>> adb connect <ip-address>:5555

# Remove USB.
>>> adb shell input text connected
>>> adb shell input keyevent 66
'''

key = Fernet.generate_key()
fernet = Fernet(key)

os.system(f'''adb shell input text {key.decode("utf-8")}''')
os.system("adb shell input keyevent 66")

def send(message):
    encoded = message.encode()
    encMessage = fernet.encrypt(encoded)
    return str(encMessage)

while True:
    text = input('\n>>> ')
    text = send(text)
    print('\n', text)

    for i in text:
        if   i == ' ': os.system("adb shell input keyevent 62")
        elif i == '*': os.system("adb shell input keyevent 17")
        elif i == ';': os.system("adb shell input keyevent 74")
        elif i == '(': os.system("adb shell input keyevent 71")
        elif i == ')': os.system("adb shell input keyevent 72")

        elif i in ('"', "'"): os.system("adb shell input keyevent 75")
        else: os.system(f'''adb shell input text {i}''')
    os.system("adb shell input keyevent 66")
