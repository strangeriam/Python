import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
  if not (filename.endswith('.png') or filename.endswith('.jpg')) \
  or filename == LOGO_FILENAME:
    continue
  im = Image.open(filename)
  width, height = im.size

Lu- 250407: 未完成, 有空再學...
