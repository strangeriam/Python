import os
os.chdir('D:\\BeeStation\\02_python\\250402_mouseMove4\\')

from PIL import Image
catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width / 2), int(height / 2))) # quartersize 四分之一大小
quartersizedIm.save('quartersized.png')
svelteIm = catIm.resize((width, height + 300)) # svelte 苗條
svelteIm.save('svelte.png')
