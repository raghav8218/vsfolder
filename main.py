import webbrowser
import time
import pyautogui


mastipur ='https://discord.com/channels/1201097362312003664/1201097362312003670'
webbrowser.open(mastipur)
time.sleep(15)

message="sabhi mastipur ke logo ko hello world"

pyautogui.write(message, interval=0.1)



