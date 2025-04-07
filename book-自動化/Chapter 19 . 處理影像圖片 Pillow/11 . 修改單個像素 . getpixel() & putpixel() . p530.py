# 程式流程

import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
im = Image.new('RGBA', (100, 100)) # --> 先取得一個 100 x 100 的透明正方形.
im.getpixel((0, 0)) # --> 對一些座標呼叫 getpixel() 會返回 0, 0, 0, 0

# OUTPUT: (0, 0, 0, 0)

for x in range(100): # --> 用 putpixel() 設定每個像素的色彩.
  for y in range(50):
    im.putpixel((x, y), (210, 210, 210)) # --> 灰色.

from PIL import ImageColor
for x in range(100):
  for y in range(50, 100):
    im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
im.getpixel((0, 0))

im.save('putPixel.png')
