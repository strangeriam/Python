# 目的: 在螢幕截圖上取得欲控制的 按鈕 圖的座標.

# 步驟: 擷取當前操作螢幕畫面 --> 帶入愈取得 按鈕 的截圖 --> 取得其 X Y 座標.
import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

# 將螢幕截圖存成檔 screen.png
import pyautogui
im = pyautogui.screenshot()
im.save('screen.png')

# 欲控制的 按鈕 圖檔. 輸出符合此 按鈕 左上角的座標 x, y. 以及其寬度和高度.
# 如沒符合, 則 locateOnScreen() 函式會返回 None.
b = pyautogui.locateOnScreen('submit.png')
b

# OUTPUT: Box(left=1706, top=256, width=91, height=106)

b[0]
# OUTPUT: 1706

b.left
# OUTPUT: 1706

# 如果此 '按鈕' 在螢幕上有多處比對都吻合, 則可用 locateAllOnScreen() 函式.
# 並使用 list() 返回這些都吻合的多組座標數值.
list(pyautogui.locateAllOnScreen('submit.png'))

# OUTPUT: (此輸出只有一組, 因為測試時, 還是只有一左相同)
[Box(left=1706, top=256, width=91, height=106)]
