import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

>>> faceIm = catIm.crop((335, 345, 565, 560))
>>> faceIm.size
(230, 215)

catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')
