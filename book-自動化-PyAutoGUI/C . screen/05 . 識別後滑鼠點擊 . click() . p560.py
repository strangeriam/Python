# 2 種方式點擊 按鈕.
# Way 1
pyautogui.click((1706, 256, 91, 106))
# OUTPUT: click normal ..  (2025, 4, 7, 14, 11, 58)

# Way 2
pyautogui.click('submit.png')
# OUTPUT: click normal ..  (2025, 4, 7, 14, 12, 54)

# 如果在螢幕上找不到符合的圖片時, locateOnScreen() 會引發例外異常.
# 所以最好要在 try 陳述句中呼叫.

try:
  location = pyautogui.locateOnScreen('submit.png')
except:
  print('Image could not be found')
