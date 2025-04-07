import pyautogui

>>> fw = pyautogui.getActiveWindow()
>>> fw.width # 取得視窗寬度.
878

>>> fw.topleft # 取得視窗位置.
Point(x=-2532, y=-95)
>>>

>>> fw.width = 500 # 調整視窗寬度.
>>> fw.topleft = (800, 400) # 移動視窗到指定座標.
