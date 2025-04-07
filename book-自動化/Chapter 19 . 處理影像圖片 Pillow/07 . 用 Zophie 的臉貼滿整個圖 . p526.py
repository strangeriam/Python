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
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()

for left in range(0, catImWidth, faceImWidth):
  for top in range(0, catImHeight, faceImHeight):
    print(left, top)
    catCopyTwo.paste(faceIm, (left, top))
