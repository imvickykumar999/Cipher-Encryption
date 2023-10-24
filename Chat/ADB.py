
'''
>>> adb devices
>>> adb tcpip 5555
>>> adb shell "ip addr show wlan0 | grep -e wlan0$ | cut -d\" \" -f 6 | cut -d/ -f 1"
>>> adb connect <ip-address>:5555
>>> adb shell input text connected
'''

import os
while True: # Ctrl+C to exit.
    text = input('>>> ')

    for i in text:
        if   i == ' ': os.system("adb shell input keyevent 62")
        elif i == '*': os.system("adb shell input keyevent 17")
        elif i == ';': os.system("adb shell input keyevent 74")
        elif i == '(': os.system("adb shell input keyevent 71")
        elif i == ')': os.system("adb shell input keyevent 72")

        elif i in ('"', "'"): os.system("adb shell input keyevent 75")
        else: os.system(f'''adb shell input text {i}''')
    input('... ')
    os.system("adb shell input keyevent 66")
