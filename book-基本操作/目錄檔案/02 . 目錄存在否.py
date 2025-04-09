# 事前準備: 在 D:\\BeeStation\\02_python\\250402_mouseMove4\\

from pathlib import Path
fname = Path('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt')

if fname.is_dir():
  print('directory exists')
else:
  print('no directory')
