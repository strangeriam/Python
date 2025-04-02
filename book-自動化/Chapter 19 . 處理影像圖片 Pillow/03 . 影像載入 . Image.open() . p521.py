import os
# 切換圖檔所在工作目錄.
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

# 圖檔資訊:
# filename: sample.png
# size 642 x 232

>>> from PIL import Image
>>> catIm = Image.open('sample.png')

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

