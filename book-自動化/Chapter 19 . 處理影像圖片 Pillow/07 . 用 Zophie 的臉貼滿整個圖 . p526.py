
import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIm = Image.open('zophie.png')
catCopyIm = catIm.copy()

faceIm = catIm.crop((335, 345, 565, 560)) # crop 修剪
faceIm.size
# OUTPUT: (230, 215)

catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save('pasted.png')

# Page 526
# 將 catIm.size 存到 catImWidth 和 catImHeight
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()

for left in range(0, catImWidth, faceImWidth):
  for top in range(0, catImHeight, faceImHeight):
    print(left, top)
    catCopyTwo.paste(faceIm, (left, top))

catCopyTwo.save('tiled.png')

# OUTPUT:
0 0
0 215
0 430
0 645
0 860
0 1075
230 0
230 215
230 430
230 645
230 860
230 1075
460 0
460 215
460 430
460 645
460 860
460 1075
690 0
690 215
690 430
690 645
690 860
690 1075
[Finished in 284ms]
