# 程式目的:
# 新增一個寬高是 (100, 200) 的紫色圖檔.
# 新增另一圖, 寬高是 (20, 20), 沒指定顏色, 所以此圖輸出成 透明的背景色.

from PIL import Image

im = Image.new('RGBA', (100, 200), 'purple')
image.save('purpleImage.png')

im2 = Image.new('RGBA', (20, 20))
im2.save('transparentImage.png')
