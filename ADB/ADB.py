
'''
USB DEBUG:
---------
https://stackoverflow.com/a/35642973/11493297

Exception : ADB Shell commands:
------------------------------

adb shell input text '\'
\

adb shell input text '\"'
"

adb shell input text "\'"
'

OUTPUT:
------ 
https://youtube.com/shorts/Tri_bp0lRlQ
https://youtube.com/shorts/uHvtl3Ky0aw
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
