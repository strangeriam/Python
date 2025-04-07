# 程式目的: 較可靠方法.
# 取得 Window 物件後, 就可以截取所有屬性.

left, right, top, bottom
topleft, topright, bottomleft, bottomright
midleft, midright, midleft, midright
width, height
size
area
center
centerx, centery
box 視窗方塊 (left, top, width, height)
title 視窗頂端標題文字


import pyautogui
>>> fw = pyautogui.getActiveWindow()
>>> fw
Win32Window(hWnd=531288)
>>>

>>> str(fw)
'<Win32Window left="-2532", top="-95", width="673", height="519", title="Python 3.11 (64-bit)">'
>>>
>>> fw.title
'Python 3.11 (64-bit)'
>>>
>>> fw.size
Size(width=878, height=539)
>>>
>>> fw.left, fw.top, fw.right, fw.bottom
(-2532, -95, -1654, 444)
>>>
>>> fw.area
473242
>>>
>>> pyautogui.click(fw.left + 10, fw.top + 20)
>>>

