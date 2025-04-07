import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIm = Image.open('zophie.png')

# 轉置 transpose . 翻動 flip
catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png') # 左右水平翻轉
catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png') # 上下垂直翻轉
