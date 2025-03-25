import pyautogui
screenWidth = pyautogui.size()[0]
screenHeight = pyautogui.size()[1]
screenSize = screenWidth, 'x', screenHeight
print(screenSize)
