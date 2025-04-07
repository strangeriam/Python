

catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()

for left in range(0, catImWidth, faceImWidth):
  for top in range(0, catImHeight, faceImHeight):
    print(left, top)
    catCopyTwo.paste(faceIm, (left, top))
