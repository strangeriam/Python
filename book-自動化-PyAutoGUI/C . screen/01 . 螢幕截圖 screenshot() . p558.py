import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

import pyautogui
im = pyautogui.screenshot()
im.save('screen.png')
