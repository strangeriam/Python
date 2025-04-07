import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

