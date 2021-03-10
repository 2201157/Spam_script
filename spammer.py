import pyautogui
import time

time.sleep(5)
file = open("file","r", encoding="utf8")

for linha in file:
    pyautogui.typewrite(linha)
    pyautogui.press("enter")
    time.sleep(0.1)

file.close()
