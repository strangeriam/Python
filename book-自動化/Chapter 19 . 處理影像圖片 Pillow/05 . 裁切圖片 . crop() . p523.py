# 程式目的: 裁切一部分圖, 並存成另一新檔.

import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIM = Image.open('zophie.png')

croppedIm = catIM.crop((335, 345, 565, 560))
croppedIm.save('cropped.png')
