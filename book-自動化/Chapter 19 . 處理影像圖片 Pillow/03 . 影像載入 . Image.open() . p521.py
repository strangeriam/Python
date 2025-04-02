# 目的: 將1個 png檔 (zophie.png) 轉換格式成 jpg 檔 (zophie.jpg)

# 圖檔資訊:
# filename: zophie.png
# size 816 x 1088

# 注意: 其他圖檔會出現錯誤, 需釐清.

import os
# 切換圖檔所在工作目錄.
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

>>> from PIL import Image
>>> catIm = Image.open('zophie.png')

>>> catIm.size
(816, 1088)

>>> width, height = catIm.size
>>> width
816

>>> height
1088

>>> catIm.filename
'zophie.png'

>>> catIm.format
'PNG'

>>> catIm.format_description
'Portable network graphics'

>>> catIm.save('zophie.jpg')
>>>



