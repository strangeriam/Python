import os
# 切換圖檔所在工作目錄.
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

# 圖檔資訊:
# filename: zophie.png
# size 816 x 1088

>>> from PIL import Image
>>> catIm = Image.open('zophie.png')

>>> catIm.size
(642, 232)

>>> width, height = catIm.size
>>> width
642

>>> height
232

>>> catIm.filename
'sample.png'

>>> catIm.format
'PNG'

>>> catIm.format_description
'Portable network graphics'

