# 注意:
# 當影像旋轉了 90 或 270 度時, 寬度和高度會產生變化.
# 如果旋轉成其他角度, 則會保持原始影像大小.

# 原因為:
# Windows 會用黑色的背影來填補旋轉所造成的空隙.
# macOS 會以透明像素填補空隙.

import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIm = Image.open('zophie.png')
catIm.rotate(90).save('rotated90.png') # rotate 旋轉
catIm.rotate(180).save('rotated180.png')
catIm.rotate(270).save('rotated270.png')
