import pyautogui

>>> fw = pyautogui.getActiveWindow()

# 取得視窗寬度.
>>> fw.width
878

# 取得視窗位置.
>>> fw.topleft 
Point(x=-2532, y=-95)

# 調整視窗寬度.
>>> fw.width = 500

# 移動視窗到指定座標.
>>> fw.topleft = (800, 400)

# 視窗是否最大化
>>> fw.isMaximized
False

# 視窗是否最小化
>>> fw.isMinimized
False

# 視窗是否正在使用
>>> fw.isActive
True

# 最大化視窗
>>> fw.maximize()
>>> fw.isMaximized
True

# 重作先前的狀態, Lu-250407: 沒感覺.
>>> fw.restore()

# 最小化視窗
>>> fw.minimize()

import time
time.sleep(5); fw.activate()

# 關閉視窗
fw.close()



